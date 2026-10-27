# Extended graph pilot: UPI rule changes and IPO limits

14 October 2026. Development pilot; independent source and answer evaluation pending.

**Later update:** the OCR defect below has now been corrected in Markdown and a new corpus release. The corrected passage is eligible for generation again. The launcher selects graph v3. See [source repair, repeated evaluation and rollout decision](SOURCE_REPAIR_AND_GRAPH_DECISION_20261014.md). The v2 results and failures below describe the earlier source snapshot and remain preserved.

## Decision being tested

Can a small source-linked graph help the assistant retrieve the specific rule, its amendments and relevant conditions together? The target is evidence-grounded payments research. A graph is not a replacement for source acquisition, correct extraction, applicability review or answer validation.

This extends the [OC128/226 pilot](GRAPH_PILOT_128_226.md) with the user-requested OC76, OC141 and OC185 series and IPO mandate-limit history. The graph contains 55 marked source anchors in 15 documents, 13 relationships and six topics. The original 50-question evaluation and corpus contents are unchanged.

## Scenarios and what the graph contributes

| Scenario | Evidence to keep together | What must not be inferred |
|---|---|---|
| OC76 series | Original restrictions, OC76A, and OC76C's domestic/international distinction | A domestic amount limit authorises an international flow; unavailable OC76B contents are known |
| OC141 series | Updated OC141, OC141B, OC141D rent-mode addition, and mandate exclusions | The updated snapshot is the original 2022 wording; missing OC141A/C/E requirements are known |
| OC185 series | Hospitals/education, tax category, newer category table, verified-merchant requirement, bank discretion and cumulative limits | All categories share one limit; a daily ceiling is a per-transaction ceiling; P2P limits increased |
| IPO mandates | Historical OC71, IPO-specific OC127, the retained IPO/RDS reference in OC185A, and the separate capital-market table in OC185B | A capital-market cumulative amount automatically becomes a single IPO mandate ceiling |
| OC128 / OC226 | Original and addendum passages, unchanged conditions and effective-date text | Entire original circulars are replaced merely because an addendum exists |

For the IPO example, the prototype prioritises the IPO-specific source passages and keeps the broader category table as related context. It does not select whichever document is newest, whichever amount is highest, or whichever source shares MCC6211. Purpose code, transaction type and limit period remain separate. These are interpretations of the saved source snapshot, not a certification of current applicable rules.

## Implementation

The existing hybrid search and reranker find starting documents. A topic and source-ID match activates the overlay; explicit product names prevent activating a different product's graph. Shared documents do not automatically activate every topic they contain. Source-anchored traversal remains bidirectional, cycle-safe and bounded to two hops and 12 graph passages within the existing 18-passage / 18,000-character budget.

Relationships distinguish explicit references, proposed aspect-level amendments and **related topics**. Related-topic edges require anchors at both endpoints and do not assert amendment or legal precedence. Page hashes and quoted locators must match the actual indexed text; a stale graph falls back visibly to standard retrieval.

The extended overlay adds source-gap notices and scope labels. Original OC128 table fragments are marked as citation companions. The graph-enabled generation prompt asks the model to cite all necessary fragments, distinguish limit types, preserve obligation strength and retain date/scope qualifications. These hints are not themselves evidence, and early answer captures show that models do not always follow them.

No new database, model download, embedding build, corpus rewrite or public API endpoint was introduced. The graph is a source-anchored, AI-curated manifest stored in JSON alongside the existing SQLite/Chroma system. Graph curation is currently manual with AI assistance; automatic relationship extraction and an approval workflow are future work.

## Controlled retrieval results

The [40-case catalogue](../evaluation/GRAPH_PILOT_V2_CASEBOOK.md) contains 28 substantive questions and 12 routing/filter controls. The substantive questions require **78 source-passage anchors**; several questions need more than one. Two questions also test disclosure of missing intermediate sources. This is a development set co-designed with the graph, not an independent or held-out test.

| Measure | BM25 baseline | BM25 + graph | Hybrid + reranker | Hybrid + reranker + graph |
|---|---:|---:|---:|---:|
| Required anchors found | 60/78 | 78/78 | 69/78 | 78/78 |
| Questions with all required anchors | 13/28 | 28/28 | 21/28 | 28/28 |
| Routing/filter controls | 12/12 | 12/12 | 12/12 | 12/12 |
| Required source gaps disclosed | 0/2 | 2/2 | 0/2 | 2/2 |

