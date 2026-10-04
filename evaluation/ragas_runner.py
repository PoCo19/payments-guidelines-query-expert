"""Capture actual app answers, then score immutable records with local RAGAS."""
import argparse
import asyncio
import csv
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import statistics
import subprocess
import time
import urllib.request
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PILOT = ['RAG-001', 'RAG-006', 'RAG-008', 'RAG-017', 'RAG-024', 'RAG-028',
         'RAG-030', 'RAG-032', 'RAG-033', 'RAG-039', 'RAG-045', 'RAG-048']
METRICS = ('faithfulness', 'factual_correctness', 'context_recall', 'context_precision', 'citation_support')
CAVEAT = ('Provisional automated evaluation. AI-assisted references await independent review. '
          'Scores are not overall answer accuracy. Same-model judging can share generation errors.')


def sha(value):
    return hashlib.sha256(value).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def save(path, data):
    path = Path(path)
    pending = path.with_suffix(path.suffix + '.pending')
    pending.write_text(json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False), encoding='utf-8')
    pending.replace(path)


def local_url(url):
    parsed = urlparse(url)
    if parsed.scheme != 'http' or parsed.hostname not in ('localhost', '127.0.0.1', '::1') or parsed.username or parsed.password:
        raise ValueError('This runner accepts only local HTTP endpoints; remote judging is not configured.')
    return url.rstrip('/')


def request(url, payload=None, timeout=900):
    body = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.load(response)


def displayed_answer(response):
    """Use displayed blocks in reading order, never the success banner as an answer."""
    blocks = response.get('answer_blocks') or []
    claims = [claim for block in blocks for claim in block.get('claims', [])]
    if not claims:
        claims = response.get('claims') or []
    if claims:
        return '\n'.join(c['text'] for c in claims), claims
    if response.get('abstained') or response.get('retrieval_trace', {}).get('ambiguities'):
        return response.get('answer', ''), []
    raise ValueError('No displayed answer claims; refusing to score an application status banner.')


def adapt(case, response):
    if response.get('mode') != 'generate':
        raise ValueError('RAGAS answer evaluation requires mode=generate.')
    text, claims = displayed_answer(response)
    sources = response.get('sources', [])
    source_map = {s['citation']: s for s in sources}
    invalid = [sid for c in claims for sid in c.get('sources', []) if sid not in source_map]
    uncited = sum(not c.get('sources') for c in claims)
    hits = [any(s['document_id'] == a['document_id'] and s['page'] == a['page']
                and a['quote'] in ' '.join(s['text'].split()) for s in sources) for a in case['references']]
    # Metadata is included because dates and attribution can be supported by it.
    contexts = [json.dumps({k: s.get(k) for k in (
        'citation', 'document_id', 'title', 'circular_number', 'page', 'issue_date', 'text',
        'needs_priority_review', 'section_heading', 'retrieval_reason', 'roles',
        'source_corrections', 'product_memberships', 'metadata_quality', 'source_coverage')}, ensure_ascii=False)
        for s in sources]
    return dict(user_input=case['query'], response=text, retrieved_contexts=contexts,
                reference=case['expected_answer'], claims=claims,
                abstained=bool(response.get('abstained')),
                clarification_requested=bool(response.get('retrieval_trace', {}).get('ambiguities')),
                citation_ids=[s['citation'] for s in sources],
                checks=dict(anchor_hits=hits, anchors_expected=len(hits),
                            invalid_citations=invalid, uncited_claims=uncited,
                            citation_ids_valid=(not invalid and not uncited) if claims else None,
                            expected_abstention=bool(case.get('expect_abstain')),
                            abstention_matches_expectation=(bool(response.get('abstained')) == bool(case.get('expect_abstain')))),
                reference_status=case.get('review_status', 'unreviewed'),
                reference_kind='rubric_only' if case['route'] in ('summary', 'compare') else 'draft_answer')


def load_cases(path):
    path = Path(path)
    raw = path.read_bytes()
    cases = json.loads(raw)
    if path.resolve() == (ROOT / 'evaluation/rag_cases.json').resolve():
        if sha(raw) != (ROOT / 'evaluation/rag_cases.sha256').read_text().strip():
            raise ValueError('Frozen dataset changed; use a new version instead.')
    if len({c['id'] for c in cases}) != len(cases):
        raise ValueError('Duplicate case IDs.')
    return cases, sha(raw)


