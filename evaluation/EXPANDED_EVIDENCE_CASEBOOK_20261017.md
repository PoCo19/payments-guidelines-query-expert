# Additional evidence experiment casebook

28 AI-assisted development paraphrases; not an independently reviewed or held-out benchmark. Original datasets are unchanged. Freeze before running. Queries use the normal auto route. Graph cases have an explicit UPI filter; payment cases retain their original filters.

## X-PAY-001 (from PAY-001)

How much money may a fully KYC-verified prepaid wallet hold at once under RBI rules? Is that a transaction ceiling?

The full-KYC PPI maximum outstanding balance is Rs.2,00,000 at any point in time. This is an outstanding-balance limit, not a universal transaction limit or the limit for UPI LITE.

- rbi:ppi:2026-09-30, page 1: The amount outstanding shall not exceed Rs.2,00,000/- at any point of time

## X-PAY-002 (from PAY-002)

We are applying to operate as a non-bank payment aggregator. What net worth do we need initially and by year three, and must we keep it thereafter?

A non-bank PA applicant requires at least Rs.15 crore net-worth when applying and Rs.25 crore by the end of the third financial year of authorisation. The applicable minimum must be maintained on an ongoing basis. Do not generalise this to all payment businesses.

- rbi:payment-aggregators:2025-09-15, page 1: minimum net-worth of ₹15 crore
- rbi:payment-aggregators:2025-09-15, page 1: minimum net-worth of ₹25 crore by the end of third financial year

## X-PAY-003 (from PAY-003)

Which organisations fall within the Reserve Bank bill-payment system directions?

The directions apply to NPCI Bharat Bill Pay Limited (NBBL) and all Bharat Bill Payment Operating Units (BBPOUs). Do not describe every bank or fintech as a BBPOU.

- rbi:bbps:2024-02-29, page 1: All Bharat Bill Payment Operating Units (BBPOUs)

## X-PAY-004 (from PAY-004)

For a small authorised non-bank payment system operator, when does the phased cyber-resilience compliance timetable take effect?

The phased implementation date for small non-bank PSOs is April 1, 2028. The directions apply to authorised non-bank PSOs; the small-PSO date should not be applied to medium or large PSOs.

- rbi:nonbank-pso-cyber:2024-07-30, page 1: April 1, 2028
- rbi:nonbank-pso-cyber:2024-07-30, page 1: all authorised non-bank PSOs

## X-PAY-005 (from PAY-005)

Must a bank use a text-message OTP as its second factor, or can it offer other compliant ways to authenticate a payment?

No. The directions set authentication principles rather than mandating SMS OTP as the only factor. At least two distinct factors are required unless exempted. Issuers may offer compliant choices; for transactions other than card-present transactions, at least one factor must be dynamically created or proven.

- rbi:authentication:2025-09-25, page 1: at least two distinct factors of authentication
- rbi:authentication:2025-09-25, page 1: offer a choice of authentication factors

## X-PAY-006 (from PAY-006)

For recurring debits, distinguish the usual additional-authentication threshold from the exceptions for insurance, mutual funds and credit-card bills.

The general recurring-transaction threshold without AFA is Rs.15,000 per transaction, with AFA above it. Insurance premiums, mutual-fund subscriptions and credit-card bill payments have a Rs.1,00,000 per-transaction threshold. Registration and first-transaction AFA requirements remain separate.

- rbi:e-mandates:2026-04-21, page 1: without AFA up to ₹15,000/- per transaction
- rbi:e-mandates:2026-04-21, page 1: without AFA up to ₹1,00,000/- per transaction

## X-PAY-007 (from PAY-007)

Does a payment-system licence always require the same capital, regardless of the service being operated?

No. The 2026 authorisation directions say the capital requirement follows the guidelines or directions for the specific payment system. They cover both applicants and authorised entities. A PA threshold should not be reused for all systems.

- rbi:authorisation:2026-06-15, page 1: capital requirement shall be in accordance with the Guidelines/ Directions issued for the specific payment system

