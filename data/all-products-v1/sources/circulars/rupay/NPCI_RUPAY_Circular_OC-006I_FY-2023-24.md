# RuPay I OC006 I FY 23-24 I RuPay Credit Card Bill Payment Through BBPS

Circular/reference number: NPCI/2022-23/BBPS/007
Date: 26th May 2023

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCl/2023-24/RuPay/006 26th May 2023
To,
All RuPay Members -- Credit Card Issuers
Dear Sir/Madam,
Subject: RuPay Credit Card Bill Payment via Bharat Bill Payment System (BBPS)
With reference to the RBI guidelines on Bharat Bill Payment System (BBPS) vide circular no.
DPSS.CO.PD.No.605/02.27.020/2019-20 on 16th September 2019, it was approved to expand
the scope and coverage of BBPs to include all categories of billers who raise recurring bills
(except prepaid recharges) as eligible participants, since then the category list is further
expanded in RBl Monetary and credit information review dated 31st December 2022.
Bharat Bill Payment System (BBPS) is an interoperable platform operated by NPCl Bharat Bill
Pay Ltd. (NBBL). It provides a secure and accessible platform for customers to make their bill
payments conveniently.
Recognizing the significance of credit card bill payment for credit card users, it is imperative
to establish a standard platform that ensures secure, interoperable, and accessible bill
payment functionality. In line with this objective, NBBL has released the necessary guidelines
(BBPS). These guidelines are outlined in the operating circular NPCI/2022-23/BBPS/007,
subject "Bharat Bill Payment System - Standardization of Retail Credit Card Category," dated
5th December 2022 (Annexure A).
It is important for credit card issuers, to provide this feature to their RuPay credit card
customers for a rich and seamless experience. Hence, member banks should implement this
feature across their entire RuPay credit card portfolio by 31st July 2023. This enablement will
significantly elevate the customer experience by facilitating a convenient and frictionless credit
card bill payment process.
Thanking You,
SD/-
Kunal Kalawatia
Chief Products
1001A, The Capital, B Wing, 10th Floor.
Bandra Kurla Complex, Bandra (E), Mumbai 4OO O51.
T: +912240009100 F:+9122 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

BHARAT
BILLPAY
Circular:NPCl/2022-23/BBPS/007 5th December 2022
Al BBPOUS
BharatBill PaymentSystem
Dear Sir/Madam,
Bharat Bill Payment System-Standardization of Retail Credit Card Category
Members to take a note that Bharat Bill Payment System had introduced a retail credit card category that
enables the consumers to pay their respective credit card bills, either partially or in full or any other
amount, on BBPS enabled platform.
Key details below:
1.Standard user experience with respect to retail credit card category
2.Credit Card billers will be configured cn Fetch & Pay model, wherein customers would use
unique identifier for fetching their bill details
3. Customer will be allowed to make payments on total billed amount, minimum amount due,
current outstanding amount due or any other amount
4. Payment modes/ channels allowed for this category shall be subject to regulation. Customer can
pay through all payment mode, except credit cards
Further details with respect to retail credit card category is explained in the Annexure. We request
members to take note of the same and bring the contents of the circular to the notice of the relevant
personnel down the line.
Enclosed-
Annexure: Standardization of Retail Credit Card Category
Warm Regards,
SD/-
(Noopur Chaturvedi)
Chief Executive Officer
NPCIBharat BillPayLtd.
NPcI Bharat BillPay Limited
NPCIBHARATBILLPAYLTO. (A wholly owned subsidlary of NPCD)
Registred office:1oO1A,The Capital,B Wing,1o Floor.
Bandra Kuria Complex, Bandra (E).Mumbai 4O0 O51.
T:+912240009100F:+912240009101

<!-- Page 3 -->

BHARAT
BILLPAY
Annexure
Standardization of Retail Credit Card Category
Introduction
Through retail credit card category, customers can pay their respective credit card bills, either partially or in full or
any other amount, on BBpS enabled piatforms, The interoperability of BBps platform would ensure that customers
have the ease of paying all their credit card bills on a single platform.
Customer will be allowed to make full payment, part payment and/ or advance payment. This would be facilitated
by configuring Credit Card Billers with Adhoc payments enabled with payment mode specific amaunt limits in place.
Biller will be onboarded as a fetch and pay biller for credit card category
User Journey
Enter Customer
Select Credit Card Category Select Biller Parameters Bll Payments
Bnl Pay Credit Card Credil Card Bil Psy
SELECTBILLERSERVICE
aSeloctSerch Senvke: 9875545210
Las4deicctteoedtan
907543210
Dee Date
Fat Cataety
Usbibed Amount R5 1000
1234
bren Categorkes Select Arcountto Pry
Wncoe R01 O
Cable iy CedrCe'd MinimunAmoutas 5, 300
R字 5030
Amouat
Hosad
Get bill detats
Approach
1. Customer logs in the Al/coU platform, selects Credit Card category and selects the biller
2. Customer inputs unigue identifiers - Mobile number, Last 4 digit of primary Credit card number to fetch
his/her bill details
3. In Fetch request APl, above unique parameters will be passed to respective biller through BBPS ecosystem
to fetch details
4. In Fetch response APl, after successful validation, details like customer name, total billed amount, minimum
amount due, unbilled amount, current outstanding amount due, and due date wil be sent back by biller
In case of invalid details, appropriate response code message will be provided
NPCI BHARAT BILLPAY LTD.

