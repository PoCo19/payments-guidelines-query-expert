# Validation report - v0.4.0

Executed 25 September 2026 on this Windows laptop. All six RAG improvements are implemented. Source/evaluation review remains a continuing human activity.

## Automated checks

59 tests passed, including the original 35 plus 24 new routing, coverage, review, reranker and claim-check checks. Real ONNX CPU inference and Chroma storage are exercised; most generation failure cases use deterministic mocks. Python compilation, JavaScript syntax and pip dependency checks passed. Model assets passed their SHA-256 integrity checks. The current Chroma snapshot has 916 vectors and reports Ready.

## Frozen retrieval comparison

50 AI-assisted questions, 55 proposed source anchors. All cases await independent review. The baseline was captured before v0.4 changes. The JSON dataset hash is verified by the runner; no cases were tuned after freezing. Baseline and current pipelines differ in routing, budgets and overlays, so gains cannot be attributed solely to the reranker.

| Run | Source anchors found | Negative cases with no evidence | Median / p95 retrieval time |
|---|---:|---:|---:|
| v03_bm25 | 44/55 | 5/6 | 0.0 / 1 ms |
| v04_bm25 | 55/55 | 6/6 | 0.0 / 0 ms |
| v04_bm25_reranked | 55/55 | 6/6 | 40.5 / 128 ms |
| v04_hybrid_reranked | 55/55 | 5/6 | 159.5 / 294 ms |

Anchor recall is an exact phrase retrieval measure, not answer accuracy. The reranker did not improve this set's aggregate anchor recall beyond adaptive BM25; its value needs harder independently authored questions. Hybrid still returns unrelated semantic neighbours for one negative query. Generation abstained on that query in the live check. The comparison table separates empty retrieval from generated abstention.

## Live local-model checks

| Case | Supported claims | Withheld claims | Abstained | Total time |
|---|---:|---:|---|---:|
| clause | 1 | 0 | False | 5.46 s |
| currency | 1 | 1 | False | 7.92 s |
| summary | 14 | 0 | False | 60.25 s |
| compare | 16 | 0 | False | 71.05 s |
| missing | 0 | 0 | True | 0.00 s |
| outside | 0 | 0 | True | 1.40 s |

Summary input covered all 14 OC 186A chunks. Comparison input covered all 12 OC 186 chunks and 14 OC 186A chunks. This does not certify answer completeness. The final currency run withheld one otherwise plausible per-transaction-limit statement because the judge's quotation did not match the source. This is a visible false-withholding cost of conservative checking. The source reader still shows the corrected figures.

The separately injected claim “No consent is required before enabling the feature” was withheld against evidence requiring explicit consent. Generation and judging use the same local Qwen model; passing these checks is not independent proof. Repeat runs can vary even at temperature zero.

## Browser and source inspection

Verified v0.4 rendering; summary coverage 14/14; source review queue and fingerprint loading; accepted correction display alongside unchanged raw extraction; conditional review fields; claim support details and evidence reader. Captured current screenshots in docs/screenshots/v04-*.png. No fake human approval was saved to the production annotation file; writes/conflicts are tested in temporary stores.

Original PDF images checked: OC 186A pages 1-2 and OC 201 page 2. Five currency corrections, one issue-date annotation, three feature/role annotations and one reference annotation are accepted with assistant_source_checked provenance. There are 213 automatically flagged review-candidate pages and 21 register metadata gaps. Flags are not error counts. Full-corpus human review remains pending.

## Fixes caught during validation

- Circular-number attribution initially failed numeric guards because metadata was omitted; added citation metadata and a regression test.
- Curly apostrophes versus straight apostrophes caused false quotation failures; added typography-only normalization and tests that still reject changed OCR words.
- Conflicting accepted corrections could previously poison the next index build; simulate accepted overlays before atomically persisting a review.
- Corrected UI text encoding and exposed all review queue entries, metadata gaps, raw text and review provenance.

## Reproduce

Open Ollama. Run `run.cmd test`, `run.cmd validate`, then `run.cmd live-check`. The last two need local models and a matching vector index. Live output overwrites its current result report; copy it first if preserving a comparison. Independent review uses evaluation/independent_review.csv. Dataset changes require a new version/hash and new baseline, not silently replacing the frozen set.

Evidence: evaluation/v04_retrieval_results.json, evaluation/v04_live_results.json, evaluation/v04_adversarial_check.json, evaluation/rag_cases.json, models/reranker/manifest.json.

## Shareable document QA

The five-page v0.4 flow PDF includes three current application screenshots. Rendered every page with Poppler, inspected all pages, corrected a page-3 footer overlap, and rechecked the revised page. Confirmed five pages and page-number footers using pypdf. The PDF is output/pdf/Circular_Intelligence_Project_Flow_v04.pdf; its reproducible authoring script is docs/build_flow_pdf.py.
