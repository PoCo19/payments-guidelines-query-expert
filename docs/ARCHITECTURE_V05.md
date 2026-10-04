# v0.5: multi-product corpus and retrieval

Implemented and activated 25 September 2026. The detailed flow is in [HOW_IT_WORKS](../HOW_IT_WORKS.md). v0.4 retrieval, reranking and claim checking remain in place; this release extends source identity, import and filtering.

## Import and identity

`tools/import_products.py` reads the 12 supplied product inventories and Markdown files. It stages a new directory, hashes and copies inputs, writes structured records, checks unique document/page keys and listing totals, then renames the staging directory. It refuses an existing destination. It never modifies the Downloads source folders.

Canonical identity uses normalized source URLs. Existing overlaps retain their old IDs and reviewed text. New IDs use a 24-character SHA-256 source-identity suffix. Duplicate website listings become `source_listings` of one document; product memberships are a union of the listing products. Different URLs are not merged merely because their text matches. Alternative Markdown extractions remain in `import_variants` with paths and hashes.

The merged register has 1,921 records, preserving all 1,955 incoming inventory rows plus the prior register. There are 1,562 searchable documents, 4,826 page records and 14,060 chunks. Counts per product overlap because a document can belong to several products. The original 916 UPI-era chunks retain their IDs and text. Newer retained UPI circulars 186A and 227A are not lost merely because the new inventories are older.

Raw inventory number, title, year, fiscal year, source links, extraction status and generated timestamp remain available. New issue dates are null: fiscal year is not an issue date. Missing numbers display “Reference not verified.” The UI does not add an unconditional OC prefix to new records.

Two known title/body conflicts (`npci:rupay:726`, `npci:imps:533`) are quarantined as `needs_source_review`. Their source copies and register records remain, but their text is excluded from retrieval. The possible new extraction of old UPI 76B is retained as a candidate rather than silently replacing the prior failed-link state. ZIP attachments and unavailable records remain visible as gaps.

## Page and chunk provenance

Page markers determine the imported source-page number. Blank pages remain reader records and are excluded from embeddings. Thin pages are flagged. The unchanged deterministic chunker works inside each circular and page: heading/clause blocks, a maximum of 220 words, 35-word overlap only when splitting a long block. Each chunk has document ID, source page, exact word offsets, section ID and same-document previous/next pointers.

JSONL records are split on newline only. Real imported text contains Unicode line separators; Python `splitlines()` would split inside a JSON string and corrupt loading. A regression test covers this actual input.

Coverage separates `available_text_complete` from full source coverage. A summary is never marked complete if an extracted page is blank or the original PDF page count is unverified. A verified page count is an imported metadata assertion, not a new PDF-image audit.

## Retrieval and ambiguity

`product_scope.py` resolves product memberships, number normalization, fiscal years and explicit `document_ids` (up to four). Leading zeros normalize; letter suffixes remain distinct. A single product mentioned in the query may be inferred, while a selected product overrides inference. All filters apply to the selected document too.

Reference resolution considers unavailable records as well as searchable records. A repeated number across products/years cannot silently choose an arbitrary available circular. Ambiguous requests return candidate records and abstain before model generation. A missing comparison side also causes abstention. Library actions send stable IDs for summaries/comparisons, allowing two selected documents with the same number.

`adaptive_context.py` retains clause, summary and balanced-comparison routes. Summary/comparison bypass reranking and use up to 48 chunks under the same 18,000-character budget. Clause queries rerank up to 32 candidates and retain bounded direct/related context. Membership, fiscal-year, feature and cutoff filters apply through assembly.

18 product-scoped feature rules replace the candidate corpus's original eight-rule vocabulary. These are heuristics; participant roles still use the existing cue-based vocabulary. Imported cross-product relationship edges are not guessed from matching numbers or titles. Existing/reviewed reference edges are retained, and new relationships need source review.

## Storage and rebuild

`data/all-products-v1/` is selected by `config.json:data_dir`. It contains the structured register/pages, immutable source copies, review overlays, Chroma, and fingerprinted SQLite registries. `data/` still contains the preserved v0.4 corpus. Current review writes follow the selected dataset.

`embedding_cache.py` stores vectors in `data/embedding_cache.sqlite3`, keyed by model name, model digest and exact embedding input (title/heading/text). Completed batches are committed so an interrupted build can reuse them. Metadata changes still cause a fresh index snapshot, but unchanged embedding inputs can use cached vectors. This is embedding reuse, not an automatic live website refresh.

The actual build produced 14,060 vectors of 1,024 dimensions: 13,700 computed inputs and 360 reuse hits, in 926.78 seconds. Chroma publishes a new immutable physical collection via its existing atomic manifest only after a complete write. Model digest and corpus fingerprint must match. SQLite preserves ownership and reference relationships separately from similarity vectors.

Activation uses `tools/activate_corpus.py`: require current validation and live-check reports, a ready vector index, matching registry/corpus fingerprints and model digest, and unchanged copied-source hashes; atomically replace `config.json`. Restart the server to load the new snapshot. See [operations and rollback](MULTI_PRODUCT_IMPORT.md).

## UI and boundaries

The library has product/year/status filters and 50-record pagination. The reader exposes product memberships, reference labels, metadata quality, missing pages and PDF availability. Exact-document selection, ambiguity choices and coverage warnings are carried into research-note exports. New imported originals are not on disk: their links open the official PDF externally. Existing saved PDFs continue through the original guarded source-pack endpoint; adding other local PDF roots is deferred until originals are obtained.

No automatic date extraction, full table reconstruction, complete participant ontology, new PDF downloading/OCR, expert corpus certification, effective-rule reconstruction or authenticated public service is implied by this release.
