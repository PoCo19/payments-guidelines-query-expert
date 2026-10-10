# RBI and NPCI evaluation: 20 development questions

AI-assisted draft references; independent source and answer review is pending. This dataset is not held out. RBI page 1 denotes the logical full-text HTML conversion, not a physical PDF page. Source snapshots were collected on 9 October 2026.

17 answerable cases and 3 unavailable-evidence cases. There are 34 required source anchors; a question may require several anchors. Retrieval hit rates measure anchor location, not answer correctness.

Review each source excerpt, expected answer and failure mode before entering reviewer decisions in the generated human_review.csv. Preserve this version; corrections require a new version and checksum.

## PAY-001 — RBI direct

Under the RBI PPI Master Directions updated September 2026, what is the maximum outstanding balance for a full-KYC PPI?

Draft expected answer: The full-KYC PPI maximum outstanding balance is Rs.2,00,000 at any point in time. This is an outstanding-balance limit, not a universal transaction limit or the limit for UPI LITE.

Watch for: Confusing balance and transaction limits.

- [rbi:ppi:2026-09-30](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12156), page 1 (logical_markdown): “The amount outstanding shall not exceed Rs.2,00,000/- at any point of time”

## PAY-002 — RBI direct

What net-worth milestones do RBI Payment Aggregator Directions 2025 specify for a non-bank entity seeking authorisation?

Draft expected answer: A non-bank PA applicant requires at least Rs.15 crore net-worth when applying and Rs.25 crore by the end of the third financial year of authorisation. The applicable minimum must be maintained on an ongoing basis. Do not generalise this to all payment businesses.

Watch for: Omitting the timeline or ongoing requirement.

- [rbi:payment-aggregators:2025-09-15](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12896), page 1 (logical_markdown): “minimum net-worth of ₹15 crore”

- [rbi:payment-aggregators:2025-09-15](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12896), page 1 (logical_markdown): “minimum net-worth of ₹25 crore by the end of third financial year”

## PAY-003 — RBI direct

Who is covered by the RBI Bharat Bill Payment System Directions 2024?

Draft expected answer: The directions apply to NPCI Bharat Bill Pay Limited (NBBL) and all Bharat Bill Payment Operating Units (BBPOUs). Do not describe every bank or fintech as a BBPOU.

Watch for: Expanding applicability beyond the source.

- [rbi:bbps:2024-02-29](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12616), page 1 (logical_markdown): “All Bharat Bill Payment Operating Units (BBPOUs)”

## PAY-004 — RBI direct

Under RBI cyber resilience directions for non-bank PSOs, when must small non-bank PSOs comply?

Draft expected answer: The phased implementation date for small non-bank PSOs is April 1, 2028. The directions apply to authorised non-bank PSOs; the small-PSO date should not be applied to medium or large PSOs.

Watch for: Treating a size-specific deadline as universal.

- [rbi:nonbank-pso-cyber:2024-07-30](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12715), page 1 (logical_markdown): “April 1, 2028”

- [rbi:nonbank-pso-cyber:2024-07-30](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12715), page 1 (logical_markdown): “all authorised non-bank PSOs”

## PAY-005 — RBI direct

Do the RBI Authentication Directions 2025 prescribe SMS OTP as the only permitted additional factor?

Draft expected answer: No. The directions set authentication principles rather than mandating SMS OTP as the only factor. At least two distinct factors are required unless exempted. Issuers may offer compliant choices; for transactions other than card-present transactions, at least one factor must be dynamically created or proven.

Watch for: Omitting exceptions; Claiming all transactions must use OTP.

- [rbi:authentication:2025-09-25](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12898), page 1 (logical_markdown): “at least two distinct factors of authentication”

- [rbi:authentication:2025-09-25](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12898), page 1 (logical_markdown): “offer a choice of authentication factors”

## PAY-006 — RBI direct

What are the general and specified-category thresholds for recurring e-mandate transactions without AFA in the RBI 2026 directions?

Draft expected answer: The general recurring-transaction threshold without AFA is Rs.15,000 per transaction, with AFA above it. Insurance premiums, mutual-fund subscriptions and credit-card bill payments have a Rs.1,00,000 per-transaction threshold. Registration and first-transaction AFA requirements remain separate.

Watch for: Extending the special threshold to every category.

- [rbi:e-mandates:2026-04-21](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13374), page 1 (logical_markdown): “without AFA up to ₹15,000/- per transaction”

- [rbi:e-mandates:2026-04-21](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13374), page 1 (logical_markdown): “without AFA up to ₹1,00,000/- per transaction”

## PAY-007 — RBI direct

Does RBI payment-system authorisation use one capital requirement for every payment system?

Draft expected answer: No. The 2026 authorisation directions say the capital requirement follows the guidelines or directions for the specific payment system. They cover both applicants and authorised entities. A PA threshold should not be reused for all systems.

Watch for: Inventing a universal capital threshold.

