# Using the application

Complete [setup](../../HOW_TO_RUN.md) first. This guide is about the user experience; [project flow](PROJECT_FLOW.md) explains the implementation.

## Choose the right workspace

| Workspace | Use it when | What you keep |
|---|---|---|
| Ask & Research | You want to explore a question or inspect documents | An answer and evidence; save useful cited answers to Query Desk |
| Query Desk | You want to retain and refine a response for your team | The question, answer, source snapshot, edits and optional human decision |
| Change Briefs | You want to understand a document against a comparison baseline | Cited findings, analyst considerations and unresolved questions |

An exploratory answer and a saved response are different things. Query Desk adds persistence and a work history; it does not use a separate, inherently more accurate model.

## First walkthrough: Ask & Research

1. Open `http://127.0.0.1:8765/` and choose the relevant product where useful.
2. Enter a specific question. For example: “What does OC186A say about UPI Tap & Pay?” Treat this as a practice question, not a guaranteed correct demonstration.
3. Keep **Cited AI answer** selected. **Source excerpts** instead shows retrieved passages without a model-written explanation.
4. Leave **Answer style → Automatic**. The answer can use prose, lists, steps or a table. More complex formatting is not automatically better.
5. Read the answer's qualification and warning text. Select a citation such as S1 to inspect the supporting passage, page and document identity.
6. Where an original-document link is available, check the original. Extracted text can be incomplete or wrong.
7. If the answer is useful, save it to Query Desk using the provided save action. Saving copies the completed answer and evidence; it does not regenerate them.

If a reference matches several products or years, choose the intended document. Do not treat a clarification request as an answer. If the document is unavailable, the correct behaviour can be an explanation of the gap rather than a generated answer.

The job cache is temporary; save a useful answer before restarting the server. Saved Query Desk records persist locally. They are not uploaded to GitHub.

## Query Desk

Create a query request, define the question and scope, optionally select sources, then generate an answer. You can read it, inspect citations, edit the wording, save changes and export with evidence.

The answer comes first. **Human sign-off (optional)** and **History** are collapsed. You do not need approval to read or export an answer. Export includes the actual review status; an unsigned answer does not become approved by being exported.

**Mark as awaiting review** only records a local status. It does not send an email or assign work to a colleague. If a person reviews it, they enter a name, rationale and decision after checking sources and qualifications. The name provides attribution, not authenticated identity.

History keeps saved snapshots. Its revision numbers track changes to the work item, not a model version or a confidence score. Editing an approved answer creates a new draft without carrying approval forward. Earlier decisions remain in History. Relevant evidence/settings changes can require revalidation.

Human-edited text is not automatically rechecked. Generated layouts are preserved while the text remains unchanged; the editor currently supports plain text, not rich table-cell editing.

## Change Briefs

1. State the change question and select the document being investigated.
2. Select and confirm the earlier/comparison sources. A suggested relationship is a lead to inspect, not proof that it applies.
3. Generate and inspect **Documented findings** and their citations.
4. Optionally classify findings as a documented change, retained requirement or unresolved finding after checking the sources.
5. Record **possible actions** and **questions to resolve** separately from source requirements.
6. Save, optionally obtain human sign-off, and export with evidence.

For example, an analyst might propose that an operations team assess whether an internal procedure is affected. That is an analyst consideration; it is not automatically an obligation stated by the circular. Audience and operating-context fields record useful analyst context. They do not establish institution-specific facts or automatically turn the answer into an implementation plan.

The application does not send instructions to departments, alter transaction-risk rules, make a compliance verdict or deploy business changes.

## How to interpret warnings

| Message or state | Meaning | Useful next step |
|---|---|---|
| Incomplete answer / withheld statement | A central fact, qualification or supported claim may be missing | Inspect the evidence and the checker details |
| Completeness check unavailable / invalid | The checker did not produce a usable conclusion | Keep the uncertainty; do not treat silence as a pass |
| No additional issue found | The checker did not flag another issue | Still inspect consequential facts |
| Partial source coverage / missing pages | Some original content is absent from the indexed text | Find and review the original document |
| Needs revalidation | The saved response no longer matches its previous evidence/settings snapshot | Regenerate and reassess before reuse |
| Graph degraded | Maintained graph links failed validation or could not load | Use ordinary retrieval cautiously and report the status |

## Report a useful failure

Capture the exact question, selected product/documents, answer style, commit, answer, citations and warning text. Explain the expected behaviour and identify the original source supporting it. Distinguish “I think this is wrong” from an original-document-verified finding.

The current UPI Lite historical-limit failure is a useful example: the model gave older figures, a newer amendment existed in the corpus, and the completeness check was unavailable. Do not remove that record because it makes a demonstration less favourable. See [the evaluation record](../../evaluation/release_20261027/README.md).
