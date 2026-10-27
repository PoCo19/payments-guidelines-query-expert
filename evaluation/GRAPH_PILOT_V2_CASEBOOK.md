# Extended graph pilot: questions and source anchors

14 October 2026. AI-assisted development set, co-designed with the graph; independent review pending. The original 50-question set is unchanged.

40 cases: 28 substantive questions, requiring 78 passage anchors in total, and 12 routing/filter controls. Two substantive cases additionally require explicit source-gap disclosure.

Graph and expected anchors are not independent; these results cannot establish held-out answer accuracy.

## BIO-01

What is the UPI on-device biometric transaction limit, and when did it change?

- **bio_original**: 2025-OC-226, page 1 — This facility shall initially be available for transactions up to Rs. 5,000.
- **bio_amendment**: 2026-OC-226A, page 1 — enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.

Independent reviewer and verdict: **pending**.

## BIO-02

Does UPI OC 226A remove the device security validations and customer consent requirements?

- **bio_amendment**: 2026-OC-226A, page 1 — enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.
- **bio_continuity**: 2026-OC-226A, page 1 — All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable
- **bio_security**: 2025-OC-226, page 1 — restricting usage on rooted or jail-broken devices
- **bio_consent**: 2025-OC-226, page 2 — shall ensure explicit customer consent is obtained

Independent reviewer and verdict: **pending**.

## BIO-03

Under UPI biometric authentication, what happens after a UPI PIN reset? Does the limit addendum change that?

- **bio_reset**: 2025-OC-226, page 2 — shall disable this method for the account for all UPI Applications
- **bio_amendment**: 2026-OC-226A, page 1 — enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.
- **bio_continuity**: 2026-OC-226A, page 1 — All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable

Independent reviewer and verdict: **pending**.

## BIO-04

According to UPI OC 226 and its addendum, was the new biometric limit effective on 15 July 2026 or only later?

- **bio_original**: 2025-OC-226, page 1 — This facility shall initially be available for transactions up to Rs. 5,000.
- **bio_amendment**: 2026-OC-226A, page 1 — enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.

Independent reviewer and verdict: **pending**.

## BIO-05

Is UIDAI Face Authentication for UPI PIN setup the same as on-device biometric transaction authentication?

- **bio_pin_setup**: 2025-OC-226, page 1 — UIDAI Face Authentication shall be introduced as an additional option, for UPI PIN Set/Re-Set
- **bio_original**: 2025-OC-226, page 1 — This facility shall initially be available for transactions up to Rs. 5,000.
- **bio_amendment**: 2026-OC-226A, page 1 — enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.

Independent reviewer and verdict: **pending**.

## BIO-06

After the UPI biometric limit change, what do the sources say about key rotation and inactivity?

- **bio_rotation**: 2025-OC-226, page 2 — before one year of biometric enablement.
- **bio_inactive**: 2025-OC-226, page 2 — activated only upon customer confirmation.
- **bio_continuity**: 2026-OC-226A, page 1 — All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable

Independent reviewer and verdict: **pending**.

## DD-01

How did UPI deemed debit treatment for response codes 59 and K1 change from OC 128 to OC 128A?

- **dd_original**: npci-source-1a52e564b7b10a4cc8b13dde, page 1 — shall be considered as failure and shall not be treated as Deemed Debit.
- **dd_original_codes**: npci-source-1a52e564b7b10a4cc8b13dde, page 1 — VO- Payment stopped by court order Remitter Bank VH- Mandate signature is tampered or corrupt
- **dd_amendment**: 2026-OC-128A, page 1 — response codes VH, K1, 59, and VO were excluded from the deemed debit scope.
- **dd_effective**: 2026-OC-128A, page 2 — The changes in deemed debit applicability in the URCS system will be effective from

Independent reviewer and verdict: **pending**.

## DD-02

For UPI deemed debit, do VO and VH declines have the same treatment for MCC 6211 and other OTM use cases?

