# Local RAG integration validation — 2026-09-24

Models: qwen3.5:9b and qwen3-embedding:0.6b. Answer context: 8192; thinking disabled.
Index: 428 passages, 1024-dimensional embeddings, 107 documents, 251 pages.
Raw evidence and outputs: `live_results.json`. Reproduction script: `run_live.py`.

## Retrieval smoke checks

| Method | Passed / total | Positive-case MRR | Positive-case document recall |
| --- | --- | --- | --- |
| BM25 | 12/12 | 1.00 | 1.00 |
| Vector | 11/12 | 1.00 | 1.00 |
| Hybrid | 11/12 | 1.00 | 1.00 |

Vector and hybrid return neighbors for the out-of-domain quantum-photosynthesis question.
This failed the expected-empty retrieval check. No threshold was fitted to make that check pass.
The numbered missing-document and date-filter checks returned no evidence as expected.
These queries are developer checks with exact identifiers and title-like wording, not a held-out benchmark.

## Live generated answers

| Question | Observed result | End-to-end time |
| --- | --- | --- |
| OC 186A consent | Three claims covering enablement consent, opt-out, and consent after device binding; S1/S2 citations. | 8.701 s |
| OC 201 primary/secondary users | Two definitions with S1 citations. | 2.951 s |
| Missing OC 999 | No evidence; abstained without calling generation. | <1 ms reported |
| Quantum photosynthesis | Six retrieved passages; model abstained with no claims. | 1.732 s |

Developer review compared the five emitted claims directly with the saved extracted passages:
the consent claims are supported by OC 186A pages 1–2, and the user definitions by OC 201 page 1.
This review checks support in the extracted text; it is not independent regulatory interpretation
or a new verification of the original PDF/OCR. Numerical claims were not part of these two positive cases.
Timing varies with model residency, workload and question length; these are individual observations.

## Application checks

- 14 unit tests passed, covering provenance, metadata filters, missing documents, reference navigation,
  citations, abstention, query instruction, context/output limits and truncated-output rejection.
- JavaScript syntax check passed.
- Browser generated the OC 186A answer using Hybrid + AI draft answer in 4.759 seconds.
- The S2 citation and Read page 2 opened the matching source reader with the consent clause.

## What remains unmeasured

Independent answer accuracy, page-level recall on a held-out set, multi-document completeness,
prompt-injection resistance, OCR-number handling, sustained concurrency and business time savings.
Do not present these smoke results as production or compliance accuracy.
