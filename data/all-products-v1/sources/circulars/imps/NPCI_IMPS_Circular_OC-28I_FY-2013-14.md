# IMPS I OC 28 I FY 13-14 I Processing of Timed Out Txn

Circular/reference number: OC-28I
Date: 22nd July, 2013

<!-- Page 1 -->

NPCI    p
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/IMPS/OC No 28/2013-14
Oct 31, 2013
To,
All Member Banks, Immediate Payment Service (IMPS)
Dear Sir/Madam,
Sub: Processing of BENEFICIARY TIMED OUT TRANSACTION as deemed successful (IMPS RC-O8 / ISO RC-91)
Obiective:
The objective of issuing this document is to explain the process for elimination of raising debit adjustments
by beneficiary banks for timed-out P2P and P2A & P2U transactions.
The instructions contained herein will come in to effect from 2oth November 2013. From this date treating
Beneficiary Timed-out Transactions as "deemed successful" will be implemented. When such transactions
are treated as successful and settled between remitter and beneficiary banks, the remitting bank need not
beneficiary's account.
This matter was discussed in the IMPS Steering Committee meeting held on 22nd July, 2013. As per the
directions given in the IMPS Steering Committee, a sub group was constituted of SC member banks and NPCl
officials. The sub group met on 26th July 2013 and the proposal contained herein was approved and agreed
for circulation to banks by the sub group members. This was approved for implementation by IMPS steering
committee in its meeting held on 18th October 2013.
Existing practice:
Presently, when P2P/P2A transactions are timed out at the Beneficiary banks' end (Response code O8/ISO
Response Code 91); such transactions are treated as declined transaction by NPCl system and are not settled
in the IMPS settlement process. After reconciliation between CBS data and IMPs settlement reports,
settlement process. In such case, beneficiary bank raises debit adjustment through NPCI's IMPs system on
the remitting bank. if beneficiary bank has not credited to the beneficiary's a/c online and the transaction is
timed out at beneficiary bank's end, the remitting bank has to wait for 5 days to refund to their customer's
a/c. Thus, on 6th day, the remitting bank will reverse the entry from their pooling a/c to the credit of
customer a/c after ensuring that they have not received any debit adjustment from the beneficiary bank.
This process has become a cause of concern to remitting banks to handle customer complaints that their
customer's a/c is debited but beneficiary a/c is not credited.
The proposed process: It is proposed to treat the beneficiary timed out transactions i.e. (IMPs RC-o8 / ISO
RC-91) as successful transactions. Consequently, such transactions will be settled in the IMPs Settlement
process. (In other words, the beneficiary bank will be credited and remitting bank debited for transactions
that are timed out at beneficiary banks' end as part of IMPS settlement process.)
-9,8
C-9, 8th Floor T / Phone: 022 2657 3150
RBIPremises q / Fax: 022 2657 1001
bb -
Bandra-Kurla Complex 专- / email: contact@npci.org.in
Bandra East
- 400 051 aa专c / Website: www.npci.org.in
Mumbai400051

<!-- Page 2 -->

NPCi  p h p
NATIONALPAYMENTSCORPORATIONOFINDIA
Verification Request (vR): Verification request process through online switch shall remain same as existing
process. There will not be any change. If the original transaction and VR is success the transaction is settled
as approved with RC-O0. If the Original transaction is declined and VR is successful the transaction will be
treated as declined with RC-MO.
Reconciliation Actions: There will not be any change to existing methodology of making available various
reports to banks. The response codes too will remain same. An additional report containing beneficiary
timed out transactions that are settled will be made available to beneficiary banks. Beneficiary banks will
have to reconcile the CBS data with settled transactions report of IMPS provided by NPCl (all approved and
beneficiary timed out transactions) and initiate manual credits to customer's a/c where online credit was
not processed. In order to facilitate beneficiary banks to take immediate action of crediting beneficiary's a/c
for Timed out transactions, NPCl will make available a separate report that contain only Beneficiary Timed
OUT IMMEDIATELY AND THE BENEFICIARY'S A/C IS CREDITED WITHIN 2 HOURS IF CREDIT HAS NOT BEEN
GIVEN ONLINE.Please refer to Annexure -A forfurtherdetails.
Adiustment process through DMS: When this process of settling beneficiary bank timed out transactions
gets implemented, it will not be necessary to raise debit adjustments by beneficiary banks. In case
beneficiary bank cannot credit the customer's a/c for any reason post reconciliation (e.g. invalid a/c no., a/c
closed, etc.), the beneficiary bank should return the funds to the remitting bank by raising Return
Adiustment immediately in any case within T+1 day.
The remitting bank will be permitted to raise Chargeback for timed out transactions to get the funds back
from beneficiary bank if - (a) Beneficiary a/c is not credited and (b) Return adjustment is not raised.
In this connection, please refer to Annexure - B wherein timelines and adjustment process for chargeback
and return adjustments are given.
TcC-T'ransaction credit confirmation: An option called Tcc-Transaction credit confirmation will be provided.
Beneficiary bank can confirm that customer's a/c is credited for timed out transactions through TcC option.
For marking successful, the beneficiary bank can use front end option or through bulk upload option. When
remitter bank try to raise chargeback, a pop up message will be displayed to make them aware that the
customer a/c has been credited and therefore there is no necessity to raise chargeback. Initially, DMs will
allow raising chargeback even if TCC is already raised. Please refer Annexure-C for details. This will be
reviewed in three months post implementation of settlement of beneficiary timed out transactions.
Return process: Beneficiary bank can return the funds to the remitting bank where beneficiary bank is not
able to credit their customer's a/c due to wrong a/c no., a/c closed, etc. Beneficiary bank can login in to the
DMS and return the funds by using front end or bulk upload option (Please refer to Annexure D for bulk
upload csv file format). The returns must be processed maximum within T+1 day.
Applicability: The above implementation will be applicable only for P2P, P2A & P2U transactions.
Not applicable to Merchant Transactions (P2M & M2P): This process is not applicable to merchant
transactions because the status of transaction at merchant end is known only to the merchant in most of the
cases.

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Separate file for Rc-08 Transactions: In addition to the existing settlement files,NPCl shall provide separate
report which will contain data pertaining to only RC-08 transactions.This will facilitate banks to match the
RC-08 transactions with CBS.If the beneficiary customer's a/c is found to be already credited online,there
will be no further action needed. HoweverTC should be uploaded in DMS using suitable reason codes-
please refer to Annexure E for reason codes, if it is found that beneficiary's a/c is not credited online,then
the same should be credited manually within two hours and thereafter TCC can be uploaded in DMS using
suitable reason codes.If the beneficiary bank cannot credit the customer's account for any reason
whatsoever (such as, credit freeze in the a/c, closed a/c, etc.) same should be refunded back to remitting
bankbyraising ReturnAdjustmentwithinT+1day.Please refertoAnnexure-Dforformat.
Settlement File formats:Please note that there will not be any change in response code,settlement files and
namingconventionsofsettlementfiles.
Fraud Reporting:In case of anyfraud transactions, same can be reported to fraudrisk@npci.org.in as per the
existingprocess.
Bulk Upload fileformat:Bulk upload can be done using csv file. Please refer to the Annexure-D for csv file
due to Return and Transaction Credit Confirmation.
Reason Codes for raising adjustments: Please use the reason codes while raising dispute either through
frontendoptionorbulkuploadoption.PleasereferAnnexure-Efordetails.
Upload evidence for re-presentment or reiecting pre-arbitration: Beneficiary bank has to upload
confirmationthatthe customeraccounthasbeen credited.PleasereferAnnexure-Fforformat.
Effective Date:This revised process will be implemented w.e.f.2othNovember2013.All are requested to
take a note of the above and ensure that instructions contained herein are delineated to all concerned.
Should you need any further assistance, please contact Mr Saktiswar Rao at saktiswar.rao@npci.org.in
Mobile:08108122856/MrSourabhShuklaatsourabh.shukla@npci.org.inMobile:08108122897.
Yours faithfully,
SD/-
Ram Sundaresan
Head-Operations
Enc.

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Reconciliation Actions
Annexure - A
NPCI
Status at proposed
S. No Scenario beneficiary bank actions Remitting Bank Actions
Beneficiary Bank Actions
Customer account NPCI settle
Beneficiary is credited but the trans-
bank response got timed action as Remitting bank can see Beneficiary bank can upload TCC
response out (Beneficiary deemed the status of timed-out with reason code 102 that the
timed out bank to NPCI) successful transaction in TCC report. credited online. customer account has been
Beneficiary bank to reconcile and
identify the transactions with RC-08
Remitting bank to check if where transaction is approved at
return adjustment is NPCl and not credited to customer
raised. If not, bank can online. Beneficiary bank to initiate
raise chargeback. While manual credit to their customer's
raising chargeback, bank a/c.
has to ensure that TCCis Upload TCC confirmation using 103
Customer account NPCI settle not flagged. If beneficiary as reason code through DMS. This
Beneficiary is NOT credited and the trans- bank has confirmed credit
bank response got timed action as to beneficiary's a/c will help remitting bank to
response out (Beneficiary deemed through TCC, chargeback understand that manual credit has
timed out bank to NPCI) successful should not be raised. been given. Therefore Remitting
bank need not raise chargeback.
Remitting bank to check if
beneficiary bank has
initiated returns through
return option. If not, the
bank can raise chargeback.
While raising chargeback,
bank has to ensure there
is no pop-up message of
TCC/RET.
(TCC means beneficiary If customer account cannot be
Customer account bank has credited their
credited due to various reasons,
is NOT credited and customer a/c and RET
beneficiary bank has to raise pro-
response got timed means funds are returned active returns using return
out. (Beneficiary to remitting bank). If the
bank to NPCI). adjustment option within T+1 day,
funds are returned by to reverse the funds to the
Post reconciliation beneficiary bank, system
it is found that remitting bank. The return of funds
will not allow remitter to remitting bank should be made
customeraccount NPCI settle bank to initiate
Beneficiary cannot be credited the trans- chargeback. using"Returns"optioninDMSwith
bank because of closed action as If TCC/RET is not flagged, suitable reason codes. On raising
response account, no such deemed then chargeback can be returns, beneficiary bank will be
timed out a/c, etc. successful raised. credited. debited and remitting bank will be
If beneficiary bank has credited
their customer account post
Customer account Remitting bank raised
Beneficiary is NOT credited and NPCI settle chargeback as there is no reconciliation and fail to upload
bank response got timed the trans- return adjustment and no TCC, beneficiary bank can re-
response out (beneficiary to action as TCC flag while raising present it by uploading duly signed
timed out NPCI), successful chargeback. Annexure - F. acknowledgement form as per

