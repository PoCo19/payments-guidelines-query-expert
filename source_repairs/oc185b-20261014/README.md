# OC185B source transcription repair — 14 October 2026

The original PDF page 1 says **Tax Payments to ₹5 lakh**. The indexed OCR read **Tax Payments to 25 lakh**. The source PDF SHA256 and before/after page hashes are recorded in `repair_record.json`. This is an AI visual check, not independent expert verification of the entire circular.

- `OC185B_corrected.md`: reusable Markdown with explicit page markers, the corrected amount on page 1 and the existing table transcription on page 2. Other page-1 OCR text is retained; this is a targeted repair, not a claim that every character is clean.
- `OC185B_legacy_before.md`: preserved pre-correction reading copy for provenance. Do not ingest it as the current source.
- `repair_record.json`: exact correction, source PDF hash, previous/current text hashes and release identity.
- `embedding_build.json` and `validation.json`: new snapshot structural validation. One new embedding, 14,479 cache hits; document and chunk counts remain unchanged.
- `regression.json` and `regression-tests.log`: 306 passing automated tests, zero failures/skips.

The original research-pack Markdown was also corrected at the path recorded in `repair_record.json`. Historical corpus releases and the old alternate import remain untouched. The new release's document record points to `sources/corrections/OC185B_corrected.md`; its page text, chunks and vector index use the corrected content. Future intake starts from the active corrected release. Rebuilding from an older archived corpus requires replaying this repair; corrected Markdown does not silently rewrite frozen historical archives.

The document ID remains `2025-OC-185B`: this is a transcription repair of the same source, not a new circular or legal amendment. `raw_extracted_text` preserves the old page for audit. The exact corrected page hash is explicitly accepted by the source-quality gate, so this passage can support answers again. The historical corrupt version is still protected if an old release is restored. Unknown later changes require another review.

The graph manifest `pilot/upi_extended_graph_v3.json` updates only the four anchors on the corrected page, checks their existing quotations, and removes the obsolete OCR-ambiguity caution. It retains proposed-link status. The v2 graph and experiment captures remain frozen.

## Reproduce on the original baseline

`python tools/repair_oc185b_source.py` prepares `payments-oc185b-repair-20261014` and corrects the legacy reading copy after checking the original page and PDF hashes. It refuses an existing destination or changed source. Run this only against the recorded original baseline, with its saved source PDF and uncorrected legacy Markdown available; do not reapply it to the active corrected version.

Then use `python tools/document_pipeline.py build --release payments-oc185b-repair-20261014`, inspect the candidate, and activate with `python tools/document_pipeline.py activate --release payments-oc185b-repair-20261014`. The build uses the installed embedding model and content cache. Existing servers must restart to read the selected release. Rollback is supported by the same pipeline; it does not undo the separately corrected legacy reading copy.

This release is local. It has not been added to the frozen colleague source archive or pushed to GitHub.