- **dd_amendment**: 2026-OC-128A, page 1 — response codes VH, K1, 59, and VO were excluded from the deemed debit scope.
- **dd_capital_market**: 2026-OC-128A, page 1 — Acquirer / Payee may claim the transaction amount if it is as per the mandate created;
- **dd_other_otm**: 2026-OC-128A, page 1 — are to be considered as declined and no service should be rendered by the Acquirer/Payee.
- **dd_effective**: 2026-OC-128A, page 2 — The changes in deemed debit applicability in the URCS system will be effective from

Independent reviewer and verdict: **pending**.

## DD-03

What reconciliation and report checks accompany the UPI deemed debit changes?

- **dd_amendment**: 2026-OC-128A, page 1 — response codes VH, K1, 59, and VO were excluded from the deemed debit scope.
- **dd_report**: 2026-OC-128A, page 2 — use the Deemed Debit report and raw files for reconciliation
- **dd_reconciliation**: 2026-OC-128A, page 2 — perform three (3) way reconciliation

Independent reviewer and verdict: **pending**.

## DD-04

For UPI deemed debit mandate execution, what are the expiry, BGGD validity and duplicate execution conditions?

- **dd_amendment**: 2026-OC-128A, page 1 — response codes VH, K1, 59, and VO were excluded from the deemed debit scope.
- **dd_expiry**: 2026-OC-128A, page 2 — auto unblocked upon expiry of the mandate period.
- **dd_claim_window**: 2026-OC-128A, page 2 — within the mandate validity period.
- **dd_execution**: 2026-OC-128A, page 2 — no duplicate executions are processed.

Independent reviewer and verdict: **pending**.

## DD-05

When do the UPI OC 128A deemed debit changes take effect, and what did OC 128 exclude?

- **dd_original**: npci-source-1a52e564b7b10a4cc8b13dde, page 1 — shall be considered as failure and shall not be treated as Deemed Debit.
- **dd_original_codes**: npci-source-1a52e564b7b10a4cc8b13dde, page 1 — VO- Payment stopped by court order Remitter Bank VH- Mandate signature is tampered or corrupt
- **dd_amendment**: 2026-OC-128A, page 1 — response codes VH, K1, 59, and VO were excluded from the deemed debit scope.
- **dd_effective**: 2026-OC-128A, page 2 — The changes in deemed debit applicability in the URCS system will be effective from

Independent reviewer and verdict: **pending**.

## DD-06

Explain the UPI deemed debit response-code changes and the settlement scope in the available circulars.

- **dd_original**: npci-source-1a52e564b7b10a4cc8b13dde, page 1 — shall be considered as failure and shall not be treated as Deemed Debit.
- **dd_amendment**: 2026-OC-128A, page 1 — response codes VH, K1, 59, and VO were excluded from the deemed debit scope.
- **dd_settlement**: 2026-OC-128A, page 1 — shall continue to be treated as Deemed Debit and settlement shall be done by debiting respective Remitter bank

Independent reviewer and verdict: **pending**.

## CTRL-01

Explain OC 226

Control expectation: clarification.


Independent reviewer and verdict: **pending**.

## CTRL-02

Explain UPI OC 9999

Control expectation: empty.


Independent reviewer and verdict: **pending**.

## CTRL-03

What is the biometric transaction limit?

Control expectation: graph_inactive.


Independent reviewer and verdict: **pending**.

## CTRL-04

Explain deemed approval under UPI OC 39A

Control expectation: graph_inactive.


Independent reviewer and verdict: **pending**.

## CTRL-05

Summarise selected circular

Control expectation: unchanged.


Independent reviewer and verdict: **pending**.

## CTRL-06

What does UPI OC 128 say about deemed debit?

Control expectation: unchanged.


Independent reviewer and verdict: **pending**.

## CTRL-07

What is the UPI biometric transaction limit?

Control expectation: cutoff.


Independent reviewer and verdict: **pending**.

## CTRL-08

What are UPI Tap & Pay limits?

Control expectation: graph_inactive.


Independent reviewer and verdict: **pending**.

## MODE-01

Under UPI OC 76 series, does the domestic QR share and pay limit also permit international UPI Global P2M?

