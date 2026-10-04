# AePS | OC 46| FY 19 20 | AePS Harmonisation of TAT & Customer compensation

Circular/reference number: NPCI/AePS/2019-20/009

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/AePS/2019-20/009 October16,2019
To,
AllAePSMemberBanks
DearMadam/Sir,
Sub:AePS-Harmonisationof TurnAroundTime(TAT)and customer compensation for
failed transactions
We refer to RBI circular DPSS.CO.PD. No.629/02.01.014/2019-20 dated 20th September,
failedtransactionsusingauthorizedPaymentSystems.
RBl circular states that for every failed transaction, the credit amount shall be auto reversed
to the customer's account suo moto, without waiting for customer's complaint/claim along
withthe compensation in case of delayas per stipulated time.The circular also harmonises
the turnaround time (TAT) for such adjustments and compensation to be charged to the
participant deferring the adjustment.
directly attributable to the customer. Eg. Disruption of communication links, time out of
sessions etc.
Please refer Annexure A for change in TAT and customer compensation along with the
interimprocesstobeimplemented.
Please make note of the above and disseminate the instructions contained herein to the
officialsconcerned.
Foranyqueriesorclarification,pleasecontact:
Name E-mail MobileNumber EscalationMatrix
Rajendra Maurya rajendra.maurya@npci.org.in Level 1
Nayan Bhandarkar nayan.bhandarkar@npci.org.in Level 2
Gururaj Rao gururaj.rao@npci.org.in Level 3
Yours faithfully,
Giridhar GM
Chief-OfflineProductOperations
1001A,The Capital,BWing,10thFloor,
BandraKurlaComplex,Bandra(E),Mumbai4ooO51.
T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure A
AePs transactions includefinancial transactionssuch asCashwithdrawal,BHiM Aadhaar &
Fund Transfer (with successful bio-metric authentication)which are settled by NPCl with
Member banks.
AePs disputes are due to reasons such as Cash or Goods and Services not received by
customer.For AePS disputes, there is an existingprocess for calculation and settlement of
customer compensation fromchargeback datefor dispute types suchas Chargeback,Pre-
arbitration acceptance/deemed acceptance,Arbitration acceptanceandNRP/PRDdecision
in favour of Issuing bank.
As per new RBl circular, the framework for auto reversal and compensation for AePs
transactions are as follows:
FrameworkforAutoReversalandCompensationforAePStransactions
Descriptionof the Incident Timelinefor auto Compensation Payable
reversal
Cash Withdrawal -MicrolPro-active reversal (R)10o/-per dayof delaybeyond T +5
-ATMS for the faileddays, to the credit of the account holder.
transactionwithin
Customers account debitedmaximumof T+
butcashnotreceived 5 days.
AadhaarPay Acquirer  to initiateR100/-per day if delay is beyond T + 5
Account debited but"CreditAdjustment"days.
transaction confirmationwithin T + 5 day.
not received at merchant
location.
FundTransfer
Remitters Account is
debited but beneficiary
account not credited.
MemberBanksto notethat:
Tisthedayoftransactionand referstocalendardate.
TheprescribedTATistheouterlimitforresolutionoffailedtransactions.
Customercompensationshallbeapplicableondisputes/adjustmentssuchas
a)Chargebackacceptance/deemedacceptance
b)Credit adjustment
c)Pre-arbitrationacceptance/deemedacceptance
d)ArbitrationacceptanceORNRP/PRDdecision infavourofIssuingBank
e) Good faith Chargeback acceptance/deemed acceptance
1001A, The Capital, B Wing, 1th Floor,
BandraKurlaComplex,Bandra(E),Mumbai4oOO51.
T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
RolesandResponsibilities(Cashwithdrawal/BHiMAadhaar)
NATIONALPAYMENTSCORPORATIONOFINDIA
Acquirer/Issuer
a) For transaction failures at Issuer's Switch and NPCl switch,it is the responsibility
oftheIssuerBanktoreversetheamountto customer'saccount.
b) For transactionfailures at Acquirer/BC/Merchant locationand wherecustomer
has not received Cash, availed Good orServices:
Acquirer/BC/Merchant to initiate a credit adjustment within 4 calendar days
from the transaction date. Amount to be reversed to the Customer's account
within 5 calendar days
WhereAcquirer/BC/Merchanthavefailedto initiateaCredit
adjustment/Refund,if thecustomerlodgesacomplaint withtheIssuing bank,
IssuingbanktoinitiateachargebackwithspecificMMT (MemberMessageText)
as ‘Transaction not successful - Failed at Bc/Merchant location' to identify
disputes arising dueto such Failed Transactions.
RolesandResponsibilities(FundTransfer)
Acquirer/Issuer
Issuer Bank to initiate Debit Adjustment for Timed out transaction (RC -O8) where
customeraccount iscredited onlinewithin4daysfrom thetransaction date.
Acquirer Bank shall wait for Debit adjustment upto 4 days from the date of transaction,
if not received then reverse the customeraccount on 5th day.
In view of RBl circular, we have to introduce certain changes in the BCS back office system
which is as mentioned herein below:
(The changes in Bcs shall take some time. Therefore, we shall implement an interim
processforcompensationcalculationandsettlement.)
1. Existing DRC penalty for failed Cash Withdrawal transactions will be discontinued.
However,Memberbanksshall continuetoreceivetheDRC reports.
2. Debit Adjustment TAT for Fund transfer transactions shall be revised from the
existing5calendardaysto4calendardays.
Manual process for calculation & settlement of customer compensation (before
implementationofchangesinBcS)
Customer compensation on the disputes/adjustments for transaction dated from
15thOctober,2019 shall be calculated as pernew RBl circular and settled through
manual adjustment at regular intervals.
Thepenalty amount settled through manual adjustment shall be captured inDaily
SettlementReport(DSR/NTSL)asseparatelineitemwithpropernarration.
Thedisputewise/adjustmentwisedetailsofthecompensationcalculated shallbe
provided at regularintervals under'File Download'option in BCS system.
1001A,TheCapital,BWing,10thFloor
BandraKurlaComplex,Bandra(E),Mumbai400O51.
CIN:U74990MH2008NPL189067
