"""Source-backed, AI-labelled claim challenge; independent review remains pending."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app import Engine,read_json
from claim_check import check_claims
from evaluation.ragas_runner import save,request,local_url


def main():
    source_path=ROOT/'evaluation/readiness_runs/20261018T050704935147Z/capture.json'
    rows={r['id']:r['response']['sources'] for r in read_json(source_path)['rows']}
    pre=next(s for s in rows['X-PAY-015'] if 'Pre-transaction notification is not required' in s['text'])
    post=next(s for s in rows['X-PAY-015'] if 'An issuer shall send a post-transaction notification' in s['text'])
    table=next(s for s in rows['X-LIMIT-03'] if '| 5 | Credit Card Bill Payments |' in s['text'])
    failure_path=ROOT/'evaluation/readiness_runs/20261018T063852267607Z/capture.json'
    failure=next(r['response'] for r in read_json(failure_path)['rows'] if r['id']=='G-LIMIT-04')
    collective=next(c for c in failure['claims'] if 'consistently' in c['text'])
    collective_sources=[s for s in failure['sources'] if s['citation'] in collective['sources']]
    specifications=[
        ('Pre-transaction notification is not required for FASTag auto-replenishment.',True,[pre]),
        ('An issuer shall send a post-transaction notification to the customer.',True,[post]),
        ('Post-transaction notification is not required for FASTag auto-replenishment.',False,[pre]),
        ('Post-transaction notification is not required for FASTag auto-replenishment.',False,[pre,post]),
        ('FASTag auto-replenishment is exempt from pre-transaction notification, while the issuer must send post-transaction notification.',True,[pre,post]),
        ('Pre-transaction notification is mandatory for every FASTag auto-replenishment.',False,[post]),
        ('Credit Card Bill Payments have an enhanced per-transaction limit of INR 5 lakh.',True,[table]),
        ('Credit Card Bill Payments have a cumulative limit of INR 6 lakh over 24 hours.',True,[table]),
        ('Credit Card Bill Payments have a cumulative limit of INR 10 lakh over 24 hours.',False,[table]),
        ('Tax payments have a cumulative limit of INR 10 lakh over 24 hours.',False,[table]),
        ('Capital Market has a cumulative limit of INR 10 lakh over 24 hours.',True,[table]),
        ('Capital Market has a per-transaction limit of INR 10 lakh.',False,[table]),
        ('Credit Card Bill Payments allow INR 5 lakh for a single payment while INR 6 lakh is cumulative over 24 hours.',True,[table]),
        ('Credit Card Bill Payments allow INR 6 lakh for a single payment while INR 5 lakh is cumulative over 24 hours.',False,[table]),
        (collective['text'],False,collective_sources),
        ('OC185A enhances the per-transaction limit to INR 5 lakh for verified merchants aligned to tax payments.',True,
         [s for s in collective_sources if s['citation']=='S3']),
    ]
    cases=[dict(id=f'CHECK-{i:02}',claim=dict(text=text,sources=[s['citation'] for s in sources]),
                sources=sources,expected_supported=expected,review_status='AI_assisted_requires_independent_review')
           for i,(text,expected,sources) in enumerate(specifications,1)]
    config=read_json(ROOT/'config.json');models=request(local_url(config['ollama_url'])+'/api/tags',timeout=10)
    engine=Engine(config=config)
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    code={str(p.relative_to(ROOT)):sha(p) for p in ROOT.glob('*.py')}
    out=ROOT/'evaluation/readiness_runs'/('checker-'+dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    out.mkdir(parents=True)
    record=dict(status='running',configuration=config,installed_models=models,code_hashes=code,source_capture_sha256=sha(source_path),
                failure_capture_sha256=sha(failure_path),runner_sha256=sha(Path(__file__)),
                cases=cases,rows=[],caveat='Sixteen development claims, including an observed false acceptance, with AI-assisted expected labels. Not independent accuracy or a full checker benchmark.')
    save(out/'capture.json',record)
    for c in cases:
        kept,flagged,checks=check_claims(engine,[c['claim']],c['sources'])
        record['rows'].append(dict(id=c['id'],accepted=bool(kept),expected_supported=c['expected_supported'],checks=checks,kept=kept,flagged=flagged))
        save(out/'capture.json',record);print(c['id'],bool(kept),'expected',c['expected_supported'],flush=True)
    record['summary']=dict(false_acceptances=sum(r['accepted'] and not r['expected_supported'] for r in record['rows']),
        valid_withheld=sum(not r['accepted'] and r['expected_supported'] for r in record['rows']),
        checker_unavailable=sum(bool(c.get('failure_reason')) for r in record['rows'] for c in r['checks']))
    record['snapshot_unchanged']=all(sha(ROOT/p)==h for p,h in code.items()) and config==read_json(ROOT/'config.json')
    record['status']='complete';save(out/'capture.json',record);print(record['summary'],out,flush=True)


if __name__=='__main__':main()
