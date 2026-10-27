# Scope, citations and source accuracy — 15 October 2026

The work addresses two distinct failure modes: a model can attach a rule to the wrong category or circular, and the source text itself can contain OCR errors. Better retrieval alone does not resolve either problem.

## Changes to answer checking

The existing search, hybrid retrieval, reranking, document selection and context budgets remain in place. The changes sit between drafting and displaying the answer:

1. Table-based amounts must retain their category and limit-column meaning. A shared merchant code is insufficient to transfer a limit between categories. This deterministic check recognises explicit monetary Markdown tables; it is not a general rules engine.
2. A claim naming a circular cannot silently borrow an explicit acronym scope from a different cited circular. This narrow check addresses cases such as attributing a specific mandate rule to a general category table. It also applies to other sources and acronyms; there is no NPCI/RBI precedence table.
3. Explicitly linked companion fragments can complete a citation before checking, but only when already retrieved from the same document and page and eligible for generation. This handles a table split across chunks without adding unrelated citations. Both the original and added citation IDs are retained. The checker then selects immutable source excerpts. Most chunks remain whole, retaining their qualifications. Numbers must appear in the selected support or attribution metadata, rather than somewhere else in a cited document.
4. Up to two failed claims can each receive one correction attempt using already retrieved, generation-eligible evidence. Corrected claims must pass the same checks again. The original claim and attempted correction are retained. Timeouts do not trigger content repair.
5. The checker returns a compact verdict and source IDs. The application supplies readable status explanations. This avoids lengthy checker narration consuming the review budget. It does not increase the model context or output settings.
6. A within-ceiling exemption cannot establish what happens above that ceiling. A targeted guard catches this extrapolation when the cited evidence contains no explicit above-ceiling rule.

Unsupported statements remain withheld. The UI and exported notes retain repair information. The local model still performs semantic checking, so agreement between generation and checking is not independent verification.

## Random source audit

Sampling used seed **20261015**: six documents drawn without replacement from a sorted population of 89 converted documents with OCR, one to three indexed pages and a locally available PDF. All ten sampled pages were visually compared with rendered original PDF pages. This was a targeted AI-assisted comparison of operational text, dates, amounts, references and tables; it was not a word-for-word certification of logos, signatures or contact details.

| Circular | PDF-verified correction | Important content retained |
|---|---|---|
| UPI OC107A | Three damaged date suffixes | RRN formats and the source's printed volume figures |
| UPI OC186 | Header reference/date and January deadline | Original Rs.500 threshold, initiation mode 06, NFC Type 2 and liability wording |
| UPI OC193A, including attached OC193 | Date suffixes and attached circular reference | Printed “35 digits” and “35 characters (alphanumeric)” wording; effective date and bank obligations |
| UPI OC208B | Reference OCR and referenced date suffixes | August 20, 2025 go-live date |
| Product Compliance Q4 | Page-1 dates and eight-row compliance table | Restored certificate-date and RBI Oversight instructions; page-2 action numbers 3 and 4 remain as printed |
| UPI OC160 | Eleven-entry dispute table and date suffixes | Restored Re-presentment and RET; no-reversal condition and zero report values |

There are **21 explicit replacements on nine pages across six documents**. One inspected page needed no targeted edit. No additional incorrect monetary amount was found in this sample. Historical limits were not updated to later rules. The prior OC185B ₹5 lakh repair remains intact.

The original reading Markdown files were corrected, with original-byte backups. Canonical corrected Markdown, exact before/after changes, PDF and page hashes, and the inspected page images are saved under [the audit folder](../source_repairs/ocr-audit-20261015/README.md). Raw OCR and historical corpus releases remain available.

## Source release and checks

Active release: `payments-ocr-audit-20261015`. The prior release remains available for rollback.

- Document/page identities preserved: 1,929 records, 4,834 pages and 14,480 chunks.
- Exactly nine page texts changed; 4,825 page texts are unchanged.
- Thirteen vectors recomputed; 14,467 reused from the embedding cache.
- All 55 existing graph anchors still validate against source text.
- Targeted retrieval finds all six corrected documents.

