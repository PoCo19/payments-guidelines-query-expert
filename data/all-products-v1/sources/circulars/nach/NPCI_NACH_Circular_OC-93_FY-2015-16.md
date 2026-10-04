# Circular No.93 - Technical Specifications - API for OD Under PMJD

Circular/reference number: NPCI/NACH/2014-15/CircutarNo.93

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NACH/2014-15/CircutarNo.93
March11,2015
To
AllNACHMemberBanks
Technical specifications-APIforOD underPMJDY
This has reference to our circular no 87 dated February 12, 2015 regarding facility to check
the OD flag through NACH application, additionally now wehave modified the APi given to the
member banks to provide the OD flag and OD date in addition to Aadhaar mapping status.
Now the banks can view the Aadhaar status along with OD status using the following options
1,NACHapplication-usethefollowingoption
a.Bank MIS
i.Aadhaar Status
2.ByIntegratingtheAPIprovidedbyNPCI
a.Technical specification document is provided as AnnexureI
Further to the above we advise the member banks to follow the below process for managing
OD flag viewing and updation.
1.OD flag in the Aadhaar mapper should be updated only in case of OD sanctioned under
PMJDY scheme.
2.Banks should not updateNon-PMJDYOD facilityin NPCIMapper
3..At the time of evaluating the OD proposal the banks shoutd first check the OD flag in
the mapper through any one of the options provided above.
4. If Aadhaar is not present in the mapper or in inactive stage or the OD flag is already
"y"then such proposal should not be considered for OD facility under PMJDY.
5. If Aadhaar number is not present or inactive the bank may choose to upload the
Aadhaar number in NpCImapper and proceedwith sanctionof OD.However in caseOD
flag is "y"bank will not be able to update the NpCl mapper.
6. On sanctioning the OD before disbursement the bank should upload the OD status in
mapper and confirm that such updation has indeed taken place.
7. Only post confirmation of OD being marked in NPCI mapper bank should proceed to
release the funds.
C-9, 8th Floor -r/Phone:02226573150
RBIPremises 1Fax:02226571001
Bandra-Kurla Complex 专-a/emall:contact@npci.org.in
Bandra East aqensc/Website:www.npci.org.in
-400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Member banks are reguested to take note and ensure strict adherence to the process to avoid
ODbeingsanctionedtothesamecustomerinmultiolebanks.
Please refer to our Circular No.67 dated December 05,2014member banks should take
note that OD flag updation is possible only through new mapper format.Banks should
contemplate sanctioning OD facility under PMJDY only if they are live with new mapper
format.
For all the circulars please visit our website:npci.org.in
With Warm Regards
(Giridhar G.M)
Vp&HeadCTSandNACHOperations
Encl:
1.Technical specification DocumentforAadhaarLookupusingweb serviceversion
1.1
2.Annexure 1-Samplerequest&response
3.Annexure2-wsdlfiles

<!-- Page 3 -->

NPCT NATIONALPAYMENTSCORPORATKOINOFINDIA TSD:AadhaarLookupusingWebService
NATIONALAUTOMATEDCLEARINGHOUSE
Technical Specification Document for
AadhaarLookupusing WebService
Version 1.1
March11,2015
Page 1 of 10

<!-- Page 4 -->

NPCI NATONALPAYMENTSCORPORATION OFINOIA TSD:AadhaarLookup using Web Service
Technical Specification Document (TSD)
Document Details
Version No. Date Description
1.0 04-12-2014 AadhaarLookupusingHTTPsDocument
1.1 10-03-2015 Added ODflag,MandateFlag,ODDate &MandateDate
Prepared By
Version Date Name&Position Signature
1.0 04-12-2014 PradeepKumarReddy,Officer
1.1 10-03-2015 PradeepKumarReddy,Officer
Reviewedby
Version Date Name&Position Signature
1.0 04-12-2014 Vikas Sharma,Manager
1.1 11-03-2015 Vikas Sharma,Manager
Approvedby
Version Date Name&Position Signature
1.0 04-12-2014 NeerajChoudhary,AvP
1.1 11-03-2015 Neeraj Choudhary,AvP
TOMATEOOL Page 2 of 10