## X-PAY-008 (from PAY-008)

Who is eligible to seek entry to payment systems under the RBI participation framework, and is that the same as permission to operate one?

The access directions apply to scheduled/licensed banks operating in India and authorised PSPs seeking participation. Actual admission depends on the relevant system criteria. Participation and authorisation to operate a payment system are distinct questions.

- rbi:access-criteria:2021-07-28, page 1: all scheduled/ licensed banks operating in India and authorised payment system providers

## X-PAY-009 (from PAY-009)

Does automatic top-up of FASTag or NCMC require an alert a day before the debit? Explain how the RBI framework and UPI implementation fit together.

RBI exempts registered FASTag and NCMC auto-replenishment e-mandates from pre-transaction notification. NPCI OC 207 implements the exception for NETC FASTag (MCC 4784) and RuPay NCMC (MCC 7412) in UPI Autopay, where replenishment follows the customer-set balance threshold. Other e-mandate requirements continue; this is not an exemption for all recurring payments.

- rbi:e-mandates:2026-04-21, page 1: Pre-transaction notification is not required
- 2024-OC-207, page 1: Exemption from 24-Hours prior Pre-Debit Notification
- 2024-OC-207, page 1: MCC 4784

## X-PAY-010 (from PAY-010)

Are customers required to replace their existing UPI authentication with biometrics? Distinguish RBI principles, PIN setup and transaction authentication.

No. RBI specifies compliant authentication principles, including distinct factors and exceptions. NPCI OC 226 introduces optional additional methods and says users may continue existing methods. Distinguish UIDAI face authentication for PIN set/reset from on-device biometrics for transaction authentication. OC 226 describes an initial Rs.5,000 limit, not a verified current limit.

- rbi:authentication:2025-09-25, page 1: offer a choice of authentication factors
- 2025-OC-226, page 1: These additional methods are optional for the user

## X-PAY-011 (from PAY-011)

Can I apply the full-KYC prepaid-wallet balance ceiling to UPI LITE? Explain the differences in balance and single-payment limits.

No. RBI full-KYC PPIs have a Rs.2,00,000 outstanding-balance ceiling. OC 169A states Rs.1,000 per transaction and Rs.5,000 total for UPI LITE, with online replenishment using AFA. These limits concern different products and cannot be merged into a universal wallet limit.

- rbi:ppi:2026-09-30, page 1: The amount outstanding shall not exceed Rs.2,00,000/-
- 2025-OC-169A, page 1: ₹1,000 per transaction with ₹5,000 being the total limit

## X-PAY-012 (from PAY-012)

Can full-KYC prepaid-wallet holders use third-party UPI apps? Reconcile the RBI PPI directions with the older NPCI issuer-onboarding circular, without assuming blanket supersession.

NPCI OC 134, referring to the November 2021 RBI snapshot, states PPI holders are onboarded by their own issuer and authenticate with existing wallet credentials. The September 2026 RBI snapshot also allows full-KYC PPI discovery through third-party UPI applications, using UPI credentials for those transactions. Preserve version and channel differences; this evidence alone does not prove formal supersession of every provision in OC 134.

- npci-source-01e7e3bc387186fe8cdbcc9a, page 1: PPI holders shall be on-boarded for UPI by their own PPI issuer only.
- rbi:ppi:2026-09-30, page 1: A PPI issuer may also facilitate discovery of its full-KYC PPIs on third-party UPI mobile applications

## X-PAY-013 (from PAY-013)

If the required authentication is completed, may a UPI AutoPay app move a customer mandate on its own? Explain customer initiation and repeat-porting restrictions.

No. RBI requires issuer AFA validation for modification or withdrawal of an existing e-mandate. NPCI OC 223 separately makes mandate porting strictly user-driven, bars inducements and limits porting to once in a rolling 90-day period. Authentication is not permission for app-initiated porting.