### Verification results

- **331 Python tests passed**, including existing flows and new scope, citation, repair-budget and source-integrity checks. The final prompt-only refinement was followed by another **25/25 targeted tests**. Both JavaScript renderer suites and syntax checks passed.
- The [frozen 50-case retrieval run](../evaluation/payments_runs/20261015T155206938369Z/capture.json) found **55/55 expected source anchors across 44 positive cases**. Five of six negatives returned no evidence. RAG-048 still retrieved an irrelevant passage; its separate generated-answer check abstained. These are retrieval observations, not an answer-accuracy percentage. The dataset is AI-assisted and awaits independent review.
- Normal HTTP statistics and source-reader checks confirmed the repaired release. Browser search for OC160 opened the corrected text, including the restored **Re-presentment** and **RET** entries. The [source reader screenshot](images/ocr-audit-source-20261015.png) records the document and correction label.
- The [real-source scope replay](../source_repairs/ocr-audit-20261015/scope_replay.json) rejected wrong tax-category and per-transaction amounts while retaining the matching cumulative-limit examples. These are controlled probes, not generated-answer scores.

### Generated-answer findings

| Scenario | Observed result | Saved evidence |
|---|---|---|
| Deemed-debit citation fragments, DD-01 | Same-page citation completion resolved the missing-fragment check in this run | [Graph comparison](../evaluation/graph_runs/20261015T154738338732Z/) |
| Tax versus GeM limits, LIMIT-04 | Both modes produced supported drafts in the reviewed run | [Graph comparison](../evaluation/graph_runs/20261015T154738338732Z/) |
| Direct PoS question and comparison | Cited drafts returned; unrelated negative question abstained | [Representative cases](../evaluation/payments_runs/20261015T155440901000Z/capture.json) |
| IPO attribution, IPO-02 | Graph mode retrieved all four anchors, but still generated incorrect attribution. The final attribution guard withheld it and rejected the attempted repair; the answer remained incomplete | [Later IPO run](../evaluation/graph_runs/20261015T155409622507Z/) |
| OC186A summary, RAG-033 | Review exposed an unsupported claim about transactions above the ceiling. The new guard withheld that claim. The latest correction attempt also failed checks; eleven other claims remained | [Final summary check](../evaluation/payments_runs/20261015T160001177841Z/capture.json) |

Earlier drafts accepted by the checker are not counted as proof of correctness. In particular, the earlier IPO repair escaped the first version of the attribution guard, and the initial summary contained the above-ceiling inference. Both findings drove regression checks. Runs under `evaluation/graph_runs/20261015T034654346218Z/` were interrupted by an extended execution pause; their wall-clock latency is unsuitable for performance conclusions. Earlier stopped or superseded development runs remain saved. No aggregate generated-answer accuracy claim is made from these iterations.

### Remaining acceptance work

Automatic correction is not yet reliably producing complete answers for the IPO and summary failures. The implemented protection is to withhold failed claims and expose the limitation. Before enabling graph retrieval by default, independently review these failure cases, rerun the broader graph cases on the final code, and demonstrate correct complete answers without weakening the checks. Broader source sampling should include longer documents and other product families. None of these gates is represented as completed here.

## Limits and rollout decision

This sample is predominantly UPI plus one Product Compliance document. It cannot estimate error rates for the entire corpus, long documents or other product families. Independent human review of the corrected passages remains pending.

The table and attribution guards are conservative heuristics. They cannot establish every synonym, applicability condition, amendment relationship or legal precedence. Some correct claims may still be withheld. Source completeness and independent answer evaluation remain separate requirements.

Graph-assisted retrieval remains an opt-in pilot. These fixes apply to normal and graph-assisted answers; they do not justify enabling the graph for every question or claiming production-wide correctness. No GitHub push is part of this work.
