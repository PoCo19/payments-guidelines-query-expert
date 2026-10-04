# Circular 18 – Bank Compliances to enable UPI Merchant ecosystem

Circular/reference number: OC-18
Date: 20th March, 2017

<!-- Page 1 -->

 
Public - Public - 
 
NPCI/UPI/OC No. 18 / 2016-17 
 
 
 
 
 
20th March, 2017 
 
To, 
All Member Banks, Unified Payments Interface (UPI) 
Dear Sir / Madam, 
Subject: Bank Compliances to enable UPI Merchant ecosystem  
1) Unified Payment Interface was launched to reform the Merchant payment ecosystem. Banks 
are formulating multi-prong strategies to enable merchants on UPI platform and have been 
instrumental in popularizing this product by offering innovative solutions across industries. 
  
2) NPCI had issued guidelines to member Banks for merchant on-boarding. Whilst the guidelines 
have been adhered by the Banks however it has been observed that there are challenges with 
respect to customer experience and Merchant adoption.  
 
3) It is identified that there is lack of uniformity across PSPs with respect to product design and 
functions, thus limiting widespread product adoption. 
 
4) This Circular briefs about following product functions and essentials for Merchant payments. 
The details are given here as an Annexure. 
 
a) Functional uniformity in QR based merchant solutions 
b) Uniformity in Android Intent function in UPI payments 
c) Implementation of Manage & List VAE (Virtual address entries) APIs 
d) Other Specific requirements to ensuring seamless Merchant payments 
e) Merchant on-boarding related standardisations 
 
5) Member Banks are requested to comply to the requisites mentioned above and confirm on or 
before 21st Apr 2017 to NPCI at - Sarika.sorte@npci.org.in, Amaya.pande@npci.org.in 
For queries related to the above circular please contact the following; 
a) Maria Francis 
b) Anurag Priyadarshi 
c) Bivek Rath 
 
Yours truly, 
 
Dilip Asbe 
Chief Operating Officer

<!-- Page 2 -->

 
Public - Public - 
Annexure 
 
A. QR Related 
Objective: Functional Uniformity in QR based merchant solutions: 
 
1.) Challenges with the current implementations (Based on observations & live scenarios): 
 
a. Bank PSPs scanning QR codes, fail to pass parameters populated by initiating PSPs or 
Merchant apps/web. 
b. The Bank PSP apps have built in business logics to read QR codes by defining MCCs. 
This may lead to transactions being declined in case of MCC = ‘0000’(P2P). 
c. There is an imminent need to populate few critical business parameters like MCC, 
Transaction reference number (tr) and Amount (am) while generating Dynamic QR. 
d. In case of Static QR wherein the Transaction reference number (tr) is not generated, 
the Bank PSPs scanning such QR are not able to populate and pass the parameters. 
 
2.) Impact: Lack of uniformity in the PSP app functionality may lead to poor customer experience 
across eco system, resist wide merchant adoption and may lead to reconciliation challenges 
and payment confirmation. 
 
3.) Responsibility of the member Banks in the UPI ecosystem:  
 
a) The Acquiring PSP should ensure that the following critical business parameters for 
Dynamic or Static QR code. 
 
<TABLE 1> - QR (Key Deep Linking parameters) 
 
PN: Mentioned above are only the critical parameters for Merchant transactions. There are other additional 
parameters which are optional and can be referred to, from the Deep Linking Specs provided to member banks. 
 
b) It is a prudent norm that elements present in QR are scanned and passed back to the 
issuing app. PSPs should not apply any preferred criteria in this regard. 
c) The bank PSPs should read and process all QR codes generated irrespective of whether it 
is a merchant QR code (P2M with specific MCC) or individual QR code (P2P with MCC 
‘0000’).  
d) The mandatory parameters passed in the message string for dynamic QR should be non-
editable. However, in case of static QR code the amount may be input by the customer. 
Critical 
Parameters 
Description 
As per 
 'Deep 