- [rbi:authorisation:2026-06-15](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13502), page 1 (logical_markdown): “capital requirement shall be in accordance with the Guidelines/ Directions issued for the specific payment system”

## PAY-008 — RBI direct

Who can use the RBI access criteria framework for participation in payment systems?

Draft expected answer: The access directions apply to scheduled/licensed banks operating in India and authorised PSPs seeking participation. Actual admission depends on the relevant system criteria. Participation and authorisation to operate a payment system are distinct questions.

Watch for: Conflating participation with operation authorisation.

- [rbi:access-criteria:2021-07-28](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10833), page 1 (logical_markdown): “all scheduled/ licensed banks operating in India and authorised payment system providers”

## PAY-009 — RBI + NPCI

For FASTag and NCMC automatic replenishment, do RBI e-mandate rules and NPCI OC 207 require a 24-hour pre-debit notification?

Draft expected answer: RBI exempts registered FASTag and NCMC auto-replenishment e-mandates from pre-transaction notification. NPCI OC 207 implements the exception for NETC FASTag (MCC 4784) and RuPay NCMC (MCC 7412) in UPI Autopay, where replenishment follows the customer-set balance threshold. Other e-mandate requirements continue; this is not an exemption for all recurring payments.

Watch for: Generalising the exemption; Missing MCC scope.

- [rbi:e-mandates:2026-04-21](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13374), page 1 (logical_markdown): “Pre-transaction notification is not required”

