# Circular No.88 - Updation of mapper files response in banks database

Circular/reference number: NPCI/2014-15/NACH/CircularNo.88

<!-- Page 1 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2014-15/NACH/CircularNo.88 February18,2015
To
AllNACHMemberBanks,
Updationof mapperfiles response in banks database
Please refer to the standard operating procedure for Aadhaar seeding by the banks.For
seeding the Aadhaar numbers into NPCl mapper the member banks are using the upload
format,for every file uploaded by the banks the system will provide a response file.It is
essential that the member banks use the response file to update the status of NpCl mapper
against each Aadhaar number in their database so that the status can be accessed by the
frontofficeofficialsto answerthequeriesof thecustomer.
PleaserefertoourcircularNo:NPCI/2014-15/NACH/CircularNo67datedDecember05,2014
where in the detailed guidelines are given for Aadhaar seeding in a new file format.
Theinputfileand responsefilenaming conventionwillbeasfollows
Inputfile:ACH-CM-KUNS-KUNSMaker-13022015-000005-MAP.txt
Responsefile:UID_Response--ACH-CM-KUNS-KUNSMaker-13022015-000005-MAP.xml
1.There is a possibility of all the records uploaded in thefile areaccepted by NPCl mapper
then in such a case the format of response file generated is provided in Annexure I and XML
formatisprovidedinAnnexureIl.
2. If some of the records in the file are accepted and others are rejected then the format of
response file generated is provided in the Annexure Ill and XML format is provided in
Annexure IV.
3. The status / reject codes and their respective description is provided in the Annexure V.
Member banks are requested to be guided by the circular and make sure to utilize the
response files to update the status in their databases and provide the view facility to their
staff.
Thanking you
Yoursfaithfully,
Giridhar G.M.
(VPandHead-CTS&NACHOperations)
C-9, 8th Floor qT/Phone:02226573150
RBIPremises q/Fax:02226571001
Bandra-Kurla Complex 专-/email:contact@npci.org.in
Bandra East aw/Website:www.npci.org.in
-400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexurel
S.No XML Field
Description
<?xmlversion="1.0"encoding="UTF-8"standalone="no"?>
<Result>
FileACH-CM-KUNS-KUNSMaker-13022015-000005-MAP.txtis Success
SuccessfullyUploaded
message
</Result>
*Note:This filewill be created if and onlyif all Aadhaarnumbers are
accepted.
Annexure ll
<?xmlversion="1.0"encoding="UTF-8"?>
<Result>FileACH-CM-KUNS-KUNSMaker-13022015-000005-MAP.txtisSuccessfully
Uploaded</Result>
Note:Samplefileenclosed asannexureA

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureII
S.N
XML Field Description
<?xmlversion="1.0"encoding="UTF-8"?>
<Result>
<Record>
<AADHAAR_NO>328283420871</AADHAAR_NO> AadhaarnogiveninMapperfile
<MAPPED_IIN>508680</MAPPED_IIN> liNofuploadedBank
<SCHEME>EBT</SCHEME>
BydefaultitisEBT
<MANDATE_CUST DATE>2015-01-
O2</MANDATE_CUST_DATE> MandatedateinMapperfile
<MAPPINGSTATUS>A</MAPPINGSTATUS>
Mapping status giveninfile
<UID_RESULT>DuplicateUIDrecord</UID_RESULT> Rejectreason
</Record>
</Result>
*Note:Aadhaar numbers which has been successfutly uploaded will not be mentioned in
this file
AnnexureIV
<?xml.version="1.0"encoding="UTF-8"?>
-<Result>
-<Record>
<AADHAAR_NO>875216224242</AADHAAR_NO>
<MAPPED_IIN>607261</MAPPED_IIN>
<SCHEME>EBT</SCHEME>
<MANDATE_CUST_DATE>2014-12-16</MANDATE_CUST_DATE>
<MAPPING_STATUS>A</MAPPING_STATUS>
<UID_RESULT>DuplicateUIDrecord</UID_RESULT>
</Record>
</Result>
Note:Samplefile enclosed asannexureB

<!-- Page 4 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureV
STATUS
CODE Status Description
Mandate date in the record must be greater than that of the existing
UID
DuplicateUIDrecord
Futuremandatedateisnotaccepted
FreshinsertmustbeActiveonly
AadhaarNumberisnotmappedtoyourliNorScheme
InsertedFortheFirstTime
UpdatedUIDrecord
InvalidAadhaar_No,VerhoeffChecksumvalidationFailed
10 InvalidAadhaar_No,Aadhaarnumberisnotequalto12digits
11 InvalidAadhaar_No,Aadhaarnumbermust notstartwith1
MandateFlagmustbeY
13 MappedtoSomeOtherBank andODalreadyexists
14 OD canbesetYonlywhenmandateflagisY
15 Aadhaar numbercannotbeinactivatedwhenODflagY
16 Future OD date is not accepted
17 OD date in the record must be greater than that of the existing OD date
18 OD date in the record must begreater than or equal to Mandatedate
19 Mandateshould notbepriorto2012January
