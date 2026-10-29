# Product clarity and maturity — 28 October 2026

The product is now presented as **Payments Guidelines Query Expert**, with two tasks using one shared RAG engine. The 29 October development publication packages this implementation and its saved evidence; see [publication checks](GITHUB_UPDATE_20261029.md). API integration is outside this increment.

## Six implementation items

| Item | Implementation |
|---|---|
| One coherent product | Shared navigation and naming across the research and saved-work screens |
| One question entry point | Ask a question replaces separate research/query-creation choices; Save answer retains the completed result |
| A clear second task | Understand a change starts with document selection and a confirmed baseline, then saves and generates in one action |
| Less secondary clutter | Advanced settings, review/history, internal notes and management tools are collapsed; evidence warnings remain visible |
| Targeted quality repair | Broad explanations can recover operative amendment clauses already in candidate retrieval; existing scope and budget controls remain |
| Explainable demonstration | Updated teammate guides and a six-minute demonstration with explicit quality limitations |

## How the tasks differ

**Ask a question** starts from something the user wants to know. **Understand a change** starts from a specific document and sources the user chooses for comparison. It asks what changed, which conditions/dates are supported and what remains unresolved. Both reuse the current evidence engine and source reader.

**Saved work** stores either result, its sources, settings and history. Optional human sign-off is available when the team needs it. This is separate from independent evaluation of the project. Saving or exporting does not approve an answer. Existing records and source-change revalidation remain intact.

The change summary no longer appends a generic four-department action checklist. Internal actions/questions are optional analyst notes and survive regeneration. Institutions must supply evidence before asserting institution-specific impact.

## Retrieval repair and limits

The known broad UPI Lite failure was traced beyond candidate retrieval: the operative OC169A clause was retrieved, demoted, and lost while its historical introduction remained. The fix recovers at most two matching operative-change passages from existing candidates for broad explanations. It requires the topic in both title and passage and explicit change wording. It respects product/date filters and skips strict document and historical requests. No circular IDs, publishers or monetary values are hardcoded.

A follow-up found that explanation-style stop words were not normalized like query terms. Normalizing both fixes “in simple words/terms” handling. This is a bounded retrieval heuristic, not a complete amendment resolver. It does not infer precedence from recency or suffixes, and it cannot guarantee synthesis quality.

## Verification and remaining work

See [saved evaluation records](../evaluation/product_maturity_20261027/README.md) for final counts and actual model outputs, including failures. See [interface QA](../evaluation/product_maturity_20261027/design-qa.md) for screenshots and browser journeys.

The first change-summary answer confused an RBI reference date with the NPCI issue date and inferred a restriction to accounts after a deadline. Comparison instructions now explicitly distinguish these concepts; prompt instructions are not a correctness guarantee. Existing advisory warnings and source inspection remain necessary.

Independent acceptance and reviewed source/graph evidence remain pending. The next quality work should address only demonstrated synthesis and checker defects using reviewed examples. Do not add larger models, new providers or automatic graph expansion merely to make the roadmap longer.

## Documentation and compatibility

Start with [TEAM_START_HERE](../TEAM_START_HERE.md), [using the app](team/USING_THE_APP.md), [project flow](team/PROJECT_FLOW.md), and [demonstration](team/DEMONSTRATION.md). [HOW_TO_RUN](../HOW_TO_RUN.md) retains the established installation and model setup.

Existing `/work?kind=query&id=...` and impact links still open saved records. Corpus content, storage formats, model settings, embeddings and maintained graph are unchanged. Automatic whole-corpus graph expansion remains unselected. The frozen 27 October source archive is preserved. Historical reports remain dated evidence, not instructions for the current interface.
