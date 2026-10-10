"""Compare installed local generators on one frozen application prompt.

Measures generation only, excluding retrieval and the second claim-check call.
Does not download models or change config.json. Saved drafts require human review.
"""
import argparse
import copy
import datetime as dt
import hashlib
import json
from pathlib import Path
import sys
import time
import urllib.request
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app import Engine, default_config_path, read_json


class CapturedRequest(Exception):
    pass


def get_local(base, endpoint):
    url = urlsplit(base)
    if url.scheme != 'http' or url.hostname not in ('127.0.0.1', 'localhost', '::1') or url.username or url.password:
        raise ValueError('Only local Ollama endpoints are supported.')
    with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(base+endpoint, timeout=15) as reply:
        return json.load(reply)


def freeze(engine, query):
    captured = {}
    original = engine.ollama
    def intercept(endpoint, payload):
        if endpoint == '/api/generate':
            captured.update(copy.deepcopy(payload))
            raise CapturedRequest()
        return original(endpoint, payload)
    engine.ollama = intercept
    try:
        engine.answer(dict(query=query, mode='generate', method='hybrid'))
    except CapturedRequest:
        return captured
    finally:
        engine.ollama = original
    raise ValueError('No generation request: the question was ambiguous or had no evidence.')


def run_one(base, payload, timeout):
    request = urllib.request.Request(base+'/api/generate', json.dumps(dict(payload, stream=True)).encode(),
                                     {'Content-Type': 'application/json'})
    start = time.perf_counter()
    first = None
    chunks = []
    final = {}
    with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(request, timeout=timeout) as reply:
        for raw in reply:
            row = json.loads(raw)
            if row.get('error'):
                raise ValueError(row['error'])
            if row.get('response'):
                if first is None:
                    first = time.perf_counter()-start
                chunks.append(row['response'])
            if row.get('done'):
                final = row
    seconds = time.perf_counter()-start
    if not final:
        raise ValueError('Generation stream ended before completion.')
    answer = ''.join(chunks)
    parsed = None
    try:
        parsed = json.loads(answer)
    except ValueError:
        pass
    sources = {s['citation'] for s in json.loads(payload['prompt'])['evidence']}
    claims = parsed.get('claims') if isinstance(parsed, dict) else None
    valid = (isinstance(parsed, dict) and isinstance(parsed.get('abstain'), bool) and isinstance(claims, list)
             and (parsed['abstain'] or bool(claims))
             and all(isinstance(c, dict) and isinstance(c.get('text'), str) and c['text'].strip()
                     and isinstance(c.get('sources'), list) and c['sources']
                     and all(isinstance(s, str) and s in sources for s in c['sources']) for c in claims))
    duration = final.get('eval_duration', 0)/1e9
    return dict(wall_seconds=round(seconds, 3), time_to_first_output_seconds=round(first, 3) if first is not None else None,
                load_seconds=final.get('load_duration', 0)/1e9, prompt_tokens=final.get('prompt_eval_count'),
                output_tokens=final.get('eval_count'), output_tokens_per_second=final.get('eval_count', 0)/duration if duration else None,
                done_reason=final.get('done_reason'), structure_and_citation_ids_valid=bool(valid),
                response=answer, parsed=parsed, ollama_timings={k:v for k,v in final.items() if k.endswith('_duration')})


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--models', nargs='+', required=True)
    p.add_argument('--query', default='What is UPI Circle and who are its primary and secondary users?')
    p.add_argument('--context', type=int, default=8192)
    p.add_argument('--output-tokens', type=int, default=1024)
    p.add_argument('--repeats', type=int, default=3)
    args = p.parse_args()
    if not 1 <= args.repeats <= 10 or not 4096 <= args.context <= 32768 or not 256 <= args.output_tokens < args.context:
        p.error('Use 1–10 repeats, 4096–32768 context tokens and an output limit below context length.')
    cfg = read_json(default_config_path())
    engine = Engine(config=cfg)
    base = cfg.get('ollama_url', 'http://127.0.0.1:11434').rstrip('/')
    tags = get_local(base, '/api/tags')['models']
    installed = {m['name']:m['digest'] for m in tags}
    missing = [m for m in args.models if m not in installed]
    if missing:
        p.error('Models must already be installed: '+', '.join(missing))
    payload = freeze(engine, args.query)
    payload['options'].update(num_ctx=args.context, num_predict=args.output_tokens)
    folder = ROOT / 'reports/model-benchmarks' / dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    folder.mkdir(parents=True)
    request_bytes = json.dumps(payload, ensure_ascii=False, indent=2).encode()
    (folder/'request.json').write_bytes(request_bytes)
    results = dict(created_at=dt.datetime.now(dt.timezone.utc).isoformat(), fingerprint=engine.fingerprint,
                   request_sha256=hashlib.sha256(request_bytes).hexdigest(), installed_model_digests=installed,
                   config=cfg, settings=vars(args),
                   scope='One frozen app prompt. Generation only; excludes retrieval and claim checking. First run may include loading. Not an accuracy benchmark.', runs=[])
    for model in args.models:
        for i in range(args.repeats):
            row = dict(model=model, repeat=i+1)
            try:
                row.update(run_one(base, dict(payload, model=model), cfg.get('model_timeout_seconds', 300)))
                row['residency_after'] = get_local(base, '/api/ps')
                row['digest_unchanged'] = installed[model] == next((m['digest'] for m in get_local(base, '/api/tags')['models'] if m['name']==model), None)
            except Exception as exc:
                row['error'] = str(exc)
            results['runs'].append(row)
            (folder/'results.json').write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding='utf-8')
            print(json.dumps({k:v for k,v in row.items() if k not in ('response','parsed','residency_after')}, ensure_ascii=False), flush=True)
    print('Saved:', folder)


if __name__ == '__main__':
    main()
