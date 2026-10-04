# AePS | OC 71| FY 22 23 | Implementation of Fraud Chargeback in AePS ARCS System

Circular/reference number: NPCI/2022-23/AEPS/042
Date: 1st November
2022

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTSCORPORATIONOFINDIA
NPCI/2022-23/AEPS/042 27thOct2022
To,
AllMemberofAadhaarEnabledPaymentsSystem(AePS)
Madam/DearSir,
Sub:Implementation of fraud chargeback in AePS ARcs System w.e.f.1st November
2022
2021 wherein the process forhandle the fraud chargebacks for AePsfraudulent transactions
has been defined.
We wish to submit that we have now automated fraud chargeback process in AePS ARcs
back office.After implementing the said automated fraud chargeback mechanism in ARCS,
NPcl shall discontinue the existing manual process which was carried out through emails.
ReferAnnexure-1 for process flow and details set for handling the fraud chargebacks.
Members are requested to note the following key features of the Guideline:
1. The Guidelines will be applicable for all financial transactions in AePs (Viz., Cash
withdrawal, Cash Deposit, Funds transfer and BHiM Aadhaar) involving Business
Correspondents (BC), BC agents, Customer Service Points (CSP) etc.
2. Every fraud chargeback should be reported in NPCl's EFRM portal and Banks should
include the Case ID generated therein while raising fraud chargeback in ARCS Portal.
3. Member banks are requested to use ARCS portal for raising fraud chargeback effective
from 1st November2022and with effect from this date, the manual process over emails
willbe discontinued.
4. NPCl's role will be limited to handling cases raised to arbitration of any issues (raised by
the aggrieved party) in the last stage of fraud chargeback lifecycle.
5. Memberbank can raise fraud chargeback within 60 calendar days from date of transaction.
6. If the bank does not submit responses within TAT in their respective stages, the case
would be considered as deemed accepted and closed in favor of the other party.
7. Maker/ Checker is mandatory for raising, accepting and rejecting fraud chargeback/ good
faith chargeback
8. ARCS allow to raise fraud chargeback both through front end and bulk upload mode
9. Once the fraud charge back is raised, the Acquirer is debited & Issuer is credited
immediately. However, Issuers are advised to hold the credit and post it to the customer
only after thefinal closure of theFraud Liability shift chargeback process.
Member Banks are requestedto take note ofabove and disseminate the information contained
hereinto allthestakeholder concerned.
Yours sincerely,
S.m. Na
SaiprasadNabar
ChiefTechnologyOfficer
Enclosed:Annexure-1Process flowand procedures for handlingAePSfraud chargebacks
1001A, PageNpitd/13 Wing, 10th Flo0
BandraKurlaComplex,Bandra(E),Mumbai 4o0o5
T:+912240009100F:+91224000910
contact@npci.org.inwww.npci.org.i
CIN:U74990MH2008NPL18906

<!-- Page 2 -->

ANNEXURE-1
Qualifying Criteria for Fraud Reporting:
The criteria for reporting a fraud transaction under this guideline is detailed below:
Issuerbanksshall reportonlyoff-ustransactionsunderthisguideline
2) Declined transactions are not eligible for reporting as fraud transactions.
3) Transactions raisedas disputechargebacks cannot be raised under Fraud Chargeback and
vice versa
PROCESSFLOWANDPROCEDURESFORHANDLINGAEPSFRAUDCHARGEBACKSINARCS
Disputestype,TATs&DisputeFlags:
Dispute
Adjustment Type Raised by TAT Period
Flag
Fraud Chargeback ISSUER 60 days FC
Fraud Chargeback Accept ACQUIRER 15 days FCA
FraudChargeback Re-presentment ACQUIRER 15 days FCR
Fraud ComplaintRe-raiseAccept ACQUIRER 03 days FCPA
FraudComplaint Re-raise Reject ACQUIRER 03 days FCPR
Fraud Compliance ISSUER 05 days FCP
Fraud ComplianceCheck NPCI 05 days FCC
60 days from
Good Faith Fraud Chargeback ISSUER expiry of FC GC
TAT
Good FaithFraud Chargeback Accept ACQUIRER 15 days GFA
GoodFaithFraudChargebackReject ACQUIRER 15 days GFR
Txn Type Dispute Raised
Dispute Type Flag RC Previous Stage TAT By
04,32,01, FC, 60
Fraud Chargeback FC 00 Issuer
25 days
Fraud Chargeback 04,32,01, FC, FCA 00 Fraud Chargeback 15 Acquirer
Accept 25 days
Fraud Chargeback 04,32,01, FC, 15
Re-presentment FCR 00 Fraud Chargeback Acquirer
25 days
(Reject)
04,32,01,FC, FraudChargebackRe-
Fraud Compliance 25 FCP 00 presentment(Reject) 5 days Issuer
Fraud Compliance 04,32,01, FC, FCC 00 Fraud ComplaintRe- 5 days Acquirer
Check 25 raise Reject
Fraud Complaint 04,32,01,FC, FCPR 00 Fraud Compliance 3 days NPCI
Re-raise Reject 25
Page No.2/12

