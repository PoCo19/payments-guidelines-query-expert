# Circular 132 - Settlement reconciliation and dispute management procedure for card to card fund transfer

Circular/reference number: NPCI/NFS/OCNo.132/2014-15
Date: 15th September, 2014

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.132/2014-15 15th September, 2014
To,
All MemberofNational Financial Switch (NFS)
Madam/Dear Sir,
Sub: Settlement,reconciliation and dispute management procedure for card to card fund transfer
One of the value added services operationalised by NPCl in NFS is card to card funds transfer. Using this
mode, bank customers would be able to transfer funds from one account to another account either in the
same bank or with another bank by using their Debit/ATM card at the ATMs of those NFS members who are
enabledforthis service.
Objective:
The objective of this circular is to familiarise NFS members with the settlement, reconciliation and dispute
management procedureforcardto card fund transfertransactions.
Transactionflow of cardtocardfund transfertransactionthroughATM
Cardto card fund
Beneficiary Beneficiary
transfertransaction BankSwitch BankCBS
10
AcquirerBank NPCI Remitter
Switch CentralSwitch (Issuer)Bank
FISwitch
11
12 The Remitter needs toinput the
beneficiary card numbertwice to
initiate the transaction.
Bank CBS
ATM
(Fig. 1)
Note: In case of beneficiary timed out response (i.e. Leg 1o shown in Fig. 1 above), the transaction shall be
treated as deemed successful transaction with response code (RC)as'71'for the credit (beneficiary) leg and
it will be considered for settlement.
Page 1 of 7
C-9,8thFloor HTqT/Phone:02226573150
RBIPremises ar/Fax:02226571001
Bandra-KurlaComplex 专-/email:contact@npci.org.in
Bandra East q专/Website:www.npci.org.in
400051 Mumbai400051
CIN：U74990MH2008NPL189067

<!-- Page 2 -->

