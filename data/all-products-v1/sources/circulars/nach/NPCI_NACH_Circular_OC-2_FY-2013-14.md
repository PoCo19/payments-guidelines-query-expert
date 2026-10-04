# Circular No. 2 - Enabling of Aadhaar Lookup Feature for APB -Credit on NACH System

Circular/reference number: OC-2
Date: 15 March, 2013

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCl: 2012-13: NACH: Circular No 2 15 March, 2013
To.
All Member Banks of Aadhaar Payments Bridge - Credit (APB-Credit) on National Automaled
Clearing House (NACH) System
Enabling of AADHAARLookup Featurefor APB-Credit on NACHI system
Respected Madam / Sir,
We are pleased to inform you that a new facility called AADHAAR Lookup' has been introduced in
the NACH systemforthebenefitof the banks.
2. This facility would allow the banks to know the status of AADHAAR mapping in the NACH
System and can be used for verification of a list of AADHAAR numbers through an upload process
and response thereof.. This would help the banks to process Direct Benefits Transfer (DBT)
transactions more efficiently and help reduce returns.
The AADHAAR Lookup Process Document is attached at Annexure A.
4. This facility would be available for banks from 1.30 PM up to 5.00 PM on daily basis from
5. For any queries/further help required, please feel free to email at ach@npci.org.in. Kindly
acknowledge the receipt of the circular.
We look forward for your continued support to make APB-Credit a great success.
With warm regards,
uleek
M.Balakrishnan
Chief Operating Officer
C-9,8thFloor pT/Phone:02226573150
RBIPremises G/Fax:02226571001
Bandra-KurlaComplex 专/email:contact@npci.org.in
Bandra East aews/Website:www.npci.org.in
-400051 Mumbai400051

<!-- Page 2 -->

NATIONAL AUTOMATEDCLEARINGHOUSE
AadhaarLookup Feature Process Document
14-March-2013

<!-- Page 3 -->

NPCi
NATIONALPAYMENISCORPORATIONOEINOA Aadhaar LookupFeature
Tableof Contents
1. REQUIREMENT
2. SOLUTION
2.1 INPUTFILE
2.2 RESPONSE FILE
3. SAMPLE FILES
Page12

<!-- Page 4 -->

NPCI
LATIONALPAYMENISCOFPORAIONONOA Aadhaar Lookup Fcature
Requirement
Banks, Government Departments and other stakeholders wanted NPCl to make
available facility should be available to the end user to query the status of a list
ofAadhaarnumbers
Solution
numbers and a response file (RES) will be generated.
Thefile formats of thedifferent files involved are explained indetail below:
2.1 Input file
File Name
UID-ST-<GROUP NAME>-<USER'S LOGIN NAME>-<CURRENT DATE IN DDMMYYYY
FORMAT>-<SEQUENCE>-INP.txt
Example:
UID-ST-SBIN-SBINUser2-29012013-900004-INP.txt
File Format
Sr. Field Field
No Description Length Type Mandatory/Optional Remarks
Aadharnumbertobe
Aadhar checkedforstatusfrom
Number 12 NUM database
12
Page/3

<!-- Page 5 -->

NPCI
NATIONALPAYMENISCORPORATIONOEINOA AadhaarLookup Feature
UID-ST-SBIN-SBINUser2-02022013-500046-INP.tt
995068213680
923605303877
241752451202
921366926758
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
Number 12 NUM statusfromdatabase
Status from Database,will be
Status NUM 0/1/2/3
13
Page 14

<!-- Page 6 -->

NPCI
NATONALPAMENISCORPORATINOEIA Aadhaar Lookup Feature
Status Code Remarks
Aadhar Number is in Status Active
AadharNumberisinStatusInactive
AadharNumberisNotPresentin
Database
Not aValid AadharNumber
digits.
UID-ST-SBIN-SBINUser2-02022013.500046-RES.t
99506821368010
92360530387710
24175245120210
92136692875810
53945225089911
38214274674011
39317204970511
77512737632012
35218758721112
10 38978985212012
11 85637478626312
12 98439832993983213
13 12342343 1213
Page15

<!-- Page 7 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFDA Aadhaar Lookup Fcature
3. SampleFiles
A sample input and response file have been enclosed below for your reference.
UID-ST-SBIN-SBINUser2-02022013-500046-INP.txt
UID-ST-SBIN-SBINUser2-02022013-500046-RES.txt
Page16
