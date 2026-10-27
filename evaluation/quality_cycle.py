"""Paired evidence recovery / frozen-answer coverage review, plus live answers.

Development diagnostics only. No independent answer-accuracy score is computed.
"""
import argparse,datetime as dt,hashlib,json,statistics,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from evaluation.ragas_runner import load_cases,case_payload,save,request,local_url
from evaluation.payments_eval import validate_anchors,source_hits
from tools.document_pipeline import input_hashes
import evidence_focus,research

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',choices=['retrieval','coverage','generate'],required=True)
    ap.add_argument('--ids');ap.add_argument('--dataset',action='append',type=Path)
    ap.add_argument('--coverage-cases',type=Path)
    a=ap.parse_args();config=read_json(ROOT/'config.json')
    models=request(local_url(config['ollama_url'])+'/api/tags',timeout=10)
    e=Engine(config=config);assert e.vector_ready
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    code={p.name:sha(p) for p in ROOT.glob('*.py')}
    paths=a.dataset or [ROOT/'evaluation/context_regression_20261017.json',ROOT/'evaluation/reference_graph_rbi_cases_20261018.json']
    cases=[];datasets={}
    for path in paths:
        loaded,fp=load_cases(path);cases.extend(loaded);datasets[str(path)]=fp
    assert len({c['id'] for c in cases})==len(cases)
    if a.ids:
        ids=set(a.ids.split(','));assert ids<={c['id'] for c in cases}
        cases=[c for c in cases if c['id'] in ids]
    validate_anchors(cases,e)
    out=ROOT/'evaluation/quality_runs'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True)
    record=dict(status='running',mode=a.mode,configuration=config,installed_models=models,code_hashes=code,
        dataset_hashes=datasets,runner_sha256=sha(Path(__file__)),source_hashes=input_hashes(e.data_dir),rows=[],
        caveat='AI-assisted development cases. Anchor matches are not answer accuracy. Coverage findings require review. Both arms use the same models and corpus; the broader graph is off.')
    original=evidence_focus.phase_matches
    prior_path=ROOT/'evaluation/quality_review_20261019/before/research.py'
    prior={};exec(compile(prior_path.read_text(encoding='utf-8'),str(prior_path),'exec'),prior)
    if a.mode=='coverage':
        capture=ROOT/'evaluation/readiness_runs/20261018T154442787264Z/capture.json'
        cases=read_json(capture)['rows'];record['frozen_capture_sha256']=sha(capture)
        record['baseline_reviewer_sha256']=sha(prior_path)
        if a.coverage_cases:
            cases=read_json(a.coverage_cases);record['coverage_cases_sha256']=sha(a.coverage_cases)
        record['candidate_reviewer_sha256']=sha(ROOT/'evaluation/coverage_candidate.py')
        record['candidate_second_reading_sha256']=sha(ROOT/'evaluation/coverage_review_candidate.py')
    save(out/'capture.json',record)
    try:
        for i,c in enumerate(cases):
            arms=['current'] if a.mode=='generate' else (['baseline','candidate'] if i%2==0 else ['candidate','baseline'])
            for arm in arms:
                row=dict(id=c['id'],arm=arm);start=time.monotonic()
                if 'expected_material_warning' in c:row['expected_material_warning']=c['expected_material_warning']
                try:
                    if a.mode=='coverage':
                        from evaluation.coverage_candidate import check_answer_coverage as candidate_coverage
                        source=c['response'];fn=prior['check_answer_coverage'] if arm=='baseline' else candidate_coverage
                        result=fn(e,source['claims'],source['sources'],source['retrieval_trace']['query_plan'])
                        row.update(status='ok',coverage_check=result)
                    else:
                        evidence_focus.phase_matches=(lambda *args,**kwargs:[]) if arm=='baseline' else original
                        result=e.answer(case_payload(c,mode='generate' if a.mode=='generate' else 'evidence',method='hybrid',rerank=True))
                        row.update(status='ok',case=c,response=result,anchor_hits=source_hits(c,result))
                except Exception as exc:row.update(status='error',error=f'{type(exc).__name__}: {exc}')
                row['seconds']=round(time.monotonic()-start,3);record['rows'].append(row);save(out/'capture.json',record)
                print(row['id'],arm,row['status'],row.get('anchor_hits',row.get('coverage_check',{}).get('status')),row['seconds'],flush=True)
    finally:evidence_focus.phase_matches=original
    arms=sorted({r['arm'] for r in record['rows']});summary={}
    for arm in arms:
        rows=[r for r in record['rows'] if r['arm']==arm];ok=[r for r in rows if r['status']=='ok']
        times=sorted(r['seconds'] for r in ok)
        summary[arm]=dict(cases=len(rows),errors=len(rows)-len(ok),anchors_found=sum(sum(r.get('anchor_hits',[])) for r in ok),
            anchors_expected=sum(len(r.get('case',{}).get('references',[])) for r in rows),
            negative_cases=[dict(id=r['id'],status=r['response'].get('response_status'),sources=len(r['response']['sources'])) for r in ok if 'case' in r and not r['case']['references']],
            fallbacks=sum(bool(r.get('response',{}).get('model_failure')) for r in ok),
            median_seconds=statistics.median(times) if times else None,p95_seconds=times[min(len(times)-1,int(.95*len(times)))] if times else None)
    if a.mode=='retrieval':
        paired={arm:{r['id']:r for r in record['rows'] if r['arm']==arm and r['status']=='ok'} for arm in arms}
        changes=[]
        for key in paired['baseline'].keys() & paired['candidate'].keys():
            b,c=paired['baseline'][key],paired['candidate'][key]
            if b['anchor_hits']!=c['anchor_hits']:changes.append(dict(id=key,before=b['anchor_hits'],after=c['anchor_hits']))
        record['anchor_changes']=sorted(changes,key=lambda x:x['id'])
    record['summary']=summary
    record['snapshot_unchanged']=(all(sha(ROOT/n)==h for n,h in code.items()) and config==read_json(ROOT/'config.json')
        and all(sha(Path(p))==h for p,h in datasets.items()) and input_hashes(e.data_dir)==record['source_hashes'])
    record['status']='complete';save(out/'capture.json',record);print(summary,out,flush=True)
    return int(not record['snapshot_unchanged'] or any(s['errors'] or s['fallbacks'] for s in summary.values()))

if __name__=='__main__':raise SystemExit(main())
