# Circular No.183 NACH Mandate ReInitialization Specifications for Banks Mandate Re-initialization V1.0

Circular/reference number: OC-183
Date: 0 
 
 
 
 
 
 
 
 
 
August, 2016

<!-- Page 1 -->

 
 
 
NATIONAL PAYMENTS CORPORATION OF INDIA 
NACH Project 
MMS re-initialization of mandates with existing UMRN 
number 
Bank Specification Document 
Version 1.0 
 
 
 
 
 
 
 
 
 
August, 2016

<!-- Page 2 -->

NPCI NACH MMS Solution 
Bank Specification Document_V1.0 
NPCI Confidential 
Page 2 of 10 
 
DOCUMENT RELEASE NOTICE 
 
Document Details 
Name 
Version 
No. 
Date 
Description 
Bank 
Specifications 
Document 
1.0 
6th Aug 2016 
Provides operations and technical details for the 
change - A feature in MMS for the mandate 
initiating banks to re-initiate the mandate with 
same UMRN which were cancelled or rejected at 
the receiver bank. 
Bank 
Specifications 
Document 
1.1 
16th Aug 2016 
Updated as per Review Comments 
Bank 
Specifications 
Document 
1.2 
19th Aug 2016 
Updated as per Review Comments 
 
This document and any revised pages are subject to document control. Please keep them up-to-date 
using the release notices from the distributor of the document.

<!-- Page 3 -->

NPCI NACH MMS Solution 
Bank Specification Document_V1.0 
NPCI Confidential 
Page 3 of 10 
Table of Contents 
1. 
INTRODUCTION ............................................................................................................................... 4 
2. 
MANDATE RE-INITIATION ........................................................................................................... 4 
2.1 
MANDATE RE-INITIATION THROUGH GUI ........................................................................................ 4 
2.2 
MANDATE RE-INITIATION THROUGH XML ...................................................................................... 4 
2.3 
MANDATE BULK-RE INITIATION THROUGH CSV ............................................................................ 7 
3. 
APPENDIX ........................................................................................................................................ 10 
3.1 
APPENDIX 1 –MMS BULK RE-INITIATION XML INP FILE ............................................................. 10 
3.2 
APPENDIX 2 – MMS BULK RE-INITIATION INP ACK FILE ............................................................. 10 
3.3 
APPENDIX 3 – FILE FORMATS ................................................... ERROR! BOOKMARK NOT DEFINED.

<!-- Page 4 -->

NPCI NACH MMS Solution 
Bank Specification Document_V1.0 
NPCI Confidential 
Page 4 of 10 
1. Introduction 
This document details the mechanism of incorporating a new feature in MMS for the mandate 
initiating banks to re-initiate the mandate with same UMRN which were TAT Expired, cancelled or 
rejected at the receiver bank. 
2. Mandate Re-Initiation  
Mandate Re-initiation can be done through either of the below mentioned ways 
 
Mandate Re-Initiation through GUI 
 
Mandate Re-Initiation through XML 
 
Mandate Bulk Re-Initiation through CSV 
The Reject reason codes for which Mandate can be Re-initiated are controlled at NPCI end. 
2.1 Mandate Re-initiation through GUI 
 
Through GUI, only individual re-initializations can be done. 
 
 The REJECTED mandates can be re-initiated by the Mandate Initiator Bank and the 
CANCELLED mandates can be re-initiated by either creditor or debtor bank.  
 
The list of rejected/cancelled mandates which are allowed by NPCI for re-initiation will be 
displayed on the GUI. From this User can select the mandate that has to be Re-initiated. 
 
For the Rejected/Cancelled mandates system will auto populate all the initial details that 
where provided at time of mandate initiation and will allow user to modify all the fields that 
can be modified in the normal amendment process (user will  not be able to edit 
“UMRN,Message Reference, Payment Type, Currency,Debitor Bank “fields)   
 
Upon confirmation of checker approver, the mandate will be available to the receiver bank 
for further processing.  
 
If checker rejects the re-initiation request, then the mandate status will remain as 
rejected/removed. 
 
