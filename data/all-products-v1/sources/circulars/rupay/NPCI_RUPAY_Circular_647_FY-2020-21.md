# 09-Oct-2020 - NPCI/2020-21/RuPay/039 - Implementation of Reports and Dispute Management for Money Add transactions on RuPay Contactless Cards

<!-- Page 1 -->

NPCL
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCl/2020-21/RuPay/039 October 9, 2020
To,
All Members - RuPay
Dear Madam/Sir,
Subiect: Implementation of Reports and Dispute Management for Money Add transactions on
RuPay Contactless cards
store value of the card. Money add transactions currently feature in the following clearing reports.
Raw Data Files (85-Acquirer and 86-lssuer).
b) Approved DMS files (87-Acquirer and 88-lssuer)
A. In order to provide details about Money add transactions, a new report has been introduced in the
system which displays the transaction details of money add done through cash, money add done
through account and balance updates.
The naming convention of the report is MoneyAddReport_YYYY-DD-MM-N.csv, where YYYY.
DD-MM is the settlement date and N is the RuPay clearing cycle number.
This report will carry both approved and rejected money add records for any given cycle.
Please refer Annexure A for report formats.
B. Life Cycle Management:
Please refer Annexure B for sample illustrations to explain the possible scenarios and allowable life
cycles on Money Add Transactions - Cash.
Please refer Annexure C for allowable reason codes on progressive life cycles.
Member banks are requested to take a note of the same and disseminate the instructions contained
herein to all the stakeholders concerned
Page 1of7
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 400 O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
C1N:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTS CORPORATIONOFINDIA
Should you need any further assistance, please contact the following:
Name Email ID Contact Details
RuPay Operations rupayoperations@npci.org.in 022-40503495
Sonal Pagare Sonal.Pagare@npci.org.in 91-9152023894
Vaibhav Joshi Vaibhav.joshi@npci.org.in 91-8291847139
Murlesham Mithapalli murlesham.mithapalli@npci.org.in 91-8291847122
Gopakumar K P gopa.kumar@npci.org.in 91-9152085801
Yours faithfully,
SM.N
Saiprasad Nabar
Chief-Onfine Products Operations
Page 2 of 7

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
ANNEXURE A
Money Add Report File Format
The report has following elements and will be generated in .csv format.
S.No Field Data Type Sample Values
MTI N4 0100
Function Code N3 100
Masked Pan NS12-19 Masked Pan-Panwith onlyfirst 6 digits and last 4
digits in clear format and remaining Pan filled with
Eg : 123455*****1234
Transaction Local Date and Time N12 Actual date and time of transaction in
YYMMDDhhmmss
Retrieval ReferenceNumber N12 RRN - DE - 37 of online message
Transaction Type N2 23 - Money Add through account
24 - Money Add through Cash
29 - Money Add - Balance Update
Acquirer Institution ID code N6 Transaction acquirer - DE-32 of online message
Approval Code AN6 DE-38 of online message
Card Acceptor Terminal ID ANS8 Unique code assigned to the terminal - DE-41 of
online message
10 Transaction Amount N12 Transaction amount with 2 decimal piaces
eg : 1000 represents 10.00
30050 represent 300.50
11 Transaction Originator Institution AN11 Participant ID of the originator
ID code
12 Transaction Destination Institution AN11 Participant ID of the destination
ID code
13 Settlement Date N6 Settlement Date in YYMMDD format
14 Settlement Amount N12 . Settlement amount with 2 decimal places in case
of successful money add through cash
transactions
• 0 in case of
o Declined transactions
o Money add through account
o Balance update
Page 3 of 7

<!-- Page 4 -->

NPCIV
NATIONALPAYMENTSCORPORATION OFINDIA
15 Settlement DRICR Indicator A1 Debit/Credit indicator for settlement amount
D-Debit
C-Credit
"c" by default whenever settlement amount is 0 -
in case of
Declined transactions
Money add through account
Balance update
16 Processing_FeeTpCd N4 Processing Fee Type code
17 Processing_FeeAmt N18 Processing Fee amount
18 ProcessingFeeDCind A1 Processing debit/credit indicator
19 Assessment_FeeTpCd N4 Assessment Fee Type code
20 Assessment_FeeAmt N18 Assessment Fee amount
21 Assessment_FeeDCind A1 Assessment debit/credit indicator
22 IntrchngCtg_FeeTpCd N4 Interchange Fee type code
IntrchngCtg_FeeAmt N18 Interchange Fee amount
24 IntrchngCtg_FeeDCInd A1 Interchange debit/credit indicator
25 IntrchngCtg_Code N4 Interchange fee category
Page 4 of 7

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
ANNEXURE B
Illustration:AllowableLifeCycleScenarios
Charged to
Cardholder
Request
Txn by Money Money
by Resolution
Merchant Add add
customer
through through
account cash
INR 100 INR 100 INR 100 NA
INR 100 INR 100 INR 100 NA
Credit adjustment by Acquirer (Issuing bank to
ensure wallet is credited and not the Savings
account)
INR 1000 INR 100 INR 1000 Good faith by Issuer/Cardholder
Chargeback by issuer in case of partial/no
amount returned by acguirer and issuer can
prove that cash collected is more than the
amount credited in wallet
INR 1000 INR 100 INR 100 Customer requests merchant to add the
remaining 900
Credit adjustment by Issuer
INR 100 INR 1000 INR 100 Debit adjustment/good faith
(Merchant/Acquirer)
INR 100 INR 1000 INR 1000 Customer to sort this out with the issuing bank
Note: Chargeback life cycles will be available only for Money Add through Cash transactions as
illustrated above.
Page 5 of 7

<!-- Page 6 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Allowable Life Cycles forMoneyAdd throughCash
Current Status Dispute action for Dispute action for
Acquirer Issuer
Money Add through Cash - Declined 1) Debit Adjustment
Money Add through Cash - Approved 1) Credit Adjustment 1) Chargeback
2) Debit Adjustment 2) Credit Adjustment
3) Goodfaith 3) Goodfaith
Credit adjustment by Acquirer 1) Goodfaith 1) Chargeback
2) Goodfaith
Credit Adjustment by Issuer 1) Debit Adjustment 1) Goodfaith
2) Goodfaith
Debit adjustment by Acquirer* 1) Goodfaith 1) Chargeback
2) Goodfaith
Chargeback 1) Credit Adjustment 1) Goodfaith
2) Chargeback
Acceptance
3) Re-Presentment
4) Goodfaith
*Interchange movements shall be applicable.
Page 6 of 7

<!-- Page 7 -->

NPCI
NATIONAL PAYMENTS CORPORATION OFINDIA
ANNEXURE C
Allowable Reason Codeson progressiveLife cycles
The following reason codes will be availabie in the system for disputes.
1. Chargeback
Reason Code Description
1064 Goods or services not provided/not received
Note: Dispute amount can be greater than the transaction amount.
2. Debit Adjustment
Reason Code Description
2301 Cardholder was charged less than the actual amount
3. Credit Adiustment
Reason
Initiator Description
Code
2351 Issuer Duplicate Transaction
2352 Acquirer A Cardholder was charged more than the actual amount
2353 Acquirer A Cardholder was charged for unsuccessful/ Invalid/ Incomplete transaction
4.Pre-Arbitration
Reason
Code Description
1064 Goods or services not provided/not received
5. Good-Faith
Reason
Description
Code
2360 Others (Default)
Note:
1. Dispute amount can be greater than the transaction amount
2.  The existing TAT shall apply on the allowable reason codes.
Page 7 of 7
