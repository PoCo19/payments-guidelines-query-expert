# v0.4 implementation map

Read `../HOW_IT_WORKS.md` for the complete flow and `ARCHITECTURE_V03.md` for the retained storage/chunking design. v0.4 adds the following modules:

| File | Responsibility |
|---|---|
| adaptive_context.py | Route inference/override, complete/partial coverage, balanced comparison, clause seeds and bounded expansion. |
| quality.py | Hash-bound overlays, append-only review validation, QA queue, feature and role enrichment. |
| reranker.py | Manifest integrity checks, cached ONNX CPU session, batched query-passage scoring. |
| claim_check.py | Numeric/OCR guards, local support judge, quote validation and withholding. |
| download_reranker.py | Explicit setup-time pinned download with SHA-256 checks. |
| evaluation/validate_v04.py | Frozen dataset validation, three current retrieval modes and historical baseline comparison. |
| evaluation/live_v04.py | Six live answer/abstention checks and contradictory-claim check. |
| tests/test_v04.py | Routing, filters, coverage, overlays, conflicts, real CPU reranker and claim-check regression tests. |

## API additions

POST `/api/answer` accepts `route`: auto/clause/summary/compare and boolean `rerank`. Existing query/method/mode/scope/series/cutoff/feature remain. Results add claim_checks, flagged_claims and route/coverage/reranker fields in retrieval_trace. Generation receives coverage notes. An unknown or incomplete required source suppresses summary/comparison generation.

GET `/api/review` returns page flags, metadata gaps and annotations. POST `/api/review` validates and atomically appends an annotation. Accepted records take effect after rebuild/restart. POSTs retain the existing same-origin and payload-size checks. ReviewStore serializes writes within one server process; do not run two app servers writing the same annotations concurrently.

Accepted corrections are applied to deep copies before chunking. Raw input files are untouched. Word spans belong to effective page text. Labels, metadata and accepted reference changes participate in the registry fingerprint; chunk content and chunk metadata determine the vector fingerprint. Run the rebuild command after accepted changes to publish matching snapshots, then restart; changes confined to registry-only fields do not alter the vector fingerprint.

## Configuration

`adaptive_retrieval`, `reranker_enabled`, `claim_check_enabled`, `review_overlays` enable v0.4 behavior. Reranker files are resolved from project-relative `reranker_path`. Model files are verified at session load; a missing/corrupt model errors explicitly, and the UI allows reranking off for an experiment. No hidden network fallback or cloud model exists.

Reranker input combines query with title, section heading and passage, truncating at 512 tokenizer tokens; batches of eight, four CPU intra-op threads. Output logits are relative ranking scores. It can neither retrieve a candidate absent from the first stage nor establish truth.

Each support check uses local Qwen, temperature zero, the configured context length and up to 650 output tokens. Claims are checked sequentially, increasing latency with answer length. A truncated/malformed check withholds that claim. Typography normalization permits curly/straight quote or dash differences; it does not change OCR words, numerical values or missing content.

## Reproduce and restore

Existing installation: open Ollama, `run.cmd`, browse localhost:8765. New environment: `setup.cmd` installs the pinned dependency lock and downloads the pinned reranker; source/model pack paths in config must exist. Then pull the two configured Ollama models and run `run.cmd embed`.

`run.cmd test`: automated tests. `run.cmd validate`: 50-case retrieval comparison. `run.cmd live-check`: slower generation checks. `run.cmd evaluate`: historical 12-case smoke retrieval evaluation, retained separately. `run.cmd reranker`: verify/download model files.

Before v0.4, application/config/UI/tests/docs were preserved under `versions/v0.3.0/`. To restore, stop the server and copy those files back into the project root, preserving data and model artifacts. v0.3 config disables the overlays/new routes. Run its embed command to publish a matching snapshot, then restart. Do not launch the backup directory directly: it is not a standalone copy of the corpus. Old fingerprinted Chroma/SQLite snapshots and legacy vectors are retained.

## Limits retained

No automatic new-document ingestion, graph database, table reconstruction, full feature ontology, authenticated review, current legal applicability engine or production hosting. Reviewed dates and relationships are stored but are not a rule-conflict resolution engine. A source review can be wrong; the software validates provenance and structure, not the reviewer's judgment.