If checker approves the re-initiation request, then the INW and RES will be generated as per 
the existing process flow. Please refer section 2.2 for the file naming convention of INW and 
RES files. 
2.2 Mandate Re-Initiation through XML 
 
All the mandates TAT Expired, cancelled & rejected by Debtor banks can be re-initiated in 
this case. 
 
The changes in the file format and file naming conventions are mentioned below. 
 
 When a Creditor bank re-initiates a Mandate, it is optional to upload image. If the creditor 
bank doesn’t upload any image, the mandate will be re-initiated with existing images.

<!-- Page 5 -->

NPCI NACH MMS Solution 
Bank Specification Document_V1.0 
NPCI Confidential 
Page 5 of 10 
 
Any Number of re-initialization Mandates can be raised through XML until the size of the file 
doesn’t exceed 10MB. 
 
 All the fields that can be modified during Amendment via XML can be modified during re-
initiation via XML. 
 
After Re-initializing a Mandate, the mandate will be considered as a Normal Mandate. And 
thus when that mandate is Amended, the file formats will be same as that of existing Amend 
file format. 
 
 
Changes in file format and naming convention for XML initiation 
 
Format 
 
For Mandate Re-initiation Request, the ISO20022 format is pain010. 
 
For Mandate Acceptance Request, the ISO20022 format is pain012. 
 
Input File 
Bundled File i.e.zip file containing the data file and the image files. 
<ProcessName>-<TransType>-<Bank Short Code>-<LoginId>-<MMS BusinessDate>-<nnnnnn>-
INP.zip 
 
ProcessName –MMS 
 
Trans Type –RECREATE 
 
Bank Identifier – 4 Char Unique Bank Identifier in System 
 
LoginId - User Login Id  
 
MMS Business Date –ddmmyyyy 
 
nnnnnn –Running sequence number for each zip file 
E.g. MMS-RECREATE-HSBC-HSBC001-10062012-000001-INP.zip 
The zip file will contain the xml file and the image files with the below naming convention 
MMS-RECREATE-Bank Short code-Loginid-Business Day-nnnnnn-INP.xml 
MMS-RECREATE-Bank Short code-Loginid-Business Day-nnnnnn _detailfront.jpg 
MMS-RECREATE-Bank Short code-Loginid-Business Day-nnnnnn _front.tiff 
 
Acknowledgement File to sender bank 
Acknowledgement file will be provided for all the input file uploaded into MMS 
<ProcessName>-<TransType>-<Bank 
Short 
Code>-<LoginId>-<MMS 
Business 
Date>-
<nnnnnn>-INP-ACK.zip

<!-- Page 6 -->

NPCI NACH MMS Solution 
Bank Specification Document_V1.0 
NPCI Confidential 
Page 6 of 10 
E.g. MMS-RECREATE-HSBC-HSBC001-10062012-000001-INP-ACK.zip 
Same format as for any mandate request ACK is used pain.012.001 
 
Inward File to Receiver Bank 
Inward file will be generated when MRC (Mandate Request Cutoff) Timetable is executed.  
<ProcessName>-<TransType>-<Bank Short Code>-<MMS Business Date>-<nnnnnn>-INW.zip 
E.g. MMS-RECREATE-HSBC-10062012-000001-INW.zip 
Zip file will contain individual re-create mandate requests from different initiator banks and will carry 
the name as given by initiator bank while creating the request.  
MMS-RECREATE-HSBC-HSBC001-10062012-000005-INP.xml 
MMS-RECREATE-HSBC-HSBC001-10062012-000005_detailfront.jpg 
MMS-RECREATE-HSBC-HSBC001-10062012-000005_front.tiff 
 
