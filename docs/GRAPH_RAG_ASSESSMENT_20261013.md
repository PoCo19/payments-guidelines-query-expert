# Graph-assisted retrieval assessment — 13 October 2026

## Conclusion

The application preserves document ownership and has a small document-reference graph. It does not guarantee amendment-chain coverage or determine which individual requirements apply at a given date. A graph-assisted, clause-level extension is relevant to the user's scenario; installing a graph database alone would not solve it.

This records the initial read-only assessment. A subsequent user-authorised, opt-in pilot around OC 128/128A and OC 226/226A is now documented in [the pilot report](GRAPH_PILOT_128_226.md). The baseline described below remains unchanged when the pilot is disabled. Earlier reliability validation work remains separate.

## Verified implementation

Inspected `registry.py`, `adaptive_context.py`, `research.py`, `tools/document_pipeline.py`, the active source index and its SQLite registry. Active release: `payments-rbi-core-20261009`. Registry fingerprint: `41d838e42cedf7bb619b1b7adbc6bb1d1cfd8fd003223d2a026a861a2102d7b5`.

- 54 stored relationships: all have type `references`.
- 48 resolve to available text, five have missing targets and one has unavailable text. Resolution means document identity/text availability, not verified legal effect.
- Evidence basis: 48 number occurrences, five metadata-only entries, one source-anchored review.
- No explicit relationship edges originate from or target the eight `rbi:` records in this registry.
- Accepted review overlays can store more specific relationship types, but none of the current edges encode an amendment or supersession.
- Imported automatic references resolve by circular number within the same series. They are not a publisher-neutral cross-source resolver.
- New document intake initially sets `related_circulars=[]`. Its `revision_of` field identifies an intake snapshot revision, not a legal amendment relationship in the graph.

Examples present in the active graph:

| Source | Stored targets | Stored meaning |
|---|---|---|
| UPI OC 169A, addendum to enhancement of LITE limits | OC 169 and OC 138 | References |
| UPI OC 138B, addendum to introduction of LITE | OC 138 | References |
| UPI OC 179, customer awareness/enablement | OC 138 and OC 169 | References |

These are source-identity examples, not confirmation of currently applicable monetary limits. The user's 500-to-1000 illustration remains hypothetical in this assessment.

For ordinary related-context retrieval, the implementation follows incoming and outgoing resolved edges from at most the first two seed documents. It adds at most two related documents, normally one selected passage per added document, at one hop. It can also add a same-feature passage and neighbouring text. The ordinary route has an 18-passage and configured character budget. Summary and selected-document comparison use separate coverage routes. Topic retrieval can independently find additional documents beyond graph links.

Therefore a linked addendum may be found, but its decisive clause may still be omitted. An unlinked dispute circular can be found by keyword/vector/topic retrieval; this is not guaranteed. The generator and same-model checks only see assembled evidence and cannot certify that an absent amendment does not exist.

## Proposed extension

Retain BM25, embeddings and Chroma. Extend the structured relationship layer alongside them. Begin in SQLite; consider a dedicated graph database only if graph size, traversal, editing or operational requirements justify it.

Represent four distinct concepts:

1. **Document/version:** issuer, stable identity, collection time, issue/update dates, original source and hash.
2. **Clause:** exact source passage, page/logical-page basis and document owner.
3. **Topic/aspect:** product or feature plus an aspect such as transaction limit, balance limit, authentication, disputes or reporting.
4. **Requirement/version:** actor, action, channel, value/unit, conditions and source-supported effective interval where known.

Use different relationships for `references`, `covers_topic`, `amends_clause`, `replaces_requirement` and `clarifies`. A shared topic is a navigation link. An amendment or replacement claim requires source evidence and review. Automatic extraction should create proposed links; unknown dates, ambiguous identities and uncertain legal effects must remain explicit.

For the hypothetical example, an addendum can replace the transaction-limit requirement from 500 to 1000 while other clauses in the introduction remain potentially relevant. A disputes clause is another aspect of the same product; it must not be silently discarded because a later limit circular exists. Scope and effective dates determine whether requirements can be combined. A graph cannot prove that an unchanged provision remains applicable when relevant sources are missing.

## Query flow

1. Interpret topic, requested aspect, entity/channel and date. Clarify only material ambiguity.
2. Retrieve initial passages through existing hybrid search.
3. Follow evidence-backed amendment/clarification links in both directions and retrieve their exact affected clauses. Detect cycles and unresolved targets; bound traversal.
4. Add other requested aspects through topic links and ordinary retrieval. Keep an explicit coverage list.
5. Resolve only supported changes within matching scope and time. Do not use publication order, publisher names or graph proximity as automatic precedence rules.
6. Assemble passages with mandatory amendment evidence ahead of optional background. If the budget excludes decisive evidence, expose that limitation or narrow the response.
7. Produce a cited answer distinguishing the rule supported for the requested date, its change history, separate obligations and unresolved gaps. Unknown current applicability must not become a confident current-rule claim.

Keep the schema publisher-neutral: RBI, NPCI and future sources use the same identity, scope, relationship and provenance fields. Linking documents across publishers does not establish that one overrides another.

## Pilot and acceptance

Use a small reviewed UPI LITE slice containing the introduction, limit addenda and operational/dispute documents. Add cross-publisher relationships only where the source supports them. Compare existing retrieval against the graph-assisted version on a separately reviewed set, holding models, corpus and context budget constant.

Test older versus later dates, future-effective amendments, partial amendments, different limit types, unchanged obligations, several amendment hops, missing targets, ambiguous references, conflicting provisions and unsupported cross-publisher precedence. Measure complete required-clause retrieval, stale-rule answers, unsupported supersession assertions, correct clarification/abstention and latency. No superiority claim is justified before this evaluation.

## External reference

Microsoft GraphRAG local search combines graph entities/relationships with original text chunks: [official local-search documentation](https://microsoft.github.io/graphrag/query/local_search/). The complete Microsoft pipeline also extracts entities and relationships and builds community summaries: [official overview](https://microsoft.github.io/graphrag/). The focused amendment-aware extension above is a proposed design for this project, not a claim that those tools independently establish regulatory applicability.
