"""Opt-in real-model validation of an existing-feature workspace and transaction rules."""
import json
import sys
import time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from launch_orchestrator.core import Store
from launch_orchestrator.demo import create_feature_demo
from launch_orchestrator.generation import Worker


def main():
    out=ROOT/'output/launch-v2';out.mkdir(parents=True,exist_ok=True)
    store=Store(out/('live-'+str(int(time.time()))+'.sqlite3'));w=create_feature_demo(store,'Automated V2 synthetic validation')
    config=json.loads((ROOT/'config.json').read_text(encoding='utf-8-sig'));results=[]
    def action(action,**kw):
        nonlocal w
        w=store.mutate(w['id'],{'actor':'Automated V2 synthetic validation','role':'product','revision':w['revision'],'action':action,**kw})
    for fact in list(w['facts']):action('fact_remove',id=fact['id'])
    worker=Worker(store,config)
    for kind,team in [('extract',None),('generate','cs'),('generate','marketing'),('generate','bd'),('generate','risk')]:
        if kind=='generate' and not w['facts_approved']:
            if w['questions']:action('questions_resolve',note='Synthetic contract test only; not a human domain approval. Questions are retained in the test report.')
            action('facts_approve',note='Automated synthetic test approval to exercise downstream workflows. Not a business sign-off.')
        store.enqueue(w['id'],{'actor':'Automated V2 synthetic validation','role':'product','revision':w['revision'],'kind':kind,'team':team,'mode':'ollama'})
        start=time.monotonic();worker.process_one();w=store.get(w['id']);j=w['jobs'][0]
        row={'kind':kind,'team':team,'state':j['state'],'seconds':round(time.monotonic()-start,2),'error':j['error'],'questions':w['questions'] if kind=='extract' else w['artifacts'].get(team,{}).get('open_questions',[])}
        results.append(row);print(json.dumps(row),flush=True)
        (out/'live-report.json').write_text(json.dumps({'model':config['generation_model'],'results':results,'workspace':w},ensure_ascii=False,indent=2),encoding='utf-8')
        if j['state']!='completed':return 1
    assert len(w['artifacts']['risk']['rule_assessments'])==len(w['risk_rules'])
    (out/'live-review.md').write_text(store.export(w['id']),encoding='utf-8')
    return 0


if __name__=='__main__':sys.exit(main())
