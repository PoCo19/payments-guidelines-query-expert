"""Recovery/intake verification in an isolated staged application only."""
import hashlib,json,os,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from graph_context import graph_status
from work_items import WorkStore
from tools import document_pipeline as pipeline
from evaluation.ragas_runner import save

def main():
    if not (ROOT/'ENGINEERING_CANDIDATE.json').exists():raise ValueError('Run only inside an isolated engineering candidate')
    out=ROOT/'data/qa-checks';out.mkdir(exist_ok=True)
    config=read_json(ROOT/'config.json');before=(ROOT/'config.json').read_bytes();e=Engine(config=config)
    record=dict(status='running',checks={},scope='Isolated engineering recovery; not independent payments acceptance')
    report=ROOT/'evaluation/engineering_20261024/recovery.json';report.parent.mkdir(exist_ok=True)
    record['checks']['rebuilt_index']=pipeline.validate_engine(e)
    record['checks']['active_graph']=graph_status(e)
    offline=Engine(config=dict(config,ollama_url='http://127.0.0.1:1'))
    result=offline.answer(dict(query='UPI consent requirements',mode='generate',method='hybrid'))
    assert result['response_status']=='model_unavailable' and result['sources'] and not result['claims']
    record['checks']['model_outage']=dict(status=result['response_status'],evidence_count=len(result['sources']),claims=len(result['claims']))
    for query in ('zzqqvv mmkkrr', 'What is required under UPI OC999999X?', 'Tap & Pay limit?'):
        result=e.answer(dict(query=query,mode='generate',method='bm25'))
        assert result['response_status'] in ('abstained','clarification_needed') and not result['claims']
        record['checks'][query]=result['response_status']
    graph=read_json(ROOT/config['evidence_graph_path']);graph['nodes'][0]['page_sha256']='invalid-source-snapshot'
    pipeline.write(out/'stale-graph.json',graph)
    stale=Engine(config=dict(config,evidence_graph_path=str(out/'stale-graph.json')))
    assert graph_status(stale)['status']=='degraded'
    assert stale.answer(dict(query='UPI consent requirements',mode='evidence',method='bm25'))['sources']
    record['checks']['stale_graph']=graph_status(stale)
    # Abruptly terminate a child after its persisted generation-start event.
    code="""import os
from pathlib import Path
from app import Engine,read_json
from work_items import WorkStore
e=Engine(config=read_json(Path('config.json')))
s=WorkStore(Path('data/qa-checks/interrupted.sqlite3'))
i=s.create(dict(query='UPI consent requirements'),e)
Path('data/qa-checks/interrupted-id.txt').write_text(i['id'])
e.answer=lambda payload:os._exit(7)
s.generate(i['id'],i['revision'],e)
"""
    child=subprocess.run([sys.executable,'-X','utf8','-c',code],cwd=ROOT,timeout=40)
    assert child.returncode==7
    restored=WorkStore(out/'interrupted.sqlite3').get((out/'interrupted-id.txt').read_text(),e)
    assert not restored['busy'] and restored['version']==1 and restored['history'][-1]['action']=='interrupted'
    record['checks']['interrupted_work']=dict(busy=restored['busy'],version=restored['version'],event=restored['history'][-1]['action'])
    save(report,record)
    # A clearly synthetic local upload exercises prepare, incremental embedding,
    # validation, activation and rollback without touching the user's corpus.
    (out/'fixture.md').write_text('# Synthetic QA intake fixture\n'+('This fictional test document exercises local import, source ownership, retrieval, model embedding and rollback. It states no real payment requirement. '*5),encoding='utf-8')
    item=dict(id='qa:synthetic:intake:20261024',file='fixture.md',title='Synthetic QA intake fixture',issuer='QA fixture',document_type='Test fixture',reference='QA-20261024',products=['Payments'],source_url='https://example.org/qa-fixture',retrieved_on='2026-10-24')
    pipeline.write(out/'intake.json',dict(schema_version=1,documents=[item]))
    name='qa24-isolated-intake'
    pipeline.prepare(out/'intake.json',name,ROOT/'config.json')
    built=pipeline.build(name);active=pipeline.activate(name)
    new=Engine(config=read_json(ROOT/'config.json'))
    assert new.search('Synthetic QA intake fixture',method='bm25',document_ids={item['id']})
    rollback=pipeline.rollback(name)
    assert (ROOT/'config.json').read_bytes()==before
    record['checks']['intake_activation_rollback']=dict(build=built,activation=active,rollback=rollback,original_config_restored=True)
    record.update(status='passed',corpus_unchanged=e.fingerprint==Engine(config=read_json(ROOT/'config.json')).fingerprint)
    save(report,record);print(report)

if __name__=='__main__':main()
