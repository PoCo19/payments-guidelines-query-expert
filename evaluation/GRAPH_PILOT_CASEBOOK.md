# Graph pilot question and evidence catalogue

AI-assisted development cases, co-designed with the graph. Independent review pending. These are separate from the original 50-question evaluation.

Twelve substantive questions need 39 total passage anchors; eight additional cases exercise routing and filters. All expected text is a locator in unchanged extracted source text, not a corrected transcription.

## BIO-01

What is the UPI on-device biometric transaction limit, and when did it change?

- **bio_original** — 2025-OC-226, page 1: “This facility shall initially be available for transactions up to Rs. 5,000.”
- **bio_amendment** — 2026-OC-226A, page 1: “enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.”

Reviewer / verdict: **pending**.

## BIO-02

Does UPI OC 226A remove the device security validations and customer consent requirements?

- **bio_amendment** — 2026-OC-226A, page 1: “enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.”
- **bio_continuity** — 2026-OC-226A, page 1: “All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable”
- **bio_security** — 2025-OC-226, page 1: “restricting usage on rooted or jail-broken devices”
- **bio_consent** — 2025-OC-226, page 2: “shall ensure explicit customer consent is obtained”

Reviewer / verdict: **pending**.

## BIO-03

Under UPI biometric authentication, what happens after a UPI PIN reset? Does the limit addendum change that?

- **bio_reset** — 2025-OC-226, page 2: “shall disable this method for the account for all UPI Applications”
- **bio_amendment** — 2026-OC-226A, page 1: “enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.”
- **bio_continuity** — 2026-OC-226A, page 1: “All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable”

Reviewer / verdict: **pending**.

## BIO-04

According to UPI OC 226 and its addendum, was the new biometric limit effective on 15 July 2026 or only later?

- **bio_original** — 2025-OC-226, page 1: “This facility shall initially be available for transactions up to Rs. 5,000.”
- **bio_amendment** — 2026-OC-226A, page 1: “enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.”

Reviewer / verdict: **pending**.

## BIO-05

Is UIDAI Face Authentication for UPI PIN setup the same as on-device biometric transaction authentication?

- **bio_pin_setup** — 2025-OC-226, page 1: “UIDAI Face Authentication shall be introduced as an additional option, for UPI PIN Set/Re-Set”
- **bio_original** — 2025-OC-226, page 1: “This facility shall initially be available for transactions up to Rs. 5,000.”
- **bio_amendment** — 2026-OC-226A, page 1: “enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.”

Reviewer / verdict: **pending**.

## BIO-06

After the UPI biometric limit change, what do the sources say about key rotation and inactivity?

- **bio_rotation** — 2025-OC-226, page 2: “before one year of biometric enablement.”
- **bio_inactive** — 2025-OC-226, page 2: “activated only upon customer confirmation.”
- **bio_continuity** — 2026-OC-226A, page 1: “All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable”

Reviewer / verdict: **pending**.

## DD-01

How did UPI deemed debit treatment for response codes 59 and K1 change from OC 128 to OC 128A?

- **dd_original** — npci-source-1a52e564b7b10a4cc8b13dde, page 1: “shall be considered as failure and shall not be treated as Deemed Debit.”
- **dd_original_codes** — npci-source-1a52e564b7b10a4cc8b13dde, page 1: “VO- Payment stopped by court order Remitter Bank VH- Mandate signature is tampered or corrupt”
- **dd_amendment** — 2026-OC-128A, page 1: “response codes VH, K1, 59, and VO were excluded from the deemed debit scope.”
- **dd_effective** — 2026-OC-128A, page 2: “The changes in deemed debit applicability in the URCS system will be effective from”

Reviewer / verdict: **pending**.

## DD-02

For UPI deemed debit, do VO and VH declines have the same treatment for MCC 6211 and other OTM use cases?

