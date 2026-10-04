# NFS OC 396 NFS compliance to RuPay Specification

Circular/reference number: NPCI/NFS/OCNo.396/2021-22
Date: 28th May, 2021

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.396/2021-22 28th May, 2021
To,
All members of National Financial Switch (NFS)
Madam / Dear Sir,
Sub: NFS -Compliance to RuPay specification
We refer NFs Steering Committee meeting dated 26th Dec'19, where members were informed to comply
with RuPay online technical specification. It was also discussed that for few of the DE (data elements),
decline compliance rules shall be implemented in NFS switch.
In view of the above, please be informed that NPCl shall start declining transactions which have incorrect
where transactions shall be declined at NFS end is given in Annexure A for reference.
Please note importantly that for such transaction declines, the online Response Code (RC) sent to
member banks by NPCl shall be as given below:
'CA'for Compliance Acquirer for member bank acquiring transactions
‘Cl' for Compliance Issuer for member bank issuing transactions
Thus, members are requested to make note of the above and disseminate the information to the teams
/ department concerned for handling these RC in online message.
Date of enabling this validation for declining online NFs transactions shall be communicated separately.
Members shall be able to check the transaction count declined due to these RCs in response code wise
report in NFs back office (BCS) system. Members are once again requested to review the online
transaction messages and ensure that they are as per RuPay online technical specification.
Members can contact following officials for any further clarification / assistance:
Name e-mail ID Mobile Number
Sameer Gauli sameer.gauli@npci.org.in 88797 72730
Anand lyer anand.iyer@npci.org.in 98200 66464
ImranPatni Imran.patni@npci.org.in 82919 68533
Miller Koli Miller.koli@npci.org.in 88797 54947
Yours sincerely,
SMN
Saiprasad Nabar
Chief -OnlineProduct Operations
1001A,The Capital, B Wing,1thFloor,
BandraKuriaComplex,Bandra(E),Mumbai4ooO51
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

Annexure A
Details of scenarios where transactions shall be declined at NFS end:
Sr. DE. Particulars Decline Additional
No. details RC RC (DE - 44)
DE -22 Valid values: CA A022
021 - Magstripe stripe read, PIN entry capability
051 -ICC, PIN entry capability
080 - QR code, Unspecified
801 - Fallback transaction, PIN entry capability
901 - Full and Unaltered magnetic stripe read, PIN entry capability
951 - Chip card with unreliable CVD or iCVD, PIN entry capability
Transactions shall be declined for Invalid values i.e. Any values
otherthanthe above or if it is absent
DE-61 Transactions with ATM location PiN codevalues as non-numeric or CA A061
value contains all zero's (DE 61 - position 16 to 21 digits) or if it is
absent
DE - 4 Non-financial transactions containing amount shall be considered as CA A004
invalid value and it shall be declined:
a. Balance Inquiry
b. Mini Statement
c. Pin Change
d.Cheque Book Request
e. Statement Request
f. Aadhar number Seeding
g. Mobile number registration.
Financial transactions containing values more than the below given
limits shall be declined:
a) Cash withdrawal > Rs.10,500/- per transactions
b) Interoperable Cash Deposit transaction = > Rs.50,000/- deposit
c) Card to Card (C2C) transactions > Rs.5,000/- per transaction
DE - 3 Decline transaction type, other than the below types for MCC 6012 CA A018
a. Cash Withdrawal
b. Balance Inquiry
DE- 18 MCC other than the following values shall be declined: CA A018
6011-ATM transaction
6012-Micro-ATMtransaction
0880-Pungraintransaction
6013 - Card less cash withdrawal (ICCW)
DE - 35 In Service code 1st digit containing value other than the below CA A040
values shall be considered as invalid and these transactions shall be
declined:
1. 2, 5 and 6
acquired on NFSATMNetwork