<!-- Page 4 -->

BHARAT
BILLPAY
5. Customer can verify the details displayed on coU platform and initiate payrnent for any amount he/she
wants to pay or can choose either of total billed amount, minimum amount due or current outstanding
amount due (Adhoc payment configuration)
6. coU will initiate Payment Request APl, and pass the bill details mentioned along with payment amount to
billerthroughBBpSecosystem
7.  Through Payment response APl, biller system will provide payment status, along with the payment
reference numberfor futureuse incase of successful transaction
8.  CoU will display the payment status to the rcustomer as per BBPS guidelines. Payment receipt to be shared
with the consumer
Note: Payment modes/ channels allowed for this category shall be subject to regulation. Customer cannot pay
through credit cards as a payment mode
Multiple credit cards associated with same input parameters
As confirmed by Credit Card issuer banks, chances of having multiple credit cards associated with the same input
parameters (Registered Mobile Number and last 4 digits of Card Number) is very low.
But if such cases occur, below error code must be passed by the BOU in bill fetch response APl:
Response Cade Compliance Code Compliance Description
200 BFR030 Multiple credit cards associated with the sarme input
parameters. Please do the payment from the
respective card issuer portal
Process Flow
Bi Fekh
BHARAT
BILLPAY
Bia Papuent
API TagName Biller Value Expected Requirement
Request CustomerParams Mobile Number Mandatory
CustomerParams Last 4 digit of primary Mandatory
credit card number
Response BillerResponse.amount Total Billed Amount Mandatory
BillerResponse.customerName Customer Name Mandatory
BillerResponse.dueDate Due Date Mandatory
BillerResponse.billDate Bill Date Mandatory
Additionallnfo Minimum Amount Due Mandatory
Additionallnfo Current Outstanding Mandatory
Amount Due
Additionallnfo Unbilled Amount Optional
NPCI BHARAT BILLPAY LTD.

<!-- Page 5 -->

BHARAT
BILLPAY
Types of Amounts in Output parameters
Amounts Explanation
Total Billed Amount Total amount dueof iaststatement(s) which
needs to be paid
Minimum Amount Due Itistheminimumamountwhich needstobe
paid on or before payment due date
Unbilled Amount The sum of all the transaction that the
customer made after the statement is
generated
Current Outstanding Total Billed Amount + Unbilled Amount --
Amount Due Payment/Credit
Example: Suppose the billing date of a credit card is 18th of every month, and the payment due date is 6th of the
following month.
Date of transaction Type of Transaction Output Parameters post transaction
transaction amount
19 March Purchase #500 Total Bilied Amount: -
Minimum Amount Due: -
Unbilled Amount: Rs 500
CurrentOutstandingAmountDue:Rs.5oo
31 March Purchase #500 Total Billed Amount: -
Minimum Amount Due: -
Unbilled Amount: Rs 1000
Current Qutstanding Amount Due: Rs.
1000
18 April Statement is Total Billed Amount: Rs 1Q00
generated Minimum Amount Due: Rs 50
Unbilled Amount: Rs. Q
Current Outstanding Amount Due: Rs.
1000
Due Date: 6th May
20 April Purchase 400 Total Billed Amount: Rs 1000
Minimum Amount Due: Rs 50
Unbilled Amount: Rs, aoo
Current Outstanding Amount Due: Rs.
1400
Due Date: 6th May
1 May Payment ≤900 Total Billed Amount: Rs 1000
Minimum Amount Due: Rs 50
Unbilled Amount: Rs. 400
Current Outstanding Amount Due: Rs. 500
Due Date: 6th May
Note: Unbilled Amount (Optional Field), and Current outstanding amount due will be updated on a real time basis
NPCI BHARAT BILLPAY LTD,

<!-- Page 6 -->