- **mode_a**: 2024-OC-76A, page 1 — transactions (Initiation mode ‘04’ and ‘05’) shall be
- **mode_c_domestic**: 2025-OC-76C, page 2 — 2000/- for all P2M (non-verified offline merchants)
- **mode_c_global**: 2025-OC-76C, page 2 — QR share & Pay shall not be allowed for all (Modification for International) UPI Global P2M transactions

Independent reviewer and verdict: **pending**.

## MODE-02

How did UPI OC 76A and OC 76C treat P2P intent initiation modes 04 and 05?

- **mode_a**: 2024-OC-76A, page 1 — transactions (Initiation mode ‘04’ and ‘05’) shall be
- **mode_c_ref**: 2025-OC-76C, page 1 — NPCI/UPI/2024-25/OC76B dated 23 August 2024

Independent reviewer and verdict: **pending**.

## MODE-03

What do UPI OC 76 and its addenda say about wallet load through collect and QR share modes?

- **mode_original**: npci-source-1ab364443958f0c6fcad0acf, page 2 — disable all Wallet loads (MCC 6540) through Collect requests.
- **mode_a**: 2024-OC-76A, page 1 — transactions (Initiation mode ‘04’ and ‘05’) shall be
- **mode_c_global**: 2025-OC-76C, page 2 — QR share & Pay shall not be allowed for all (Modification for International) UPI Global P2M transactions

Independent reviewer and verdict: **pending**.

## MODE-04

Can you confirm the complete change history of the UPI OC 76 series, including unavailable intermediate sources?

Required gap disclosure: OC76B.

- **mode_c_ref**: 2025-OC-76C, page 1 — NPCI/UPI/2024-25/OC76B dated 23 August 2024

Independent reviewer and verdict: **pending**.

## SAFE-01

Does UPI OC 141D add Bharat QR for rent, and how does the updated OC 141 relate to it?

- **safe_rent**: npci-source-853953bec76d31753dfa5904, page 1 — 141D/2024-25(Addendum) dated 2nd April 2025.
- **safe_d_rent**: 2025-OC-141D, page 1 — transactions will be allowed on initiation mode 03(Bharat QR).
- **safe_d_mandate**: 2025-OC-141D, page 1 — This circular is not applicable for Mandate transactions (One time and Recurring Mandates)

Independent reviewer and verdict: **pending**.

## SAFE-02

Do the rent payment mode restrictions in UPI OC 141 and OC 141D also apply to one-time or recurring mandates?

- **safe_mandate**: npci-source-853953bec76d31753dfa5904, page 2 — This circular is not applicable for Mandate Transactions (One time and Recurring Mandates)
- **safe_d_mandate**: 2025-OC-141D, page 1 — This circular is not applicable for Mandate transactions (One time and Recurring Mandates)

Independent reviewer and verdict: **pending**.

## SAFE-03

What does UPI OC 141B say about collect for digital gold and silver on Android?

- **safe_b**: npci-source-ab9a46ef29ebae2022dbb869, page 1 — not be allowed from 10th November 2022 for android users.

Independent reviewer and verdict: **pending**.

## SAFE-04

Can the available updated UPI OC 141 be used to quote its exact original 2022 wording?

Required gap disclosure: OC141A.

- **safe_snapshot**: npci-source-853953bec76d31753dfa5904, page 1 — (Updated as on 23rd February 2026*)

Independent reviewer and verdict: **pending**.

## LIMIT-01

Did UPI OC 185A change the hospital and education limit, or introduce tax-payment coverage?

- **limits_hospital**: 2023-UPI-185, page 1 — lakhs for merchants under categories aligned to hospitals and educational services.
- **limits_tax**: 2024-OC-185A, page 1 — lakhs for entities under categories aligned to tax payments.
- **limits_annex**: 2024-OC-185A, page 2 — Purpose Code — 01 (IPO), 25 (RDS) | (Existing - No Change)

Independent reviewer and verdict: **pending**.

## LIMIT-02

Do the higher UPI merchant limits under OC 185B apply to every merchant and P2P transfer, and can banks set lower limits?