Acceptance File from Receiver Bank 
Receiver bank can send acceptance of the mandate request either through file or can do it through GUI. 
The file needs to be sent before MAC – Mandate Acceptance Cutoff timetable.  
<ProcessName>-<TransType>-<Bank 
Short 
Code>-<LoginId>-<MMS 
Business 
Date>-
<nnnnnn>-ACCEPT.zip 
E.g. MMS-RECREATE-HSBC-HSBC001-10062012-000001-ACCEPT.zip 
Zip file will contain individual acceptance of request from different initiator banks and will carry the 
name as mentioned  
E.g. MMS-ACCEPT-HSBC-HSBC001-10062012-000005-INP.xml 
 
Acknowledgement File to Receiver Bank 
Acknowledgement file will be sent to the receiver bank for all the acceptance requests file uploaded into 
MMS 
<ProcessName>-<TransType>-<Bank Short Code>-<LoginId>-<MMS Business Date>-
<nnnnnn>-ACCEPT-ACK.zip 
E.g. MMS-RECREATE-HSBC-HSBC001-10062012-000001-ACCEPT-ACK.zip 
Zip file will contain ACKs for individual acceptance of request from the receiver banks and will carry the 
name as mentioned in the ACCEPTANCE request

<!-- Page 7 -->

NPCI NACH MMS Solution 
Bank Specification Document_V1.0 
NPCI Confidential 
Page 7 of 10 
E.g. MMS-ACCEPT-HSBC-HSBC001-10062012-000005-INP-ACK.xml 
 
Acceptance File to Initiating Bank 
MMS will send the mandate response files to the mandate initiating bank after MARC for which receiver 
bank has responded or exceeded the TAT. 
<ProcessName>-<TransType>-<Bank Short Code>-<LoginId>-<MMS Business Date>-<Time>-
RES.zip 
E.g. MMS-RECREATE-HSBC-HSBC001-10062012-000001-RES.zip 
Zip file will contain Response for individual acceptance of request from the receiver banks and will carry 
the name as mentioned in the ACCEPTANCE request 
E.g. MMS-ACCEPT-HSBC-HSBC001-10062012-000005-INP.xml 
2.3 Mandate BULK-Re Initiation through CSV 
The below is the process flow for the bulk re-initiation of TAT expired by providing only UMRN. 
 
A bulk mandate re-initiation request file can contain a maximum of 100 UMRN’s for re-
initiation. 
 
User will upload the csv file in SFG.(Please refer annexure for file format)  
 
Only the mandates which are “TAT expired” can be reinitiated in this case. 
 
Once reinitialized the status of the existing mandates will change from “REJECT”(Reject 
reason-TAT expiry) to “Approve” or “Pending for acceptance” 
 
Bulk Re-initiation and Amendment cannot be performed simultaneously. 
 
The changes in the file format and file naming conventions are mentioned below. 
 
