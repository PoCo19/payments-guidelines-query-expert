"""Download pinned, hash-verified local reranker assets. Explicit setup only."""
import hashlib,json,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parent;folder=ROOT/'models/reranker'
manifest=json.loads((folder/'manifest.json').read_text())
for name,checksum in manifest['sha256'].items():
 target=folder/name
 if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest()==checksum:
  print(name,'verified');continue
 remote='onnx/'+name if name.endswith('.onnx') else name
 url=f"https://huggingface.co/{manifest['repository']}/resolve/{manifest['revision']}/{remote}"
 temp=target.with_suffix(target.suffix+'.download')
 with urllib.request.urlopen(url,timeout=180) as response:blob=response.read()
 if hashlib.sha256(blob).hexdigest()!=checksum:raise ValueError('Download hash mismatch: '+name)
 temp.write_bytes(blob);temp.replace(target);print(name,'downloaded and verified')
