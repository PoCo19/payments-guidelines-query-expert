# Circular No.138 - Migration of NACH Credit 156 characters to 306 characters

Circular/reference number: NPCI/2015-16/NACH/Circularno.138

<!-- Page 1 -->

NPC
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/NACH/Circularno.138 December01,2015
To
AllNACHMemberbanks
Migrationof NACHCredit156charactersto306characters
Refer to our Circular no 119 dated August 25, 2015 on migration of NACH credit file format to
the ACH credit file format. Please be informed that a separate session will be opened for
processing the NACH credit files in the ACH credit file format from December 03, 2015.
This session will be on similar lines with the NACH credit (156) session wherein the input files
can be uploaded up to 7 days in advance. The product type for this session will be “"Ecs", which
needs to be given in the columns 262-264 in the ACH credit file format so that this can be tagged
intothespecificsessioncreatedforthis purpose.
The inward files will be made available to the member banks in the previous day evening itself
to allow sufficient time for processing the old account numbers. As directed by RBl during the
20th NACH steering committee meeting at Mumbai on October 15, 2015 the member banks have
to process the files if received with old account numbers as well and not to return the same for
technical reasons. Member banks are advised to put in place relevant utilities/arrangements to
convert the old account numbers to CBS account numbers for this purpose.
We have already taken up the project of converting the old account numbers, under this project
7.55 lakh records are already converted. It is expected that over a period of next 3 to 4 months
the old account number issue will be brought down to manageable levels. Member banks should
make arrangements to process the residual transactions that will come with the old account
numbers. Such transactions should not be returned.
To help the banks and corporates to move to the new file format, we are providing a file
converter to those sponsor banks who are still not ready to prepare the ACH 306 file format. The
convertor will have the following utilities
1.Validation offileprepared in306characterformat
2.:Validation of file prepared in 156 character format
The Capital, r-T/Phone:02240009100
1001 Unit No. 1001A, B Wing, gqm/Fax:02240009101
10 ,70, 10th Floor, Plot No. C-70, -/ email:contact@npci.org.in
 , f , GBlock,BandraKurlaComplex, aa / Website: www.npci.org.in
400051 Bandra (E),Mumbai 400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
3.Conversion of a validated 156 characterformat into 306 character format uploadable into
NACH system
4. Conversion of 306 character response file into 156 character response files.
The converter can be downloaded from the website www.npci.org.in.We have enclosed the User
guide cum installation manual.
Member Banks can upload maximum of 75,000 records in an EcS file and the file convertor is
capable of converting the same to ACH 306 format. In case Banks have multiple files with more
than 20,000 records (subject to maximum of 75,000 records per file) it is advised to convert one
file at a time rather uploading as bulk in the file convertor. Files with 20,000 or lesser records
can be converted in bulk subject to a maximum of 10 files per batch. Please note that the banks
using converter should take care of duplication of files due to manual errors by implementing
proper operational controls.
The converter will be available for a limited period hence all the member banks/users
institutions are advised to start processing the files directly on the 306 characters at the earliest.
The support for the converter will be available only for a limited period.
A separate session in the following name will be created on the similar lines of Ecs for the
migration purpose. The inward files for this session will be shared in the previous day similar to
the existing EcS session. Member banks can start present the files with effect from December
03, 2015 for the settlement date December 04, 2015.
Session Type Session Name SessionTime
Presentation Session ACHCR ECS PRES 10:00AMto 6:00PM
Return Session ACHCR ECS PRES_R 10:00AMto4:00PM
In case of any further clarifications please write to ach@npci.org.in.
For National Payments Corporation of India
(Giridhar G M)
VP & Head - NACH & CTS Operations
Annexure 1-User Guide cum Installation manual
The Capital, rHqT/Phone:02240009100
1001
Unit No. 1001A, B Wing, qm/Fax:02240009101
10-70,
10th Floor, Plot No. C-70, -/email:contact@npci.org.in
, f , G Block, Bandra Kurla Complex,
aarc / Website: www.npci.org.in
  400 051 Bandra (E),Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCi NATIONALPAYMENTSCORRORATONOINDIA UserManual:File Validator&Convertor
NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
FileValidator&ConvertorUserManual
Version 1.0
ATEDCLEA Page 1of 11

<!-- Page 4 -->