<!-- Page 3 -->

Documentsto be uploadedby Bankswhile takingaction on disputes
Reportingfraudswithin 6o daysfromdateof transaction
Sr.
Stage Document Name Raised by Settlement FieldsDetails
No
Supporting Document PoliceFIR
Fraud copy,Complaintcopy,customer Acquirer → Document
complaintletter,bank statement,
Chargeback passbook copy, etc.: Non Issuer Issuer Non
mandatory mandatory
Non
mandatory
Accept document
Fraud Supporting documents:Non No Action Acquirer
Chargeback Acquirer
mandatory Response -
Accept/Reject
with freetext
BC letter confirming cash
handoverto customer.
2) Customerletter confirming Reason for
Represent receipt of cash/funds raising fraud
Fraud 3) Others:Any1 of the above Acquirer Issuer→ chargeback
Chargeback supporting documents Acquirer reject
(Reject) required to upload into system Document
also, the points mentioned 1,2 Mandatory
& 3 to be reflected on the
screen with tick to upload
multiple documents
Additionalfield
-'Reason for
raising fraud
repeat
Acquirer → complaint'
Any Supporting Document:
Compliance Issuer made
Mandatory Issuer available in
portal while
raising fraud
repeat
complaint
Additional field
-'Reasonfor
accepting Re-
Accept Re- raised fraud
Any Supporting Document:Non-
raisedFraud Acquirer No action complaint'
Mandatory
Complaint made
available in
portal while
accepting
Page No. 3/12

<!-- Page 4 -->

fraudrepeat
complaint
Additional field
-'Reasonfor
rejecting Re-
Reject Re- raised fraud
raised Fraud Issuer → complaint'
Complaint AnySupportingDocument Issuer Acquirer made
available in
portal while
rejecting fraud
repeat
complaint
Good faith-Reporting frauds after 6o days fromdateof transaction
To be uploaded
Stage Document Name Settlement
No by
Good faith Fraud Supporting documents:Non
No action Issuer
Chargeback mandatory
Good Faith Accept Fraud Any Supporting Document: Acquirer→
Acquirer
Chargeback Non mandatory Issuer
Good Faith Represent Fraud Supporting documents:Non No action Acquirer
Chargeback mandatory
NTSL report changes for Fraud chargeback disputeentries present in NTSL report
Samplereports&screenshotforyourreference.
DisputeAdjustments
Description Ref. No Debit Credit
Chargeback Details
ChargebackfromKKM 224410969944 2501
Total Chargeback Amount 2501
Credit Details
CreditAdjustmenttoKKM 224410687716 2501
Total Credit Amount 2501
Page No. 4/12

<!-- Page 5 -->