linking 
specs' 
Revisions 
Remarks/ Rationale 
Dynamic 
QR 
Static 
QR 
Pa 
Payee 
virtual 
payment 
address 
M 
M 
M 
For address resolution 
Pn 
Payee Name 
M 
M 
M 
To identify verified Entity/ 
Merchant name 
Tr 
Transaction Ref No. (upto 
35 digits) 
C 
M 
 
Merchant reference number 
for Reconciliation 
Am 
Amount 
O 
M 
 
Value of financial transaction 
(Non-editable) 
Mam 
Minimum amount 
O 
C 
 
Minimum amount to be paid, 
different 
from 
transaction 
amount (Editable)

<!-- Page 3 -->

 
Public - Public - 
e) If the Minimum amount (mam) parameter is present, then the amount field should be 
editable. However, the amount field will be non-editable if the ‘mam’ parameter is 
absent. 
f) It is mandatory for Acquiring PSP to populate Transaction Reference No. (tr - upto 35 
digits). However, in case of static QR code (tr is not populated) the PSP app scanning the 
QR code must populate the Transaction Ref. No. and pass the parameter. 
 
 
B. Intent Related 
Objective: Uniformity in Android Intent function in UPI payments:   
 
1. Present broad challenges with respect to intent in Merchant Ecosystem: 
a) In some instances, Bank PSP apps & UPI compliant merchant apps are not responding to 
intent call initiated by Merchant apps. 
b) IN other instances, Merchant apps initiating Intent are unable to receive confirmation of 
payment or status of the transaction. 
c) PSP apps responding to intent;  
- 
With App passcode, are unable to handle or progress with transaction (Apps may 
crash),  
- 
Post transaction completion the PSP app fails to pass back the control to initiating 
merchant app. 
 
2. Impact: Lack of uniformity across ecosystem on Response to Intent function can lead to poor 
customer experience, poses fundamental business challenges w.r.t transaction failure, 
reconciliation and payment realization, impacts merchant confidence and adoption. 
 
3. Intent protocols & recommendations for PSP Banks & Merchant Apps: 
a. Merchant initiated intent call should mandatorily include the details as per <TABLE 1> 
above as part of the key Deep linking parameters. Following may be additionally noted: 
b. If the Minimum amount (mam) parameter is present, then the amount field should be 
editable. However, the amount field will be non-editable if the 'mam' parameter is absent. 
c. PSP apps/ SDK integrated UPI compliant apps should respond to the intent call initiated 
by a Merchant app and confirm the transaction status with the following mandatory 
parameters; 
PN: Mentioned above are only the critical parameters for Merchant transactions. There are other additional 
parameters which are optional and can be referred to, from the Deep Linking Specs provided to member 
banks. 
Mandatory 
Parameters 
Description 
As per 
'Deep linking 
specs' 
Revisions 
Remarks/ Rationale 
txnId 
Transaction ID (35 digit) 
O 
M 
Unique 
transaction 
identifier on UPI switch 
TrtxnRef 
Transaction Ref No. (upto 35 
digit) 
O 
M 
Customer 
reference 
number 
for 
Reconciliation 
& 
Disputes 
Status 
Success/ Failed 
O 
M 
To 
confirm 
the 
transaction status 
responseCode  
‘00’ for success or any other 
appropriate response code 
for decline 
O 
M 
To verify the reason for 
decline

<!-- Page 4 -->

 
Public - Public - 
d. In response to the intent raised by merchant app, PSP apps/ SDK integrated UPI compliant 
apps should read the string and display the parameters of the string in a non-editable 
view. 
e. Upon customer confirmation the app should re-direct the customer to NPCI CL page for 
UPI PIN input. 
f. Post transaction completion, the PSP apps/ SDK integrated UPI compliant apps should 
provide the intent response to Merchant app and pass on the control to merchant app 
along with mandatory response parameters. 
 
 
C. Merchant Whitelisting related 
 