NPCI NATIONALPAYMENTSCORPORATIONCE NJIA
UserManual:FileValidator& Convertor
UserManual:FileValidator
Document Details
Version No. Date Description
1.0 30-11-2015 InitialDocument
Prepared By
Version No. Date Name & Position Signature
1.0 30-11-2015 PradeepKumarReddy,Officer
Reviewedby
Version No. Date Name&Position Signature
1.0 30-11-2015 Sankara Subramanian, Senior Manager
1.0 30-11-2015 Venkatesh SrinivasaRao,Manager
Approved by
Version No. Date Name&Position Signature
1.0 30-11-2015 BalamuruganVeeraswamy,AVP
NAIHIC
Page 2 of 11

<!-- Page 5 -->

NPCI NATICMALPAYMENTSCORPORATION GF INEIA
UserManual:File Validator  Convertor
TableofContents
FileValidator & Convertor UserManual
Objective
Installation.
Features
Processing Steps for File Validator.
Validation.
Basic Validations
FileNameValidations
FileDataValidations
Conversion.
Reports.
Validations that are not handled in this tool. 11
Support.
Page 3 of 11

<!-- Page 6 -->

NPCI NATICNALPAYMENESCDRPORATIONOEINDA UserManual:File Validator & Convertor
Objective
The objective of this manual is to provide step-by-step procedures for installationand usage of
the file validator & Convertor.
This tool will ensure that file passes through all technical validations before uploading to NACH
and also it will generate reports.
This tool will ensure to convert the credit format files from 156 to 306 format and vice versa
Installation
This file validator tool is a binary application which does not require any installation. Jar file to be
copied to the local hard diskand run by double clicking on it.
The following are the minimum system requirements to run thefilevalidator
System Os : Windows 98 and above
SystemRAM : 2 GB
SystemHardDisk :500MB
InternetExplorer : IE 6+
Java version : 1.6
Features
1.Validatorwill validate inputfileof ECSCR,NECSCR,ECSDR,ACH CR,ACHDR, ECSPUN
format.
2. Will accept only unsigned files.
3. Multiple files up to maximum of 10 files can also be validated at the same time (Note: If
the file is having 75,o00 transactions, then it is suggested to put one by one).
4. Summary report will be generated on every execution and detailed error report will be
generatedwhenthereisanerrorinthefile.
5.Validates the file naming convention as per the NACH standards other than the Bank short
code and Bank NACH userID.
6. Userfriendlytoolwithoutanyinstallationpackage.
NAHE
Page 4 of 11

<!-- Page 7 -->

NPCI NATIONALPAYMENTSCOHPORATIONCENOIA UserManual:FileValidator& Convertor
Processing Stepsfor File Validator
Userhastodoubleclickthetooltoopen,clickbrowsetoselectthefile(s)fromthe local machineand
click on the validate button to validate the files. Once all the files are validated, then only valid files
will be readyto convert from156to306format.
Userhas to click ontheconvertbuttonto initiate theconversion.Only successfullyvalidatedfilesof
Credit format are applicable for conversion.
The below screen describes thetool in detail.
10
File Validator&Civener v1.0
NACIE
NACHFileValidatcr&Converterv1.0
FileHame stuatss Totai Fioos Total Amount Acpt ficdtCont Acut Amount Rit itcds Cat Coey BicdsCat Cony Amou Export Remarts
ACH-CRUTKOC-JTKXM37Er-23112015-000011-NPtC 10.00 10.00 0.00 inValisFomat
23.00 20.00 0.00 in Vad Fomat
ECSCR-CSBk-CSBXMaker-23112515-300055-RES.tt FileName vanid
ECS-CR-SSIN-9EN/1234-23112015-100005-N:Ftt 100060 100003 03 160000 1E0000 00 0.00 100000 1000000.co
ECS-CR-JTX-UTKOMaker-22112015-00001E-INPDt 10.00 10.00 0.00
ECS-OR.VES8-YE5BMaker-22112C15-4NEWDCe-NP.t4 3.03 3.00 0.00 in.VangFormal
Brcws
Disclaimer
te theacrareement.
eGettirgtreflevelidaredinmeaidsteisoesncttantamourtoprocessngthebieinNac-systen,ternsveteprocesstrefeinNAc-nstenseuereteyeostvatdaon,Tesameshoul beoctifiedtc aift
ingbsnksheuidensurethp
fries
1. Click browse button to select thefile(s) from local machine
2. Click Validateto dothe validations of the selected files
3. Processed steps and status of each file will be displayed.
a. Valid':on successful validationof theentirefile
b. ‘Partial':for partial acceptance of the file (even if entire records are rejected, the files
will be shown as partial).
C. 'Error':iffile format is wrong
d.Converted':On successful conversion offile from156 to306and vice versa.
4. Click to select the product typeforconverting the INP file from156to306 format.Banks to take
caution when choosing the product type from drop down as it will affect the tagging to sessions.
5. Click on convert to initiate the conversion process.
6. Total number of records andamount uploaded for each of thefile will be displayed
7. Accepted Records and amount of each file will be displayed
8. Rejected Records and amount of eachfile will be displayed
9. Converted Records and amount of each file will be displayed
Page5of 11

