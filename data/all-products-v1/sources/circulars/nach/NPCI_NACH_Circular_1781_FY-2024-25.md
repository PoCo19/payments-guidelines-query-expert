# NACH | 003 | FY 24-25 | Emandate Authentication through Simplified Aadhaar

Circular/reference number: NPCI/2024-25/NACH/003

<!-- Page 1 -->

NPC
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/2024-25/NACH/003 October 20, 2024
To
All NACH member banks
Emandate Authentication through Simplified Aadhaar
Reference may be taken from Circular No. 9 (NPCI / 2021-22 / NACH / Circular no. 009, dated Feb
10, 2022) regarding Emandate Authentication through Aadhaar based authentication and Circular No.
3 (NPCI / 2023-24 / NACH / 003, dated July 21, 2023) regarding E-mandate simplification and
harmonization of the limit of all variants of mandates.
in addition to Aadhaar based authentication where applicable limit is of Rs. 1.00 crore (Rupees one
crore), we have introduced Simplified Aadhaar with limit of Rs. 15,000 where UiDAl authentication
will not be required and banks shall send OTP to the customer on registered mobile number for
authentication, post successful OTP validation mandate will be registered.
Validation of Aadhaar linkage to the account: It is mandatory for the banks to validate that the
given Aadhaar number in the mandate registration request is linked to account number in which
mandate is registered. Register mandate only if Aadhaar is already linked to the account. This
validation is mandatory for Aadhaar based mandates as well as for Simplified Aadhaar mandate.
Aadhaar based mandate (where mandate value is above 15,000 up to Rs. 1 Cr): It may please
be noted that in case of Aadhaar based mandate the "uidaiAuthenticated" flag value shall be 'Y" the
banks must necessarily validate this value before taking up the mandate request for processing and
registration. if the value is anything other than 'Y' such registration requests shall be rejected by the
bank.
Simplified Aadhaar mandate (where mandate value is up to Rs. 15,o00): For authentication under
Simplified Aadhaar mechanism banks shall follow the existing validations of Aadhaar based
authentication with the only difference of "uidaiAuthenticated" flag value can be N or Y.
NPCl shall depending on the regulatory and other approvals will decide on the following:
1. UIDAl validation requirement for different categories of Aadhaar based mandate
2. Limit of amount for simplified mandate.
Detailed process flow is provided in Annexure I and Technical specifications are provided in the
Annexure-ll. Member banks are advisedto take note and disseminate the information to all concerned
for implementation.
With warm regards,
SD
Giridhar G. M
Chief - Customer Success
1001A, The Capital, B Wing. 1oth Floor,
Bandra Kurla Complex, Bandra (E),Mumbai 4oO O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

Annexure-l
NPCIV
hhu Liph hia pat
NATIONAL PAYMENTS CORPORATION OF INDIA
NPClMandateApproval GatewayService
Bank Specification Document
Version 1.0.

<!-- Page 3 -->

DOCUMENTRELEASENOTICE
Document Details
Name Version No. Date Description
Provides technical & operation specification
Bank Specification Document for Banks to develop compatibte application
First 18-10-2024
for Simplified Aadhaar at their end for communicating with the
Mandate Authorization application

<!-- Page 4 -->

Contents
1.  Introduction
Abbreviation.
2.  Interface specification details for Mandate Approval
Registration with NPCl.
3. Simplified Aadhaar Based Authentication Flow.
4. API sevices.. 16
API to get Transaction Status for Banks. 16

<!-- Page 5 -->

1.Introduction
This document details the requirement for destination banks to develop the required interface for
interacting with the Mandate Authorization gateway service.
The file formats for request & response are covered in this document.
Abbreviation
The below abbreviations are used in the document.
NPCI National Payments Corporation of India
ONMAGS Online MandateApproval Gateway Service
UIDAI Uniqueldentification Authority of India

<!-- Page 6 -->

