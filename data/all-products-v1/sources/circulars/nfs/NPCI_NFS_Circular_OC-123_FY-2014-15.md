# NFS OC 123 Credit Adjustment overriding charge back raise on the same date & Change in handling multiple charge backs as per OC109

Circular/reference number: NPCI/NFS/OCNo.12.3/2014-15

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.12.3/2014-15 June26,2014
To,
All MembersofNational FinancialSwitch(NFS)
Dear Sir/Madam,
Subject:Credit Adjustment overriding chargeback raised on the same date and
changesinhandlingmultiplechargebacksasperOc1og
Obiective:
in crediting the customer's account for failed ATM cash withdrawal transactions.This will also help in
reduction of chargebacks in the NFS network and bring in operational efficiency at the bank's end.
Existing Process:
When a chargeback is raised bythe Issuer in Dispute Management System (DMs), the option available
for Acquirer is to either accept or represent the chargeback after checking the status of the
transaction. In the present scenario, Acquirer is not able to raise credit adjustment in DMs if a
chargebackhasalreadybeenraised bythe Issuer.
Proposed process:
DMs will allow the Acquirer to raise credit adjustment overriding the chargeback provided following
conditions are meet:
a) Thecredit adjustment is raised on the sameday (i.e.up to 23:00 Hours)on which chargeback
was raised
b) The chargeback has not been accepted or represented by the Acquirer before raising the
credit adjustment
c) Thecreditadjustmentamountisequal tothe chargebackamount
Once the credit adjustment is raised as above, it shall override the chargeback i.e.the chargeback will
be cancelled.Areport of such cancelled chargebacks shall beavailable in DMS which can bechecked
bymembers inDMSthroughthefollowingMenuOption.
Reports->CR.Adj.overridingchargebackreport
The screen shots of menu option and sample report is provided in annexure A for reference.There
shall be no change in daily settlement report (NTSL). Issuer shall receive credit in daily settlement as
Page1of4
C-9, 8th Floor HAT/Phone:02226573150
RBIPremises cRT/Fax:02226571001
Bandra-Kurla Complex -/email:contact@npci.org.in
Bandra East aaisc/Website:www.npci.org.in
-400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

credit adjustments instead of chargebacks raised for these transactions. Issuer should credit the
customeraccountimmediatelyonreceiptofthecreditadjustments.
ChangesinhandlingofmultipleChargeback(oC1o9)
As per existingprocess, Issuer has to upload dispute letter while raising chargeback in DMSasper Oc
109dated 25th February2014under reason code'Single Dispute Multiple Chargeback'in any one of
thechargeback,preferablyforthefirsttransaction.
After implementation of credit adjustment overriding the chargeback, Issuer needs to upload the
dispute letter in all the chargebacks raised as per OC 109.This is required to ensure that the dispute
letter is available in DMs for remaining chargeback, if the chargeback for which dispute letter is
uploaded is cancelled due to processing of credit adjustment bythe Acquirerfor that transaction.
Process of handling credit adjustment by DMS under different scenarios is provided in Annexure Bfor
readyreference.
EffectiveDate:Theaboveprocess will beimplemented witheffect from3othJune2014.
We request you to take a note of the above and disseminate the changes implemented to the officials
concerned.
Foranyqueriesorclarification,pleasecontact:
1.AvinashKunnoth,NFSOperations,E-mailID-avinash.kunnoth@npci.org.in;Mobile-8879772725.
2.AbhayParekh,NFSOperations,E-mail ID-abhay.parekh@npci.org.in;Mobile-8879772794.
Yoursfaithfully,
RamSundaresan
Head-NFS
Page2of 4

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-A
Menuoptionfordownloading Verification Reversal Report
NpCI-DisputeManagement System
Admin Adjustments Reports Files Reports MIS Bulk Insert INFO ContactUs Services and DownTime/Bin Add BIN
LastLogin:25/06/20143AdjustmentReport Statistos Form Addition
Chargeback Report
ScheduledDownTimes RepresentmentReport
ArbitrationReport
Check JP Proof NFsDisputeManagementSystem
MISArbitrationReport
VerificationAnd Reversal The National Financial Switch facilitates inter-connectivity between the Banks'
TransactionReport ATM Switches and provides to the customers a wider reach across the country.
Cr.Adj.overriding
Chargeback Report Enabling on-line resolution...Business needs of NFs members.
NPcl-DisputeManagement System
NPCl-DisputeManagementSystem
Page3of 4

<!-- Page 4 -->

Annexure-B
Process of handling Credit Adjustments in DMS where chargeback is raised
HandlingCreditAdjustmentbyDMSapplication
S.No Scenario
ActionbyDMs
Chargeback is notraised -Credit Adjustment will be allowed
Chargebackisraisedbuthasnotbeenaccepted -Chargeback will be rejected and
orrepresented -Credit Adjustment will beallowed, if raised on
sameday
Chargeback is raisedand represented onthe -Chargebackand representmentwill beconsidered
sameday -CreditAdjustmentwill notbeallowed
Chargebackisraisedandacceptedonthesame -Chargeback will be considered
day - Credit Adjustment will not be allowed
AttempttoraiseCreditAdjustment on
subsequentdayof raisingchargeback (i.e.after DMswill not allowAcquirerto raise Credit
chargeback is considered for settlement) AdjustmentasChargebackhasalreadybeensettled
ActionbyIssuer:
1. Issuer need to check credit adjustment overriding chargeback report'to identify the
cancelled chargebacks
2.Issuer shall receive credit for these transactions by way of credit adjustments instead
of chargeback in the daily settlement report. Bank should credit the amount to
cardholder's account immediately on receipt of the credit adjustments.
3. Issuer should upload dispute letter for all the chargebacks raised as per OC 1o9 with
reasoncode'SingleDisputeMultipleChargeback'
ActionbyAcquirer:
1. Acquirer will be allowed to raise credit adjustment on the same day of receiving
chargeback if itisnotrepresentedoraccepted inDMS.
2. There shall be no change in process to be followed by Acquirer for addressing
chargebacks raised as per OC 109formultipletransactions.
Page4of4