<!-- Page 5 -->

NATIONALFAYMENTSCORPORATIONOFIHDA TSD:Aadhaar Lookup using Web Service
Contents
Contents
1. Introduction.
2. Proposed Solution.
3. Approach.
4. RequestandResponseformat
5. ProcessFlow.
6. Annexure
7. Requirements at ClientSide:.
8. Support. 10
NAH
CATIONALAUTOMATED CLEARINGHDUST Page3of 10

<!-- Page 6 -->

NPCi NANONALPAYMENISCORPORATION CF INDIA TSD:Aadhaar Lookup using Web Service
1.Introduction
The purpose of this document is to provide details on Aadhaar Mapper web service. This
Aadhaarmapper web service will provide the status of customer's Aadhaarnumber along with
hasbeenbuiltforBankuser'susageonly.
2.Proposed Solution
The solution uses web service APl where in the Service gets requested with Aadhaar No,
mobileno,requestno,andrequestDate&Time.
BasedontheRequest,Responsewill beprovidedback tothe stakeHolderasbelow.
i. Aadhaar number
Bank Name
Error
iv. LastUpdateDate
MandateCustomerDate
vi. MandateFlag
vi. MobileNumber
viii. OD Flag
ODDate
X. Processed Date Time
xi. Request No
xii. RequestReceivedtime
xii. RequestedDateTime
xiv. Aadhaar Status
HONALAUTOMATEDCLEARRNHOU Page 4 of 10

<!-- Page 7 -->

NPCi NATIONALPAYMENTSCORPORATION OFINCIA TSD:AadhaarLookupusingWebService
3.Approach
The HTTPs request alongwith the SOAP request containing the Request Number,Aadhaar
Number, Mobile Number, Request date and time will be sent from Bank platform. The
request will reach exposed APl, which in turn queries the Mapper database and the
required values, will be Fetched and sent back to the Bank platform. The exposed APl
willberestrictedbasedonIP/Port.
ATIONALAUTOMATEDCLEARINGHOUSE Page5of10

<!-- Page 8 -->

NPA NATIONALPAYMENTSCONPCBATIONOF BCIA TSD:Aadhaar Lookup using Web Service
4.Requestand Responseformat
The Request and theresponseareasper mentioned below:
ReguestMessage
Max
S.No. Field Name FieldType Status Remarks
Length
AadhaarNumber NUM 12 123456789012
MobileNumber NUM 10 1234567890
Request No ALPNUM 10 ABCD000001(BankShortCode
followedbyreferencenumber)
RequestDateTime Date&Time 23 2015-03-10 14:47:47.741
Stamp (YYYY-MM-DD HH:mm:ss.S)
ResponseMessage
Max
S.No. Field Name Field Type Status Remarks
Length
Aadhaarnumber NUM 12 123456789012
Bank Name ALPNUM 80 ABC BANK
Error ALPNUM 150 Invalid AadhaarNumber
Date Format
LastUpdateDate 10 2015-02-13
YYYY-MM-DD
MandateCustDate Date 10 2015-02-13
MandateFlag ALPHABET YIN
MobileNumber NUM 10 1234567890
ODDate Date 10 2015-02-13
OD Flag ALPHABET Y/N
2015-03-10 14:47:47.741
10 ProcessedDate Date&TimeStamp 23 (YYYY-MM-DD
HH:mm:ss.S)
ABCD000001(BankShort
11 Request No ALPNUM 10 Code followed by
referencenumber)
2015-03-10 14:47:47.741
12 Request Received time Date&TimeStamp 23 (YYYY-MM-DD
HH:mm:ss.S)
2015-03-10 14:47:47.741
13 RequestedDateTime Date&TimeStamp 23 (YYYY-MM-DD
HH:mm:ss.S)
Aadhaar Status ALPNUM A/I
ATIONALAUTOMATEDCLEARINGHOUSE Page 6 of 10

<!-- Page 9 -->

