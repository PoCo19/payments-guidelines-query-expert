# Circular No. 7 - Transactions Processed on National Automated Clearing House (NACH) System

Circular/reference number: NPCI/NACH/2013-14/Circular
Date: 31st May, 2013

<!-- Page 1 -->

 
Registered Office - C-9, 8th Floor, Reserve Bank of India Premises, 
Bandra-Kurla Complex, Bandra-East, Mumbai-400 051 
 
 
 
 
NPCI:2013-14:NACH:Circular 7  
 
 
 
 
 
       31st May, 2013  
 
To,  
All Member Banks of National Automated Clearing House (NACH) System  
 
Transactions Processed on National Automated Clearing House (NACH) System 
 
Madam / Dear Sir,  
 
NPCI has been successfully processing the Direct Benefit Transfer (DBT) transactions on NACH 
system since the last 4 months. Based on the discussion and feedback received from the 
member banks, NPCI would like to highlight the following points which member banks need to 
take care while processing the DBT transactions. 
 
a) Transaction Narration in Customer Account Statement – The narration in the 
customer statement/passbook is extremely critical as it would let the customer 
identify the source and reason of receipt of benefit transfer. Therefore, it is important 
that the sponsor bank includes it as part of input file and destination banks’ are 
advised to capture narration of the EBT transaction in the customer account 
statement. A reference may be made to Annexure - 1 where an example illustrating 
the same is enclosed for ease of reference to all concerned.  
 
b) Return and Response Files –Banks are requested to refer NPCI circular Ref. No. 
NPCI/NACH/2013-14/Circular 4 dated 16th April, 2013 (copy enclosed) for return reason 
codes. The members are requested to follow the return reason codes mentioned in the 
above circular only.  
 
It has also been observed that as per the NACH Procedural Guidelines, the destination 
banks are required to provide the status of all the inward files/transactions received at 
their end.  The status of the transactions not received in the response file cannot be 
treated as a “Deemed Acceptance/Success” as there is no such status called “Deemed 
Acceptance/Success”. This has been communicated earlier as well vide circular Ref No 
NPCI:2013-14:NACH:Circular 5 dated 19th April, 2013 (copy enclosed). More so, in case 
of Government transactions, it is important that there are no deemed success else it 
impacts the audit and accounting practice of government departments and their

<!-- Page 2 -->

 
Registered Office - C-9, 8th Floor, Reserve Bank of India Premises, 
Bandra-Kurla Complex, Bandra-East, Mumbai-400 051 
 
 
 
 
sponsor banks. Therefore, it is once again re-iterated that all banks should take 
necessary steps to ensure processing of all inward transactions during the return 
window.  
 
c) System Processing Capacity – It is highlighted to the member banks that from 01st 
June, 2013 onwards, destination banks will start receiving large number of EBT 
transactions mainly on account of LPG subsidy from Oil Marketing Companies (OMCs). 
Member banks are advised to put in place necessary infrastructure having adequate 
capacity to process transactions in the range of 5-10 lakh or any other number in tune 
with the customer base and Aadhaar Numbers’ seeded in a window of 2-3 hours.  
 
2. We are enclosing a compliance form along with the circular to be submitted by the member 
banks on their letterhead on the following points:  
(i) 
Transaction Narration in customer account statement  
(ii) 
Processing of every inward transaction received as per the time window 
(iii) 
Capability to process transactions in tune with the customer base and Aadhaar 
numbers seeded as per session timelines.  
The compliance form in this regard may be submitted to NPCI latest by 07th June, 2013.  
 
3. It may be highlighted that NPCI reserves the right to take appropriate measures in case of 
failure by specific member bank to comply or violate any of the provisions of the NACH 
Procedural Guidelines in the interest of all the participants. 
 
For any further help/queries, please feel free to reach us at ach@npci.org.in 
 
With Warm Regards,  
 
Vipin Surelia 
Head – Cheque Clearing & ACH 
Encl: 
(i) DBT Narration for Account System 
(ii) Compliance Certificate Form

<!-- Page 3 -->

 
Registered Office - C-9, 8th Floor, Reserve Bank of India Premises, 
Bandra-Kurla Complex, Bandra-East, Mumbai-400 051 
 
 
 
 
Annexure - I 
 
 
 
 
 
 
DBT Narration for Account Statement

<!-- Page 4 -->

 
Registered Office - C-9, 8th Floor, Reserve Bank of India Premises, 
Bandra-Kurla Complex, Bandra-East, Mumbai-400 051 
 
 
 
 
 
Table of Contents 
 
1. 
INPUT FILE: ........................................................................................................ 5 
2. 
INWARD FILE: ..................................................................................................... 5 
3. 
RESPONSE FILE: .................................................................................................. 6

<!-- Page 5 -->

 
Registered Office - C-9, 8th Floor, Reserve Bank of India Premises, 
Bandra-Kurla Complex, Bandra-East, Mumbai-400 051 
 
 
 
 
1. 
Input File: 
 
 
The Username field can now be used for narration text, to explain the customer about 
the transaction. 
 
The Narration text field is of length 20 characters, starting from position 88 till position 
107. Possible usage to convey purpose Ex: DBTIOCLLPGCYL1 
 
The User Credit Reference no has to unique for a customer for a day. Ex: LPG consumer 
no. 
 
The fields highlighted in the below picture are the Destination Bank IIN Number, 
Narration filed and User Credit Reference number. 
 
Figure 1 - Input File Format 
2. 
Inward File: 
 
 
NPCI will automatically populate the IIN number into the inward file that reaches the 
destination Bank and also the NACH Unique reference no of 10 digits. 
 