- rbi:e-mandates:2026-04-21, page 1: Any modification in, or withdrawal of, an existing e-mandate shall require AFA
- 2025-OC-223, page 1: strictly user-driven
- 2025-OC-223, page 1: once in a rolling 90-day period

## X-PAY-014 (from PAY-014)

For a non-bank PA applicant, how should we read the general payment-system capital framework alongside the payment-aggregator-specific capital milestones?

The generic 2026 authorisation directions defer capital requirements to the specific payment-system guidelines. The PA 2025 directions specify Rs.15 crore at application and Rs.25 crore by the end of the third financial year of authorisation, maintained as applicable. Describe the generic framework and PA-specific rule separately.

- rbi:authorisation:2026-06-15, page 1: capital requirement shall be in accordance with the Guidelines/ Directions
- rbi:payment-aggregators:2025-09-15, page 1: minimum net-worth of ₹15 crore
- rbi:payment-aggregators:2025-09-15, page 1: minimum net-worth of ₹25 crore

## X-PAY-015 (from PAY-015)

If a FASTag or NCMC automatic top-up does not need advance debit notice, can the issuer skip the message after the debit as well?

The RBI e-mandate directions exempt specified auto-replenishment mandates from pre-transaction notification, while separately requiring the issuer to send a post-transaction notification. Do not extend the pre-transaction exemption to post-transaction notices.

- rbi:e-mandates:2026-04-21, page 1: Pre-transaction notification is not required
- rbi:e-mandates:2026-04-21, page 1: An issuer shall send a post-transaction notification

## X-PAY-016 (from PAY-016)

Can every authorised non-bank PSO wait until April 2028 for cyber-resilience compliance? Distinguish operator size.

No. April 1, 2028 is the small non-bank PSO deadline. The phased schedule lists April 1, 2025 for large and April 1, 2026 for medium non-bank PSOs. Retain size classification and applicability to authorised non-bank PSOs.

- rbi:nonbank-pso-cyber:2024-07-30, page 1: April 1, 2025
- rbi:nonbank-pso-cyber:2024-07-30, page 1: April 1, 2026
- rbi:nonbank-pso-cyber:2024-07-30, page 1: April 1, 2028

## X-PAY-017 (from PAY-017)

Historically, what was the first UPI on-device biometric payment ceiling in circular 226, and did it say that ceiling could be reviewed?

OC 226 initially makes on-device biometric authentication available for transactions up to Rs.5,000 and explicitly says the limit will be reviewed based on performance and evaluation. This answers the historical initial-limit question, not the current limit after subsequent documents.

- 2025-OC-226, page 1: initially be available for transactions up to Rs. 5,000
- 2025-OC-226, page 1: The limit shall be reviewed in due course

## X-PAY-018 (from PAY-018)

What exact fraud-score cutoff does our company Acme Payments configure in production to decline a UPI transfer?

The supplied public circular corpus does not establish Acme Payments internal production fraud-score threshold. Abstain from inventing a value and request the approved internal policy.


## X-PAY-019 (from PAY-019)

Give me the private mobile number of Acme Payments on-call incident responder.

This confidential company contact is not established in the available public payment guidelines. State the evidence limitation and do not invent a phone number.


## X-PAY-020 (from PAY-020)

What percentage did Acme Payments private fraud model reduce losses by in September 2026?

The corpus does not contain the company performance measurement needed to answer. Abstain from a numerical performance claim and request the relevant internal evaluation.


## X-BIO-01 (from BIO-01)

For UPI payments approved with biometrics on the device, explain the original ceiling, its later increase and when the change applied.

Address the question using the source-owned reference passages; retain conditions, dates and distinct categories. Do not infer blanket supersession.

- 2025-OC-226, page 1: This facility shall initially be available for transactions up to Rs. 5,000.
- 2026-OC-226A, page 1: enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.

## X-BIO-03 (from BIO-03)

If a customer resets their UPI PIN, what happens to on-device biometric transaction authentication? Does the later ceiling increase remove that condition?

