# IMPS I OC 39 I FY 14-15 I Importance of Daily Reconciliation

Circular/reference number: NPCI/IMPS/OCNo.39/2014-15

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/IMPS/OCNo.39/2014-15 June06,2014
To,
AlltheMembersof ImmediatePaymentService (IMPS)
Dear Sir / Madam,
Sub:IMPS-Importance of Daily Reconciliation
Objective:The objective of this circular is to elucidate the importance of daily reconciliation of IMpS transactions.
This circular recommends process to befollowed by banks so as to attain efficiency in IMPS reconciliation and handling
exceptionaltransactions.
REMITTING BANK
Remitting banks should do reconciliation between switch & CBS data with IMPS raw data and ensure that total amount
debited to their customers'a/c (remitting bank's pooling a/c) is equal to the total amount shown as debit in the DsR
reconcile the total amount shown as debit in DsR is equal to the pooling a/c balance as per the cut-off. Any discrepancy
should be investigated entry-wise and appropriate action should be taken. We give below indicative action point under
various scenarios:
Initiate chargeback only in case of customer complaint for non-credit of beneficiary's a/c, provided the
beneficiary bank has not raised TCC (102/103)or Return,as the case may be.(Please referOperating Circular
NPCl/IMPS/OCNo33/2013-2014formoredetails).
Chargeback should not be raised if TCC is already present or funds are returned by beneficiary bank.
Download the Returns and credit adjustments raised by beneficiary banks and credit the remitting customer's
account immediately.
Download all settlement files and adjustments data daily which are made available in DMS application for each
settlement cycle and store it for future reference.
BENEFICIARYBANK
Beneficiary banks should do reconciliation between Switch, CBS and IMPS raw data. Please ensure that the total
amount shown as credit in DSR (Daily Settlement Report) is equal to the GL balance in the receivable pooling a/c. Any
discrepancy should be investigated entry-wise and appropriate action should be taken. Identify the un-reconciled or
unmatched entries and raise adjustments through DMS application, after taking appropriate action,wherever
necessary,asfollows.
ForTimedouttransactionsRC-08(ISO8583RC-91):
UploadTCC-102if beneficiarycustomer'sa/cis creditedonline
Upload TCC -1o3 if beneficiary customer's a/c is credited manually (since the transaction amount was not
credited online)
Upload RET-(Returns) if customer a/c cannot be credited due to various reason using relevant reason codes.
Do not return the funds without ascertaining whether manual credit can be afforded to your customer.
(Please refertoOperatingCircularNPCI/IMPS/OCNo28/2013-2014fordetailed reconciliationactions).
价-9，8升， C-9,8thFloor Hia / Phone:022 26573150
RBIPremises q/Fax:02226571001
Bandra-Kurla Complex 专-/email:contact@npci.org.in
Bandra East aa专/Website:www.npci.org.in
-400051 Mumbai400051
CIN：U74990MH2008NPL189067

<!-- Page 2 -->

Ensure that chargebacks are re-presented withvalid proof withintheTAT of3days (excluding chargeback day)
if thecustomera/c is credited eitheronlineormanually(pleaserefertoOperating CircularNPCi/IMPS/OCNo
28/2013-2014for details).
Download all settlement files and adjustments which are made available in DMS and perform reconciliation
accordingly,similarly respondtotheadjustments raisedby otherbankswithintheTAT.
ForapprovedtransactionsRC-oo
BankshouldcheckapprovedtransactionsbetweenIMPSrawdataandCBS.Incasetransactionis approvedat IMPSraw
customer a/c cannot be credited dueto anyreason, bank shouldreturn thefunds byraising credit adjustment in DMs.
Thereconciliationof RC-00and RC-08 (detailedabove)canbemerged intoa singleprocess.
Best practices:
Reconcile GL a/cs maintained for remitting and beneficiary transactions every day.This will help banks to
address the issue of surplus credits getting accumulated.
TimelyprocessingofTCCs/Returns/Creditadjustmentswill resultin:
Reduction of chargebacks,thereby saving time and efforts involved in addressing chargebacks raised by
remittingbanks.
Reductionofcustomercomplaintsfortimedout (RC-O8)transactions:
Facilitatetimelyresolutionofcustomercomplaints.
Properimplementation ofdaily reconciliation process shall not onlyhelp thebanks to haveabettercontrol overthe Gt
a/csforIMpStransactionsandaddress customercomplaints effectivelybutshall alsobenefittheoverallecosystem.
OtherOperational arrangements-Our suggestions
+ Automated Recon System-Avoid manual reconciliation system which may beerror prone.Banks should
automatetheentire IMPSreconciliation processtoavoiderrors andresultantfinancial loss.
SeparateReconciliationTeam-Banks should haveseparateand dedicatedteamtoreconcileIMPstransaction
andinitiateactionsonT+o/T+1.
Operations Team-Banks should have separateoperations team to handlecustomercomplaints of your own
bank andtorespondotherbank complaints.
TechnologyTeam-Toperform analysis ondailybasis andfind ifany incorrectrequestorresponsemessage is
sent or received by your switch or CBS.This has to be fixed immediately toavoid any repetitive errors and
resultantfinancial loss.
DR Setup-Banks shouldhaveDRsetup:In caseofmajorissueattheproduction system,bank can switchover
totheDRtoavoid declinetransactions thereby resultingto customericomplaints&reconciliation issue.
Foranyqueries orclarification,please contact:
1. SourabhShukla,E-mailiD.sourabh.shukla@npci.org.in;Mobile-8108122897.
2.;SaktiswarRao,E-mailiD.saktiswar.rao@npci.org.in;Mobile-8108122856.
Yoursfaithfully,
RamSundaresan
Head-Operations