Settlement and reconciliation procedurefor card to card fund transfertransaction
There shall be three entities involved for card to card fund transfer transaction as mentioned below:
a)Acquirer :whoseATMisusedbycardholderfortransferringfunds
b) Remitter(lssuer) :whoholdstheremitter'saccount
c) Beneficiary :whoholdsthebeneficiary'saccount
Settlement entries for card to card fund transfer(Net of reversals, ifany) is depicted in the tablegiven below:
Sr.No Remitter Transactionamount Interchange + Switching fees +
Acquirer Beneficiary servicetax service tax
(Issuer)
Debit Credit Debit Credit Debit Credit
Remitter* NPCI*
Remitter Beneficiary Remitter NPCI
Remitter Beneficiary Remitter Acquirer Remitter NPCI
Remitter Acquirer Remitter NPCI
Remitter Beneficiary Remitter Acquirer Remitter NPCI
Allamountsin (K)
SameBank
Different Bank
*Only ifthetransactionsareroutedthroughNFs
RawFiles,STL&DailySettlement(DSR)reports
Card to card fund transfer transactions shall be provided in the existing raw files, STL and DSR reports in same
format whichcan beused byNFSmembers for reconciliationand settlement.
RawFiles&STLReports
Details of cardtocard fund transfertransactions in rawfile&STLreport
TransactionType Transactions settled
Typeoftransaction (Record) File Card no.
Raw file STLreport (successful)
Acquirer Acquirerfile FT FTD Remitter ResponseCode-oo
Remitter (Issuer) Issuerfile TD FTD Remitter ResponseCode-oo
Beneficiary Issuer file TC DEP Beneficiary ResponseCode-oo&71
Note:
1.  For ON US transactions, RRN shall besame in all the three records for a particular transaction.
2.  ON US transactions can be identified on the basis of Card no. (BIN), Acquirer ID and RRN.
DailySettlementReport (DSR)
A separate line item shall available in DsR for card to card fund transfer transactions under Acquirer and
Issuer(Beneficiary &Remitter)section.SampleDSR report is provided in annexure'A'for reference.
Page 2 of 7

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Deemedsuccessfultransactions (RC-71)
For transactions that are timed out at Beneficiary's end (Leg '10' in Fig. 1 above), response code (RC) shall be
‘71'and the transaction will be considered as 'deemed successful'for the credit (beneficiary) leg i.e. for
transaction type TC'provided in issuer raw file. NFs members should consider the transaction amount
available in raw filefor reconciling deemed successful transactions.
Beneficiary bank should ensure that all the transactions settled (with RC-'Oo' and ‘71') by NFS are credited
to the cardholder's account. In case cardholder's account has not been credited online for a particular
transaction, it should be identified and manually credited to the cardholder's account by the beneficiary bank
as part of their daily reconciliation process. If Beneficiary bank is unable to credit the cardholder's account
due to any reason, in such cases the beneficiary should immediately raise credit adjustment for that
transaction to return the funds to the remitter. This is critical to avoid customer inconvenience and disputes
forcardto card fundtransfertransaction.
DisputeManagementProcedure
There shall be two records for a card to card fund transfer transaction in DMS as mentioned below:
Type of Bankcode Bankcode ResponseCode
transaction inAcquirer in Issuer Card No. forSuccessful Remarks
(Record) field field Transaction
Debit leg ConsideredforInterchangeand
Acquirer Remitter Remitter 00
(TD) switching fees for settlement
Consideredforfundsmovement
Credit leg
Remitter Beneficiary Beneficiary 00 & 71 for settlement (transaction
(TC)
amount)
Detailsofdisputecycleareprovided below:
DisputeType Tobe raised by Remarks
Chargeback Remitter Remittercan raisechargeback forsettledtransactioni.e.with
RC-oo&71,if customercomplaintsthat beneficiary
cardholder'saccountisnotcredited.
Representment Beneficiary Beneficiarycan representthechargeback providingtheproof
of credit (details)bythewayof a declaration provided in
annexure'B'.
Chargeback Beneficiary Beneficiarycan acceptthechargeback incaseamount cannot
Acceptance be credited to cardholder'saccount dueto any reason.
Pre-arbitration Remitter Remitter can raise pre-arbitration in casethedisputeis not
resolved at chargeback stage i.e.beneficiary cardholder's
account isnotcreditedorproperdeclarationisnotprovided.
Pre-arbitration reject Beneficiary Beneficiary can reject the pre-arbitrationproviding theproof
of credit (details)by the way of a declaration provided in
annexureB'along with additional documents like copy of
statement of cardholder's account having the credit entry for
the disputed transaction.
Page 3 of 7

<!-- Page 4 -->

Pre-arbitration Beneficiary Beneficiarycan accept the pre-arbitration in case amount
acceptance cannot becredited to cardholder's accountdueto any reason.
Arbitration Remitter Remitter can raise Arbitration in case the dispute is not
resolved atpre-arbitration stagei.e.beneficiary cardholder's
account isnotcredited/propersupportingdocumentsarenot
provided by beneficiary.
Debit adjustment Not applicable Sincebeneficiarytimedouttransactionsshall beconsideredas
deemed successfuland settled byNFS, therewouldnotbeany
requirementforraisingdebitadjustment bythebeneficiary.
Credit adjustment Beneficiary In casebeneficiary is not able to credit the beneficiary
cardholder's account dueto any reason, the amount needs to
be returned to the remitterbyraising creditadjustmentwith
appropriate reason code.
Please note the following for raising / addressing disputes and adjustment for card to card fund transfer
transactions in DMs
A separate menu option is provided in DMs for raising disputes and adjustments for card to card fund
transfer transaction. Menu options for raising dispute and adjustments are provided in annexure 'C'for
reference.
Disputes and adjustments can be raised only on transaction type ‘TC' having response code as 'oo' and
‘71'(i.e.successful transactions)for which funds are settled between Remitter and Beneficiary.
The timelines (TAT) for raising dispute shall be same as applicable for NFS cash withdrawal transactions
including applicable penalties. Customer penalty of Rs.1oo per day for delayed resolution shall not be
applicableforcardtocardfundtransfertransactions.
There shall beno movement of Interchangefeefordisputes and adjustments.
Disputes/adjustmentcannotberaisedforpartialamount.
Foranyqueries orclarification, pleasecontact:
Name e-mailID. Mobilenumber
AvinashKunnoth avinash.kunnoth@npci.org.in 8879772725
AbhayParekh abhay.parekh@npci.org.in 8879772794
Yours faithfully,
RamSundaresan
Head-Operations
Page4of7

<!-- Page 5 -->

AnnexureA
Sample DSR report containing card to card (C2C)transactions
DailySettlement StatementforABCBank ason8/08/2014
Description No.Of Debit Credit
Txn
AcquirerFundTransferDeclined
AcquirerBIApprovedFee
AcquirerBlApprovedFee-ServiceTax 0.618
AcquirerFundTransferApprovedFee 24
AcquirerFundTransferApprovedFee-ServiceTax 2.9664
AcquirerMSApprovedFee
AcquirerMSApprovedFee-ServiceTax 0.618
AcquirerWDLApprovedFee 15
AcquirerWDLApprovedFee-ServiceTax 1.854
AcquirerWDLTransactionAmount 500
Beneficiary Fund TransferTransaction Amount 800
IssuerWDLDeclined
RemitterFund Transfer Approved Fee 24
RemitterFund TransferApprovedFee-ServiceTax 2.9664
RemitterFundTransferApproved NPCISwitchingFee 2.5
Remitter Fund TransferApproved NPCI SwitchingFee-ServiceTax 0.309
RemitterFund Transfer Declined
RemitterFund TransferTransactionAmount 1,900.00
Rejected Chargeback &processed late reversal count
SettlementCharges
Issuer/AcquirerSubTotals 1,929.78 1,355.06
SettlementAmount 574.72
Page5of7

<!-- Page 6 -->

Confirmationofcredittobeneficiarya/c. Annexure-B
(OnBank'sletterhead)
Formatforrepresentment/RejectingPre-arbitrationforNFscardtocardfundtransfer
Madam/Dear Sir,
We refer to the below mentioned chargeback/pre-arbitration raised against our bank through Dispute
Management System (DMS)forNFS card to card fund transfertransaction:
Description Particulars
Disputedate
Remittercard number (masked)
Beneficiary card number (masked)
Transactiondate
RRN
ATMID
Transactionamount
We hereby confirm that afore mentioned transaction amount was successfully credited to the Beneficiary's
accountasperthedetailsmentionedbelow:
Description Particulars
Date&Timeof Credit
AccountNumber
Beneficiary Card Number (masked)
CBSReferenceNumber
We confirm that this declaration will be considered as a conclusive proof of our bank having credited the
Beneficiary's account and will be used as an documentary evidence in the dispute management process.We
also confirm that the remitting bank can confirm theremitter that beneficiary's account has been credited
as above and can share this confirmation form with their customer and/or any other authority as the
remittingbankmayconsidernecessary.
(AuthorisedSignatory)
Bankseal
NameoftheOfficial
Designation
Date
(Note:KindlyuseseparatedeclarationforeachRepresentment)
Page6of7

<!-- Page 7 -->

AnnexureC
Menu Option for raising disputesand adjustments for card to card (C2C)transactions:
Npcl-DisputeManagementSystem
Admin Adjustments Reports Files Search HISReport oustments IHPS BiAddition Adjustments
LMStLK9W126108/20143154100-PM Raie Credit
AdjustmentC2C
Scheduled DownTimses RaiceChargebackic2c
RaiseRepresentmentc2c
NFsDisputeManagementSystem Aoceptchargebackczc
Pre-Arbitratianlczc
Tha National Financiat Sotch Facilitates Interconngctivilty betraenPre-Arbitration Reject C2c
ATh Switchea and pirevides to thecusbomers a mderreachactosa thPre-Arbitration
Enabling on-lina rasolutiontBusinassneads ofinFsmembers AcceptC2C
artrabion_c2c
NpCI-DisputeManagementSystem
RaiseChargebackc2c
20/03/2014
RRN 407912099356
Submit
NPCl-DisputeManagementSystem
Dn20/00/2014
nefotarytlo RAN
407512999056 2G1219:1984127452003/201420/03/2014 409409
ktntlornto chackAdjustnhent
Raeod Annt
407912099156
NaanonCode Aaun
Note: Disputes/adjustments are raised on transaction type ‘TC'thus the card no.to be entered by the user
. should be of beneficiary.If beneficiary card no.is not available, keep it blank, transaction can be retrieved
onthebasisofdateandRRN.
Page7of7