def capture(args):
    base = local_url(args.base)
    config = read(args.config)
    ollama = local_url(config['ollama_url'])
    cases, dataset_sha = load_cases(args.dataset)
    selected_ids = args.ids.split(',') if args.ids else ([c['id'] for c in cases] if args.all else PILOT)
    by_id = {c['id']: c for c in cases}
    if len(selected_ids) != len(set(selected_ids)) or any(i not in by_id for i in selected_ids):
        raise ValueError('Unknown or duplicate selected IDs.')
    stats = request(base + '/api/stats')
    if stats.get('generation_model') != config['generation_model']:
        raise ValueError('Running app model differs from selected config.')
    out = Path(args.out) if args.out else ROOT / 'evaluation/ragas_runs' / dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    out.mkdir(parents=True, exist_ok=False)
    models = request(ollama + '/api/tags')
    try:
        revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
        dirty = bool(subprocess.check_output(['git', 'status', '--porcelain'], cwd=ROOT, text=True).strip())
    except (OSError, subprocess.CalledProcessError):
        revision, dirty = None, None
    manifest = dict(schema_version=1, created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                    dataset_sha256=dataset_sha, config_sha256=sha(Path(args.config).read_bytes()),
                    configuration={k: v for k, v in config.items() if k != 'source_pack'},
                    application_stats=stats, installed_models=models, git_revision=revision, dirty_worktree=dirty,
                    case_ids=selected_ids, method=args.method, rerank=args.rerank,
                    caveat=CAVEAT, human_review='pending', rows=[], capture_status='running')
    save(out / 'capture.json', manifest)
    for case_id in selected_ids:
        case = by_id[case_id]
        payload = dict(query=case['query'], series=case.get('series') or 'UPI',
                       cutoff=case.get('cutoff', ''), scope=case['scope'], method=args.method,
                       rerank=args.rerank, mode='generate')
        row = dict(id=case_id, case=case, payload=payload)
        start = time.monotonic()
        try:
            row['raw_response'] = request(base + '/api/answer', payload, args.timeout)
            row['sample'] = adapt(case, row['raw_response'])
            row['status'] = 'ok'
        except Exception as exc:
            row.update(status='error', error=f'{type(exc).__name__}: {exc}')
        row['wall_seconds'] = round(time.monotonic() - start, 3)
        manifest['rows'].append(row)
        save(out / 'capture.json', manifest)
        print(case_id, row['status'], row['wall_seconds'], flush=True)
    after = request(base + '/api/stats')
    manifest['snapshot_unchanged'] = all(stats.get(k) == after.get(k) for k in ('fingerprint', 'registry_fingerprint', 'chunks', 'generation_model'))
    manifest['capture_status'] = 'complete' if manifest['snapshot_unchanged'] and all(r['status'] == 'ok' for r in manifest['rows']) else 'completed_with_errors'
    save(out / 'capture.json', manifest)
    export_review(out, manifest)
    print(out, flush=True)
    return 0 if manifest['capture_status'] == 'complete' else 1


def export_review(out, capture_data):
    fields = ['id', 'question', 'draft_reference', 'actual_response', 'abstained', 'reviewer',
              'source_verified', 'answer_correct', 'answer_complete', 'citations_supported', 'notes']
    with (out / 'human_review.csv').open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in capture_data['rows']:
            sample = row.get('sample', {})
            writer.writerow(dict(id=row['id'], question=row['case']['query'],
                                 draft_reference=row['case']['expected_answer'],
                                 actual_response=sample.get('response', ''), abstained=sample.get('abstained', '')))


def metric_skip(sample, metric):
    if sample['checks']['expected_abstention']:
        return 'negative_case_use_abstention_checks'
    if metric in ('factual_correctness', 'context_recall', 'context_precision') and sample['reference_kind'] == 'rubric_only':
        return 'requires_complete_reference_answer'
    if metric in ('faithfulness', 'factual_correctness', 'citation_support') and (sample['abstained'] or not sample['claims']):
        return 'no_substantive_answer_use_abstention_checks'
    if metric != 'factual_correctness' and not sample['retrieved_contexts']:
        return 'no_context_use_retrieval_checks'
    return None


def aggregate(rows, metric):
    entries = [r.get('metrics', {}).get(metric, {'status': 'pending'}) for r in rows]
    values = [e['value'] for e in entries if e['status'] == 'ok']
    return dict(mean=statistics.mean(values) if values else None, scored=len(values),
                errors=sum(e['status'] == 'error' for e in entries),
                skipped=sum(e['status'] == 'skipped' for e in entries),
                pending=sum(e['status'] == 'pending' for e in entries), total=len(entries))


def verify_resume(saved, expected):
    for key in ('capture_sha256', 'judge_model', 'judge_digest', 'judge_endpoint', 'ragas_version',
                'openai_version', 'temperature', 'max_tokens', 'context_length', 'timeout_seconds', 'metric_names'):
        if saved.get(key) != expected.get(key):
            raise ValueError('Cannot resume with changed scoring configuration: ' + key)


