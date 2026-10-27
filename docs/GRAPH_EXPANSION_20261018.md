# Broader graph coverage and answer reliability — 18 October 2026

The project keeps hybrid retrieval, local reranking, cited answers and the maintained UPI graph. The new corpus-wide reference graph is a **candidate**, separately switchable and disabled in the active configuration until its evaluation justifies activation.

## Relationship model

| Relationship | What is recorded | What it does not imply |
|---|---|---|
| Numbering family | Same issuer/product namespace and numeric base, such as 115 and 115A–F | Every numbered suffix amends the same provision, or replaces the original in full |
| Explicit reference | A source passage names another document; its identifier is resolved or left unresolved | The referenced document's entire contents apply to the question |
| Topic mention | A source passage matches a configured topic pattern; a document can mention many topics | Applicability, precedence, or a verified amendment |
| Existing curated relationship | The maintained pilot's source-anchored reference, clarification or aspect amendment | Independent expert approval of every relationship |

These are separate records. UPI Lite can appear in its introduction, limits, auto top-up, customer-awareness and broader operational circulars. A general UPI document need not belong to any feature. Documents remain searchable when they have no graph relationship or topic annotation. Topic labels are extensible patterns, not a complete taxonomy or automatically inferred legal rules.

The new expansion follows only resolved explicit reference edges, in either direction and at most one hop. Numbering families and topic mentions are available for review but do not automatically expand the answer context. Shared topics across different number families therefore remain visible without being mislabelled as amendments. Existing hybrid search and same-feature retrieval still find topical material without explicit references.

## Implementation

- `reference_graph.py`: page-anchored reference extraction, namespace-aware identity matching, optional fiscal-year disambiguation, numbering families and many-to-many topic mentions. Ambiguous, unavailable and incomplete references remain explicit.
- `tools/build_reference_graph.py`: builds a versioned graph without modifying corpus text or embeddings.
- `tools/document_pipeline.py`: every newly prepared candidate release includes `reference_graph.json`. It reuses unchanged page scans when a prior graph exists, but resolves all targets again so a newly added document can satisfy an older missing reference. The graph participates in candidate-integrity fingerprints. Preparing it does not enable graph retrieval automatically.
- `app.py` / `adaptive_context.py`: separately controlled candidate expansion, preserving document/date filters, selected-document routes and the existing evidence budget. The final candidate order appends only after existing evidence; it cannot displace that evidence. Graph-load failure falls back with a warning. Each loaded reference/topic anchor is checked against its page hash and exact offsets/quote.
- `evaluation/reference_graph_eval.py`: paired comparisons with the maintained pilot enabled in both arms. Only the new reference expansion differs; order alternates. Saves actual responses, source hits and code/data fingerprints.

Parser corrections include preserving `OC115(B)`, `OC115-B` and `OC.115B` as 115B, instead of incorrectly resolving them to 115. Incomplete identifiers such as a number followed by an unrecognised numeric suffix remain unresolved. Extraction remains conservative: noisy OCR, unrecognised reference styles and aliases can still prevent matching.

## Candidate inventory

`pilot/corpus_reference_graph_v4.json` scans 4,832 eligible pages across a catalogue of 1,929 records. Two page records belong to non-converted documents and are not scanned for usable relationships. It records:

- 2,095 reference occurrences: 334 resolved, 39 pointing to unavailable records, nine ambiguous, 123 incomplete and 1,590 without an exact recognised target.
- 234 unique resolved document pairs; repeated occurrences retain their own page provenance.
- 210 numbering-family groups.
- 2,963 topic mentions across 1,131 documents. These are pattern matches, not verified semantic relationships. Generic product-specific keywords are restricted to their product scope; explicit primary topic names can still match across products. This avoids labelling an RBI document as RuPay merely because it says “issuer”.

Unresolved counts are **not** counts of missing publications: they include incomplete metadata, unmatched aliases, self-identifiers not recognised as such and extraction noise. Full exact reference matching works across issuers; practical RBI coverage remains limited by identifier matching and must be evaluated independently. “Scanned across the corpus” does not mean “all relationships discovered.”

A repeat build reused all 4,832 scans and reproduced identical edges and topic mentions. No active source text, embeddings, model settings or graph configuration changed.

## Answer-quality changes

1. Collective claims naming multiple circulars must not borrow an explicit payment/transaction category from another circular. The new conservative literal-category check also runs on selected supporting excerpts. Synonyms may require separate source-specific wording; it is not a general semantic proof.
2. Known `Document S9`-style navigation labels no longer introduce a fictional factual number into support checks. Real codes, amounts, section identifiers and unknown citation labels remain checked.
3. Identical repaired statements are displayed once, merging their valid citations and preserving which original primary claims they cover. Audit records retain both repair attempts. Different wording is not automatically merged.
4. Coverage-review inputs now carry circular numbers, and the prompt distinguishes earlier versus amended requirements and per-transaction versus cumulative measures. This remains a same-model advisory check; a prompt change alone does not prove reliability.

The earlier tax-series false acceptance is now withheld in the 16-claim development challenge, with zero false acceptances, zero valid claims withheld and zero unavailable checks in that run. An attempted extra per-document model-checking pass did not fix the failure and was removed, avoiding additional inference cost. These development labels await independent review.

Regression also exposed a Windows HTTP rejection issue: unread small non-JSON request bodies could reset the connection before the client received the 415 response. The handler now drains only bounded small bodies with a short timeout; content-type rejection is preserved.

