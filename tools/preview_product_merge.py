"""Produce a reviewable merge manifest without changing active retrieval data."""
import collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
r=json.loads((ROOT/'reports/all_products_audit.json').read_text(encoding='utf-8'));old=json.loads((ROOT/'data/index.json').read_text(encoding='utf-8'));oldby={d['id']:d for d in old}
groups=collections.defaultdict(list)
for row in r['rows']:groups[row['source_url'] or row['key']].append(row)
known={'npci:rupay:726':'Listing title/year and extracted body describe different dates/subjects; verify original PDF before selecting metadata or text.','npci:imps:533':'Inventory/Markdown number 2I appears to include a listing separator; body reads Circular 2. Fiscal-year labels also differ. Verify PDF.'}
manifest=[]
for key,rows in groups.items():
 existing=sorted({i for row in rows for i in row['existing_document_ids']});converted=[i for i in existing if oldby[i]['availability']=='converted'];candidates=[row for row in rows if row['file_exists']]
 action='preserve_existing_text_add_memberships' if converted else 'candidate_fill_existing_gap' if existing and candidates else 'candidate_new_text' if candidates else 'register_gap_only'
 stable_id=existing[0] if len(existing)==1 else 'npci-source-'+hashlib.sha256(key.encode()).hexdigest()[:24]
 manifest.append(dict(proposed_document_id=stable_id,action=action,existing_document_ids=existing,source_url=rows[0]['source_url'],product_memberships=sorted({row['product'] for row in rows}),source_inventory_keys=[row['key'] for row in rows],text_candidates=[dict(inventory_key=row['key'],path=row['markdown_file'],sha256=row['markdown_sha256'],flags=row['flags'],empty_pages=row['empty_pages'],thin_pages=row['thin_pages'],known_review_note=known.get(row['key'])) for row in candidates],requires_identity_review=len(existing)>1,requires_source_review=any(row['flags'] or row['key'] in known for row in rows),issue_date_policy='Preserve existing verified metadata; new inventory fiscal year is not an issue date.',publication_state='preview_only'))
bykey={x['key']:x for x in r['rows']}
body_different_urls=[ids for ids in r['identical_body_groups'].values() if len({bykey[k]['source_url'] for k in ids})>1]
report=dict(note='Dry-run candidate mapping only. Not an import or an active corpus. URL equality is a merge candidate, not proof of identical PDF version; new same-body/different-URL groups require review. No-PDF items lack strong identity keys and may duplicate retained gaps.',summary=dict(source_inventory_rows=len(r['rows']),source_groups=len(manifest),actions=dict(collections.Counter(x['action'] for x in manifest)),identical_text_groups_with_different_urls=len(body_different_urls)),retain_existing_documents_without_url_match=r['existing_not_url_matched'],known_review_cases=known,identical_text_groups_with_different_urls=body_different_urls,documents=manifest)
assert len({x['proposed_document_id'] for x in manifest})==len(manifest)
assert sum(len(x['source_inventory_keys']) for x in manifest)==len(r['rows'])
(ROOT/'reports/all_products_merge_preview.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(report['summary'],indent=2))
text='''# All-product NPCI pack: audit and incorporation plan

Audited 25 September 2026. Sources: `C:\\Users\\Admin\\Downloads\\circulars\\circulars` and `C:\\Users\\Admin\\Downloads\\circulars\\inventory`. This is a local audit, not a live NPCI website reconciliation. The supplied inventories were generated between 9 and 15 September 2026, while the current project snapshot extends through 22 September. Their archival year fields span 2009-2026; these are not verified issue dates.

## Findings

| Product folder | Inventory entries | Markdown files | Page sections | Empty sections |
|---|---:|---:|---:|---:|
'''
for p in r['products']:text+=f"| {p['product']} | {p['listed']} | {p['available_markdown']} | {p['pages']} | {p['empty_pages']} |\n"
text+='''
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

`tools/audit_product_pack.py`: rerunnable read-only audit (`.venv\\Scripts\\python.exe -X utf8 tools/audit_product_pack.py`).

`tools/preview_product_merge.py`: regenerate the reviewable merge manifest from the audit.

The source folders and active project data/index/embeddings/configuration were not changed. No new corpus was embedded or promoted during this inspection. Next implementation phase: staged importer + membership-aware identity/filtering + partial-source coverage handling, followed by a validated index build.
'''
text+=f"\nDry-run grouping summary: {json.dumps(report['summary'],ensure_ascii=False)}\n"
(ROOT/'docs/ALL_PRODUCTS_INTEGRATION.md').write_text(text,encoding='utf-8')