During Re-initiation via CSV, a mandate can only be re-initiated with the existing Mandate 
details, and none of the fields can be modified.  
 
 
Examples for bulk create flow: 
1. User uploads a csv file with maximum of 100 UMRN (example 100 UMRN's) without any images. 
2. MMS will process the requests and sends a single ACK to SFG which has status of all the 100 
requests in CSV format. 
3. After MRC (Mandate Request Cut-off) executed by NPCI inward files along with images (old 
images will be picked and sent) will be sent to the receiver bank in pain 010 format (Same as 
recreate functionality). 
4. Receiver bank sends acceptance in pain 12 format. 
5. After NPCI executes MAC (Mandate Acceptance Cut-off) response files will be sent to sender 
bank in pain 012 format

<!-- Page 8 -->

NPCI NACH MMS Solution 
Bank Specification Document_V1.0 
NPCI Confidential 
Page 8 of 10 
File format and File naming for CSV BULK initiation files 
File formats for bulk mandate re-initialization and bulk mandate acceptance operations are: 
 
For bulk mandate re-initiation request, the input is in CSV format.  
 
For Recreate mandate inward, the ISO20022 format is  pain.010.001.01 
 
For Recreate mandate acceptance request, the ISO20022 format is  pain.012.001.01 
 
For Recreate mandate response, the ISO20022 format is  pain.012.001.01 
 
Input File 
<ProcessName>-<TransType>-<Bank Short Code>-<LoginId>-<MMS BusinessDate>-<nnnnnn>-
INP.csv 
 
ProcessName –MMS 
 
Trans Type –BULKRECREATE 
 
Bank Identifier – 4 Char Unique Bank Identifier in System 
 
LoginId - User Login Id  
 
MMS Business Date –ddmmyyyy 
 
nnnnnn –Running sequence number for each zip file 
E.g. MMS-BULKRECREATE-HSBC-HSBC001-10062012-000001-INP.csv 
 
Acknowledgement File to sender bank 
Acknowledgement file will be provided for all the input file uploaded into MMS 
<ProcessName>-<TransType>-<Bank 
Short 
Code>-<LoginId>-<MMS 
Business 
Date>-
<nnnnnn>-INP-ACK.csv 
E.g. MMS-BULKRECREATE-HSBC-HSBC001-10062012-000001-INP-ACK.csv 
 
 
Inward File to Receiver Bank 
Inward file will be generated when MRC (Mandate Request Cutoff) Timetable is executed.  
<ProcessName>-<TransType>-<Bank Short Code>-<MMS Business Date>-<nnnnnn>-INW.zip 
E.g. MMS-RECREATE-HSBC-10062012-000001-INW.zip 
Zip file will contain individual bulk re-create mandate requests from different initiator banks and will 
carry the name as given by initiator bank while creating the request.  
MMS-RECREATE-HSBC-HSBC001-10062012-000005-INP.xml

<!-- Page 9 -->

NPCI NACH MMS Solution 
Bank Specification Document_V1.0 
NPCI Confidential 
Page 9 of 10 
 
Acceptance File from Receiver Bank 
Receiver bank can send acceptance of the mandate request either through file or can do it through GUI. 
The file needs to be sent before MAC – Mandate Acceptance Cutoff timetable.  
<ProcessName>-<TransType>-<Bank 
Short 
Code>-<LoginId>-<MMS 
Business 
Date>-
<nnnnnn>-ACCEPT.zip 
E.g. MMS-RECREATE-HSBC-HSBC001-10062012-000001-ACCEPT.zip 
Zip file will contain individual bulk acceptance of request from different initiator banks and will carry the 
name as mentioned  
E.g. MMS-ACCEPT-HSBC-HSBC001-10062012-000005-INP.xml 
 
Acknowledgement File to Receiver Bank 
Acknowledgement file will be sent to the receiver bank for all the acceptance requests file uploaded into 
MMS 
<ProcessName>-<TransType>-<Bank Short Code>-<LoginId>-<MMS Business Date>-
<nnnnnn>-ACCEPT-ACK.zip 
E.g. MMS-RECREATE-HSBC-HSBC001-10062012-000001-ACCEPT-ACK.zip 
Zip file will contain ACKs for individual bulk acceptance of request from the receiver banks and will carry 
the name as mentioned in the ACCEPTANCE request 
E.g. MMS-ACCEPT-HSBC-HSBC001-10062012-000005-INP-ACK.xml 
 
Acceptance File to Initiating Bank 
MMS will send the mandate response files to the mandate initiating bank after MARC for which receiver 
bank has responded or exceeded the TAT. 
<ProcessName>-<TransType>-<Bank Short Code>-<LoginId>-<MMS Business Date>-<Time>-
RES.zip 
E.g. MMS-RECREATE-HSBC-HSBC001-10062012-000001-RES.zip 
Zip file will contain Response for individual acceptance of request from the receiver banks and will carry 
the name as mentioned in the ACCEPTANCE request 
E.g. MMS-ACCEPT-HSBC-HSBC001-10062012-000005-INP.xml

<!-- Page 10 -->

NPCI NACH MMS Solution 
Bank Specification Document_V1.0 
NPCI Confidential 
Page 10 of 10 
3.  Appendix 
3.1 Appendix 1 –MMS Bulk Re-Initiation using CSV INP formats 
                 
CSV BULK 
formats.zip
 
               
3.2 Appendix 2 – MMS Bulk Re-Initiation using XML INP formats 
            
XML Formats.zip
