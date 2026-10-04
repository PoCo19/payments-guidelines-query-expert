"""Opt-in local Ollama smoke test. Uses isolated synthetic data, never live launch records."""
import json
import sys
import time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from launch_orchestrator.core import Store
from launch_orchestrator.demo import FACTS
from launch_orchestrator.generation import Worker


def main():
    output=ROOT/'output/launch-validation';output.mkdir(parents=True,exist_ok=True)
    store=Store(output/('live-'+str(int(time.time()))+'.sqlite3'))
    config=json.loads((ROOT/'config.json').read_text(encoding='utf-8-sig'))
    w=store.create({'actor':'Automated synthetic validation','role':'product','title':'Synthetic UPI feature validation','brief':'Fictional pilot for workflow testing. No real product claims.','simulated':True})
    def action(action,**kw):
        nonlocal w
        w=store.mutate(w['id'],{'actor':'Automated synthetic validation','role':'product','revision':w['revision'],'action':action,**kw})
    action('source_add',title='Synthetic brief',kind='simulated',scope='shared',text='\n\n'.join(v for _,v in FACTS))
    action('partner_save',name='Synthetic Bank A',capabilities='Pilot integration team',stage='testing',evidence='Simulated test plan')
    action('control_save',name='Synthetic enrollment review',scope='Pilot opt-in evidence',status='documented',owner='Test risk owner',evidence='Draft description, not testing evidence')
    worker=Worker(store,config);results=[]
    for kind,team in [('extract',None),('generate','cs'),('generate','marketing'),('generate','bd'),('generate','risk')]:
        if kind=='generate' and not w['facts_approved']:
            if w['questions']: action('questions_resolve',note='Automated smoke test only; open questions retained in report. Not a substantive human review.')
            action('facts_approve',note='Synthetic schema smoke test approval only; does not assess factual accuracy or real launch readiness.')
        store.enqueue(w['id'],{'actor':'Automated synthetic validation','role':'product','revision':w['revision'],'kind':kind,'team':team,'mode':'ollama'})
        started=time.monotonic();worker.process_one();w=store.get(w['id']);j=w['jobs'][0]
        result={'kind':kind,'team':team,'state':j['state'],'seconds':round(time.monotonic()-started,2),'error':j['error'],'open_questions':w['questions'] if kind=='extract' else w['artifacts'].get(team,{}).get('open_questions',[])}
        results.append(result);print(json.dumps(result),flush=True)
        (output/'live-report.json').write_text(json.dumps({'model':config['generation_model'],'results':results,'workspace':w},indent=2,ensure_ascii=False),encoding='utf-8')
        if j['state']!='completed':return 1
    (output/'live-launch-pack.md').write_text(store.export(w['id']),encoding='utf-8')
    return 0


if __name__=='__main__':sys.exit(main())
