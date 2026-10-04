# Circular No.191 Narration in Customer Statement for NACH Transactions

Circular/reference number: OC-191

<!-- Page 1 -->

NPCL
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI: 2016-17/NACH/Circular No 191 October 05, 2016
To
All member Banks participating in NACH
Dear Sir,
Sub: Narration in Customer Statement for NACH transactions
As per the : RBI guidelines vide their circular DPSS(CO)EPDD No.
788/04.03.01/2010-11 dated 0ctober 8, 2010 all the banks should
furnish remitter details for credits received by customers through all
payment modes. Reference may be taken from NPCl circular 155/36
and 7 dated April 7, 2016, march 7, 2014 and May 31, 2013
respectively(copies attached) on providing valid narration in the
input file by the sponsor banks/corporates. The member banks need
to take care while processing the transactions in NACH.
The narration in the customer statement/pass book is extremely
critical as it would be help the customer identify the source and
reason of benefit transfer. Therefore it is important that the sponsor
bank includes it as a part of input file and destination banks are
advised to capture narration of NACH transactions in the customer
account statement/pass book. It is therefore essential to adopt a
uniform and standardized approach for providing relevant and
meaningful information to the beneficiaries/customers which will
help them to identify the source of credit/debit processed through
NACH.
Sponsor Banks/Corporates:
Sponsor banks should make it mandatory to provide ‘User Name' and
"User Ref. No.* in the relevant fields with meaningful information. In
addition to this banks may provide any additional information as they
deem necessary or useful.
Destination Banks:
The CBs system of the banks should be enabled to consume these
details and capture the complete information (including the name of
the corporate as provided in the transaction file) in the appropriate
fields (lnward file formats appended in Annexure) which will be
displayed whenever the accounts are accessed either through on line
mode or off line mode i.e. pass book and account statements.
1001A, The Capital, B Wing. 10th Floor, Bandra Kurla Complex, Bandra (El. Mumbai 400 051. T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN : U74990MH2008NPL189067

<!-- Page 2 -->

NFCI
NATIONAL PAYMENTS CORPORATION OF INDIA
The above would help the member banks to identify, track and
reconcile transactions without hassle for speedy resolution of
customer queries/complaints.
Member banks are advised to take a note of this and ensure strict
compliance to providing valid narration across all transactions
processed through NACH.
In case of any clarification please write to ach@npci.org.in.
Withwarm regards,
Giridhar GM
Vp & Head NACH & CTS operations
1001A, The Capital, B wing, 10th Flo0r, Bandra Kuria Complex, Bandra (E1. Mumbai 400 051. T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN : U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
ANNEXURE 1 NATIONAL PAYMENTS CORPORATION OF INDIA
APB INPUT (INP) FILE FORMAT
Input File:
The Username field can now be used for narration text, to explain the customer
about the transaction.
The Narration text field is of length 20 characters, starting from position 88 till
position 107. Possible usage to convey purpose Ex: DBTIOCLLPGCYL1
The User Credit Reference no has to unique for a customer for a day. Ex: LPG
consumer no.
The fields highlighted in the below picture are the Destination Bank lN Number,
Narration filed and User Credit Reference number.
00J221173555175 0005085481G31234 FIANUSUROT Q000.0000J100
000250629682154 PHANJ9TR02 0000000062100
00:317262625578 0005+954:1Gs_234narratic123 PHANJSJRO S 0016000540000
05026518601241
002355742348975 345 F"AHSJROS J 000200600
Destination Bank Naration Field, 20
JIN Number, 9 Digits, Alpha Numeric,
digit, Numeric, Mandatory
Optional User Credit Reference,
13 Digits, Alpha
Numeric, Mandatory
Inward file
 NPCl will automatically populate the lIN number into the inward file that reaches
the destination Bank and also the NACH Unique reference no of 10 digits.
The User Name field in Inward file will have the Narration value sent by Sponsor
will be populated with the data taken from the Input file.
 On successful transaction processing Destination banks needs to print the value in
User Name (Narration text) + User Credit Reference (sponsor bank transaction
ref. no.) into the Account statement / Pass book for Beneficiary customers.
77050558548C0 104221173555175 F'LNJS JRO1
0.0250329632164 PHAnJSUR02
09172626*5576 001555481GS12344L1113 FHA WSRO3 C3000000001000604999651275134550
701353859864i PHANJSUR04
170c0508698.: Q0035574211885 PMANJSUR'S 000000000010200001939572107035020
7700 150:548.J 00096927614121
Narration Field, 20
Destinstion Bank IIN Digits, Alpha Numeric,
Number, 9 Digits? Mandatory User Credit Reference.
Numeric, Mandatory. 20 Digits, Alpha
Numeric, Mandatory
Response file
The Narration field and the User Credit Reference number will be present in the
Return file also.
The Response file will contain the llN number populated by NPCl.
The file will have a Success flag with status (0 and 1). Where 1 is success and 0 is a
failure. This will be of 1 digit and will be at the position 154 in the file.
The Reason code will have “oo" for a Success transaction or a valid failure reason
code if the transaction has failed. This will be of 2 digits and will be filling positions
156 and 157 in the file.
The combination of Narration field and the User credit reference number can be
used to update the customer's passbook.
1001A, The Capital., B Wing. 10th Floor, Bandra Kurla Complex. Bandra [E). Mumbai 400 051. T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN : U74990MH2008NPL189067

<!-- Page 4 -->

NPCI
he Lpe h a
NATIONALPAYMENTSCORPORATIONOFINDIA
ACH -INPUT (INP) 3O6-FILE FORMAT
ACH Input File forimat
This File will be sent by User Instution ta h;PClI through sponsor bank
Freld Descrpbon Existng 'engn New Lengih.Fid ype Mal datory. Remaks
fHeacerjf redit Contra Reord
ACH transaction code NUM Mandatory 12 for ACH Credit, 33 for ACH APBS Cre dit, 56 for ACH Debit
Control ALP NUM [euogdo Spaces
User Name 40 40 AIP NUM Mandatory Alpha Numeric desciption
Control 14 14 ALP NUM Opdonal iSpaces
ACH File Number NUM Optional User defined inputtape
Control ALP NUM Optional Spaces
Contrel 15 15 ALP NUM Optional Spaces
Ledger Folio Number ALP NUM Optional Alphanumeric LedgerFolio particulars
User Cefined limit for individual Items 13 13 NUM Optiona Userdefined timit which would be taken for validating the credrt
/ debit items, in paise
10 [Total Amount in pa/se (Balancing Amount) 13 13 NUM Mandatory Amount in paise
11 Settlenent Date (CMMYYY) NUM Mandatory Date on which settlement is sought to be effected
12 Reserved (kept blank by usen 20 10 NUM Optional ACH File sequence number to be allotted by NPC
13 Reserved (kept blank by user) 10 NUM Optional Checksum Total generated by NPCI
14 Filler ALP HUM Optional Spaces
15 User Number Change 18 ALP NUM Mandatory FUser Bumberallotted by NPCI at the time of Registration
16 User Reference Change 18 ALP NUM Mandatory User defined reference number for the entire transaction (Alpha
Numeric)
17 Sp-onsor Bank IFSC / MICR / IN Change ALP NUM 5ponsor Bank IFSC / MICR /IIN code
18 User's Bank Account Number Change 35 ALP HUM reuogdo Account number of the User to be debited by Sponsor Bank
[Alpha numeric]
19 [Total Items New NUM Mandatory Total Iterns in File
20 [Settlenent Cycle (Kept blank by Userd] New NUM Optional Inthe presentation session forinput file, the settlement cyce
fiedilllankerrossing,whtheflesnto
destination bank, settlement cyde field will have system
generated waluein file header.
21 Fller New 57 ALP NUM Optional ISpaces
Total 303
Credit Records
ACH Transactlon Code NUM Mandatory. 23 for ACH Credit, 77 for ACH APBS, 57 for ACH Debit
Control ALP NUM Optional Spaces
Destination Aceount Type NUM As provided by Bank- Needs to be as per
NECS(10/11/12/29/3Q/31) or blank.
Ledger Folio Number ALP NURM Optional Alpha numeric Ledger Folio particulars
Control 15 15 ALP NUM Optlonal Spaces
Be neficiary Account Holder's Name 40 ALP NUM Mandatory for ACH- CA and ACH-DR Aipha humeric descri ption
control ALP NUM Optional Spaces
Control ALP NUM Optional Spaces
Usar kame 20 20 ALP NUM Mandatory Alpha numeric description
10 [Control 13 13 ALP NUM Optional Spaces
11 Amount 13 NUM Mandatory Amountin paise
12 [Reserved (ACH Item Sag No.) 10 NUM Optlonal To be alank
13 [Rese rved (Checksum) 10 NUM Optional To be Blank
14 Rese rved (Flag for success / retum) NUM Optional To be Blank
15 Reserved (Reason Code) NUM Optional To be Blank
16 Cestlratlon Bank IFSC/ MICR / IN Change 11 AUP NUM Mandatory for ACH-CR and ACH-DR Destn Bank IFSC/MICA/IIN
Beneficlary's Bank Account numbe? Change 35/ ALP NUM Mandatory for ACH+ CR and ACH-CR [Alpha numerlc descrlptlon
18 Sponsor Bank IFSC/ MICR / IN Change ALP NUM Mandatory Spnsr Bank IFSC/MICR/lIN
19 User Num ber Change 18 ALP NUM Mandatory User numberailotted by NPC
20 Transaction Reference Change ALP NUM Mandatory User deflned Reference Number such as Ladgar Folio huinber, or
Share / Debenture Cert, No, or Job Card No, orany other unique
identification numbergivenby theUserforthe Individual
beneficiaries
21 Product TYpe New AUP NUM Mandatory Itis a 3digit alpha numeric which is mapped te product feg: APB5
[Schemes), Ust of product types will be provded by NPCl.
Beneficiary Aadhar Number New 15 NUM Mandatoryfor APBS [Used in APBS fle for Aadhaar number.
22 UMRN New 20 ALP NUM Meandatory for Debit Unique Mandate Reference Number
23 Fillier New ALP NUM Optional Spaces
Total 156 306
CIN : U74990MH2008NPL189067

<!-- Page 5 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
ACH.--INWARD (INW) 3O6-FILE FQRMAI
ACH Inward data for Destinations Banks
This File will be send by NPCI to Destination Bank
Sr No Fieid bescr:ption Eusong Hew Field Mandatory'Optianal Remarks
Type
Heacer Record.
ACH transaction code NUM Mandatory 12 for ACH Credit, 33 for ACH APBS,56 for ACH Debit
Controf NUM Jeuondo Spaces
Filler 87 ALP NUM Optional Spaces
Control Character [Destn Bank Code] NUM Optional Spaces
Total Number of Items NUM Mandatory 999990 in the header actual number of transactions in the trailer
Total Amount (Balancing Amount) 13 13  NUM Mandatory Total amount in the file, in paise.
Settlement Date (DDMMYY) NUM Mandatory Settlement Date in ddmmyyy format
Filler 27 27 ALP NUM Optional saseds
Destination Bank [FSC / MICR /IIN Change 11 AlP NUM Mandatory Destn Bank IFSC/MICR/IN
Settlement Cyde New  NUM Mandatory Settement Cycle
11 Filler New 133 ALP NUM Optional ISpaces
306
CreditRecords
ACH Transaction Code Num Mandatory 23 for ACH Credit, 77 for ACH APBS, 67 for ACH Deblt
Control 9 alP NuM Optlonal Spaces
Destination AcxountType 2NUM Optional As providad In Input file
Ledger Follo Number 3 AlP NUM Optlonal Alpha numeric Ledger Folio particulars
Control 15 AlP NUM Optional Spaces
Beneficlary Account Holder's Name 40 ALP NUM Mandatory for ACH CR Name of Benoficiary
and DR
Control 8 Alp num! Optional Spaces
Control 8 ALP NUM Optional Spaces
User Name 20 2C ALP NUM  Mandatory Alpha Numeric description
10 Contro! 13 13 ALP NUM Optional Spaces
11 Amount? 13 13 NUM Mandatory Amount in paise
Reserved (ACH Item Seg No. 10 10  NUM Mandatory ACH item Sequence Number to be allotted by NPC
13 [Reserved (Checksum) 10  NUM Mandatory Checksum total generated by NPCl
Reserved (Fller) 7 AlP NUM Optlonal Spaces
Destl natlon Bank IFSC / MICR / IIN Change 11 AlP NUm Mandatory Destn Bank IFSC/MICR/IIN
16 Beneficiary'sBank Account humber Changt 35 ALP NUM Mandatory for CR and DR Account number of beneficiary
17 Sponsor Bank IFSC / MICR / IIN Change 11/ALP NUM Mandatory Spnsr Bank IFSC/MICR/IN
18 User Number Change 18 AlP NUM Mandatory User number allotted by NPCl at the time of Registration
19 Transaction Reference Change 30) ALP NUM Mandatory User deflned Rafarence Number such as LedgerFolia number, or Share
/Debenture Cert.No.or job card na,or any otherunlque idantification
number glven by the User for the individuat beneficlarles
Product Type New 3ALP NUM Mandatory Jtis a3digit alpha numericwhlch is mappedtoproduct(e.g.: schemes
In APas]
21 Beneficlary Aadhaar Number New 15 Mandatory for APES A number through which Beneficjary can be jdentifled. Used in APBS
file for Aadhaar number.
22 New 20 ALP NUM Mandatory for DR and Unlque Mandate Reference Number
Optional For CR
Reserved (Flag for success / return) NuM Optional Will be Blank
23 Reserved (Reason Code! NuM Optional will be Blank
Total 306
1001A. The Capital, B Wing. 10th Floor, Bandra Kurla Complex., Bandra (E1. Mumbai 400 051. T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN:U74990MH2008NPL.189067

<!-- Page 6 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NACH-DR - INP.156-FILE FORMAT
ECS Debit Input File Fomat
This File will be sent by User Institution to NPcl through sponsor bank
St No Freld De senphon. tength Fleld Typa Mandatory Remarks
fHeadar! Cradit Contra ecord
ECS transaction code for NECS NUM Mandatory Code SS for ECS Debit
User Number NUM Mandatory User number allotted by NPCI for NECS
User Name 40 ALP NUM Mandatory Alpha Numeric description - Contains Institution Nare
User Reference ALP NUM jeuondo User defined reference number for the entire transaction (Alpha
Numericl, If not provlded, wlll be populated trom SFG.
ECS flle number NUM Optional User deflned Input tape
Sponsor Bank MICR NUM Mandatory Sponsor Bank MICR
User's Bank Account Number AlP num Optional Account number of the User to be debltad by Sponsor Bank
(Alpha numerlc)
Ledger Follo Number AlP NUM Optional Alpha numeric Ledger Folio partlculars.
User Defined limit for Indivldual Items 13 NUM Usar defined limit which would be taken for validating the credit
/ debit items, in paise
10 Total Amount in pal se (Balanding Arnaunt) 13 NUM Mandatory Amount in paise
11 Settlement Date (DDMMYY) NUM Mandatory Date on which settlement is sought to be effected
12 Reserved (kept blank by user) NUM Optional ACH File sequence number to be allotted by NPCl
Reserved (kept blank by user) 10 Num Optional Checksum Total generated by NPC!
14 Filler 3. ALP NUM Optional Spaces
Total 156
Credrt Records
ECS Transaction Code NUM Mandatory Code 66 for ECS Debit
Destination sort code NUM Mandatory Destn Ban* MICR
Destination Account'Type NUM Optionat As provided by Bank - Needs to be as per
NEC5(10/11/12/29/30/31] or blank.
Ledger Folio Number Alp num Optionail Alpha numeric Ledger Folio particulars.
Beneficiary's Bank Account number 15 ALP nuM Mandatory Atpha numeric description
Beneficiary Account Holder's Name 40 AlP NuM Mandatory Aipha numeric description
Sponsor Bank MICR NUM Mandatory Sonsr Bank IFSC/MICR/IIN
User Number NuM Mandatory User number allotted by NPCI
User Name/ Narrazion 20 ALP NUM Optional Alpha numeric descriptior. Can be blank or will contain Narration
10 Transaction Reference 13 ALP NUM Mandatory User defined Reference Number such as Ledger Folio number,or
Share / Debenture Cert. No. or Job Card No. or any other unique
identification number given by the User for the individual
beneficiaries
Amount 13 NuM Mandatory Amount In paise
12 Reserved (ACH Item Seg No.] 10 NUM Optional To be Blank
13 Reserved (Checksum) 10 NUM Optional To be Blank
14 Reserved (fFlag for success / return) NUM Optional To be Blank
Reserved (Reason Code) NUM Optional To be Blank
Total 156
1001A, The Capital. B Wing. 10th Floor, Bandra Kurla Complex, Bandra [El. Mumbai 400 051. T; +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN : U74990MH2008NPL189067

<!-- Page 7 -->

NPCI
NATIONAL PAYMENTS CORPORATION OFINDIA
NACH-DR - INWARD 156-FILE FQRMAT
ECS Debit Inward File Format
This File will be send by NPCI to Destination Bank with Trailer
ON'S Field Description Length Field Mandatory/Optional Remarks
Type
Header Record
ECS transaction code for NECS Num Mandatory Code 55 for ECS Debit
Control NUM Optiornas Zeros
Filler ALP NUM Optiona! . Spaces
Control Character [Destrs Bank Code] NUM Mandatory Three digit Bank MICR code followed by four Zeros
Total Number of Items NUM Mandatory 999999900 in the header field. Should be hardcoded
Total Amount (Balancing Amount) 13 NUM Mandatory Blank for NECS
Settlement Date [DDMMYYYY] NUM Mandatory [Se ttlement Date in ddmmyy farmat
Filler 27 ALP NUM Optional Spaces. Filler to end with '!
Total 160
Credit Records
Ecs Transaction Code Mandatory ICode 66 for ECS Debit
Destination sort code Num Mandatory Destn Bank MICR
Destination Account Type Num Optional As provided in Input file
Ledger Folio Number ALP NUM Optional Alpha numerlc Ledger Folio particutars.
Destination Account number 15 ALP NUM Mandatory [Account humber of beneficiary
[Destination Account Holder's name 40 AlP num Mandatory [Name of Beneflclary
Sponsor Bank MICR Num Mandatory Sponsor Bank MICR
User Number Num User nurnber allotted by NPCl at the tirne af Reglstratlon
UserName 20 ALP NUM Mandatory Alpha Numerlcdescrlptlon-If Narration data was provlded, fleldwll
contain Narration details, else Will be filled with USerName from
header
10 Transacton Reference 13 ALP NuM Mandatary User deflned Reference Number such as Ledger Folionurmber, or Share
/ Debenture Cert. No. or job card no. or any other unique identification
numbergivenbytheUserfortha individual benefiaiaries
Amount 13 Num Mandatory Amount In galse
12 Reserved (ACH Item Seq Na.] 10 Num Mandator? ACH item Sequence Number to be allotted by NPCl
13 Reserved (Checksum] , 10 Mandatory. Checksur total generated by NPcl
14 Reserved [Fller] AlP nuM Optionat Flled wlth Spaces
Total 160
Traller Record
ACH transaction code Num Mandatory. Code 99 for NECS Credit
[Control 7NUM Optional 1Zeros
Flller 84 ALP NUM Optional Spaces
Control Character (Destn Bank Code) 10 NUM Mandatory Destlnatlon Bank's MicR code followed by a zero
Total Number of Items Mandatory Actual number of transactions fn the traller
6. Total Amount (Bal anaing Amount) NuM Man datory Total amount in the file, in paise.
Settlement Date (DDMMYYYY) Num. Mandatary Settlernent Date In ddmhayy format
Filf er 27 ALP NUM Optionat Spaces, Fllerto end wlth '!
Total 160
1001A, The Capital., B wing, 10th Fioor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051. T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN : U74990MH2008NPL189067