## Release boundaries

The new graph is not a legal-precedence engine and does not decide whether two requirements are contradictory. No automatic amendment or supersession inference was added. Independent source/answer review remains necessary. No broader graph activation, browser-server restart, GitHub publication or final end-to-end release verification is implied by the candidate build. Final release verification remains last, as requested.

## Evaluation and activation decision

**Keep the broader candidate disabled.** The current maintained UPI graph remains enabled. The build and intake integration are complete, but the comparisons do not establish a worthwhile improvement from automatically expanding the new graph.

| Check | Saved observation | Decision |
|---|---|---|
| Initial 138-case paired retrieval | Both arms 212/223 anchors; one gain and one loss, no execution errors; unchanged recorded snapshot | Reject early insertion of graph passages: it displaced useful existing context |
| Safer ordering, ten new development cases | Both arms 15/15 anchors; zero gain/loss; all existing source sequences preserved; no extra passages added on these cases | No demonstrated extra retrieval benefit; do not activate globally |
| Three additional RBI/mixed-source paraphrases | Both arms 3/5 anchors; no gain/loss; the post-debit-notification paraphrase missed both anchors | Broader graph does not fix this retrieval failure |
| Safer ordering, seven targeted replays | Both arms 3/4 anchors; original lost passage preserved, original gain no longer added; scope controls retained | Displacement fixed, but broader gain remains unproven |
| Final software regression | 390 tests passed | Includes intake, graph integrity/filters, suffix parsing, existing-evidence preservation and answer fixes |
| 16-claim challenge | Eight valid/eight invalid labels matched; zero false acceptances, false rejections or unavailable checks | Narrow development evidence; independent review pending |
| Four final live answers | 13/13 expected anchors; no generation fallback or unavailable support checks; all four coverage reviews raised findings | Do not describe these as four independently correct answers |

The final live tax answer withheld the known incorrect collective assertion and was marked incomplete. The credit-card limit answer retained its two measures; the Deemed Debit answer retained original/addendum chronology; the IPO answer retained the distinction between cumulative Capital Market and single-transaction IPO limits. The IPO response contained no identical duplicate statements. The citation-label and exact-duplicate repair paths also have targeted regression fixtures; the live model need not reproduce every earlier wording.

Coverage warnings still include incorrect interpretations, including treating a GeM EMD row as tax payments generally and questioning correctly separated historical rules. Adding metadata and prompt guidance did not establish a reliable fix. Some findings may identify real missing conditions; they require review rather than blanket suppression. Stronger claim rejection can also leave incomplete answers. These remain separate answer-quality work, not solved by a larger graph.

The 138-case run predates the final append-only ordering. Only the ten-case and seven-case captures test that ordering; do not relabel the earlier full run as final-code verification. The paired captures use graph v3. Graph v4 changes only topic annotation scope; its explicit reference edges are identical, and only those edges participate in candidate retrieval. The new cases are AI-assisted, source-checked against stored Markdown and co-designed development cases, not held-out expert evaluation. No controlled latency improvement is claimed. Final live request durations were approximately 17–23 seconds in this run, not a service-level guarantee.

## Records and reproduction

- [Initial 138-case comparison](../evaluation/reference_graph_runs/20261018T153703603802Z/capture.json)
- [Ten new cases, final ordering](../evaluation/reference_graph_runs/20261018T154314874094Z/capture.json)
- [Three additional RBI/mixed-source cases](../evaluation/reference_graph_runs/20261018T154927750151Z/capture.json)
- [Seven targeted replays, final ordering](../evaluation/reference_graph_runs/20261018T154412193982Z/capture.json)
- [Final four live answers](../evaluation/readiness_runs/20261018T154442787264Z/capture.json)
- [16-claim challenge after the category fix](../evaluation/readiness_runs/checker-20261018T144311405321Z/capture.json)
- [Unsuccessful per-document checker experiment, removed](../evaluation/readiness_runs/checker-20261018T143837024320Z/capture.json)
- [Final 390-test log](../evaluation/readiness_review_20261018/graph-stage-tests-final-v3.txt)
- [Cache reuse and graph counts](../evaluation/readiness_review_20261018/reference_graph_build_checks.json)
- [Additional questions and their provisional source anchors](../evaluation/reference_graph_cases_20261018.json)

```powershell
.\.venv\Scripts\python.exe -X utf8 tools/build_reference_graph.py --output pilot/new-reviewed-candidate.json --previous pilot/corpus_reference_graph_v4.json
.\.venv\Scripts\python.exe -X utf8 evaluation/reference_graph_eval.py --dataset evaluation/reference_graph_cases_20261018.json
.\.venv\Scripts\python.exe -X utf8 evaluation/reference_graph_eval.py
```

The evaluator enables the candidate only in its own Engine instance. The active `config.json` remains unchanged. For a future evaluated rollout, the opt-in settings are `reference_graph_enabled` and `reference_graph_path`; they are separate from the maintained `evidence_graph_path`. Removing/turning off the candidate setting restores ordinary retrieval with the maintained pilot. No embedding rebuild is necessary merely to compare graph expansion.

Next decisions: review representative resolved/unresolved references and source aliases across products, approve source-specific relationships, and address the remaining answer/coverage-review failures. Broader traversal or automatic semantic relationship extraction should be a separate tested experiment, not silently enabled to increase graph counts.