FraudChargebackDetails
FraudChargebackfromKKM 224410782333 2501
FraudChargebackfromKKM 962642336133 1500.25
Total Fraud Chargeback Amount 4001.25
Fraud Chargeback Re-presentment Details
FraudChargebackRe-presentmenttoKKM 224410782333 2501
TotalFraud ChargebackRe-presentment 2501
Amount
Fraud Complaint Re-raise Accept Details
Fraud Complaint Re-raise Accept to KKM 224410782333 2501
Fraud ComplaintRe-raise Accept toKKM 224811289280 1500.25
Total Fraud Complaint Re-raise Accept 4001.25
Amount
Fraud Compliance Check Details
Fraud ComplianceChecktoKKM 962642336133 1500.25
Total Fraud Compliance Check Amount 1500.25
GoodFaithFraud ChargebackAccept Details
Good FaithFraud Chargeback Accept fromKKM 218711810409 2501
Total Good FaithFraud ChargebackAccept 2501
Amount
AdjustmentSubTotal 14504.75 5002
Net Adjusted Amount 9502.75
BankwiseFraudChargebackIssuer&AcquirerReport
FileName:FCB_XXX_ISS_ACQ_DDMMYYYY_3C.xls.pgp
Bank Portal
Page No. 5/12

<!-- Page 6 -->

NPCIPortal ARCS BankePortal APrileged AccountManpgex JFBest JSONFormatterandJSX OEpochConverter-UnirTim
Notsecure10.40.56.24:9501/NPCl/authLogin
APS Last Login:29-Jul-2216:40.53 Welcome!MGSUSER
Buik File Download
SetlementFiles
MENU DESCRIPTION OldReports andArtifacts
User Management Facilitates addition and modiication ofboth Bank and NPCIUsers and Roles tobe assigned todesignated users
Configure FacilitalesonfigurationofparameerslkeM,Fees,Taxrates,SetlementHolidays,Settiemtycles,SpeciaiWorkingdays
Disputes Facilitates Uploadof ManualAdjustment fles.
Member Management Facitates additionandmodification af MemberBaniks ive on AEPS
Communication FacatatesAdditionandEditionofBroadcastMessages,E-LibraryandEscalationMatrix.
File Downioad Facitates downloading of Settement Files both Individually and Bulk.
Reports Faciltates downloedingofreportspertaining tobotn NPCIand Banks
Transachion Search Facilitates transaction searchandauthentication ofcisputes/adjustments.
File Regeneration Faciitates regeneration ofNGRTGS fles andcorresponding suthentications
Status Facilitates monitoring of Settement status and Batch run status.
小ENG 29-07-2022 17:01
Goto FileDownload>Bulk FileDownload
Select from and To date, Cycle number,Member BankName,FileType and click search
NPCI Portal ARCS Bank Portal XPrmileged AccpuntManagei×JF Best JSONFormatterand JS ×EpochComverter-Unix TimX
Notsecure/10.40.56.24:9501/NPCVfileSearchMembrstr
APS Lasl Login:29-Jul-22 16:40:53 WelcomelMGSUSER-
File Search
From Date* To Date* Cycle Name
28-JU-2022 28-Jul-2022 testJM 4C
Fle Type
Adjustment Report
File Searcn
Show 10 entries Search
BetchRunid File Name File Type Created Date Action
24536948(4C) JJM20220728_4C.xXs AdjustmentRepont 28-JUL-202217:39:13
Showing1to1of1entries
Downiaad Fa
D4ENG 29-07-2022 17:05
ClickDownloadbutton
Page No. 6/12

<!-- Page 7 -->

