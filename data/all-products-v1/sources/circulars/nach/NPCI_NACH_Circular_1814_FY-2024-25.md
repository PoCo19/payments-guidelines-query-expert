# NACH | 007 | FY 24-25 | Introduction of the Get Account Details API in Bharath Aadhaar Seeding Enabler (BASE)

Circular/reference number: NPCI/2024-25/NACH/007

<!-- Page 1 -->

                                                                                              
 
NPCI/2024-25/NACH/007                                                                                                             December 19, 2024 
 
To, 
 
All NACH Member Banks, 
 
Introduction of the Get Account Details API in Bharath Aadhaar Seeding Enabler (BASE) 
 
Reference may be taken from NPCI Circular NPCI/2022-23/NACH/Circular No. 003 dated July 11, 2022, on Bharath 
Aadhaar Seeding Enabler (BASE) & NPCI/2023-24/NACH/Circular No. 009 dated October 09, 2023, on Bharath 
Aadhaar Seeding Enabler (BASE) with Full KYC. As part of the continued efforts to enhance customer experience 
and drive digitization, we are introducing an upgraded process flow for the Get Account Details API under the 
Bharat Aadhaar Seeding Enabler (BASE) application. 
Get Account Details API: This API request will be initiated by BASE application to destination bank. With this 
service, customer can know whether his/her Aadhaar number is linked with the account number in their bank CBS 
and if it is linked, whether subsidy is enabled for that account from banks response along with other account details 
Functional Process Flow: 
• 
The customer will enter their Aadhaar number as an input to verify their account details under the 
"get account number" API option, which is available on the BASE web page.  
• 
The customer must agree to the consent terms and complete the Captcha verification. 
• 
Upon submitting the request, BASE will send the Aadhaar number to UIDAI for OTP validation. 
• 
UIDAI will generate and send an OTP (One-Time Password) to the customer’s registered mobile 
number. 
• 
The customer will enter the received OTP on the BASE platform. 
• 
BASE will send the entered OTP to UIDAI for verification. UIDAI will validate the OTP and respond 
to BASE. 
• 
Upon successful OTP verification, BASE will use the NPCI mapper to find the bank linked to the 
provided Aadhaar number. 
• 
BASE will perform necessary internal validations to ensure all criteria are met. 
• 
Once validations are successful, BASE will send a request to the identified destination bank. 
• 
The bank will provide the necessary account details back to BASE. 
o 
Aadhaar number last four digits (e.g. XXXX-XXXX-1234) 
o 
Account Number (e.g. XXXX-XXXX-1234) 
o 
Customer account type 
o 
Customer name as per bank CBS in masked format (e.g. RXJXSXEXKXRXK) 
• 
Upon successful retrieval of account information, BASE will display the following details to the 
customer 
o 
Scenario 1: Aadhaar not in NPCI mapper. 
▪ 
The given Aadhaar number XXXX-XXXX-1234 is not seeded in NPCI mapper.  
You may proceed with seeding request.

<!-- Page 2 -->

                                                                                              
 
o 
Scenario 2:  Adhaar is not enabled for receiving DBT at the bank or other reason 
▪ 
The given Aadhaar number XXXX-XXXX-1234 is not linked to an account as per 
the reject reason provided below by the bank:” 
o 
Scenario 3:  
▪ 
“The following are the details of account linked with the given Aadhaar number 
XXXX-XXXX-1234 linked for receiving subsidy” 
• 
Account Number (e.g. XXXX-XXXX-1234) 
• 
Customer account type 
• 
Customer name as per bank CBS in masked format (e.g. RXJXSXEXKXRXK) 
• 
Bank name Aadhaar linked with NPCI 
• 
Account status:  “actual status provided by the bank” 
 
Detailed technical specifications for Get Account Details API are provided in Annexure I. All the Member Banks are 
advised to take necessary steps for implementation on priority.   The information herein may please be 
disseminated to all the concerned for necessary action. 
 
With warm regards, 
 
SD 
 
Giridhar G.M. 
Chief – Customer Success

<!-- Page 3 -->

 
• 
 
 
 
BASE-GET BANK ACCOUNT 
DETAILS(TSD) 
1.1