Saved evidence: [BM25 comparison](../evaluation/graph_runs/20261014T035301027243Z/summary.md), [hybrid comparison](../evaluation/graph_runs/20261014T035334060477Z/summary.md). Adjacent `capture.json` files retain every response, trace, configuration, corpus/input hashes and code hashes. The hybrid run also records installed model identities. Both completed without fallback and with unchanged input snapshots.

The median hybrid retrieval time for substantive questions was 1.339 seconds without the overlay and 1.353 seconds with it. This single run includes caching/warm-up effects and is not a general performance guarantee. Retrieval counts are not answer correctness, faithfulness or RAGAS scores. More context can still introduce noise or displace other useful passages.

An initial BM25 capture (`20261014T035219042801Z`) was interrupted by a Windows file-write error. It remains incomplete and is excluded. Capture writes now use a temporary file, atomic replacement and bounded retry so a transient lock does not destroy the previous complete capture.

A later final-code attempt (`20261014T165638455543Z`) found Ollama stopped and used keyword fallback. The runner marked it invalid for a hybrid comparison; its latency and retrieval results are excluded from the hybrid claims above. It remains saved as an outage observation. Ollama was restarted before the final live rerun.

The [final live hybrid rerun](../evaluation/graph_runs/20261014T165948998153Z/summary.md), with the source-quality gate enabled, reproduced **69/78 versus 78/78 raw anchors**, **21/28 versus 28/28 complete substantive cases**, and **12/12 controls in both arms**, without model fallback or changed input snapshots. Because one expected anchor occurs in the known-corrupt fragment, **model-usable anchors are 68/78 versus 77/78**. Keeping that fragment inspectable does not make it suitable for generation. Median substantive retrieval time was 1.392 seconds baseline and 1.331 seconds graph; this single-run difference is not evidence of a speed improvement.

## Source-quality findings

- **OC76B:** an inventory record exists, but public text is unavailable in this corpus. OC76C references it. The assistant can discuss OC76C's own text while acknowledging the missing intermediate history.
- **OC141:** OC141A and OC141C are referenced but were not found in the index. OC141E has no public text. The available OC141 is an updated February 2026 snapshot, not an archived original 2022 version.
- **OC185B:** a visual check of the saved PDF's first page shows a rupee sign followed by “5 lakh” in its tax reference. The indexed OCR reads “25 lakh”. This is an extraction error, not evidence of a new limit. A warning did not prevent the model from repeating the error. A new source-quality gate therefore excludes that known-corrupt fragment from drafting, citation acceptance and support/completeness checks in both ordinary and graph-assisted answers. The raw excerpt remains visible, labelled as excluded. A separately versioned extraction repair remains necessary.
- **OC71 / OC128:** imported passages contain incomplete lines. The graph does not reconstruct missing words or certify completeness.

The [AI visual-check record](../evaluation/graph_source_review_20261014.json) records the inspected OC185B and OC76C pages and PDF hashes. This is not independent human verification. The source corpus was deliberately preserved for the paired experiment.

The gate uses `source_quality_flags.json`: document identity, page, exact quoted error and a page-content hash. Unaffected fragments remain eligible. If the page changes, it is conservatively excluded until its flag is reviewed. This is a targeted quarantine of a demonstrated extraction defect, not a general OCR-error detector or a hardcoded answer. No default model or corpus configuration was changed.

## Generated-answer findings

Eight paired model scenarios were captured [before the source-quality guard](../evaluation/graph_runs/20261014T035607409692Z/summary.md), covering the original two topics and the four added topics. Both arms produced six draft and two incomplete statuses; **status is not an accuracy score**. The graph recovered 22/22 required anchors versus 20/22 for the baseline, but still produced an incorrect tax-limit claim from the OCR error. The automated support checker accepted that claim. Date-comparison checks and split-table citation selection also withheld useful statements despite retrieval of the relevant passages.

After the quarantine fix, [two paired scenarios were rerun](../evaluation/graph_runs/20261014T040441443135Z/summary.md):

