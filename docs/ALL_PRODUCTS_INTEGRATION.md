# All-product NPCI pack: audit and incorporation plan

**Historical pre-implementation assessment.** Implemented results and remaining boundaries are now in [ARCHITECTURE_V05.md](ARCHITECTURE_V05.md) and [VALIDATION_V05.md](VALIDATION_V05.md). The inspection-only status below describes that earlier stage.

Audited 25 September 2026. Sources: `C:\Users\Admin\Downloads\circulars\circulars` and `C:\Users\Admin\Downloads\circulars\inventory`. This is a local audit, not a live NPCI website reconciliation. The supplied inventories were generated between 9 and 15 September 2026, while the current project snapshot extends through 22 September. Their archival year fields span 2009-2026; these are not verified issue dates.

## Findings

| Product folder | Inventory entries | Markdown files | Page sections | Empty sections |
|---|---:|---:|---:|---:|
| aeps | 110 | 97 | 230 | 3 |
| bhim-aadhaar | 2 | 2 | 6 | 0 |
| cts | 248 | 235 | 640 | 0 |
| e-kyc-setu-system | 4 | 3 | 7 | 0 |
| e-rupi | 5 | 3 | 14 | 0 |
| imps | 143 | 128 | 298 | 29 |
| nach | 420 | 382 | 1194 | 5 |
| netc | 56 | 53 | 227 | 2 |
| nfs | 449 | 246 | 831 | 1 |
| others | 1 | 1 | 2 | 0 |
| rupay | 240 | 224 | 959 | 22 |
| upi | 277 | 245 | 651 | 6 |

Totals: **1,955 register entries, 1,619 Markdown files and 5,059 page sections**. All extracted entries have matching files, no orphan Markdown files were found, page-marker sequences are continuous, and supplied non-null page counts match the markers. These checks establish structural consistency, not correct transcription.

The remaining 336 entries are 281 without public PDFs, 54 skipped ZIP attachments and one extraction failure (NFS OC 139 annexure). Retain all of them as availability records. The ZIP entries may contain relevant circular annexures/specifications and must not be silently treated as complete.

Text-quality findings: 68 empty page sections across 43 documents; 122 sections with fewer than 15 word-like tokens across 67 documents (includes empty sections); 482 extracted files lack a PDF page count to independently compare with their Markdown sections. No original PDFs are present in this supplied circulars tree. All files contain some text, but some individual pages are blank. `extracted` therefore does not mean every page is usable. The is_scanned flag is not a page-level extraction method or OCR confidence score.

306 inventory rows have no structured circular number. Structured issue dates are not supplied in the inspected schema. Preserve fiscal year/year labels separately, with null issue dates until source-based extraction/review. Do not derive January 1 from a fiscal year. A title can contain several dates, including programme or effective dates.

## Overlap and quality examples

- 106 current register records match by exact normalized source URL. Keep existing document IDs, source-page text and review overlays for converted documents; add the new inventory provenance and product memberships. Existing source corrections and the 50-case evaluation depend on these IDs/text hashes.
- OC 186A and OC 227A are existing converted documents without matching source URLs in this older pack. Preserve them. This pack must not replace the current corpus wholesale.
- Existing OC 76B (2024) was a failed public link; a candidate extracted Markdown now exists at inventory key npci:upi:1803. Review it against the PDF before marking that gap recovered.
- 27 source-URL duplicate groups contain 57 additional listing rows. Several compliance circulars are listed under AePS, CTS, IMPS, NACH, NFS and UPI. Store one canonical document with several product memberships and all listing records, so these copies do not crowd out different evidence.
- 43 identical extracted-body groups exist; some span different source URLs. Treat these as duplicate/review candidates, not automatic proof that the PDFs or legal records are interchangeable.
- AePS OC 33 (2018-19) has an empty first page although the inventory says extracted. Page 2 starts the response-code annexure. Preserve page numbering and flag missing text; do not renumber annexure page 2 as source page 1.
- RuPay inventory ID 726 lists a December 2015 Hi Flyer programme title, while its Markdown body describes a September 2016 winners addendum. This apparent title/body mismatch requires original-PDF verification.
- IMPS inventory ID 533 uses circular number 2I and FY 2011-12, while the listing/body indicate Circular 2 and FY 2010-11. A separator may have entered the parsed number. Keep raw values and review the canonical reference.

## Recommended incorporation

### 1. Add a staged, repeatable inventory importer

Copy the input inventories/Markdown into a versioned project source area or record their hashes and explicit source roots. Do not depend on mutable Downloads paths for a released corpus. Parse each inventory item and its referenced Markdown. Split text on `<!-- Page N -->`; exclude the Markdown title and metadata preamble from evidence chunks. Feed each page into the existing clause chunker, preserving original page numbers and Markdown bytes/hash.