<!-- Page 4 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 1 of 14 
 
 
 
 
Document Revision History 
 
Change 
No. 
Revision 
Description 
Revision 
/ Version 
Number 
Date 
of 
Change  
Change By  
Reviewed By 
Approved By 
I 
Initial 
Document 
1.0 
18-12-24 
Ramya R  
Sankara 
Subramanian 
Sampath 
Rangasamy 
II 
Changes 
to 
ACK message 
1.1 
19-12-24 
Ramya R  
Sankara 
Subramanian 
Sampath 
Rangasamy

<!-- Page 5 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 2 of 14 
 
 
Contents 
Glossary .................................................................................................................................................................. 3 
1 Introduction ....................................................................................................................................................... 4 
2 Overview of the existing process ......................................................................................................................... 4 
3 Proposed process flow ......................................................................................................................................... 4 
4 Functional flow of Get Bank Account Details API ................................................................................................. 4 
5 Bank validations .................................................................................................................................................. 4 
6 Signing and Encryption: ....................................................................................................................................... 5 
7 Get Bank Account Details API with  Aadhaar ....................................................................................................... 5 
7.1 Get Bank Account Details API Request .............................................................................................................. 6 
7.1.1 Request Tag Specification ............................................................................................................................ 6 
7.2 ACK/NACK from Bank ....................................................................................................................................... 7 
7.3 Get Bank Account Details API Response ........................................................................................................... 7 
7.3.1 Response tag specification ........................................................................................................................... 7 
8 Elements and Attributes Definition ...................................................................................................................... 8 
9 GET Bank Account Details -ACK/NACK (BASE to Destination Bank) .................................................................... 12 
10 Sample Request Data ....................................................................................................................................... 13 
10.1 Sample Response Data (Success) .................................................................................................................. 13 
10.2 Sample Response Data (Failure) .................................................................................................................... 13 
11 Appendix ......................................................................................................................................................... 14 
11.1 List of values for accType .............................................................................................................................. 14 
11.2 Bank reasonCode .......................................................................................................................................... 14

<!-- Page 6 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 3 of 14 
 
Glossary 
 
Term 
Definition 
BASE 
Bharat Aadhaar Seeding Enabler 
NPCI 
National Payments Corporation of India. 
API 
Application Programming Interface 
ACK 
Acknowledgement 
NACK 
Negative Acknowledgement

<!-- Page 7 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 4 of 14 
 
1 Introduction 
 
Customers will be able to get the details of their bank account linked to their Aadhaar both at 
NPCI mapper and bank .Customer can directly get these details from the BASE platform by doing 
Aadhaar based OTP authentication . 
 
2 Overview of the existing process 
 
Currently there is no such API to get the Account details of the customer by providing the 
Aadhaar number from the BASE application. 
 
3 Proposed process flow  
 
• 
Customer gives the Aadhaar number in BASE . 
• 
BASE will internally validate and send the request to the bank. 
• 
Bank will respond with the various account related details to BASE . 
• 
BASE will display the details to the customer . 
 
4 Functional flow of Get Bank Account Details API 
 
• 
Customer will give only Aadhaar number as input in BASE web page. 
• 
Customer has to agree for the consent and input Captcha . 
• 
On submitting the request,BASE will send the request to UIDAI for the Aadhaar OTP 
validation . 
• 
UIDAI sends the OTP to the customer and customer has to enter the OTP on BASE 
platform. 
• 
BASE then sends the request to UIDAI for OTP verification and UIDAI will validate OTP 
and send the response to BASE . 
• 
On succesful OTP verification,BASE will find the bank linked to the Aadhaar from NPCI 
mapper. 
• 
Once the internal validations are succesful ,BASE sends the request to the destination 
bank. 
• 
Bank will provide the necessary account details to BASE . 
• 
BASE will display the details to customer. 
 
5 Bank validations 
Banks 
should 
validate 
the 
below 
details 
before 
sending 
response 
to 
BASE. 
 
