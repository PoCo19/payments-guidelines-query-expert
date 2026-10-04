# UPI OC 128 - Extension of additional response codes under Deemed Debit for mandate execution

Circular/reference number: NPCI/UPI/OCNo.128/2021-22
Date: 14th December, 2021

<!-- Page 1 -->

NPCI
e Lpe hi at
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OCNo.128/2021-22 14th December, 2021
To All Members-Unified Payment Interface
DearMadam/Sir,
Subiect: Extension of additional response codes under Deemed Debit for mandate
execution
Mandate transactions functions with the premise that any mandate that is created successfully
must also be executed successfully. To reduce the remitter end declines in case of the
mandates execution including use case of [POs, we have developed the functionality of
Deemed Debit (DD) for financial mandate execution which was introduced through UPI OC
88 dated 14th May, 2020 - Migration of "UP] - RGCS" system to “UPI Real Time Clearing &
Settlement" (URCS) system w.e.f. 25th May 2020 wherein a few response codes under
mandate execution was considered as Deemed Debit.
Basis the ecosystem feedback, we have now extended the scope of Deemed Debit at the
remitter side further wherein any declines at the remitter end shall be considered as Deemed
Debit. Only in case if the remitter bank declines the transaction with the below mentioned
response codes the transaction shall be considered as failure and shall not be treated as
Deemed Debit.
Sr. No Decline ResponseCode and Description Decline by
59-- Suspected fraud,decline/transaction declinedbased on
Remitter Bank
risk scoreby remitter
K1- Suspected fraud, decline/transaction declined based on
RemitterBank
risk score by remitter
VO- Payment stopped by court order Remitter Bank
VH- Mandate signature is tampered or corrupt Remitter Bank
Any un-responded/declined transactions with invalid response code apart from the above for
mandate execution by remitter bank with Purpose Code 1, response shall be treated as
Deemed Debit and settlement shall be done by debiting respective remitter bank and credit
the same to acquirer bank. The identifier for such settlement shall be with response code RC-
1001A, The Capital, B Wing, 10th Flo0r,
BandraKurlaComplex,Bandra(E),Mumbai4ooO51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONAL PAYMENTS CORPORATION OFINDIA
DD (Deemed Debit) in URCS for identifying the deemed debit transactions separately and
initiate suitable actions in CBs. Also, additional report for transaction treated as Deemed Debit
is also provided to the member banks in URCs. The format of such report is mentioned in
Annex I.
With the increase of scope of Deemed Debit, the acquirer bank has to ensure that there should
transactions and reverse the same to respective remitter bank through credit adjustments on
same day or T+1 where T is the execution day of the transaction. Remitter banks are aiso
advised use the Deemed Debit report for reconciliation purpose and necessary actions.
With reference to the above request the member banks to take note of the above
enhancement and undertake the requisite changes.
Yours sincerely,
Saiprasad Nabar
Chief Online Products Operations & Technology
1001A, The Capital, B Wing, 10th Floor,
BandraKurlaComplex,Bandra(E),Mumbai4ooQ51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

Annex!
Please find the details available in the transaction Deemed Debit File
Sr, No Particulars (Headers in report) Description
TXN ID TransactionID
TXN Type Transaction Type
TXN Date Transaction Date
TXN Time TransactionTime
Settlement Date TransactionSettlementDate
Response Code Response Code
Error Code Error Code
RRN Reference No
STAN System Trace Audit Number
10 UMN/PayerAddress UMN/PayerAddress
11 InitiationMode Initiation Mode
12 Purpose Code Purpose Code
13 Payer Mcc Payer Merchant CategoryCode
14 Payee Mcc Payee Merchant Category Code
15 Payee Address Payee VPA
16 RemitterBank Remitter Bank
17 BeneficiaryBank BeneficiaryBank
18 BeneficiaryAccount Number Beneficiary Account Number
19 RemitterAccount Number RemitterAccountNumber
20 Amount Transaction Amount
21 PayerpSP PayerPSP
