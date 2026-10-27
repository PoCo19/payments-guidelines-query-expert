"""Compare keyword candidate order across Python hash seeds on frozen queries."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--worker',action='store_true')
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    if args.worker:
        from app import Engine,read_json
        engine=Engine(config=dict(read_json(ROOT/'config.json'),vector_backend='json'))
        cases=read_json(ROOT/'evaluation/expanded_evidence_cases_20261017.json')
        result={c['id']:[p['id'] for p in engine.search(c['query'],'bm25',series=c.get('series',''),k=64,candidate_mode=True)] for c in cases}
        print(json.dumps(result));return
    assert args.output
    runs={}
    for seed in ('1','2','3'):
        child=subprocess.run([sys.executable,'-X','utf8',str(Path(__file__).resolve()),'--worker'],cwd=ROOT,
            env=dict(os.environ,PYTHONHASHSEED=seed),capture_output=True,text=True,encoding='utf-8',check=True)
        runs[seed]=json.loads(child.stdout)
    changed=[key for key in runs['1'] if any(runs[seed][key]!=runs['1'][key] for seed in ('2','3'))]
    result=dict(mode='BM25 candidate-only; no model calls',cases=len(runs['1']),hash_seeds=list(runs),changed_cases=changed,
                code_sha256=hashlib.sha256((ROOT/'app.py').read_bytes()).hexdigest(),runs=runs)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='runs'},indent=2))


if __name__=='__main__':main()