<!-- Page 8 -->

NPCI NATIONALPAYMEN'SCORPORATIONCFNDIA
UserManual:File Validator Convertor
10.Descriptionon thestatus oftheeachfilewill bedisplayed
11. Remarks column will display the description of the error.To view the entire error message place
the mouse pointer on the error message which will pop up the entire error message.
Validation
Tool handlesthefollowingthree differentlevels of validations
Basic Validations
File Name Validations
FileContent Validations
Tool handles the following types of conversions.
ECSCRINP156toACHCRINP306format
ACHCRRES306toECSCRRES156format
Basic Validations
The following are the basic validations that are handled in this tool,
1..User clicks on Validate without browsing the file, then the alert will be displayed as “No File
Chosen".
2.File is uploaded without accepting the terms and conditions of the disclaimer, then error will
be displayed as "Accept the terms and conditions".
FileNameValidations
File name validations are handled as given below :
1.The files with the name starting with ECS-CR/ECS-DR/NECS-CR/ACH-CR/ACH-DR will only be
visible in the browsing windowto pick the filesfor validating.
2. In case the user uploads files other than theabove name,then file will be rejected with
3.  If the file name is not as per the naming convention given below, then the same will be
rejected.
File Naming Convention:
<Process Name>-<TransType>-<Bank ldentifier>-<Loginld>-<Date>-<Seg No>-INP.txt
Where:
ProcessName-Ex:ECS/NECS/ACH
TransType-
Page 6 of 11

<!-- Page 9 -->

NPCI NATCNALPAYMENTSCORFOHATIONCFNOA UserManual:File Validator& Convertor
CR-Credit file
DR--Debit file
BankIdentifier-4CharbankIdentifierasdefined inNACHsystem
Loginld-User Login Id of sponsorbank in NACHsystem
Date-ddmmyyyy (Dateof Upload)
Seq No-Running sequence number
Sample File Name:
ECS-CR-SBIN-SBINUser1-23062015-000001-INP.txt
4.Date in the file name will be validated against the current system date,forexample if the
date in the file name is not the current system date, then the same will be rejected with the
errormessageas"File date is not thecurrentdate".
5.If there are multiple errors in the file naming convention, say the date in the file name is
incorrect and RTN instead of INP, then error message will be displayed asThe file should be
an INP.txt file".
6.If the bank Identifier is not equal to four characters, then error message will be displayed as
"The file name should contain the bank short name".
7.If any file with improper naming convention or with incorrect data format is uploaded the
statusof thefilewill bedisplayedas"Error in Processing file"
File Data Validations
Only Technical validations will be done
Field format (Character, Alpha Numeric)
Type(Optional/Mandatory)
Header and Transaction codes should be as follows.
S.No Product Header Record
identifier identifier
ECS/NECSCR(NACHCR） 11 22
ECSDR(NACHDR) 55 66
ECSPungrain 11 21
ACHCRPRESENTATION 12 23
ACHDRPRESENTATION 56 67
Destination account type is an optional field, this field should be either space or to be filled
with any one of the fixed value 10,11,12,13,29,30,31.
The file length will be accepton belowvalues in between with Minimum and Maximum of
Page 7 of 11

<!-- Page 10 -->

NPCI NATIONALPAYMENTSCORPORATICNCF NDIA
UserManual:FileValidator&Convertor
ECS-CR/DRHeaderLength=133-156
ECS-CR/DRRecordLength=133-156
ACH-CR/DRHeaderLength=306
ACH-CR/DRRecordLength=306
Conversion
The userwill be able to upload ECS/NECS-CR INP file to convert ACH-CR 306fileformatand
vice versa.
Product type drop down will be available for the user to select the product type for the
ACH-CR INPfilethat will begeneratedfromtheECS-CR INPfile.
A convert button will be provided to initiate the conversion.
If the upioaded file ECS-CRINP/ACH-CR RES file, tool will be validated and then convert to
ACH-CRINP/ECS-CRRES file respectively on submittingtheconvertbutton.
The below fields are taking inputs from the tool while converting from ECS to ACH format.
1)In ECS INPformat, User Reference number in the Header is optional. Currently, if not
provided it will be populated from SFG. Now this field will be populated by tool with a
unique number.
2)Product type is a three character filed available in ACH file but not in ECS file format. So to
populate this field in converted ACH file, user has to select the product type from the
dropdown list given in the tool while converting. The chosen product type will be applicable
forallvalidfilesbrowsedforconversion.
3)Ledger Folio field characteristics are different from ECS to ACH file formats.We are handling
inthe below said manner.
LedgerFolio Field conversion
INPFile INW File RES File
S.No ECSFile ToolConverted SystemGenerated ACH Tool Converted
ACH File ACH INW File Generated ECSRESFile
.000. .000.. .00.. .000.. .000..
"01" "01" "01" "01" " 01"
"1" "1" "1 "1"
" 11" "11" "11" "11" "11"
"111" "111" "111" "111" "111"
"010" "010" "010" "010" "010"
"101" "101" "101" "101" "101"
"100" "100" "100" "100" "100"
NAH
Page 8 of 11

