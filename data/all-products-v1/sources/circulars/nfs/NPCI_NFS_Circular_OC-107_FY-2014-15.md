# NFS OC 107 NFS Network ATM - late reversal send by Acquiring bank

Circular/reference number: NPCI/NFS/OCNo.107/2013-14
Date: 4th January, 2014

<!-- Page 1 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.107/2013-14
February3,2014
TO,
All MemberBanksofNationalFinancial Switch(NFS)
DearSir/Madam,
Subject:NFSNetworkATM-LateReversal sentbyAcquiringbank
Obiective:
The objective of implementing the proposal contained herein is to reduce chargeback arising due to late
reversals sent by Acquiring bank. This will help customers to get online credit for the failed transactions
immediately.
Meaning:
NFs Business Day:All the transactions between 23:00 hrs.of immediately preceding day to 23:00 hrs. of
currentdayis consideredasoneNFsbusinessday.
E.g. from 4th January, 2014 23:00 hrs. to 5th January, 2014 23:00 hrs. is one NFS business day.
Late Reversals: Late reversal means a reversal message sent to NFs by the Acquiring bank after the cutover
of NFs business day.
E.g. transaction has happened between 4th January, 2014 after 23:00 hrs. and 5th January, 2014 up to 23:00
hrs. (i.e. at 4.00 pm on 5th January, 2014) and the reversal for the same transaction is sent by the Acquiring
bank after 23:00 hrs. of 5th January, 2014 (i.e. at 1.00 am on 6th January, 2014).
ExistingProcess:
When the Acquiring bank sends reversals after cutover of NFs business day, such reversals are not sent to
issuing bank online and are not settled as part of the daily settlement. Customer complaints are handled by
Issuingbankbyraisingchargebackforsuchtransactions.
ProposedprocessatNPCl:
NPCl will handle laterreversals received afterthe cutoverof NFs Business dayas follows:
Reversal will be sent to the Issuing bank online by NFS, if received upto immediately succeeding next
NFS business day i.e. T+1.
The original transactions will get settled as a successful transaction i.e. on T+1 as per the existing
process since NFS has not received the reversal till cutover time. [Debit Issuer - Credit Acquirer ]
The reversal transaction received after cutover of NFs business day but before the end of
immediately succeeding NFS business day will be settled as late reversal.[Debit Acquirer-Credit
Issuer]
HandlinglatereversalsinDMSduringsettlementprocess:
1.During settlementprocessDMS application will checklatereversals and match it with theoriginal
transactionoftheprecedingday.
Page1of6
C-9,8thFloor qT/Phone:02226573150
RBIPremises ga/Fax:02226571001
Bandra-Kurla Complex -/email:contact@npci.org.in
BandraEast aqisc/Website:www.npci.org.in
-400051 Mumbai400051

