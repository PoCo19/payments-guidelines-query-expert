# Circular No. 81 - Addition Of Reason Codes For NACH DBTL Transactions

Circular/reference number: NPCI/2014-15/NACH/CircularNo.81

<!-- Page 1 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2014-15/NACH/CircularNo.81 January07,2015
To
AllNACHMemberBanks
Addition of Reason codes forNACHDBTL transactions
Usage of “Miscellaneous-Others”return reason is causing inconvenience to the customers.
Onreview of the said return reason code and based on the feedback received from
participating banks it is decided to add three new codes to the existing list of return reasons.
Sl. No. Reason Description Reason Code
CustomerInsolvent/insane 69
Customer to referto the Branch 70
InvalidAccount(NRE/PPF/CC) 71
Revised return codes are provided in Annexure-l.Memberbanks are advised to review the
mapping of the entire set of return reason in their Core Banking System and include the above
reasons so that the"Miscellaneous -other"return reason is eliminated completely.
Further it is observed that member banks are returning the transactions with the following
reasons
1.Nosuchaccount (Reasoncode:2)
2. Account Description nottally (Reason code:3)
Inthecase of 1if thereis no suchaccount thenthememberbanks should deseed the Aadhaar
number immediately and also review the process to find out how the Aadhaar has been
updatedintheNPClmapperwithoutaccountbeinginexistence
In case of 2 the Aadhaar based transactions does not carry the name of the account holder,in
such a case the possibility of transactions getting returned with the reason ‘Account
description does not tally' are nil.
The above indicates that the banks have wrongly mapped the above return reasons instead of
"Aadhaar Number not mappedto Account Number(Reason code:64)'.Such inappropriate
mapping of return reasons should strictly be avoided.All the banks should immediately
review the mapping of all the return reasons and take corrective action.
WithWarn Regards,
(GiridharGM)
VP&Head-CTS&NACHOperations
C-9, 8th Floor TqT/Phone:02226573150
RBIPremises q/Fax:02226571001
Bandra-KurlaComplex -/email:contact@npci.org.in
Bandra East a/Website:www.npci.org.in
400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-A
Return
Code NACHCredit/APBCredit/NACHDebit
AccountClosedorTransferred
No Such Account
AccountDescriptionDoesnotTally
Miscellaneous-Others
51 Miscellaneous-KYCDocumentsPending
52 Miscellaneous-Documents Pending forAccount HolderturningMajor
53 Miscellaneous-A/cInactive(NoTransactionsforlast3Months)
54 Miscellaneous-DormantA/c(NoTransactionsforlast6Months)
Miscellaneous-A/cin Zero Balance/NoTransactionshaveHappened,First Transaction in
55 CashorSelf Cheque
56 Miscellaneous-SimpleAccount,FirstTransactiontobefromBaseBranch
57 Miscellaneous-Amount Exceeds limit setonAccountbyBankforCreditperTransaction
58 Miscellaneous-Account reachedmaximumCredit limit seton accountbyBank
59 Miscellaneous-NetworkFailure(CBS)
60 AccountHolder Expired
61 Mandate Cancelled
62 Account UnderLitigation
63 InvalidAadhaarNumber
64 AadhaarNumbernot MappedtoAccountNumber
65 Account HolderNameInvalid
66 UMRNDoesnotExist
68 A/cBlockedorFrozen
69 CustomerInsolvent/insane
70 Customerto referto theBranch
71 InvalidAccount(NRE/PPF/CC)