Address the question using the source-owned reference passages; retain conditions, dates and distinct categories. Do not infer blanket supersession.

- 2025-OC-226, page 2: shall disable this method for the account for all UPI Applications
- 2026-OC-226A, page 1: enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.
- 2026-OC-226A, page 1: All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable

## X-DD-01 (from DD-01)

For UPI mandate execution, explain how response codes 59 and K1 were treated before and after the deemed-debit addendum.

Address the question using the source-owned reference passages; retain conditions, dates and distinct categories. Do not infer blanket supersession.

- npci-source-1a52e564b7b10a4cc8b13dde, page 1: shall be considered as failure and shall not be treated as Deemed Debit.
- npci-source-1a52e564b7b10a4cc8b13dde, page 1: VO- Payment stopped by court order Remitter Bank VH- Mandate signature is tampered or corrupt
- 2026-OC-128A, page 1: response codes VH, K1, 59, and VO were excluded from the deemed debit scope.
- 2026-OC-128A, page 2: The changes in deemed debit applicability in the URCS system will be effective from

## X-SAFE-02 (from SAFE-02)

Do UPI rent payment initiation-mode restrictions also govern one-time and recurring mandates, or do the circulars distinguish them?

Address the question using the source-owned reference passages; retain conditions, dates and distinct categories. Do not infer blanket supersession.

- npci-source-853953bec76d31753dfa5904, page 2: This circular is not applicable for Mandate Transactions (One time and Recurring Mandates)
- 2025-OC-141D, page 1: This circular is not applicable for Mandate transactions (One time and Recurring Mandates)

## X-LIMIT-02 (from LIMIT-02)

Are the enhanced UPI merchant payment ceilings available to any merchant or person-to-person transfer? May a bank retain a lower ceiling?

Address the question using the source-owned reference passages; retain conditions, dates and distinct categories. Do not infer blanket supersession.

- 2025-OC-185B, page 1: applicable for merchants which are categorised as ‘Verified Merchant’.
- 2025-OC-185B, page 1: within the overall ceilings prescribed by NPCI.
- 2025-OC-185B, page 1: The per transaction limit for P2P shall continue as per the extant guidelines.
- 2025-OC-185B, page 2: | 1 | Capital Market | 6211 | ₹5 Lakh | ₹10 Lakh |

## X-LIMIT-03 (from LIMIT-03)

For UPI credit-card bill payment, distinguish the ceiling for a single payment from the total permitted over 24 hours.

Address the question using the source-owned reference passages; retain conditions, dates and distinct categories. Do not infer blanket supersession.

- 2025-OC-185B, page 2: | 5 | Credit Card Bill Payments | 5413 | ₹5 Lakh | ₹6 Lakh |
- 2025-OC-185B, page 2: Issuing banks are required to ensure that such cumulative limits are kept at their end.

## X-IPO-03 (from IPO-03)

How did the UPI ASBA IPO mandate ceiling evolve from the earlier two-lakh figure? Identify the later enhancement and explain retained older annexure references.

Address the question using the source-owned reference passages; retain conditions, dates and distinct categories. Do not infer blanket supersession.

- npci-source-9c7b5f01193a8e2a82195b29, page 1: maintain the per transaction limit of Rs. 2 lakhs for UPl based ASBA transactions
- npci-source-4e6fac099b791778ded35153, page 1: now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.
- 2024-OC-185A, page 2: Purpose Code — 01 (IPO), 25 (RDS) | (Existing - No Change)

## X-IPO-04 (from IPO-04)

IPO and RBI Retail Direct share merchant category 6211. Does that mean they also share the same UPI purpose code?

Address the question using the source-owned reference passages; retain conditions, dates and distinct categories. Do not infer blanket supersession.

- npci-source-4e6fac099b791778ded35153, page 1: now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.
- 2024-OC-185A, page 2: Purpose Code — 01 (IPO), 25 (RDS) | (Existing - No Change)
