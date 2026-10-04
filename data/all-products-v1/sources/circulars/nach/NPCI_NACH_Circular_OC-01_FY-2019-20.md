# Circular No.01 - Introdution of new product type in NACH

Circular/reference number: OC-01

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
April 08, 2019
NPC/2019-20/NACH/CircularNo.001
To
AllNACHMemberbanks
IntroductionofnewproducttypesinNACH
Product type in NACH is a 3 digit code used to identify different categories of transactions.
Readinessofthebankstoacceptthenewproducttypewillfacilitatelaunchofanynewscheme
by Government departments or for introduction of new products of NPCl in future. Since new
product type creation is an activity carried out on an ongoing basis, banks are advised to build
parameterised facility to create 3 digit product type in system so that they will be able to
present as well as process inward transactions for any new products introduced on an on-
going basis. NPCl will provide a notice of 15 days to the member banks to configure the new
product type introduced before the actual launch of the new product. There will not be any
change in file format for the mentioned product types, however there will change in file naming
convention and product type or transaction code captured inside the file, details are provided
below.
To accept any alpha numeric value between field length 262 to 264 at record level in-
case ofACH Credit.
To accept any numeric value between field length 01 to 02 at record level in-case of
APB credit, reference can be taken to Circular no. 103 on "NACH header and
transactioncode"datedJune12,2015.
To accept any alphanumeric value in inward file name of both APB Credit & ACH
Credit in sequence number field between the length 4 to 6 characters.
Thefirst lot of product types that areto becreatedbybanks isprovided inAnnexurel.Banks
should be ready to process the new product types provided in Annexure Iby April 30, 2019.
Foranyclarification,pleaseraisethroughCRMtracker.
With warm regards,
Giridhar G.M
(Chief -Offline Products Operations)
1001A,TheCapital,BWing.10thFloor,Bandra Kurla Complex,Bandra (E),Mumbai 400051.T:+912240009100F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

ULN
NATIONALPAYMENTSCORPORATIONOFINXA
Annexurel
1. PM-KISAN
Product type-"KSN":
Applicable for account based credit only
Inputfile-Length262to264at record level
Inward file-Length266to268 at record level
Transaction code-“81"
Applicable for APB Credit only
Input file - Length 01 to 02 at record level
Inwardfile-Length01to02at record level
Input&responsefile naming convention (Both account&Aadhaar):
There is no change in input and response file naming convention, the same
process as followed by sponsor bank can be continued.
Inward file naming convention:
APB Credit: APB-CR-<Bank code>-<Date>-TPZKSN<Sequence no.>-INW.txt
ACH Credit:ACH-CR-<Bank code>-<Date>-TPZKSN<Sequence no.>-INW.txt
2.General
Product type-"GEN":
Applicable for account based credit only
Input file - Length 262 to 264 at record level
Inward file-Length266to268at record level
Transaction code-“82"
Applicable for APB Credit only
Inputfile-Length01to02atrecordlevel
Inward file - Length 01 to 02 at record level
Transactions which does not fall under any existing product type in ACH Credit
in APB Credit (77, 78, 79, 80) are to be presented under this product.
Input&responsefilenaming convention (Both account&Aadhaar):
There is no change in input and response file naming convention, the same
processasfollowedbysponsorbankcanbecontinued.

<!-- Page 3 -->

NPCI
NAFIONALPAYMENTSCORPORATIONOFNDIA
Inward filenaming convention:
APBCredit:APB-CR-<Bank code>-<Date>-TPZGEN<Sequenceno.>-INW.txt
ACHCredit:ACH-CR-<Bankcode>-<Date>-TPZGEN<Sequenceno.>-INW.txt
3.PRADHANMANTRISHRAMYOGIMAAN-DHANSCHEME:
Producttype-“"sYM"
Applicableforaccountbased(BothCredit&Debit)
Input file - Length 262 to 264 at record level
Inwardfile-Length266to268atrecordlevel
Input&responsefilenamingconvention(Accountbased-Credit&debit):
process asfollowed by sponsor bank can be continued.
Inwardfilenamingconvention:
ACHDebit:ACH-DR-<Bankcode>-<Date>-TPZSYM<Sequenceno.>-INW.txt
ACHCredit:ACH-CR-<Bank code>-<Date>-TPZSYM<Sequenceno.>-INW.txt