NPCIPorta ARCSBank Pontal XPnileged AccountManageXJF Best JSONFormatterand JS X OEpachConverter-UnixTimeX
ANotsecure/10.40.56.24:9501/NPCi/fleSearchMembrStr#
APSI Last Login.29-Ju-22 16.40:53 WelcomelMGSUSER
Slatis-
File Search
From Daa To Data' MemberNiame Cyce Name
2842022 28-J62022 testJUM
Fle Type
AdjustmentRepon
Fle Search
Show 10 Ventries Searche
BatchRunid Flle Name Fle Type Action
24538048（4C) JJM20220T28_4C.ls AdjustmentRepont 28-JUL-2022 17:38:13
Showing 1to 1of1 enties
Downiad Files
JM20220728_4C.xls Showall
17:05
29-07-2022
OpentheReport
JM20220728_4C-ENCel
Home Data Sign in. &Share
Cut Calibri WtapTest General ZAutosum
Paste Copy FomatPainter Merge&Center Formatting Conditional Fomat as Table" Styles Cell Insert DeleteFormat EClear Filter-Select- Sont&Find&
Clipboard Fom Alignment Number Styles Cells Editing
Adjustment
bxnuid uidAdjDate AdjType AcquirerIssuerResponseTxnDateTxnTime RRN TerminallD CardNo ChbDate
c2a82d2320d74866be0c7ddd3coe6f47112610293628-07-2022 FraudChargeback JM KKM register5555881002235845908
e825109cde8b4ee5b6931b073a0a569a117202141928-07-2022FraudChargeback JM KKM 0027-07-2022 11:16:50220811915859 register5555881002235845908
'1c4893df275147t7a9ee6232a5c6d41b119419510228-07-2022FraudChargeback JM KKM register5555881002235845908
42d3db196160476489f885dcele35953 1235785200 28-07-2022 FraudChargeback JM KKM 00'27-07-202211:16:50220811439255 register5555881002235845908
1c4893df275147f7a9ee6232a5c6d41b1466554537 28-07-2022FraudChargebackRepresentment JM KKM register5555881002235845908
'dd17407dfb644a96b268046ed65fcfd4145840123528-07-2022GoodFaithFraudChargeback JM KKM register5555881002235845908
11 'dd17407dfb644a96b268046ed65fcfd4112165081228-07-2022GoodFaithFraudChargebackAccept JM KKM register5555881002235845908
12
13
14
15
18
20
JJM20220728_4C
100%
ENG 17:07
29-07-2022
Page No. 7/12

<!-- Page 8 -->

Pleaseprefer Bankwisefraud chargeback summary reports
FileName:FCB_ISS_XXX_Summary_DDMMYYYY_3C.xls.pgp
GotoFileDownload→BulkFileDownload
Select From and To date, Cycle number,Member Bank Name,File Type and click search
RNPCIPortal ARCS Bank Portal PrvilegedAccountManage ×JF Best JSONFormaterand sXOEpochConverter-Unix Tint×
Notsecure/10.40.56.24:9502/AEPS/fileSearch
APS Last Login:29-Jul-2216:49.50 Welcomel shantajimmaker-
File Search
From Date* To Date* Cycle Nam File Type
28-Ju-2022 28-Jl-2022 FCBReport
File Sesren
Show entries Search:
Flle Name File Type Created Date Action
FCB_ACQ_JM_Summary_28072022_4Cxs FCBRepont 28-JUL-202217:40:28 Downioad
FCB_SS_JJM_Summary_28072022_4Cxls FCBRepont 28-JUL-202217:40:28 Download
FCB_ACQ_JJM_Summary_28072022_4C.csv FCBReport 28-JUL-202217:40.28 Download
FCB_SS_JJM_Summary_28072022_4C.csv FCBReport 28-JUL-202217:40:28 Download
Showing 1to 4of4entries (fitered from6total entries) Previous Next
Downoad Files
ENG 29-07-2022 17:17
Click Download file for download, pleasefind the below screen shot of summaryfile
BankName-JJM
Home Insent Dafa PShare
XCut Calibn General ZAutosum
ormatPainter Formatting Conditional Format as Table" Styles Cel Inset Delete Format EClear Flter-Select- Sort&Find&
Clipboard Number Shles Cells Editing
A1 NationalP aymentsCorporatianof india
National Payments Corporationof india
AadhaarEnabledPayment Service (AEPS)
BankwiseFraudChargebackSummaryReportfor28/07/2022to28/07/20224C
FraudCharFraud CharFraudCharFraud CharFraudCom.Fraud ComFraud Com Fraud Cor Amount
2501 2501
10
FCBACQJJM_Summary_28072022._4c
Ready
4ENG 29-07-2022 17:15
Page No. 8/12

<!-- Page 9 -->

