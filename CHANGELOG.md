# v0.5.1 — Context-sensitive answer formatting

Replaced the fixed bullet renderer with validated paragraph, bullet and ordered-step blocks over existing checked claims. Added Automatic/Paragraphs/Bullet points/Mixed control, generation guidance and layout schema, stable claim indices across filtering, safe fallback, inline citations and matching Markdown export. No second rewriting model call or corpus rebuild. 103 Python tests and renderer checks pass; three local-model formatting cases exercised. Backed up v0.5.0 before edits. See docs/ANSWER_FORMATTING.md.

# v0.5.0 — 25 September 2026

Activated multi-product corpus: 1,921 register records, 1,562 searchable documents, 4,826 page records and 14,060 vectors. Added audited staged import, source hashes/variants, canonical identity and memberships, stable document selection, fiscal-year filters, ambiguity abstention, partial-source warnings, library pagination, product-scoped features and resumable embedding cache. Preserved original UPI chunks/reviews and quarantined two known conflicts. Added guarded activation and rollback, 34 new tests (93 total), expanded validation, live checks and current documentation/screenshots.

Remaining source-quality and answer-evaluation work is recorded in PROJECT_STATUS.md; no expert-accuracy or live-website completeness claim is made.

---

## 2026-09-25 - v0.4.0

Implemented the six RAG improvements: frozen evaluation and review worksheet; source QA overlays/workbench; adaptive clause/summary/comparison retrieval; pinned local ONNX reranker; clause/role labels and relationship review; per-claim checks with quoted evidence and withholding. Rebuilt 916 vectors, passed 59 tests and six live cases plus a contradiction check. Browser/source QA caught metadata-attribution and quotation-normalization issues; regression checks added. Updated project flow, operating/review/architecture/validation docs and shareable illustrated PDF. Full-corpus and independent evaluation review remain pending, not represented as completed expert verification.

# Changelog

## Context tuning — 2026-09-24

Raised configured generation context to 16,384, output cap to 3,072 and evidence budget to 18,000 characters after testing on the local 12 GB GPU. Detailed-answer and abstention checks completed; previous settings and results preserved in evaluation/. No embedding change.

## 0.3.0 — 2026-09-24

Added persistent Chroma vectors and SQLite registry snapshots; migrated the legacy index with 24/24 sampled ranking matches. Built 916 clause-aware chunks preserving circular/page ownership and exact word spans. Added bounded related context, title-feature filters, inclusion provenance and an inspectable chunk reader. Preserved v0.2 rollback materials. Validated 35 tests, six live answers and desktop workflows; documented algorithms, setup, limitations and rollback.

## Startup fix — 2026-09-24

Added run.cmd to start Python directly on Windows without changing PowerShell execution policy. Updated the beginner and technical guides to use this launcher.

## 0.2.0 — 2026-09-24

Connected installed Qwen3.5 and Qwen3 embedding models; built 428 passage vectors; configured query instructions, 8192-token answer context, thinking disabled, bounded output and longer model timeout. Added truncated-answer rejection, model-free empty-filter handling, browser generation progress and a choice of retrieval methods in Experiments. Validated live cited answers and abstention; recorded semantic retrieval failure for an out-of-scope question. Added beginner guides, a review template and reproducible live-model checks. Fourteen unit tests passed.

## 0.1.0 — 2026-09-23

Initial local prototype: page-bounded BM25 retrieval; metadata filters; full circular register and reader; family timelines and recorded references; source PDF access; evidence-note export; optional local Ollama embeddings, hybrid retrieval and structured generation; unit tests and transparent retrieval smoke evaluation.
