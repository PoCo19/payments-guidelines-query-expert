# 4 October 2026 — Midterm slide refinements

Reworked roadmap into indicative weeks, implementation tasks and deliverables. Explained preliminary retrieval metrics and their limits; source-anchor counts do not measure answer accuracy. Replaced the document-count panel with actual chunking and indexing steps verified in ingestion.py. Added an enlarged genuine local response to a shop card-machine question with question text visible. Preserved a second, unfocused response as a finding. Updated the three-page report, speaker notes, scope and share bundle. No model, corpus, retrieval configuration or storage changes.

# 4 October 2026 — Query Expert clarity revision

Reframed the active RAG UI and midterm package as Payments Guidelines Query Expert, with NPCI as the initial corpus. Prioritised the question flow, grouped technical controls, simplified repeated notices, and consolidated the roadmap. Rebuilt eight slides and a three-page report, matching PDFs and narration. Native renders reviewed; fresh browser journeys passed. No corpus, model or storage changes. Team identity and recording remain pending. See output/midsem/START_HERE.md.

# 2026-10-03 — payments RAG mid-sem closure

Repositioned the RAG landing and current entry documents around payments research, explicitly starting with NPCI. Removed the workflow navigation shortcut without altering its implementation or data. Added a timestamped same-snapshot four-variant evaluation runner, two metric regression tests, six saved live scenarios and a browser journey covering sources, filtering, summary, comparison, export, ambiguity, missing evidence, partial extraction and simulated model-outage recovery.

All variants retrieved 55/55 proposed anchors. BM25 returned no evidence for 6/6 negative cases; semantic variants did so for 5/6. No recall benefit from reranking was demonstrated. Preserved the limitation, single-pass timing caveat and human-review-pending status. Built an eight-slide reference-inspired presentation and four-page report with editable originals, PDFs and team narration. Team metadata, recording and submission remain pending. Full evidence and reproduction details are in MIDSEM_VALIDATION.md.

## 2026-10-03 - UPI Feature Workspace V2.0.0

Reframed the product for existing-feature reviews, feature changes and new launches. Rebuilt navigation and screens around the actual work order; added next-step guidance, local form errors, source previews, unsaved-edit protection and actionable stale-dialog recovery. Added exact-name/revision workspace deletion and result suppression for deleted jobs, bounded PDF/DOCX/Markdown/text upload previews, atomic batch drafting, an internal transaction-rule register and structured rule-by-rule assessment. Preserved V1 records and a pre-change backup; legacy controls are not reinterpreted as transaction rules.

Validation: 168 Python tests, existing answer-rendering JavaScript checks, a complete isolated V2 browser journey including all workspace types, role recovery and concurrent deletion, plus five real Qwen workflows. Screenshot review led to mobile navigation and notification placement fixes. Browser validation exposed and fixed a stale-delete-dialog reload race. Current product, user, implementation and validation documentation now describe V2.

## 2026-10-03 - Feature Launch Orchestrator V1.0.0

Added a separate local launch application on port 8766 with persistent SQLite state, reviewed and cited facts, four local-model workflows, explicit template demonstrations, partner/control registers, version-bound reviews, task dependencies, readiness gates, launch decisions and Markdown exports. The evidence picker imports selected UPI passages without rebuilding the research corpus or opening Chroma. Source-span selection fixed quotation paraphrasing exposed by live model tests. Scoped content invalidation and transitive task reopening were verified separately. Late generation cannot overwrite newer inputs or reviews.

Validation: 143 Python tests, existing JavaScript rendering checks, a complete isolated Edge browser journey and all five real Qwen3.5 workflows passed. Added a concise shareable product brief, beginner demonstration, technical/operations guide and validation record. This remains a local capstone with self-reported roles and evidence, not an authenticated production workflow. Original RAG v0.5.1 and its core-guide PDF remain separate.
## 2026-09-25 - all-product pack assessment (no runtime migration)

Read all 12 supplied product inventories and validation reports; audited 1,619 Markdown files / 5,059 page sections against 1,955 entries. Recorded 68 empty sections, missing structured dates/numbers, source-URL overlaps and title/reference review cases. Created repeatable audit and merge-preview scripts, reports and ALL_PRODUCTS_INTEGRATION.md. Merge preview retains all inventory rows and existing unmatched circulars, preserves converted UPI text/review IDs, and identifies one possible recovered gap. Active data, embeddings, source folders and runtime configuration remain unchanged. Source inventories date from 9-15 September; live-site completeness was not checked.

## 2026-09-25 - v0.4.0

Implemented the six RAG improvements: frozen evaluation and review worksheet; source QA overlays/workbench; adaptive clause/summary/comparison retrieval; pinned local ONNX reranker; clause/role labels and relationship review; per-claim checks with quoted evidence and withholding. Rebuilt 916 vectors, passed 59 tests and six live cases plus a contradiction check. Browser/source QA caught metadata-attribution and quotation-normalization issues; regression checks added. Updated project flow, operating/review/architecture/validation docs and shareable illustrated PDF. Full-corpus and independent evaluation review remain pending, not represented as completed expert verification.

# Development log

## 2026-09-24 — v0.3 implementation

Preserved v0.2 before changing storage or chunking. Installed Chroma in a project virtual environment and pinned its dependencies. Separated ingestion, registry, vector storage and context assembly from the HTTP/engine module.

