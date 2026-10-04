# 28th Sept 2016 - NPCI/2016-17/AEPS/06 - Circular 10 Adherence to AePS XML specification - 28th Sept 2016

Circular/reference number: NPCI/2015-16/AEPS/06
Date: 28th September, 2016

<!-- Page 1 -->

NPCIL
NATIONALPAYMENTSCORPORATIONOFINDIA
Circular:NPCI/2015-16/AEPS/06 28th September, 2016
To,
AllthemembersofAadhaarEnabledPayment System
AdherencetoAePsXMLspecification
RespectedSir/Madam,
Aadhaar Enabled Payment System has matured and have witness exponential
growth in the number of transaction over the period of time. It is very important
for banks to adhere to specification to ensure standardisation across the Aes
ecosystem.
In the Meeting with banks, held on 23rd September at NPCI BKC office, NPCI has
informed banks that they need to be compliant to the AePs XML specification. In
view of the above, banks have to perform one round of comfort testing, for test
cases mentioned in Annexure for the services that bank has opted. Post successful
test run, bank will be migrated to a new environment.
The schedule for this activity would be shared post discussion and consent of the
bank. Member entities are requested to kindly take a note of the same.
WithWarmRegards,
Pispiader Singh
HeadFI&NewBusiness
1001A,The Capital, B Wing,10thFloor,Bandra Kurla Complex, Bandra (E), Mumbai 400 051.T:+91 22 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure 1
TransactionType Onus
Case 1 Successful Balance Inguiry Transaction
Balance Enquiry 1.Customer requests for Balance enquiry at Authentication 00
Bank's BC should be ret
2. Initial level validation of Account and successful.
Aadhaar number mapping will be done at
acquirer switch end.
3. If validation is successful; Authentication
Request will be routed to NPCl.
4. NPCI routes the message to UIDAI for
authentication and responds back to acquirer
bank switch.
5.Bank performs balance enquiry and responds
back to BC
Case 2 Successful Cash WithdrawalTransaction
Onus Cash 1. Acquirer Customer requests for Cash Acquirer 00 in
Withdrawal Withdrawal. bank/UIDAI ret
(Authentication 2. Initial level validation of Account and should approve
Only) Aadhaar number mapping will be done at
acquirer switch end.
3.if validation is successful ;Authentication
Request will be routed to NPCl.
4. NPCI routes the message to UIDAI for
authentication and responds back to acquirer
bank with the response from UIDAl.
5. Acquirer bank debits the customer account
and route message to MicroATM.
Case 3 Successful Cash Deposit Transaction
OnusCashDeposit 1.Customer requests for Cash Deposit at acquirer 00 in
(Authentication acquirer bank's BC bank/UIDAI ret
Only) 2. Initial level validation of Account and should approve
Aadhaar number mapping will be done at
acquirer switch end.
3. if validation is successful ;Authentication
Request will be routed to NPCl.
4. NPCI routes the rinsg to UIDAI for
authentication and responds back to bank
5. Acquirer bank credits the customer account
and responds back to BC.

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Case 4 Successful FundTransferTransaction
Onus Fund Transfer 1. Customer requests for Fund RemitterBank/UIDAI 00 in
(AuthenticationOnly) transfer at RemitterBank's BC /remitterBank ret
2. Initial level validation of Account should approve
and Aadhaar number mapping will be
done at remitter switch end.
3. if validation is successful
;Authentication Request will be
routed to NPCl.
4. NPCI routes the message to UIDAI
for authentication and respondsback
to remitter bank.
Transaction Type-Authentication
NPCI UIDAL
Transaction Expected
Remark Response Response
Type Result Code Message
Scenerio 1 Successful Authentication
1. AUA enters the Customers Authentication 00 in ret 'y'
Aadhaar number and captures should be
the biometric data of the successful.
customer.
2. AUA sends the encrypted
request of authentication
containing biometric data to
NPCI.
3. NPCI routes the message
after digitally signing the
request to UIDAIfor
authentication and responds
back to respective AUAwith
the response from UIDAl.
4.AUA will receive successful
authentication.
Transaction Type-BFD
Test Cases Response code RRN
BFDrequestwithUIDandFpof sameperson
1.Residentchooseto doaBFD transaction.
2. Application prompt to take finger print of all 10 finger one after the other.
TC 1 3. BFD Request will be routed to NPCl.
4. NPCI routes the message to UIDAl for BFD authentication and responds back to
Customer with successful matching and ranking of each finger.
TC 1.1 BFD initiated with2 finger 00
TC 1.2 BFD initiated with 3 finger 00

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
TransactionType_eKYCandOTP
Case 1 OTPRequest(Successful)
OTP 1.KUA enters the Customers Aadhaar number. OTP should be 00/NA
Request 2.KUA sends the encrypted request of OTP to received on
NPCI. customer's linked
3.NPCI routes the message after digitally signing mobile number
the request to UIDAl for authentication and with Aadhaar
responds back to respective KUA with the number.
responsefrom UIDAl.
4.Customer will receive OTP on his registered
mobile number.
Case 2 KYC request with OTP.
KYC request 1.KUA enters the Customers Aadhaar number and Demographic and 00/NA
with OTP OTP received on customer registered mobile KYC details of the
number . customer should be
2.KUA sends the encrypted request of KYC received by the
containing OTP to NPCI : respective KUA
3.NPCI routes the message after digitally signing
the request to UiDAl for authentication and
responds back to respective KUA with the
response from UIDAl .
4.KUA will receive the demographic and KYC
data including photograph of the respective
customer.
Case 3 KYC request with BIOMETRIC data.
KYC request 1.KUA enters the Customers Aadhaar number and Demographic and 00/NA
with captures the biometric data of the customer . KYC details of the
BIOMETRIC 2.KUA sends the encrypted request of KYC customer should be
containing biometric data to NPCl . received by the
3.NPCl routes the message after digitally signing respective KUA
the request to UIDAl for authentication and
responds back to respective KUA with the
responsefromUIDAl.
4.KUA will receive the demographic and KYC
data including photograph of the respective
customer.
Transaction Type-Demographic Authentication
Test case of Pi, Pa, Pfa, Pi & pa and Pi & pfa