• 
If an Aadhaar is linked to single account,then bank has to check whether the subsidy flag 
is enabled in that account ,then respond with the account number ,account holder name 
and account type linked to the Aadhaar along with other details. 
• 
If an Aadhaar is linked to multiple accounts ,then bank has to check the exact account 
number to which Aadhaar is linked and subsidy flag is enabled and send the appropriate 
response to BASE. 
• 
Only for the cases where an account is linked to Aadhaar number provided in the request 
and subsidy flag is enabled,bank has to respond with result as ‘SUCCESS’ and provide the 
customer details to BASE.In all other cases ,it will provide the result as ‘FAILURE’ with 
the appropriate reason code given in the list below and bank will not provide the 
customer detail. 
• 
If subsidy flag is not enabled to any account linked to the Aadhaar ,then bank has to 
consider it as failure and send the appropriate reason code response to BASE.No other 
account details will be given by bank.

<!-- Page 8 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 5 of 14 
 
 
6 Signing and Encryption: 
➢ BASE(Source) to Bank (Destination) – Request  
❖ Encryption will be done using the public key certificate shared by Destination Bank.  
❖ Signing Using Private key certificate of the NPCI. 
➢ Bank(Destination) to BASE (Source) - Response 
❖ Encryption will be done using the Public Key certificate shared by NPCI.  
❖ Signing Using Private key certificate of Destination Bank. 
Attributes applicable for encryption are Aadhaar number, Account number, Account 
name, Account type and if any other personal information. 
Algorithms to be used for signing and encryption: 
XML Signing:  
DigestMethod.SHA256,http://www.w3.org/2001/04/xmldsig-more#rsa-sha256 
Encryption: RSA/ECB/PKCS1Padding 
• 
SSL Handshake protocol will exchange public key certificates to authenticate server & 
client to each other and it is mandatory 
7 Get Bank Account Details API with  Aadhaar  
 
Purpose :This API request will be initiated by BASE application to Destination bank. With this 
service customer can know whether his/her aadhaar number is linked with the account number 
in their bank CBS and if it is linked whether subsidy is enabled for that account from banks 
response along with other account details . 
 
 
• 
All REST APIs are exposed as stateless service over HTTPS. All the APIs shall be initiated 
as an HTTPS call and acknowledged with an ACK/NACK message. 
 
          Following is the URL format for all APIs under the BASE interface: 
https://<host>/base/<api>/<ver> 
 
For example , 
 
https://npci.org/base/GetBankAccDltsRqst/1.0 
 
host – API server address (Actual production server address will be provided to members     
at the time of rollout and all API clients should ensure that actual URL is configurable). 
base – static value denoting the root of all API URL paths under the NACH API 
api – name of the API URL endpoint. 
ver – version of the API. Multiple versions of the same API may be available for supporting 
gradual migration. For this migration, default version will be "1.0".

<!-- Page 9 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 6 of 14 
 
 
 
 7.1 Get Bank Account Details API Request   
 
Privilege: Initiated by BASE 
 
API type and format: Asynchronous API & XML format 
 
 
<base:GetBankAccDltsRqst xmlns:base="http://npci.org/base/schema/" > 
<Head ver="1.0" ts="2021-10-16T10:02:00" /> 
 
<Source type="CODE" value="BASE" name="" /> 
<Destination type="CODE" value="XXXX" name="" /> 
<Request id=" " type="GETBANKACC_DETAILS" refUrl=" "/> 
<ReqData custConsent="Y" filler1=" " filler2=" "> 
<Detail> 
data =Encrypted block of aadhaarNumber  
</Detail> 
</ReqData> 
 
<NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa"/> 
</base:GetBankAccDltsRqst> 
 
   7.1.1 Request Tag Specification   
 