Keep empty pages as page-level availability records but do not embed them. Preserve non-empty flagged pages with review metadata; a summary must distinguish text coverage from complete PDF coverage. The current included-chunk coverage would otherwise show complete even when the source extraction omitted pages. Repair this before publishing the expanded corpus.

### 2. Extend document identity and provenance

Separate the canonical document from its website listing records. Keep existing IDs on verified overlap. New document IDs should derive from a durable source identity, not just circular number. Store product membership as an array and keep the native circular series/reference separately. For same-URL variants, compare available hashes/text and preserve extraction variants rather than silently replacing existing reviewed text. Do not merge different URLs solely because their text matches.

Keep raw circular number, normalized reference, financial year, issue date, date basis, listing URL, PDF URL, inventory ID, generated_at, file hash, page count provenance and extraction/review status. Original PDFs are missing from this new pack; use existing saved PDFs for overlap and obtain originals for new documents before claiming verified page/metadata correctness.

### 3. Adapt retrieval and the reader for multiple products

The current UI creates its product list dynamically, but engine filters use one `series` string per document. Add membership-aware filtering, and show the document's own series/reference separately from its product memberships. Stop displaying an unconditional `OC` prefix: RuPay/NFS/CTS and compliance references vary.

Resolve circular references using product/series + number + year or stable document ID. Circular 13 exists in many products and years. Ask for product/year when ambiguous rather than combining unrelated rules. Product-specific features and participant vocabularies should replace the current eight UPI-focused rules as coverage expands. Cross-product references need explicit source anchors; the same number is not a relationship.

Make snapshot dates and coverage counts data-driven instead of the currently hard-coded 2023-2026 window. The saved-PDF endpoint assumes one source-pack root; extend it to a validated per-source mapping, and show when only an external PDF link is available.

### 4. Publish a new index snapshot with a rollback path

Use the existing Chroma + SQLite architecture; another vector database is not required. The dry run produces about 14,647 chunks from the new pack BEFORE deduplication, quality decisions and merging. This is an index-size estimate, not the final number. More documents do not require sending every document to Qwen or automatically raising the context limit.

Build a separate candidate corpus/index, preserve the active v0.4 snapshot, test it, then switch the active dataset path. Add incremental hashing/caching so later imports embed only changed text. Retrieval should still select a bounded set of relevant passages; measure recall/latency as the candidate pool grows.

### 5. Validate before switching the application

Retain the existing UPI regression suite. Add product-balanced questions, same-number/different-product cases, repeated circular numbers across years, unavailable ZIP/annexure cases, partial-page extraction, duplicate listings and metadata contradictions. Confirm product filters work on all memberships, chunk links never cross documents, citations retain PDF page numbers, and existing review hashes remain valid. Run a small multi-product pilot before embedding the entire merged corpus.

## Mapping to current data

| Supplied inventory field | Target treatment |
|---|---|
| product / source-page folder | product_memberships; retain listing product |
| id | source_inventory_id, namespaced by product |
| title | listing_title; do not assume PDF subject matches |
| circular_number | raw number; reviewed normalized reference separately |
| fy / year / year_label | fiscal/archive metadata, not issue date |
| pdf_url / file_url | original source link; distinguish PDF and ZIP |
| extraction_status | availability plus text-review state |
| output_filename | hashed source Markdown artifact |
| Page N markers | source_page; preserve blank-page gaps |
| is_scanned | imported document hint; page extraction method unknown |
| generated_at | inventory snapshot timestamp, not current-site freshness |

## Deliverables and execution status

`reports/all_products_audit.json`: per-document audit, structural findings, overlaps and duplicates.

`reports/all_products_merge_preview.json`: grouped candidate identity/product mappings and proposed actions. It is a dry-run manifest, not an engine-ready corpus. Gaps without a PDF URL have no strong merge key and may duplicate current missing records until metadata review.

`tools/audit_product_pack.py`: rerunnable read-only audit (`.venv\Scripts\python.exe -X utf8 tools/audit_product_pack.py`).

`tools/preview_product_merge.py`: regenerate the reviewable merge manifest from the audit.

The source folders and active project data/index/embeddings/configuration were not changed. No new corpus was embedded or promoted during this inspection. Next implementation phase: staged importer + membership-aware identity/filtering + partial-source coverage handling, followed by a validated index build.

Dry-run grouping summary: {"source_inventory_rows": 1955, "source_groups": 1898, "actions": {"candidate_new_text": 1457, "register_gap_only": 335, "preserve_existing_text_add_memberships": 105, "candidate_fill_existing_gap": 1}, "identical_text_groups_with_different_urls": 23}
