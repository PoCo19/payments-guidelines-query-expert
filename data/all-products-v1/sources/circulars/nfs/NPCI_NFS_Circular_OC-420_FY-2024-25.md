# NFS | OC 420 | FY 24-25 | Online reversal for failed ICCW transactions.

Circular/reference number: NPCI/2024-25/NFS/420
Date: 20th June 2024

<!-- Page 1 -->

NPC
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2024-25/NFS/420 Date:20th June 2024
To,
All Member of National Financial Switch (NFS) & Unified Payments Interface (UPl)
Dear Sir/Madam,
Sub: Online reversal for failed IcCW transactions
We refer to the NFS OC no.417 & UPI OC No.150 dated 17th June 2022 on Enablement of
Interoperable Card-less Cash Withdrawal (ICCW) transactions on NFS ATM Networks using UPl
for authorization.
For UPl-ATM ICCW transactions, the existing ReqPay API is extended with Reversal/Auto
Reversal functionality, to be implemented for both Issuer and Acquirer. The APl supports online
reversal in UPl for failed / unsuccessful ICCW transactions in below scenarios:
A.AcquirerinitiatedReversal-ATMReversal
In case the customer account is debited in UPl (success/deemed success) and the
transaction is failed at the ATM/ATM Switch, an online reversal shall be initiated from
NFs to UPl, based on the reversal request received from the Acquirer.
B.UPl initiated Reversal-AutoReversal
In case the customer account is debited in UPl (success/deemed success) and no
cash withdrawal request is initiated from the ATM/ATM Switch (Acquirer), the UPl
switch shall initiate an auto reversal.
The Technical specification document (TSD) for Reversal in UPI for failed / unsuccessful ICCW
has been released to members. To improve the customer experience, members are advised to
implement the ATM Reversal/ Auto Reversal functionality at the earliest.
Members are requested to disseminate the information contained herein with the concerned
department/officials.
Yours Sincerely,
SD/
KunalKalawatia
Chief of Products
1001A, The Capital, B Wing, 10th Floor
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 051.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067