<!-- Page 2 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
If theoriginaltransaction is settledsuccessfully (RC-oo)onT+1 (NFSworkingday),then itwill be
reversed inDSRonT+2NFSworkingday.(Referannexure-A&B)
Additionally,inDMSapplication theresponsecodeforthat particulartransactionwill beupdated
(changed)fromRC-ootoacquirerdeclineresponse codeas perthe online reversal message i.e.
NFSRC-28,31,40,41&50andRC-26incaseofpartialdispense.
2.If chargeback is alreadyraised fortheoriginal transaction, DMS will check thefollowing:
If the chargeback is re-presented or accepted, there would be no updation of response
code in DMS and late reversal will not be considered in settlement.
If the chargeback is not re-presented, then the chargeback will be rejected and late
reversal shallbe processed by debiting acquiring bank & crediting the issuing bank during
thesettlementprocess (Referannexure-A).
List of such rejected chargeback will be made available in a separate menu option in DMs
forIssuingbank'sreference.(Referannexure-D&E)
3.If credit adjustment is already raised bythe acquiring bank then there would be no updation of
response code in DMS.Credit adjustment shall be settled as per theexisting process.Sincelate
reversal is sent online to Issuing Bank, it must be ensured that customer account is verified
before processingmanual credit as to avoid duplicate credit to the customer account.
4.Once late reversal is processed and settled on T+2, any attempt to raise chargeback or credit
adjustment will fail and the userwill beprompted witha message (Referannexure-C).
The above mentioned points are summarised in annexure G for ready reference.
ProposedprocesstobefollowedbyBank:
Banks mustdownloadtheVerification Reversal Report'madeavailableinDMSinXLSformat(Referannexure
D& E)and initiate action as applicableto different scenariosenumerated annexure F.This will facilitate bank
to handle exceptions identified during the reconciliation process.
Effective Date:The above process will be implemented with effect from 1gth February2014. (i.e.late
reversalssentfor18thFebruary2014transactions).
We requestyouto takea noteof the aboveand handlethe reconciliationprocess appropriately
For any queries in this regard, member banks may please contact the following:
Mr.RamaRaju,E-mailiD:rama.raju@npci.org.inMobile:08108122895
Mr.SourabhShukla,E-mailID:sourabh.shukla@npci.org.in:Mobile:08108122897
Mr.SaktiswarRao,E-mail ID:saktiswar.rao@npci.org.in;Mobile:08108122856
Yursfaithfully,
RamSundaresan
Head-NFs
Page2of6

<!-- Page 3 -->

Annexure-A
SampleDSR
Acquiring Bank DSR Issuing Bank DSR
Description No.OfTxn Debit Credit Description No.Of Txn DebitCredit
AcquirerWDLApprovedFee 13 195 IssuerWDLApprovedFee 13 195
AcquirerWDLApprovedFee-ServiceTax 24.102 lssuerWDLApprovedFee-ServiceTax 24.102
Acquirer WDL Declined IssuerWDLApprovedNPCISwitchingFee 6.5
AcquirerWDLTransactionAmount 8.000.00 lssuerWDLApprovedNPCISwitchingFee-ServiceTax 0.8034
AcquirerWDL-ProcessedLateReversalsandReversedAcquirerWDL Issuer WDLDecined
Approved fee 14 150 11
AcquirerWDLProcessedLateReversals andReversedAcquirerWDL Issuer WDLDeclinedNPCISwitching Fee
Approvedfee-Service Tax 18.54
AcquirerWDLProcessedLateReversalsandReversedAcquirerWDL IssuerWDLTransactionAmount
Transaction Amount 1413,000.00 13800.00
IssuerWDLProcessedLateReversalsandReversed IssuerWDL
Approved fee 150
lssuerWDL-ProcessedLateReversalsandReversed IssuerWDL
Rejected chargeback&processed late reversals-Count Approvedfee-ServiceTax 18.54
lssuerWDL-ProcessedLateReversalsandReversed ssuerWDL
Transaction Amount 14 13,000.00
Setlement Charges Rejected chargeback&processed late reversals-Count
Setiement Charges
Issuer/AcquirerSubTotals 13,168.548,219.10
lssuer/AcquirerSubTotals 8.226.4013.168.54
Setlement Amount 4,949.44 Settlement Amount 04.942.14
Page3of6

<!-- Page 4 -->

AnnexureB
Latereversalssettlementtable
LateReversalsSettlement
InterchangeFee+ SwitchingFee+
Transactionamount
S. Response ServiceTax Servicetax
No Code
Debit Credit Debit Credit Debit Credit
26 Acquirer Issuer ---Nil-- ---Ni-- ---Nil-- ---Nil--
28 Acquirer Issuer Acquirer Issuer ---Nil-- ---Nil--
31 Acquirer Issuer Acquirer Issuer ---Nil-- ---Nil--
40 Acquirer Issuer Acquirer Issuer ---Nil-- ---Nil--
41 Acquirer Issuer Acquirer Issuer ---Nil-- ---Nil--
50 Acquirer Issuer Acquirer Issuer ---Nil-- ---Nil--
Annexure-C
Following message will be displayed while raising chargeback/credit adjustment on reversed
transaction.
Possible ReasonsForHo Action
Action disabled because the transaction is not a successful
transaction - check response codes s transaction bype codes.
Close
Page4of6