IssuerBankInvestigation
FraudAnalysis &InvestigationReport
ISSUERBANKINVESTIGATION
CASEDETAILS
A. Date of Occurrenceof Fraud Transaction
B. Date of fraud reported by customer
2. CUSTOMERDETAILS
Full Name (mention namesof all joint holders,if
applicable)
B. Contact Number
MaskedAadhaarNumber(mentionAadhaarnumbersof
C. all joint account holders, if applicable Ex:XxxX XxxX
5678)
D. ResidentialAddress
City
State
PINCODE
BankBranchaddress
3. TRANSACTIONDETAILS
A. CorrectAadhaarSeeded (Y/N)
Transaction Type(Cash Withdrawal,Funds transfer,
Purchase transaction (Aadhaar pay), Cash Deposit)
C. Numberof Transaction Reported
Total amount of reported transactions (in Indian
Rupees)
TrxnDate|AcqID|TerminalID|RRNNumber（12
digitsasperBCS)/Amount/Timespan
4. ISSUERINVESTIGATIONDETAILS
HasIssuerBankreceivedwrittenfraud complaintletter
A.
from customer? (Y/N)
B. Is there any joint holder in customer's account? (Y/N)
Is joint account holder aware of fraudulent transactions
C.
reported by other account holder? (Y/N)
D. Customer's accounttype(Savings/Current)
Hascustomersharedhis/herbiometricwithother
entity/person for any purpose since the last 6 months? If
yes, provide details.
Is the customer regularly carrying out AePS transactions
at same BC locations?
G. HascustomerpreviouslydoneanyAePStransactionin
last6months
How did the customer cometo knowabout the
fraudulent transactions in his/ her account?
Page No.9/12

<!-- Page 10 -->

Customer's location at the time of transaction?
IstheCustomer'saccountstatementcheckedfor
J. reported transactions?
K. Any othercases reported against the same Bc?
L. What istheactiontakenbyIssuerBanktostop
M. Aadhaar No delinked from account? (Y/N)
N. Is customer's'mobilenumber/email id'updated in
AadhaarCard?(Y/N)
Is the customer's currently used mobile number updated
with the bankfor SMS alert?Also was the samenumber
used by customer at time of disputed transaction?
Are SMS notifications been sent to customer'smobile
P. number forreported transactions? If“No",provide
reason.
Reason for late reporting of fraudulent transactions by
customer
R. If any other specific details issuer want to report
S. Otherdetails
FIRDETAILS
A. FIR/Complaint Lodged (Y/N).
B. IF"No"Providereason
C. FIRNumber&Date
D. Police Station
Status of the case
PageNo.10/12

<!-- Page 11 -->

AcquirerInvestigationReport
Fraud Analysis&InvestigationReport
ACQUIRERBANKINVESTIGATION
1. CSP/BCDETAILS
A. BCAgentFull Name
B. Terminal ld
C. Contact Number
MaskedAadhaarNumber(Ex:XXXXXXXX5678)-Last
D. 4digitsonly
ResidentialAddress
City
State
PIN CODE
F. On-boardDate
G. Off-board/Termination/suspensionDate(lfapplicable)
H. ExitReason
Corporate BC details (If any)
2. ACQUIRERINVESTIGATIONDETAILS
IsBC contactable? If no, action taken by Bank for the
A. givencase
RegistermaintainedbyCSP/BC(YES/NO).IfYES,
B. share details.
C. Has BC agent collected any ID proof of the customer
What was the location of the agent at the date of
D. disputed transaction?
Whether the agent is working from a fixed location? If
E. yes, what is the location?
If No, where from he was operating during the last six
F. months and share the locations.
Whetherthereareattempts,successfulorfailedbythe
agent for the given Aadhaar with multiple banks? If so
G. the details thereof.
What is the procedure adopted by the acquirer bank for
H. engaging the BC agents?
If Acquiring bank is complied with Two factor
authentication(Yes/No)
What are the transaction limits,daily limits setforthe
agent?
Actiontakenbytheacquirerto stop subsequent
K. operationbyagent.
IsBCinvolvedinFraud?(YIN)
M. AnyPolicecomplaintfiledagainstBC?(YIN)
If BC is involved in fraud, hashebeen added in the
M1 negativelist&reportedtoNPCl
M2 If no, specify the reason
Page No.11/12

<!-- Page 12 -->

Fraud Type(FakeBiometric, Wrong Aadhaar Seeding,
N. SiphoningFraud,Others(withreason)
Brief Descriptionof the case/Modus Operandi
O.
Is Acquirer Bank providing consent forrefund to
P. customer?(YIN)
Q. Any otherdetails w.r.treported transactions/ case
Page No.12/12
