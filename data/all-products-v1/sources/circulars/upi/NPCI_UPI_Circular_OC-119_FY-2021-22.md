# Circular 119 - Advisory on Reconciliation and handling declined timed-out transactions in UPI for One Time Mandate block transaction types

Circular/reference number: OC-119

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/UPI/OC No.119/2021-22 September 17,2021
To,
All Member Banks-Unified Payments Interface (UPl)
Madam / Dear Sir,
Sub: Advisory on Reconciliation and handling declined/timed out transactions in UPl for One Time
Mandate block transaction types
We refer to NPCI/UPl/0C No 78/2019-2020 dated January 27, 2020 towards 'Reconciliation and handling
declined/timed out transactions in UPl for One Time Mandate biock transaction types'.
Based on the analysis of disputes/grievances received on mandate transactions, following points to be
noted for purpose of reconciliation.
1. One Time mandate was made on the premise that mandate created successfully, should also be
executed successfully. But it has been observed that few of the execution transactions are getting
declined at the member banks/psPs end which has resulted hampering the product use cases. We
shall be working with the ecosystem as a network and try to handle such scenarios by deemed debit
for such declined transactions.
2. Acquiring Bank to ensure that the manual files are shared to NPCi on T+1 where T is the
execution/Revoke initiation day of the transactions post the reconciliation. The acquiring bank to
share the manual file only after proper 3-Way reconciliation of the transactions from NPCI RAW Files
as well as bank Switch and CBs files. Only transaction that are failed to be settled should be the part
of the recovery file and there should not be any duplicate cases/already successful/Deemed
Debit/Settled/Revoked mandates in the files shared by Acquiring Bank
3. Acquiring Bank to ensure that the execution has to be initiated before the mandate end date. And if
any execution which has not been initiated by the bank and the end date of the mandate is expired
the acquirer bank should inform the members on the same and take it up with the respective remitter
member bank. It will be the responsibility of Acquiring Bank to handle any disputes arising on account
of manual execution if any.
4. In case of revoke, file shall have all the revoke failed transactions.
5. In case of any duplicate settlement has happened, it shall be the responsibility of the Acquiring Bank
to identify such duplicate transactions and reverse the same to the respective issuer banks through
credit adjustments.
6. Post NPCl received the file, the same will be settled accordingly. It will responsibility of Acquiring bank
to ensure the correct file shared with NPCI. NPCI will not do any validation in files shared by Acquiring
Bank.
7.  Post the manual settlement of mandate transactions, it is the responsibility of Acquiring Bank to
resolve the dispute arising out of the same, if any.
8. File format to be shared for manual recovery transactions shall contain the following details to issuer
Banks.
1001A, The Capital, B Wing, 1Qth Floor.
Bandra Kurla Compiex, Bandra (E), Mumbai 4oo O51.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Sr. No Fields
Creation Date of the Mandate
Creation Txn ID
RRN
Blocked Amount
Payer PSp
RemitterPSP
Beneficiary PSP
PayeePSP
Mandate End date
10 Execution/RevokeDate
11 Execution/RevokeTxnID
12 Execution/RevokeRRN
13 Amount tobe Debited/Revoked/Partial
Debit
14 UMN Number
15 Online Response code
16 Online Error Code
17 Remitteraccount number
18 Remitter IFSC
Kindly make a note of the above and disseminate the information contained herein to the officials
concerned.
For any queries or clarification, please contact the following officials:
Name E-mail ID Mobile Number
Sapna Gupta Sapna.gupta@npci.org.in 7056446590
Pankaj Samarth Pankaj.samarth@npci.org.in 8108122861
Yours faithfully,
Saiprasad Nabar
Chief-OnlineProductOperations
