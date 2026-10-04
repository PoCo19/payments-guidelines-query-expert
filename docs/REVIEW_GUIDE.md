# Source and evaluation review - v0.4

## Review a source

1. Open Source review. Inspect a flagged page, then its Saved original PDF. Compare the actual page image; another OCR copy is not independent verification.
2. Expand Record a source review. Enter the document ID and page, then Load source & fingerprint.
3. Select OCR correction, Date metadata, Feature / participant mapping, or Circular relationship.
4. Copy an exact phrase from the effective source text. A correction must identify a unique phrase. For dates and labels, the phrase anchors the reviewed decision.
5. Enter the change, reviewer name and an explanatory note. Save Proposed until checked; save Accepted only after checking the original. Proposed/rejected records do not change retrieval. To accept a proposal, create a new accepted entry and mention the proposal ID in the note.
6. Stop the app, run `run.cmd embed`, then restart with `run.cmd`. The review response explicitly reminds you. Until restart, the running process continues using its previous snapshot.

Review records are append-only through the UI. There is no delete/revoke control. To undo a correction, record an inverse correction against the current effective phrase; retain the earlier record for provenance. Back up the annotation file before developer-led cleanup. Accepted overlapping/conflicting corrections are rejected before writing the file. Source hash mismatches require re-review after a source update.

The initial ten annotations are `assistant_source_checked`, based on PDF images, not human approval. Saving in the local UI is attributed to the named local reviewer, without authenticated identity or an approval hierarchy. This is a single-user localhost prototype.

## Fields and participant labels

Date fields: issue_date, listed_update_date, effective_date. Enter ISO dates. Issue-date filters still use issue/public-revision dates; adding an effective_date annotation does not implement as-of applicability logic.

Feature IDs: use `data/feature_rules.json` (tap_pay, etc.). Participant IDs: payee_psp, payer_psp, remitter_bank, issuer_bank, beneficiary_bank, upi_app, primary_user, secondary_user, acquiring_bank. Only mark roles explicitly supported by the text. A generic PSP Banks reference does not by itself establish payer PSP responsibility.

Relationships need a target register document and an exact source anchor. Record references unless the source supports a stronger relationship. Do not infer supersession from a suffix or later date. The source reader displays relation provenance; retrieval still uses one-hop navigation.

## Independently review the evaluation set

Use `evaluation/independent_review.csv`. For each question:

- Check expected_answer and every source anchor against original PDFs.
- Record reviewer and source_verified. Correct questionable cases in a NEW version of the dataset, preserving the current frozen JSON/hash and baseline.
- Read generated outputs and mark answer_correct, citation_support and missing_requirements. Review omissions as well as individual claims.
- Include hard paraphrases, ambiguous numbers, missing sources, conflicting clauses, tables and multi-circular questions. Current cases are concentrated on a few product families and many name a circular explicitly.

No expert-reviewed accuracy score is published until that work is done. The v0.4 report is a reproducible development comparison. The local model checking its own claims is not an independent judge.
