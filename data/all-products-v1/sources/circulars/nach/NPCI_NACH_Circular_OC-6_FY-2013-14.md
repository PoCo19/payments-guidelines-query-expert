# Circular No. 6 - Use of Aadhaar Lookup by Member Banks

Circular/reference number: OC-6
Date: 14th May, 2013

<!-- Page 1 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCl: 2013-14: NACH: Circular 6 14th May, 2013
To,
All Member Banks of National Automated Clearing House (NACH) System
UseofAadhaarLookupbyMemberBanks
RespectedMadam/Sir,
Based on the daily APB transaction processing, it has been observed that the major
reason for rejection of transaction is because Aadhaarnumbers data is not uploaded
to NPCl Aadhaar Mapper by the member banks.Therefore, in order to reduce the
rejected transactions, it is required that all Aadhaar numbers that are successfully
seeded in the Bank Accounts are to be uploaded on to the NpCl Mapper by the
memberbanks at end ofthedayon dailybasis.
2.NPCl has developed the facility of"Aadhaar Lookup"to enable the member banks
to ascertain the details of Aadhaar numbers available on the NPCl Mapper.Member
banks were informed about the same vide NPCI Circular No. 2 dated 15th March,
2013 (copy enclosed).Banks are requested to arrange the access of "Aadhaar
Lookup" facility to their Lead District Managers (LDM) so that the seeding of Aadhaar
numbers to NpCi Aadhaar Mapper can beensured in up to date manner.
3. In view of the seeding of Aadhaar number with Bank Account in Banks' Core
Banking System and uploading of the same to NACl Aadhaar Mapper, it is requested
that the member banks may consider issuing appropriate guidelines to their
respective LDMs to start using"Aadhaar Lookup"facility of NPCl to ascertain the
details of Aadhaar numbers successfully seeded in Bank Accounts and uploaded on
NPCI mapper.
For any queries/further help required, pleasefeel freeto emailat ach@npci.org.in
Withwarmregards,
Vipin Sureliay
HeadACH& ChequeClearing
C-9,8thFloor pt/Phone:02226573150
RBIPremises /Fax.02226571001
Bandra-Kuria Complex /email:contact@npci.org.in
Bandra East aanse/Website:www.npci.org.in
400051 Mumbai400051

<!-- Page 2 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI:2012-13:NACH: CircularNo 2 15th March, 2013
To.
All Member Banks of Aadhaar Payments Bridge - Credit (APB-Credit) on National Automated
Clearing House (NACH) System
Enabling of AADHAARLookup Feature forAPB-Crcdit on NACH system
Respected Madam / Sir,
We are pleased to inform you that a new facility called 'AADHAAR Lookup' has been introduced in
the NACH system for the benefit of the banks.
2. This facility would allow the banks to know the status of AADHAAR mapping in the NACH
System and can be used for verification of a list of AADHAAR numbers through an upload process
and response thereof.. This would help the banks to process Direct Benefits Transfer (DBT)
transactions more efficiently and help reduce returns.
The AADHAAR Lookup Process Document is attached at Annexurc A.
4. This facility would be available for banks from 1.30 PM up to 5.00 PM on daily basis from
Monday to Friday and 1.00 PM up to 2.30 PM on Saturday.
5. For any queries/further help required, please feel frce to email at ach@npci.org.in. Kindly
acknowledge the receipt of the circular.
6. We look forward for your continued support to make APB-Crcdit a great success.
With warm regards,
M.Balakrishnam
Chief Operating Officer
价9,8 C-9, 8th Floor pT/Phone:02226573150
RBIPremises q/Fax:02226571001
Bandra-Kurla Complex 专/email:contact@npci.org.in
phe Bandra East aqwsc/Website:www.npci.org.in
400051 Mumbai400051

<!-- Page 3 -->

NATIONALAUTOMATED CLEARING HOUSE
Aadhaar Lookup FeatureProcess Document
14-March-2013

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOINOA AadhaarLookupFcature
Tableof Contents
1. REQUIREMENT
SOLUTION
2.1 INPUTFILE
2.2 RESPONSE FILE
3. SAMPLE FILES
Page12

<!-- Page 5 -->

NPCI
NATIONALPAYNENTSCORPORATIONOFBDA Aadhaar Lookup Featurc
Reguirement
Banks, Government Departments and other stakeholders wanted NPCl to make
available facility should be available to the end user to query the status of a list
ofAadhaarnumbers
2. Solution
The end user can upload an input (INP) text file containing a list of Aadhaar
numbers and a response file (REs)will begenerated.
The file formats of the different files involved are explained in detail below:
2.1 Inputfile
File Name
UID-ST-<GROUP NAME>-<USER'S LOGIN NAME>-<CURRENTDATE IN DDMMYYYY
FORMAT>-<SEQUENCE>-INP.tXt
Example:
UID-ST-SBIN-SBINUser2-29012013-900004-INP.txt
File Format
St. Field Field
No Description Length Type Mandatory/Optional Remarks
Aadhar number to be
Aadhar checkedforstatusfrom
Number 12 NUM database
12
Page /3

<!-- Page 6 -->

NPCI
NATENALPAYMENISCORPORATIONOEINOA Aadhaar Lookup Feature
UID-ST-SBIN-SBINUser2-02022013-500046-INPLd
995068213680
923605303877
241752451202
921366928758
539452250899
382142746740
393172049705
775127376320
352187587211
2.2 ResponseFile
File Name
UID-ST-<GROUP NAME>-<USER'S LOGIN NAME>-<CURRENT DATE IN DDMMYYYY
FORMAT>-<SEQUENCE>-RES.tXt
Example:
UID-ST-SBIN-SBINUser2-29012013-900006-RES.txt
File Format
Maximu
Sr. Field Field Mandatory/
No Description Length Type Optional Remarks
Aadhar Aadharnumbertobecheckedfor
Number 12 NUM status from database
Status from Database, will be
Status NUM 0/1/2/3
13
Pagc14

<!-- Page 7 -->

NPCI
NAIIONAL-AMENISCOROORATIONOEDIA AadhaarLookupFeature
Status Code Remarks
Aadhar Numberis in Status Active
AadharNumberisinStatusInactive
AadharNumber isNotPresent in
Database
Nota Valid Aadhar Number
Note: Not a valid Aadhaar Number (Status Code: 3) can indicate either that
aadhaar number is not an integer or that the length of aadhaar number is not 12
digits.
UID-ST-SBIN-SBINUser2-02022013-500046-RES.td
99506821368010
92360530387710
24175245120210
92136692875810
53945225089911
38214279674011
39317204970511
77512737632012
35218758721112
10 38978985212012
11 85637478626312
12 98439832983983213
13 12342343 1213
Page/5

<!-- Page 8 -->

NPCi
NATHONALPATMENISCORPORATIONOENA Aadhaar Lookup Fcaturc
3. SampleFiles
A sample input and response file have been enclosed below for your reference.
UID-ST SBIN-SBINUser2-02022013-500046-INP.txt
UID-ST-SBIN-SBINUser2-02022013-500046-RES.txt
Pagel6
