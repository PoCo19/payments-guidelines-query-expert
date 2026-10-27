# Readiness diagnostics — 22 October 2026

These are development investigations of known failures, not a held-out benchmark or a supervised-pilot acceptance result. Sources, embeddings, configured model sizes, context budgets and graph coverage were preserved.

| Capture | Purpose | Observation and decision |
|---|---|---|
| `20261022T175416438468Z/capture.json` | Three previously failing questions, repeated twice with timing fixes and exact-ID normalization | Six completed answers, zero model failures, 10.250–25.453 seconds. Four answers remained incomplete; two biometric answers had unavailable coverage review. No accuracy or p95 claim. |
| `20261022T175705950313Z/capture.json` | Three-question generation instruction experiment to omit internal IDs | No timeouts; IPO answer still omitted relevant source history. Additional generation instruction removed; no general quality benefit established. |
| `20261022T175948159474Z/capture.json` | Attach-evidence-only repair for a malformed registry label | Three completed answers, but the IPO history repair still repeated the disputed amount and failed support checks. Failure retained. |
| `20261022T180219029498Z/capture.json` | Exact frozen-claim replay with an instruction to repair only its source-specific point | Repair recovered the Circular 127 provision and passed the existing automated checks. This is one claim, not a complete-answer or independent correctness result. Source qualifications still need review. |

All four captures reported unchanged fingerprints during their respective runs. Their code and runner hashes identify different revisions intentionally. Do not mix these outputs into one fixed-code benchmark.

The final [known-question API smoke check](../workbench_20261020/final-readiness-http-smoke.json) exercised the restarted server after the last repair-instruction refinement. It completed in 19.406 seconds and retained the OC185B cumulative-limit distinction plus the OC127 provision. Two other statements were withheld and coverage review flagged issues; the response remained incomplete. On 23 October, current root Python file hashes were checked against that capture and matched. This one live answer is not the independently reviewed paired-answer gate or final release verification.

The first repeat's cold attempt overlapped the initial software regression process. GPU readings were boundary samples only. Later runs were separate from that process, but none used continuous load monitoring. These timings are diagnostic observations, not a controlled hardware comparison or proof that the earlier unusually long delays have been explained.

## Implemented changes

- Normalize only an exact explicitly labelled internal document ID belonging to an attached citation, retaining original text. Unknown or misspelled IDs still fail the ordinary checks.
- For the bounded repair of a numeric failure containing a registry label, use the claim's attached evidence only. Do not borrow another circular's amount. The resulting sentence must pass all existing support checks.
- Record model-metadata calls, configured call timeout and actual duration; restore retrieval timing after embedding/metadata calls. Reject responses arriving after the call budget instead of recording them as timely successes. This is not a hard cancellation mechanism during operating-system suspension.
- Record unavailable completeness-review causes as `timeout`, `invalid_response` or `model_error`; preserve the separate no-additional-issue status. Do not promote invalid output to success.

Original failure: `../maintained_graph_runs/20261022T171138330902Z/capture.json`. That earlier six-attempt run had three model failures. Its failure record remains unchanged.

Run `evaluation/readiness_diagnostics.py --repeats 2` for the known questions, or `--replay-only` for the exact failed claim. The runner retains raw answers, source text, timing and fingerprints in a new directory. It does not score independent correctness.

See [active action register](../../docs/ACTION_ITEMS_20261022.md) for remaining work.