<!-- Page 5 -->

NPCI   h p
NATIONALPAYMENTSCORPORATIONOFINDIA
Adjustment table for P2P/P2A & P2U
Annexure-B
S. Adjustments Fund Transfer
No Type TAT Initiated by Remarks
From (Dr) To (Cr)
Beneficiary bank has not
60 days from the next
Chargeback day of transaction Remitter Beneficiary Remitter credited their customer's
date. bank bank bank a/c and has not returned
the funds to Remitting
bank.
T + 3 days (T is
Chargeback chargeback day).
Acceptance (Beneficiary bank has
to upload document as Beneficiary Remitter Beneficiary No document required for
/Re- per Annexure F at the bank bank bank chargeback acceptance.
presentment
time of re-
presentment).
30 days from the next
Pre-arbitration day of the Re- Remitter Beneficiary Remitter
presentment date. bank bank bank
No fund transfer shall
Pre-arbitration Beneficiary happen as adjustment
Acceptance 5 days amount is already settled
bank
to remitting banks when
pre-arbitration is raised.
Pre-arbitration 5 days Beneficiary Remitter Beneficiary If rejected within TAT the
Rejection bank bank bank transaction will be settled.
30 days from the next
Arbitration day of the Pre- Remitter
bank Based on panel decision
arbitration Rejection.
This option is provided only
to make remitter bank
Maximum within T+1
understand that customer
day from the date of
TCC Transaction, however Beneficiary No Fund No Fund a/c has been credited either
bank Movement online or by initiating
systemwill allow Movement
manual credit by
beyond T+1.
beneficiary. This will avoid
raising chargeback by
remitter bank.
Beneficiary bank can return
Maximum within T+1
the funds to the remitting
day from the date of
RET Transaction, however Beneficiary Beneficiary Remitter bank where beneficiary
systemwill allow bank bank bank bank is not able to credit
their customer's a/c due to
beyond T+1.
wrong a/c no, a/c closed,
etc.

