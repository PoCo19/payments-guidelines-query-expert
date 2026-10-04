# 30-Apr-2020 - Product Bulletin - Update on Card Payments - Relaxation in requirement of Additional Factor of Authentication for small value card present transactions

Date: 30th April 2020

<!-- Page 1 -->

                                                                     
 
 
Product Bulletin                                                                                                        30th April 2020 
 
Update on Card Payments – Relaxation in requirement of Additional Factor of Authentication 
for small value card present transactions 
 
This 
has 
reference 
to 
the 
RBI 
circular 
Ref. 
No. 
RBI/2014-15/601 
DPSS.CO.PD 
NO.2163/02.14.003/2014-15, dated 14th May, 2015 towards Card Payments – Relaxation in 
requirement of Additional Factor of Authentication for small value card present transactions (Circular 
enclosed) wherein requirement of Additional Factor of Authentication (AFA) for small value Card 
Present (CP) transactions was relaxed for transaction values up to ₹ 2,000/- per transaction, 
performed using NFC-enabled EMV Chip cards 
 
In this regard, as per the email communication dated April 27th, 2020, received from RBI, it has been 
clarified that Card Present transactions using NFC-enabled EMV chip and PIN cards may be 
processed in contactless mode, irrespective of the transaction value. However, the transactions with 
values above ₹ 2,000/- shall be authenticated using PIN. 
 
It may also be noted that customers will still have a choice to make all Card Present payments using 
NFC-enabled EMV chip and PIN cards in “contact payment” form with AFA, irrespective of the 
transaction value. All other provisions mentioned in the said circular shall continue to remain in force. 
 
NPCI is the pioneer in promoting contactless transactions across India. RuPay Contactless is a game 
changer for driving contactless payments in India (like transit, toll, parking, retail). With increase in 
digital payment acceptance infrastructure across the nation, contactless payment has been a big boost 
in driving digital transactions and further, with the clarification provided by RBI, the adaptation of the 
same will benefit all the stake holders (Consumers and Merchants), especially in these times where 
social distancing is of supreme importance. 
 
However, a systematic step by step approach needs to be followed for successful rollout of the above 
change in your payment infrastructure and following are some key points to take note of :-  
Issuing Banks: 
1. Changes to be reviewed and updated on the host system. 
2. Modification to be made in the risk rules to allow contactless transactions above ₹ 2,000/- with 
PIN.

<!-- Page 2 -->

                                                                     
 
 
3. Technical considerations for these transactions are as given:  
• 
Transaction amount less than or equal to ₹ 2,000, Data Element 22 (POS Entry Mode) will 
be 07 and PIN will not be present (DE 52 will be absent)  
• 
Transaction amount greater than ₹ 2,000, Data Element 22 (POS Entry Mode) will be  07 
and PIN must be present (DE 52 will be present)   
Acquiring Banks: 
1. In order to prompt PIN for transactions greater than ₹ 2,000/-, changes needs to be 
implemented in the terminal software by making the appropriate change in the contactless 
transaction limit. 
2. The changes may be implemented remotely or in other cases may have to be done onsite. 
3. Acquiring Banks may also get the changes implemented through their payment aggregators. 
In addition to above, it is extremely imperative that effective communication, handholding & training is 
provided to all stakeholders (merchants, aggregators, customers) through various channels in order 
to rollout the same successfully. 
 
Please do let us know if you require our support during the process of creating and evaluating 
communication plans. NPCI will be happy to partner with you. 
 
We recommend that, as all the stakeholders are rolling out RuPay Contactless in their respective 
market, they may take necessary actions & implement this change as well within 3 months, i.e. by July 
31st 2020. We thus request all member banks to take immediate and appropriate steps. 
 
We thank you for continued patronage. 
 
For any queries, please write to us at rupay@npci.org.in or contact your NPCI Relationship Manager. 
 
Yours faithfully, 
 
SD/- 
Nalin Bansal 
Head – RuPay & NFS 
NPCI
