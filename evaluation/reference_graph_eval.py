"""Paired candidate-reference-graph evaluation; the maintained pilot stays on in both arms."""
import argparse,datetime as dt,hashlib,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from reference_graph import ReferenceGraph
from evaluation.ragas_runner import load_cases,case_payload,save
from evaluation.payments_eval import validate_anchors,source_hits


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dataset',type=Path,default=ROOT/'evaluation/context_regression_20261017.json')
    ap.add_argument('--graph',type=Path,default=ROOT/'pilot/corpus_reference_graph_v4.json')
    ap.add_argument('--mode',choices=['evidence','generate'],default='evidence')
    ap.add_argument('--ids');a=ap.parse_args()
    cases,fp=load_cases(a.dataset)
    if a.ids:
        ids=set(a.ids.split(','));assert ids<={c['id'] for c in cases};cases=[c for c in cases if c['id'] in ids]
    config=read_json(ROOT/'config.json');e=Engine(config=config);assert e.vector_ready
    validate_anchors(cases,e);graph=ReferenceGraph(a.graph,e)
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    code={p.name:sha(p) for p in ROOT.glob('*.py')}
    out=ROOT/'evaluation/reference_graph_runs'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True)
    record=dict(status='running',mode=a.mode,configuration=config,code_hashes=code,dataset_sha256=fp,
        graph_sha256=sha(a.graph),corpus_fingerprint=graph.data['corpus_fingerprint'],runner_sha256=sha(Path(__file__)),rows=[],
        caveat='AI-assisted development evidence. Existing pilot graph on in both arms. Candidate expansion only differs. No independent correctness claim.')
    save(out/'capture.json',record)
    for i,c in enumerate(cases):
        for arm in (['baseline','candidate'] if i%2==0 else ['candidate','baseline']):
            e.reference_graph=graph if arm=='candidate' else None
            started=time.monotonic();row=dict(id=c['id'],case=c,arm=arm)
            try:
                response=e.answer(case_payload(c,mode=a.mode,method='hybrid',rerank=True))
                row.update(status='ok',response=response,anchor_hits=source_hits(c,response))
            except Exception as exc:row.update(status='error',error=f'{type(exc).__name__}: {exc}')
            row['seconds']=round(time.monotonic()-started,3);record['rows'].append(row);save(out/'capture.json',record)
        print(c['id'],[(r['arm'],r.get('anchor_hits')) for r in record['rows'][-2:]],flush=True)
    paired={arm:{r['id']:r for r in record['rows'] if r['arm']==arm and r['status']=='ok'} for arm in ['baseline','candidate']}
    gains=losses=0
    for key in paired['baseline'].keys() & paired['candidate'].keys():
        for b,c in zip(paired['baseline'][key]['anchor_hits'],paired['candidate'][key]['anchor_hits']):
            gains+=not b and c;losses+=b and not c
    record['summary']=dict(gained=gains,lost=losses,errors=sum(r['status']=='error' for r in record['rows']),
        arms={arm:dict(anchors=sum(sum(r['anchor_hits']) for r in rows.values()),
            expected=sum(len(r['anchor_hits']) for r in rows.values()),
            model_fallbacks=sum(bool(r['response'].get('model_failure')) for r in rows.values()),
            coverage_unavailable=sum(r['response'].get('coverage_check',{}).get('status')=='unavailable' for r in rows.values()))
            for arm,rows in paired.items()})
    record['snapshot_unchanged']=all(sha(ROOT/name)==h for name,h in code.items()) and config==read_json(ROOT/'config.json') and sha(a.dataset)==fp and sha(a.graph)==record['graph_sha256']
    record['status']='complete';save(out/'capture.json',record);print(record['summary'],out,flush=True)

if __name__=='__main__':main()
