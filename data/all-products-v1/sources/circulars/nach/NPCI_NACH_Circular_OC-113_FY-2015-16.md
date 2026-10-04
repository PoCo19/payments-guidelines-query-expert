# Circular No 113 - Old Account Confirmation (OAC) Inclusion of PAN details in NSDL & CDSL records

Circular/reference number: NPCI/2015-16/NACH/CircularNo.113

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/NACH/CircularNo.113
August 05, 2015
To
AllNACHMemberBanks,
OldAccount Confirmation(OAC)-Inclusionof PANdetailsin NSDL & CDSLrecords
This is with reference our circular number 107& 108dated July 01,2015& July07,2015on
Old Account Confirmation (OAC) introduced by NPCIfor overcoming the legacy issue of the old
account number.
As you are aware National Securities Depository Limited (NSDL)& Central Depository Service
Limited (CDSL) are the major contributors in the Electronic Clearing Service (ECS) Credit. We
have persuaded them to use this service to convert the old account number to CBS account
number.
In order to facilitate matching and additional verification of the account numbers, Both CDSL
and NSDL will be providing PAN number of the customer. The bank receiving the record should
verify the PAN number (wherever available and provided by NSDL and CDSL) of the customer
and providethePAN number intheresponsefile.
Technical specifications
Input file (Annexure l)
1. PAN number at record level will be provided in “"Record reference number"which
is 15 character field.
2.This field will have 10 digit PAN number with right padded spaces for the
remaining 5 characters.
Response file (Annexure ll)
1. Destination bank should validate the records of the old account number with the
data available in their core banking system and the PAN details available.
2. If the PAN number matches with the old and the CBS account number, it should be
classified as the valid account number provided the account is eligible for receiving
the credits/ debits.
3. In case of mismatch of the PAN details, banks can directly treat that particular
record as invalid account.
4.This field is an optional field, hence in case if the PAN details are not provided by
CDSL/NSDL bank cango with the normal process of confirmation as per our circular
numberNPCI/2015-16/NACH/Circularno108datedJuly07,2015.
5. In case of valid accounts destination bank can update the records in the response
filewith thePANnumbers in "filler"field which has 22 characters.
The Capital,
1001 4T/Phone:02240009100
10-70 Unit No.1001A, B Wing, ar/Fax:02240009101
10th Floor, Plot No.C-70,
专-/email:contact@npci.org.in
G Block,Bandra Kurla Complex,
400051 aa专c/Website:www.npci.org.in
Bandra (E), Mumbai 400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFIINDIA
6. If the account valid flag is"N", then the filler field should be only spaces, System
will reject the file if the PAN details are updated in filler field if the account valid
flag is "N".
7. This field should be updated with PAN number as first 10 digit with right padded
spaces for the remaining 12 digits.
8.For the provided PAN details, system will validate whether the provided PAN is in
the valid format.System will look for the below
a.The first 5characters should be alphabets
b.The next 4 characters should be numeric
c.The last one character will be again alphabet
d. If the details updated in the filler field is not in order as above, system will
reject the file with reason“invalid PAN".
e. This field is an optional field, hence banks can update the PAN if the same is
updated in the core banking, else can be filled with spaces.
Member banks are request to kindly note the update and do necessary corrections at your
end.
Thanks and Regards
Giridhar G.M
(VP & Head Operations -CTS and NACH)
The Capital, y-ar/Phone:02240009100
1001
Unit No.1001A, B Wing, qr/Fax:02240009101
10-70 10th Floor,Plot No.C-70,
专-/email:contact@npci.org.in
G Block,Bandra Kurla Complex, q专/Website:www.npci.org.in
Bandra (E),Mumbai 400051
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure1
Input file from NSDL& CDSL
Old Account Conversion (OAC) File Format
Input File:To be Uploaded by Originator
Sr. No Field Description Length FieldType Mandatoryl Optional Field Description Sample Data Remarks
Header
Headerldentifier NUM Mandatory Theheaderidentifierto identitythetypeof file 31-ConstantValue
Originator Code ALPNUM Mandatory Bank codedefinedby NPC! HDFC FourCharactercodeassignedbyNPCi
ResponderCode ALPNUM Mandatory Bankcodedefined byNPCI Four Character code assignedbyNPCI
File Upload Date DATE Mandatory Date Onwhich fileis uploaded to NACH 02052015
Flie Reference Number 10 ALP NUM Optional Flle Numbergiven by Originatorfortheir H123456789
identification
Totai numberofrecords in thefile NUM Mandatory Total numberof records excluding header 020000
Filler 316ALPNUM Optionai Spaces ReservedField
Total 350
Records
Record Identifier NUM Mandatory Thedetail record identifier 71-Constant Value
Record ReferenceNumber 15 ALPNUM Mandatony PANNumber.First10digit followedbyspaces ABCDE1234F
iFSC/MICRcodeofthebankbranchat ALPNUM Mandatory IFsc/MICRcodewherecustomerholdsaccount SBIN0000001/6000020
which.customeraccountismaintained 01
AccountType NUM Optional NeedstobeasperNECS(10/11/12/13/29/30/31)or 10
blank
OldAccountNumber ALP NUM Mandatory CustomerBank accountnumber SB 1234
Account Holder Name 100 ALPNUM Mandatory Aspertherecords of Originator ROHIT
User Number NUM Optional CorporateUsernumberallotted byNPCi 6165920
UserName 20 ALPNUM Optional Name of the Corporate AirTel
Transaction Reference ALPNUM Optional LedgerFolionumberShare/DebentureCert 9878912345
No.,etc.
10 Accountvalidflag ALPNUM Optional Flag valueto indicate validity of account Reserved Field Spaces inINP file
11 CBS account number 35 ALPNUM Optional CBS account number ReservedField Spaces in INP file
12 Customernameas perCBS 100 ALPNUM Optional Asper therecords of Responder ReservedField Spaces inINP file
13 Filler 24 ALPNUM Optionai Spaces Reserved Field Spaces in INPfile
Total 350
The Capital, -TaT/Phone:02240009100
1001 Unit No. 1001A, B Wing, ar/Fax:02240009101
1070 10th Floor, Plot No. C-70,
-/email:contact@npci.org.in
G Block, Bandra Kurla Complex, aa/Website:www.npci.org.in
400051 Bandra (E),Mumbai 400051
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure 2
Response file
Old Account Converslon [OAC File Format
Response File:As Received by Originator
Sr, No Field Descriptlon Length FleldType Mandatory/ Optional Field Descriptlon Sample Data Remarks
Header
Header ldentifier NUM Mandatory The headeridentifierto identitythe type of file As giveninINPfile
OriginatorCode ALPNUM Mandatory Bank codedefined byNPCI HOFC As givenin INPflle
ResponderCode ALPNUM Mandatory BankcodedefinedbyNPCI SBIN As givenin INP file
File Upload Date DATE Mandatony Date On whichfile isuploadedto NACH C2052015 Asgiven in INPfile
Filie ReferenceNumber 10 ALP NUM Optional File Numbergiven by Onginator for their H123456789 Asgiven in INPfile
dentification
Filler Total numberofrecords in the file 316ALPNUM NUM Mandatory Optional Spaces Total numberofrecords excludingheader Reserved Field 020000 As given in INP file
Total 350
Records
RecordIdentifier NUM Mandatory Tne detail record identifier As given inINPfiie
Record Reference Number 15 ALP NUM Mandatory Uniquenumberto identifytherecord givenby H1234567 Asgiven in INPfile
Originator
IFSC/MICRcodeofthebankbranchat 11 ALP NUM Mandatory IFSC/MiCRcodewhere customerhoids account SBIN0000001/6000020AsgiveninINPfile
whichcustomeraccountismaintained 01
AccountType NUM Optional NeedstobeasperNECS(10/11/12/13/29/30/31)or 10 As givenin INPfile
blank
OldAccountNumber 20 ALP NUM Mandatony CustomerBankaccountnumber SB1234 As given inINPfile
Account HolderName 100 ALPNUM Mandatory Aspertherecordsof Originator ROHIT As given in INP file
UserNumber NUM Optional Corporate User numberallotted by NPCi 6165920 As given inINPfile
User Name 20 ALPNUM Optional Nameof the Corporate AirTel Asgiven inINPfile
TransactionReference 13 ALPNUM Optional LedgerFolionumber,Share/DebentureCert 9878912345 AsgiveninINPfile
No.,etc.
10 Accountvalidflag ALPNUM Mandatony Flag valueto indicate validity ofaccount Y/Nory/n Y/Nory/n
11 CBS accountnumber 35 ALPNUM Optional CBSaccountnumber 0123987456781234 if Accountvalid fiag is Yorythen CBSaccount
numbermandatory
itAccountvaidflagis'Norn'then CBS account
12 Customername as per CBS 100 ALP NUM Optional AspertherecordsofResponder ROHIT number should be space -If Accountvaild flag is"Yorythen Customer
name is mandatory.
ifAccountvalid flagis'Nornthen Customer
13 Return Reason code NUM Optional Two digit code as permentionedin the Return Aspermentionedin "if Accountvalid flag is"Yorythen return nane shouid be space
Reason codesheet theReturn Reason reason code will beblank if
codesheet Accountvalid fiag isNorn'then return reason
code should be twodigit code as permentioned
14 Filler 22ALPNUM Optional First1C Chartobe filledwithVAUDPAN if account intheReturn Reason codesheet If Account valid flag s Norn'then thefield
validflagis Yor'yandremaining12withspaces should be space
Total 350
The Capital, 7T/Phone:02240009100
1001 Unit No.1001A, BWing, arT/Fax:02240009101
1070 10th Floor, Plot No.C-70, 专-/email:contact@npci.org.in
 , af  GBlock,Bandra Kurla Complex, aa/Website:www.npci.org.in
Bandra (E),Mumbai 400051
CIN:U74990MH2008NPL189067