<!-- Page 6 -->

NPCI  p h pt
NATIONALPAYMENTSCORPORATIONOFINDIA
Upload Proof/Adiustments front-end and bulk upload option: Annexure-C
Type of Adjustments Transaction Type RC Upload Front end Bulk upload
Evidence option option
Transaction Credit Confirmation P2P/P2A/P2U 08 Yes Yes
Return Adjustment P2P/P2A/P2U 08 Yes Yes
Chargeback P2P/P2A/P2U 08 Yes Yes
Chargeback Acceptance P2P/P2A/P2U 08 Yes Yes
Re-presentment P2P/P2A/P2U 08 Yes Yes Yes
Pre Arbitration P2P/P2A/P2U 08 Yes No
Pre Arbitration Accept P2P/P2A/P2U 08 Yes No
Pre Arbitration Reject P2P/P2A/P2U 08 Yes Yes No
Arbitration Logging P2P/P2A/P2U 08 Yes Yes No

<!-- Page 7 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Bulk Upload File Format:
Annexure - D
Header Description
Length Example
Bankadjref Bank Adjustment Reference Number Length-100
(AN) REM/BEN/CB/081013
Flag B/R/TCC/A/RET
Length-03 (A)
shtdat Transaction Date YYYY-MM-DD
(AN) 2013-10-08
adjamt Dispute amount
(N) 1000
Shser RRN Length-50
(AN) 123456789102
E.g.
1. P2P - NBIN + Mobile Number (19 Digits) 5234001008108122883)
Shcrd 2. P2A - NBIN + Account Number (19 Digits) Length-53 5234(NBIN)/ 00 (Reserved)/
3. P2U - NBIN + Aadhar Number (19 Digits) (AN) 1 (Product Number) 00
(Reserved)/ Mobile
Number
filename .csV file name Length-50
(AN) Remcbfile.csv
reason Reason Codes Length-05
(AN) 108
specifyother Bank remarks Length-400 Beneficiary account not
(AN) credited
Note: A-Alpha and N-Numeric.
Flag Description:
Flag
Description
Chargeback
Chargeback Acceptance
Re-presentment
TCC Transaction credit confirmation
RET Returns confirmation by beneficiarybank
Illustration of csV file
BulkflefomatSampleNotepad
FleEdtFomat Yew Hep
RB00343000028ahghhan
R923049434000022884C32.11tranyhnganotheohwiblan
R904930000288rnhganothhlan
RB000343000288agohhan
RNB95C030003493000288CB7ranhgianotherhlank
REB9300034900002288CB64rnthinganthertherwiela

