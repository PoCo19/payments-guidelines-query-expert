# IMPS I OC 74 I FY 16-17 I Verification Request (VR) preceding Original Request (OR) and Implementation of two ports (One for remitting and for beneficiary transactions)

Circular/reference number: OC-74I

<!-- Page 1 -->

N?C/ 
   f.r,r,r 
NATIONAL PAYMENTS CORPORATION OF /NOIA 
NPCI/IMPS/OC No 74/2014-15 
August 12, 2016 
To, 
All Member Banks, IMPS & PPls 
Dear Sir/Madam, 
Sub: (A) IMPS -Verification Request (VR) preceding Original Request (OR) 
{B) Implementation of two ports (one for remitting & another for beneficiary 
transactions) 
Objective: 
Objective of this circular is to explain the process to follow for VR preceding OR issues & Implementation 
of two ports (one for inward & another for outward transactions). 
A.
VR Preceding OR issue
OR means original request message sent by remitting bank to credit the beneficiary customer's a/c
for which the beneficiary bank should send response with response code for the transaction. VR
means Verification Request message which is sent by remitting bank, when there is no response
received from beneficiary bank for the OR.
The remitting bank should send OR first and if there is no response received within the TAT from the
beneficiary bank, only then VR should be sent. However, due to technical issues (switch or network)
remitting banks are sometimes sending VR first and OR thereafter, due to which remitting banks are
getting in to out of fund situation for such transactions. Please refer to the scenario given below:
i)
Remitting bank sends VR without any OR
ii)
Beneficiary bank sends RC-MO (Decline Response) because there is no original transaction
present
iii)
Remitting bank will reverse the customer account in online mode based on the declined
response received i.e. RC-MO from beneficiary bank
iv)
Subsequently, for the same transaction, the remitting bank is sending OR
v) 
Beneficiary bank receives the OR, credits the customer's a/c online successfully and sends
approved response to the remitting bank online i.e. RC-00
vi)
If the OR response is RC-00 then NPCI will settle the funds by debiting remitting bank and
crediting the beneficiary bank
Thus remitting banks are getting in to out of fund situation for sending VR first and OR later.
Proposed Solution and responsibilities for remitting and beneficiary banks are as 
follows: 
Remitting Banks: 
i)
Remitting banks should not to send VR before OR. We recommend that remitting banks
should review their process of sending original online message and if any issues are found
(as explained above), it must be fixed immediately.
1001A, The Capital, S Wing, 10th Floor, Sandra Kurla Complex, Sandra (El. Mumbai 400 051. T •912240009100 F •912240009101 www.npc1.org In 
CIN: U74990MH2 00BNPL189067

<!-- Page 2 -->

Beneficiary Banks: 
We request beneficiary banks to configure their system to send timed out response in the online 
message (i.e. RC-08 / ISO-91 instead of RC - MO) when VR is received without OR in data 
element - 39. Based on the time out response, remitting bank will not reverse and credit the 
customer's a/c online. Thus, the remitting banks will not get in to out of fund situation for VR 
preceding OR transactions. 
Please note Importantly that it will be the responsibility of Remitting Bank to ensure that first OR is 
sent and VR is sent only thereafter. Any financial impact due to sending VR before OR will have to be 
borne by the Remitting Bank only. 
B.
Implementation of two ports - one for inward and another for outward transactions
Banks which are having single port system for sending/receiving inward & outward transactions may
experience following problems:
•
During peak transaction volume, the messages may get queued up resulting in technical declines
and timeouts.
•
If bank as a beneficiary bank is not sending any online responses to NPCI, then NPCI will switch
off the node to avoid time outs (deemed approved transactions). In such situation, the same
bank as remitting bank will not be able to send outward transactions to NPCI.
Proposed Solution 
To avoid the issues explained above due to single port, we recommend members to implement (if not 
already done) two ports i.e. one for inward and another for outward transactions. 
•
Two ports will help in managing the load.
•
Increase the approval ratio and reduce the decline transactions (Technical & business declines).
•
Time out transactions (Deemed Approved) is also expected to come down.
•
In case NPCI brings down the bank's node for beneficiary transactions (due to time out issue),
the bank can still continue sending the outward transactions because it will be on another port.
Effective Date: September 15, 2016 
All IMPS members are requested to make necessary changes as per effective date and get it certified 
with NPCI. Same will be moved in to production system after certification. 
Please make a note of the above and disseminate the information contained herein to all officials 
concerned. 
For any queries or clarification, pleame contact: 
Name 
Mr. Soumyajit Roy 
Mr. Rama Raju 
Yns faithfully,
RamSopn· 
Head - Operations 
E-Mail ID 
soumvaiit.rovf@noci.orn.in 
ram a. ra iu(ci) noci.orn: .in 
Contact Number 
08879754970 
08108122895 
SD/-