- [2024-OC-207](https://www.npci.org.in/uploads/NPCI_UPI_OC_207_Auto_replenishment_of_NETC_FAS_Tag_and_Ru_Pay_NCMC_with_UPI_Auto_Pay_375b0d066f.pdf), page 1 (source_page): “Exemption from 24-Hours prior Pre-Debit Notification”

- [2024-OC-207](https://www.npci.org.in/uploads/NPCI_UPI_OC_207_Auto_replenishment_of_NETC_FAS_Tag_and_Ru_Pay_NCMC_with_UPI_Auto_Pay_375b0d066f.pdf), page 1 (source_page): “MCC 4784”

## PAY-010 — RBI + NPCI

Do RBI authentication principles and NPCI OC 226 mean every UPI user must switch to biometric authentication?

Draft expected answer: No. RBI specifies compliant authentication principles, including distinct factors and exceptions. NPCI OC 226 introduces optional additional methods and says users may continue existing methods. Distinguish UIDAI face authentication for PIN set/reset from on-device biometrics for transaction authentication. OC 226 describes an initial Rs.5,000 limit, not a verified current limit.

Watch for: Confusing PIN reset with payment authentication; Treating initial limit as latest.

- [rbi:authentication:2025-09-25](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12898), page 1 (logical_markdown): “offer a choice of authentication factors”

- [2025-OC-226](https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf), page 1 (source_page): “These additional methods are optional for the user”

## PAY-011 — RBI + NPCI

Can we use the RBI full-KYC PPI balance ceiling as the UPI LITE limit in NPCI OC 169A?

Draft expected answer: No. RBI full-KYC PPIs have a Rs.2,00,000 outstanding-balance ceiling. OC 169A states Rs.1,000 per transaction and Rs.5,000 total for UPI LITE, with online replenishment using AFA. These limits concern different products and cannot be merged into a universal wallet limit.

Watch for: Merging distinct product limits.

- [rbi:ppi:2026-09-30](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12156), page 1 (logical_markdown): “The amount outstanding shall not exceed Rs.2,00,000/-”

- [2025-OC-169A](https://www.npci.org.in/uploads/UPI_OC_No_169_A_FY_202425_Addendum_to_Enhancement_in_UPI_LITE_Limits_270c24bcbc.pdf), page 1 (source_page): “₹1,000 per transaction with ₹5,000 being the total limit”

## PAY-012 — RBI + NPCI

Compare PPI UPI onboarding in NPCI OC 134 with third-party UPI app access in the RBI PPI directions updated September 2026.

Draft expected answer: NPCI OC 134, referring to the November 2021 RBI snapshot, states PPI holders are onboarded by their own issuer and authenticate with existing wallet credentials. The September 2026 RBI snapshot also allows full-KYC PPI discovery through third-party UPI applications, using UPI credentials for those transactions. Preserve version and channel differences; this evidence alone does not prove formal supersession of every provision in OC 134.

Watch for: Ignoring snapshot dates; Inferring legal supersession.

- [npci-source-01e7e3bc387186fe8cdbcc9a](https://www.npci.org.in/uploads/UPI_OC_134_Adherence_to_RBI_PPI_Interoperability_Guidelines_455e2af154.pdf), page 1 (source_page): “PPI holders shall be on-boarded for UPI by their own PPI issuer only.”

- [rbi:ppi:2026-09-30](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12156), page 1 (logical_markdown): “A PPI issuer may also facilitate discovery of its full-KYC PPIs on third-party UPI mobile applications”

## PAY-013 — RBI + NPCI

Do the e-mandate AFA rules mean UPI Autopay apps may automatically port a customer mandate under OC 223?

Draft expected answer: No. RBI requires issuer AFA validation for modification or withdrawal of an existing e-mandate. NPCI OC 223 separately makes mandate porting strictly user-driven, bars inducements and limits porting to once in a rolling 90-day period. Authentication is not permission for app-initiated porting.

Watch for: Conflating authentication with user authorisation.

- [rbi:e-mandates:2026-04-21](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13374), page 1 (logical_markdown): “Any modification in, or withdrawal of, an existing e-mandate shall require AFA”

- [2025-OC-223](https://www.npci.org.in/uploads/UPI_OC_No_223_FY_2025_26_Enhancement_of_UPI_Autopay_88b38535cb.pdf), page 1 (source_page): “strictly user-driven”

- [2025-OC-223](https://www.npci.org.in/uploads/UPI_OC_No_223_FY_2025_26_Enhancement_of_UPI_Autopay_88b38535cb.pdf), page 1 (source_page): “once in a rolling 90-day period”

## PAY-014 — RBI cross-document

For a non-bank payment aggregator applicant, how do the generic authorisation and PA-specific capital rules fit together?

Draft expected answer: The generic 2026 authorisation directions defer capital requirements to the specific payment-system guidelines. The PA 2025 directions specify Rs.15 crore at application and Rs.25 crore by the end of the third financial year of authorisation, maintained as applicable. Describe the generic framework and PA-specific rule separately.

Watch for: Resolving precedence solely by issuer or date.

- [rbi:authorisation:2026-06-15](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13502), page 1 (logical_markdown): “capital requirement shall be in accordance with the Guidelines/ Directions”

- [rbi:payment-aggregators:2025-09-15](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12896), page 1 (logical_markdown): “minimum net-worth of ₹15 crore”

- [rbi:payment-aggregators:2025-09-15](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12896), page 1 (logical_markdown): “minimum net-worth of ₹25 crore”

## PAY-015 — Scope and qualification

Is the FASTag/NCMC pre-debit notification exemption an exemption from post-transaction notifications too?

Draft expected answer: The RBI e-mandate directions exempt specified auto-replenishment mandates from pre-transaction notification, while separately requiring the issuer to send a post-transaction notification. Do not extend the pre-transaction exemption to post-transaction notices.

Watch for: Transferring an exception to a different duty.

- [rbi:e-mandates:2026-04-21](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13374), page 1 (logical_markdown): “Pre-transaction notification is not required”

- [rbi:e-mandates:2026-04-21](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13374), page 1 (logical_markdown): “An issuer shall send a post-transaction notification”

## PAY-016 — Scope and qualification

Is the April 2028 cyber-resilience date the deadline for all non-bank PSOs?

Draft expected answer: No. April 1, 2028 is the small non-bank PSO deadline. The phased schedule lists April 1, 2025 for large and April 1, 2026 for medium non-bank PSOs. Retain size classification and applicability to authorised non-bank PSOs.

Watch for: Missing phased applicability.

- [rbi:nonbank-pso-cyber:2024-07-30](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12715), page 1 (logical_markdown): “April 1, 2025”

- [rbi:nonbank-pso-cyber:2024-07-30](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12715), page 1 (logical_markdown): “April 1, 2026”

- [rbi:nonbank-pso-cyber:2024-07-30](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12715), page 1 (logical_markdown): “April 1, 2028”

## PAY-017 — Scope and qualification

What was the initial transaction limit for on-device biometric authentication in NPCI OC 226, and was it final?

Draft expected answer: OC 226 initially makes on-device biometric authentication available for transactions up to Rs.5,000 and explicitly says the limit will be reviewed based on performance and evaluation. This answers the historical initial-limit question, not the current limit after subsequent documents.

Watch for: Presenting a historical initial limit as current.

- [2025-OC-226](https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf), page 1 (source_page): “initially be available for transactions up to Rs. 5,000”

- [2025-OC-226](https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf), page 1 (source_page): “The limit shall be reviewed in due course”

## PAY-018 — Unavailable evidence

What is our company Acme Payments internal production fraud-score threshold for rejecting a UPI transfer?

Draft expected answer: The supplied public circular corpus does not establish Acme Payments internal production fraud-score threshold. Abstain from inventing a value and request the approved internal policy.

Watch for: Inventing an internal risk parameter.

## PAY-019 — Unavailable evidence

What is the confidential incident response phone number for Acme Payments on-call engineer?

Draft expected answer: This confidential company contact is not established in the available public payment guidelines. State the evidence limitation and do not invent a phone number.

Watch for: Inventing private operational information.

## PAY-020 — Unavailable evidence

What exact percentage improvement in fraud losses did Acme Payments achieve after deploying its private model in September 2026?

Draft expected answer: The corpus does not contain the company performance measurement needed to answer. Abstain from a numerical performance claim and request the relevant internal evaluation.

Watch for: Inventing an outcome metric.
