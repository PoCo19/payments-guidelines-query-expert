# IMPS I OC 114 I FY 22-23 I Credit Card Bill Payments using virtual number through IMPS

Circular/reference number: OC-114I
Date: 7th September, 
2021

<!-- Page 1 -->

 
 
1001A, The Capital, B Wing, 10th Floor, 
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in 
CIN: U74990MH2008NPL189067 
NPCI/IMPS/OC No.114/2022-23 
March 3rd, 2023 
To, 
All Members of IMPS 
Dear Madam/Sir, 
Subject: Credit Card Bill Payments using virtual number through IMPS 
Immediate Payment Service (IMPS) allows a customer to make their credit card bill payments 
seamlessly just by inputting credit card number as account number and IFSC of card issuing bank in 
IMPS P2A transaction mode. Card holders are empowered to conveniently make their monthly credit 
card bill payments through their Banking channels using IMPS by inputting 16-digit actual card number 
as account number and dedicated IFSC code of the card as input parameters under P2A mode. 
To safeguard the sensitive information of credit card holders including full card details from circulating 
in the ecosystem, Reserve Bank of India (RBI) had issued tokenization guidelines on 7th September, 
2021 via operating circular CO.DPSS.POLC.No.S-516/02-14-003/2021-22. 
On similar lines, to provide a secured experience on IMPS platform, we propose card issuer banks to 
also allow card holders to make their credit card bill payment using 16-digit virtual number which will 
be combination of “91 + 10-digit mobile number associated with the card + last 4 digit of the actual 
credit card number” and “dedicated IFSC” of card issuer bank for accepting credit card payments. The 
existing provision of allowing actual credit card number as account number via IMPS should be 
allowed. 
Proposed Process: 
Through IMPS P2A (Virtual Number + IFSC): Remitter can initiate payment towards their credit card 
using P2A transaction type by inputting virtual number proposed above as account number & IFSC of 
beneficiary bank where card was issued. This facility shall be made available by member banks that 
are live with IMPS on P2A. Beneficiary Bank should identify that the payment is intended for credit 
card basis the dedicated IFSC of issuer bank to accept credit card payments. 
Funds has to be instantly credited against customer’s actual credit card number in real-time. 
The broad roles and responsibilities of the members/participants in this service is laid out in the 
Annexure. 
We hereby request you to take steps towards implementation of the above before 31st May, 2023. 
Yours Sincerely, 
 
SD/- 
Kunal Kalawatia 
Chief of Products

<!-- Page 2 -->

 
 
1001A, The Capital, B Wing, 10th Floor, 
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in 
CIN: U74990MH2008NPL189067 
Annexure: 
a) Role of the Remitter Bank: 
 
To allow customers to make credit card bill payment via IMPS in P2A mode using 16-digit virtual 
number as account number and dedicated bill payment IFSC of card issuer bank 
 
Transaction to be routed to NPCI as IMPS P2A and NPCI will forward the request to intended 
Credit card issuer 
 
Credit card issuer will identify the transaction as credit card bill payment and validate the details 
inputted by customer 
 
Credit card issuer to accept the payment and send response to remitter bank via NPCI 
 
Remitter Bank to clearly communicate the transaction status to customer as per current practice, 
in case of timeout bank should request customer not to initiate new transaction in order to avoid 
multiple debits 
 
b) Role of NPCI: 
 
Route the transaction to Credit card issuer bank 
 
Communicate transaction status back to the remitter bank 
 
No Incremental change required at NPCI 
 
c) Role of Beneficiary Bank/Credit card issuing bank: 
 
To educate customers through SMS/Email/Social media/Bank’s official website/Bank branch that 
credit card payments can be done instantly using IMPS by inputting 16-digit virtual card number 
(91+10-digit mobile number associated with credit card + last 4 digit of actual card) 
 
Display 16-digit virtual card number to the customers in banking channels under credit card 
section. Example: “Your Credit Card Bill Payment virtual card number is “91<Your 10 digit 
registered mobile number><last 4 digits of your Credit Card>” 
 
Display 16-digit virtual number to the customers in the back of the cards for making credit card 
bill payments 
 
Have a mapping of 16-digit virtual number (91+10-digit mobile number associated with credit 
card + last 4 digit of actual card) against the actual credit card to identify the account in real time 
from their credit card database/system 
 
Credit card issuer who will act as a beneficiary bank for receiving such payments should follow 
below steps to accept payment: 
1. Identifying credit card payment basis dedicated card IFSC. 
2. Validate customers mobile number mentioned in the request and identify accounts 
associated with the mobile number from the database. 
3. Identify actual credit card number associated against the mobile number by matching with 
the last 4 digit of the virtual account number present in the request. 
4. Facilitate the credit to customer’s credit card and respond back to remitter bank via NPCI. 
 
To have online integration with the credit card system for validating the virtual number against 
details associated with actual card (registered mobile number, last 4 digit of actual card) 
 
To facilitate real time credit to the customer credit card 
 
To send instant response to the remitter regarding the status of the transaction
