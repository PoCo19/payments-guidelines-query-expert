"""Paired baseline/graph experiment on the same model, source snapshot and context budget."""
import argparse
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path
import statistics
import sys
import time
import os
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine, read_json
from graph_context import EvidenceGraph, normal
from tools.document_pipeline import input_hashes


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def save(path,data):
    # Preserve the last complete capture if Windows scanners briefly lock a file.
    temporary=path.with_suffix('.pending.json')
    text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    for attempt in range(4):
        try:
            temporary.write_text(text,encoding='utf-8');os.replace(temporary,path);return
        except OSError:
            if attempt==3:raise
            time.sleep(0.1*(attempt+1))


def control(case,response):
    kind=case.get('control')
    trace=response['retrieval_trace'];g=trace.get('graph_context',{})
    if kind=='clarification':return response['response_status']=='clarification_needed' and not response['sources']
    if kind=='empty':return not response['sources']
    if kind=='graph_inactive':return g.get('status','not_applicable')=='not_applicable'
    if kind=='cutoff':return all(s.get('issue_date') and s['issue_date']<=case['cutoff'] for s in response['sources'])
    if kind=='unchanged':return 'graph_context' not in trace
    return None


def review_answer(response):
    """Export actual visible claims, not only the UI's draft-status preface."""
    lines=[response.get('answer','')]
    for claim in response.get('claims',[]):
        citations=', '.join(claim.get('sources',[]))
        lines.append(claim.get('text','')+(' ['+citations+']' if citations else ''))
    return '\n\n'.join(line for line in lines if line)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--config',type=Path,default=ROOT/'config.json')
    ap.add_argument('--graph',type=Path,default=ROOT/'pilot/upi_128_226_graph_v1.json')
    ap.add_argument('--dataset',type=Path,default=ROOT/'evaluation/graph_pilot_cases_v1.json')
    ap.add_argument('--method',choices=['bm25','hybrid','vector'],default='hybrid')
    ap.add_argument('--rerank',action=argparse.BooleanOptionalAction,default=True)
    ap.add_argument('--mode',choices=['evidence','generate'],default='evidence')
    ap.add_argument('--ids',help='Comma-separated IDs; omitted means all cases')
    args=ap.parse_args()
    cases=read_json(args.dataset)['cases']
    if args.ids:
        ids=set(args.ids.split(','))
        if ids-{c['id'] for c in cases}:ap.error('Unknown case ID')
        cases=[c for c in cases if c['id'] in ids]
    config=read_json(args.config);config.pop('evidence_graph_path',None)
    # BM25 needs no vector database or model service. Both arms use this same setting.
    if args.method=='bm25':config['vector_backend']='json'
    engine=Engine(config=config);graph=EvidenceGraph(args.graph,engine)
    for c in cases:
        if any(n not in graph.nodes for n in c['required_anchor_ids']):raise ValueError('Unknown expected anchor')
    if args.method!='bm25' and not engine.vector_ready:raise ValueError('Vector index is unavailable; benchmark not started')
    out=ROOT/'evaluation/graph_runs'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True)
    code=['app.py','adaptive_context.py','context.py','graph_context.py','source_quality_gate.py','source_quality_flags.json','research.py','product_scope.py','query_understanding.py','query_policies.json','claim_check.py','evidence_spans.py','answer_format.py','request_runtime.py','evaluation/graph_pilot_eval.py']
    code.extend(['scope_guard.py','claim_repair.py','structured_evidence.py','contextual_retrieval.py'])
    report=dict(status='running',method=args.method,rerank=args.rerank,mode=args.mode,
        dataset_sha256=sha(args.dataset),graph_sha256=sha(args.graph),configuration=config,
        original_config_sha256=sha(args.config),source_hashes=input_hashes(engine.data_dir),
        corpus_fingerprint=engine.fingerprint,code_hashes={p:sha(ROOT/p) for p in code},
        caveat='AI-assisted development set; graph and expected anchors co-designed. Not held-out, not independent correctness evaluation.',
        answer_correctness='Pending source and independent human review',rows=[])
    if args.method!='bm25' or args.mode=='generate':
        from evaluation.ragas_runner import request,local_url
        try:report['installed_models']=request(local_url(config['ollama_url'])+'/api/tags',timeout=10)
        except Exception as exc:report['model_metadata_error']=str(exc)
    save(out/'capture.json',report)
    for i,c in enumerate(cases):
        pair=[]
        for arm in (['baseline','graph'] if i%2==0 else ['graph','baseline']):
            engine.evidence_graph=graph if arm=='graph' else None
            payload=dict(query=c['query'],mode=args.mode,method=args.method,rerank=args.rerank,
                         series=c.get('series','UPI'),scope=c.get('scope','related'),route=c.get('route','auto'))
            for field in ('cutoff','document_ids'):
                if field in c:payload[field]=c[field]
            row=dict(case_id=c['id'],arm=arm,payload=payload,required_anchor_ids=c['required_anchor_ids'])
            start=time.perf_counter()
            try:
                r=engine.answer(payload)
                hits={key:any(p['document_id']==graph.nodes[key]['document_id'] and p['page']==graph.nodes[key]['page'] and normal(graph.nodes[key]['quote']) in normal(p['text']) for p in r['sources']) for key in c['required_anchor_ids']}
                row.update(status='ok',response=r,anchor_hits=hits,control_pass=control(c,r))
                row['model_usable_anchor_hits']={key:any(p.get('generation_eligible') is not False and p['document_id']==graph.nodes[key]['document_id'] and p['page']==graph.nodes[key]['page'] and normal(graph.nodes[key]['quote']) in normal(p['text']) for p in r['sources']) for key in c['required_anchor_ids']}
                if c.get('expected_gap'):
                    row['gap_disclosed']=c['expected_gap'] in ' '.join(r.get('warnings',[]))
            except Exception as exc:row.update(status='error',error=f'{type(exc).__name__}: {exc}')
            row['seconds']=round(time.perf_counter()-start,3)
            report['rows'].append(row);pair.append(row);save(out/'capture.json',report)
            print(c['id'],arm,row['status'],row.get('anchor_hits'),row['seconds'],flush=True)
        if c.get('control')=='unchanged' and all(r['status']=='ok' for r in pair):
            same=[s['id'] for s in pair[0]['response']['sources']]==[s['id'] for s in pair[1]['response']['sources']]
            for r in pair:r['control_pass']=r['control_pass'] and same
    report['summary']={}
    for arm in ('baseline','graph'):
        rows=[r for r in report['rows'] if r['arm']==arm];ok=[r for r in rows if r['status']=='ok']
        positives=[r for r in ok if r['anchor_hits']]
        report['summary'][arm]=dict(cases=len(rows),errors=len(rows)-len(ok),
            anchors_found=sum(sum(r['anchor_hits'].values()) for r in positives),
            anchors_expected=sum(len(r['required_anchor_ids']) for r in rows),
            model_usable_anchors_found=sum(sum(r['model_usable_anchor_hits'].values()) for r in positives),
            all_anchor_cases=sum(all(r['anchor_hits'].values()) for r in positives),
            positive_cases=sum(bool(r['required_anchor_ids']) for r in rows),
            control_passed=sum(r.get('control_pass') is True for r in ok),
            control_cases=sum(bool(c.get('control')) for c in cases),
            model_fallbacks=sum(bool(r['response'].get('model_failure')) for r in ok),
            required_gaps_disclosed=sum(r.get('gap_disclosed') is True for r in ok),
            required_gap_cases=sum(bool(c.get('expected_gap')) for c in cases),
            median_seconds=round(statistics.median(r['seconds'] for r in rows),3),
            positive_median_seconds=round(statistics.median(r['seconds'] for r in positives),3) if positives else None,
            response_status_counts={s:sum(r['response']['response_status']==s for r in ok) for s in sorted({r['response']['response_status'] for r in ok})})
    report['snapshot_unchanged']=(sha(args.dataset)==report['dataset_sha256'] and sha(args.graph)==report['graph_sha256'] and sha(args.config)==report['original_config_sha256'] and input_hashes(engine.data_dir)==report['source_hashes'] and all(sha(ROOT/p)==h for p,h in report['code_hashes'].items()))
    report['status']='complete'
    report['benchmark_valid']=report['snapshot_unchanged'] and not report.get('model_metadata_error') and all(not s['errors'] and not s['model_fallbacks'] for s in report['summary'].values())
    save(out/'capture.json',report)
    (out/'summary.md').write_text('# Graph pilot comparison\n\n'+report['caveat']+'\n\nAnswer correctness remains unscored. Controls measure routing/filtering, not general negative-answer accuracy. Single-run latency includes cache/model warm-up.\n\n```json\n'+json.dumps(report['summary'],indent=2)+'\n```\n',encoding='utf-8')
    with (out/'human_review.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f);w.writerow(['case','arm','question','answer','stale_rule','incorrect_scope','unsupported_supersession','missing_condition','verdict','reviewer','notes'])
        for r in report['rows']:w.writerow([r['case_id'],r['arm'],r['payload']['query'],review_answer(r.get('response',{})),'','','','','','',''])
    print(out,flush=True)
    return int(not report['benchmark_valid'])


if __name__=='__main__':raise SystemExit(main())
