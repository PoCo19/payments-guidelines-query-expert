# Adaptive answer presentation — 26 October 2026

**Closeout, 27 October:** the final Automatic-style handling for prompts combining tables and prose passed all 15 formatting tests. All four frontend suites were rerun successfully, and the current code was loaded by restarting the localhost application. The earlier approval-service usage-limit interruption is resolved.

Automatic answer style can combine paragraphs, bullets, numbered steps and evidence tables. There is no new output mode and no requirement to use a table, an introduction or a list. Explicit Paragraphs, Bullet points and Paragraphs + bullets selections keep their existing behaviour.

## What changed

The existing generation call can propose a table in its layout. Each cell references one complete factual statement with its citations. The same support checks run before any statement is displayed. Presentation does not rewrite surviving statements or generate an unchecked summary afterward.

Table headers are restricted to neutral **Evidence 1–4** labels. The cells name their subjects/documents and keep their conditions in the statement. This first implementation deliberately avoids unverified headings such as “current rule” or “superseded requirement.” It supports side-by-side evidence, not arbitrary spreadsheets or merged cells.

Query Desk and Change Briefs now use the shared answer renderer while the saved answer text still matches the generated statements. Saving and reopening retains the structure already stored in the result. Markdown export preserves paragraphs, lists, tables and citations. Editing the answer's wording uses the existing plain-text editor and display; old generated tables are not silently applied to changed text. Rich table editing is not included.

## Validation and fallback

- Every real draft statement must appear exactly once in a valid layout. Missing or duplicated references fall back to the existing presentation without dropping retained statements.
- Nonexistent references in prose/list blocks can be removed only if every real statement still appears exactly once. This narrow repair does not add facts or alter table cells.
- Invalid tables, unknown headers, uneven rows or nonexistent table-cell references trigger fallback.
- If a table cell is withheld by support checking, that table becomes prose. Surviving cells never shift columns, and missing evidence is not labelled “not applicable.”
- Text is escaped; generated HTML or Markdown is not executed. Tables use column headers, adjacent citation buttons and a keyboard-focusable horizontal scroll region.
- Incomplete-answer warnings, abstention, clarification, human review and source freshness rules remain intact.

The schema and formatting instructions changed, so generated wording may vary. Retrieval, graph assistance, evidence checks, model choice/budgets, corpus and embeddings are unchanged. This is a presentation enhancement, not a demonstrated improvement in factual correctness or completeness.

## Verification

463 Python tests and four JavaScript suites passed. Coverage includes mixed layouts, cell citations, unsafe markup, explicit styles, withheld cells, nonexistent/duplicate references, saved-answer rendering, export and preservation of human edits.

Seven development model calls were saved during implementation. Simple explanations used prose. Comparison attempts exposed invalid layout references and fell back safely. A saved two-statement comparison replayed through the final narrow repair produced a valid table; this is a layout replay, not another model generation. All seven generated answers remained marked incomplete. No answer-quality acceptance or latency improvement is claimed.

Browser checks inspected a clearly labelled synthetic paragraph/table/bullet fixture and an isolated Query Desk replay of the saved model response. Its table citations opened the appropriate evidence. Independent benchmark/source review remains separate and pending.

See [test logs, model attempts and browser evidence](../evaluation/adaptive_format_20261026/README.md). Existing saved answers are not regenerated. Refresh the browser after the application restarts to load the updated renderer.
