# Circular No.27 API service - Aadhar number linkage to account number - Changes in data and validation process

Circular/reference number: NPCI/2018-19/NACH/CircularNo.027

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2018-19/NACH/CircularNo.027 October04,2018
To
AlltheNACHmemberbanks
APl service-Aadhaar number linkage to account number-Changes in data and validation
process
RefertoourCircularno.260datedNovember23,2017on“lntroductionofnewAPlservices.It
has been decided to restrict the Aadhaar numbers provided as part of APl service“Aadhaar
linkage to the account" to only last four digits of Aadhaar prefixing with digit “o",If value other
than "o" is captured in the first 8 characters of the Aadhaar field then NPCl will reject such
request with appropriate reason.
There will be no change in the APl message structure and format i.e. request and response.
Sender to provide the last 4 digit of Aadhaar prefixing 8 characters as "o" and receiver to verify
the linking status in Core banking based on the last four digit of Aadhaar and account number
combination and provide the response.
Details of the fields is given below:
1. Field name: Aadhaar
2.Value will be in plain text format
3. Length -12 digits
Field level validations:
1.First8charactersofAadhaartobecapturedas“o
Incase of any clarification required the same may beraised in CRM tracker inNACH.(Path:NACH
With warm regards,
(Giridhar G M)
SVP- NACH & CTS Operations
1001A,TheCapital,BWing,10thFloor,Bandra Kurla Complex,Bandra (E),Mumbai 4C0051.T:+912240009100F:+912240009101www.npci.org.in
CIN：U74990MH2008NPL189067