Migrated the original 428 embeddings first, preserving the legacy chunk fingerprint. Used identical query vectors for JSON/Chroma comparisons; all 24 sampled vector/hybrid rankings matched. Then rebuilt 916 clause-aware embeddings under a new fingerprint.

Kept each chunk page-bounded and source-attributed. Recognized headings attach to their first clause. Long blocks use 220-word windows with 35-word overlap; page-to-page relationships remain explicit links. Kept OCR noise to avoid silently deleting source words. Added word-coverage and offset tests across the whole corpus.

Added a SQLite snapshot for documents, chunks, title features and imported references. An initial Windows file replacement failed because a SQLite connection was still open. Fixed by explicitly closing connections before replacement and revalidated the migration/build. Unique temporary filenames avoid temporary-path collision during snapshot creation.

Published Chroma collections via atomic manifests to protect the last complete snapshot from build failures. Tested failed collection creation and failed upsert. Added incomplete-record and corrupt-manifest handling, model-digest checks and a digest guard for legacy migration.

Bounded related context to one reference hop, limited related documents, optional same-feature passage and section neighbors. Filters and provenance apply throughout. Missing references are reported without fabricated text. Broadened explicit circular-number parsing so unknown suffixes/long numbers do not silently become general searches.

Added scope/feature controls, source inclusion labels, retrieval trace, chunk/edge audit panels and metadata in exported notes. Browser review found a long-line overflow in the new chunk panel; added wrapping and verified no horizontal overflow. In-app download observation timed out; Chrome export was successfully downloaded and inspected.

Updated all primary guides and added technical architecture, migration/rollback, validation and a documentation map. Preserved the earlier PDF as a clearly labelled v0.2 artifact. Final checks: 35 tests, 24 migration comparisons, three retrieval evaluations and six live answer requests. No held-out answer-quality gain is claimed.

## 2026-09-24 — context tuning

Raised configured generation context/output/evidence limits to 16384/3072/18000 after checking local RAM/GPU and running before/after plus abstention checks. Preserved original settings and raw token metrics. A stale server survived the first stop attempt; terminated its verified process tree and confirmed the replacement through a live HTTP answer and Ollama context report. See CONTEXT_TUNING.md. No embedding rebuild or global Ollama setting change was required.



## 2026-09-25 — v0.5 multi-product implementation

Staged all-products-v1 independently of the old corpus, preserving 1,955 inventory listings, 1,619 source Markdown files, old reviewed UPI chunks and newer retained entries. Same-source URL groups use canonical identities with multiple product memberships; different URLs remain distinct even when text matches. Kept unavailable ZIP/PDF records and blank-page records, quarantined two known source contradictions, and withheld the unverified 76B recovery candidate.

Added membership/fiscal-year filtering and exact-document selection. Repeated references now abstain with candidates instead of guessing; source coverage includes extraction gaps and unverified page counts. Added 18 product-scoped feature rules. Cross-product relationship inference and broader participant ontology remain review work.

Built 14,060 embeddings using local Qwen, caching 13,700 computed inputs with 360 reuse hits in about 15.4 minutes. Verified source hashes, SQLite integrity, vector ownership, model digest and corpus fingerprints before atomic configuration activation. Old corpus and versions/v0.4.0 remain intact.

Real-data testing found Unicode line separators breaking JSONL reads; fixed to split records only on newline. Browser testing found duplicate availability options and invalid unknown fiscal-year options; fixed both. Verified 50-row pagination, two NACH circulars with reference 13 compared by exact ID, AePS missing page warnings, ambiguity choices and a cited UPI generation result. No final captured browser console errors.

93 tests passed after activation, 55/55 UPI anchors retained in each evaluated retrieval mode, all 12 product-isolation checks passed, and seven product generation examples plus two abstentions were exercised. The live test assertions were corrected to the existing automated_supported label; this was a test expectation mismatch. Product-specific examples replaced two initial shared-compliance selections for more useful coverage. Tests are not expert accuracy evidence; response brevity and OCR spelling remain limitations.

Updated current flow and all entry-point docs, added architecture/validation/import guides and screenshots, and marked old PDFs/assessment as historical. Current server runs v0.5 on port 8765; stopped the temporary preview server.


## v0.5.1 — Context-sensitive answer formatting

The original schema returned claims and the browser always wrapped them in a bullet list. Added a layout of paragraph/bullets/steps referencing one-based draft claims, validated for exact coverage and legal block types. Claim filtering precedes layout materialization, with stable indices preventing reassignment after withholding. Fallbacks preserve all retained claims; explicit styles override an incompatible model layout. No unchecked prose fields or post-check rewriting call were added.

Added the style control, safe shared HTML/Markdown renderer, inline citation buttons and one support notice per answer. Kept raw model HTML/Markdown inert. Automated testing caught an explicit “bullet points only” parsing gap; fixed and verified. All 103 Python tests and renderer/export checks pass. Live Qwen cases returned paragraph, bullet-list and mixed layouts with support checks; exact brevity remains imperfect. Verified real paragraph rendering with no list elements and a working citation link. No embeddings changed; server restarted at the original localhost address. Pre-change files are in versions/v0.5.0.

