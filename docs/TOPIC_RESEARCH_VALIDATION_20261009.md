# Topic research validation — 9 October 2026

The implementation is exercised locally. These checks demonstrate working code paths, not independently measured answer accuracy. No RBI documents have been ingested; mixed-publisher coverage is currently tested using synthetic fixtures.

## Automated and browser checks

- 228 Python tests passed (`python -m unittest discover -s tests`, 14.702 seconds). Includes document intake, unchanged corpus fingerprints, explicit filters, mixed-source retrieval, bounded context, qualification recovery, review failures and source-bound excerpts.
- Both JavaScript suites passed: answer formatting and research coverage rendering/export, including escaping and citation links.
- `git diff --check` found no whitespace errors.
- Local browser topic search returned 14 excerpts across three UPI Circle circulars. The optional entity appeared in the scope panel, documents were grouped once with their citation links, and missing exceptions were visibly labelled as partial coverage. Source navigation and export were exercised during implementation; rendering/export logic is also covered by the JavaScript tests.

## Controlled retrieval comparison

Saved evidence: `reports/research-comparison/20261009T143535Z/results.json`.

| Measure | Previous selection | Topic research |
|---|---:|---:|
| Expected source anchors located | 55/55 | 55/55 |
| Negative cases returning no evidence | 5/6 | 5/6 |
| Request errors | 0 | 0 |
| Median retrieval latency | 167.26 ms | 173.80 ms |

The frozen 50-case set contains 44 positive cases with 55 anchors and six negative cases. It is AI-assisted and awaiting independent review. These results show no regression on those retrieval measures in one run; they do not establish improved answer correctness or mixed-authority coverage. One negative case still returns passages in both variants. The earlier `20261009T143301Z` run used incorrect case settings and is retained only as a debugging record.

## Actual model observations, including failures

All live runs use the active Qwen 3.5 9B model and unchanged corpus. The question requested a two-sentence UPI Circle consent overview and identified the research entity as payer bank.

| Saved run under `reports/research-live/` | Observation |
|---|---|
| `20261009T144036Z` | Incorrectly assigned generic device-linking user consent to a specific participant. Existing claim checking accepted it. Coverage review produced invalid quotations and was marked unavailable. |
| `20261009T144431Z` | After prompt clarification, this answer preserved the generic user wording. Coverage quotation validation still failed. This single improvement is not a reliable quality score. |
| `20261009T151954Z` | Excerpt-ID review completed and attached exact original text. Generation still misstated who accepts the delegation request. The reviewer incorrectly called different participant responsibilities a conflict. Full request took 26.887 seconds. |

The quotation failure was addressed structurally: the model selects locally assigned excerpt IDs instead of writing quoted text. Interpretation failures remain open. A valid citation, automated-supported label or review finding is not a correctness guarantee. Findings remain separate from the answer and require source inspection.

## Token limits and next evaluation

Configuration remains 16,384 context tokens, 3,072 maximum output tokens and an 18,000-character evidence budget. The second live run used 6,189 generation prompt tokens and 155 generated tokens, ending normally. Neither token limit constrained that answer. Increasing limits alone would not fix the observed role-attribution or false-conflict errors.

Prioritise independently reviewed entity/action/condition cases and mixed-source questions. Measure supported claims, omitted qualifications, reviewer false positives, negative-case behaviour and end-to-end latency. The current implementation is complete as a prototype feature; demonstrated model-quality limitations remain explicit. Changes are local and have not been pushed to GitHub.