Index 
Message Item 
<XML Tag> 
Occurrenc
e 
1 
API Name 
GetBankAccDltsRqs
t  
1..1 
2 
API Schema namespace 
xmlns 
1..1 
3 
Header for the message 
<Head> 
1..1 
4 
Version of the API 
ver 
1..1 
5 
Time of request from the creator of the 
message (Transmission time) 
ts 
1..1 
6 
Source of the message 
<Source> 
1..1 
7 
Routing type of the Source banks – based on 
short code of the bank the corresponding URL 
will be identified  
type 
1..1 
8 
Actual value of the routing type shortcode of 
source 
value 
1..1 
9 
Name of the Source Bank 
name 
0..1 
10 
Destination of the message 
<Destination> 
1..1 
11 
Routing type of the Source banks – based on 
short code of the bank the corresponding URL 
will be identified  
type 
1..1 
12 
Actual value of the routing type short code of 
destination 
value 
1..1 
13 
Name of the Destination Bank 
name 
0..1 
14 
Request Message element 
<Request> 
1..1 
15 
Id of the Request generated by the originator 
Id 
1..1 
16 
Type 
of 
the 
request. 
Should 
be 
GETBANKACC_DETAILS 
type 
1..1

<!-- Page 10 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 7 of 14 
 
17 
Reference URL for the transaction  
refUrl 
0..1 
18 
input data related to the request 
<ReqData> 
1..1 
19 
Details of the Input parameters of the request 
<Details> 
1..1 
20 
Customer Aadhaar number in encrypted 
Data 
1..1 
21 
Customer consent will always ‘Y’ 
custConsent 
1..1 
22 
Filler 1 – should be left blank  
filler1 
0..1 
23 
Filler 2 – should be left blank 
filler2 
0..1 
24 
Unique Identified assigned by NPCI for the 
request 
<NpciRefId> 
1..1 
25 
Actual unique value generated by NPCI 
value 
1..1 
 
 7.2 ACK/NACK from Bank 
 
HTTP Response 202 should be initiated from bank end once the request is received by bank 
successfully. Else we consider it as request failed to post at bank endpoint as it is not reachable. 
So, http -202 resp is mandatory 
 
7.3 Get Bank Account Details API Response 
 
This API response will be initiated by Destination Bank for GET BankAccount Details to BASE 
application. 
 
Privilege: Initiated by Bank 
 
API type and format: Asynchronous & XML format 
 
<base:GetBankAccDltsResp xmlns:base="http://npci.org/base/schema/" > 
<Head ver="1.0" ts="2017-10-16T10:02:00" /> 
 
<Source type="CODE" value="XXXX" name="" /> 
<Destination type="CODE" value="BASE" name="" /> 
<Request id=" " type=" GETBANKACC_DETAILS" refUrl=""/> 
<RespData subsidyFlag="Y" filler1=" " filler2=" "> 
<Detail> 
     data =Encrypted block of accNo, accHolderName ,accType  
</Detail> 
<Resp ts="2021-10-16T10:02:00" result=" " reasonCode=" " /> 
 
</RespData>  
<NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa"/> 
</base:GetBankAccDltsResp > 
 
7.3.1 Response tag specification 
 
 
Index 
Message Item 
<XML Tag> 
Occurre
nce 
1 
API Name 
<GetBankAccDltsRe
sp> 
1..1 
2 
API Schema namespace 
xmlns 
1..1 
3 
Header for the message 
<Head> 
1..1

<!-- Page 11 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 8 of 14 
 
4 
Version of the API 
ver 
1..1 
5 
Time of request from the creator of the message 
(Transmission time) 
ts 
1..1 
6 
Source of the message 
<Source> 
1..1 
7 
Routing type of the Source banks – based on short 
code of the bank the corresponding URL will be 
identified  
type 
1..1 
8 
Actual value of the routing type shortcode of source 
value 
1..1 
9 
Name of the Source Bank 
name 
0..1 
10 
Destination of the message 
<Destination> 
1..1 
11 
Routing type of the Source banks – based on short 
code of the bank the corresponding URL will be 
identified  
type 
1..1 
12 
Actual value of the routing type short code of 
destination 
value 
1..1 
13 
Name of the Destination Bank 
name 
0..1 
14 
Request Message element 
<Request> 
1..1 
15 
Id of the Request generated by the originator 
Id 
1..1 
16 
Type of the request. Ie GETACC_DETAILS 
type 
1..1 
17 
Reference URL for the transaction  
refUrl 
0..1 
18 
Response Data element 
<RespData> 
1..1 
19 
Response status element 
<Resp> 
1..1 
20 
time of response generation 
ts 
1..1 
21 
Result of the request(SUCCESS || FAILURE) 
result 
1..1 
22 
Error reason codes for the failure message 
reasonCode 
1..1 
23 
Details of the Input parameters of the request 
<Detail> 
1..1 
24 
Encrypted block of accNo, 
accHolderName,accType 
          data 