Objective: Implementation of Manage & List VAE (Virtual address entries) APIs - UPI product 
facilitates 2 APIs to whitelist and publish UPI verified merchants. 
 
1. Banks acquiring merchants for UPI payment mode must whitelist merchants using manage 
VAE API, to publish their list of verified merchants. Thus, promote and encourage 
merchants to adapt UPI payment option. 
2. All UPI PSP apps must use List VAE API to download and store UPI verified merchants. Thus, 
build confidence in customers to use UPI as a preferred mode of payment at these 
merchants. 
 
D. Other Specific requirements 
Objective: Ensuring Seamless Merchant payments: 
 
1. In case of Collect request initiated from any PSP or merchant website, the details passed 
by the PSP in the ‘transaction note’ tag should be non-editable and passed on by the 
receiving PSP. It should also be displayed to the customer on the payment app. 
2. The merchant name fetched by the Acquiring PSP during vpa resolution should always be 
the verified name from the issuer CBS. 
3. For push transactions initiated to a merchant VPA, wherein ‘MCC’ & ‘Type’ is absent or 
incorrectly populated in Payee tag, it is observed that the Acquiring PSP fails to identify 
this anomaly and thus fails to resolve the vpa with correct merchant credentials. This will 
lead to reconciliation issues, since the transaction will be treated as P2P and issues in 
interchange computation. 
i. 
Thus, the Acquiring Bank while resolving the VPA for its merchant must check 
for ‘MCC’ & ‘Type’ parameters 
ii. 
They should also verify these parameters with the actuals (MCC & Type) 
captured at the time of merchant on-boarding. 
iii. 
In case of absence or discrepancy in these parameters the Acquiring bank must 
replace these parameters or populate the correct parameters accordingly. 
4. It is observed that Banks are responding with default or dummy IFSC (only 4 digit) in Payer 
tag. IFSC is imperative for businesses like Insurance & Capital markets for address resolution 
purpose and refunds, hence the banks must populate complete 11 digit IFSC. 
5. Collect request raised by merchants on-boarded through Aggregators, should display the 
Merchant name in the collect notification to customer. 
6. Some Banks partnering with Aggregators are populating static MCC, for all merchant 
transactions. Banks are expected to populate merchant specific MCCs.

<!-- Page 5 -->

 
Public - Public - 
 
7. Banks to note the following for QR generation & Intent: 
- 
While generating an intent/QR string, ‘space’ has to be represented by  ’%’ and while 
reading an intent, ‘%’ has to be replaced with ‘space’ by the UPI app.  
- 
For example, remarks entered by user “test transaction” shall generate intent 
message as ‘’tn=test%transaction’’ and when read by UPI app, % should be replaced 
with ‘space’. 
 
 
E. Merchant On-boarding related 
Objective: Standardization 
1.) Merchant Onboarding Report: Banks Acquiring merchants on UPI should provide below details 
fort nightly by 15th & 30th of every month for the next 4 months only;  
Bank 
nam
e 
Aggregator 
name/ 
Merchant 
Name 
Sub-merchant 
name 
(in case of 
Aggregators) 
MCC 
populate
d 
Integration 
Type 
(Web Collect/ 
SDK/ intent ) 
Type of Services 
offered (P2P/ P2M 
or Both) 
  
  
  
  
  
 
2.) Banks must provide the following for all Merchants on-boarded through SDK route; 
i. Network Architecture for merchant integration. 
ii. UPI App checklist stamped and signed by the Bank. 
iii. External security audit report and compliances for SDK Third Party Audit report and 
merchant/ PSP provider application (As mentioned in Circular 15A) 
iv. Bank Assurance letter with the following; 
 Accuracy and completeness of scope coverage and compliances to findings 
of security audit report. (As mentioned in Circular 15A) 
 Merchant details: Merchant name, App ID, Payee vpa, MCC
