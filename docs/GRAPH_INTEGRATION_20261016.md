# Graph-assisted retrieval in the main flow — 16 October 2026

## Decision

Use the existing bounded graph overlay in the main local application for its supported source families. This is a controlled adoption of a retrieval improvement, not a claim that graph-assisted answers are always correct. The user approved this integration after reviewing the remaining answer-quality limitations.

This decision supersedes the opt-in rollout status in the 14–15 October reports. Their experiment results and unresolved findings remain historical evidence, not newly passed acceptance gates.

## Flow

Question and filters → hybrid search and reranking → relevant starting documents → matching graph topic and source links → bounded evidence assembly → answer generation → citation and scope checks → supported answer and visible gaps.

- The graph covers UPI OC128 deemed debit, OC226 biometrics, OC76, OC141, OC185 and IPO-limit relationships. It does not cover every document or every payments topic.
- It expands only when a supported topic/reference and a retrieved source identity match. Unrelated questions retain ordinary retrieval.
- Traversal remains limited to two hops and twelve graph chunks, within the existing overall evidence budget. Product and date filters continue to apply.
- Strict context and selected-document summary/comparison routes bypass graph expansion. Ambiguous questions still require clarification.
- Every anchor must match the stored page hash and quotation. An unavailable or stale graph falls back to ordinary retrieval with a warning.
- Proposed references, aspect amendments and topic relationships remain distinct. Relationships do not decide legal precedence or establish full supersession.
- The UI shows which marked graph passages are present. This is coverage of the graph's selected evidence, not all potentially applicable rules.
- The original scope, citation, source-quality and bounded-repair checks remain enabled. Unsupported claims remain withheld.

## Configuration and rollback

The active `config.json` selects `pilot/upi_extended_graph_v3.json` through `evidence_graph_path`, using the corrected `payments-ocr-audit-20261015` release. Use the normal application on port 8765; a separate graph-preview window is no longer necessary.

To disable the overlay, remove `evidence_graph_path` from the active configuration and restart the app. This does not change source documents, chunks, embeddings or stored reviews. A pre-integration configuration copy and final activation evidence are retained under `evaluation/graph_integration_20261016/`.

The older colleague handoff archive and its matching configuration remain a historical release. They have not been silently pointed at a graph whose anchors require the repaired corpus. Updating that distributable requires packaging the repaired source release and manifest together; no GitHub publication is included here.

## Known limitations

The latest generated-answer findings include an IPO attribution error and a Tap & Pay summary extrapolation. Checks withhold those claims, but automated repair does not yet reliably produce complete answers. Graph retrieval improves evidence availability; answer interpretation remains a separate problem. Independent review and unseen-question evaluation are still pending.

The graph is an AI-curated JSON overlay with source anchors, not a new graph database or an automatically maintained whole-corpus knowledge graph. New documents do not acquire verified graph relationships merely by being embedded. Source changes require anchor review before graph reactivation.

## Validation

The final activation record links the paired forty-case retrieval comparison, regression results and live main-app checks. Retrieval metrics are separate from generated-answer correctness; the co-designed development questions are not held-out independent evaluation.

The [16 October paired run](../evaluation/graph_runs/20261016T024256266183Z/summary.md) completed all 40 cases in both arms with no errors or model fallback. Across 28 substantive cases, graph assistance retrieved **78/78 expected, model-usable anchors**, compared with **69/78** without it; complete anchor coverage improved from **21/28 to 28/28 cases**. All **12/12 routing/filter controls** passed in both arms. Both designated missing-source warnings appeared with the graph (0/2 without it).

Median substantive retrieval time was 1.632 seconds baseline and 1.555 seconds graph in this single run. Cache/warm-up effects prevent concluding that graph retrieval is faster. These figures exclude answer generation and do not score answer correctness.

All 20 graph regression tests passed, covering route isolation, product boundaries, stale anchors, missing sources, provenance and traversal bounds. JavaScript syntax and evidence rendering checks passed. See [the activation record](../evaluation/graph_integration_20261016/activation.json) for configuration and live verification evidence. The broader 331-test run is recorded in the previous day's audit; this activation changes configuration and UI labels rather than retrieval algorithms.
