# Circular No. 274 - Change in Return codes and descriptions

Circular/reference number: NPCI/2017-18/NACH/CircularNo.274

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2017-18/NACH/CircularNo.274 March 08,2018
To
AllNACHmemberbanks
ChangeinReturncodesanddescriptions inNACH
In view of feedback from different sources it has been decided to modify the descriptions of
few Return reason codes,further a few returns codes are blocked in the system as the same
conveythesamemeaningand henceappearstobeduplication.
Change in Return codes descriptions
The descriptions have beenmodified forthe following return codes:
Applicability
Sl.No.Code Existing descriptions
Reviseddescriptions
APB ACH
AccountClosed or
Yes Yes Account closed
Transferred
A/c Inactive (No
53Transactions for last 3 Yes Yes Account inoperative
Months)
DormantA/c(No
54Transactions for last 6 Yes Yes Dormant account
Months)
Simple Account, First Smallaccount,First
56Transactiontobefrom Yes Yes Transactiontobefrom
Base Branch Base Branch
InvalidAccount Invalidaccount Type
71 Yes Yes
（NRE/PPF/CC/Loan/FD) （NRE/PPF/CC/Loan/FD)
Comprehensive list of return and reject codes are provided in Annexure I & Il respectively.
Banks are advised to take extra care while returning the transactions with the reasons
mentioned inAnnexure lll whichareavoidable.
Central and State Governments have expressed difficulties in remittance of social security
benefits to the beneficiaries due to some returns which should not occur. Hence banks are
advised to review their internal guidelines in view of RBl notifications and eliminate returns
with the reasons mentioned in Annexure IV.
All the member banks are advised to take note of the amendments and make necessary changes
in their system.
1001A,TheCapitat,BWing.10thFloor,BandraKurla Compiex,Bandra(E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
ThechangeswillbemadeeffectivefromApril 1,2018.
This circular is issued in supersession of circular number 164A dated June 17, 2016.
Thahks,andRegards
GiridharGM
(SVP - CTS & NACH Operations)
1001A,TheCapital,BWing.10thFloor,BandraKuria Compilex,Bandra(E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN：U74990MH2008NPL189067

<!-- Page 3 -->

Annexure l
Return
code Return description ACH Credit ACH Debit APBS Credit ECS Debit
Account closed Yes Yes Yes Yes
No Such Account Yes Yes NA Yes
Account Description Does not
Tally Yes NA NA Yes
Balance Insufficient NA Yes NA Yes
Miscellaneous - Others Yes NA NA NA
Not. Arranged For NA Yes NA NA
Not Arranged For/Exceeds
Arrangement NA NA NA Yes
Payment Stopped by Drawer NA Yes NA Yes
Payment Stopped under Court
Order/Account Under
Litigation NA Yes NA Yes
Mandate Not Received NA Yes NA Yes
Miscellaneous - Others NA NA NA Yes
11 Invalid IFSC/MICR Code Yes Yes NA NA
Mismatch in mandate
12 frequency NA Yes NA NA
Duplicate transaction -
transaction already debited
either under ACH or NACH
13 debit (ECS) NA Yes NA NA
14 Mandate expired NA Yes NA NA
Incorrect amount-Mismatch
between mandate &
15 transaction NA Yes NA NA
16 Customer name mismatch NA Yes NA NA
Returned as per customer
17 request NA Yes NA NA
51 KYC Documents Pending Yes Yes Yes NA
Documents Pending for
52 Account Holder turning Major Yes Yes Yes NA
53 Account inoperative Yes Yes Yes NA
54 Account dormant Yes Yes Yes NA
A/c in Zero Balance/No
Transactions have Happened,
First Transaction in Cash or
55 Self Cheque Yes Yes Yes NA

<!-- Page 4 -->

Small account, First
Transaction to be from Base
56 Branch Yes Yes Yes NA
Amount Exceeds limit set on
Account by Bank for Credit
per Transaction Yes NA Yes NA
57
Amount Exceeds limit set on
Account by Bank for Debit. per
Transaction NA Yes NA NA
Account reached maximum
Credit limit set on account by
Bank Yes NA Yes NA
58
Account reached maximum
Debit limit set on account by
Bank NA Yes NA NA
59 Network Failure (CBS) Yes Yes Yes NA
60 Account Holder Expired Yes Yes Yes NA
61 Mandate Cancelled NA Yes NA NA
62 Account Under Litigation Yes NA Yes NA
Aadhaar Number not Mapped
64 to Account Number NA NA Yes NA
65 Account Holder Name Invalid Yes NA NA NA
68 A/c Blocked or Frozen Yes Yes Yes NA
69 Customer Insolvent / Insane Yes Yes Yes NA
Customer to refer to the
70 branch Yes Yes Yes NA
Invalid account type
71 (NRE/PPF/CC/Loan/FD) Yes NA Yes NA

<!-- Page 5 -->

Annexure II
Reason code Reason description
21 Invalid UMRN or inactive mandate
22 Mandate not valid for Debit transaction
23 Mismatch in mandate debtor account number
Mismatch in mandate debtor bank
Mismatch in mandate currency
26 Amount exceeds mandate max amount
27 Mandate amount mismatch
28 Date is before mandate start date
Date is after mandate end date
33 item unwound
76 Invalid Aadhaar format
82 Item marked pending
75 Transaction has been cancelled by user
77 Invalid currency
85 Participant not mapped to the product
86 Invalid transaction code
94 Amount is Zero
34 Invalid amount
31 Duplicate reference number
32 Invalid date
73 Settlement failed
74 Invalid file format
78 Invalid Bank Identifier
79 File sent after EOD and before SOD
96 Aadhaar mapping does not exist/Aadhaar number not mapped to IIN
81 Product is missing
83 Unsupported field
84 Invalid data format
87 Missing original transaction
88 Invalid original transaction
89 Original date mismatch
90 Amount does not match with original
91 Information does not match with original
92 Core error
93 Wrong clearing house name in SFG
95 Inactive Aadhaar

<!-- Page 6 -->

80 Wrong IIN
97 Bad batch corporate user number/name
Bad item corporate user number/name
99 Too many mark pending returns
72 Item cancelled

<!-- Page 7 -->

Annexure Ilf
Si. No. Return Reason Actionable
Bank should have an automated process to
deseed such Aadhaar number from NPCI Mapper
Account Closed or Transferred after account is closed
Banks are seeding NpCl mapper without linking
the Aadhaar in CBs or have wrong return reason
mapping in CBs. Banks should reconcile the
Aadhaar Number not Mapped to|Adhaar dump as per CBs and Aadhaar mapper
Account Number dump and seed/deseed the Adhaar number
Invalid Account Aadhaar numbers should not be seeded with this
(NRI/NRE/PPF/CC/LOan/FD) type of account
Bank shauld have an automated process to
Account Holder Expired deseed such Aadhaar numbers from Mapper
Bank should not return transactions with this
reason as NPC have provided a facility of
Network Failure (CBS) extension

<!-- Page 8 -->

Annexure IV
Code Descriptions RBI Circular Guidelines
Banks are advised to ensure that accounts of all
student beneficiaries under 'the various
Central/State Government Scholarship Schemes
Documents are free from restrictions of ‘minimum balance
RBI/2014-
Pending for and ‘total credit limit'.
15/226.RPCD.RRB.RCB.BC.
Account Have separate product code in CBs to accounts
No.32/03.05.33/2014-15
Holder opened by the beneficiaries under the various
dated September 10, 2014
turning Major Central/State Government Schemes including
Scholarship schemes for students so that the
stipulation of inoperative/dormant account due
to non-operation does not apply.
Appropriate steps to be taken including
Account allotment of a different 'product code' in their
Inoperative CBs to all such account so that stipulation of
RBI/2013.- 14/262.DBOD.No. inoperative accounts/dormant account due to
Leg.BC.53/09.07.005/2013 non-operation for over a period of 2 years does
-14 dated Sept 17, 2013 not apply while crediting the proceeds to such
RBI/2013- accounts for cheques, DBT, EBT, Scholarships,
14/313.RPCD.RCB.BC.No.4 Zero balance account etc. under Central and
Dormant 2/07.51.014/2013-14 dated State Government benefit schemes.
In order to reduce risk of fraud etc., in such
account Oct 7, 2013
accounts, while allowing operations in these
accounts, due diligence should be exercised by
ensuring the genuineness of transactions,
verification of signatures, identity etc.
Account Role of destination banks is limited affording
holder name credit to beneficiary's: account based on details
Invalid RBI/2010- furnished by the remitter/originating bank.
11/235/DPSS(CO)EPPD Reliance will be only on account number for
Account No./863/04.03.01/2010-11 affording credit.
description dated 0ct 14, 2010 The beneficiary name details may be used for
65 does not verification based on risk perception, value of
tally transfer, nature of transfer, post-credit.
checking.
