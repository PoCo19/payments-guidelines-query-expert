# Answers, human sign-off and evaluation

Implemented 26 October 2026. This guide supersedes the review-related interface wording in the 25 October product guide. It changes presentation, not the RAG engine or the saved-work lifecycle.

## Three separate concepts

| Concept | Purpose | What happens |
|---|---|---|
| Answer checks | Help expose evidence limitations in an answer | Existing automatic citation, support and completeness checks run. Warnings remain advisory and visible. |
| Human sign-off | Record a person's validation of one saved response or brief | A user optionally marks it as awaiting review. A person inspects the sources and records their name, rationale and decision. This does not assign or notify anyone. |
| Project evaluation | Measure how the system performs across reviewed cases | The separate benchmark, including the proposed 50-case acceptance set, requires independent source/outcome review and scoring. Saving or approving an answer does not run or satisfy that evaluation. |

Independent benchmark and graph/source review remain deferred. A human sign-off inside the app is not a project-quality score, regulatory certification or enterprise identity verification.

## The normal experience

**Ask & Research:** ask a question and read its answer and evidence. A useful cited answer can be saved to Query Desk.

**Query Desk:** define a question, generate an answer, inspect citations, and optionally edit, save or export it. Human approval is not required to read, save or export. Export retains evidence and the actual review status, including when nobody has signed off.

**Change Briefs:** select the document and comparison baseline, generate documented findings, then record analyst considerations separately. The same optional sign-off controls apply. Findings, proposed actions and unresolved questions remain distinct.

The main actions are **Generate answer**, **Save changes** and **Export with evidence**. **Human sign-off (optional)** is collapsed when opening a saved item. It explains the distinction from evaluation and provides **Mark as awaiting review**, followed by the existing human decision form. Approval still requires a name, rationale and attestations about sources and qualifications.

## Why history remains

History preserves what was saved previously: the request, generated answer, edits, evidence snapshot and human decisions. Revision numbers appear inside History rather than beside the main answer. They track saved snapshots, not model versions or confidence. An initial request can exist before any answer has been generated.

Editing an approved response creates a new draft without carrying its approval forward. Earlier sign-off remains in History. Source/model/graph freshness guards remain unchanged; evidence or settings changes can require revalidation. These guards are conservative and do not establish that every answer is correct.

## Labels and compatibility

| Existing stored state | Current presentation |
|---|---|
| Draft | Saved; no human sign-off recorded |
| Needs review | Awaiting human review |
| Approved | Human sign-off recorded |
| Rejected | Changes requested |
| Needs revalidation | Evidence or settings changed; sign-off needs revalidation |

Stored states, API payloads, revisions, decisions and export metadata are retained. No migration is required. Existing records are not rewritten. Exports can still contain internal state names and revision numbers for traceability.

Automatic check wording distinguishes a possible evidence gap, an unavailable check, invalid checker output and no additional issue found. An incomplete answer remains explicitly incomplete. A successful automatic check is not presented as human approval or proof of completeness.

## Verification and limits

457 Python tests and all four JavaScript suites passed. Browser checks used an isolated copy of saved workflow records to verify optional sign-off, the local status transition, preserved warnings, hidden history, and Change Briefs. No human sign-off was fabricated. The browser responses were saved model outputs from 25 October; this work does not claim a new generation-quality evaluation.

Core backend/configuration hashes match the start of this change. Corpus files, embeddings, models, retrieval and generation were not modified. No GitHub publication or replacement of the frozen 24 October handoff was performed.

Verification records: [review clarity checks](../evaluation/review_clarity_20261026/README.md).
