# Sampled OCR repair evidence

This folder records a reproducible six-document, ten-page audit against original PDFs. The review is AI-assisted; independent human review is pending. It is not a whole-corpus accuracy certificate.

- `sample.json`: seed, eligible population size, selected documents, PDF hashes, page-image hashes and review notes.
- `images/`: the ten original PDF page renderings inspected during the review.
- `*-indexed.txt`: pre-repair indexed text for each sampled document.
- `original_markdown/`: original reading Markdown bytes retained before correction.
- `corrected/`: reusable corrected Markdown with explicit page ownership.
- `corrections.json`: the 21 exact before/after replacements and pre-repair page hashes.
- `repair_record.json`: post-repair hashes, original reading-file paths and release provenance.
- `source_validation.json`: page/identity checks, graph-anchor validation and targeted retrieval results.
- `regression.log`: latest full Python regression result.
- `final_validation.json`: final code hashes, check results, local server checks and explicit remaining limitations; handoff verified on 16 October 2026.
- `prepare_reviewed_plan.py`: records explicit reviewed edits; it does not automatically infer corrections.
- `validate_repair.py`: reruns source integrity and targeted retrieval checks.
- `finish_audit.py`: records inspected images/status and original Markdown table spacing; this is an execution record, not a general ingestion command.

The release was prepared by `tools/repair_ocr_sample.py`, then built through `tools/document_pipeline.py`. Unchanged text reused cached embeddings. Historical releases remain intact. The repair tool refuses changed PDF/page hashes, missing/ambiguous replacement anchors, or an already-existing release.

See [the implementation and results report](../../docs/SCOPE_CITATIONS_AND_OCR_AUDIT_20261015.md) for limitations and rollout status.
