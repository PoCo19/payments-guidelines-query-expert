"""Summarize paired retrieval changes without treating anchors as answer accuracy."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import statistics

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('capture', type=Path)
    parser.add_argument('--dataset', type=Path, default=ROOT/'evaluation/context_regression_20261017.json')
    args = parser.parse_args()
    report = json.loads(args.capture.read_text(encoding='utf-8'))
    assert report['status'] == 'complete' and report['benchmark_valid'], 'Do not summarize an invalid/unfinished run.'
    assert hashlib.sha256(args.dataset.read_bytes()).hexdigest() == report['dataset_sha256']
    cases = {c['id']: c for c in json.loads(args.dataset.read_text(encoding='utf-8'))}
    pairs = {i: {} for i in cases}
    for row in report['rows']:
        assert row['arm'] not in pairs[row['id']]
        pairs[row['id']][row['arm']] = row
    assert all(set(p) == {'baseline', 'variant'} for p in pairs.values())
    details = []
    for case_id, pair in pairs.items():
        case = cases[case_id]
        b, v = pair['baseline'], pair['variant']
        assert b['status'] == v['status'] == 'ok'
        row = dict(id=case_id, group=case['evaluation_group'], anchors=len(case['references']),
                   baseline=sum(b['anchor_hits']), variant=sum(v['anchor_hits']),
                   gained=sum(not x and y for x, y in zip(b['anchor_hits'], v['anchor_hits'])),
                   lost=sum(x and not y for x, y in zip(b['anchor_hits'], v['anchor_hits'])))
        for arm, entry in pair.items():
            response = entry['response']; trace = response.get('retrieval_trace', {})
            row[arm+'_route'] = trace.get('route', response.get('response_status', 'unknown'))
            row[arm+'_reranked'] = bool(trace.get('reranker', {}).get('enabled'))
            row[arm+'_seconds'] = entry['wall_seconds']
            row[arm+'_negative_empty'] = bool(case.get('expect_abstain')) and not response.get('sources')
            row[arm+'_raw_top6'] = sum(entry.get('raw_top6_anchor_hits', []))
            row[arm+'_raw_expected'] = len(entry.get('raw_top6_anchor_hits', []))
            kind = case.get('control'); graph = trace.get('graph_context', {})
            checks = {
                'clarification': response.get('response_status') == 'clarification_needed' and not response.get('sources'),
                'empty': not response.get('sources'),
                'graph_inactive': graph.get('status', 'not_applicable') == 'not_applicable',
                'cutoff': all(s.get('issue_date') and s['issue_date'] <= case.get('cutoff', '') for s in response.get('sources', [])),
                'unchanged': 'graph_context' not in trace and [s['id'] for s in b['response']['sources']] == [s['id'] for s in v['response']['sources']],
            }
            row[arm+'_control_pass'] = checks.get(kind)
            row[arm+'_gap_disclosed'] = (case['expected_gap'] in ' '.join(response.get('warnings', []))) if case.get('expected_gap') else None
        details.append(row)
    summary = {}
    strata = {'all': details}
    strata.update({g: [r for r in details if r['group'] == g] for g in sorted({r['group'] for r in details})})
    strata['reranked_both'] = [r for r in details if r['baseline_reranked'] and r['variant_reranked']]
    strata['bypass_both'] = [r for r in details if not r['baseline_reranked'] and not r['variant_reranked']]
    strata['reranking_changed'] = [r for r in details if r['baseline_reranked'] != r['variant_reranked']]
    for group, rows in strata.items():
        summary[group] = dict(cases=len(rows), anchors=sum(r['anchors'] for r in rows),
                              positive_cases=sum(bool(r['anchors']) for r in rows),
                              negative_cases=sum(bool(cases[r['id']].get('expect_abstain')) for r in rows),
                              gained=sum(r['gained'] for r in rows), lost=sum(r['lost'] for r in rows))
        for arm in ('baseline', 'variant'):
            summary[group][arm] = dict(found=sum(r[arm] for r in rows),
                all_anchor_cases=sum(r['anchors'] > 0 and r[arm] == r['anchors'] for r in rows),
                negative_empty=sum(r[arm+'_negative_empty'] for r in rows),
                raw_top6=sum(r[arm+'_raw_top6'] for r in rows), raw_expected=sum(r[arm+'_raw_expected'] for r in rows),
                controls_pass=sum(r[arm+'_control_pass'] is True for r in rows),
                controls_total=sum(r[arm+'_control_pass'] is not None for r in rows),
                gaps_disclosed=sum(r[arm+'_gap_disclosed'] is True for r in rows),
                gaps_total=sum(r[arm+'_gap_disclosed'] is not None for r in rows),
                median_seconds=statistics.median(r[arm+'_seconds'] for r in rows) if rows else None)
    out = args.capture.parent
    with (out/'paired_cases.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(details[0])); writer.writeheader(); writer.writerows(details)
    (out/'stratified_summary.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')
    lines = ['# Consolidated contextual retrieval comparison', '',
        'AI-assisted development regression, not held-out testing or answer accuracy. '
        'Both arms retain the existing graph, vectors, reranker configuration and context budget. '
        'Only lexical metadata enrichment differs. Original request routes are preserved.', '',
        '| Family / execution stratum | Cases | Expected anchors | Baseline found | Enriched found | Anchors gained / lost |',
        '|---|---:|---:|---:|---:|---:|']
    for group, result in summary.items():
        lines.append(f"| {group} | {result['cases']} | {result['anchors']} | {result['baseline']['found']} | {result['variant']['found']} | {result['gained']} / {result['lost']} |")
    lines += ['', 'Family rows partition the full set. Execution strata are a separate partition; do not add both sets of rows together. '
              'Bypass cases cannot demonstrate a reranking benefit. Graph controls include filtering and missing-reference routing, not general answer correctness.', '',
              'See `stratified_summary.json` for negative empty-evidence counts, raw top-six diagnostic retrieval, graph controls, '
              'missing-source disclosures and local median times. Negative empty-evidence counts are not generated-answer abstention scores. '
              'Single-run latency includes warm-up and cache effects; it is not a proven performance difference.', '',
              'Case-level gains/losses and routes: `paired_cases.csv`. Full evidence, traces and fingerprints: `capture.json`.']
    (out/'comparison.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))
    print('CHANGED ANCHORS', json.dumps([r for r in details if r['gained'] or r['lost']], indent=2))


if __name__ == '__main__':
    main()