- **limits_verified**: 2025-OC-185B, page 1 — applicable for merchants which are categorised as ‘Verified Merchant’.
- **limits_bank**: 2025-OC-185B, page 1 — within the overall ceilings prescribed by NPCI.
- **limits_p2p**: 2025-OC-185B, page 1 — The per transaction limit for P2P shall continue as per the extant guidelines.
- **limits_capital**: 2025-OC-185B, page 2 — | 1 | Capital Market | 6211 | ₹5 Lakh | ₹10 Lakh |

Independent reviewer and verdict: **pending**.

## LIMIT-03

Under UPI OC 185B, distinguish the credit card bill payment per-transaction ceiling from its 24-hour cumulative limit.

- **limits_cc**: 2025-OC-185B, page 2 — | 5 | Credit Card Bill Payments | 5413 | ₹5 Lakh | ₹6 Lakh |
- **limits_cumulative**: 2025-OC-185B, page 2 — Issuing banks are required to ensure that such cumulative limits are kept at their end.

Independent reviewer and verdict: **pending**.

## LIMIT-04

Does UPI tax payment have a 25 lakh limit in the available OC 185 series? Check the source quality and category.

- **limits_tax**: 2024-OC-185A, page 1 — lakhs for entities under categories aligned to tax payments.
- **limits_tax_mcc**: 2024-OC-185A, page 1 — 9311’ strictly adheres to the tax payments only.
- **limits_ref**: 2025-OC-185B, page 1 — Vide reference to NPCI/UPI/2024-25/0C/185 A

Independent reviewer and verdict: **pending**.

## IPO-01

What UPI IPO mandate limit is supported by the available circulars, and which specific circular establishes it?

- **ipo_enhanced**: npci-source-4e6fac099b791778ded35153, page 1 — now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.
- **limits_annex**: 2024-OC-185A, page 2 — Purpose Code — 01 (IPO), 25 (RDS) | (Existing - No Change)

Independent reviewer and verdict: **pending**.

## IPO-02

Does the 10 lakh cumulative Capital Market figure in UPI OC 185B make a single IPO mandate limit 10 lakh?

- **ipo_enhanced**: npci-source-4e6fac099b791778ded35153, page 1 — now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.
- **limits_annex**: 2024-OC-185A, page 2 — Purpose Code — 01 (IPO), 25 (RDS) | (Existing - No Change)
- **limits_capital**: 2025-OC-185B, page 2 — | 1 | Capital Market | 6211 | ₹5 Lakh | ₹10 Lakh |
- **limits_bank**: 2025-OC-185B, page 1 — within the overall ceilings prescribed by NPCI.

Independent reviewer and verdict: **pending**.

## IPO-03

Explain the UPI ASBA IPO limit history from the older 2 lakh limit to the later enhancement and retained annexure reference.

- **ipo_original**: npci-source-9c7b5f01193a8e2a82195b29, page 1 — maintain the per transaction limit of Rs. 2 lakhs for UPl based ASBA transactions
- **ipo_enhanced**: npci-source-4e6fac099b791778ded35153, page 1 — now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.
- **limits_annex**: 2024-OC-185A, page 2 — Purpose Code — 01 (IPO), 25 (RDS) | (Existing - No Change)

Independent reviewer and verdict: **pending**.

## IPO-04

IPO and RBI Retail Direct both use MCC 6211. Do the UPI sources give them the same purpose code?

- **ipo_enhanced**: npci-source-4e6fac099b791778ded35153, page 1 — now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.
- **limits_annex**: 2024-OC-185A, page 2 — Purpose Code — 01 (IPO), 25 (RDS) | (Existing - No Change)

Independent reviewer and verdict: **pending**.

## EXT-CTRL-01

Explain UPI OC 76B

Control expectation: empty.


Independent reviewer and verdict: **pending**.

## EXT-CTRL-02

What new safeguards did UPI OC 141E introduce?

Control expectation: empty.


Independent reviewer and verdict: **pending**.

## EXT-CTRL-03

What UPI IPO limit is stated by OC 185C?

Control expectation: empty.


Independent reviewer and verdict: **pending**.

## EXT-CTRL-04

Explain RuPay rent payment rules

Control expectation: graph_inactive.


Independent reviewer and verdict: **pending**.
