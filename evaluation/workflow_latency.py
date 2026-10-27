"""Serial, sampled-load workflow timing on development cases, not answer scoring."""
import datetime as dt,hashlib,json,math,subprocess,sys,threading,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from work_items import WorkStore
from model_transport import local_json
from evaluation.ragas_runner import save
from tools.document_pipeline import input_hashes

def main():
    e=Engine(config=read_json(ROOT/'config.json'))
    out=ROOT/'evaluation/workflow_latency_runs'/dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True)
    store=WorkStore(out/'timing.sqlite3')
    cases=[]
    for name in ('context_regression_20261017','reference_graph_rbi_cases_20261018','notification_paraphrases_20261019'):
        data=read_json(ROOT/'evaluation'/f'{name}.json');cases+=data if isinstance(data,list) else data['cases']
    byid={c['id']:c for c in cases}
    queries=[dict(kind='query',query=byid[k]['query']) for k in ('G-BIO-02','G-DD-03','G-IPO-02','PAY-013','RBI-REF-03')]
    def doc(number):
        found=[d for d in e.docs if str(d.get('circular_number','')).upper()==number and d.get('availability')=='converted' and (d.get('series')=='UPI' or 'UPI' in d.get('product_memberships',[]))]
        if len(found)!=1:raise ValueError(f'Expected one UPI source for {number}, found {len(found)}')
        return found[0]['id']
    pairs=[('226A','226'),('128A','128'),('185B','185A'),('127','71'),('141','76')]
    briefs=[dict(kind='impact',query=f'Compare the documented requirements and conditions in circulars {a} and {b}. Explain what differs, retaining each source attribution.',document_ids=[doc(a),doc(b)]) for a,b in pairs]
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    record=dict(status='running',configuration=e.config,code_hashes={p.name:sha(p) for p in ROOT.glob('*.py')},
        source_hashes=input_hashes(e.data_dir),graph_fingerprint=e.evidence_graph.fingerprint if e.evidence_graph else None,
        models=local_json(e.config['ollama_url']+'/api/tags',timeout=10),gpu_samples=[],rows=[],
        caveat='Development workload, five inputs per workflow repeated twice. Incomplete answers remain in timing denominators. First execution of each workflow is reported separately; only measured model load time establishes cold loading. Ten warm observations per workflow give a provisional p95, not a production SLA or independent answer score.')
    stop=threading.Event()
    def monitor():
        while not stop.is_set():
            try:
                p=subprocess.run(['nvidia-smi','--query-gpu=memory.used,utilization.gpu','--format=csv,noheader,nounits'],capture_output=True,text=True,timeout=3)
                record['gpu_samples'].append(dict(at=time.time(),reading=p.stdout.strip(),status=p.returncode))
            except (OSError,subprocess.TimeoutExpired):record['gpu_samples'].append(dict(at=time.time(),status='unavailable'))
            stop.wait(1)
    thread=threading.Thread(target=monitor,daemon=True);thread.start()
    schedule=[('first_execution',queries[0]),('first_execution',briefs[0])]
    for _ in range(2):
        for q,b in zip(queries,briefs):schedule.extend([('warm',q),('warm',b)])
    save(out/'capture.json',record)
    try:
        for number,(phase,payload) in enumerate(schedule,1):
            started=time.monotonic();row=dict(number=number,phase=phase,kind=payload['kind'],request=payload)
            try:
                item=store.create(payload,e);item=store.generate(item['id'],item['revision'],e)
                response=item['draft']['result'];row.update(item_id=item['id'],response=response,
                    status='model_failure' if response.get('model_failure') else 'completed')
            except Exception as exc:row.update(status='error',error=f'{type(exc).__name__}: {exc}')
            row['seconds']=round(time.monotonic()-started,3);record['rows'].append(row);save(out/'capture.json',record)
            print(number,phase,payload['kind'],row['status'],row.get('response',{}).get('response_status'),row['seconds'],flush=True)
            if sum(x['status']!='completed' for x in record['rows'])>=3:break
    finally:stop.set();thread.join()
    summary={}
    for kind,limit in [('query',45),('impact',90)]:
        rows=[r for r in record['rows'] if r['phase']=='warm' and r['kind']==kind]
        times=sorted(r['seconds'] for r in rows)
        p95=times[math.ceil(.95*len(times))-1] if times else None
        summary[kind]=dict(attempts=len(rows),failures=sum(r['status']!='completed' for r in rows),p95_seconds=p95,target_seconds=limit,
            target_met=len(rows)==10 and all(r['status']=='completed' for r in rows) and p95<=limit,
            incomplete=sum(r.get('response',{}).get('response_status')=='incomplete' for r in rows),
            coverage_unavailable=sum(r.get('response',{}).get('coverage_check',{}).get('status')=='unavailable' for r in rows))
    record.update(status='complete' if len(record['rows'])==len(schedule) else 'stopped_after_failures',summary=summary,
        snapshot_unchanged=all(sha(ROOT/k)==v for k,v in record['code_hashes'].items()) and input_hashes(e.data_dir)==record['source_hashes'])
    save(out/'capture.json',record);print(json.dumps(summary),out,flush=True)
    return int(not record['snapshot_unchanged'] or any(not s['target_met'] for s in summary.values()))

if __name__=='__main__':raise SystemExit(main())
