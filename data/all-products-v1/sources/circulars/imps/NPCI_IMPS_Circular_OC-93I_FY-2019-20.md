# IMPS & UPI I OC 93 I FY 19-20 I Harmonisation of Turn Around Time(TAT) and customer compensation for failed transaction

Circular/reference number: OC-93I

<!-- Page 1 -->



<!-- Page 2 -->

Ni='C/ 
  ?JTTffPf f.'ro/r 
NATIONAL PAYMENTS CORPORATION OF IND/A 
Annexure A 
A)
Banks Actionable for unsuccessful transactions:
Remitter/Acguirer:
l.
For declined transactions (customer account is debited and declined at NPCI) it is the remitter
responsibility to reconcile & reverse customer account if not done in online within T+l, otherwise
remitting bank has to pay compensation to customer.
2. 
Remitting bank should reverse the customer account on the same day as and when the
returns/credit adjustments are received, otherwise remitting bank has to pay compensation to
customer.
3.
In case of non-fulfilment of UPI Merchant transactions, acquiring bank should raise returns/ credit
adjustments within 4 calendar days from the transaction date, otherwise compensation shall be
debited from acquiring bank and credit the same to issuing bank.
Beneficiary/Issuer: 
l.
Bank as a Beneficiary should credit the customer's account within T +l day (if not credited online),
otherwise customer account has to be credited with compensation. Bank to update TCC 102/103.
2.
If the amount cannot be credited due to any reason, same has to be returned to remitting bank on
or before 4 pm every day for UPI transactions and 5.30 pm for IMPS transactions by T+l, otherwise
NPCI shall debit the beneficiary bank and credit to the remitting bank. Remitting bank should credit
their customer account (Transaction amount + Compensation) on same day. If delayed then
remitting bank has to pay additional compensation to the customers.
3.
For UPI Merchant transactions, acceptance by acquiring bank for chargeback or pre-arbitration
(including deferred chargeback cycle) should be done within 4 days for chargebacks raised under
reason code "1065". If acquiring bank does not accept chargebacks/pre-arbitration within 4 days
then NPCI shall debit the acquiring bank and credit issuing bank transaction amount +
Compensation. Issuing Bank should credit the amount to the customer's account on the same day
or latest by 5th day from the transaction day. If delayed then issuing bank has to pay additional
compensation to the customers.
B)
Changes in adjustment / dispute process: For deemed approved P2P IMPS & UPI transactions,
Customer compensation shall be applicable in case beneficiary fails to update "RET" as per below
table. TAT for raising returns by Beneficiary Bank are highlighted below.
Product 
Adjustment Type 
IMPS 
RET 
UPI
RET 
X 
No. of days after Transaction date 
4C of 1st day (before 5.30 PM) 
4C of pt day (before 4 PM) 
1001A, The Capital, B Wing, 10'" Floor, 
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in 
CIN: U74990MH2008NPL189067

<!-- Page 3 -->

Changes in dispute processing: 
N?CI 
'Jfffiftil   F,rrr,:r 
NATIONAL PAYMENTS CORPORATION OF IND/A 
Condition for customer compensation shall be calculated from transaction date to the customer 
account credited/reversed date if it is within T+l for P2P and T+S for P2M customer compensation 
will not be applicable (Example:-lf the P2P transaction amount is credited to the customer account 
on T+3 then customer will be eligible for 100X2=200 rupees compensation, similarly, if P2M 
transaction amount is credited to the customer account on T+7 then customer will be eligible for 
100X2=200 rupees compensation). 
For IMPS & UPI P2P transactions: 
Adjustment Type 
Within T+l 
*After T+l
Chargeback Accept/ Deemed Accept 
NA 
Applicable 
Pre-Arbitration Accept 
NA 
Applicable 
Pre-Arbitration Deemed / Deemed Accept 
NA 
Applicable 
Arbitration Accept 
NA 
Applicable 
Deferred Chargeback Accept/ Deemed Accept 
NA 
Applicable 
Deferred Pre-Arbitration Accept/ Deemed Accept 
NA 
Applicable 
Deferred Arbitration Accept 
NA 
Applicable 
* T +1 indicate transaction next day 4 PM for UPI & T +5.30 PM for IMPS.
For UPI Merchant transactions:
Dispute Name 
Within T+4 
*After T+4
Return/ Credit Adjustment 
NA 
Applicable 
Chargeback Accept/ Deemed Accept 
NA 
Applicable 
Pre-Arbitration Accept/Deemed Accept 
NA 
Applicable 
Arbitration Accept 
NA 
Applicable 
Deferred Chargeback Accept/Deemed Accept 
NA 
Applicable 
Deferred Pre-Arbitration Accept / Deemed Accept 
NA 
Applicable 
Deferred Arbitration Accept 
NA 
Applicable 
* * T +4 indicate 4 pm of 4th day from the next day of the transaction date.
Note: 
a.
Compensation shall not be applicable for wrong credits and fraudulent transactions.
b.
Existing Disputes TAT for chargebacks, re-presentments etc. shall remain same including for new
reason codes i.e. failed TXNs at merchant.
c.
New reason code "1065 (P2M) - Account debited but transaction confirmation not received at 
merchant location" will be introduced in RGCS while raising chargebacks for issuing bank to claim
compensation basis the customer information. Penalty shall only be applicable for the new reason
code i.e. for failed TXN at merchant. No penalty shall be calculated for exiting reason codes.
d.
Acquiring bank to initiate return/credit adjustments with specific MMT "Account debited but
confirmation not received at merchant location" to identify disputes arising due to such failed
Transactions.
1001A, The Capital, S Wing, 10'" Floor, 
Sandra Kurla Complex, Sandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in 
CIN: U74990MH2008NPL189067

<!-- Page 4 -->

NF'C/ 
'lfffifTz!   frrTrq 
NATIONAL PAYMENTS CORPORATION OF /NOIA 
e.
Where Acquirer/Merchant have failed to initiate a credit adjustment/refund, if the customer
lodges a complaint with the Issuing bank, Issuing bank to initiate a chargeback with specific MMT
(Member Message Text) as 'Account debited but confirmation not received at merchant location'
to identify disputes arising due to such failed Transactions.
f.
Till proposed changes are implemented in BCS & RGCS, the customer compensation on the
disputes/adjustments for transaction from 15th Oct, 2019 shall be calculated as per new RBI
circular and settle the same through manual adjustment in regular intervals, details of the same
shall be provided to members in report format on regular basis.
g.
NPCI shall provide cycle wise reports even on RTGS holidays. However RTGS settlement shall
happen as per RBI RTGS calendar. It should be noted that Banks NDC limit shall be refreshed only
once on RTGS holidays.
Changes in Adjustment Report: NPCI shall populate flag "Cust Comp" in SHDT70 column and "ADJ 
Raise Time" in SHDT71 which helps banks to know the status of compensation. 
NTSL reports/DSR: New line item will be introduced in DSR with narration "Customer compensation 
for Non-Compliance" under which compensation val
v
flect 
1001A, The Capital, S Wing, 10th Floor, 
Sandra Kurla Complex, Sandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in 
CIN: U74990MH2008NPL189067
