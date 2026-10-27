# Readiness improvements — 18 October 2026

This iteration improves evidence selection and targeted support checks within the existing RAG flow. It does not certify the product for operational use. Final browser, clean-install and recovery verification remain the last release step, as requested.

## Changes and their purpose

1. **Preserve relevant table evidence.** Limit questions can lose a matching table during reranking. The assembler now protects up to two original candidate chunks whose multiword category matches the question. Headers, row context and source ownership remain intact. Matching a generic word or an MCC alone is insufficient.
2. **Recover the requested notification phase.** A pre-debit exemption is not an answer about post-debit duties. The assembler can include up to two adjacent, explicitly headed notification passages from an already retrieved document. This is bounded neighbouring context, not unrestricted document expansion.
3. **Check the evidence actually selected for a claim.** Table-column and notification-phase checks run again on selected supporting excerpts. Other text in a citation cannot silently supply missing support. Explicit collective claims naming several circulars require evidence from each named circular; this checks ownership, not semantic agreement.
4. **Retain valid combined-limit answers.** The checker separately examines amount-bearing clauses such as “5 lakh per payment while 6 lakh is cumulative.” Previously, a later reference to a daily limit could wrongly cause both values to be checked as cumulative. Swapped values still fail the targeted tests.
5. **Record checker failures.** A timeout or malformed response has a bounded failure reason attached to that claim. Diagnostics do not carry over to the next claim.
6. **Make review reproducible.** Added frozen-case retrieval/answer runs, paired paraphrases, a source-backed checker challenge, a process-repeatability probe and a source-review queue builder. Captures preserve inputs, outputs and fingerprints rather than only aggregate scores.

The answer continues through ordinary question-focused generation and citation checking. These changes do not replace answers with retrieved chunks. Model choices, context/output budgets, corpus text, embeddings and storage formats were not changed. Explicit filters and the 18,000-character evidence budget remain enforced. Graph assistance remains enabled; experimental contextual BM25 and structured synthesis remain disabled.

## Measured evidence

| Check | Result | Interpretation |
|---|---|---|
| Frozen 138-case retrieval run | 208 → 212 of 223 source anchors; four gained, zero lost | More required passages reached the context; not an answer-accuracy score |
| All anchors on positive questions | 102 → 105 of 114 | Nine positive questions still miss at least one anchor |
| Graph controls | 12/12 retained | Existing graph control behaviour preserved in this run |
| Negative retrieval | 10/17 empty, unchanged; two missing-source notices retained | Empty retrieval is measured separately from generated abstention |
| Four added paraphrases | 6/8 → 8/8 anchors; zero losses | Small, co-designed development check; not held-out validation |
| Full Python regression, final code | 375 tests passed | Software regression evidence, not independent answer verification |
| BM25 process repeatability | No ordering differences on 28 questions across three hash seeds | Does not establish hybrid/ANN or final-context repeatability |
| Source/graph integrity triage | 4,834 pages scanned; 55 graph anchors checked, zero stale | Hash/quote integrity only; relationship meaning still needs review |

The main retrieval capture has no execution errors or model fallback and unchanged recorded inputs. Its root-code fingerprint predates the later checker-only fixes; retrieval code and corpus were unchanged by those fixes. Do not describe it as a rerun of the final generation code. The existing development cases and added labels are AI-assisted and await independent review. No controlled latency improvement is claimed.

## Generated answers: gains and unresolved failures

The first eight-scenario capture included two model timeouts (summary and Deemed Debit chronology). They were retained as failures. A final-code five-scenario retry completed with 15/15 reference anchors, zero request errors/fallbacks and unchanged recorded inputs; observed request durations were 18.6–42.6 seconds (median 38.9). These sequential observations are not a controlled hardware/latency benchmark.

| Scenario | Final-code observation |
|---|---|
| Credit-card bill payment limits | Retained the correct combined single-payment/cumulative distinction; coverage review timed out |
| OC128 / 128A chronology | Retained the exclusion → inclusion distinction; coverage reviewer incorrectly treated the two documents as a conflict |
| OC185-series tax question | Withheld a false cumulative-tax claim, but wording about which circular sets versus references the limit still needs review; coverage review timed out |
| IPO cumulative versus single mandate | Retained the central distinction; repairs produced duplicate statements and one “Document S9” claim was wrongly caught by the numeric check; coverage warnings remain questionable |
| OC186A summary | Generated a cited summary after the earlier timeout; not independently scored |

