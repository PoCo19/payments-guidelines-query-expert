# Circular No. 154 - Changes in UID response file for New Mapper format

Circular/reference number: NPCI/2016-17/NACH/Circular

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2016-17/NACH/Circular No. 154
April 05, 2016
To
All NACH Member banks
Changes inUiDresponse file for NewMapper format
Madam / Dear Sir,
are introducing an additional xml tag to provide reject reason code in the existing UiD
code will be added as an additional field. List of status codes and description as per ACH
system is provided in Annexure l.
The new xml tag will be placed before the reject description field, the start and end tag of
the reject reason code is as given below
<UID_REASON_CODE>XX</UID_REASON_CODE>
Example:
<MAPPING_STATUS>A</MAPPING STATUS>
<UID_REASON_CODE>2</UID_REASON_CODE>
<UID_RESULT>Future mandate date is not accepted</UID_RESULT></Record></Result>
All member banks are requested to take note of the same and make necessary changes
wherever required. New UiD response file will be made live with effect from May 15, 2016.
Withwarm regards,
(Giridhar G M)
VP & Head - NACH & CTS Operations

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure!
StatusCode Description
Mandate date in the record must be greater than that of the existing UID
DuplicateUIDrecord
Future mandate date is not accepted
Fresh insert must be Active only
Aadhaar Number is not mappedto your liN or Scheme
InsertedFor the First Time
UpdatedUID record
11 Invalid Aadhaar No, Aadhaar number must not start with 1
Invalid Aadhaar No,Verhoeff Checksumvalidation Failed
10 Invalid Aadhaar _No, Aadhaar number is not equal to 12 digits
11 Invalid Aadhaar_No,Aadhaar number must not start with 1
12 Mandate Flag mustbeY
13 MappedtoSomeOtherBankandODalreadyexists
14 OD can be set Y only when mandate flag isY
15 Aadhaar number cannot be inactivated when OD flagY
16 Future ODdate is notaccepted
17 OD date in the record must be greater than that of the existing OD date
18 OD date in the record must be greater than or equal to Mandate date
19 Mandate should not be prior to 2012 January
Mandate date in the record must be greater than or equal to that of the
20
existing UID
