"""Same-snapshot mid-sem checks. These are provisional developer experiments."""
import argparse, datetime, hashlib, json, statistics, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VARIANTS = [('bm25', False), ('vector', False), ('hybrid', False), ('hybrid', True)]

def request(base, route, payload=None):
    body = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(base + route, data=body, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=650) as response:
        return json.load(response)

def summarize(rows):
    ok = [r for r in rows if 'error' not in r]
    hits = [h for r in ok for h in r['anchor_hits']]
    expected = sum(r['anchor_count'] for r in rows)
    negative = [r for r in rows if r['anchor_count'] == 0]
    return dict(cases=len(rows), failures=len(rows)-len(ok), anchors_found=sum(hits), anchors_expected=expected,
                anchor_recall=sum(hits)/expected if expected else None,
                negative_cases=len(negative), negative_empty=sum(r.get('empty', False) for r in negative),
                median_ms=round(statistics.median(r['elapsed_ms'] for r in ok), 1) if ok else None)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--base', default='http://127.0.0.1:8765')
    parser.add_argument('--live', action='store_true', help='Also run six actual generation requests')
    args=parser.parse_args()
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    out=ROOT/'output'/'midsem'/'evidence'/stamp
    out.mkdir(parents=True, exist_ok=False)
    def save(name, value): (out/name).write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding='utf-8')
    raw=(ROOT/'evaluation/rag_cases.json').read_bytes()
    checksum=hashlib.sha256(raw).hexdigest()
    if checksum != (ROOT/'evaluation/rag_cases.sha256').read_text().strip():
        raise ValueError('Frozen case set changed; create a new version rather than overwriting it.')
    cases=json.loads(raw)
    stats=request(args.base, '/api/stats')
    if not stats['vector_ready']: raise RuntimeError('Vector store is not ready')
    config=json.loads((ROOT/'config.json').read_text())
    tags=request(config['ollama_url'], '/api/tags')
    report=dict(created_utc=stamp, dataset_sha256=checksum, config_sha256=hashlib.sha256((ROOT/'config.json').read_bytes()).hexdigest(),
                configuration=config, stats=stats, models=tags, runs={},
                caveat='AI-assisted 50-case UPI set awaiting independent review. Anchor recall is evidence coverage, not answer accuracy. Negative empty evidence is not generated abstention. One interleaved pass after warm-up; timings are preliminary, not a capacity benchmark.')
    save('manifest.json', report)
    # Warm all retrieval paths; keep warm-up separate from measurement.
    for method, rerank in VARIANTS:
        request(args.base, '/api/answer', dict(query=cases[0]['query'],series='UPI',method=method,rerank=rerank,mode='evidence',scope='strict'))
        report['runs'][method+('_reranked' if rerank else '')]={'rows':[]}
    # Rotate order by case to reduce systematic order/cache advantage.
    for i, case in enumerate(cases):
        variants=VARIANTS[i%4:]+VARIANTS[:i%4]
        for method, rerank in variants:
            row=dict(id=case['id'], query=case['query'], split=case['split'], anchor_count=len(case['references']))
            payload=dict(query=case['query'],method=method,rerank=rerank,mode='evidence',series=case.get('series') or 'UPI',scope=case['scope'],cutoff=case.get('cutoff',''))
            try:
                answer=request(args.base,'/api/answer',payload)
                hits=[any(s['document_id']==a['document_id'] and s['page']==a['page'] and a['quote'] in ' '.join(s['text'].split()) for s in answer['sources']) for a in case['references']]
                row.update(anchor_hits=hits,empty=not answer['sources'],elapsed_ms=answer['elapsed_ms'],route=answer['retrieval_trace']['route'],source_ids=[s['id'] for s in answer['sources']],trace=answer['retrieval_trace'])
            except Exception as exc: row['error']=str(exc)
            report['runs'][method+('_reranked' if rerank else '')]['rows'].append(row)
        if (i+1)%10==0: print(f'{i+1}/{len(cases)} cases completed',flush=True)
        save('retrieval.json',report)
    for run in report['runs'].values():
        run['summary']=summarize(run['rows'])
        run['by_route']={route:summarize([r for r in run['rows'] if r.get('route')==route]) for route in ['clause','summary','compare']}
    after=request(args.base,'/api/stats')
    report['snapshot_unchanged']=all(after[k]==stats[k] for k in ['fingerprint','registry_fingerprint','chunks'])
    save('retrieval.json',report)
    lines=['# Preliminary retrieval comparison', '', report['caveat'], '', '| Variant | Expected anchors found | Negative cases with no evidence | Median ms | Errors |','|---|---:|---:|---:|---:|']
    for name,run in report['runs'].items():
        s=run['summary'];lines.append(f"| {name} | {s['anchors_found']}/{s['anchors_expected']} | {s['negative_empty']}/{s['negative_cases']} | {s['median_ms']} | {s['failures']} |")
    lines += ['', 'Summary/comparison routes bypass reranking. Per-route results are in retrieval.json. Only hybrid versus hybrid_reranked isolates the reranking toggle.', '', 'Human answer correctness and source review remain pending.']
    (out/'SUMMARY.md').write_text('\n'.join(lines),encoding='utf-8')
    if args.live:
        scenarios=[
            ('direct','Under UPI OC 186A, who checks enablement before each transaction? Answer briefly.', 'strict'),
            ('related','Under OC 186A, explain consent and opt-out for UPI Tap and Pay. Attribute any related circular evidence separately.', 'related'),
            ('summary','Summarise UPI OC 186A in a short overview and key requirements.', 'strict'),
            ('comparison','Compare UPI OC 186 and OC 186A. Attribute differences to each circular and do not assume supersession.', 'strict'),
            ('ambiguity','What does OC 13 require?', 'strict'),
            ('unavailable','What does UPI OC 999 require?', 'strict')]
        live=[]
        for name,query,scope in scenarios:
            payload=dict(query=query,series='' if name=='ambiguity' else 'UPI',scope=scope,method='hybrid',rerank=True,mode='generate')
            row=dict(scenario=name,payload=payload,human_review='pending')
            start=time.perf_counter()
            try: row['response']=request(args.base,'/api/answer',payload)
            except Exception as exc: row['error']=str(exc)
            row['wall_seconds']=round(time.perf_counter()-start,2)
            live.append(row);save('live.json',live)
            print(name,row['wall_seconds'],'error' if 'error' in row else 'completed',flush=True)
    (ROOT/'output/midsem/evidence/LATEST.txt').write_text(stamp,encoding='utf-8')
    print(out,flush=True)
    if not report['snapshot_unchanged'] or any(run['summary']['failures'] for run in report['runs'].values()):sys.exit(1)

if __name__=='__main__':main()
