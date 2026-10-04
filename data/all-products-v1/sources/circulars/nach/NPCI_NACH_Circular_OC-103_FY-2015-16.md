# Circular No. 103 - NACH Header & Transaction Codes

Circular/reference number: NPCI/2015-16/NACH/103

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/NACH/103
June 12, 2015
To,
AllNACHMemberBanks
NACH Header & Transaction Codes
Madam/Dear Sir,
We refer to our circular number 83dated January 20, 2015 on Bank readiness to process new type of
transaction identifiers.NACH has five different products viz.APBS, ACH Credit, ACH Debit, NACH
Credit, EBT Credit. Each product is having its own file format, header & transaction level identifiers.
Based on the same, the products are identified by NACH system and Banks CBS.
2. The following are the Transaction codes which are currently used in NACH system
Transaction Files Transaction Transaction
Code Code
Header level Record level
ACH Credit
12 23
ACH Debit 56 67
APB Credit (Non-DBTL) 33 77
APB Credit (DBTL) 33 78
NACHCredit(ECSCredit-NonPungrain) 11 22
NACH Credit (ECS Credit-Pungrain) 11 21
(effectivefromOctober2015)
NACH Debit (ECS Debit) 55 66
AV/Mapper/Reverse SeedingFiles Transaction Code Transaction Code
Header level Record level
APBMapper(OldFormat) 21 24
APBMapper(NewFormat) 31 34
AccountValidationFile(AV)/ReverseSeeding(RS) 30 70
OACKFile 32 71
C-9, 8th Floor qT/Phone:02226573150
RBIPremises /Fax:02226571001
Bandra-Kurla Complex -/email:contact@npci.org.in
Bandra East aarc/Website:www.npci.org.in
-400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
3. To facilitate multiple sessions for multiple products in future, it is decided to have a fixed header
code as given in the above table. For the transaction code at the record level, the range will be
between 11 to 99.
4) Member banks are requested to get themselves prepared, by making necessary changes in their
internal system to handle the transaction codes at record level for each of NACH products as listed
WithWarm Regards,
(Giridhar G.M.)
VP&Head-CTS&NACHOperations
9，8 C-9,8thFloor -TqT/Phone:02226573150
RBIPremises /Fax:02226571001
Bandra-KurlaComplex -☆/email:contact@npci.org.in
Bandra East aa/Website:www.npci.org.in
400051 Mumbai400051
CIN:U74990MH2008NPL189067