<!-- Page 8 -->

NPCI  p  hp
NATIONALPAYMENTSCORPORATIONOFINDIA
Reason codes for raising disputes & Dispute flag for bulk upload option
Annexure - E
Dispute Category Dispute Reason
Flag Code Reason CodeDescription
Chargeback 108 Remitter account debited but beneficiary account not
credited
Chargeback Acceptance 111
Beneficiary bank unable to credit their customer account
Re-presentment 208
Beneficiary account credited online
Re-presentment 209
Beneficiary account credited manually post reconciliation
Pre-Arbitration 109 Remitter bank customer still disputes that beneficiary
account is not credited
Pre-Arbitration Accept 111
Beneficiary bank not able to credit the customer account
Pre-Arbitration Reject PR 112 Beneficiary account credited online
Pre-Arbitration Reject PR 113
Beneficiary account credited manually post reconciliation
Arbitration AR 101
Both the parties denies to agree
Transaction Credit
Confirmation TCC 102 Beneficiary account has been credited online
Transaction Credit
Confirmation TCC 103 Beneficiary account has been credited manually
Returns RET 114 Account closed
Returns RET 115 Account does not exist
Returns RET 116 Party instructions
Returns RET 117 NRI account
Returns RET 118 Credit freezed
Returns RET 119 Invalid beneficiary details
Returns RET 120 Any other reason

<!-- Page 9 -->

NPCI  p h p
NATIONALPAYMENTSCORPORATIONOFINDIA
Confirmation of credit to beneficiary a/c Annexure F
(On bank's letterhead)
Format for Re-presentment/Rejecting Pre-arbitration -
Madam/Dear Sir,
We refer to the below mentioned chargeback/Pre-arbitration raised against our Bank through Dispute
Management System (DMS) for IMPS RC-08 (P2P / P2A / P2U)
Description Particulars
Remitterdetails (Mobile Number)
Beneficiary Details (Mobile Number/Account Number
with IFSC/ Aadhar Number)
RRN
Transaction Type
Transaction Amount
Transaction Date
Transaction Time
Dispute Date
We hereby confirm that afore mentioned transaction amount was successfully credited to the Beneficiary's
account as per the details mentioned below.
Account No:
Beneficiary Details: (Mobile Number/Account Number with IFsc/ Aadhar Number)
Date & Time of Credit:
Mode of credit: (Online/Manual Credit)
Voucher/Reference No:
We confirm that this declaration will be considered as a conclusive proof of our Bank having credited the
Beneficiary's account and will be used as an documentary evidence in the Dispute Management process. We
also confirm that the remitting bank can confirm to the remitter that beneficiary's a/c has been credited as
above and can share this confirmation form with their customer and/or any other authority as the remitting
bank may consider necessary.
(Authorized Signatory)
Bank Seal
Name of the Official:
Designation:
Bank name:
Date:

<!-- Page 10 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Separate report option in DMS which contains only Rc-08 transactions Annexure -G
llustrationofTransaction(SAMPLE)
TXN UID 1234567
TXN Type (FC,F3) FC/F3
TXN Date
7/10/2013
TXN Time
15:24:55
Settlement Date 7/10/2013
Response Code 08
RRN
328020000000
STAN
4435167493
Remitter
AXB
Beneficiary VJB
BeneficiaryMobile/Account/AadharNumber 1234568108122856
RemitterMobileNumber 1234568108122897
TXN Amount
5000
Sample View of the table (Report shall be made available in XLS & .CSV format)
Beny
TXN UIDTXNType(FC,F3)TXN Date TXN Time Settlement Date Response Code RRN STAN RemmitterBeneficaryMobile/Acount/Aad Remitter Mobile TXNAmount
Number
har Number
1234567 FC/F3 /10/2013 15:24:55 7/10/2013 08 328000004435167493 AXB VJB 1234568108122856 1234568108122897 500
10