0..1 
25 
subsidy enabled flag for the account (Y || N) 
    subsidyFlag 
0..1 
26 
Filler 1 should be kept blank 
     filler1 
0..1 
27 
filler 2 should be kept blank 
      filler2 
0..1 
28 
Unique Identified assigned by NPCI for the request 
<NpciRefId> 
1..1 
29 
Actual unique value generated by NPCI 
value 
1..1 
 
 
 
8 Elements and Attributes Definition 
 
Element: Root  
Definition: 
 
XML 
root 
element 
representing 
each 
API 
(base:GetBankAccDltsRqst, 
GetBankAccDltsResp) 
 
 
Attribute: xmlns 
Definition:  API Schema Namespace. 
Data Type: 
Alphanumeric 
Format:     
Min Length:   1 
                
Max Length:  255 
 
Element: <Head> 
Definition:  Header of the Message

<!-- Page 12 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 9 of 14 
 
 
Attribute: ver 
Definition:   Version of the API 
This is the API version. NPCI may host multiple versions for supporting gradual migration. As of 
this specification, default production version is "1.0". 
Data Type: 
Float 
Format:     
Min Length:   1 (length is not checked as version should be “1.0”) 
                
Max Length:  6 
 
 
Attribute: ts 
Definition:   Time of request from the creator of the message. API request time stamp. Since 
timestamp plays a critical role, it is highly recommended that devices are time synchronized 
with a time server. 
Data Type: 
ISODateTime 
Format:     
Min Length: 19 
Max Length: 19  
                
YYYY-MM-DDThh:mm:ss 
                
(e.g., 1997-07-16T19:20:30) 
Where, 
  
YYYY = Four-digit year 
  
MM = Two-digit month (01=January, etc.) 
  
DD = Two-digit day of month (01 through 31) 
  
hh = Two digits of hour (00 through 23) (am/pm NOT allowed) 
  
mm = Two digits of minute (00 through 59) 
  
ss  = Two digits of second (00 through 59) 
GMT in hours and minutes 
 
Element: <Request> 
Definition:  This element contains the Request details and is visible to all parties involved in 
the transaction processing. This element is populated by the originator of the request 
and the same must be passed across all the entities. 
 
 Attribute: id 
Definition:  Unique Identifier for the request across all entities. This will be created by the 
originator. This field will be used to identify each request uniquely across all the entities.  
Data Type: 
Alphanumeric 
Format:     
Min Length:   1 
                
Max Length:  22 
Attribute: type 
Definition:  This attribute describes the type of the Request 
Data Type: 
Enumeration or Code. Length check is not there as it should be in the list of 
prescribed types. The allowed values are GETBANKACC_DETAILS as per the request initiated 
by user. In response the type value should be same as received in the request. 
Format:     
Min Length:   NA 
                
Max Length:  NA 
Attribute: refUrl 
Definition: URL for the transaction 
Data Type: 
Alphanumeric with special characters  
Format:     
Min Length:   1 
                
Max Length:  35

<!-- Page 13 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 10 of 14 
 
Element: <Source> 
Definition:  This element contains the details of the originator of the request and the same 
must be passed across all the entities.  
Attribute: type 
Definition:  This indicates the routing type to be used. Currently allowed routing type is only 
Bank short code and it should be always ‘CODE’. Length check will not be done as it should be 
always CODE 
Data Type: 
Alpha 
Format:     
Min Length:   NA 
                
Max Length:  NA 
Attribute: value  
Definition:  This attribute contains the actual value of the routing type and this value will be 
used to identify the endpoint URL of the participant which is used to initiate any communication 
from NPCI 
Data Type: 
Alpha 
Format:     
Min Length:   4 
                
Max Length:  4 
Attribute: name 
Definition:  This attribute carries the name of the Source.  
Data Type: 
Alphabets with special characters like dot, space, hyphen & single quote 
Format:     
Min Length:   0 
                
