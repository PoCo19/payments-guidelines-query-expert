# Circular no.012 - NACH Direct debits

Circular/reference number: NPCI/2021-22/NACH/CircularNo:012

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2021-22/NACH/CircularNo:012 March 30,2022
To,
AllNACHMemberBanks
Madam/DearSir,
NACH-Directdebits
Refer tocircular NPCl/2016-17/NACH/CircularNo.219 dated March30,2017 and as perRBl mandate
we had migrated all the transactions credit and debit from ECs (156 file format) to ACH (306 file format).
We have been receiving new request from banks with regards to opening of additional legacy windows
for registering new mandates. Since the legacy has already been sunset, to streamline the process we
the request received from member bank. The change from previous process is only the file format, banks
are advised to go through the same (process flow & technical specifications enclosed) and ensure
compliance.
Withwarmregards,
(Giridhar G M)
Chief-Offlineproductoperations&technology
1001A,TheCapital,BWing,10thFloor,
BandraKurlaComplex,Bandra(E),Mumbai4OOO51
T:+912240009100F:+912240009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

HATEHLALTOAATEO LEARNE, HGUSE
Direct Debit Mandate Processing Document

<!-- Page 3 -->

NATICNALPAYMENYTSCORPDRATIOYOFANGA
Table of Contents
1.DIRECTDEBITMANDATEPROCESS
2. FILEFORMATS AND NAMING CONVENTIONS:
ACK FILE RECEIVED TO THE BANK
4. INW FILE RECEIVED TO THE BANK
5.. RESFILERECEIVEDTOTHEBANK.
Page | 2

<!-- Page 4 -->

NAIIONAL FAYATENTS CORPORATCNCEENA
1. Direrit.cebit Mandate Pirocess
Process to be followed for Preparation of Files:
The below is the process.flaw for the bulk jnitiation of mandates.
Create mandate. ml file need to be prepared:as per the enclosed file format and
zip the:xmi files. zip file should not exceed maxirium of 10mb post. encryption of
the file for initiation of the mandates by bank.
User will upload the file in gateway /h2h.
Gateway will perform technical validation, if fails the entire file will be rejected
and error ACK file will be sent to-the bank.
For files successfully passed the technical validations, an AcK file will be sent to.
bank.
 .MMs will perform business validation;, UmRN will be generated for all the accepted
items in Mms .and for thie failed cases Ack information will be given back to. the
banks
UMRN generated fcr this direct debit mandates'will be of below format.
BANK3000000000000001
BANK denotes:the bank short code. eg. SBIN, HDFC etc.s
"3" represents.direct debit mandate
 Remaining digits are running sequence numbers
Direct debit mandates which are created against the destination bank are auto.
accepted by the 'system.
When MMs event "Mandate .Acceptance Report. Cut-off" is reached, INW.zip -and
REs.zip will be created and pushed ta respective destination and sponsor banks.
2.file Farrnats ard Naming Conventkons:
Input File. to Npcl
The flat:file uploaded by sponsor bank wilt be. of. below format.
<ProcessName>-<TransType>-<Bank Short Code>≤Loginld><MMs. BusinessDate>:
<DIRDEB>≤nnnnnn>-INP.Xm!
ProcessName -mMs
Trans Type -CREATE
Bank Identifier - 4 Char Unique Bank [dentifier in System
Loginld - User Login Id
MMS Business Date -ddmmyyyy
Mandate identifier - DIRDEB
nnnnnn -Running sequence number for each xml file
E.g. MMS-CREATE-ICIC-1CICMaker-16022022-DIRDEB000001-INP.xml
Each xmil should contain single record data only.
Page13

<!-- Page 5 -->

NATICNAL PNMENTSCORPCRATONYOF NDA
All the child xml files need to be zipped.at once and'the zip file shoutd not exceed the
size 10 mb .after encrypting the zip file.
Zip file tame.shouid be as.below
<ProcessName>-<TransType>-<Bank Short' Code>-<Loginid>-≤MMs BusinessDate>-
<DIRDEB><nnnnnn>-JNP.zip
ProcessName -Mms
Trans Type -CREATE
Bank Idenitifier' - 4. Char Unique.Bank ldentifier in System
ILoginld - User Login. id.
MMS Business Date -ddmmyyyy
Mandate identifier - DIRDEB
nnnnnn -Running seguence number for each zip file
E.g. MMS-CREATE-ICIC-ICICMaker-16022022-DIRDEB000001-INP:zip
3. AK fle received to thebark
Once the INP zip file is received in Mms, it will.be validated xrnl.files in the zip and MMs
system will. generate UmRN for valid mandate request. The UMRN number will be provided
in the ACK.xml which is received in INP-ACK.zip
AcK file will contain the following for'each mandate
<ProcessName>-<TransType>*Bank Snort Code>-<Loginld>-<MMs Business Date>-
<DIRDEB><nnnnnn>-iNP-ACK.zip
The parent ACK zip (INp-ACK.zip) file name must be same as the input zip file name. The
parent zip (INP-ACK.zip) file contains the (INP-ACK.xml) for the child xmi files present
within it.
Child xml file will contain tne following for each mandate:
<ProcessName>--.TransType>-<Bank Short Code>-<Loginld> <MMs Business Date>-
<DIRDEB><nnnnnn>-INP-ACK.Xmt
E.g. MMS-CREATE-ICIC-ICICMaker-16022022-DIRDEB000001-INP-ACK.Xmi
MMS-CREATE-1CIC-ICICMaker-16022022-DIRDEB000002-INP-ACK,Xml
MMS-CREATE-1CIC-ICICMaker-16022022:DIRDEB000003-INP-ACK:xml
Page [ 4

<!-- Page 6 -->

NATIONAL RAYMENTS LORAGRATION GF INDA
4. INWfite received to thebank
Inward file will be generated when MAC Timetable:is execuited.
<ProcessName>-TransType>"<Bank Short.Code>-<MMS Business Date>-<DIRDEB><nnninnn> -
INW.zip
E.g. MMS-CREATE-HSBC-16022022-HVDIRDEB000121-INW.zip
MMS-CREATE-HSBC-16022022-LVDIRDEB000122-INW.zip
XML file generated in INw zip will .contain the original sequence no.of the [Np.xm!
E.g. MMS-CREATE-ICIC-IC1CMaker-16022022-DIRDEB000001-INP.xml
Sequence no.
used while
uploading.INP File
by Initiator Bank
5. REs filereceived tothe bark
MMs will send the mandate response files to.the mandate initiating bank after MAC.which
will be:received in gateway/h2h.
<ProcessName>+<TransType>:<Bank Short Code>-Loginld>-<mMs Business Date>.
<DIRDEB><nnnnnn>-RES.zip
E.g. MMS-CREATE-ICIC-IC1CMaker-16022022-DIRDEB000001-RES.zip
Zip file will contain Response for individual.acceptance of request from the receiver banks
anid'will'carry the narne as mentioned in the ACCEPTANCE request
E.g. MMS-ACCEPT-HSBC-SYSTEM-10062012- 000001-INP.Xml
Page15
