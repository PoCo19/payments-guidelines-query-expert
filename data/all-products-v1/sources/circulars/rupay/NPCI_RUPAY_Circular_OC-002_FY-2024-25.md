# RuPay | OC002 | FY 24-25 | Compliance Enablement of RuPay International Transaction Functionalities

Circular/reference number: NPCI/2024-25/RuPay/002

<!-- Page 1 -->

 
NPCI/2024-25/RuPay/002 
 
 
 
 
 
 
           23rd May’24 
 
To, 
All Member Banks - RuPay 
 
Dear Sir / Madam, 
Subject: Compliance Enablement of RuPay International Transaction 
Functionalities 
RuPay cards are accepted domestically and internationally. To further increase success 
rate of RuPay cards internationally, Issuer member banks shall comply to RuPay Online 
Switching Interface Specification V20.3 dates 1st Aug’23 or versions released thereafter. 
The enablement to the below mentioned functionalities will enhance the RuPay cardholder 
payment experience for international transactions. 
1. Mail Order Telephone Order (MOTO): A Mail Order / Telephone Order (MOTO) 
transaction is a card-not-present transaction where the cardholder provides the 
merchant with their order and payment details by regular mail, letter or fax or telephone 
or email requests.  
 
2. Card Account Verification (CAV): A Card Account Verification (CAV) is a transaction 
which allows an Acquirer to send a CAV request to an Issuer to verify the integrity of 
the card. This helps the card acceptor or the merchant to perform a check on the card 
status prior to initiating a purchase transaction to ensure a better success rate. Issuers 
shall validate the card status, account status, eligibility for international transaction and 
respond to the transaction message.  
 
3. Dynamic Currency Conversion (DCC): Dynamic Currency Conversion (DCC) is a 
service offered by merchants at the point of sale (POS and ECom) to the cardholders 
to pay for goods or services in their own billing currency or in the merchant’s own local 
currency. The merchant or acquirer performs currency conversion locally and submits 
the transaction in the cardholder’s billing currency.  
 
4. Card Not Present ECom Transaction: With Card Not Present (CNP) ECom 
transactions RuPay customers can use their card on international merchant site, where 
issuer shall validate transaction basis card-number, CVV and Expiry date. 
 
5. International Non-PIN POS Transaction: Non PIN International transactions are card 
present transaction without PIN. The transaction is performed in contact or contactless 
mode; however, PIN is not asked at the terminal basis the regulations/guidelines in the 
respective geography. 
 
6. International Contactless Transaction: Contactless transactions have become 
popular mode of transaction internationally. Post pandemic customers and merchants 
prefer to transact digitally in contactless mode even in physical stores. It is also popular 
in transit solution. 
 
7. Merchant attempted 3DS: With Merchant attempted 3DS ECom transactions RuPay 
customers can use their card on international merchant site, where issuer shall validate

<!-- Page 2 -->

 
transaction basis card-number, CVV and Expiry date – where the transaction will be 
received by issuer with different Ecommerce transaction identifier (ECI).  
 
8. Pre-Authorization: Pre-authorization often referred to as ‘pre-auth’, is a feature which 
serves as a means for businesses to reserve a specific amount of a customer's funds 
temporarily, ensuring that the necessary funds are secured before the services are 
availed and the transaction can be settled subsequently.  
 
9. NPCI SecureNxt – RuPay 3DS: NPCI SecureNxt allows RuPay to process EMV 3DS 
transactions for card not present transactions. It provides a strong security layer for 
user authentication and complies with EMV and regulator’s regulations. This 
enhancement will be applicable for both Domestic as well as International RuPay 
transactions. 
Additionally, banks are required to set appropriate Gross Debit Limit (GDC) and Velocity 
Limit at BIN level. Banks need to mandatorily comply with adherence to above mentioned 
functionalities by 31st Jul’24. 
The transaction identifiers are mentioned in Annexure A. 
 
Your faithfully, 
SD/- 
Kunal Kalawatia 
Chief of Products

<!-- Page 3 -->

 
Annexure A 
Data Element Identifier as per RuPay Online Switching Interface Specification document 
Sr 
No 
Transaction 
Description 
DE-22 
DE-25 
DE-61  
DE-19  
DE-49  
DE-52 
DE-48 
Point of 
Service Entry 
Mode 
Point of 
Service 
Condition 
Code 
Pos Data 
Code 
Acquiring 
country code 
Currency 
Code, 
Transaction 
PIN Data 
Additional Data 
1 
MOTO 
transaction 
with 
cardholder 
not present 
indicator 
Digit 1 & 2 -  
01 (Manual) 
Digit 3 - 0 
(Unspecified) 
Value -  
08 (MOTO 
request / 
Standing 
Instruction) 
Subfield 5 -  
3 (Cardholder 
not present, 
Mail 
transaction) 
/4 
(Cardholder 
not present, 
telephone 
transaction)  
& 
Subfield 7 -  
1 (Manual 
Input, no 
terminal) 
Other than 356 
As per 
Specificatio
n 
NA 
As per Specification 
2 
MOTO 
transaction 
with 
cardholder 
present 
indicator  
Digit 1 & 2 - 
 01 (Manual) 
Value -  
08 (MOTO 
request / 
Standing 
Instruction) 
Subfield 5 - 
1 (Cardholder 
present) &  
Subfield 7 -  
7 (Key 
entered) 
Other than 356 
As per 
Specificatio
n 
NA 
As per Specification 
3 
CAV 
As per 
Specification 
Value -  
54 (Request 
for Card 
Account 
Verification 
without 
amount) 
As per 
Specification 
Other than 356 
As per 
Specificatio
n 
As per Specification 
As per Specification 
4 
DCC 
As per 
Specification 
As per 
Specification 
As per 
Specification 
Other than 356 
356 
As per Specification 
Tag 88 - 
Value 1 (Numeric) 
5 
Card not 
present 
Ecom 
transaction 
Without AFA 
Digit 1 & 2 -  
81 (E-
commerce) 
Value -  
59 (E-
Commerce 
Request) 
Subfield 5 -  
6 (E-
Commerce 
transaction) 
& 
Subfield 7 -  
5 
(Ecommerce) 
Other than 356 
As per 
Specificatio
n 
NA 
Tag 56 -  
08 (Non secure 
transaction) 
6 
Non-Pin 
POS 
transaction 
Digit 3 -  
2 (No PIN 
Entry 
Capability) 
Value -  
00 (Normal) 
As per 
Specification 
Other than 356 
As per 
Specificatio
n 
NA 
As per Specification 
7 
Contactless 
Digit 1 & 2 - 
07 
(Contactless 
payment 
using chip 
card) 
Value -  
00 (Normal) 
Subfield 1 -  
8 (Magstripe 
& contact 
ICC & 
Contactless 
Capability) 
Other than 356 
As per 
Specificatio
n 
NA 
As per Specification 
8 
Merchant 
attempted 
3DS with 
AFA 
Digit 1 & 2 -  
81 (E-
commerce) 
Value -  
59 (E-
Commerce 
Request) 
Subfield 5 -  
6 (E-
Commerce 
transaction) 
& 
Subfield 7 -  
5 
(Ecommerce) 
Subfield 8-  
0 (Unknown) 
Other than 356 
As per 
Specificatio
n 
NA 
Tag 56 -  
06 (Merchant 
attempted to 
authenticate using 3D 
secure) 
Note: Refer Latest RuPay Online Switching Interface for further details