Max Length:  100 
Element: <Destination> 
Definition:  This element contains the details of the originator of the request and the same 
must be passed across all the entities.  
Attribute: type 
Definition:  This indicates the routing type to be used. Currently allowed routing type is only 
Bank short code and it should be always ‘CODE’. Length check will not be done as it should be 
always CODE 
Data Type: 
Alpha 
Format:     
Min Length:   NA 
                
Max Length:  NA 
Attribute: value  
Definition:  This attribute contains the actual value of the routing type and this value will be 
used to identify the endpoint URL of the participant which is used to initiate any communication 
from NPCI. Allowed value is bank shortcode 
Data Type: 
Alphanum  
Format:     
Min Length:   4 
                
Max Length:  4 
Attribute: name 
Definition:  This attribute carries the name of the destination.  
Data Type: 
Alphabets with special characters like dot, space, hyphen & single quote 
Format:     
Min Length:   0 
                
Max Length:  100 
Element: <Detail> 
Definition:  This element contains the parameters of the actual request and the same must be 
passed to Destination for processing.  
Attribute: data 
Definition:  This attribute carries the encrypted block of Aadhaar number passed in the request.

<!-- Page 14 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 11 of 14 
 
Data Type: 
Numeric 
Format:     
Min Length:   1 
                
Max Length:  35 
On decryption actual data provided under this field will have the below clear format . 
 
<aadhaarNumber>"123456789012"</aadhaarNumber> 
Attribute: custConsent 
Definition:  To provide the customer consent on this parameter value.  
Data Type: 
ENUM 
Format:     
Min Length:   1 
                
Max Length:  1 
Values may be Y/N 
Attribute: filler1/ filler2 
Definition:  for the use of future purpose in both request and response. It should be left blank  
Data Type: 
Alphanum 
Format:     
Min Length:   1 
                
Max Length:  50 
Element: <Resp> 
Definition:  This element contains the information about the Response. 
Attribute: result 
Definition:  This attribute is used to indicate the result of the requested message. And it should 
have the any one of the values from the pre-defined list. 
Data Type: 
Code  
Format:     
Min Length:   NA 
                
Max Length:  NA 
  Values: 
 
   
 
 
 
Attribute: reasonCode 
Definition:  This attribute is used to indicate the reasons for rejection in case of failure.  Or 
the status code in case of success and it should have the one or many values from the pre-
defined list. Multiple error codes will be separated by comma.  
Data Type: 
Code  
Format:     
Min Length:   NA 
                
Max Length:  NA 
Values : For success response value should be ‘0000’ .For failure, reason codes can be referred 
from Appendix1. 
 
 
Element: <Detail> in Response 
Definition:  This element contains the parameters of the actual response and the same must 
be passed to BASE from destination bank. 
 
Attribute: data 
Definition:  This attribute carries the Encrypted block of accNo, accHolderName ,accType 
passed in the response 
Data Type: 
Alphanumeric 
Code 
Value 
SUCCESS 
If Aadhaar is linked to account and subsidy flag is 
enabled 
FAILURE 
All other cases it will be considered as Failure.

<!-- Page 15 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 12 of 14 
 
Format:     
Min Length:   1 
                
Max Length:  500 
 
On decryption actual data provided under this field will have the below clear format . 
 
<accNo>"123456789034"</accNo>" 
<accHolderName>"GUPTA"</accHolderName> 
<accType>"01"</accType> 
 
Values :accType values can be referred from Appendix 1. 
 
 
Attribute: subsidyFlag 
Definition:  This will provide if the subsidy flag is enabled for the account . 
Data Type: 
Alphanum 
Format:     
Min Length:   1 
                
Max Length:  2 
Values : Values will be Y or N. 
 
 
Attribute: NpcirefId 
Definition:  This attribute is used to indicate the uniqueness for each request which will be 
generated by the NPCI only. In the request this attribute value should be given and in  response 
destination bank should provide the exact value which they have received in the request file  
Data Type: 
Code  
Format:     
Min Length:   36 
                
Max Length:  36         
 
9 GET Bank Account Details -ACK/NACK (BASE to Destination Bank) 
 
