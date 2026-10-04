# UPI | OC No. 208 A | FY 2025-26 | Addendum to OC - 208 Implementation of NRP & PRD process & arbitration guidelines

Circular/reference number: NPCI/UPI/OC208A/2025-26

<!-- Page 1 -->

NPC
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/UPI/OC208A/2025-26 Jun 30, 2025
To,
All Members of Unified Payment Interface (UPl)
Subiect - Addendum to implementation of NRP & PRD Process & arbitration guidelines
Reference may be taken from circular No. NPCi/UPI/OC 208/2024-25 dated 03rd Oct 2024 where we
have implemented NRP & PRD process from 05th Oct 2024 (chargeback raise date) and communicated
that the process wifl be carried out through email till it is automated in the back-office system (URCS).
In view of the above, please be informed that we have automated the NRP process as listed below
(refer Annexure - E user manual for details), changes will be implemented in URCS w.e.f. 01st Aug
2025.
Submit complaint document option is made available while raising arbitration in URCs through
front-end option for remitting/issuing banks.
2) Funds will be settled through URcs if arbitration is accepted/deemed accepted, settlement
details are made available in the adjustment report.
 NPCI will give NRP verdict in URCS. Users can view the status in transaction search page and
adjustment report. NPCl will discontinue the email process for communicating the NRP verdict
status.
RBI customer compensation confirmation (AC/AT) has been implemented in URCS for P2M
transactions where beneficiarylacquiring bank should update the status in URCS with ACIAT
when the verdict is given in favour of the remitting/issuing bank. Member banks can view the
status in transaction search page and adjustment report. NPCI will discontinue taking AC/AT
confirmation from beneficiarylacquiring banks through email. If the beneficiary bank does not
confirm the status of AC or AT, then the same will be considered by URCS on deemed
acceptance basis i.e. AT and process the compensation.
5) Refer Annexure - C for NTSL new line items.
(9 Introduced new dispute flag & reason codes for arbitration (refer Annexure - A for details)
7) Refer other process automations list in the Annexure -- D for details.
In addition to the above, please note the revised process has been briefed as follows (refer Annexure
- B life cycle for details).
S. No Existing Process Revised Process
Arbitration fee is charged in Arbitration fees will be charged after giving NRP/PRD
NRP/PRD raise stage. verdict for the chargebacks raised from 05h Oct 2024.
TAT to raise PRD is 15 calendar TAT to raise PRD is 5 calendar days from next day of NRP
days from next day of NRP Verdict. Verdict.
The information herein may please be disseminated to all the concerned.
With warm regards,
SD/-
Giridhar GM
Chief-Customer Success
Page 1/6

<!-- Page 2 -->

