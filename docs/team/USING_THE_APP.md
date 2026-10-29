# Using the application

Complete [setup](../../HOW_TO_RUN.md) first. Two main tasks use the same evidence engine.

| Task | Start with | Get |
|---|---|---|
| Ask a question | A question about a payment guideline | A question-focused answer with citations |
| Understand a change | A document and confirmed comparison sources | A cited change summary, conditions and unresolved points |

**Saved work** keeps either result; it is not a third AI product. **Document library** supports search, inspection, summaries and comparisons. Intake, source review and retrieval checks are under **Manage library & tools**.

## Ask a question

1. Open `http://127.0.0.1:8765/`, enter a question and select a product when useful.
2. Select **Ask question**. The default is a cited AI answer with automatic formatting.
3. Read the answer and visible limitations. Select a citation to inspect its passage and original document.
4. Select **Save answer** to retain the result. This copies the completed answer and evidence without regenerating them.

**Filters and answer settings** contains advanced scope, issue-date cutoff, output mode and style. **Source excerpts** shows passages without model-written explanations. Automatic style can combine paragraphs, lists and tables; it does not force a layout.

Clarify ambiguous references. If evidence is unavailable, explaining the gap can be the correct result. An issue-date cutoff is not an effective-date guarantee. Temporary jobs disappear when the server restarts; saved work persists locally.

## Understand a change

1. Select **Understand a change → Choose documents**.
2. Search by reference or title. Choose the document to investigate, then add one to five comparison sources. Use **Inspect** to read them.
3. Select **Continue** and confirm the baseline. Related-document suggestions are leads, not proof of supersession.
4. Optionally add a focus question or operating context. The default asks for changes, source-backed conditions and dates, and unresolved points.
5. Select **Prepare change summary**. This saves the comparison and starts generation in one action.
6. Inspect the answer and citations. Add your considerations under **Internal notes (optional)** if needed, then export with evidence.

The model can still confuse dates or interpret silence too strongly. A requirement absent from a later document is not automatically unchanged or withdrawn. The tool does not issue departmental instructions, deploy transaction rules or make compliance decisions.

## Saved work, review and history

Open **Saved work** to search both saved answers and summaries. Optional filters narrow by task, review state or active/archive/trash location. **Organise** offers recoverable archive/trash controls; use the location filter to find and restore records.

Read, edit or export without human sign-off. **Human sign-off (optional)** records a name, rationale and decision after someone checks sources. Marking a result for review does not notify or assign anyone. A typed name is attribution, not authentication.

**History** stores earlier snapshots. Editing an approved response clears approval on the revised draft. Relevant source/settings changes can require revalidation. Exports retain evidence and actual review status; exporting does not approve a result. Human edits are not automatically rechecked, and the editor supports plain text rather than rich table-cell editing.

In-product sign-off is separate from the independently reviewed 50-case project evaluation.

## Read warnings accurately

| State | Meaning |
|---|---|
| Incomplete answer / withheld statement | A fact or qualification may be missing or unsupported |
| Completeness check unavailable / invalid | No usable checker conclusion; this is not a pass |
| No additional issue found | No further issue was flagged; correctness is not certified |
| Partial source coverage | Indexed text may omit original content |
| Needs revalidation | Evidence/settings changed; regenerate and reassess before reuse |
| Graph degraded | Maintained links failed validation; ordinary retrieval remains available |

Report failures with the exact question, filters, answer, citations, warnings, commit and original evidence supporting the correction. Keep unsuccessful results. See [current findings](../PRODUCT_MATURITY_20261028.md).