The User Name field in Inward file will have the Narration value sent by Sponsor bank 
and the User Credit reference number (sponsor bank transaction ref. no.) field will be 
populated with the data taken from the Input file. 
 
On successful transaction processing Destination banks needs to print the value in User 
Name (Narration text) + User Credit Reference (sponsor bank transaction ref. no.) 
into the Account statement / Pass book for Beneficiary customers.  
 
Figure 2 - Inward File Format

<!-- Page 6 -->

 
Registered Office - C-9, 8th Floor, Reserve Bank of India Premises, 
Bandra-Kurla Complex, Bandra-East, Mumbai-400 051 
 
 
 
 
3. 
Response File: 
 
 
The Narration field and the User Credit Reference number will be present in the Return 
file also. 
 
The Response file will contain the IIN number populated by NPCI. 
 
The file will have a Success flag with status (0 and 1). Where 1 is success and 0 is a 
failure. This will be of 1 digit and will be at the position 154 in the file. 
 
The Reason code will have “00” for a Success transaction or a valid failure reason code 
if the transaction has failed. This will be of 2 digits and will be filling positions 156 and 
157 in the file. 
 
The combination of Narration field and the User credit reference number can be used 
to update the customer’s passbook. 
 
Figure 3 - Response File Format

<!-- Page 7 -->

 
Registered Office - C-9, 8th Floor, Reserve Bank of India Premises, 
Bandra-Kurla Complex, Bandra-East, Mumbai-400 051 
 
 
 
 
(To be printed on Bank’s Letterhead) 
 
Date:  
 
To, 
National Payments Corporation of India 
C-9, 8th Floor, RBI Premises, 
Bandra Kurla Complex, Bandra East, 
Mumbai – 400051 
 
Compliance Certificate – National Automated Clearing House (NACH) 
 
A reference may be made to NPCI circular ref. no. NPCI/NACH/2013-14/Circular 7 dated 31st 
May, 2013. In this regard, we hereby confirm the following: 
 
a) Transaction Narration in Customer Account Statement 
We hereby confirm that our bank is capturing and passing the transaction narration of 
EBT transaction to customer statement/passbook. 
 
b) Return and Response Files 
We hereby confirm that our bank is capturing correct return reason codes and 
providing the status of all the inward files/transactions received at their end to the 
sponsor bank. 
 
c) System Processing Capacity 
We hereby confirm that our bank has put in place necessary infrastructure with 
adequate processing capacity to process transactions in the range of 5-10 lakh or any 
other number in tune with the customer base and Aadhaar Numbers’ seeded in a 
window of 2-3 hours. 
 
For XYZ Bank 
 
 
Authorised Signatory

<!-- Page 8 -->



<!-- Page 9 -->



<!-- Page 10 -->



<!-- Page 11 -->



<!-- Page 12 -->

 
 
C-9,8TH FLOOR, RBI PREMISES, BANDRA KURLA COMPLEX, 
BANDRA EAST, MUMBAI 
 
NPCI: 2013-14: NACH: Circular 5 
 
 
 
 
                
19th April, 2013 
To, 
All Member Banks of National Automated Clearing House (NACH) System 
Serial Transactions Processing on National Automated Clearing House (NACH) using Aadhaar Number 
followed by Bank Account in case Aadhaar Number is not available 
Respected Madam / Sir, 
NPCI is thankful to you for your support to Electronic Benefit Transfer (EBT) processing on National 
Automatic Clearing House (NACH) system.   
2. Based on the feedback and suggestions received from different stakeholders, a single file serial 
transaction format has been devised to process the Electronic Benefit Transfer (EBT) transaction 
processing on NACH system for AADHAAR based transactions and Account based transactions. The file 
format for this single file serial transaction is attached here as an Annexure A. All banks that are sponsor 
banks and processing files on behalf of govt departments/agencies would have to get ready to get the 
additional details and convert into the single file format for uploading into NPCI NACH system. 
3 In case of the availability of Aadhaar Number in EBT transaction, it will be processed as per the 
payment type APB-Credit on NACH system. In case, the Aadhaar Number is not available in transaction 
details, and instead Account Number and IFSC Code/MICR/IIN is available, it will be processed on the 
basis of Bank Account Number as per the payment type NACH-Credit on the NACH system. Therefore, 
the destination banks have to get ready with NACH-Credit receiving capability at the earliest.  
4. For the processing of inward EBT transaction processing, destination banks will receive two separate 
files i.e. identical to APB-Credit and NACH-Credit as two distinct files. However, sponsor bank will receive 
a single file consist of Aadhaar based as well as Account based transactions as a final response file from 
NACH system to reconcile with the original single file uploaded. 
5. As per the NACH Procedural Guidelines, banks have to confirm the status of all the inward 
transactions received at an individual transaction level in the return response file and the status of the 
transaction not received cannot be treated as a deemed success. Banks are requested to adhere to the 
NACH Procedural Guidelines.  
6. This single file serial transaction format for EBT has a provision to capture additional data point like 
Scheme code, district code and Village / Block code to cover comprehensive MIS coverage. 
7. Banks are requested to initiate onboarding process at the earliest on the single file serial transaction 
file format on NACH system.

<!-- Page 13 -->

 
 
C-9,8TH FLOOR, RBI PREMISES, BANDRA KURLA COMPLEX, 
BANDRA EAST, MUMBAI 
 
For any queries/further help required, please email at ach@npci.org.in 
 
With warm regards, 
 
Vipin Surelia 
Head –Cheque Clearing & NACH
