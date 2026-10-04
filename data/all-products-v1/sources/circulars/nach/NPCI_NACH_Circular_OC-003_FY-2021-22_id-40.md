# Circular no. 003 - Annexure II - Linkage status of Acc no - API Specification - V 1.0

Circular/reference number: OC-003

<!-- Page 1 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
1 
 
 
 
 
 
 
 
 
 
 
NACH-API Specification 
Get Aadhaar Linkage status of the AccNo for the 
given Aadhaar number. 
 
 
Version 1.0

<!-- Page 2 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
2 
 
 
Contents 
 
1. 
Introduction ........................................................................................................................ 3 
1.1 
Objectives ....................................................................................................................... 3 
2. 
Communication Channel.................................................................................................... 4 
2.1 
Channel Encryption Details ........................................................................................... 4 
2.2 
Certificate Format ......................................................................................................... 4 
2.3 
Plain JSON message of request .................................................................................... 5 
2.4 
Sample Message with signature .................................................................................... 7 
2.5 
Encoding and decoding of the each value of the JSON and singed XML message 
using Base64 ................................................................................................................................ 8 
2.6 
Encryption and Signing process .................................................................................. 10 
3. 
API Protocol ...................................................................................................................... 10 
3.1 
Obtaining/Get Linkage Status of Account number for the given Aadhaar Number
 
12 
3.2 
General ACK/NACK Message format........................................................................... 16 
3.3 
Destination Asynchronous Failure Response Message format.................................. 16 
3.4 
Elements and Attributes Definition............................................................................ 17 
4. 
Error Codes ....................................................................................................................... 25 
4.1 
Technical Validation Error Codes ............................................................................... 25 
4.2  Business Validation Error Codes ...................................................................................... 27

<!-- Page 3 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
3 
 
1. Introduction 
 
This is a value added services from NACH to Govt Bodies/Corporates. This service 
will help to know the Account status and aadhaar linkage status for the given aadhaar 
number. This will also improve the overall efficiency of the echo system. 
 
1.1 Objectives 
 
Objectives of introducing Application interface in NACH is to offer a standard API 
to facilitate for verifying the account information from the destination banks for 
the given input. 
 
By using this API sender party can get the details like  
o Status of the customer account, 
o Aadhaar Linkage status  
o Account number 
Any Govt.Bodies / Corporates can use this API after NPCI authorisation

<!-- Page 4 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
4 
 
 
2. Communication Channel 
 
2.1 Channel Encryption Details 
 
NACH network communication channel should be encrypted and secured to maintain the 
secrecy and eligibility of the data travelling through the medium. 
Source and Destination banks need to exchange the RSA public keys with NPCI as 
demonstrated in below figure. 
 
Figure 1 Key Exchange 
Signing Description: 
 
Source/destination Bank signs the XML message using their private key. 
 
When Source message received at NACH system, it trusts the message using 
Source/destination Bank Public Key. 
 
SSL Handshake Description: 
 
Handshake protocol will exchange public key certificate to authenticate server 
(i.e., Source Host) & client to each other. 
 
In case of RSA key exchange, 
 
Source Host generate pre-master secret. 
 
Pre-master secret is encrypted using NACH Public Key. 
 
NACH can decrypt the PMK (Pre Master Key) using Private Key.  
 
Similarly, when Destination Host acts as server the respective public key will be 
used to exchange the pre-master secret key. 
 
Client authentication by server is mandatory 
2.2 Certificate Format  
 
Certificate formats 
 
509 certificates v3: (etc.npci.org.in)

<!-- Page 5 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
5 
 
 
We need fully qualified domain name certificate from authorised 
CA.(Main,Intermediate,root) 
 
No wildcards in certificate 
 
Self-signed certificate not acceptable 
 
TLS_RSA_WITH_AES_256_CBC_SHA 
 
Chiper Suites 
 
Key exchange- RSA 
 
Authentication- RSA 2048 
 
Block Chiper AES 256 
 
Hash –SHA 256 (HMAC & PRF) 
 
 
Figure 2 Flow Chart 
2.3 Plain JSON message of request 
 
Following is the JSON format of request and response messages. 
 
Source :<< Source Bank Short Name>>   // Base64 encoded 
Service : <<Service Name>>       // Base64 encoded 
Type    : <<Request | Response >>    // Base64 encoded 
Message : << Signed XML message of actual Request or Response >>// Base64 
encoded 
 
