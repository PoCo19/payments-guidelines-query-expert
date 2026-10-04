# Technical architecture — v0.3

## Inputs and source authority

`data/index.json` contains 129 register entries, including unavailable/cancelled entries. `data/all_circular_pages.jsonl` contains 251 extracted pages from 107 documents. The engine indexes these structured inputs, not the combined Markdown plus individual Markdown simultaneously. Each source page retains extraction method and review metadata. PDFs remain in the configured original research pack.

## Chunking: clauses-v1

`ingestion.clause_chunks` works on one document at a time with pages sorted numerically. Line-start headings are detected from Markdown headings and a limited vocabulary (for example Key Guidelines, Payee PSP, UPI Application Provider and Remitter Bank). Numbered clauses and single-letter list markers split blocks. A heading-only block stays with its first clause. Text with no detected boundaries remains a block.

Long blocks use 220-word windows with 35-word overlap. Short clauses are not overlapped. Every chunk stays inside one page. Section identity can continue to the next page, and previous/next links can cross pages only within a document. All non-whitespace source words are retained; offsets address `page.text.split()` with an inclusive start and exclusive end. Source whitespace is normalized. No OCR correction, footer removal or table reconstruction occurs.

Chunk IDs use `document_id:pPAGE:v3cORDINAL`. They are deterministic for unchanged input, but ordinals can shift after text edits. Snapshot fingerprints identify the exact corpus; these are not permanent IDs across all revisions.

Metadata includes document ID, circular number, series, page, title, issue date, public-update date, source URL, extraction/review status, word span, section ID/heading, clause marker, previous/next IDs, chunker version, `heuristic_not_reviewed` status, family and feature IDs. The 916 chunks range from 3 to 220 words (median 44). A page-header fragment can inherit a preceding section label: treat the label as a hint and inspect the source.

## Feature and reference registry

Eight regex rules in `data/feature_rules.json` inspect document titles. Multiple labels are allowed. Chunks inherit their document labels; this is not clause-specific semantic classification. Features currently cover Tap & Pay, UPI Circle, AutoPay, NETC/NCMC, NRP/PRD, UPI LITE, credit on UPI and numeric UPI ID. No match means no label, not proof of irrelevance.

References come from imported `related_circulars`. The resolver matches circular number within the same series. One matching target resolves; multiple matching years remain ambiguous. The 54 edges currently comprise 32 resolved, 21 missing and one with unavailable text. Relation type is always `references`. Matching number occurrences identify candidate evidence pages only; they do not verify the meaning of the reference. Otherwise evidence is metadata-only. Nothing infers amendment, supersession or legal applicability.

SQLite snapshot tables:

| Table | Principal fields |
|---|---|
| metadata | key, value (full fingerprint) |
| documents | id PK, series, circular_number, issue_date, metadata_json |
| chunks | id PK, document_id FK, page, section_id, metadata_json |
| features | document_id FK + feature_id composite PK, basis, evidence |
| relationships | edge_id PK, from_id FK, target_id, relation, metadata_json |

Snapshots use `registry-<fingerprint-prefix>.sqlite3`. Writes are transactional in a unique temporary file, closed before atomic replacement (necessary on Windows). Existing snapshots verify the stored fingerprint. Full metadata remains in JSON columns for inspection. Reference-neighbor queries read the active snapshot; BM25 and other metadata lookups use in-memory objects. This is not a multi-user graph service.

## Vector store

Chroma 1.5.9 `PersistentClient` stores explicit vectors produced by local Ollama. `embedding_function=None` prevents automatic embedding selection. Telemetry is disabled. Collections use HNSW cosine distance, `ef_search=200`; returned distance is converted to similarity `1-distance`.

Each logical collection is keyed by the chunk/metadata fingerprint and embedding model name. Each build creates a unique physical collection. Its metadata records fingerprint, model name/digest, dimensions, count and ready flag. After all batches are written and counted, a temporary JSON manifest is atomically promoted to the active manifest. A failed build leaves the previous manifest active. Old collections and failed-build orphans are retained; automatic garbage collection is not implemented.

Startup validates ready state, fingerprint, model, record count and exact chunk ID set. Invalid/missing manifests require rebuilding. Each semantic query checks the installed model digest against the stored digest; a tag replaced with different weights cannot silently reuse vectors. Fingerprint changes require rebuilding. Concurrent builds are not a supported operational workflow; stop the server for maintenance.

## Retrieval and filtering

BM25 indexes title twice plus text, using lowercase alphanumeric tokens and a stop list (k1=1.5, b=0.75). Explicit `OC`/`circular` numbers restrict eligible documents and receive a lexical boost. Product, issue-date, known public-revision date and optional feature filters apply before selection. Unknown dates are excluded when a cutoff is set.

Ollama embeds the query with the configured retrieval instruction. Chroma receives the eligible document IDs as its filter and returns up to 100 candidates. Hybrid RRF merges the top 100 lexical and dense rankings with `sum(1/(60+rank))`. No cross-encoder reranker is implemented. Ordinarily at most two chunks per document are selected; an exact single-circular query with clauses-v1 can fill its requested passage count from that circular.

## Context assembly

| Scope | Selection |
|---|---|
| strict | Up to six direct matches; no expansion. |
| related | Four direct seeds, then bounded reference/feature/neighbor expansion. |

Related scope considers only the first two distinct seed documents for incoming/outgoing one-hop references, adding at most two new documents. Each contributes its best body-keyword-overlap passage. A zero-overlap passage can still be selected from an explicit reference; the inclusion label makes that visible. One additional same-feature passage may be selected if the question matches a feature rule and the passage has positive body overlap. Then up to three previous/next chunks in the seed's same section can be added.

All expansion respects product/date/revision/feature filters, availability and duplicate IDs. No seeds means no expansion. Total context is capped at ten passages and a configured 18,000-character estimate (text + title + 300 per passage). This is not tokenizer-exact accounting; other prompt/schema overhead is outside that estimate. Character budget is configurable between 2000 and 18000. Omitted context and unresolved references generate notes. Sources retain separate citations, inclusion reasons, via-document IDs and reference provenance; trace records seed/included IDs and budget use.

## Generation and API

Local Qwen3.5:9b receives only selected evidence plus instructions and a JSON schema. Configured limits: context 16384, output 3072, thinking false, timeout 300 seconds. Source metadata and inclusion reasons accompany passages. Generated citation IDs must exist in supplied evidence. Malformed/truncated responses and fabricated IDs are rejected. The model may abstain. Citation support still needs human review.

The HTTP server binds only `127.0.0.1:8765`. Endpoints: GET `/api/stats`, `/api/library`, `/api/document?id=...`, `/api/pdf?id=...`, `/api/evaluation?method=...`; POST `/api/answer` with query, method (bm25/vector/hybrid), series, cutoff, feature, scope (strict/related), mode (evidence/generate). Other failures are surfaced rather than silently replaced by an answer. The UI enables model controls based on configuration/index presence, not a continuous model-health check.

## Scope limits and references

No automated source refresh, effective-rule engine, reviewed amendment graph, semantic segmentation, reranker, comprehensive role ontology, public deployment or multi-user authentication. Neural retrieval can return irrelevant neighbors; no calibrated semantic relevance threshold is claimed. Current evidence budget and expansion caps can omit relevant clauses. OCR confidence is not factual confidence.

Implementation references: [Chroma collection configuration](https://docs.trychroma.com/docs/collections/configure), [explicit embeddings](https://docs.trychroma.com/docs/collections/add-data), [metadata filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering), [Ollama embeddings](https://docs.ollama.com/api/embed), [Ollama generation](https://docs.ollama.com/api/generate).
