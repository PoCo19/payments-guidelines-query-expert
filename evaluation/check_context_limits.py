import json,time,urllib.request
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import Engine,read_json
old=read_json('evaluation/context_tuning_config_before.json')
new=dict(old,context_length=16384,max_output_tokens=3072,context_char_budget=18000)
report={'settings_before':old,'settings_after':new,'runs':[]}
query='According to OC 186A, give a detailed explanation of the UPI Tap & Pay requirements supported by the excerpts. Cover transaction scope, consent and opt-out, device security, and member responsibilities where evidence is available. Cite each point and identify any requested information not covered by the excerpts.'
for label,config,q in [('before',old,query),('after',new,query),('after_abstention',new,'Explain quantum photosynthesis and chlorophyll.')]:
 e=Engine(config=config);provider=e.ollama;metrics={}
 def measured(endpoint,payload):
  response=provider(endpoint,payload)
  if endpoint=='/api/generate':
   metrics.update(options=payload['options'],**{k:response.get(k) for k in ['prompt_eval_count','eval_count','done_reason','total_duration','load_duration']})
  return response
 e.ollama=measured
 result=e.answer(dict(query=q,method='hybrid',scope='related',mode='generate'))
 report['runs'].append(dict(label=label,query=q,metrics=metrics,**result))
 print(label,metrics,'claims',len(result['claims']),'words',sum(len(c['text'].split()) for c in result['claims']),flush=True)
 Path('evaluation/context_tuning_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
with urllib.request.build_opener(urllib.request.ProxyHandler({})).open('http://127.0.0.1:11434/api/ps') as r:report['loaded_models']=json.load(r)
Path('evaluation/context_tuning_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