NPCI
NATIONALPAYMENTS CORPORATION OF INDIA
New Dispute Flags & Reason Codes Annexure - A
TXN Sub Ady Adjustment
Dispute Stage Reason Adjustment Reason Code Description
Type Flag Code
U2/U3/UC ACC 1105 Beneficiary account is credited successfully as per the document uploaded
Arbitrafion Continuation U2 ACC 1106 Goods/Services provided to custonrer
U2 ACC 1107 Refund processed to custormer via alternate channels
1126 Dispute on fraud TXN raised under normal chargeback category
1127 Merchant refunded/reversed to customer
NRP Verdict - ACIAT U2/U3/UC NVB 1128 Goods/Services fuffilled to customer
1129 Customer has withdrawm complaint
1130 Beneficiary customer account credited successfuly
1131 Goods/Services fulifilled to customer in good condition and as per the order
1132 Rejection document says merchant accepting dispute
1133 Blurry evidence
1134 CBS details provided in editable file instead of CBS screenshot
1135 CBS screenshot uploaded without last digits of beneficiary account
1136 CBS screenshot uploaded without TXN details
1137 Details in the rejection document are not matching with dispute details
1138 Uploaded evidence is blank
Goods/services fuiflment declaration letter uploaded which is invalid as
1139
merchant does not pertain to Smal/Offine category
1140 Illegible evidence
1141 Invalid document which does not address the customer dispute
1142 Invalid evidence consisting generic statements
1143 Merchant fraudulent
1144 No/Parfial/lncorrect refund details present in the rejecfion document
1145 No evidence has been provided
1146 Only door-delivery details attached as rejection document which is invalid
NRPVerdict-ACIAT U2/U3/UC|NVR because no TXN details present
1147 Only merchant details provided not about the fulfilment of goods/services
provided
1148 Others
1149 Rejection document of partial refund uploaded but the customer is disputing
for the balance amount
1150 Rejection reason mentioned as customer account closed/freezelien marked
which is invalid reason
1151 Rejection reason mentioned as customer not giving debit consent which is
invalid reason
1152 Rejection reason mentioned as customer not in contact which is invalid reason
1153 Rejection reason mentioned as merchant is black-listed/fraudulent which is
invalid reason
1154 The refund has failed as per the refund details in the rejection document
1155 TXN details not matching with invoice details
1156 TXN status in the rejecfion document is showing cancelled/pendinig/failed
1157 Uploaded rejection document does not pertain to the dispute
NRP Verdict in favor of
Rem Bank - Customer
U2 NVCA AT Atributing to the Technical issue at bank/aggregator/merchant
Compensation Accept (or)
Deemed Accept
NRP Verdict in favor of
Rem Bank - Customer U2 NVCR AC Atributing to the Customer
Compensation Reject
Note: Removed the reason code 1102 - 'Customer has still not received the service' under Arbitration
Continuation.
Page 2/6

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
ArbitrationLifeCycle Annexure - B
Fund Movement
Arbitration Raised TXN Adl Adl Dispute RB Customer NRP Fee Rs. PRD.Fee Rs.
Stage By TAT Sub Hag Reason Amount Compensation Amount 500- & GST 3,0001- &
Typg Code GST
Dr Cr
Arbitration
Arbitration 15 days from
Raise! REM! nex day of U21 AR 1100
Deferred Iss Pre- U3/
Arbitration Arbitration uc FAR 127
Raise Decline
15 days from U21
Arbitration REM! next day of U31 ACW 1103
Withdraw Iss Arbitration
Raise
Arbitration 15 days from AT BENIACQ REM/ISS
Accept ! BENI next day of BENREM
ACA AC
Deemed ACQ Arbitration ACQ
U3/
Accept Raise UC 1101 BENTACQ REM/ISS
1105
15 days from
Arbitration BEN/ next day of U2 1106
Continue ACQ Arbitration ACC 1107
Raise U3/ 1105
NPCI Review Panel (NRP)
NRP Verdict 30 days from
in favor of next day of U2 / 1126 to REM
NPCI U3/ NVB NPCI
BENTACQ Arbitration UC 1131 Iss
Bank Continue
NRP Verdict 30 days from
in favor of next day of U2 1132toBEN/REM BEN/
REM/ISS NPCI Arbitration U3/ NVR 1157 ACQ /ISS ACQ NPCI
Bank Continue BENIACQ REM/ISS
NRPVerdict
in favorof
Rem Bank- 3 days from
Cus tomer next day of
BENT NRPVerdict
Compensatio ACQ in favor of U2 NVCA AT BEN1ACQ REMIISS
REM/ISS
AcceptDeem
Bank
ed Accept
(**)
NRP Verdict 3 days from
int favor of nex day of
Rem Bank - BEN/ NRPVerdict
U2 NVCR AC
Customer ACQ in favor of
Compensatio REM/ISS
n Reject (+**) Bank
(***) Applicable only on arbitrations where the chargeback raised with RC 1065-Account debited but
transaction confirmation not received at merchant location.
Page 3/6

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Fund Movement
Arbitration Stage Raised TAT Sub NXI Hag Adl Reason Adl Amount Dispute CompensationAmount RBl Customer 500f-& GST NRP Fee Rs. PRD Fee Rs. 3,000-&
Type Code GST
Dr
Panel for resolution of disputes (PRD) : NRP Verdict given in favour of BENI ACQ Bank
5days from
next day of
REMI NRP Verdict U2 1
PRD Raise ISS given in U3/
favour of UC
BEN/ACQ
Bank
PRD REM! 15daysfrom U2/
Withdraw ISs next day of U3/
PRD Raise UC
BENTACQ REM/ISS
PRDAccept/ BEN! 15daysfrom U2 BENREM (upon 'AT
Deemed ACQ next day of ACQ contimation) confirmation)
Accept PRD Raise U3/
BENIACQ REM/ISS
PRD BEN/ 15days from U2/
Continue ACQ next day of U3/
PRDRaise UC
PRDVerdict 30 days from U2/
BEN /ACQ in favor of PRD next day of PRD U3/ REM! iss NPCI
Bank Continue UC
PRD Verdict 30 days from BEN1ACQ REM/ISS
in favor of REM/ISS PRD next day of PRD U2 BEN/REM ACQ /Iss confirmation) (upon 'AT confirmation) (upon 'AT* ACQ BEN/ REM/ iss BEN / ACQ NPCI
Bank Continue U3/ BEN 1ACQ REM/ISS
Panel for resolution of disputes (PRD) :NRP Verdict given in favour of REM / [Ss Bank
5 days from
next day of
PRD Raise BEN/ NRP Verdict U21
(**) ACQ given in U3/
favour of
REM/ISS
Bank
PRD BEN/ 15days from 02 /
Withdraw ACQ next day of U3/
PRD Raise
REM/ISS(if BENIACQ(if
PRDAccept! REM! 15days from U2 REM BEN/ paid after paidafterNRP
Deemed next day of /ISS ACQ NRP verdict) verdict)
Accept PRDRaise U3/ REM/ISS BEN /ACQ
PRD REM! 15days from U21
Continue Iss next day of U3/
PRD Raise
PRD Verdict 30 days fom REM/ISS (if BEN /ACQ (if
BEN/ACQ in favor of PRD next day of PRD U37 U2 REM BEN ACQ NRP verdict) paid after paid after NRP verdict) REM/BENIREMI ISS ACQ NPCI
Bank Continue REM/ISS BEN 1ACQ
PRD Verdict 30 days fom
REM/ISS in favor of PRD nexf day of PRD U3 / ACQ BEN / NPCI
Bank Continue UC
(***) When the verdict is given in favour of remitting/issuing Bank, URCS will settle the funds. However,
remitting/issuing Bank should keep the funds on hold up to 5 calendar days where beneficiary/acquirer
bank may raise PRD. Remitting/lssuing Bank can reverse the funds to their customer on 6th calendar
day provided there is no PRD raised by the beneficiary/acquirer bank.
Page 4/6

<!-- Page 5 -->

NPCI
NATIONAL PAYMENTS CORPORATIONOFINDIA
New Line Items in NTSL Annexure - C
NRP Fee andNRP Fee Reversal Settlement Entries:As per OC -2o8, we have coillected NRP fee +
GsT when arbitration is raised. This process has been revised and started collecting NRP fee + GST
only after giving the verdict, corresponding NTSL line items are listed below. Amount column will appear
zero because the fee has been made zero at arbitration raise.
National Payments Corporation of India
Unified Payments Interface
Daily Settiement statement forHDFc Bank -uPl as on 30-0o4-2025 23c
11:45:00 TO 12:00:00)
Description No of Txns Debit Credit
41 NRP Raise Fees 37 10
42 NRP Raise Fees GST 37
Reversal of NRp Fee From Beneficiaryto
43 Remitter(ArbitrationAcceptance)-Debit
ReversalofNRPFeeGsTFromBeneficiaryto
44 Remitter(ArbitrationAcceptance)-Debit
Reversai of NRpFee From Beneficiaryto
45 Remifter(ArbitrationAcceptance)-Credit 12
Reversal ofNRP Fee GsT Frorm Beneficiary to
46 Remitter (ArbitrationAcceptance)-Credit 12
Reversalof NRpFee FromBeneficiaryto
Rernitter(NRP Verdict infavour afRemitter)
47 Debit
Reversalof NRPFee GSTFromBeneficiaryto
RemitterNRPVerdictinfavourofRemitter)-
48 Debit
Reversal of NRp Fee From Beneficiary to
Remitter(NRp Verdictinfavour of Remitter)
49 Credit 10
Reversal ofNRPFeeGsTFromBeneficiaryto
Remitter (NRP Verdict in favour of Remitter)-
50 Credit 10
Dispute Amount Settlement Entries: Funds will be settled if beneficiarylacquiring bank accepts / deemed
accepts the arbitration and NPCl gives verdict in favour of remitting/issuing bank, all settlement entries
will be netted and processed in 'Net Adjusted Amount' ine item in NTSL.
National Payments Corporation of India
Unified Payments Interface
Daily Settiement statement for HDFc Bank - UPl as on 30-04-202s (23c
11:45:00 TO 12:00:00)
Description No ot Txns Debit credit
27 Net AdjustedAmount 28350
RBl TAT Harmonization Customer Compensation Settlement Entries: Customer Compensation will be
settfed and the same is included in 'Customer Compensation For Non Compliance' line items in NTSL.
National Payments corporation of lndia
Unified Payments Interface
Daily settlement Statement for HDFc Bank - UPl as 0n 30-04-2025 ( 23C
11:45:00 TO 12:00:00 )
Desciption No of Txns Debit Credit
Customer CompensationForNonCompliance
51 Debit
Customer Compensation For Nan Compliance
52 Credit 12 34000
Page 5/6

<!-- Page 6 -->

NPCI
NATIONAL PAYMENTS CORPORATIONOFNDIA
Additional developments-Work in progress Annexure-D
Following processes are still under development and will be handled as per the current offline process:
i) Process of raise PRD by remitting/issuing bank or beneficiarylacquiring bank will continue
to be carried out through email.
i) NRP & PRD Verdict fee + GST collection will be settled through adjustment entry and will
communicate through email.
In addition to the front-end option, upload bulk evidence option will be provided in URCS.
Banks should continue to update the same through front end tilil the automation is
completed.
Page 6/6
