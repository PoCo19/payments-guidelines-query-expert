# Interface QA — 28 October 2026

Scope: consolidate the existing product, retaining its visual language and source safeguards. This is not a complete accessibility certification.

The original research screen and revised home were inspected together in `design-comparison.png`, both at 1265 × 712. The same content area, typography, colours and answer entry remain. The navigation now consistently distinguishes Ask a question, Understand a change, Saved work and Document library. Advanced settings are collapsed. The revised home exposes the primary action and examples earlier.

## Verified journeys

- Ask → real model answer → Save answer: completed in an isolated work database. Saved output retains the generated answer, sources, warnings and original settings.
- Export with evidence: downloaded Markdown without human sign-off; status remained Draft, version 1. No approval was inferred.
- Change flow: selected OC169A, added related OC169, confirmed baseline, generated a real comparison and opened citation S5 in the source reader. Issue date and extracted page text were inspectable.
- Empty comparison: Continue produced a visible actionable error requiring the changed document and a comparison source.
- Work → Document library: the cross-page link opened the correct view. Saved work listed both record types.
- Human sign-off, History, internal notes and organisation actions remained secondary; incomplete-answer warnings stayed visible.
- 390 × 844 responsive checks: saved list and document-selection form had no horizontal overflow (document width 375, viewport 390). Selection focused the document search input with a visible focus ring. The two-step indicator and controls wrapped without overlap. Temporary viewport override reset.
- Browser console check: no error entries observed during these journeys.

Screenshots: `02-choose-documents.png`, `03-source-reader.png`, `04-saved-answer.png`, `05-mobile-saved.png`, `06-mobile-change.png`, `07-final-home.png`.

## Findings and boundaries

The original generic comparison request made an unhelpful saved title. New default requests include the selected source's title; existing saved records are preserved. A raw retrieval-reason identifier was replaced with “Matching amendment provision”.

The first live comparison had substantive interpretation errors despite support checks. Those are preserved in `change-first.json`; later prompt trials are separate records. Interface success does not imply correctness. Review the evaluation README before presenting model results.

No source corpus, embeddings, graph, model configuration, public API or database schema was changed by the UI work. The bounded overview-context fix is separately evaluated.
