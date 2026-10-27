"""Freeze existing development families for a broader lexical-context comparison."""
import copy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from evaluation.ragas_runner import load_cases


def main():
    cases, inputs = [], {}
    for name, group in [('rag_cases.json', 'original_upi'),
                        ('payments_cases_v1.json', 'payments'),
                        ('expanded_evidence_cases_20261017.json', 'paraphrases')]:
        rows, fingerprint = load_cases(ROOT / 'evaluation' / name)
        inputs['evaluation/' + name] = fingerprint
        for original in rows:
            case = copy.deepcopy(original)
            case['evaluation_group'] = group
            case['provenance'] = {'dataset': name, 'case_id': original['id']}
            if group == 'original_upi':
                case['series'] = 'UPI'  # Original runner's legacy filter.
            cases.append(case)
    graph_path = ROOT / 'pilot/upi_extended_graph_v3.json'
    graph = {n['id']: n for n in json.loads(graph_path.read_text(encoding='utf-8'))['nodes']}
    source_path = ROOT / 'evaluation/graph_pilot_cases_v2.json'
    inputs[str(graph_path.relative_to(ROOT)).replace('\\', '/')] = hashlib.sha256(graph_path.read_bytes()).hexdigest()
    inputs[str(source_path.relative_to(ROOT)).replace('\\', '/')] = hashlib.sha256(source_path.read_bytes()).hexdigest()
    for original in json.loads(source_path.read_text(encoding='utf-8'))['cases']:
        case = copy.deepcopy(original)
        case.update(id='G-' + original['id'], evaluation_group='graph',
                    provenance={'dataset': source_path.name, 'case_id': original['id']},
                    references=[{k: graph[n][k] for k in ('document_id', 'page', 'quote')}
                                for n in original['required_anchor_ids']],
                    route=original.get('route', 'auto'), scope=original.get('scope', 'related'),
                    series=original.get('series', 'UPI'),
                    expect_abstain=original.get('control') in ('empty', 'clarification'),
                    expected_answer='Retrieval/control case only; no reference answer authored.',
                    review_status='AI_assisted_requires_independent_review')
        cases.append(case)
    ids = [c['id'] for c in cases]
    assert len(ids) == len(set(ids))
    # Retain provenance and route differences; disclose overlap instead of pretending independence.
    keys = [json.dumps({k: c.get(k, '') for k in ('query', 'series', 'scope', 'route', 'cutoff', 'document_ids')}, sort_keys=True) for c in cases]
    out = ROOT / 'evaluation/context_regression_20261017.json'
    content = (json.dumps(cases, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    out.write_bytes(content)
    fingerprint = hashlib.sha256(content).hexdigest()
    out.with_suffix('.sha256').write_text(fingerprint + '\n', encoding='utf-8')
    manifest = dict(cases=len(cases), unique_request_specs=len(set(keys)),
                    groups={g: sum(c['evaluation_group'] == g for c in cases) for g in sorted({c['evaluation_group'] for c in cases})},
                    input_sha256=inputs, dataset_sha256=fingerprint,
                    caveat='Consolidated existing development cases, including related paraphrases. Not new independent questions or a held-out benchmark. Graph and expectations were co-designed. Original routes preserved; legacy UPI filter explicit. No answer-correctness metric.')
    out.with_suffix('.manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    main()
