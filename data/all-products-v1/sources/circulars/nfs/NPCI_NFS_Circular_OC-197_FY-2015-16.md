# NFS OC 197 AADHAAR Seeding through NFS

Circular/reference number: OC-197

<!-- Page 1 -->

 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
Process Note for AADHAAR Seeding through NFS ATM Network  
 
 
Aadhaar Number Seeding  
 
a. Interoperable: This will enable customers of participating NFS Member Banks to avail 
Aadhaar number seeding at other participating NFS member ATMs. 
 
b. Card based transaction: The transaction can be initiated only using card (ATM/Debit). The 
authorization by the Issuer Bank will be based on card and PIN, as per regular ATM 
transactions. 
 
c. Log-only request: Aadhaar Number seeding is a log-only transaction as it requires further 
processing i.e. verification and seeding of Aadhaar Number in the customer account linked 
with the card used to initiate the transaction. 
 
 
Transaction Flow  
 
 
                 
         
  
 
 
                                                                                                                                                                                                             
              
 
 
         
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
10 
2 
9 
8 
3 
1 
6 
5 
4 
7 
Bank ABC 
(Issuer) CBS 
Bank ABC (Issuer) 
Switch 
 
Bank ABC 
Customer 
NFS ATM 
(Acquirer) 
Acquirer Switch 
Transaction should be sent to 
Issuer CBS for checking 
account status

<!-- Page 2 -->

 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
Transaction Flow explained: 
 
1. At the participating NFS Member’s ATM, the Cardholder will initiate the transaction 
using the ‘ATM/Debit Card’ and PIN and choose the option for ‘Aadhaar Number 
Seeding’. 
2. The customer will be prompted to enter the Aadhaar Number at the ATM (twice). After 
entering the Aadhaar number (twice), ATM will display customer entered Aadhaar 
number on next screen along with an undertaking seeking customer consent for seeding 
the Aadhaar number to the bank account linked to the card. The recommended message 
that can be displayed on the ATM screen is given below:  
 
“I hereby authorize my card issuer Bank to link my Aadhaar number to my bank account 
linked with this card.” 
3. Once customer confirms the Aadhaar Number displayed on the ATM screen, the 
transaction will be forwarded by the Acquirer switch to NFS.  
4. NFS will route the transaction to respective Issuing bank on the basis of BIN. 
5. Issuing bank will verify the card and PIN details of the customer and check for account 
status.  
6. Upon successful verification, approved response will be sent by Issuing bank. 
7. The message is sent to NFS from the Issuing bank switch. 
8. NFS will forward the message to the Acquirer switch. 
9. The message received from NFS will be sent by Acquirer switch to the ATM. 
10. ATM displays the message on the screen stating that the request for seeding the 
customer’s Aadhaar number has been logged.  
Indicative ATM screens attached for ready reference. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
ACQUIRER RESPONSIBILITIES: 
1. Displaying the option for Aadhaar number seeding on ATM screens (making screen level 
changes). 
2. Ensuring data flow in specific format as per Technical Specifications shared by NPCI. 
ISSUER RESPONSIBILITIES: 
1. Logging requests received for seeding Aadhaar number in a customer’s account. 
2. Extracting required details (transaction logs for all Aadhaar seeding transactions) from bank’s 
ATM switch for Demographic Authentication (DA). 
3. Validating the Aadhaar numbers entered by customers for correctness through Demographic 
Authentication process. 
4. Seeding the Aadhaar number in the bank account of the customer. 
5. On successful seeding of Aadhaar number in the customer account, banks should send 
suitable SMS to the customer.

<!-- Page 3 -->

 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
START
Customer uses card, enters PIN & selects option for 
Aadhaar seeding
Customer will be prompted to enter Aadhaar number 
Customer will be prompted to re-enter Aadhaar 
number (second time)
Customer consent for 
seeding Aadhaar number
Card & PIN validation done by Issuing 
bank
Valid account
Customer a/c status checked by Issuing 
bank
Transaction declined
NO
YES
NO
YES
END
“Request successfully logged” 
message displayed on ATM
ONLINE TRANSACTION FLOW

<!-- Page 4 -->

 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
Aadhaar number validated by Issuing bank using 
NPCI’s Demographic Authentication process*
Aadhaar number 
validated
NO
Aadhaar number seeding 
unsuccessful
“Aadhaar seeding 
unsuccessful” 
message sent to 
customer’s mobile 
number
YES
Aadhaar number seeding successful
“Aadhaar seeding 
successful” message sent 
to customer’s mobile 
number
AADHAAR SEEDING PROCESS AT BANK’s END
Data culled out at EOD from 
switch by Issuing bank for 
Aadhaar number validation 
and seeding
START
END
*Please find attached NPCI’s Demographic Authentication process at the end of the document
 
 
Indicative Screen Flow 
 
1. 
2.
 
 
 
 
 
 
 
 
 
 
Please refer the following link for details on Demographic Authentication process: 
“http://uidai.gov.in/images/FrontPageUpdates/aadhaar_authentication_api_1_6.pdf”

<!-- Page 5 -->

 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
3.
  4.
 
 
 
  5.
6.
 
 
 
    
     7.

<!-- Page 6 -->

 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
8.
  
 
 
     
         9. 
 
 
      
 10.

<!-- Page 7 -->

 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
       
 11.
 
 
 
12. 
 13.