Thus **zero generation fallbacks does not mean five clean answer-quality passes**. Two coverage reviews were unavailable and two raised issues. A reproducible tax-series false acceptance was added to the checker challenge so that narrow success counts cannot hide it. Collective source-presence checks alone cannot detect every wrong interpretation when all named documents are cited. Fixing that requires more precise semantic ownership evaluation, not simply adding more citations.

The initial 14-claim challenge matched all seven valid and seven invalid expected labels, with no unavailable checks. Those labels are AI-assisted. The expanded 16-claim challenge included the observed collective-attribution failure and a valid tax-specific control: **one false acceptance, zero valid claims withheld, zero unavailable checks** (eight valid/eight invalid labels; 15/16 matched). This is the more informative result; do not report the earlier 14/14 as general checker reliability.

A generic prompt-only instruction requiring each named document to support collective assertions was tested against the same 16 claims. It produced the same false acceptance, so the instruction was reverted. Both records are retained. No unsupported improvement is claimed, and the tested final runtime code matches the five-scenario capture and passing full regression again after reversion.

The browser server was not restarted or verified against this final code in this iteration. New evaluation processes exercised the code directly. Final release verification remains deferred.

## Source-review queue

The queue contains 2,132 priority pages across 946 documents. A separate metadata queue lists 1,455 converted documents without an issue date; 359 unavailable records are preserved. Signals include monetary values, table layouts, operational codes, qualifications, empty/thin pages and graph participation. They overlap and are **not counts of confirmed errors**.

All 13 graph relationships remain proposed and AI-assisted. Original-URL availability was not checked live. No new OCR correction or embedding rebuild was performed in this iteration. Reviewers must compare originals before approving any text change; uncertain cases stay flagged. See the [record guide](../evaluation/readiness_review_20261018/README.md).

## Closure boundaries

| Workstream | Status after this iteration |
|---|---|
| Specific missing table and post-notification evidence | Implemented; retrieval and paraphrase checks passed |
| Targeted table/phase/ownership safeguards | Implemented; software regression passed; broader semantics still open |
| Reproducible evaluation and source-review tools | Implemented with saved records |
| Full-library source correctness | Not established; queue prepared for review |
| Checker reliability and answer completeness | Still open; automated support is fallible |
| Repeatability/performance | BM25 probe completed; hybrid context variation and controlled warm/cold latency remain open |
| Final release verification and refreshed colleague package | Deferred until quality decisions are complete |
| GitHub publication | Not performed |

Next work should focus on the remaining source-scope and coverage-review failures, then independent review of reference answers. Do not promote contextual retrieval, structured synthesis or a larger model based solely on these targeted gains. Final release verification follows those decisions.

## Saved records

- [138-case retrieval capture](../evaluation/readiness_runs/20261018T050704935147Z/capture.json)
- [Four paired paraphrases](../evaluation/readiness_runs/paraphrases-20261018T063720397774Z/capture.json)
- [Initial eight generated scenarios, including failures](../evaluation/readiness_runs/20261018T063852267607Z/capture.json)
- [Initial 14-claim checker challenge](../evaluation/readiness_runs/checker-20261018T064719013412Z/capture.json)
- [Final-code five-scenario retry](../evaluation/readiness_runs/20261018T101911169903Z/capture.json)
- [Expanded 16-claim challenge, including the false acceptance](../evaluation/readiness_runs/checker-20261018T102246174010Z/capture.json)
- [Unsuccessful prompt-only experiment, reverted](../evaluation/readiness_runs/checker-20261018T102354782157Z/capture.json)
- [Final full Python test log](../evaluation/readiness_review_20261018/python-tests-final.txt)
- [Source triage summary](../evaluation/readiness_review_20261018/source_review_summary.json)
- [BM25 process probe](../evaluation/readiness_review_20261018/repeatability-before.json)