- **dd_amendment** — 2026-OC-128A, page 1: “response codes VH, K1, 59, and VO were excluded from the deemed debit scope.”
- **dd_capital_market** — 2026-OC-128A, page 1: “Acquirer / Payee may claim the transaction amount if it is as per the mandate created;”
- **dd_other_otm** — 2026-OC-128A, page 1: “are to be considered as declined and no service should be rendered by the Acquirer/Payee.”
- **dd_effective** — 2026-OC-128A, page 2: “The changes in deemed debit applicability in the URCS system will be effective from”

Reviewer / verdict: **pending**.

## DD-03

What reconciliation and report checks accompany the UPI deemed debit changes?

- **dd_amendment** — 2026-OC-128A, page 1: “response codes VH, K1, 59, and VO were excluded from the deemed debit scope.”
- **dd_report** — 2026-OC-128A, page 2: “use the Deemed Debit report and raw files for reconciliation”
- **dd_reconciliation** — 2026-OC-128A, page 2: “perform three (3) way reconciliation”

Reviewer / verdict: **pending**.

## DD-04

For UPI deemed debit mandate execution, what are the expiry, BGGD validity and duplicate execution conditions?

- **dd_amendment** — 2026-OC-128A, page 1: “response codes VH, K1, 59, and VO were excluded from the deemed debit scope.”
- **dd_expiry** — 2026-OC-128A, page 2: “auto unblocked upon expiry of the mandate period.”
- **dd_claim_window** — 2026-OC-128A, page 2: “within the mandate validity period.”
- **dd_execution** — 2026-OC-128A, page 2: “no duplicate executions are processed.”

Reviewer / verdict: **pending**.

## DD-05

When do the UPI OC 128A deemed debit changes take effect, and what did OC 128 exclude?

- **dd_original** — npci-source-1a52e564b7b10a4cc8b13dde, page 1: “shall be considered as failure and shall not be treated as Deemed Debit.”
- **dd_original_codes** — npci-source-1a52e564b7b10a4cc8b13dde, page 1: “VO- Payment stopped by court order Remitter Bank VH- Mandate signature is tampered or corrupt”
- **dd_amendment** — 2026-OC-128A, page 1: “response codes VH, K1, 59, and VO were excluded from the deemed debit scope.”
- **dd_effective** — 2026-OC-128A, page 2: “The changes in deemed debit applicability in the URCS system will be effective from”

Reviewer / verdict: **pending**.

## DD-06

Explain the UPI deemed debit response-code changes and the settlement scope in the available circulars.

- **dd_original** — npci-source-1a52e564b7b10a4cc8b13dde, page 1: “shall be considered as failure and shall not be treated as Deemed Debit.”
- **dd_amendment** — 2026-OC-128A, page 1: “response codes VH, K1, 59, and VO were excluded from the deemed debit scope.”
- **dd_settlement** — 2026-OC-128A, page 1: “shall continue to be treated as Deemed Debit and settlement shall be done by debiting respective Remitter bank”

Reviewer / verdict: **pending**.

## CTRL-01

Explain OC 226

Control: clarification. This does not establish general answer correctness.


Reviewer / verdict: **pending**.

## CTRL-02

Explain UPI OC 9999

Control: empty. This does not establish general answer correctness.


Reviewer / verdict: **pending**.

## CTRL-03

What is the biometric transaction limit?

Control: graph_inactive. This does not establish general answer correctness.


Reviewer / verdict: **pending**.

## CTRL-04

Explain deemed approval under UPI OC 39A

Control: graph_inactive. This does not establish general answer correctness.


Reviewer / verdict: **pending**.

## CTRL-05

Summarise selected circular

Control: unchanged. This does not establish general answer correctness.


Reviewer / verdict: **pending**.

## CTRL-06

What does UPI OC 128 say about deemed debit?

Control: unchanged. This does not establish general answer correctness.


Reviewer / verdict: **pending**.

## CTRL-07

What is the UPI biometric transaction limit?

Control: cutoff. This does not establish general answer correctness.


Reviewer / verdict: **pending**.

## CTRL-08

What are UPI Tap & Pay limits?

Control: graph_inactive. This does not establish general answer correctness.


Reviewer / verdict: **pending**.
