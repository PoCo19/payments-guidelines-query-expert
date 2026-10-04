# Circular No.002 - Proper Consumption of Mapper Acknowledgement at Bank end

Circular/reference number: NPCI/2018-19/NACH/Circular

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2018-19/NACH/Circular no.002 June 22, 2018
To,
All NACH memberbanks
Proper consumption of mapper acknowledgement at bank end
Refer to our Circular No.265dated December 26, 2017on“Mapper file format with field for
capturing previous seeded bank llN", a mapper response file is generated with one of the
following flags
a) Success
b) Failure
The response is provided at record level.
It is necessary for the banks to take the following action on receipt of the response file
a) Success: In-case of success response the flag in CBs has to be updated as seeded in
NPCl mapper. The banks may also provide the date of seeding.
b) Failure: In case of rejected records the bank should assess the reason for rejection
and take corrective action, wherever applicable, and re-upload the files. If
correction is not possible then bank should update CBs with rejection reason.
Provision should be made in CBs to make this data available to the front office officials
so that they can resolve the customer queries, also banks should send SMs to customers
for both success and failure seeding.
The list of scenario where negative response will be generated is provided in Annexure I.
Member banks should ensure to consume mapper responses as and when received and follow
the process as detailed above.
For any clarifications please write back to us ach@npci.org.in.
With(Warm Regards
(Giridhar. G.M)
SVP - NACH & CTS Operations
1001A,The Capitat,BWing,10th Floor,Bandra Kurta Compiex,Bandra (E),Mumbai 400051.T:+912240009100F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexurel
Reject
Codes Reject Reasons
Mandate date in the record must be greater than that of the existing UiD
Duplicate UID record
Future mandate date is not accepted
Fresh insert must be Active only
Aadhaar Number is not mapped to your lIN or Scheme
Inserted For the First Time
Updated UID record
Invalid Aadhaar No, Verhoeff Checksum validation Failed
10 Invalid Aadhaar_No, Aadhaar number is not equal to 12 digits
11 Invalid Aadhaar No, Aadhaar number must not start with 1
12 Mandate Flag must be Y
13 Mapped to Some Other Bank and OD already exists
14 OD can be set Y only when mandate flag is Y
15 Aadhaar number cannot be inactivated when OD flag Y
16 Future OD date is not accepted
17 OD date in the record must be greater than that of the existing OD date
18 OD date in the record must be greater than or equal to Mandate date
19 Mandate should not be prior to 2012 January
21 Aadhaar number updated as banks merged
22 Mandate flag and Mandate date is mandatory for fresh insert
23 Mandate flag and Mandate date is mandatory
Mandate date in the record must be greater than or equal to that of the
20
existing UID
24 Reseeding is not allowed for your Bank
27 Previous Bank lIN is NOT matching with Current Mapped IIN of Aadhaar
26 Previous Bank lIN is Mandatory in case of Re-Seeding the Aadhaar
Previous Bank liN should be Empty or should be same as Mapped IIN for
25
Fresh Insert
28 Same record in multiple times in same file
99 Technical issue. Kindly re upload the Aadhaar Number.
29 Org Id not available in DB
30 Fresh Insert is NOT allowed for your Bank
1001A,The Capital,BWing.10thFloor,Bandra Kurla Compiex,Bandra(E),Mumbai 400051.T:+912240009100F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067
