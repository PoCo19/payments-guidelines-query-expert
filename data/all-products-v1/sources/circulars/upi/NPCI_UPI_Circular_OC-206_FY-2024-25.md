# UPI | OC No. 206 | FY 24-25 – Implementation of Generic Good Faith Debit & Credit Adjustments in URCS.

Circular/reference number: NPCI/UPI/OCNo.206/2024-2025

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OCNo.206/2024-2025 Sep 03, 2024
To,
All Members of Unified Payments Interface (UPl)
Subject: lmplementation of Generic Good Faith Debit & Credit Adjustments in URCS
For managing exceptional transactions (viz. wrong credit recoveries done after the TAT js expired where
dispute has been already represented because of non-availability of funds, similarly fraud chargebacks
recovery, IPO executions etc.). Currently, member banks are sending all such exceptional requests to
NPCI with debit consent for passing adjustment entries and NPCl pass adjustment entries through back-
office system. we have made provision for processing of such exceptional adjustments through which
member banks can directly manage the adjustments through UPI back-office system (URCs - UPl Real
Time Clearing System) without NPCl intervention.
Generic Good Faith Debit & Credit adjustments option in URcs. Member banks should set up internal
processes for managing the generic good faith adjustments in URcs and make necessary development in
funds done after the TAT expiry (as mentioned above). This option should not be used to avoid any
compensations and penalties, any deviation shall be treated as non-compliance to the NPCl guidelines.
Key Points:
URCs will not validate credit adjustment entries raised by the member banks in the system
unlike current disputes process where URcs verify all the logical conditions and process the
dispute successfully or reject (as the case may be). Hence, member banks should ensure to
do due diligence and propervalidation of all adjustments before raising in URCs. Only bulk file
format and other mandatory data fields length & format will be validated (refer section BULK
FILE FORMATin the Annexure- 1)
URCS will validate Debit Adjustment entries (BGGD). URCS will check if the original TXN
already present with RC oo, RB and DD if present then debit adjustment will not be allowed,
otherwise URCS shall process adjustments (refer section BENEFICIARY BANK RAISING
GENERIC GOOD FAITH DEBITADJUSTMENT (BGGD) in Annexure -1)
Good faith adjustment once settled will not be allowed again if all the fields are same with
duplicate adjustment error code and description.
URCs has harmonisation of TAT & customer compensation for BGGC. Member banks should
choose penalty flag wherever it is applicable Y or N (Yes or No). If bank is raising with flag Y,
then penalty will be processed as per existing process and for N no penalty shall be applied.
No penalty is applicable for BGGD & RGGC.
V) Banks shoutd use proper and correct three digits code while raising adjustments through front
bank - ABC and Beneficiary bank XYZ then same bank codes has to be used for raising
debit/credit adjustments), three-digit code should not be altered.
vi) Account number is mandatory for banks to enter when manual adjustment is raised through
front end or bulk upload, Use account number of other bank customers/merchants where
credit or debit has to be done by the respective bank who receives generic good faith
adjustments (Debit/Credit). Once the adjustments are successfully settled URCS will update
the account number in adjustment report (refer SHDT74 column).
vii) Generic good faith debit/credit adjustment amount & customer compensation amount (if any
- as per the beneficiary bank declaration while raising the BGGC in URCS) will be settled in
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 400 O51.
T: +9122 40009100 F: +9122 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
existing NTs! line item ‘Net Adjusted Amount' & 'Customer Compensation for Non-
Compliance Debit/Credit.
vili) The above functionality shall be made available to the banks with effect from September 15,
2024.
Refer Annexure -1, Detailed process for handling generic good faith debit & credit adjustments.
Warns Regards,
GirtdharGM
Chief-Customer Success
Enclosed:Annexure-2UserManual for genericgoodfaithadjustments.
1001A, The Capital, B Wing. 1Qtn Floor,
BandraKurlaComplex, Bandra (E),Mumbai 4o0 O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCL
NATIONAL PAYMENTS CORPORATION OFINDIA
Annexure-1
BGGD-BENEFICIARY BANK RAISING GENERIC GOOD FAITHDEBITADJUSTMENT: Beneficiary/SponSor
Bank can raise generic good-faith debit adjustments for iPO executions ONLY on remitter/issuing bank.
Adjustment, the issuing bank should accept or reject within 3 calendar days otherwise the adjustment
window will be closed on deemed acceptance on 4th day. Funds will be settled by debiting the issuing bank
onty for U2, IPO transactions with initiation mode 11,13 and purpose code 01. If original TXN atready
present with RC oo, RB and DD then URCS will decline the BGGD adjustment.
BGGC-BENEFICIARY BANK RAISING GENERIC GOOD FAITHCREDIT_ADJUSTMENT: Beneficiary Bank
remitting banks (e.g. beneficiary bank recovers the chargeback amount of wrong credit
funds/chargebacks amount of fraud transaction funds etc. after the 35 days TAT). Once the adjustment is
raised funds will be settled immediately by debiting the beneficiary bank who has raised the adjustment
and credit the same to remitting bank who has received credit adjustment. Remitting bank who has
received the credit adjustments has to accept or represent BGGC within 3 calendar days otherwise the
adjustment window will be ciosed on deemed acceptance.
RGGC REMITTING BANK RAISING GENERIC GOOD FAITH CREDIT ADJUSTMENT: Remitting Bank can
raise generic good-faith credit adjustments (for P2P or P2PM or P2M) for giving funds to other beneficiary
banks (e.g. Beneficiary bank missed to re-present the chargeback within TAT and raise good faith request
to remitting bank, remitting bank can raise RGGC for giving the funds to the beneficiary bank (if the funds
are not credited or recovered by remitting bank). Once the RGGC adjustment is raised, funds will be settled
immediately by debiting the remitting bank who has raised the RGGC adjustment and credit the same to
beneficiary bank who has received credit adjustment. Beneficiary bank who has received the credit
adjustments has to accept or represent within 3 catendar days otherwise the adjustment window will be
closed on deemed acceptance.
are as follows,
i) Raise: BGGD & BGGC can be raised by beneficiary banks and RGGC has to be raised by the
Remitting bank.
ii) Acceptance: Bank who has received the generic good faith adjustments has to accept in
URCS.
ii) Re-presentment: Bank who has received the generic good faith adjustments may reject the
adjustments (if customer account cannot be credited, etc.).
iv) Deemed Acceptance: Bank who has received the generic good faith adjustments has not
taken any action (accept/re-presentment) on adjustments within TAT of 3 calendar days, then
adjustment wilt be closed on deemed acceptance.
Non. - Compliance: Banks should not raise any adjustments for which the life cycle of the dispute is
already within TAT which has to be accepted or represented (as the case may be) in URCS. NPCI will take
up the matter as non-compliance to the NPCl guidelines, in case, if any bank raises generic good faith
adjustments instead of accepting or representing in URCS which are within TAT.
100iA, The Capital, B Wing,10tn Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 O5].
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NPCU
NATIONAL PAYMENTS CORPORATIONOFINDIA
IAT FOR GENERIC GOOD FAITH ADJUSTMENTS: All good faith adjustments should be either
accepted/represented within 3 calendar days from the next day of generic good faith adjustment is raised.
Otherwise, the window will be closed on deemed acceptance.
VALIDATION OF ADJUSTMENTS: URCS will not validate BGGC & RGGC adjustments with original
transaction or disputes. BGGD will be validated with original transactions as mentioned above. For BGGC
However, once the manual adjustment is processed, successfully it will be stored in repository and
transaction details are same).
RBI PENALTY CALCULATION: RBI Compensation will be processed for BGGC only as per the RBI circular
DPss.CO. PD. No.629/02.01.014/2019-20 dated 20th September 2019 towards harmonisation of Turn
and NPCI OC vide reference number NPCI/IMPS-UPl/ OC-93/2019-20. Refer below the details for
reference,
i) BGGD - No penalty is applicable, because it's an offline IPO execution where the fulfilment of
IPO services is already given by registrar to customer. Note: The "Penatty Flag" field will not
be availablte in the front-end interface. However, in the bulk file format, the penalty flag
wilt be visible for all three generic good faith adjustments. If a beneficiary bank
mistakenty setects "y", still the penalty will not be processed for BGGD.
RGGc - No penalty is applicable, because these are good faith request raised by the
beneficiary bank on remitting banks for not re-presenting the chargebacks/pre-arbitrations
etc. within TAT. Note: The "Penaity Flag" field will not be availabte in the front -end
interface. However, in the bulk file format, the penalty flag will be visibie for all three
generic good faith adjustments. if a beneficiary bank mistakenly selects "y", still the
penalty will not be processed for RGGC.
ii) BGGC -URCs will allow beneficiary bank to choose the penaity flag Y/N (Yes or No) while
raising BGGC in both front end and bulk. If the beneficiary bank chooses the penalty flag Y,
then penalty will be processed and if the penalty flag is chosen N, then penalty will not be
settled similar to the existing ACAT flags
iv)
TAT of 3 days URCS will reverse the transaction amount along with RBI penalty (if RBl penalty
is already settled).
INVALID THREE DIGITS CODE/PARTICIPANT D
Member banks should use proper three digits code viz. sponsor bank codes, sub-member bank codes,
RuPay CC on UPl bank codes etc. If invalid codes are used, then adjustment will be settled to the invalid
banks. Hence, banks shoutd use proper and correct three digits code as per the AUTH settiement.
file where primary is already processed successfully/failed), then URCS will reject the entire file.
1001A, The Capital, B Wing, 10 Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4Oo O51.
T: +91 22 40009100 F: +9122 40009101
contact@npci.org.inwww.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 5 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
in the existing adjustment report with separate flag i.e. BGGC, RGGC & BGGD under two headers i.e.
Adjitype & Dispute Flag.
Unsettled Transactions: Member banks should not raise any generic adjustments in URCs for unsettled
transactions. Such cases must be reported to NPCl.
BULK FILEFORMAT
Fields Format & Length Entity
As per current bulk file format specs (If IPO claim is raised then
Bank Adj Ref No sponsor bank has to update the name of IPo for issuing banks Bank
reference in this field)
Remitting Bank Code (three
Digits) 3 digits Alpha Bank
Beneficiary Bank Code (three
Digits) 3 digits Alpha Bank
TRAN ID 35 Alpha Numeric Bank
Transaction Date 20240604 "YYYYMMDD" (e.g. 4th June 2024) Bank
Transaction Sub-Type U2/U3/UC Bank
RRN/LRN/UMN 12 Numeric Bank
Dispute Flag 4 digits Alpha Bank
AdjustmentAmount Numeric-9 digits length including decimals (e.g.495495.75) Bank
Reason Code 4 digits Alpha Numeric Bank
Penalty Flag Y/N 1 digit Alpha Bank
Account number 9 digits minimum and 21 digits maximum to support both alpha & Bank
numeric
DISPUTES (RAISE) REASON CODES, DISPUTE FLAGS & DeScription
Reason
Entity Dispute Flag Reason Code Description
Codes
RGGC RGA1 Good faith request from another bank
RGGC RGA2 TAT expire disputes
Raised by
RGGC RGA3 Technical issues by bank
Remitter
RGGC RGA4 Dispute incorrectly accepted/represented
RGGC RGA5 Any other reason
BGGC BGA1 Amount recovered for wrong credit charge back after expiry of TAT
BGGC BGA2 Amount recovered for fraud charge back after expiry of TAT
BGGC BGA3 Good faith request from another bank
Raised by
Beneficiary BGGC BGA4 TAT expire disputes (e.g. Accept/ Reject of the Dispute fifecycle,
merchants refund (Credit Adjustment / RET)
BGGC BGA5 Technical issues by bank
BGGC BGA6 Disputeincorrectly accepted/represented
1001A, The Capital, B Wing. 10t Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 6 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
BGGD BGA7 IPO Claim by Sponsor/Beneficiary Banks
BGAC BCA1 Good faith Acceptance for Credit RGGC
Acceptance RGAC RCA1 Good faith Acceptance for Credit BGGC
RGAD RDA1 Good faith Acceptance for Debit BGGD
DISPUTES(RESPONSE)REASONCODES,DISPUTEFLAGS&Description
Adjustment Type Dispute Flag Reason Codes Reason Code Description
RGRC RGR1 Account closed
RGRC RGR2 Account does not exist
Represented by RGRC RGR3 Party instructions
Remitter
RGRC RGR4 NRIaccount
(For BGGC
Adjustment) RGRC RGR5 Account freeze
RGRC RGR6 Invalid Remitter details
RGRC RGR7 Any other reason
RGRD RGD1 Execution TAT expired
Represented by
Remitter RGRD RGD2 Duplicate execution
(For BGGD RGRD RGD3 Initiation not done - Invalid execution
Adjustment)
RGRD RGD4 Any other reason
BGRC BGR1 Account closed
BGRC BGR2 Account does not exist
Represented by BGRC BGR3 Party instructions
Beneficiary
BGRC BGR4 NRi account
(For RGGC
BGRC BGR5 Account freeze
Adjustment)
BGRC BGR6 Invalid beneficiary details
BGRC BGR7 Any other reason
Deemed Good faith Deemed Acceptance for
BGCD BCA2
Acceptance RGGC
RGCD RCA2 Good faith Deemed Acceptance for
(Deemed Flag to BGGC
be updated by Good faith Deemed Acceptance for
RGDD RDA2
the URCS) BGGD
1001A, The Capital, B Wing, 10tn Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 400 O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067
