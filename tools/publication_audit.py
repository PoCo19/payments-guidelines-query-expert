"""Bounded publication hygiene check, not a comprehensive security audit."""
import json,re,subprocess,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def inspect():
 names=set(filter(None,subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT).decode().split('\0')))
 findings=[];large=[];total=0
 patterns=[rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',rb'\bgh[pousr]_[A-Za-z0-9]{30,}\b',
           rb'\bgithub_pat_[A-Za-z0-9_]{50,}\b',rb'\bAKIA[0-9A-Z]{16}\b',rb'\bsk-proj-[A-Za-z0-9_-]{40,}\b']
 binary={'.png','.jpg','.jpeg','.pdf','.pptx','.docx','.zip','.onnx'}
 for name in sorted(names):
  p=ROOT/name
  if not p.is_file():continue
  size=p.stat().st_size;total+=size
  if size>50_000_000:large.append(dict(path=name,bytes=size))
  if p.suffix in ('.sqlite3','.db','.pem','.key') or name in ('config.json','config.products.json') or name.startswith(('data/qa','inbox/','.venv/')):
   findings.append(dict(path=name,reason='Local-only or credential/database file'))
  if p.suffix not in binary:
   raw=p.read_bytes()
   for i,pattern in enumerate(patterns):
    if re.search(pattern,raw):findings.append(dict(path=name,reason='Credential pattern '+str(i)))
 return dict(candidate_files=len(names),total_bytes=total,files_over_50mb=large,findings=findings,
             limitation='Checks known credential patterns and local-file exclusions only; not a security certification.')

if __name__=='__main__':
 report=inspect();path=ROOT/'evaluation/release_20261027/publication-audit.json'
 path.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(report,indent=2));raise SystemExit(bool(report['findings'] or report['files_over_50mb']))
