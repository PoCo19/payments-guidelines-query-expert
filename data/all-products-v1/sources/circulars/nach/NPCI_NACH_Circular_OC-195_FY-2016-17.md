# Circular No 195 - ACH file creation tool for salary product

Circular/reference number: NPCI/2016-17/NACH/CircularNo.195

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/2016-17/NACH/CircularNo.195 November15,2016
To
All member banks participating in NACH
ACHfilegenerator-SAL&PEN
Refer to NPCl circular no.188 dated September 23, 2016 on“NACH salary credit identifier"
An offline tool has been developed for smooth and easy generation of ACH credit files for
salary and pension products. This tool along with user manual will be made available in
NACH landing page under FAQs tab.
Member banks to take note and share the offline tool & user manual to their respective
We wish to reiterate that government has formed Working Group on Development of
Employment Index, the group directed that salary and pension be categorized separately
with an identifier so that proper Mis can be generated for further analysis. All the
member banks are advised to process salary and pensions using the product codes “SAL'
and PEN'respectively (as detailed in the circular no.188 referred to above)
Foranyclarification,pleasewritebacktoach@npci.org.in
With warm regards,
(Giridhar G M)
VP & Head-NACH & CTS Operations
1001A,The Capital,B Wing.10th Floor, Bandra Kurla Complex, Bandra (E),Mumbai 400 051.T: +9122 40009100 F:+9122 40009101 www.npci.org.in
CIN：U74990MH2008NPL189067

<!-- Page 2 -->

NACHW
NATIONAL AUTOMATEO CLEARNGHOTSE
Usermanual forACHfilecreationtool

<!-- Page 3 -->

NATIONALPUMENTSCORPORATIONOFNDA Userguide forACHfile creation tool
Table of Contents
1. PROCESSFORPREPARATION OFINPUTFILES
2. POINTSTONOTE
3. DO'SANDDON'T'S...
Page12

<!-- Page 4 -->

NATIONALPAYMENTSCORPORATIONOFANDIA User guide for ACH file creation tool
1. Process for preparation of Input Files
The below are the details to be filled one time in the ACH file creation tool before
uploading the data file.
Maximum
Sr.
Field Description Field Type Remarks
No
Length
It is the name of corporate/ user
Alpha
User Name 40 institution (Eg Employer name) registered
numeric
as in NACH
Settlement Date Date onwhich settlementis soughtto be
Numeric
(DDMMYYYY) effected
UsernumberallottedbyNPClatthetime
User Number 18 of registration of corporate/ user
institution (Eg Employer name)
Alpha User defined (corporate/ user institution
numeric (Eg Employer name) reference number
User Reference 18 fortheentiretransaction(Alpha
Numeric) which will be used for the
corporate internally.
Sponsor Bank IFSC Alpha Sponsor Bank IFSC / MICR / IIN code
/ MICR / IN 11 numeric (corporate/ user institution's (Eg
Employer name) bank?
Alpha Alpha Numeric column in Record Level
Product Type
numeric (Eg :SAL,PEN)
ACHINP FileGenerator-NPCI
NPCI NACH
ACH INp File Generator
0 Input ORespone
User Nome Corporate name as registered in NACH
Settement daie 15-18-2016 Dateonwhichtheaccountshould actuallyhappen
Ueer Numbes 7/18 digit user number provided by NPCI
User Reference User/corporatereferencenumberforintemaluse
Sporsor Bank Code SponsorBankIFSC/MICR/IIN
SAL for salary& PEN for pension transactions
Eronrse
Generate
Page13

<!-- Page 5 -->

NC
NATIONALPAYMENTSCORPORATIONOFINDA User guide for ACH file creation tool
The data uploaded in the tool should be of the below specification
Maximum
Sr. Field
FieldDescription field Remarks
No Type
Length
Beneficiary Account Alpha Name of the beneficiary (Eg,
40
Holder's Name numeric Employee)
Amount 13 Numeric Amount for Individual
transactions to be given
Destination Bank IFSC/ Alpha DestinationBankIFSC/MICR/IIN
MICR /IIN numeric (Beneficiary bank details)
Beneficiary's Bank Account Alpha Beneficiary Bank Account
35
number numeric Number
Alpha A unique in number given by the
Transaction Reference 30 numeric User for the individual
transactions
Ram 10000.00 400002000687001015790 BUSXACH6382
Raj 12000.00 400002000 687001015790BUSXACH6383
Rajesh 14000.00 400002000 687001015790 BUSXACH6384
Krishnan 16000.00400002000 687001015790 BUSXACH6385
Rajasekhar18000.00400002000687001015790BUSXACH6386
Vinod 20000.00 400002000687001015790BUSXACH6387 TransactionReference
Beneficiary's Bank Account number
DestinationBankIFSC/MICR/IIN
Amount
Beneficiary Account Holder's Name
Page14

<!-- Page 6 -->

NATIONALPXYMENTSCORPORATIONYOFINOA UserguideforACHfilecreationtool
2. Points to note
This tool will support xlsx & .xls files
1i.. The file created in ACH format will be saved in the location where the tool is
placed.
i. Producttypeshouldbementioned as SAL,PENonly
3. Do's and Don't's
Do's
1. The Bank should provide amount with decimal values in the excel to be uploaded
(Eg 100.00)
2. The corporate has to share the file with the bank for uploading into NACH.
3. Transaction reference number should be unique for transactions in a single
settlement date.
4. Single quote () should be given for account number and reference number
records, if the same is starts with zero.
Don'ts
1.Do notprovidenull values inthetool.
2. Do not provide unnecessary spaces in the excel file uploaded in the tool.
Page/5
