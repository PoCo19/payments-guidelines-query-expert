# Corrected source and graph rollout decision

14 October 2026. Payments Guidelines Query Expert.

**Closed out on 15 October:** [completion verification](../source_repairs/oc185b-20261014/completion-check-20261015.json) confirmed the active release, corrected Markdown and legacy reading copy, source hashes, passage eligibility and unchanged code hashes for the 306-test regression record. The saved model comparisons remain valid; they were not rerun solely for closeout. The repair is complete. Default graph rollout remains deferred for the evaluation gates below.

## Source repair completed

The original OC185B PDF page 1 says **₹5 lakh** in its reference to the earlier tax-payment enhancement. Its indexed OCR said **25 lakh**. This was visually checked against the original PDF; it is not a new limit or a new circular.

The [reusable Markdown](../source_repairs/oc185b-20261014/OC185B_corrected.md) now contains the corrected amount and both source pages. The original research-pack Markdown reading copy was also corrected. A new local corpus release, `payments-oc185b-repair-20261014`, replaces the indexed page text while preserving the document identity, original extraction and previous release. The source record points to the corrected Markdown. The new Chroma/SQLite snapshot passed structural validation; one embedding was recomputed and 14,479 were reused.

The corrected passage **is available for generation and support checks**. The old exclusion applies only to historical corrupt or unreviewed versions. An exact corrected-page hash releases the repaired version; no broad guard is disabled. The alternate historical import and old releases remain preserved for audit, not silently overwritten. See the [repair record and reproduction instructions](../source_repairs/oc185b-20261014/README.md).

Graph v3 updates the four anchors on the repaired page and removes the obsolete OCR warning. Graph v2 and its experiments remain frozen. The separate graph launcher uses v3; ordinary app startup selects the corrected corpus but keeps graph expansion opt-in.

## What the evaluation actually establishes

The [repaired-source paired run](../evaluation/graph_runs/20261014T171328151412Z/summary.md) used the same 40 development cases, model settings, corpus and budgets for both arms. It completed without fallback and with unchanged snapshots.

| Measure | Hybrid baseline | Hybrid plus graph |
|---|---:|---:|
| Required source anchors retrieved and eligible for model use | 69/78 | 78/78 |
| Substantive questions with all expected anchors | 21/28 | 28/28 |
| Routing/filter controls | 12/12 | 12/12 |
| Required missing-source disclosures | 0/2 | 2/2 |

There are 28 substantive questions plus 12 controls, not 78 questions. Questions can require multiple source passages. The previously excluded passage is now usable, so raw and model-usable anchor counts agree. The graph and these expected anchors were co-designed; this is a development result, not independent or held-out evidence. Single-run median substantive retrieval latency was 1.629 seconds baseline and 1.563 seconds graph; the small difference is not evidence that the graph is faster.

**The demonstrated improvement is evidence coverage. General answer correctness has not been established.** Earlier generated-answer captures included wrong table-category attribution, incomplete split-table citations and date-check failures even when the required evidence was retrieved. The same-model checker sometimes accepted an incorrect interpretation. Repairing one source does not prove those different failures are fixed.

The [post-repair tax and IPO answer rerun](../evaluation/graph_runs/20261014T171533381283Z/summary.md) completed all four model requests without fallback. Both tax answers rejected 25 lakh and retained the source's 5 lakh amount; both cited the repaired OC185B passage. The graph tax draft withheld two of four proposed claims. For IPO, the graph retained the cumulative-versus-single-mandate distinction but withheld another claim and returned `incomplete`; the baseline returned a draft. These observed outcomes support fixing the extraction, but do not demonstrate a consistent graph answer-quality improvement. Independent review sheets remain unfilled. Saved captures include the claims and warnings, not only the status labels.

## Rollout recommendation

Keep the graph implementation as a maintained part of the project, but **do not enable it by default for all users yet**. It is currently a curated six-topic pilot, not an automatically maintained graph of every payment source. Default activation would imply more reliability than our measurements support.

Before default activation, complete these concrete gates:

1. Independently review the graph relationships and missing-source notices against the original circulars. Separate explicit references, aspect-level amendments and related topics; avoid unsupported legal supersession.
2. Independently author and review a fresh set of questions, including category/purpose-code traps, per-transaction versus cumulative limits, changed dates, unchanged exceptions and unavailable sources. Keep the evaluation questions separate from graph curation.
3. Score both baseline and graph answers, with the reviewer blinded to the variant where feasible: correct conclusion, applicable scope, current-versus-historical wording, all material conditions, citation support, justified abstention and latency. Report critical errors separately from averages. RAGAS can supplement this work but cannot replace source-expert review.
4. Resolve the observed scope and citation failures and show no critical regression on the reviewed set, plus repeat the existing original-50 and mixed-source checks before widening the pilot. Agree acceptance thresholds with the intended users rather than treating 78/78 retrieved passages as a production approval.

Automated regression after the source-gate change: [306 tests passed](../source_repairs/oc185b-20261014/regression.json), zero failures/skips. This covers engineering behaviour, not regulatory correctness. Nothing was committed or pushed to GitHub; the frozen colleague archive has not been replaced.
