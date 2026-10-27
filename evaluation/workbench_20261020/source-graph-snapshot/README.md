# Matching graph and source snapshot

This development bundle preserves the exact maintained graph with the matching source-release hashes. It is not a standalone corpus or a release-approved handoff. Verify all source hashes against `payments-ocr-audit-20261015` before use. The normal Engine graph loader verifies quote presence and page hashes; a mismatch degrades graph assistance and keeps ordinary retrieval available.

Intake candidates automatically copy this maintained manifest into their release and validate it. Rollback restores the previous source/configuration pair. Independent review of all 55 anchors and 13 relationships remains pending.