<!-- Page 11 -->

NPCI NATIONALPAYMENTSCDRPORATIONCEINDIA UserManual:FileValidator Convertor
Reports
DatalevelvalidationsarefollowedasperNPCl fileformats.
Tool will generated thefollowing two reports based on the input file uploaded.
1)Summaryreport
2) Detailed report
SampleFileName:
The report file name will have the uploaded file name itself for easy identification.
SummaryReport_ECS-CR-SBIN-SBINUser1-30112015-000001-INP.txt
DetailedReport_ECS-CR-SBIN-SBINUser1-30112015-000001-INP.txt
If there are no errors then detailed report will not be generated and only summary report will
be generated.
In case status of the file is Error then, the error description will be displayed only in the tool
under Remarks Column. No Summary and Detailed reports will be generated.
To view the Summary and Detailed Report, user has to double click on the file name visible in
the Tool interface which will open the reports.
SampleSummaryand Detailed Reports aregiven below.
Page9of 11

<!-- Page 12 -->

NPCi NATIONALPAYMENTSCORPOHATONOFINDIA UserManual:File Validator& Convertor
Summary Report
TheSummaryreportwili bedisplayedasbelow.
REPORI:MACH-R-! DM7ED:90/:172025
NATICIUL FAYMEHTS COFORATIOHI CEINDIA
DATAVALIDATTON SURDARY BEPORT (FART-A)
TILEIANE:EC5-CR-331M-557U3299894-30L:2015-AGT1:-10T.TN5
UBER DETATLS
CCRFORATEOSERNE PSocisl Weitoze
2:SPOMSOR BANE AND BRANCH ：799002002
SITEM CEILING AMOUNIT ：3060506756096
:16/11/2915
VALDATION DETAILS
3,TOTAL MMSEROF FECORDS 136952
S.L,SEMER CF VALID FECORDS 86947
S.3.WOSER OFINVALID RECORDS :4
6. HEADER ANGONT 1:5958809.00
Detailed Report
The detailed report will be displayed as below with all the errors in the file in detail.
REFCRT: NACH CR-R-2
RATIORA FAYMENIS CCRFOFATION CE INDIA
MANY Cr THE USTR:Scesel Welcere
NACH-DATA VALEDATION REFORT(FART-3)
GENERATEDBYNFCIASON30/11/203S SETTLENENTDATE AS FER FILE:S6/11/2ORE
records
REC-NO USER-BASK TFE AGCCUNT-MUNBER BNFY-SANX USER-N0 ANGUNT(aR PalSe) ERROR-MESSAGES
26 22 200200654 11869393495 2002c066. 0000000050090 reneficiary sheald te
799002902 3248101050739 799035501 T6:5029 000000030600 penetscsary shouia 
06597 799002302 124810:000-57 TO95TO664 renetaciary ahouid in Ascil Torma.
13 22 799002002 371810:000695 T813023 reneticiary
teras Totel oRs.15/056.000.00
Ceedit Teral -R3.15,25.40.00
Ditterence incant - R5.0.00
Teral Pecords #36952
Ne Cf Ferora -4
Page 10 of 11

<!-- Page 13 -->

NPCi NATONALFAYMENTSCCRPOHATIONOFINDIA UserManual:FileValidator&Convertor
Validations that arenot handled in this tool
NACH Business validation will not been included in this tool and all the Business validations
will betakencareonlyintheNACHsystem.
Validation is done for each field type as per current file formats.
Duplicatefile check indifferent executions arenot handled in this Validator.
Validation will not be automatically done once a change is done to a field in the file. User
needs to again browse the file and click validate button to do the validations.
Content in Bank Short name and Login user Id in the filename are not validated in this tool.
Support
Forany clarifications, kindly contact the following email ids.
ForOperational queries: ach@npci.org.in
ForTechnical queries: nachsupport@npci.org.in
NAHIO
Page 11 of 11
