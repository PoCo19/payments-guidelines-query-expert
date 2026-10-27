# IPO answer regression investigation — 17 October 2026

Question reported by the user:

> Does the 10 lakh cumulative Capital Market figure in UPI OC185B make a single IPO mandate limit 10 lakh?

## What failed

The failure was reproduced against the running application on port 8765, using hybrid retrieval, reranking, related context and no product filter. Both experimental settings were absent from configuration and therefore **off**: `contextual_bm25_enabled=False`, `structured_evidence_enabled=False`. Graph-assisted retrieval was active.

The [before-fix response](../evaluation/ipo_regression_20261017/live_exact_before.json) retrieved 18 passages, including OC71 (S8), OC127 (S2), OC185A (S3) and OC185B (S1). All 14 anchors expected by the triggered graph topics were present. The answer failure was not caused by an empty search or lost embeddings.

1. The generator drafted a valid distinction between the cumulative Capital Market figure and a single IPO mandate.
2. The deterministic scope guard treated the compact reference **OC185B** as a product acronym. Because the source metadata says `185B` and its text does not contain that exact compact word, the guard wrongly withheld the statement.
3. A second draft statement incorrectly attributed an IPO-specific rule to the general OC185B table. Withholding that attribution was appropriate.
4. Both attempted repairs timed out in the first capture. No statement remained, producing the reported empty answer.

After the first guard fix, the valid distinction passed; the incorrect attribution still failed. A later repair correctly located the specific rule in OC127 but hit another false rejection: the imported source joins the words as **UPIbasedASBAIPO**, so a word-boundary-only lookup treated **ASBA** as absent.

The UPI-filtered variant exposed a third failure: the model put citation labels such as `(S1)` inside claim text. Acronym and numeric validators interpreted those labels as factual content. This could withhold an otherwise supported historical explanation even though structured citations were valid.

## Corrections and boundaries

- Exclude only circular-reference spans actually matched to cited metadata from acronym checking. This handles compact, spaced and hyphenated forms without globally exempting arbitrary identifiers.
- Recognise literal uppercase scope terms at case boundaries in joined OCR words. This permits semantic review; it does not assert that substring matching proves a claim. Ordinary word substrings such as RDS in CARDS remain rejected.
- Apply the same source-ownership checks to singular and plural acronyms (`IPO` / `IPOs`). Recognise acronym/code joins (`MCC6211`) and literal joined acronyms when both are separately named in the claim. Each statement still requires semantic support.
- Use that same scope lookup in repair navigation hints so the repair model can locate the source.
- Remove redundant bracketed citation markers only when they identify evidence already cited by that claim. Keep the structured citations and original wording in the audit record. Unknown citation labels, ordinary numbers and factual response codes remain subject to validation.
- Clarify the generation instruction for proposed changes: explain each document's relevant rule separately before comparing them. No question-specific answer, issuer hierarchy or statutory precedence was hardcoded.
- Cover `beyond which` in the existing above-ceiling extrapolation guard after the summary control exposed that phrase gap.

Original text, embeddings, graph data, context budgets and model settings remain unchanged. Citation validation, monetary ownership checks, table-scope checks, semantic support checks and bounded repair remain enabled.

Failed attempts are retained, including a prompt variant that produced a plausible-looking but jointly misattributed claim. It is not counted as a successful fix merely because the local checker accepted it.

## Source-grounded review criteria

The answer should distinguish the OC185B Capital Market cumulative 24-hour measure from a single IPO mandate. If it gives the IPO-specific amount or history, it must attribute those statements to their own evidence: the original OC71 passage, the OC127 enhancement and any relevant OC185A reference. A shared merchant category alone does not establish that one measure replaces another. Do not reconstruct the incomplete execution line in OC71.

This is a review of the imported snapshot, not a determination that all applicable documents have been collected or that the latest law has been independently verified.

## Verification

The [six live journeys](../evaluation/ipo_regression_20261017/live_20261017T073428Z.json) were captured before the final inline-marker correction. They reproduce the remaining UPI-filter failure and preserve the successful default-filter answer, rather than hiding the failed variant. The default-filter answer correctly distinguishes the cumulative figure and attributes the specific IPO rule to OC127. The spaced-reference answer also retains the central distinction and OC127 citation, although an additional statement is withheld. These answers do not always reproduce the full OC71 history.

The summary control now withholds the unsupported above-ceiling inference; it remains incomplete because repair does not recover that clause. The notification control no longer asserts that the post-debit message may be skipped, but it still fails to retrieve and explain the actual post-notification clause. The baseline chronology control correctly separates the earlier exclusion from the later inclusion. These are observations, not proof that those broader failure classes are solved.

All **365 Python regression tests passed** after the final code changes: [full log](../evaluation/ipo_regression_20261017/full-regression-complete.txt). Fifteen focused regression tests cover reference spelling, source ownership, plural scopes, OCR joins, numeric checks, inline citations, semantic rejection and above-ceiling statements. Passing tests establish those software behaviours, not universal answer accuracy.

The final frontend check regenerated the exact question in the existing All products view. It visibly displayed the cumulative-versus-single distinction and separately attributed the IPO-specific rule to OC127: [browser record](../evaluation/ipo_regression_20261017/browser-final.txt), [screenshot](images/ipo-answer-verified-20261017.png). The final API captures are saved in [final_verification.json](../evaluation/ipo_regression_20261017/final_verification.json). The corpus inputs and configuration hashes were checked against the broader paired run and remain unchanged.

Both final API variants (All products and UPI) returned non-empty drafts with no withheld claims. The UPI-filtered capture retained OC71's earlier amount, OC127's enhancement and OC185A's unchanged reference. The core distinction is restored. This does not make every sentence ideal: the historical claims add broader interpretive conclusions, and the final bank-discretion sentence is unnecessary and loosely framed. Those wording/entailment issues remain part of the quality review, despite the internal supported labels. The default view's shorter answer is clearer about the central distinction but omits that full history.

The separate completeness reviewer still emits a questionable conflict warning even when the displayed answer distinguishes the two measures. This warning is retained as a review finding; it does not establish that the distinction is wrong. Full historical detail and review consistency remain quality limitations.

## Wider quality conclusion

The [expanded evaluation](EXPANDED_EVIDENCE_EVALUATION_20261017.md) found failures beyond this specific bug, including wrongly extending notification exemptions and reversing amendment chronology. Some were accepted by the same model used to check support. Therefore **we cannot confirm overall answer quality is consistently improved or production-ready**. The optional experiments remain off. Graph-assisted retrieval remains on because it supplies linked evidence; it does not resolve interpretation errors by itself.