NATIONALPRYMENTSCORPORATIONCFINDIA TSD:AadhaarLookupusing Web Service
** For optional field, expecting xml tag (with blank value) to be present in request and
response message format
Regquest & ResponseDescription:
S.No Request Response
SuccessmessagewillreceivebackwithOD&
Provide 12digit valid Aadhaar number MandateDetails
ProvideAadhaarnumberlessthan12
characters Error.InvalidAadhaar Number
ProvideAadhaar numberwithalpha
characters Error-Aadhaar NumberContainsletter(s)
Provide Aadhaar number with alpha Error-Invalid Aadhaar Number,Aadhaar
characters and length<12 Number Contains letter(s)
ProvideAadhaarnumberlength>12 Error.InvalidAadhaarNumber
Provide12digit Aadhaar number not Error-Aadhaar Number is not available
availableinDatabase
Provide10digitrequestnumber Error-Firstfourcharacterofrequestnumber
withoutthebank short code must bebank short code
Providebankshortcodebutlessthan
10characters Error.Invalid request Number
Provide null requested date time Error-Invalid requested date
Error-InvalidAadhaarNumber,Invalidrequest
Provideinvalid Aadhaar,request NumberandFirstfourcharacterofrequest
number and requested date time numbermust bebank shortcode,and Invalid
10 requesteddate
Providedrequesteddate&timenot
inISOformat(YYYY-MM-DD Error-InvalidDateformat,Expected Date
11 HH:mm:ss.S) FormatisYYYY-MM-DDHH:MI:Ss.S"
MAH
LTIONALAUTOMATEDCLEARUNGHOUS Page 7 of 10

<!-- Page 10 -->

NPCI NATIONALHAYMENTSCOEPORATIONGF INDIA TSD:Aadhaar Lookup using Web Service
5.ProcessFlow
In a normal Web service, client will send a HTTPs request to server, and server will send
back a HTTPs response to client directly.In our scenario, Bank System will act as a Client
and WebSphereApplication Server (WAS)of NACH will act as the Server.
1.Client Web Service Call Server:<port>
2.Server:<Port> Web ServiceCal Client
Request from Client:
1.As mentioned in above diagram in point 1, Bank systemwill raise an online web service
call to Aadhaar mapperDB in termsof request withAadhaar No,mobile no, request
no, request date & time.
2.At Bank side, the Web Service URL will be called, using which Client will get
connected to Server.BelowURLwill beusedforproduction
Banks overInternet:
https://nach.npci.org.in/CMAadhaar/AadhaarStatusService
BanksoverNPCINET:
https://192.168.179.231/CMAadhaar/AadhaarStatusService
3.Banks to integrate the above URL to forward the request to NACH system.
AH
Page 8 of 10

<!-- Page 11 -->

NPC NATIONALPAYMENITSCOEPORATIONOFINCIA TSD:AadhaarLookupusingWebService
Response to Client:
1. As mentioned in above diagram in point 2, WAS will internally use the query to get the
Required details and send the response from UiD Repository.Details of the response are
mentioned inSection4.
2.TheXMLResponseis enclosed as Annexure1.
6.Annexure
Annexure1
SamplehttpsRequestandResponse
Annexure 2
WSDLfileforAadhaarStatusisattached.
7. Requirements at Client Side:
1.TheHTTPs SOAP requestwillbeforonlyoneAadhaarnumber ata time
2. 0 Connectivitydetailsto beprovided by Banks.
3. Banks to integrate the WSDL URL at their end.
4. All technical validations with regards to Aadhaar number will be done by the Banks
system.
5.Banks togenerate uniquerequest numberforeach webcall.
6.Below IPsneedtobewhitelistedfromBank end
Banks through Internet
S. No. iP Details Port Connectivity
103.14.161.34 443 PR
103.14.160.34 443 DR
BanksthroughNPCINET
S. No. IPDetails Port
192.168.179.231 443
MAH
ATIONALAUTOMATEDCLEARINGHOUSE Page9of 10

<!-- Page 12 -->

NPC  NATIONALPRYMENTSCORPOPATIONOFINDIA TSD:AadhaarLookup using WebService
8.Support
NACH Support Helpdesk can be contacted regarding any technical queries as per the
contactdetailsgivenbelow
Email ID :NACHSupport@npci.org.in
ContactNumbers :044-28160741/42
NAH
Page 10of 10