This 
ACK/NACK 
will 
be 
a 
HTTP 
Response 
by 
BASE 
to 
destination 
bank 
for 
GETBANKACC_DETAILS. 
 
<base:GetBankAccDltsRespAck  xmlns:base="http://npci.org/base/schema/"> 
  <NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa"/> 
  <Resp ts="2017-10-16T10:02:00" result="SUCCESS" errCode=" " rejectedBy=" " /> 
</base:GetBankAccDltsRespAck> 
 
Index 
Message Item 
<XML Tag> 
Occurrence 
1 
API Name 
<GetAccDltsRespAck> 
1..1 
2 
API Schema namespace 
xmlns 
1..1 
3 
Unique Identified assigned by NPCI 
for the request 
<NpciRefId> 
1..1 
4 
Actual unique value generated by 
NPCI 
value 
1..1 
5 
Response of the Message 
<Resp> 
1..1 
6 
Time of response from the sender 
of the message  
ts 
1..1 
7 
Result of the request 
result 
1..1 
8 
Error reason codes for the failure 
message 
errCode 
0..1

<!-- Page 16 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 13 of 14 
 
9 
Actual rejecter of the message. 
NPCI or Destination who rejected 
the message 
rejectedBy 
0..1 
 
10 Sample Request Data 
 
Below sample response contains the response without signature. 
 
<base:GetBankAccDltsRqst xmlns:base="http://npci.org/base/schema/" > 
<Head ver="1.0" ts="2021-10-16T10:02:00" /> 
 
<Source type="CODE" value="BASE" name=" " /> 
<Destination type="CODE" value="SBIN" name="" /> 
<Request id="1200001" type="GETBANKACC_DETAILS" refUrl=""/> 
     <ReqData custConsent="Y" filler1=" " filler2=" " > 
                                 <Detail>  
 data =Encrypted block of aadhaarNumber  
</Detail>   
</ReqData> 
 
<NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa"/> 
</base:GetBankAccDltsRqst> 
 
 10.1 Sample Response Data (Success) 
 
Below sample response contains the response without signature. 
 
<base:GetBankAccDltsResp xmlns:base="http://npci.org/base/schema/" > 
<Head ver="1.0" ts="2017-10-16T10:02:00" /> 
 
<Source type="CODE" value="SBIN" name="" /> 
<Destination type="CODE" value="BASE" name=" " /> 
<Request id="1200001" type="GETBANKACC_DETAILS" refUrl=""/> 
                          <RespData subsidyFlag="Y" filler1=" " filler2=" "> 
                                <Detail> 
                                     data =Encrypted block of accNo,accHolderName,accType  
</Detail> 
<Resp ts="2021-10-16T10:03:00" result="SUCCESS" reasonCode="0000"/>  
           </RespData>  
<NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa"/> 
</base:GetBankAccDltsResp> 
 
10.2 Sample Response Data (Failure) 
 
Below sample response contains the response without signature. 
 
<base:GetBankAccDltsResp xmlns:base="http://npci.org/base/schema/" > 
<Head ver="1.0" ts="2017-10-16T10:02:00" /> 
 
<Source type="CODE" value="SBIN" name="" /> 
<Destination type="CODE" value="BASE" name=" " /> 
<Request id="1200001" type=" GETBANKACC_DETAILS" refUrl=""/> 
                     <RespData> 
<Resp ts="2021-10-16T10:03:00" result="FAILURE" reasonCode="B005"/> 
           </RespData>  
<NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa"/> 
</base:GetBankAccDltsResp>

<!-- Page 17 -->

 
 
  Get Bank Account Details TSD 1.1 
 
Page 14 of 14 
 
11 Appendix  
 
11.1 List of values for accType 
 
01 -Savings account 
02-Current account 
03-OD account 
04-Others 
 
11.2 Bank reasonCode 
 
Code 
Name 
000 
Account Active 
G01 
No data available in bank CBS for given Aadhaar number for DBT 
G02 
Account  inoperative 
 G03 
Dormant account 
 G04 
A/c Blocked or Frozen 
G05 
Account requires KYC document 
 
 
End of the Document
