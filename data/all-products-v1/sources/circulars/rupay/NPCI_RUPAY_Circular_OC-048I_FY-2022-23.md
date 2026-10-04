# RuPay I OC048 I FY 21-22 I Circular - Actions for RuPay Issuers to comply with Card on File Tokenization

Circular/reference number: NPCI/2021-22/RuPay/048
Date: 31st March, 2022

<!-- Page 1 -->

 
NPCI/2021-22/RuPay/048                                                                                                           31st March, 2022 
 
To, 
All RuPay issuers 
 
Dear Sir/Madam, 
Subject: Actions for Issuers to Comply with Card on File Tokenization Guidelines 
 
With reference to the RBI Circular ‘Regulation of Payment Aggregators and Payment Gateways’ dated 
31st Mar 2021 - RBI/2020-21/117 CO.DPSS.POLC.No.S33/02-14-008/2020-2021 (Annexure A), Merchants 
and Payment aggregators are barred to store the sensitive customer information in their database and 
servers, while doing card on file ecommerce transaction. 
NPCI has come up with the card on file tokenization (CoFT) solution to facilitate token-based transactions. 
The RBI deadline to comply with CoFT changes has been extended to 30th of June 2022. For CoFT, NPCI 
has onboarded 100% of credit card issuers, 95% volume contributing debit card issuers and 99% volume 
contributing prepaid card issuers. However, from last few months we have experienced very slow progress 
from the issuers on CoFT. Since only 3 months are left to adhere with RBI compliance on tokenization 
(CoFT), we request issuers to complete the required changes on priority.  
Below are critical actions needed from RuPay issuers for card on File Tokenization: - 
1. Tokenization related changes at Authorization Switch – For token based transactions, i.e. 
subsequent transaction utilizing the token credentials, capturing of CVV at the merchant page is 
optional for the Merchant. However, for Guest checkout transactions, CVV at merchant page will 
be required as per the current process. Thus it is imperative that issuers ensure that they deploy 
appropriate measures to identify token based and guest checkout transactions through the 
following indicators 
a. DE 61 sub Field 7, Value 9 
b. DE 105 
This should ensure that token based transactions are identified, which will not necessarily carry CVV 
and therefore are not declined. Additionally, the bank has the choice to deploy any other CVV 
validation policy as per their internal compliance requirements. 
 
2. Tokenization Changes at the Authentication layer (IAS/ACS) – Issuing members have to ensure 
that following indicators are captured as part of token provisioning in auth_initiate or 
generate_OTP API at the IAS/ACS systems 
a. TW (Transaction + Token Provisioning) 
b. AW (Provisioning only)

<!-- Page 2 -->

 
 
This will ensure that every token provisioning request by the customer of the issuer is captured as 
part of authentication and available to issuer as information to take appropriate action on those 
requests. 
 
3. Token Lifecycle Management – RBI Circular-RBI/2021-22/96 CO.DPSS.POLC.No.S-516/02-14-
003/2021-22 on “Tokenisation – Card Transactions: Permitting Card-on-File Tokenisation (CoFT) 
Services” (Annexure B), dated 7th Sep 2021 mentions that,  
 
A facility shall also be given by the card issuer to the cardholder to view the list of merchants in 
respect of whom the CoFT has been opted by her / him, and to de-register any such token. This 
facility shall be provided through one or more of the following channels –  
 
Mobile application 
 
Internet banking 
 
Interactive Voice Response (IVR) or 
 
at branches / offices 
Hence to Comply with RBI guidelines, we request Issuers to – 
a. Create Credentials on the LCM portal Provided by NTS 
b. Integrate Lifecycle Management APIs for CoFT either directly or through Token TSP 
 
Non-Adherence to the Guidelines will result in serious non-compliance and hence it is of utmost 
importance for the issuers to do the required changes before the deadline of 30th June 2022. Thus, request 
all the issuers to take immediate and appropriate steps. 
 
 
Yours faithfully,  
 
SD/-  
Kunal Kalawatia 
Chief of Products 
NPCI
