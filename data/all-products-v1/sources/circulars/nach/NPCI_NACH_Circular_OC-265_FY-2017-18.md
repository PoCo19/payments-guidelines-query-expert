# Circular No.265 - “Mapper file format with field for capturing previous seeded bank IIN”

Circular/reference number: NPCI/2017-18/NACH/CircularNo.265

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2017-18/NACH/CircularNo.265 December26,2017
To
AllNACHMemberBanks
Mapper fileformat with field for capturing previous seeded bank llN
Dear Sir/Madam,
UIDAl vide their gazette notification No.13012/79/2017/Legal-UIDAl (No.6 of 2017)
datedDecember19,2017hasmandatedafewchangesinAadhaarmapper.Incompliance
with the directions of Government of India the following changes will be made to NPCl
mapper.
1. Override request pertaining to an Aadhaar holder only if it is accompanied by the
lIN of his current bank on the APB mapper and confirmation from the requesting
bank that it has obtained the requisite consent of the Aadhaar holder for switching
to the requesting bank on the mapper.
2. Stopping the move in / move out functionality on a temporary basis till the point
no 1 is implemented. This has been implemented with effect from December 21,
that fresh insert of Aadhaar numbers will be allowed as per the existing process.
NPCl is working on the modifications to the mapper format to accept the IIN of the current
will happenin different scenariosisprovided inAnnexure ll.
The following are the activities to be carried out by the banks.
1. Carry out changes in internal systems and core banking for new mapper file upload and
handling theadditional rejectreasons.
2. Implementation of the new consent format (IBA is finalizing the format, this will be
communicated to banks separately).
Important:
Mapper format:
1. Mapper continue to accept fresh inserts without the llN of the existing banks, this
field can be left blank as per the specifications.
2. Banks should obtain the existing bank name from the customer, obtaining the
existing bank information by any other means will be construed as non-compliance
to the directions of Government of India.
1001A, The Capital, B Wing,10th Floor, Bandra Kurla Complex, Bandra (E),Mumbai 400 051. T: +9122 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Consent form:
1. Consent of the customer should be obtained as per the approved format this is
applicable both for electronic as well as physical consent of the customer.
2.Banks should comply with all the directions as per the gazette sighted above (copy
enclosed)
3. Any violation of these directions shall amount to violation of Sections 37, 40, 41,
42, and 43 of the Aadhaar Act, 2016 and Regulations framed thereunder and other
applicable laws of India.
We are planning to move the new mapper file format to production on January 01, 2018.
All the banks should take immediate steps to implement all the necessary changes for
Withwarm Regards,
GiridharGM
SVP-NACH&CTSOperations

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Detail Record
Sr.No. Field Name Length Max Field Type Status FieldDescription Sample Data
1. Detail recordidentifier 2NUM Thedetailrecordidentifier 34-Constantvalue
2. Record ReferenceNumber 15|ALP / NUM Unique Numberto identify the record to be 12345
givenbybank
3. AadhaarNumber 15NUM Aadhaar number of the beneficiary,left 623456789012
padded withzero
6 digit liN of the bank which holds the
4. MappedlIN 9NUM accountforthebeneficiary,leftpaddedwith560112
zeroes
The Mandate flag can only be"Y.Mapper
Mandate Flag 1ALP data withany othervalue will be rejected byy
thesystem
This field wouldbeupdated by the
6. Dateof customermandate 8DATE participant bank user basedon date 10102015
mentioned in the mandate provided by
customer
Determines status of existing UID & lIN
mapping in mapper system i.e. active or
inactive.
Value will be one space in case of new
Mapping Status ALP mapping creation or updating to existing
mapping.Value will be"p"if existing UiD &
IIN mapping is to be deactivated.If Mapping
Status is not provided then it is considered
as space.
OD Flag 1ALP The OD flag can onlybeY'or'N'.
OD Date 8DATE M/0 OD Date is mandatorywhen theOD Flag is 10112015
i.Incase ofRe-Seeding/Mapping,thisfieldis
mandatory and it should carry the value of
previous Bank lIN
10. Previous Bank lIN 9|NUM ii. For fresh insert, this field should be either 670248
blankormapped lIN
ili. For inactivation/ activation of Aadhaar,
this field should be either blank or mapped
IIN
11. Reserved Field 291|ALP/NUM|O ReservedField
Total 360

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-1
Header Record:
Sr.No. Field Name Length Max FieldType Status FieldDescription Sample Data
1. Headeridentifier NUM Headeridentifierforthemapperfile 31-Constantvalue
6 digit liN of the bank uploading the file and
2. UploadingBanklIN ALP left padded with zeroes oriFsC code ofthe 555555
uploadingbank
3. UserName 30 ALP/NUM Name of the person who has prepared the Example-Srinivas
fileandrightpaddedwithspaces Rao
4. Date of Input DATE Date of preparation of thefileinDDMMYYYY 26122011
format
File number generated by originating bank
5. Inputfilenumber NUM for control purpose and should be unique for
a day at a bank. The field would be left
padded with zeroes.
6. Total numberofrecords NUM Total number of records to be captured by
originatingbank, leftpadded withzeroes.
Filler 301 ALP/ NUM Filler Spaces
Total 360

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure - 2
Scenario
SI.No Scenario Mandate flag ODflag IIN field Expectedresult
Fresh Insert Blank Insert reject
FreshInsert lIN of samebank Insert reject
FreshInsert lINofdifferentbank Insert reject
FreshInsert Blank Insert successful
Fresh Insert lIN of samebank Insert successful
FreshInsert lIN of different bank Insert reject
FreshInsert Blank Insert successful
Fresh Insert lIN of same bank Insertsuccessful
FreshInsert lIN of different bank Insertreject
10 Fresh Insert Blank Insertreject
11 Fresh Insert lIN of samebank Insertreject
12 FreshInsert IINof differentbank Insertreject
13 Move in/ out Blank Insertreject
14 Move in/ out lINof samebank Insertreject
15 Move in/ out lIN of previous bank Insert reject
16 Move in/ out Blank Insert reject
17 Move in/ out lIN of same bank Insert reject
18 Move in/ out lIN of previous bank Insert successful if OD of earlier bank is"N"
19 Move in/ out IIN of previous bank Insert reject if OD of earlierbank is"Y"
20 Move in/ out Blank Insertreject
21 Move in/ out lINof samebank Insertreject
Movein/ liN of previous bank Insert successful if OD of earlier bank is"N"
23 Move in/ out lIN of previous bank Insert reject if OD of earlierbank is"y"