BHARAT
BILLPAY
API Sample
The below APis sample.is for reference purpose only. Not incorporated the complete Fetch and Payment APl, just the
relevant part (Highlighted)
Bill Fetch Request APi
<ns2:BillFetchRequest xmlns:ns2-"http://bbps.org/schema">
refld-"HGPDAAH6GVYD773CWT9RXNHVDUH22842345" siTxn="No"/>
<BillDetails>
<Biller id-"BANK00000XXXXX"/>
<CustomerParams>
<Tag name="Registered Mobite Number" value-"987654321a"/
<Tag name-" Last 4 digits of Primary Credit Card Number" value-"12341/
</CustomerParams>
</BillDetails>
</ns2:BillFetchReguest>
Bill Fetch Response APl
<ns2:BillFetchResponse xmlns:ns2="http://bbps.org/schema">
<Head ver="1.0" ts="2022-10-11T16:04:05+05:30" originst="BBCU"
TefId="HGPDAAH6GVYD773CWT9RXNHVDUH22842345"/>
<Reason approvalRefNum="AB123456" responseCode="000" responseReason="Successful" complianceRespCd-"
complianceReason=""×/Reason>
-BilerRasponse customerName-"xYz" amount-"100000" dueDate="2022-10-20" billbate:*2022-09-20">
<Tag narme-"Minimum Amount Due" value-"100"/>
<Tag name-"Unbilled Amount* value-"500"[>
<Tag name-"Current Outstanding Amount" value-"500"/>
≤/BHlerResponse>
</ns2:BillFetchResponse>
Note: Default 'amount' value passed in billerResponse tag will be ‘Tatal Billed Amount' for retail credit card category
Bill Payment Request APl
<ns2:BillPaymentRequest xmlns:ns2-"http://bbps.org/schema">
<Head ver="1.0" ts="2022-10-11T12:54:06+05:30" origlnst="cc01"
refld="0sibwhk0228446254044718393222841234"/>
msgld="HGP4XXCFV7NFAZQWK3A4D63TN2422841157"txnReferenceld-"BD012284BA6AAAIN11HM"
paymentRefld="45f7c2fbeadc4e0c9fe9586735e9448f>
<RiskScores>
<Score provider="BD01" type-"TXNRISK" value-"030"/>
</RiskScores>
</Txn>
<BillDetails>
<Biler id="BANK00000XXXXX"/>
<CustomerParams>
NPCIBHARAT BILLPAY LTD.

<!-- Page 7 -->

BHARAT
BILLPAY
<Tag name-"Registered Moblle Number' value-"'9876543210"/>
<Tag name-" Last 4 digits of Prirnary Credit Card Number" value-"1234"/×
</CustomerParams>
</BillDetails?
<BillerResponse customerName="xYz" amounta"100000' dueDate-"2022-10-20" billDate-*2022-09-20">
<Tag name-"Minirnum.Amaunt Due" value-"100"js
<Tag name-"lnbilfed Amount' value-"500"/?
<Tag name="Curent Outstanding Amount" value-"500"/>
≤/BillerResponses
<PaymentMethod quickPay="No" splitPay-"No" OFFUSPay-"Yes" paymentMode-"UP!"/>
<Amount>
<Amt amount-"10000o" custConvFee="o" currency-"356" cOUcustConvFee-"o'/?
</Amount>
</ns2:BillPaymentRequest>
Bifl Payment Response APl
<ns2:BillPaymentResponse xmlns:ns2-"http://bbps.org/schema">
<Head ver="1.0" ts="2022-10-11T11:57:59+05:30" origlnst="BBCU"
refld="0sibwhk0228446254044718393222841234"/>
<Reason approvalRefNum="HGP2WPKZNXJF5P4A1H8PWTN7V6R22841157" responseCode="000"
responseReason="Successful" complianceRespCd-"" complianceReason=""></Reason>
<Txn ts="2022-10-11T11:57:55+05:30" type=*FORWARD TYPE RESPONSE"
msgld="HGP4XXCFV7NFAZQWK3A4D63TN2422841157" txnReferenceld="BD012284BA6AAAIN1IHM"/>
<BUDetails>
<GustomerParams>
<Tag name="Registered Mobile Number" alue-"9876543210"/>
<Tag name=" Last 4 digits of Primary Cradit Card Nurmber" value-"1234/s
</CustomerParams>
/BillDetails>
BillerResponse customerName-"xYz" amount=^100000" dueDate-"2022-10-20t billDate-2022-0g-20
CustCorvFee-"g" biNumber-"NA" jllPeriod-"NA">
<Tag name-"Minimum Amount Duedlure-100't?
<Tag name="Unbilled Amount" value-"5do/>
<Tag name-"current Qutstanding Amount" value-"s0o"/s
</BillerResponse>
</ns2:BilPaymentResponse>
NPCI BHARAT BILLPAY LTD,
