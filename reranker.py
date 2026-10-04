"""Pinned ONNX cross-encoder; CPU only, no network in the query path."""
import hashlib,json,threading
from pathlib import Path
_CACHE={}
_LOCK=threading.Lock()

class LocalReranker:
    def __init__(self,directory):
        import onnxruntime as ort
        from tokenizers import Tokenizer
        self.directory=Path(directory)
        manifest=json.loads((self.directory/'manifest.json').read_text())
        for name,digest in manifest['sha256'].items():
            if hashlib.sha256((self.directory/name).read_bytes()).hexdigest()!=digest:
                raise ValueError('Reranker file integrity mismatch: '+name)
        self.model=manifest['repository']+'@'+manifest['revision']
        options=ort.SessionOptions();options.intra_op_num_threads=4;options.inter_op_num_threads=1
        self.session=ort.InferenceSession(str(self.directory/'model_quantized.onnx'),sess_options=options,providers=['CPUExecutionProvider'])
        self.tokenizer=Tokenizer.from_file(str(self.directory/'tokenizer.json'))
        self.tokenizer.enable_truncation(max_length=512)
        self.tokenizer.enable_padding(pad_id=0,pad_token='[PAD]')
        self.lock=threading.Lock()

    def rank(self,query,parts):
        import numpy as np
        scores=[]
        with self.lock:
            for start in range(0,len(parts),8):
                batch=parts[start:start+8]
                enc=self.tokenizer.encode_batch([(query,p['title']+'\n'+p.get('section_heading','')+'\n'+p['text']) for p in batch])
                values={'input_ids':np.array([e.ids for e in enc],dtype=np.int64),
                    'attention_mask':np.array([e.attention_mask for e in enc],dtype=np.int64),
                    'token_type_ids':np.array([e.type_ids for e in enc],dtype=np.int64)}
                scores.extend(self.session.run(None,{i.name:values[i.name] for i in self.session.get_inputs()})[0].reshape(-1).tolist())
        if len(scores)!=len(parts) or not all(np.isfinite(scores)):raise ValueError('Invalid reranker scores')
        return sorted([dict(p,rerank_score=round(float(score),5)) for p,score in zip(parts,scores)],key=lambda p:-p['rerank_score'])

def get_reranker(directory):
    key=str(Path(directory).resolve())
    with _LOCK:
        if key not in _CACHE:_CACHE[key]=LocalReranker(key)
        return _CACHE[key]
