# Intake and model-runner validation — 9 October 2026

Implemented: `tools/document_pipeline.py`, `ingest.cmd`, optional provenance in retrieved evidence, saved intake PDF access, and `evaluation/benchmark_models.py`. The active corpus remains `all-products-v1`; no RBI text or synthetic test content was added to it.

## Automated checks

The Python regression suite passed **206 tests**, including 17 intake tests and five model-runner tests. JavaScript answer-rendering/export checks and frontend syntax checks passed. Tests cover:

- Immutable originals and live-config preservation during preparation.
- Malformed/duplicate Markdown page markers and substantive preambles.
- Unicode line separators inside JSONL text.
- Blank/scanned PDF detection, thin-page quarantine and explicit partial-source acceptance.
- Duplicate IDs/content, unchanged intake, guarded revisions and no invented supersession links.
- Real Chroma storage with mocked model responses; resumable embedding reuse.
- Embedding failure, source tampering, stale reviews and changed model digests preventing publication.
- Activation/rollback and prevention of rebuilding an active release.
- Frozen generation requests, streamed timing capture, missing completion and invalid citation IDs.

## Real local-model integration check

An isolated synthetic corpus used the installed `qwen3-embedding:0.6b` and real Chroma. Release 1 computed one vector. Release 2 reused that vector and computed one new vector. Both had 1,024-dimensional embeddings.

Verified a vector query restricted to the new PDF document, source-reader metadata, and byte-identical PDF delivery through `/api/pdf`. Activation and both rollback steps restored the isolated original configuration. The real project's config hash stayed unchanged and its **14,060 chunks** still loaded with a ready index.

Local evidence: `reports/intake-live-20261009T083832Z/smoke_report.json`. The smoke report is included with the handoff. Its synthetic source files and generated test corpora remain local and are not needed to run the regression tests; this is not regulatory evidence or answer-quality evaluation.

## Model timing observation

The installed Qwen 3.5 9B completed one frozen UPI Circle prompt twice: 18.839 seconds including model loading, then 8.455 seconds for the repeated warm request. Each response generated 464 tokens from a 4,940-token prompt. Structural/citation-ID checks passed; those checks do not assess factual support. Model digest stayed unchanged. The run used an 8,192 context limit and 1,024 output limit without changing live configuration.

Local raw prompt, outputs, timings and residency: `reports/model-benchmarks/20261009T083452564728Z/`. This is generation-only timing, with repeated-prompt caching on the second request, and excludes retrieval and claim checking. No larger model has been measured.

## Remaining work

Acquire and review complete RBI originals selected in the [source map](RBI_PAYMENTS_SOURCE_MAP.md), trial the candidate preview, and create reviewed RBI-specific questions. Add dedicated applicability/issuer filtering and source-supported amendment relationships as the corpus expands. Browser uploads, website synchronization, OCR automation, release pruning and historical effective-rule reconstruction are not part of this intake version. Submission slides/reports and the historical 50-question evidence were not rewritten in this implementation turn.