Sample Request in clear text: 
{"Source":"KART","Service":"GetAccNoInfo","Type":"Request","Message"="<ach:GetAccNoInfoRqst 
xmlns:ach="http://npci.org/ach/schema/" > 
<Head ver="1.0" ts="2017-10-16T10:02:00" />  
<Source type="CODE" value="KART" name="Karnataka Govt " /> 
<Destination type="CODE" value="508508" name="" />

<!-- Page 6 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
6 
 
<Request id="123456789" type="DBT | NON_DBT" refUrl=""/> 
<ReqData> 
<Detail aadhaar="234567890123" accNo="56475648900909" custConsent="Y" filler1="" filler2="" /> 
</ReqData> 
 
<NpciRefId value=""/> 
</ach:GetAccNoInfoRqst>"} 
 
Sample Response in clear text: 
 
{"Source":"SYND","Service":"GetAccNoInfo","Type":"Response","Message":" 
<ach:GetAccNoInfoResp xmlns:ach="http://npci.org/ach/schema/"> 
<Head ver="1.0" ts="2017-10-16T10:02:15" > 
 
 
<Source type="CODE" value="KART" name="Karnataka Govt " /> 
 
<Destination type="CODE" value="508508" name="" /> 
 
<Request id="123456789" type="DBT | NON_DBT" refUrl=""/> 
 
<Resp ts="2017-10-16T10:02:15" result="SUCCESS" errCode="" rejectedBy="" /> 
 
<RespData> 
 
 
<Aadhaar linkStatus="Y" status="S601" subsidyAccFlag="Y" accNo="7384" 
type="T659" filler1="" filler2="" filler3="" filler4="" filler5="" />  
 
 
 
</RespData> 
 
<NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa" /> 
</ach:GetAccNoInfoResp> "} 
 
JSON Format of message with encryption of values: 
{"Source":"KART","Service":"GetAccNoInfo","Type":"Request","Message"="<?xml version="1.0" 
encoding="UTF-8" standalone="no"?><ach:GetAccNoInfoRqst 
xmlns:ach="http://npci.org/ach/schema/"> 
<Head ts="2017-10-16T10:02:00" ver="1.0"/> 
 
<Source name="Karnataka Govt " type="CODE" value="KART"/> 
<Destination name="" type="CODE" value="508508"/> 
<Request id="123456789" refUrl="" type="DBT | NON_DBT"/> 
<ReqData> 
<Detail filler1="" filler2="" 
aadhaar="O+/oN/Kgql8iNsljvnQIehsrAQ4lfSJqenX+lqUTsFeIccfBes4bGZ2as5rBgVQBMqR1gejBoGRaz
KTB7C/uQaDaHkMdPSX0z1p550gAcLamVm+KU5rSrLFObxgZPPi4mQUJwg1ASmeil9Tq4fe6z0hSB+V5Z
Z9bqpRVPieFAi9NmfnDU0f5xgJuSvptbhB3V3PZgPxlgS9U4papJebFM2GWSroXj0xwL19pLJ3o22nEosvt

<!-- Page 7 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
7 
 
zXUqsd/2S03Zjg2J6SOzyIEkI4YdmE9Hv8diGmWAVRqJqAZwBRfmDYRJOvm80eOa8Y3i1HMjmIjW4zsz
eJZiZz8dBO8pmkqcchszNg==" 
accNo="vxpjU3L/pJ8ub8d50eo7QKZzrgRpHKT0kAO0PmKSkwBrKvMbBgVkmkugbsvKdArM+e311sq/u
rxdQDasJxzcwuHTTN1WiIGAi4+emknCDfQyq0n90ZlLU2DyIVowqSiKHH5C5muulazR3JzVIDqyw6W4W
e80Ei3ljO7CQAFCel9Cb76k0j7ux9MQmVLAyZSlPoyWC2NmyXbdojwVpEZxTQA3scBPLfQm+Ad+PoW
WlH7pbuy/quzzQOM0jlaZZwhVI/4ogh+fel2xNOv8AjPJNFKpqAciyuXNbvbAsmQ/gCo+6CfhZZkdZiaWq
JsIByEmpjzQqFxhvrvt1zq9tawSCA==" custConsent="Y"/> 
</ReqData> 
 
<NpciRefId value=""/> 
ach:GetAccNoInfoRqst>"} 
 
2.4  Sample Message with signature  
 
{"Source":"KART","Service":"GetAccNoInfo","Type":"Request","Message"="<?xml version="1.0" 
encoding="UTF-8" standalone="no"?><ach:GetAccNoInfoRqst 
xmlns:ach="http://npci.org/ach/schema/"> 
<Head ts="2017-10-16T10:02:00" ver="1.0"/> 
 
<Source name="Karnataka Govt " type="CODE" value="KART"/> 
<Destination name="" type="CODE" value="508508"/> 
<Request id="123456789" refUrl="" type="DBT | NON_DBT"/> 
<ReqData> 
<Detail filler1="" filler2="" 
aadhaar="O+/oN/Kgql8iNsljvnQIehsrAQ4lfSJqenX+lqUTsFeIccfBes4bGZ2as5rBgVQBMqR1gejBoGRaz
KTB7C/uQaDaHkMdPSX0z1p550gAcLamVm+KU5rSrLFObxgZPPi4mQUJwg1ASmeil9Tq4fe6z0hSB+V5Z
Z9bqpRVPieFAi9NmfnDU0f5xgJuSvptbhB3V3PZgPxlgS9U4papJebFM2GWSroXj0xwL19pLJ3o22nEosvt
zXUqsd/2S03Zjg2J6SOzyIEkI4YdmE9Hv8diGmWAVRqJqAZwBRfmDYRJOvm80eOa8Y3i1HMjmIjW4zsz
eJZiZz8dBO8pmkqcchszNg==" 
accNo="vxpjU3L/pJ8ub8d50eo7QKZzrgRpHKT0kAO0PmKSkwBrKvMbBgVkmkugbsvKdArM+e311sq/u
rxdQDasJxzcwuHTTN1WiIGAi4+emknCDfQyq0n90ZlLU2DyIVowqSiKHH5C5muulazR3JzVIDqyw6W4W
e80Ei3ljO7CQAFCel9Cb76k0j7ux9MQmVLAyZSlPoyWC2NmyXbdojwVpEZxTQA3scBPLfQm+Ad+PoW
WlH7pbuy/quzzQOM0jlaZZwhVI/4ogh+fel2xNOv8AjPJNFKpqAciyuXNbvbAsmQ/gCo+6CfhZZkdZiaWq
JsIByEmpjzQqFxhvrvt1zq9tawSCA==" custConsent="Y"/> 
</ReqData> 
 
<NpciRefId value=""/> 
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#"><SignedInfo><CanonicalizationMethod 
Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/><SignatureMethod 
Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/><Reference 
URI=""><Transforms><Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-
signature"/></Transforms><DigestMethod 
Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/><DigestValue>Tff7Q0+6lrkNtCmKYeSAIC
4Os6IZ84N+gHTOE+x4Dek=</DigestValue></Reference></SignedInfo><SignatureValue>N1IeSzz+t2B
a6WAu6es8vGgqxfVM1Je9WyJuEwdrluNB/PFhO4bhQM+PKDlVr9b5mgOzJIAxWREF 
hojoF/NcjXRvlwW5J82xHF0iwZJJNeIVv7D5gspvlxr9EylYw9Y/GnGYgLjlb5K4n9wiRmofR/Uh 
ecNv0ahLmDhRrjqkV4fDxXv/e4BBixYjvMeF7GwWX0alZAu0XpmE6hj16btW8JiMaV+OLBCeQlf2 
EoD7/WpdSD9VB/WRsuTEN3LVI2D7jXMwD2sLTUm9sCP0AmuDRFFfAIfJOM3sRvaLGJOZp/tCfJAs 
ONcRThvJpurwpg89RRumuDYnnZhK1eOPyHOuIg==</SignatureValue><KeyInfo><X509Data><X509S
ubjectName>CN=cm.npci.org.in,O=National Payments Corporation of 
India,L=Mumbai,ST=Maharashtra,C=IN,2.5.4.5=#1306313839303637,1.3.6.1.4.1.311.60.2.1.3=#1302
494e,2.5.4.15=#0c1450726976617465204f7267616e697a6174696f6e</X509SubjectName><X509Ce

<!-- Page 8 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
8 
 
rtificate>MIIFsDCCBJigAwIBAgIQBnLbLa0z7sUfIFRs0U1TjjANBgkqhkiG9w0BAQsFADB1MQswCQYDVQ
QG 
EwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMT
Qw 
MgYDVQQDEytEaWdpQ2VydCBTSEEyIEV4dGVuZGVkIFZhbGlkYXRpb24gU2VydmVyIENBMB4XDTIw 
MDIwNzAwMDAwMFoXDTIyMDIxMTEyMDAwMFowgcMxHTAbBgNVBA8MFFByaXZhdGUgT3JnYW5p
emF0 
aW9uMRMwEQYLKwYBBAGCNzwCAQMTAklOMQ8wDQYDVQQFEwYxODkwNjcxCzAJBgNVBAYTAklO
MRQw 
EgYDVQQIEwtNYWhhcmFzaHRyYTEPMA0GA1UEBxMGTXVtYmFpMS8wLQYDVQQKEyZOYXRpb25hbC
BQ 
YXltZW50cyBDb3Jwb3JhdGlvbiBvZiBJbmRpYTEXMBUGA1UEAxMOY20ubnBjaS5vcmcuaW4wggEi 
MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDuW7yVDsiHaGlj2uMrhKmgVxMisogf/9cxMZGc 
kMeJVYnQ/Mr2smIisNe3eRjS6yYdMWwen5ajYh2exhwEkyCMgXZ/owYNoMZPnZI+bU064pxTNRyS 
cr5XiA9rdV+s12sEvZ8oX2+vGGYABDj+qHKK7yGPRiMU1OH+RCha0/wJBgLe/K7myr4kVPDxibRc 
gKAQrl2+72gyT+6SClJINw66pJeQA8hY0nOOWiVes6CT2SAANnY1WJinOZwMI1PZMOmeYXv/EVg2 
HSNeF09zVZDc1vfxMkWZt4tXA6zjrhc2ANG9ju4GplP/1saORIIbQVS882pAM/3eB0QPz81XQh29 
AgMBAAGjggHrMIIB5zAfBgNVHSMEGDAWgBQ901Cl1qCt7vNKYApl0yHU+PjWDzAdBgNVHQ4EFgQU 
sNow+zZTrMHKwjKqAw/NkcOoV+8wGQYDVR0RBBIwEIIOY20ubnBjaS5vcmcuaW4wDgYDVR0PAQH/ 
BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjB1BgNVHR8EbjBsMDSgMqA
whi5o 
dHRwOi8vY3JsMy5kaWdpY2VydC5jb20vc2hhMi1ldi1zZXJ2ZXItZzIuY3JsMDSgMqAwhi5odHRw 
Oi8vY3JsNC5kaWdpY2VydC5jb20vc2hhMi1ldi1zZXJ2ZXItZzIuY3JsMEsGA1UdIAREMEIwNwYJ 
YIZIAYb9bAIBMCowKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LmRpZ2ljZXJ0LmNvbS9DUFMwBwYF 
Z4EMAQEwgYgGCCsGAQUFBwEBBHwwejAkBggrBgEFBQcwAYYYaHR0cDovL29jc3AuZGlnaWNlcnQu 
Y29tMFIGCCsGAQUFBzAChkZodHRwOi8vY2FjZXJ0cy5kaWdpY2VydC5jb20vRGlnaUNlcnRTSEEy 
RXh0ZW5kZWRWYWxpZGF0aW9uU2VydmVyQ0EuY3J0MAwGA1UdEwEB/wQCMAAwDQYJKoZIhvcN
AQEL 
BQADggEBALWJfp89KFuD6GrfRXy9mc1S8gYM/ndTAfH5svSQ0K5TrFRYjijeZ2uTrpp5tVT3SI2S 
I59TuZ9iAJCcGAdpgi5xWs8F0+guIZbn0wzLAVfIKZyMNCTR6bFg4HMqrKtZgZh/ZYhTgSYDxOXP 
zeIzIdie9nhH1pzY7jHNrLfSi/ecQKYToJpTe9S8aaKVzOHkxcpGNRjKOSuvJFEYp7O+HZVUurFw 
KI9ueR/xsPKwzLqGk3NHZaxqrkqE50lGWi93ID9B1263QAaPMFPC+lKOktgUG3pf/eVgANSu+geo 
OgSG9hmJyVz7b13JNccPqz8+Q7xV5O4qaqkP2VVP2q0ityc=</X509Certificate></X509Data></KeyInfo
></Signature></ach:GetAccNoInfoRqst>"} 
 
2.5 Encoding and decoding of the each value of the JSON and singed XML 
message using Base64 
 
The Signed XML content of input JSON message should be in encoded format using 
Base64 encoding. The output/actual response message will sent from NPCI also will 
be having encoded JSON with embedded XML value for the message. 
Encoded format of request: 
 
{"Source":"S0FSVA==","Service":"R2V0QWNjTm9JbmZv","Type":"UmVxdWVzdA==","Message"=
"PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+PGFjaDpHZ
XRBY2NOb0luZm9ScXN0IHhtbG5zOmFjaD0iaHR0cDovL25wY2kub3JnL2FjaC9zY2hlbWEvIj4KPEhlYWQ
gdHM9IjIwMTctMTAtMTZUMTA6MDI6MDAiIHZlcj0iMS4wIi8+CQo8U291cmNlIG5hbWU9Ikthcm5hdGFrY
SBHb3Z0ICIgdHlwZT0iQ09ERSIgdmFsdWU9IktBUlQiLz4KPERlc3RpbmF0aW9uIG5hbWU9IiIgdHlwZT0
iQ09ERSIgdmFsdWU9IjUwODUwOCIvPgo8UmVxdWVzdCBpZD0iMTIzNDU2Nzg5IiByZWZVcmw9IiIgdHlwZ

<!-- Page 9 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
9 
 
T0iREJUIHwgTk9OX0RCVCIvPgo8UmVxRGF0YT4KPERldGFpbCBGaWxsZXIxPSIiIEZpbGxlcjI9IiIgYWF
kaGFhcj0iTysvb04vS2dxbDhpTnNsanZuUUllaHNyQVE0bGZTSnFlblgrbHFVVHNGZUljY2ZCZXM0YkdaM
mFzNXJCZ1ZRQk1xUjFnZWpCb0dSYXpLVEI3Qy91UWFEYUhrTWRQU1gwejFwNTUwZ0FjTGFtVm0rS1U1clN
yTEZPYnhnWlBQaTRtUVVKd2cxQVNtZWlsOVRxNGZlNnowaFNCK1Y1Wlo5YnFwUlZQaWVGQWk5Tm1mbkRVM
GY1eGdKdVN2cHRiaEIzVjNQWmdQeGxnUzlVNHBhcEplYkZNMkdXU3JvWGoweHdMMTlwTEozbzIybkVvc3Z
0elhVcXNkLzJTMDNaamcySjZTT3p5SUVrSTRZZG1FOUh2OGRpR21XQVZScUpxQVp3QlJmbURZUkpPdm04M
GVPYThZM2kxSE1qbUlqVzR6c3plSlppWno4ZEJPOHBta3FjY2hzek5nPT0iIGFjY05vPSJ2eHBqVTNML3B
KOHViOGQ1MGVvN1FLWnpyZ1JwSEtUMGtBTzBQbUtTa3dCckt2TWJCZ1ZrbWt1Z2JzdktkQXJNK2UzMTFzc
S91cnhkUURhc0p4emN3dUhUVE4xV2lJR0FpNCtlbWtuQ0RmUXlxMG45MFpsTFUyRHlJVm93cVNpS0hINUM
1bXV1bGF6UjNKelZJRHF5dzZXNFdlODBFaTNsak83Q1FBRkNlbDlDYjc2azBqN3V4OU1RbVZMQXlaU2xQb
3lXQzJObXlYYmRvandWcEVaeFRRQTNzY0JQTGZRbStBZCtQb1dXbEg3cGJ1eS9xdXp6UU9NMGpsYVpad2h
WSS80b2doK2ZlbDJ4Tk92OEFqUEpORktwcUFjaXl1WE5idmJBc21RL2dDbys2Q2ZoWlprZFppYVdxSnNJQ
nlFbXBqelFxRnhodnJ2dDF6cTl0YXdTQ0E9PSIgY3VzdENvbnNlbnQ9IlkiLz4KPC9SZXFEYXRhPgkKPE5
wY2lSZWZJZCB2YWx1ZT0iIi8+CjxTaWduYXR1cmUgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvM
DkveG1sZHNpZyMiPjxTaWduZWRJbmZvPjxDYW5vbmljYWxpemF0aW9uTWV0aG9kIEFsZ29yaXRobT0iaHR
0cDovL3d3dy53My5vcmcvVFIvMjAwMS9SRUMteG1sLWMxNG4tMjAwMTAzMTUiLz48U2lnbmF0dXJlTWV0a
G9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxkc2lnLW1vcmUjcnNhLXNoYTI
1NiIvPjxSZWZlcmVuY2UgVVJJPSIiPjxUcmFuc2Zvcm1zPjxUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwO
i8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSIvPjwvVHJhbnNmb3J
tcz48RGlnZXN0TWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxlbmMjc
2hhMjU2Ii8+PERpZ2VzdFZhbHVlPlRmZjdRMCs2bHJrTnRDbUtZZVNBSUM0T3M2SVo4NE4rZ0hUT0UreDR
EZWs9PC9EaWdlc3RWYWx1ZT48L1JlZmVyZW5jZT48L1NpZ25lZEluZm8+PFNpZ25hdHVyZVZhbHVlPk4xS
WVTenordDJCYTZXQXU2ZXM4dkdncXhmVk0xSmU5V3lKdUV3ZHJsdU5CL1BGaE80YmhRTStQS0RsVnI5YjV
tZ096SklBeFdSRUYKaG9qb0YvTmNqWFJ2bHdXNUo4MnhIRjBpd1pKSk5lSVZ2N0Q1Z3Nwdmx4cjlFeWxZd
zlZL0duR1lnTGpsYjVLNG45d2lSbW9mUi9VaAplY052MGFoTG1EaFJyanFrVjRmRHhYdi9lNEJCaXhZanZ
NZUY3R3dXWDBhbFpBdTBYcG1FNmhqMTZidFc4SmlNYVYrT0xCQ2VRbGYyCkVvRDcvV3BkU0Q5VkIvV1Jzd
VRFTjNMVkkyRDdqWE13RDJzTFRVbTlzQ1AwQW11RFJGRmZBSWZKT00zc1J2YUxHSk9acC90Q2ZKQXMKT05
jUlRodkpwdXJ3cGc4OVJSdW11RFlublpoSzFlT1B5SE91SWc9PTwvU2lnbmF0dXJlVmFsdWU+PEtleUluZ
m8+PFg1MDlEYXRhPjxYNTA5U3ViamVjdE5hbWU+Q049Y20ubnBjaS5vcmcuaW4sTz1OYXRpb25hbCBQYXl
tZW50cyBDb3Jwb3JhdGlvbiBvZiBJbmRpYSxMPU11bWJhaSxTVD1NYWhhcmFzaHRyYSxDPUlOLDIuNS40L
jU9IzEzMDYzMTM4MzkzMDM2MzcsMS4zLjYuMS40LjEuMzExLjYwLjIuMS4zPSMxMzAyNDk0ZSwyLjUuNC4
xNT0jMGMxNDUwNzI2OTc2NjE3NDY1MjA0ZjcyNjc2MTZlNjk3YTYxNzQ2OTZmNmU8L1g1MDlTdWJqZWN0T
mFtZT48WDUwOUNlcnRpZmljYXRlPk1JSUZzRENDQkppZ0F3SUJBZ0lRQm5MYkxhMHo3c1VmSUZSczBVMVR
qakFOQmdrcWhraUc5dzBCQVFzRkFEQjFNUXN3Q1FZRFZRUUcKRXdKVlV6RVZNQk1HQTFVRUNoTU1SR2xuY
VVObGNuUWdTVzVqTVJrd0Z3WURWUVFMRXhCM2QzY3VaR2xuYVdObGNuUXVZMjl0TVRRdwpNZ1lEVlFRREV
5dEVhV2RwUTJWeWRDQlRTRUV5SUVWNGRHVnVaR1ZrSUZaaGJHbGtZWFJwYjI0Z1UyVnlkbVZ5SUVOQk1CN
FhEVEl3Ck1ESXdOekF3TURBd01Gb1hEVEl5TURJeE1URXlNREF3TUZvd2djTXhIVEFiQmdOVkJBOE1GRkJ
5YVhaaGRHVWdUM0puWVc1cGVtRjAKYVc5dU1STXdFUVlMS3dZQkJBR0NOendDQVFNVEFrbE9NUTh3RFFZR
FZRUUZFd1l4T0Rrd05qY3hDekFKQmdOVkJBWVRBa2xPTVJRdwpFZ1lEVlFRSUV3dE5ZV2hoY21GemFIUnl
ZVEVQTUEwR0ExVUVCeE1HVFhWdFltRnBNUzh3TFFZRFZRUUtFeVpPWVhScGIyNWhiQ0JRCllYbHRaVzUwY
3lCRGIzSndiM0poZEdsdmJpQnZaaUJKYm1ScFlURVhNQlVHQTFVRUF4TU9ZMjB1Ym5CamFTNXZjbWN1YVc
0d2dnRWkKTUEwR0NTcUdTSWIzRFFFQkFRVUFBNElCRHdBd2dnRUtBb0lCQVFEdVc3eVZEc2lIYUdsajJ1T
XJoS21nVnhNaXNvZ2YvOWN4TVpHYwprTWVKVlluUS9NcjJzbUlpc05lM2VSalM2eVlkTVd3ZW41YWpZaDJ
leGh3RWt5Q01nWFovb3dZTm9NWlBuWkkrYlUwNjRweFROUnlTCmNyNVhpQTlyZFYrczEyc0V2WjhvWDIrd
kdHWUFCRGorcUhLSzd5R1BSaU1VMU9IK1JDaGEwL3dKQmdMZS9LN215cjRrVlBEeGliUmMKZ0tBUXJsMis
3Mmd5VCs2U0NsSklOdzY2cEplUUE4aFkwbk9PV2lWZXM2Q1QyU0FBTm5ZMVdKaW5PWndNSTFQWk1PbWVZW
HYvRVZnMgpIU05lRjA5elZaRGMxdmZ4TWtXWnQ0dFhBNnpqcmhjMkFORzlqdTRHcGxQLzFzYU9SSUliUVZ
TODgycEFNLzNlQjBRUHo4MVhRaDI5CkFnTUJBQUdqZ2dIck1JSUI1ekFmQmdOVkhTTUVHREFXZ0JROTAxQ
2wxcUN0N3ZOS1lBcGwweUhVK1BqV0R6QWRCZ05WSFE0RUZnUVUKc05vdyt6WlRyTUhLd2pLcUF3L05rY09
vVis4d0dRWURWUjBSQkJJd0VJSU9ZMjB1Ym5CamFTNXZjbWN1YVc0d0RnWURWUjBQQVFILwpCQVFEQWdXZ
01CMEdBMVVkSlFRV01CUUdDQ3NHQVFVRkJ3TUJCZ2dyQmdFRkJRY0RBakIxQmdOVkhSOEViakJzTURTZ01
xQXdoaTVvCmRIUndPaTh2WTNKc015NWthV2RwWTJWeWRDNWpiMjB2YzJoaE1pMWxkaTF6WlhKMlpYSXRae
kl1WTNKc01EU2dNcUF3aGk1b2RIUncKT2k4dlkzSnNOQzVrYVdkcFkyVnlkQzVqYjIwdmMyaGhNaTFsZGk
xelpYSjJaWEl0WnpJdVkzSnNNRXNHQTFVZElBUkVNRUl3TndZSgpZSVpJQVliOWJBSUJNQ293S0FZSUt3W
UJCUVVIQWdFV0hHaDBkSEJ6T2k4dmQzZDNMbVJwWjJsalpYSjBMbU52YlM5RFVGTXdCd1lGClo0RU1BUUV

<!-- Page 10 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
10 
 
3Z1lnR0NDc0dBUVVGQndFQkJId3dlakFrQmdnckJnRUZCUWN3QVlZWWFIUjBjRG92TDI5amMzQXVaR2xuY
VdObGNuUXUKWTI5dE1GSUdDQ3NHQVFVRkJ6QUNoa1pvZEhSd09pOHZZMkZqWlhKMGN5NWthV2RwWTJWeWR
DNWpiMjB2UkdsbmFVTmxjblJUU0VFeQpSWGgwWlc1a1pXUldZV3hwWkdGMGFXOXVVMlZ5ZG1WeVEwRXVZM
0owTUF3R0ExVWRFd0VCL3dRQ01BQXdEUVlKS29aSWh2Y05BUUVMCkJRQURnZ0VCQUxXSmZwODlLRnVENkd
yZlJYeTltYzFTOGdZTS9uZFRBZkg1c3ZTUTBLNVRyRlJZamlqZVoydVRycHA1dFZUM1NJMlMKSTU5VHVaO
WlBSkNjR0FkcGdpNXhXczhGMCtndUlaYm4wd3pMQVZmSUtaeU1OQ1RSNmJGZzRITXFyS3RaZ1poL1pZaFR
nU1lEeE9YUAp6ZUl6SWRpZTluaEgxcHpZN2pITnJMZlNpL2VjUUtZVG9KcFRlOVM4YWFLVnpPSGt4Y3BHT
lJqS09TdXZKRkVZcDdPK0haVlV1ckZ3CktJOXVlUi94c1BLd3pMcUdrM05IWmF4cXJrcUU1MGxHV2k5M0l
EOUIxMjYzUUFhUE1GUEMrbEtPa3RnVUczcGYvZVZnQU5TdStnZW8KT2dTRzlobUp5Vno3YjEzSk5jY1Bxe
jgrUTd4VjVPNHFhcWtQMlZWUDJxMGl0eWM9PC9YNTA5Q2VydGlmaWNhdGU+PC9YNTA5RGF0YT48L0tleUl
uZm8+PC9TaWduYXR1cmU+PC9hY2g6R2V0QWNjTm9JbmZvUnFzdD4="} 
 
While sending the response as a destination party will do encryption of PII data(Aadhaar No/Acc No) 
and signing of XML & base64 encoding. 
 
2.6 Encryption and Signing process 
 
Below is the process for encryption during the various flows.  
 Source to NPCI 
 Encryption will be done using the public key of the certificate shared by NPCI.  
 Signing Using Private key certificate of the Source Bank 
 NPCI to Source 
 Encryption will be done using the Public Key of the certificate shared by the Source bank.  
 Signing Using Private key certificate of NPCI 
Aadhaar number , Account number attribute should be encrypted in all the request and response 
messages   
 
3. API Protocol 
 
API is exposed as stateless service over HTTPS. Usage of open data format in XML and 
widely used protocol such as HTTP allows easy adoption by the members.  
API input data should be sent to the following URL as JSON content using Content-Type as 
“text/plain”. It processed in Asynchronous manner. 
 
URL format: 
 
https://<host>/endpointcontextpath  
host – API server address (Actual production server address will be provided at the time of 
rollout and all API clients should ensure that actual URL is configurable).  
endpointcontextpath -the end point context path for the API

<!-- Page 11 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
11 
 
Common URL format for the API to reach NPCI API system from 
Bank/Corporate(Incoming) 
 
URL format of API: https://<host>/apiGatewayListener 
 
While NPCI Calling the Bank/Corporate server they can choose the below URL 
format.(Out going) 
 
URL format of API: https://<host>/apiGatewayListener 
 
 
3.1 Flow Diagram: 
 
 
 
1. Sender bank initiates the JSON request to NPCI system, NPCI performs initial 
validations and send the XML ACK with http response 200 and the connection will 
get close with bank later then NPCI proceeds for technical/business validations. 
2. If technical/business validations are passed then NPCI establishes the 
connection with receiver bank for forwarding the request to them, when the 
request has been accepted for processing, receiver bank server MUST return a http 
202 Accepted status code to NPCI, then the connection will get close with receiver 
bank. 
3. For sending the response to NPCI, receiver bank should establish a new 
connection. After receiving NPCI will perform the validations for the response if 
the response passed all the validations receiver bank will receive http 200 status 
code else XML error notification will be sent. 
4.NPCI establish the new connection with source bank and send the response, 
when the response has been accepted by source then bank server MUST return a 
http 202 Accepted status code to NPCI.

<!-- Page 12 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
12 
 
5.If receiver bank not provided with the response with in the defined SLA time, the 
NPCI will construct the failure response and establishes a new connection with 
source bank and send the failure response, when the response has been accepted 
by source then bank server MUST return a http 202 Accepted status code to NPCI. 
Note : Receiver bank should provide the response with in the SLA time else the 
request will be deemed declined by NPCI. 
 
3.1 Obtaining/Get Linkage Status of Account number for the given 
Aadhaar Number 
 
This API is initiated by Source Banks to know the linkage status of account number for the 
given aadhaar number.  
Upon receivable of the message from source, NACH –API Cloud system acknowledges the 
request to source bank by sending either ACCEPTED or ERROR. After successful validation of 
NACH – API cloud system passes the message to destination Banks based on the registered 
URL of destination Bank.  
1. Input data:  
i. Aadhaar number  
ii. Destination bank code(eg: 508508) 
iii. Account number 
iv. Customer Consent 
v. Filler 1 
vi. Filler 2 
Responding entity: Bank 
Response to be provided:  
1. Aadhaar Linkage Status (Y or N) 
2. Account status  
3. Subsidy Account Flag( Y or N) 
4. Account Number (only last 4 digits) 
5. Account type  
 
Request Message Format 
{"Source ": "KART " 
"Service ": "GetAccNoInfo " 
"Type "    : "Request " 
"Message ":  
"<ach:GetAccNoInfoRqst xmlns:ach="http://npci.org/ach/schema/" > 
<Head ver="1.0" ts="2017-10-16T10:02:00" /> 
 
<Source type="CODE" value="KART" name="Karnataka Govt " /> 
<Destination type="CODE" value="508508" name="" /> 
<Request id="123456789" type="DBT | NON_DBT" refUrl=""/> 
<ReqData> 
<Detail aadhaar="234567890123" accNo="56475648900909" custConsent="Y" filler1="" 
filler2="" /> 
 
 
</ReqData> 
 
<NpciRefId value=""/>

<!-- Page 13 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
13 
 
</ach:GetAccNoInfoRqst> "} 
 
Index 
Message Item 
<XML Tag> 
Occurrence 
1.1 
API Name 
<ach> 
1..1 
1.1.1 
API Schema namespace 
xmlns 
1..1 
2.1 
Header for the message 
<Head> 
1..1 
2.1.1 
Version of the API 
ver 
1..1 
2.1.2 
Time of request from the creator of the message 
(Transmission time) 
ts 
1..1 
3.1 
Source of the message 
<Source> 
1..1 
3.1.1 
Routing type of the Source banks – based on short 
code of the bank the corresponding URL will be 
identified  
type 
1..1 
3.1.2 
Actual value of the routing type 
value 
1..1 
3.1.3 
Name of the Source Bank 
name 
0..1 
4.1 
Destination of the message 
<Destination> 
1..1 
4.1.1 
Routing type of the Source banks – based on short 
code of the bank the corresponding URL will be 
identified  
type 
1..1 
4.1.2 
Actual value of the routing type* 
value 
0..1 
4.1.3 
Name of the Destination Bank 
name 
0..1 
5.1 
Request Message property 
<Request> 
1..1 
5.1.1 
Id of the Request generated by the originator 
Id 
1..1 
5.1.2 
Type of the request. Ie indication of DBT or 
NON_DBT enquiry 
Type 
1..1 
5.1.3 
Reference URL for the transaction  
refUrl 
0..1 
6.1 
input data related to the request 
<ReqData> 
1..1 
6.2 
Details of the Input parameters of the request 
<Details> 
1..1 
6.2.1 
Parameter of the request – Account Number  
accNo 
0..1 
6.2.2 
Parameter of the request – Aadhaar Number  
aadhaar 
1..1 
6.2.3 
Parameter of the request – Customer Consent  
custConsent 
0..1 
6.2.4 
Parameter of the request – Filler 1 – should be left 
blank  
filler1 
1..1 
6.2.5 
Parameter of the request – Filler 2 – should be left 
blank 
filler2 
1..1 
7.1 
Unique Identified assigned by NPCI for the request 
<NpciRefId> 
0..1 
7.1.1 
Actual unique value generated by NPCI 
Value 
0..1 
 
* This field is conditional mandatory when Account Number is provided

<!-- Page 14 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
14 
 
 
Response Message Format 
{"Source ": "SYND" 
"Service ": "GetAccNoInfo" 
"Type "    : "Response" 
"Message: " 
<ach:GetAccNoInfoResp xmlns:ach="http://npci.org/ach/schema/"> 
<Head ver="1.0" ts="2017-10-16T10:02:15" > 
 
 
<Source type="CODE" value="KART" name="Karnataka Govt " /> 
 
<Destination type="CODE" value="508508" name="" /> 
 
<Request id="123456789" type="DBT | NON_DBT" refUrl=""/> 
 
<Resp ts="2017-10-16T10:02:15" result="SUCCESS" errCode="" rejectedBy="" /> 
 
<RespData> 
 
<Detail linkStatus="Y" status="S601" subsidyAccFlag="Y" accNo="7384" 
type="T659" filler1="" filler2="" filler3="" filler4="" filler5="" /> 
 
 
 
</RespData> 
 
<NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa" /> 
</ach:GetAccNoInfoResp> "} 
 
 
Index 
Message Item 
<XML Tag> 
Occurrence 
1.1 
API Name 
<ach> 
1..1 
1.1.1 
API Schema namespace 
xmlns 
1..1 
2.1 
Header for the message 
<Head> 
1..1 
2.1.1 
Version of the API 
ver 
1..1 
2.1.2 
Time of request from the creator of the message 
(Transmission time) 
ts 
1..1 
3.1 
Source of the message 
<Source> 
1..1 
3.1.1 
Routing type of the Source banks – based on short code 
of the bank the corresponding URL will be identified  
type 
1..1 
3.1.2 
Actual value of the routing type 
value 
1..1 
3.1.3 
Name of the Source Bank 
name 
0..1 
4.1 
Destination of the message 
<Destination> 
1..1 
4.1.1 
Routing type of the Source banks – based on short code 
of the bank the corresponding URL will be identified  
type 
1..1 
4.1.2 
Actual value of the routing type 
value 
1..1 
4.1.3 
Name of the Destination Bank 
name 
0..1 
5.1 
Request Message property 
<Request> 
1..1 
5.1.1 
Id of the Request generated by the originator 
Id 
1..1 
5.1.2 
Type of the request. Ie indication of DBT or NON_DBT 
enquiry 
Type 
1..1 
5.1.3 
Reference URL for the transaction  
refUrl 
0..1 
6.1 
Unique Identified assigned by NPCI for the request 
<NpciRefId> 
1..1

<!-- Page 15 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
15 
 
Index 
Message Item 
<XML Tag> 
Occurrence 
6.1.1 
Actual unique value generated by NPCI 
value 
1..1 
7.1 
Response of the Message 
<Resp> 
1..1 
7.1.1 
Time of response from the sender of the message  
ts 
1..1 
7.1.2 
Result of the request 
result 
1..1 
7.1.3 
Error reason codes for the failure message 
errCode 
0..1 
7.1.4 
Actual rejecter of the message. NPCI or Destination who 
rejected the message 
rejectedBy 
0..1 
8.1 
Response Data 
<RespData> 
0..1 
8.2 
Details of the given aadhaar 
< Detail> 
0..1 
8.2.1 
Parameter – Aadhaar linkage status 
linkStatus 
1..1 
8.2.2 
Parameter –  Account status 
Status 
1..1 
8.2.3 
Parameter - subsidyAccFlag of the the primary account* 
subsidyAccFlag 
0..1 
8.2.4 
Parameter - Account Number 
accNo 
0..1 
8.2.5 
Parameter – account type* 
Type 
0..1 
8.2.6 
Parameter of the request – Filler 1 – should be left blank 
filler1 
0..1 
8.2.7 
Parameter of the request – Filler 2 – should be left blank 
filler2 
0..1 
8.2.8 
Parameter of the request – Filler 3 – should be left blank 
filler3 
0..1 
8.2.9 
Parameter of the request – Filler 4 – should be left blank 
filler4 
0..1 
8.2.10 
Parameter of the request – Filler 5 – should be left blank 
filler5 
0..1 
 
* subsidyAccFlag of the primary account is conditional mandatory when Aadhaar linkage status is Y. 
*account type is conditional mandatory when Aadhaar linkage status is Y.

<!-- Page 16 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
16 
 
3.2 General ACK/NACK Message format 
 
ACK/NACK will be a HTTP Response with below XML body. 
<ach:GatewayAck xmlns:ach="http://npci.org/ach/schema/" > 
 <NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa"/> 
 <Resp ts="2017-10-16 10:02:00" result="ACCEPTED" errCode="" rejectedBy="" />  
</ach:GatewayAck> 
 
Index 
Message Item 
<XML Tag> 
Occurrence 
1.1 
API Name 
<ach> 
1..1 
1.1.1 
API Schema namespace 
xmlns 
1..1 
2.1 
Unique Identified assigned by NPCI for the request 
<NpciRefId> 
1..1 
2.1.1 
Actual unique value generated by NPCI 
value 
1..1 
3.1 
Response of the Message 
<Resp> 
1..1 
3.1.1 
Time of response from the sender of the message  
ts 
1..1 
3.1.2 
Result of the request 
result 
1..1 
3.1.3 
Error reason codes for the failure message 
errCode 
0..1 
3.1.4 
Actual rejecter of the message. NPCI or Destination who 
rejected the message 
rejectedBy 
0..1 
 
Note: 
 This Acknowledgement will follow single root element of type GatewayAck for all 
type of request and response  
 In case of Request Message, new NpciRefID will be generated and shared along with 
Resp 
 Irrespective of success or failure scenarios at Gateway level, the NpciRefId will be 
generated for Request and shared 
 For Response Type, the NpciRefID will be empty for both success and failure 
scenarios 
 
 
3.3 Destination Asynchronous Failure Response Message format 
 
Source  : NPCI 
Service : GetPanDtls 
Type    : ErrorNote 
Message :<ach:DestErrorNotification xmlns:ach="http://npci.org/ach/schema/"> 
 
  <NpciRefId value="6afd4578-f021-4321-a908-04b355a758fa" /> 
  <Resp ts="2017-10-16T10:02:26" result="ERROR" errCode="245"     
   rejectedBy="NPCI" />

<!-- Page 17 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
17 
 
 
 </ach:DestErrorNotification> 
 
Index 
Message Item 
<XML Tag> 
Occurrence 
1.1 
API Name 
<ach> 
1..1 
1.1.1 
API Schema namespace 
xmlns 
1..1 
2.1 
Unique Identified assigned by NPCI for the request 
<NpciRefId> 
1..1 
2.1.1 
Actual unique value generated by NPCI 
value 
1..1 
3.1 
Response of the Message 
<Resp> 
1..1 
3.1.1 
Time of response from the sender of the message  
ts 
1..1 
3.1.2 
Result of the request 
result 
1..1 
3.1.3 
Error reason codes for the failure message 
errCode 
0..1 
3.1.4 
Actual rejecter of the message. NPCI or Destination who 
rejected the message 
rejectedBy 
0..1 
 
Note: 
 Any failure found in technical or business validation of Response message will 
trigger this notification  
 Only for failure scenarios, the Destination bank will receive this notification 
 
 
3.4 Elements and Attributes Definition 
Element: Root  
Definition:  XML root element representing each API (GetAccNoInfoRqst) 
 
Attribute: xmlns 
Definition:  API Schema Namespace. 
Data Type: 
Alphanumeric 
Format:     
Min Length:   1 
                
Max Length:  255 
 
Element: <Head> 
Definition:  Header of the Message 
 
Attribute: ver

<!-- Page 18 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
18 
 
Definition:   Version of the API 
This is the API version. NPCI may host multiple versions for supporting 
gradual migration. As of this specification, default production version is 
"1.0". 
Data Type: 
Float 
Format:     
Min Length:   1 (length is not checked as version should be “1.0”) 
                
Max Length:  6 
 
Attribute: ts 
Definition:   Time of request from the creator of the message. API request time stamp. 
Since timestamp plays a critical role, it is highly recommended that devices are time 
synchronized with a time server. 
Data Type: 
ISODateTime 
Format:     
Min Length: 19 
Max Length: 19  
                
YYYY-MM-DDThh:mm:ss 
                
(eg 1997-07-16T19:20:30) 
where; 
  
YYYY = Four-digit year 
  
MM = Two-digit month (01=January, etc.) 
  
DD = Two-digit day of month (01 through 31) 
  
hh = Two digits of hour (00 through 23) (am/pm NOT allowed) 
  
mm = Ttwo digits of minute (00 through 59) 
  
ss  = Two digits of second (00 through 59) 
Element: <Request> 
Definition:  This element contains the Request details and is visible to all parties involved 
in the transaction processing. This element is populated by the originator of the 
request and the same must be passed across all the entities. 
  
Attribute: id 
Definition:  Unique Identifier for the request across all entities. This will be created by 
the originator. This field along with source element’s value attribute will be used to 
identify each request uniquely across all the entities.  
Data Type: 
Alphanumeric

<!-- Page 19 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
19 
 
Format:     
Min Length:   1 
                
Max Length:  22 
Attribute: refUrl 
Definition: URL for the transaction 
Data Type: 
Alphanumeric with special characters  
Format:     
Min Length:   1 
                
Max Length:  35 
Attribute: type 
Definition:  This attribute describes the type of the Request 
Data Type: 
Enumeration or Code. Length check is not there as it should be in the list of 
prescribed types. The allowed values are “DBT” or “NON_DBT” as per the registration of 
the participant at the time of on-boarding. 
Format:     
Min Length:   NA 
                
Max Length:  NA 
 
Element: <Source> 
Definition:  This element contains the details of the originator of the request and the 
same must be passed across all the entities.  
Attribute: type 
Definition:  This indicates the routing type to be used. Currently allowed routing type is 
only Bank short code and it should be always ‘CODE’. Length check will not be done as it 
should be always CODE 
Data Type: 
Alpha 
Format:     
Min Length:   NA 
                
Max Length:  NA 
Attribute: value  
Definition:  This attribute contains the actual value of the routing type and this value will 
be used to identify the endpoint URL of the participant which is used to initiate any 
communication from NPCI 
Data Type: 
Alpha 
Format:     
Min Length:   4 
                
Max Length:  4 
Attribute: name 
Definition:  This attribute carries the name of the Source.

<!-- Page 20 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
20 
 
Data Type: 
Alphabets with special characters like dot, space, hyphen & single quote 
Format:     
Min Length:   0 
                
Max Length:  100 
Element: <Destination> 
Definition:  This element contains the details of the originator of the request and the 
same must be passed across all the entities.  
Attribute: type 
Definition:  This indicates the routing type to be used. Currently allowed routing type is 
only Bank short code and it should be always ‘CODE’. Length check will not be done as it 
should be always CODE 
Data Type: 
Alpha 
Format:     
Min Length:   NA 
                
Max Length:  NA 
Attribute: value  
Definition:  This attribute contains the actual value of the routing type and this value will 
be used to identify the endpoint URL of the participant which is used to initiate any 
communication from NPCI 
Data Type: 
Numeric ( IIN of Destination bank code) 
Format:     
Min Length:   6 
                
Max Length:  6 
Attribute: name 
Definition:  This attribute carries the name of the destination.  
Data Type: 
Alphabets with special characters like dot, space, hyphen & single quote 
Format:     
Min Length:   0 
                
Max Length:  100 
Element: <Detail> 
Definition:  This element contains the parameters of the actual request and the same 
must be passed to Destination for processing.  
Attribute: accNo 
Definition:  Few of the request is based on this parameter value. And this attribute carries 
the account number in request. 
In response the accno should be provided only last 4 digits, this will be mandatory if 
account is available in bank CBS.   
Data Type: 
Numeric

<!-- Page 21 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
21 
 
Format:     
Min Length:   1 
                
Max Length:  35 
Attribute: aadhaar 
Definition:  The request is based on this parameter value. And this attribute carries the 
Aadhaar number value.  
Data Type: 
Numeric 
Format:     
Min Length:   12 
                
Max Length:  12 
Note: Apart from length and numeric pattern, it will be validated to ensure that it is not 
begin with “0” or “1” and it is as per verhoeff algorithm. 
Attribute: custConsent 
Definition:  To provide the customer consent on this parameter value.  
Data Type: 
Alpha 
Format:     
Min Length:   1 
                
Max Length:  1 
Values may be Y/N 
Atribute: filler1/ filler2/ filler3/ filler4/ filler5 
Definition:  for the use of future purpose in both request and response. It should be left 
blank  
Data Type: 
Alphanum 
Format:     
Min Length:   1 
                
Max Length:  50 
Element: <Resp> 
Definition:  This element contains the information about the Response. 
 
Attribute: ts 
Definition:   Time of request from the creator of the message. 
API request time stamp. Since timestamp plays a critical role, it is highly 
recommended that devices are time synchronized with a time server. 
Data Type: 
ISODateTime 
Format:     
Min Length: 19 
Max Length: 19

<!-- Page 22 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
22 
 
                
YYYY-MM-DDThh:mm:ss 
                
(eg 1997-07-16T19:20:30) 
where; 
  
YYYY = Four-digit year 
  
MM = Two-digit month (01=January, etc.) 
  
DD = Two-digit day of month (01 through 31) 
  
hh = Two digits of hour (00 through 23) (am/pm NOT allowed) 
  
mm = Ttwo digits of minute (00 through 59) 
  
ss  = Two digits of second (00 through 59) 
Attribute: result 
Definition:  This attribute is used to indicate the end result of the requested message. 
And it should have the any one of the value from the pre-defined list. 
Data Type: 
Code  
Format:     
Min Length:   NA 
                
Max Length:  NA 
 
 
 
 
Attribute: rejectedBy 
Definition:  This attribute is used to indicate the source of rejection in case of failure. 
And it should have the any one of the value from the pre-defined list. 
Data Type: 
Code  
Format:     
Min Length:   NA 
                
Max Length:  NA 
 
Attribute: errCode 
Definition:  This attribute is used to indicate the reasons for rejection in case of failure.  
Or the status code in case of success And it should have the one or many values from the 
pre-defined list. Multiple error codes will be separated by comma. 
Data Type: 
Code  
Format:     
Min Length:   NA 
                
Max Length:  NA 
Code 
Value 
SUCCESS 
Request message is Successfully processed 
FAILURE 
Request has been rejected either by NPCI or DEST

<!-- Page 23 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
23 
 
Attribute: status 
Definition:  This attribute provides the any one of predefined account status. This field is 
mandatory. Only below status codes are allowed. 
Data Type: 
Code  
Format:     
Min Length:   NA 
                
Max Length:  NA 
Code  Value 
S601 
Account is in open and active state 
S602 
Account under litigation 
S603 
A/c inactive (No Transactions for last 3 Months) 
S604 
Dormant A/c (No Transactions for last 6 Months) 
S605 
Account holder expired 
S606 
A/c blocked or frozen 
S607 
Customer insolvent / insane 
S608 
Account Closed 
S609 
No such Account 
S610 
KYC Documents Pending 
S613 
A/c in Zero balance/No transactions have happened 
Attribute: linkStatus 
Definition:  This attribute is used to indicate the linkage status of the account for the 
given aadhaar number. This field is mandatory. Values allowed are Y or N 
Data Type: 
Code  
Format:     
Min Length:   NA 
                
Max Length:  NA 
Attribute: subsidyAccFlag 
Definition:  This attribute is used to indicate Is this primary account for receiving subsidy 
through Aadhaar based for the given aadhaar number. This field is mandatory for the 
Account Status Flag is other than "no such account ". Values allowed are Y or N 
If LinkStatus is  "Y" – then it can be either "Y" or "N" 
If LinkStatus is  "N" - it should be only "N" 
Data Type: 
Code  
Format:     
Min Length:   NA 
                
Max Length:  NA 
Attribute: type  
Definition:  This attribute provides the any one of predefined account type. Only below 
codes are allowed. This field is mandatory for the Account Status Flag is other than "no 
such account ". 
If subsidyAccFlag is Y system will allow only these codes T651,T659, T663,T658.

<!-- Page 24 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
24 
 
If subsidyAccFlag is N system will allow below all the codes. 
Data Type: 
Code 
Format:     
Min Length:   NA 
                
Max Length:  NA 
Code Value 
T651 
Savings account 
T652 
Current account 
T653 
Cash credit account 
T654 
Overdraft account 
T656 
FD 
T657 
RD 
T658 
Loan account 
T659 
PMJDY account 
T660 
NRE/NRO account 
T661 
HUF - Hindu Undivided family 
T662 
PF & PPF 
T663 
Basic Savings Bank Deposit (BSBD) 
 
Attribute: NpcirefId 
Definition:  This attribute is used to indicate the uniqueness for the each request which 
will be generated by the NPCI only. In the request this attribute value should be kept 
blank by source banks and in the response destination bank should provide the exact value 
which they have received in the request file  
Data Type: 
Code  
Format:     
Min Length:   1 
                
Max Length:  36

<!-- Page 25 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
25 
 
4. Error Codes 
 
4.1 Technical Validation Error Codes 
 
Error Code 
Error Description 
101 
Incorrect Request 
102 
Source Is Missing 
103 
Service Is Missing 
104 
Service Type is Missing 
105 
Message is Missing 
106 
Error in Verification - No Signature Tag Found 
107 
Error in Verification - Incorrect Signature Method Algorithm Used 
108 
Error in Verification - Incorrect Digest Method 
109 
Error in Verification - No Matching Certificate Available 
110 
Error in Verification - Signature is Invalid 
111 
Type should be either Request or Response 
112 
Dependency Failed; Unable to publish the Message in Queue 
113 
Error in DB connectivity 
114 
Message is not in correct format 
115 
Head Tag is Mandatory 
116 
Source Tag is Mandatory 
117 
Destination Tag is Mandatory 
118 
Request Tag is Mandatory 
119 
ReqData Tag is Mandatory 
120 
Detail Tag is Mandatory 
121 
NpciRefId Tag is Mandatory 
122 
Resp Tag is Mandatory 
123 
RespData Tag is Mandatory 
124 
Aadhaar Tag is Mandatory 
125 
AccountHolderList Tag is Mandatory 
128 
AccHolder Tag is Mandatory 
129 
Account Tag is Mandatory 
130 
One Or More Attribute is Missing for Head Tag 
131 
One Or More Attribute is Missing for Source Tag 
132 
One Or More Attribute is Missing for Destination Tag 
133 
One Or More Attribute is Missing for Request Tag 
134 
One Or More Attribute is Missing for Detail Tag 
135 
One Or More Attribute is Missing for NpciRefID Tag 
136 
One Or More Attribute is Missing for Resp Tag 
141 
Attribute Timestamp is Invalid 
142 
Attribute Version is Invalid 
143 
Attribute Code is Invalid 
144 
Attribute Value is Invalid 
145 
Attribute Name is Invalid

<!-- Page 26 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
26 
 
Error Code 
Error Description 
146 
Attribute ID is Invalid 
147 
Attribute Type is Invalid 
148 
Attribute RefUrl is Invalid 
149 
Attribute Result is Invalid 
150 
Attribute ErrCode is Invalid 
151 
Attribute RejectedBy is Invalid 
153 
Attribute Status is Invalid 
156 
Attribute accNo is Invalid 
159 
Attribute Type is Invalid 
160 
Attribute Status is Invalid 
162 
Attribute Value is Invalid 
163 
Decryption Failed for Aadhaar field 
164 
Decryption Failed for AccountNo field 
166 
Attribute Type of Destination Tag is Invalid 
167 
Attribute Value of Destination Tag is Invalid 
168 
Attribute Name of Destination Tag is Invalid 
169 
Attribute Timestamp of Resp Tag is Invalid 
170 
Attribute Name of AccHolder Tag is Invalid 
178 
Incorrect Message Type. Only Request is Allowed for Internal category 
161 
Attribute linkStatus is Invalid 
260 
Attribute subsidyAccFlag is invalid 
261 
Attribute custConsent is invalid 
262 
Attribute accNo value in response should be only last 4 digits 
263 
Attribute filler1 is invalid 
264 
Attribute filler2 is invalid 
265 
Attribute filler3 is invalid 
266 
Attribute filler4 is invalid 
267 
Attribute filler5 is invalid 
268 
Attribute Status of Aadhaar Tag is Invalid 
269 
Attribute Type of Aadhaar Tag is Invalid

<!-- Page 27 -->

 
                                                                                                                          
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
27 
 
4.2  Business Validation Error Codes 
 
Error Code 
Error Description 
201 
Service Name is Invalid or It Is Not Active 
202 
Source is NOT valid participant. I.e. Not Available in DB 
203 
Source is NOT active 
204 
Source is NOT having privilege for the service 
205 
Header Timestamp should not be future Timestamp 
206 
Header Timestamp should not be older than 24 Hours 
207 
Response Timestamp should not be future time  
208 
Response Timestamp should not be older than 24 Hours 
209 
Time difference between Response Received Time and Request Publish Time should 
not be more than SLA 
210 
 NpciRefID should be valid and should have valid matching record - Invalid NpciRefId 
211 
Late Resposne; Request is NOT in pending state 
212 
Source Value Is Not Match with Request Message 
213 
Destination Value is NOT matching with Request Message 
214 
Error Code is not part of Defined Destination Reject Reason List 
215 
Destination is NOT reachable 
216 
Destination sent Invalid/Incomplete Response 
217 
Destination Did not send Response with in SLA 
218 
Message Source is Not matching with the value of Source Tag 
219 
Message Source is Not matching with the value of Destination Tag 
220 
Invalid Destination. I.e. Destination is NOT available In DB 
221 
Destination is NOT active 
222 
The request is Duplicate. The fields "Source Code Value" and "Request Id" should be 
unique for each service. Ie The combination "Source Code Value + Request Id + 
Service" is unique  
223 
Request Tag of Response Message is not Matching with original request 
225 
Earlier Response 
270 
Request type is not mapped to Source corporate 
 
Note: All these technical & business validation error codes will be send by NPCI system only to 
sender/receiver banks.