def write_summary(out, report, captured):
    lines = ['# Local RAGAS evaluation', '', CAVEAT, '',
             f"Judge: `{report['judge_model']}`. Same model name as generator: **{report['same_model_as_generator']}**. Human review: **pending**.", '',
             '| Metric | Mean among successful scores | Scored | Errors | Skipped | Pending | Total cases |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for name in report['metric_names']:
        a = aggregate(report['rows'], name)
        report.setdefault('summary', {})[name] = a
        value = f"{a['mean']:.3f}" if a['mean'] is not None else 'N/A'
        lines.append(f"| {name} | {value} | {a['scored']} | {a['errors']} | {a['skipped']} | {a['pending']} | {a['total']} |")
    good = [r['sample'] for r in captured['rows'] if r['status'] == 'ok']
    negatives = [s for s in good if s['checks']['expected_abstention']]
    positives = [s for s in good if not s['checks']['expected_abstention']]
    lines += ['', f"Captured: {len(good)}/{len(captured['case_ids'])} successful application responses.",
              f"Negative cases with app abstention: {sum(s['abstained'] for s in negatives)}/{len(negatives)}.",
              f"Positive cases with app abstention: {sum(s['abstained'] for s in positives)}/{len(positives)}.", '',
              'Scores use displayed claims and supplied evidence. Reference-based scores use draft references; summary/comparison references are too incomplete and are skipped. Negative and empty-answer cases are reported separately. Failed scores are not converted to zero or hidden from denominators.', '',
              'Short draft references can produce misleading factual_correctness scores: for example, "P2M only." omits the circular and feature named in the question. Inspect judge_calls.jsonl before interpreting disagreements. Do not report these draft-reference scores as validated answer accuracy.', '',
              'Citation ID validity is a structural check. Optional citation_support applies faithfulness separately to each claim and only its cited sources; it remains a model judgement. No overall accuracy score is calculated.', '',
              'Files: `capture.json` preserves full application responses; this scoring directory contains `scores.json`, `judge_calls.jsonl` and this summary. `human_review.csv` is beside the capture.']
    (out / 'SUMMARY.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


async def score(args):
    # Disable RAGAS usage telemetry before importing the package.
    os.environ['RAGAS_DO_NOT_TRACK'] = 'true'
    from importlib.metadata import version
    from evaluation.ollama_judge import OllamaJudge
    from ragas.metrics.collections import Faithfulness, FactualCorrectness, ContextRecall, ContextPrecision
    captured_path = Path(args.capture)
    captured = read(captured_path)
    if captured.get('capture_status') not in ('complete', 'completed_with_errors'):
        raise ValueError('Capture has not finished.')
    if not captured.get('snapshot_unchanged'):
        raise ValueError('Corpus/configuration changed during capture; recapture before scoring.')
    endpoint = local_url(args.ollama)
    tags = request(endpoint + '/api/tags')
    model = next((m for m in tags['models'] if m['name'] == args.judge_model), None)
    if not model:
        raise ValueError('Judge model is not installed in Ollama.')
    names = args.metrics.split(',')
    if len(names) != len(set(names)) or any(m not in METRICS for m in names):
        raise ValueError('Unknown or duplicate metric.')
    out = args.resume or captured_path.parent / ('scores-' + dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    report = dict(capture_sha256=sha(captured_path.read_bytes()), judge_model=args.judge_model,
                  judge_digest=model['digest'], judge_endpoint=endpoint,
                  same_model_as_generator=args.judge_model == captured['configuration']['generation_model'],
                  ragas_version=version('ragas'), openai_version=version('openai'),
                  temperature=0, max_tokens=args.max_tokens, context_length=args.context_length, timeout_seconds=args.timeout,
                  metric_names=names, caveat=CAVEAT, human_review='pending',
                  runner_sha256=sha(Path(__file__).read_bytes()),
                  adapter_sha256=sha((ROOT / 'evaluation/ollama_judge.py').read_bytes()),
                  rows=[dict(id=r['id'], metrics={}) for r in captured['rows']])
    if args.resume:
        previous = read(out / 'scores.json')
        verify_resume(previous, report)
        if previous.get('runner_sha256') != report['runner_sha256'] or previous.get('adapter_sha256') != report['adapter_sha256']:
            raise ValueError('Scoring code changed; start a new scoring run.')
        report = previous
    else:
        out.mkdir(exist_ok=False)
    save(out / 'scores.json', report)
    llm = OllamaJudge(endpoint, args.judge_model, out / 'judge_calls.jsonl', args.timeout, args.context_length, args.max_tokens)
    scorers = dict(faithfulness=Faithfulness(llm=llm), factual_correctness=FactualCorrectness(llm=llm),
                   context_recall=ContextRecall(llm=llm), context_precision=ContextPrecision(llm=llm))
    try:
        for source in captured['rows']:
            row = next(r for r in report['rows'] if r['id'] == source['id'])
            for name in names:
                prior = row['metrics'].get(name)
                if prior and prior['status'] in ('ok', 'skipped'):
                    continue
                reason = 'capture_failed' if source['status'] != 'ok' else metric_skip(source['sample'], name)
                if reason:
                    row['metrics'][name] = dict(status='skipped', reason=reason)
                    continue
                sample = source['sample']
                llm.current = dict(case_id=source['id'], metric=name)
                start = time.monotonic()
                try:
                    if name == 'citation_support':
                        by_id = dict(zip(sample['citation_ids'], sample['retrieved_contexts']))
                        details = []
                        for claim in sample['claims']:
                            ids = claim.get('sources', [])
                            if not ids or any(i not in by_id for i in ids):
                                details.append(dict(value=0.0, reason='missing_or_invalid_citation', claim=claim))
                            else:
                                res = await asyncio.wait_for(scorers['faithfulness'].ascore(user_input=sample['user_input'], response=claim['text'], retrieved_contexts=[by_id[i] for i in ids]), timeout=args.timeout)
                                details.append(dict(value=float(res.value), reason=getattr(res, 'reason', None), claim=claim))
                        value = statistics.mean(d['value'] for d in details)
                        entry = dict(status='ok', value=value, details=details)
                    else:
                        keys = {'faithfulness': ('user_input', 'response', 'retrieved_contexts'),
                                'factual_correctness': ('response', 'reference'),
                                'context_recall': ('user_input', 'reference', 'retrieved_contexts'),
                                'context_precision': ('user_input', 'reference', 'retrieved_contexts')}[name]
                        res = await asyncio.wait_for(scorers[name].ascore(**{k: sample[k] for k in keys}), timeout=args.timeout)
                        value = float(res.value)
                        entry = dict(status='ok', value=value, reason=getattr(res, 'reason', None))
                    if not math.isfinite(value) or not 0 <= value <= 1:
                        raise ValueError('Evaluator returned a non-finite or out-of-range score.')
                    row['metrics'][name] = entry
                except Exception as exc:
                    row['metrics'][name] = dict(status='error', error=f'{type(exc).__name__}: {exc}')
                row['metrics'][name]['seconds'] = round(time.monotonic() - start, 3)
                if prior:
                    row['metrics'][name]['previous_attempt'] = prior
                print(source['id'], name, row['metrics'][name]['status'], flush=True)
                write_summary(out, report, captured)
                save(out / 'scores.json', report)
        write_summary(out, report, captured)
        save(out / 'scores.json', report)
    finally:
        await llm.close()
    print(out, flush=True)
    return int(any(e['status'] == 'error' for r in report['rows'] for e in r['metrics'].values()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('capture', help='Capture real local app answers; no RAGAS dependency required.')
    p.add_argument('--base', default='http://127.0.0.1:8765')
    p.add_argument('--config', type=Path, default=ROOT / ('config.json' if (ROOT / 'config.json').exists() else 'config.example.json'))
    p.add_argument('--dataset', type=Path, default=ROOT / 'evaluation/rag_cases.json')
    selection = p.add_mutually_exclusive_group()
    selection.add_argument('--ids', help='Comma-separated IDs; default is the documented 12-case pilot.')
    selection.add_argument('--all', action='store_true')
    p.add_argument('--method', choices=('bm25', 'vector', 'hybrid'), default='hybrid')
    p.add_argument('--rerank', action=argparse.BooleanOptionalAction, default=True)
    p.add_argument('--timeout', type=int, default=900)
    p.add_argument('--out', type=Path)
    p = commands.add_parser('score', help='Score a saved capture with local Ollama; each scoring run is separate.')
    p.add_argument('capture', type=Path)
    p.add_argument('--ollama', default='http://127.0.0.1:11434')
    p.add_argument('--judge-model', default='qwen3.5:9b')
    p.add_argument('--metrics', default='faithfulness,factual_correctness,context_recall')
    p.add_argument('--timeout', type=int, default=300)
    p.add_argument('--max-tokens', type=int, default=4096)
    p.add_argument('--context-length', type=int, default=16384)
    p.add_argument('--resume', type=Path, help='Existing scoring directory; resume unfinished/failed metrics with identical settings.')
    args = parser.parse_args()
    return capture(args) if args.command == 'capture' else asyncio.run(score(args))


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(ROOT))
    raise SystemExit(main())
