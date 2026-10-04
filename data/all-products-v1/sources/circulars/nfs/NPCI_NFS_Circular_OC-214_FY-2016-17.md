# NFS OC 214 Handling Single Dispute Multiple Transactions SDMT cases in DMS

Circular/reference number: NPCI/NFS/OCNo.214/2016-17
Date: 25th February, 2014

<!-- Page 1 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.214/2016-17 18th July,2016
To,
AllMembersofNational FinancialSwitch (NFS)
DearSir/Madam,
Sub:NFSATMNetwork-HandlingSingleDisputeMultipleTransactions(SDMT)casesin DMS.
We refer to 0C No. 109 dated 25th February, 2014 and 0C No. 113 dated 11th April, 2014 on the Guidelines for
handling cash withdrawal dispute for multiple transactions done by the cardholder at the ATM.The Guidelines
wereoperationalisedwitheffectfrom1stMarch,2014.
For cases where customer has done multiple cash withdrawal transactions at an ATM on a particular day and
customer complains for non-receipt of cash in one or more transactions, the Issuing bank should raise
chargeback under ‘Single Dispute Multiple Transactions (sDMT)' reason code and total chargeback amount
shouldbeequaltothedisputed amount.
As per the existing process, Issuing bank has to attach Dispute Letter containing the details of transactions and
amount disputed by the cardholder while raising chargeback under reason code‘sDMT'.This involves manual
processof gatheringthetransactiondetailsand preparingDisputeLetter.
As per the feedback received from member banks, we have made changes in DMs for automation. A'new menu
option‘Multiple Adjustments'is created in DMs for raising disputes under'Single dispute multiple transactions -
SDMT'reason code.This will allow Issuer to select the transactions to be grouped from the list of transactions
eligible for SDMT for raising the dispute.This will eliminate the manual process of preparing the Dispute Letter
anduploadingitinDMS.
Once a group of transaction is created by the Issuer, no chargeback or credit adjustment can be raised for such
grouped transactions. Issuers should ensure that proper care is taken while selecting the transactions to be
groupedunderSDMTandchargeback/s areraisedforthetotal disputed amount.
Acquirers should ensure that all the grouped transactions are checked while handling chargebacks raised with
reason code - SDMT. If the Acquirers come across any other failed transaction which has been grouped by the
Issuer, but chargeback is not raised against it i.e. total amount of unsuccessful transactions is more than the
total disputed amount, then the Acquirers should process credit for the balance amount outside of DMs.
New Menu options are created in DMS for handling Single Dispute Multiple Transactions (SDMT)cases.Details
ofthese newmenu optionsaregiven in AnnexureA.
Page1of3

<!-- Page 2 -->

Detailed process tobe followed for handling disputes related to SDMTis given inAnnexure B.
Chargebacks with reason SDMT can be raised through bulk file upload process. Separate Bulk file format to be
used for raising chargeback under reason code SDMT along with few illustrations is given in Annexure C.
Pleasenoteimportantlythat-
1. User shall be able to raise all disputes i.e. chargeback acceptance, representment, pre-arbitration, pre-
arbitration accept / reject and arbitration through “Multiple Adjustments' menu option for the
chargebacksraisedwithreasoncode'SDMT'.
Representment / acceptance for chargebacks not raised with reason code 'sDMT'needs to be done
throughexistingmenuoption.
2.User shall not be able to raise any other disputes / adjustments for the transactions which are grouped
under'SDMT'reasoncode.
3. User will not be able to select the reason code 'SDMT' through front-end using the existing menu option
-‘Adjustment.
4.Acceptance and representment for chargebacks raised with reason code 'SDMT'should be done through
front-end.Bulk option isprovided for onlyraising chargebackswith reasoncode'SDMT'.
There is no change in the process for handling Arbitration acceptance / withdrawal and Case
Presentment/Decisionprocess.
Onlygoodfaith representment will be allowedfor chargeback raised with reason code‘sDMT'.
7. Late reversal received for any transaction which is part of the ‘SDMT' group (irrespective of chargeback
being raised forthat transaction or not), will not be considered in settlement.
8. Credit adjustment overriding chargeback will not be allowed for any transaction which is part of the
'SDMT'group.
9. The existing adjustment report will have additional column i.e. ‘MultDisputeGroup' added on the
extreme right which will have details of the RRNs and chargeback amount for which the SDMT group is
formed. Bank should make note of the change in Adjustment report, especially if the report is used in
anysystematbank'send.
10.The disputes already raised under'SDMT'reason code before implementation needs to be handled as
pertheexistingprocess.
Please note that there is no change in the Guidelines mentioned in OC 109 and OC 113 other than those
mentionedabove.
The process for handling disputes / adjustments for normal chargebacks i.e.those not raised with reason code
'SDMT'includingthebulk uploadfileformat remains sameaspertheexistingprocess.
Theabove mentioned changes in DMS will be implemented witheffect from1st August, 2016.
Page2of3

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Please make note of the above mentioned process and disseminate the instructions contained herein to the
officialsconcerned.
Forany queries or clarification,please contact:
Name e-mailID MobileNumber
AvinashKunnoth avinash.kunnoth@npci.org.in 8879772725
Sarit Das sarit.das@npci.org.in 8108108694
AbhayParekh abhay.parekh@npci.org.in 8879772794
Yours faithfully,
RamSundaresan
Head-Operations
Encl: 1.AnnexureA-Detailsof Newmenuoptionscreated inDMSforhandling SDMTcases.
2. Annexure B - Process for raising disputes in DMS using menu option -'Multiple Adjustment' for SDMT
cases.
3.Annexure C-Bulk upload file format for raising chargeback
Page3of3