2.Interface specification details forMandate Approval
Registration with NPCI
The destination banks who want to leverage the service need to be registered with NPCl and get certified.
3.Simplified Aadhaar Based Authentication Flow
CTPinputbyCustomeronONAGS
andete APlrequest
Mardateintiafon MandateAPlRequest Msndate Velidation Respon
NACH
MandeteAPtResp MendsteAPiResponse OTPVerificaticn
CUSTOMER wiathUMRN withURN OTP Verit!
10 CORPORATE Resporse
Mendate Mendgteinserton DESTNATION BANK
Insertion resporse
Inwsrd File Response F
PushUMRN withNPCI PushUhRNith NPCI
RefDforCBS Ref IDforCBS
uogknsuoo consiemgton
SPONSORBANK NPCIMMS DESTNATION BANK
Stepi: Customer has initiated the request via Merchant Portal i.e., Web Browser
Step2: Customer will be redirected to ONMAGS Platform to enter the details reguired for Aadhaar
authentication. Customer enters Aadhaar Number along with required details.
Step 3: ONMAGS will send an API request to customer's Bank to verify the customer details.
Step 4: Bank will validate the mandate request and send to NpCl
Step S: Customer will be landed on ONMAGS OTP page. Banks will generate the OTP and send it to
customer for Authentication.
Step 6: Customer will enter the Bank OTP in ONMAGS platform for Authentication.
Step 7: ONMAGS ptatform will forward that OTP to destination bank for Verification.
Step &: If oTP verification is successful then only the Bank needs to mark the mandate as accepted at their
end. Until oTP validation is passed the mandate would be in non-accepted state at the Bank end.
Step 9: ONMAGS Platform in turn redirects the responseto Merchant Web Page where customer can view
the response.
Step 1o: Response is shared by corporate to customer
Step 11: Mandate will be inserted in MMs System and Inward & Response will be shared with Sponsor
and Destination Bank

<!-- Page 7 -->