<!-- Page 5 -->

Annexure-D
Menu option for downloading Verification Reversal Report
NPCI-Dispute Management System
Download SettlementFiles
26/12/2013
To Date 26/12/2013
Mode ALL
AL
NTSL
RAW Data file
STL
Verilication Reversal Report
LOgged In ASTESTBANKFOr
Annexure-E
VerificationReversal Report
National PaymentsCorporation ofIndia
Verification Report
TransT Resp Cardno RRN StanNo AcQ iss Trasn_Date Trans_ ATMId SettleDate Request Received Status
ype Code Time Amt Amt
Processed late reversal
andreversed originally
04 26 468805******8798 33571288511159744698 FBLAXB 12/23/2013 18:18:05 12/26/2013 3000 1000 settledtransaction
Processed latereversal
andreversed originally
'04 26 468805******8798 335712886752 59744704 FBL AXB 12/23/2013 18:18:06 12/26/2013 3000 1000 settledtransaction
Processedlate reversal
andreversedoriginally
'04 26 468805**#实**8798 335712890259 59744714FBL AXB 12/23/2013 18:18:10 12/26/2013 3000 1000 settledtransaction
Rejectedchargeback&
'04 26 468805*****8798 1335712888480 59744709 FBL AXB 12/23/2013 18:18:08 12/26/2013 3000 1000 processed late reversals
Rejectedchargeback&
'04 28 468805******791133571297864459744770 FBL AXB 12/23/2013 18:19:38 12/26/2013 500 processed late reversals
Rejectedchargeback&
04 28 468805*791133571298032659744775FBL AXB 12/23/2013 18:19:40 12/26/2013 500 processed late reversals
Rejectedchargeback&
'04 50 468805*****8798 33571247888559744964FBL AXB 12/23/2013 18:27:58 12/26/2013 500 processed latereversals
Rejectedchargeback&
04 50 468805**#大**8798 133571259029559745011 FBL AXB 12/23/2013 18:29:50 12/26/2013 500 processedlatereversals
Page5of6

<!-- Page 6 -->

Annexure-F
Action forhandling exceptions identified during reconciliation process by the bank
S.
Bank Description Action
No
Since the original transaction is reversed
with declined response code there is Acquiring Bank may raise debit
Acquiring
possibility of acquiring bank sending adjustmentwithvalidJP/EJproofsameas
Bank
wronglatereversal whilethetransaction existingprocess
isactuallysuccessful
1. Issuing bank to download all such
transactions on dailybasis
2. Check if the customer a/cis already
Issuing late reversal transactions,reversedtothe
reversed online-If Yes no actions.
Bank issuingbank
If customer a/c is not credited online
then issuing bank should reverse the
amountto thecustomer account
1. Issuing bank to download all such
transactions ondaily basis
2. Check if the customer a/c is already
Issuing Rejectedchargebacksandprocessedlate
reversed online-if Yes no actions.
Bank reversals transactions
If customer a/c is not credited online
then issuing bank should reverse the
amount to the customer account
Annexure-G
ProcessofhandlinglatereversalbyDMSapplication
HandlinglatereversalsbyDMSapplication
s.
No Scenario ActionbyDMs
Chargebacknot raised Late reversal will beconsidered
Chargeback raised and not re-presented Chargebackwill berejectedandlatereversal will be
oraccepted (i.e.before due date) considered
No actions
Chargeback raised and re-presented -Chargeback&re-presentmentshall beconsidered
-Late reversal will not be considered
Noactions
Chargeback raisedandaccepted -Chargebackshall beconsideredforsettlement
- Late reversal will not be considered
Credit adjustmentnotraised Latereversalwill beconsideredforsettlement
No actions
Credit Adjustment raised -CreditAdjustmentshallbeconsideredforsettlement
-Latereversal willnotbeconsidered
Page6of6
