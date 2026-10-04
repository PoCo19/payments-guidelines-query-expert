# Circular No.172 Changes in return reason for APB

Circular/reference number: NPCI/2016-17/NACH/CircularNo..172

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2016-17/NACH/CircularNo..172
July 15, 2016
To
AilNACHmemberbanks
Changes in return reason for APB
NPCl is in the process of revising the return reason codes of APB, as under APB product the
transactions are processed based on Aadhaar number and also beneficiary name is not
provided in the file uploaded by the sponsor banks hence the reason “No such account
(reason code: 02)" is found to be redundant
The above reason will be removed from the list of return reasons of APB, W.e.f August 16,
2016.
The banks might be using the above reason instead of using the reason 'Aadhaar not mapped
to account number' (reason code: 64). Member banks are advised to review the return
reason mapping in their core banking and take immediate measures to remove mapping of
the above reason.
Further the banks are advised to keep the Aadhaar mapper in sync with NPCl mapper to
ensure
1. Only the Aadhaar numbers properly mapped in the CBS are seeded in NPCI mapper
2. In case of account closure the Aadhaar number is deseeded on the same day.
The banks should ensure that there are 'nil' returns for the reasons “Aadhaar not mapped
to account number" (reason code: 64) & "Account closed or transferred" (reason code: 01).
Banks are advised to take immediate action on the above sighted reasons and report
compliance.
For any clarifications please write back to ach@npci.org.in
Withwarmregards,
(Giridhar G M)
VP&Head-NACH&CTSOperations
1001A,TheCapitat,BWing.10thFloor,BandraKurla Complex,Bandra(E),Mumbai 400051.T:+912240009100F:+912240009101www.npci.org-in
CIN:U7A990MH200RNPI1A90A7

<!-- Page 2 -->

NPCI
Annexurel
NATIONALPAYMENTSCORPORATIONOFINDIA
Return
Code Return Description
AccountClosedorTransferred
AccountDescription DoesnotTally
Miscellaneous.Others
51 KYCDocuments Pending
52 Documents Pending forAccount Holderturning Major
53 A/cInactive (NoTransactionsforlast3Months)
54 Dormant A/c (No Transactions for last 6Months)
55 A/cinZeroBalance/NoTransactionshaveHappened,FirstTransactioninCash
orSelfCheque
56 SimpleAccount,FirstTransactiontobefrom Base Branch
57
Amount Exceeds limit set on Account by Bank for Credit per Transaction
58 Account reached maximumCredit limit set on accountby Bank
59 Network Failure (CBS)
60 AccountHolder Expired
62 Account Under Litigation
64 AadhaarNumbernot Mapped toAccount Number
Account Holder Name Invalid
68 A/cBlockedorFrozen
69 CustomerInsolvent/Insane
70 Customerto referto thebranch
71 InvalidAccount(NRI/NRE/PPF/CC/Loan/FD)
1001A,TheCapital,BWing,10thFloor,BandraKurla Complex,Bandra(E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067