Annexure ll
Auth mode: Aadhaar
Privilege: Initiated by ONMAGS (NPCI)
API type: Sync
Request Type: JSON
HTTP Method: POST
Parameter Specification
Parameters Data Type Description
mandateAuthDtls JSON Object This will contain mandate Request details and aadhaar Info
transactionID String This is used for the complete transaction for mandate registration.
ALPNUM String with Length is 20.
This will contain Encrypted mandate Request Doc XML and
mandateReqguestDtl JSON Object
Encrypted checksum value.
MandateReqDoc String See below table for Mandate Request Doc.
CheckSumVal String How to generate Checksum value is mentioned above.
authMode value wil be Aadhaar and user will get aadhaarlnfo JSON
authMode String
Object in request.
This will contain the aadhaar details and flag indicating that the
aadhaarlnfo JSON Object customer authentication has been successful though UiDAl. In case
of simplified mandate this value can be either 'y' or 'N'.
aadhaarNo String Last four digit of aadhaar number
uidaiAuthenticated Char (In case of simplified mandate this value can be either 'y' or 'N')
Mandate Reguest to Bank
"mandateAuthDtls":(
"transactionID": "<Transaction ID>"
attributes>"
"mandateRequestDtl": {-]
"MandateReqDoc": "<Encrypted and Signed request XML>",
"checksumVai"; "<Check sum value of secure attributes>!
"authMode":"Aadhaar"
"aadhaarInfo": {
"aadhaarNo": "<Encrypted Aadhaar Number>"
"uidaiAuthenticated" : "Y or N"
Note-Checksumwill be validated onlyforCreate &Amend flow

<!-- Page 8 -->

Unencrypted and Unsigned request XML for MandateRegDoc Key:
Element Name Validation Data Type Length Remarks
Xmlns Namespace tag. This is mandatory tag. Alpha Numeric
Value cannot be empty. Namespace value
should be
"http://npci.org/ONMAGS/schema"
NPCI_RefMsgld NPCI_RefMsgld from NPCI should be Alpha Numeric 35 Message ID for NPCI
unique Reference
CreDtTm Should be in IsO Date time format. Alpha Numeric
E.g.2017-02-09T15:11:39
ID Request Initiating Party ID. In this case it Alpha Numeric 18 ID & UtilCode value
will be Corporate / Merchant ID. Should wouid be the same.
not be null. Will be validated if this is a
valid Merchant ID with the master.
UtilCode Utility Code would be validated against Alpha Numeric 18 ID & UtilCode value
the masters. It should be 18 digit Utility would be the same.
code.
CatCode identifies under which category the Alpha Numeric
mandate is created, Will be validated
against the masters maintained by NPCl
Name Should not be empty Alpha Numeric 40 Corporate Name.
Spn_Bnk_Nm Corporate Sponsor Bank Name Alpha Numeric 140 Should be a valid Bank
Name as per MMS
CatDesc Category Description should correspond Alpha Numeric 50
to Category Code in the Master
MndtReqild Mandate Req ID length should be <- 35. Alpha Numeric 35
Should be unique for the day
Mndtid This tag will contain the UMRN generated Alpha Numeric 20 UMRN
in MMS for the mandate.
Mndt_Type Mandate Type Alpha 35 Should be DEBIT
Schm_Nm Scheme Name/ Plan Reference Number Alpha Numeric 20
SeqTp Allowed values are RCUR or OOFF Alpha Numeric
Frqcy This is an optional field. If present should Alpha Numeric Allowed Values are:
adhere to the list value available in MMS ADHO, INDA, DAIL,
Masters. WEEK, MNTH, QURT,
MIAN, YEAR, BIMN
FrstColltnDt Date of First Collection. Mandatory Field. Alpha Numeric 16
This field is in ISODate Format
FnlColltnDt Date of Final Collection, Optional Field. Aipha Numeric 16 If this field is left
This field is in ISODate Format blank then deduction
will happen until
Cancelled.
ColltnAmt Either of CoiltnAmt or MaxAmt is Alpha Numeric 13
mandatory.
Amount Should be given as 100.00

<!-- Page 9 -->

MaxAmt Either of ColltnAmt or MaxAmt is Alpha Numeric 13
mandatory
Amount Should be given as 100.00
Debtor Nm Customer name should be maximum of Alpha Numeric 40
35 digit
De btor AccNo Customer Account Number should be Alpha Numeric 35
maximum of 35 digit.
Acct_Type Debtor Account Type Alpha 35 Should be either of
SAVINGS or CURRENT
Cons_Ref_No Consumer Reference Number Alpha Numeric 20
Phone Phone Number of the Customer Alpha Numeric 34 Should be given in the
format +9 1-xxx-
xxxxxxxx. +91- is
mandatory.
Mobile Mobile Number of the Customer Alpha Numeric 34 Should be given in the
format +91-
xxxxxxxxxx. +91- is
mandatory.
Email Email ID of the Customer Alpha Numeric 50 Should be valid email
p!
Pan Pan Number of the Customer Alpha Numeric 27 Should be in Valid PAN
format
Creditor Nm Corporate Name. Length will be 40 Alpha Numeric 140
Creditor AccNo Will be the 18 digit Corporate ID Alpha Numeric
Mmbld Will be 11 digit iFSC code Alpha Numeric 11 IFSC Code of the
Sponsor Bank which is
available in the
ONMAG Live Bank list
Mndtld Will be 20 digit UMRN Alpha Numeric Except Create Flow
ReasonCode will be 4 digit Reason code Alpha Numeric Except Create Flow
Bank needs to first verify the mandate request details
a) If the destination bank is unable to parse the mandate request it will send the response in the
below format. Bank need not validate the aadhaar details if sending failure response (because of
request XML validation failure at bank end).
Parameters Datatypes Description
mandateVerifyDtls JSON Object Mandate verify details contains transaction ID, mandate Validation and
mandate reject details
transactioniD String This is the same transaction ID which Is passed in request for mandate
registration. ALPNUM String with Length is 20.

<!-- Page 10 -->

mndtType String This will contain the operation AMEND /CANCEL/SUSPEND/REVOKE
/CUSTOM_ CANCEL. mndtType will not be present for Create Flow.
mandateValidation String This will return either success or faifure.
aadhaarValidation String This will return either success or failure.
mandateRejectDtl JSON Object This will contain error code and error desc
ErrorCode Integer This will be between 000 to 999
ErrorDesc String This will be the corresponding error description for the error code.
signature String The Response payload will be signed with bank's private key and
algorithm used as RSA_ USING_SHA256
checkSumVal String Generate checksum on the entire payload. We will use SHA-2 as the hash
function
Error Response from Bank for Mandate request:
"mandateVerifyDtls"; (日
transactionID": "<Transaction ID>",
attributes>"
"mandateValidation": "failure"
"aadhaarValidation": "none",
"mandateRejectDtl":{
"ErrorCode": "<Error Code>"
"ErrorDesc": "<Error Description>"
"signature"; "<Encrypted and signed response JsoN>",
"checksumVal": "<check sum value of complete payload>"
Note:- Attribute values Mandate Validation, Aadhaar Validation, Error Code & ErrorDesc needs to be
encrypted. Bank needs to encrypt using NPCl public key.
b) if destination bank is able to successfully parse the mandate reguest XMl but business validation
of XML fails, then bank needs to send the response in the below format. Aadhaar details need not
be validated in such a scenario.
nmandateVerifyDtls":1
"transactionID": n<Transaction ID>"
attributes>"
"mandateValidation":"faiiure",
naadhaarValidation":"none"

<!-- Page 11 -->

"mandateRejectDtl":1
"ReasonCode" : "<Reason Code>"
"ReasonDesc": "<Reason Description>"
"signature": "<EncrYpted and Signed response JsON>",
"checkSunVal": "<Check sum value of complete payload>"
Note:-_Attribute values Mandate Validation, Aadhaar Validation, Reason Code, Reason Desc &
checkSumVal needs to be encrypted
c) Aadhaar Validation
1. Aadhaar number of debtor should matches with the"Aadhaarlinked with the Debtor AccNo"
provided in the mandate Request XML
2. Aadhaar number shouid be linked with the debtor Account Number.
If the above vaidation fails, then the bank needs to provide the response as above format 2 nd type.
"mandateVerifyDtls":{
"transactionID: "<Transaction ID>"
attributes>",
"mandateValidation": "success",
"aadhaarValidation":"failure"
"mandateResponseDtl": {日
"accptRefNo": "<Accept Reference Number>"
"dbtrIfse": "<Debtor IFsC>"
aadhaarRejectDtl ": {日
*ReasonCode": "<Reason Code>t
"signature": "<Encrypted and Signed response JsON>"
"checksumVal": "<Check sum value of complete payload>"
The below table provides the error codes for different failure reasons.
Failure Reason Reason Code
Aadhaar number Does not Match with debtor Account number AP48
Aadhaar Number not iinked with the Debtor Account 1 Number AP51
d) If all the abovevalidation passes then the bank needs to provide the success response as below:-

<!-- Page 12 -->

Success Response for Mandate reguest to Bank:
"mandateVerityDtls"{E
"transactionID": <Transaction ID>"
"mndtTYpe":"<CREATE / AMEND /CANCEL / SUSPEND/ REVOKE /CUSTOM_CANCEL
attributes>"
"mandateValidation": "success"
aadhaarValidation": success"
"mandateResponseDtl":[E
"accptRefNo": "<Accept Reference Number>"
"dbtrifsc": "<Debtor IFsc>"
"dbtrAcctType": "<Debtor Account Type>n
"aadhaarVerifyDtl":[B
"signature": "<Encrypted and signed response JsoN>",
"checksumVal": "<check sum value of complete payload>"
The below table provides the code forthe success
successReason SuccessCode
Aadhaar number matches with Aadhaar linked 000
with debtor account number Validation Passed
Note:-
i. Attribute values mandateValidation, aadhaarValidation, AccptRefNo , successCode &b
checkSumVal needs to be encrypted.
Bank needs to store the mandate details received along with the transaction ID for the
subsequent OTP validation.
For scenarios (a), (b) and (c) ONMAGS will construct the merchant rejection response and redirect to the
merchant. Bank needs to mark the mandate as rejected at their end for these scenarios. For scenario (d)
if bank has opted for OTP validation then mandate status will be "In Process" for the bank until the OTP
verification is completed, eise mandate status will be "Accept" and send the response back to ONMAGs.
For scenario (d) ONMAGS will redirect to the OTP verification page.
Below are the steps to be done for securing the content of the Response JsON:
1. Generating checksum for the secure information in the Response JSON (Mandate and Aadhaar
validation).
The below attributes need to be concatenated for the purpose of generating Checksum:
A. Transaction ID
B. Mandate Validation
C. Accepted Ref No.

<!-- Page 13 -->

Dbtr Account type
E. Dbtr IFSC
F. Reason Code
G. Reason Desc
H. Error Code
Error Desc
J. Aadhaar Validation
K. Success Code
L. Aadhaar Reason Code
M. Aadhaar Error Code
N. JSON Web Signature
2. Generating checksum for the secure information in the Response JSON (OTp Validation).
The below attributes need to be concatenated for the purpose of generating Checksum:
A. Transaction ID
B. Verify Status
C. I Error Code
D. F Reason Code
E. JSON Web Signature
The above attributes need to be concatenated with “j" symbol appended as the delimiter. The order of
the attributes needs to be as mentioned above.
Note: The attributes to be concatenated might be changed at a later point of time. Please refer the latest
version of the document for any revision onthe attributes that needs to be marked for Generate checksum
on the concatenated values. We will use SHA-2 as the hash function.
3. Signing of the Response JSON.
The complete response we are going to use as a payload.
The response JsON has to be signed using the Private Key certificate of the Bank.
Json Web Signature is used for generating digital signatures and the same will be validated at the
NPCI end.
Note :
Except transaction ID, Dbtr Account Type and Dbtr IFSC field, all the fields are encrypted. For
generating checksum, we are going to use encrypted values. If value is not present in response,
then we will use empty string for that key.
Since we are using Signature value while generating Checksum, so that first we need to sign the
response then generate checksum.

<!-- Page 14 -->

Bank OTp Verification Reguest for Same Mandate request:-
Parameters DataTypes Description
This will contains the transaction Id same used in OTP generation and
otplnfo JSON Object
Encrypted OTP which is received on registered mobile in bank
Same transaction ID used in mandate request to bank. ALPNUM String
transactioniD String
with Length is 20.
otp String Encrypted OTP received on registered mobile in the bank. Length is 4.
"otpInfo":[E
"transactionID":"<Transaction ID>"
"otp": "<Encrypted OTP Value>"
• In case of retry request also, the request will be posted to bank in the above mentioned format only.
The encryption on the OTP will follow the existing encryption methodology. Bank needs to decrypt the
OTP and verify it based on the transaction ID. The OTP verification status needs to be sent in the below
json format by the bank.
Response From Bank for Bank OTP Verification forthe same Mandate request:
Parameters DataTypes Deseription
otpVerifylnfo JSON Object This will contain the same transaction Id which is sent in mandate
request to bank and encrypted status as success or failure.
transactioniD String Transaction Id is the same Which is sent in verify request bank OTP.
ALPNUM String with Length is 20.
optVerifyStatus String Encrypted OTP verification status. It will be either success / failure
a) If OTP verification at bank end is success then the response will be as below:
"otpVerifyInfo":
"transactionID": "<Transaction ID>",
"optVerifystatus": "success",
"errorCode" : w",
"reasonCode": w"
"checkSumVal": "<Check sum value of complete payload>"

<!-- Page 15 -->

b) if OtP verification failed at bank end, then response will be as below:
"otpVerifystatus": {
"transactionID" : "<Transaction ID>"
"optVerifystatus":"failure"
"errorCode";",
"reasonCode" : <Reason Code>
"signature":"<Encrypted and signed response JsoN>"
"checksumVal" : "<Check sum value of complete payload"
Failure Reason Reason Code
Invalid Bank OTp AP39
Maximum tries exceeded for OTp AP40
Time expired for OTP AP41
AP50
If OTP verification is successful only Bank needs to mark the mandate as accepted at their end. Until OTP
validation is passed the mandate would be in non-accepted state at the Bank end.
If OTP validation is failure User would be provided with option of reattempting OTP validation further 2
times. An alert message as below will be shown to the user. User can then proceed with entering the
correct OTP again and re-verify.
Reguest for Resend Bank OTP:
Parameters Datatypes Description
mandateAuthDtis JSON Object This will contains transaction Id same which is sent in the first
generate bank OTP request and encrypted aadhaar number
transactionID String transaction Id same which is sent in the mandate request to bank.
ALPNUM String with Length is 20.
aadhaarinfo JSON Object This will contains Encrypted aadhaar number
aadhaarNo String. Encrypted aadhaar number only last four digit.
JSON Request:
"aadhaarAuthDtls": {
"transactionID": "<Transaction ID>"
aadhaarInfo": (E
"aadhaarNo": "< Encrypted Aadhaar Number>#

<!-- Page 16 -->

Response for Resend Request will be '20o' status code.
If OTP verification is successful only Bank needs to register the mandate as accepted at their end.
+ In case OTP verification fails in all the attempts bank can mark the mandate as rejected at their end.
Bank will not generate any OTP, skip the OTPverification step and need to mark the mandate as accepted
at their end.
Technical Integration requirement for Aadhaar Authentication
1. Connectivity:
Communication between NPCI to Bank Server with specific port
2. Certificates
Bank SSL certificate(FQDNS)
Bank Signing certificate
One way API handshake
3. Keys exchange for UIDAI Authentication.
Bank should share their AUA Keys
Bank has to share the keys as part of onboarding process, else we will use NPCI AUA Key
4.APIservices
API to get Transaction Status for Banks
For the purpose of getting the transaction status of a particular transaction or group of transactions for
Banks, NPCI ONMAGS would expose a rest service which will accept list of NPCI Transaction Reference
Numbers in JSON format. The responseof this API will also be in JSON Format. There will be a limitation
on the number of items posted per request. Currently the limit is set as 50.
Sample Input JSON:
"npcirefmsglD":[
"000f0f29dc27f00000101b09c5227457f17
"000f0f29dc27f00000101b09c5227457E23
"000f0f29dc27f00000101b09c5227453S42"

<!-- Page 17 -->

Sample Output JSON:
" tranStatus ":[
ri
"npcirefmsglD":"000f0f29dc27f00000101b09c5227457f17"
"Accptd":"false",
"AccptRefNo":"tranid3432kkkeke"
"Mndtld":"xxxxxxxxxxxxxxxxxxxx"
"ReasonCode":"343",
"ReasonDesc":"Invalid Account"
"RejectBy":"Bank",
"ErrorCode":"ooo"”
"ErrorDesc":"NA"
1,
"npcirefmsglD*" :"000f0f29dc27f00000101b09c5227457E23"
"Accptd":"true",
"AccptRefNo":"tranid352254221"
1Mndtld":"xxxxxxxxxxxxxxxxxxxx",
"ReasonCode":"O0o"
"ReasonDesc":"NA",
"RejectBy":"NA",
"ErrorCode":"o0o"
"ErrorDesc":"NA"

<!-- Page 18 -->

"npcirefmsglD":"000f0f29dc27f00000101b09c5227453S42",
"Accptd":"NULL",
"AccptRefNo":"NULL",
"Mndtld"."NULL"
"ReasonCode'":"NULL"
"ReasonDesc":"NULL"
"RejectBy"."NULL"
"ErrorCode":"452",
"ErrorDesc":"No Details available for the requested parameters. Please check the values provided"
In case the details provided in the request are invalid then ErrorCde & ErrorDesc will have the
corresponding error code & description. Forthe valid request ErrorCode would be "ooo" and "ErrorDesc"
Would be "NA". APl URL would be of the below format:
https://enach.npci.org.in/apiservices/getTransStatusForBanks
UAT:
https://103.14.161.144/8086/apiservices/getTransStatusForBanks