| Case | Observed result | Remaining limitation |
|---|---|---|
| Tax amount / LIMIT-04 | Both answers rejected the erroneous 25 lakh interpretation and cited the 5 lakh tax provision in the saved sources | The graph answer incorrectly extended a 10 lakh cumulative table entry to tax payments generally. That entry concerns the GeM EMD category. The checker accepted this scope error; the answer is not a full pass. |
| IPO / IPO-02 | Both distinguished a 24-hour capital-market total from a single IPO mandate ceiling. The graph also retrieved and cited the historical IPO-specific sources | Baseline already made the central distinction, so this does not prove improved answer accuracy. The graph draft withheld one claim and its additional completeness review was unavailable. |

These are AI inspection findings, with unfilled independent-review worksheets beside the captures. Full response objects retain visible claims, withheld claims, citations and diagnostics. The known OCR claim was fixed; broad reliability was not established. Some completeness reviews were unavailable even though generation itself completed without model fallback. Further work must address scope-aware table interpretation and independently review answers rather than relying on the same model's support verdict.

The generated-answer worksheets were [re-exported from unchanged captures](../evaluation/graph_runs/REVIEW_WORKSHEET_NOTE.md) to include visible claims and citation IDs, rather than only the draft-status preface. Reviewer verdicts remain blank. This export-only runner change followed the final retrieval capture and does not change its recorded results.

## Try and reproduce

Double-click `run-graph-pilot.cmd`, keep the window open and use **http://127.0.0.1:8769** after startup. Use **UPI**, **Related** context and a topic question. The launcher now selects the extended v2 graph, using a copy of the normal configuration. The ordinary launcher remains unchanged.

Suggested questions:

- What UPI IPO mandate limit is supported by the available circulars, and which specific circular establishes it?
- Does the 10 lakh cumulative Capital Market figure in UPI OC185B make a single IPO mandate limit 10 lakh?
- Under UPI OC76 series, does the domestic QR share and pay limit permit international UPI Global P2M?
- Do UPI OC141 rent-payment restrictions apply to one-time or recurring mandates?
- Distinguish the OC185B credit-card bill-payment transaction ceiling from the 24-hour cumulative ceiling.

```powershell
.\.venv\Scripts\python.exe -X utf8 evaluation/graph_pilot_eval.py --method hybrid --graph pilot/upi_extended_graph_v2.json --dataset evaluation/graph_pilot_cases_v2.json
.\.venv\Scripts\python.exe -X utf8 evaluation/graph_pilot_eval.py --method bm25 --no-rerank --graph pilot/upi_extended_graph_v2.json --dataset evaluation/graph_pilot_cases_v2.json
```

For the earlier graph, run `tools/serve_graph_pilot.py --graph pilot/upi_128_226_graph_v1.json`. Original frozen v1 captures remain available; code changes after those captures are separately fingerprinted in v2 runs.

Validation: [303 Python tests passed](../evaluation/validation_runs/20261014T165836278929Z/validation.json), including 20 graph-specific and six source-quality-gate tests, with zero failures/skips. They cover stale anchors, provenance, loops, depth/budget bounds, product/topic separation, missing sources, companion citations, preservation of strict/selected routes, raw-source retention, corrupt-fragment exclusion and abstention when no clean context remains. Frontend syntax and both JavaScript rendering suites passed.

The [browser check](../evaluation/validation_runs/20261014T165836278929Z/browser-validation.json) exercised the IPO question, visible citations, linked OC127 source reader, graph coverage panel and corrupt-source exclusion label. After Ollama recovery the answer completed in 33.391 seconds and distinguished the cumulative figure from the transaction limit; its additional completeness check was unavailable and visibly disclosed. [Question/answer screenshot](images/graph-pilot-ipo-20261014.png) · [Source-reader screenshot](images/graph-pilot-source-20261014.png). Browser verification covers this journey, not a new full-product usability audit.

## Adoption gate

The evidence supports using graph assistance as an additional retrieval layer for curated, source-checked topics. It does not yet support claiming that all such questions are reliably answered, or enabling it for an unreviewed full corpus.

Before default rollout: repair the demonstrated OCR discrepancy through a versioned import, improve split-table citation handling and date-comparison checks, independently score unseen answers, review unresolved source links, and check for irrelevant additions and false conflict warnings. Expansion should be driven by source-supported relationships, not hardcoded publisher precedence or a largest/latest-number rule. Graph assistance remains opt-in while these gates are open. No GitHub publication was performed.
