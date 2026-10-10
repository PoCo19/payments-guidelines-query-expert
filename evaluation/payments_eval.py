"""Evaluate frozen mixed-source cases locally; captures are compatible with ragas_runner score."""
import argparse
import datetime as dt
import json
from pathlib import Path
import sys
import time
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app import Engine, read_json
from evaluation.ragas_runner import load_cases, sha, save, adapt, case_payload, export_review, CAVEAT, request, local_url
from tools.document_pipeline import input_hashes


def source_hits(case, response):
    return [any(s['document_id'] == a['document_id'] and s['page'] == a['page']
                and a['quote'] in ' '.join(s['text'].split()) for s in response.get('sources', []))
            for a in case['references']]


def validate_anchors(cases, engine):
    for c in cases:
        for a in c['references']:
            if not any(p['document_id'] == a['document_id'] and p['source_page'] == a['page']
                       and a['quote'] in ' '.join(p['text'].split()) for p in engine.pages):
                raise ValueError('Source anchor changed or unavailable: '+c['id']+' '+a['document_id'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=ROOT/'config.json')
    parser.add_argument('--dataset', type=Path, default=ROOT/'evaluation/payments_cases_v1.json')
    parser.add_argument('--mode', choices=['evidence','generate'], default='evidence')
    parser.add_argument('--ids', help='Comma-separated cases; default all 20')
    args = parser.parse_args()
    cases, fingerprint = load_cases(args.dataset)
    selected = set(args.ids.split(',')) if args.ids else {c['id'] for c in cases}
    if selected - {c['id'] for c in cases}: parser.error('Unknown case ID')
    cases = [c for c in cases if c['id'] in selected]
    config = read_json(args.config); engine = Engine(config=config)
    validate_anchors(cases, engine)
    out = ROOT/'evaluation/payments_runs'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    out.mkdir(parents=True, exist_ok=False)
    manifest = dict(schema_version=1, created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        dataset_sha256=fingerprint, config_sha256=sha(args.config.read_bytes()), configuration=config,
        application_stats=engine.stats(), case_ids=[c['id'] for c in cases], mode=args.mode,
        input_hashes=input_hashes(engine.data_dir),
        method='hybrid', rerank=True, caveat=CAVEAT, human_review='pending', rows=[], capture_status='running',
        code_hashes={n:sha((ROOT/n).read_bytes()) for n in ['app.py','research.py','claim_check.py','request_runtime.py','context.py','adaptive_context.py','evaluation/payments_eval.py','evaluation/ragas_runner.py']})
    try: manifest['installed_models'] = request(local_url(config['ollama_url'])+'/api/tags', timeout=10)
    except Exception as exc: manifest['model_metadata_error'] = str(exc)
    save(out/'capture.json',manifest)
    for c in cases:
        payload = case_payload(c, mode=args.mode)
        row = dict(id=c['id'],case=c,payload=payload); start=time.monotonic()
        try:
            response=engine.answer(payload)
            row.update(status='ok',raw_response=response,anchor_hits=source_hits(c,response))
            if args.mode=='generate':row['sample']=adapt(c,response)
        except Exception as exc:row.update(status='error',error=f'{type(exc).__name__}: {exc}')
        row['wall_seconds']=round(time.monotonic()-start,3)
        manifest['rows'].append(row);save(out/'capture.json',manifest)
        print(c['id'],row['status'],row.get('anchor_hits'),row['wall_seconds'],flush=True)
    rows=manifest['rows'];good=[r for r in rows if r['status']=='ok'];positive=[r for r in good if r['case']['references']];negative=[r for r in good if r['case'].get('expect_abstain')]
    manifest['summary']=dict(cases=len(rows),completed=len(good),errors=len(rows)-len(good),
        anchors_found=sum(sum(r['anchor_hits']) for r in positive),anchors_expected=sum(len(r['case']['references']) for r in rows),
        positive_cases_all_anchors=sum(all(r['anchor_hits']) for r in positive),positive_cases_expected=sum(bool(r['case']['references']) for r in rows),
        negative_cases_abstained=sum(bool(r['raw_response'].get('abstained')) for r in negative),negative_cases_expected=sum(bool(r['case'].get('expect_abstain')) for r in rows),
        latency_seconds=[r['wall_seconds'] for r in rows],answer_correctness='Not measured by anchor retrieval; human review pending')
    manifest['snapshot_unchanged']=(manifest['input_hashes']==input_hashes(engine.data_dir)
                                    and manifest['config_sha256']==sha(args.config.read_bytes())
                                    and manifest['dataset_sha256']==sha(args.dataset.read_bytes()))
    manifest['capture_status']='complete' if len(good)==len(rows) and manifest['snapshot_unchanged'] else 'completed_with_errors'
    save(out/'capture.json',manifest);export_review(out,manifest)
    (out/'summary.md').write_text('# Mixed-source evaluation\n\n'+CAVEAT+'\n\nMode: '+args.mode+'\n\n```json\n'+json.dumps(manifest['summary'],indent=2)+'\n```\n',encoding='utf8')
    print(out,flush=True)
    return int(len(good)!=len(rows))


if __name__=='__main__':raise SystemExit(main())
