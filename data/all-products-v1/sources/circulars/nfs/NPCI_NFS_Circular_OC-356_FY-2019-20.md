# Circular 356 - Change in dispute resolution rules - Union Pay International (UPI) cards on NFS ATM Network

Circular/reference number: NPCI/NFS/OCNo.356/2019-20
Date: 24th January, 2017

<!-- Page 1 -->

NPCIL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.356/2019-20 10th December,2019
To
AllMembersofNationalFinancial Switch(NFS)
Madam/DearSir,
Sub: Change in dispute resolution rules - Union Pay International (UPl) cards on NFS ATM
Network
We refer to Operating Circular (OC) number 240 dated 24th January, 2017 on acceptance of JCB
and UPI cards on NFS ATM Network, wherein, we had requested NFS members to enable JCB and
UPICardsacceptanceonBank'sATMs.
In this regard, NFs members have been given Dispute Management System (DMS) access to
download the settlement and reconciliation reports, and to raise disputes / adjustments.
Presently,UPl card's ATM disputes follows two different life cycles classified under Signature
based (UPI-C)and Pin based (UPI-D) dispute lifecycle inNFSDMS for resolutions.
The Card is identified basis the Card type marked against each Bin in Bin Management file. If the
Card type is marked as'C'then the transaction will follow Signature Based Dispute Life Cycle and
if the Card type is marked as'D'then the transaction will follow Pin Based Dispute Life Cycle.
Effective 01st December, 2019, UPl has integrated both dispute life cycles to simplify the dispute
resolution procedures and shorten the Chargeback timeframe. The new dispute life cycle is
applicableforATMdisputes irrespectiveoftransactiondateand Cardtype.
Please refer Annexure A for the change in Dispute resolution rules and Turn Around Time (TAT).
The UPl dispute resolution rules other than mentioned in the Annexure A shall be applicable as
containing new disputes resolution guidelines applicable to UPl card acceptance on the NFS ATM
network is also made available to members in DMs.[Menu option:Info >>>lmportant Documents]
Please note importantly that these changes in back office shall take some time. Meanwhile,
Acquirers need to follow new dispute rules/TAT for the disputes/adjustments received from 1st
December,2019onwards.
Please make note of the above and disseminate the instructions contained herein to the official
concerned.
Foranyqueriesorclarification,pleasecontact:
Name E-mail MobileNumber
ImranPatni Imran.Patni@npci.org.in 8291968533
Pankaj Samarth pankaj.samarth@npci.org.in 8108122861
AvinashKunnoth avinash.kunnoth@npci.org.in 8879772725
Yours faithfully,
Sm.Nam
SaiprasadNabar
Chief-OnlineProductsOperations
Encl:1.AnnexureA-ChangeinUnionPayInternational (UPl)disputeprocess&TAT

<!-- Page 2 -->

Annexure-A
Change in Union Pay International (UPl) dispute process &TAT
Sr. No. UPIDisputeRules-ATM Existing-till30thNov,2019 New-Effective1st Dec,2019
Technical violation
processing fee of us This technical violation This technical violation processing
dollar 100 at Arbitration processing fee was not fee is applicable for arbitration
level applicableforarbitration. now.
The new single dispute life cycle to
Therewere 2different dispute simplify the dispute resolution
Pin based (CUD) and procedures, shorten the
Signaturebased (CUC) resolution rules for Pin based
and Signature based card Chargeback timeframe and to
dispute life cycles integrate the dispute processing
transactions.
procedures for debit card and
credit cards.
Reason codeforRetrieval
Request
#1004-Transaction The UPl Issuers had rights to These two reason codes are
receiptrequestbyJustice raise Retrieval request under removed in new dispute life cycle
# 1027 - Transaction these reason codes before and no longer available for UPl
receipt request by card raising chargebacks. Issuer while raising Retrieval
member after responded request.
Inquiry
Thenewdispute lifecycle has
added reason code 6351.The UPI
IssuersmustsubmitRetrieval
Retrieval Request reason requestwith reason code6351
code Thereason code6351 was not before raising chargeback under
#6351-Disputeon available for UPl Issuers for reason codes
Goods/Servicedelivery raising Retrieval request. # 1065 - Cash not received
# 4532-Refund not processed.
The Chargeback right is not
subject to the Acquirer's
fulfillment.
Thereasoncode1050wasnot The new dispute life cycle has
Inquiry and Retrieval addedreasoncode1050.TheNPCl
available for NPCl acquirers
Request fulfilment code acquirer can fulfill Inquiry and
#1050 -Supporting while submitting the response
to Inquiryand Retrieval Retrievalrequestwithreasoncode
document not available 1050 if supporting documents are
Request fulfillment.
notavailable.
The new dispute life cycle has
Balance Inquiry The UPl Issuers had rights to removed thereason code 1072
Chargeback reason code raise Chargebacks under usedtoraisechargebackon
# 1072- Fees refund for Reason code 1072 for unsuccessful Balance Inquiry
unsuccessful Balance unsuccessful Balance Inquiry transactions.
Inquiry transactions.

<!-- Page 3 -->

Sr. No. UPIDisputeRules-ATM Existing-till 30thNov,2019 New-Effective1st Dec,2019
TheInquiry and Retrieval
Chargeback rule and TAT request is optional, but The Inquiry and Retrieval request
of Reason code mandatory subject to UPI is mandatory before chargeback.
1065 Cash not Card type. The Chargeback TAT is reduced to
received TheChargeback TATwas 185 125 days from transaction date.
days from transaction date.
The Inquiry and Retrieval
Chargeback rule and TAT request is optional, but The Inquiry and Retrieval request
of Reason code mandatory subject to UPI is optional before chargeback.
# 1071-Dispute on Debit Card type. The Chargeback TAT is reduced to
Adjustment The Chargeback TAT was 185 65 days from transaction date.
days from transaction date.
Chargeback rule and TAT The Inquiry and Retrieval
of Reason code requestis optional, but The Inquiry and Retrieval request
# 1121 Transaction mandatory subject to UPI is optional before chargeback.
received Decline Card type. The Chargeback TAT is reduced to
Authorizationresponse The Chargeback TAT was 185 125 days from transaction date.
days from transaction date.
UPI Fraud Reporting and
Management System It is optional for UPl Issuer to It is mandatory for Upl Issuer to
10 (FRMS) report the disputed report the disputed transaction to
Chargeback under reason transaction to UPI FRMS UPI FRMS before raising
code#4562-Counterfeit before raising Chargeback. Chargeback.
Card
Chargeback reason code Thereasoncode4532wasnot UPl Issuer has rights to raise
11 # 4532 - Refund not available for UPl Issuers for chargeback under new reason
processed raising Chargeback. code 4532, if refund is not
processed by NPCl acquirer.
Post-merger of two dispute cycles
(i.e. Signature based & PIN based)
into one dispute cycle, the
representment rights are not
The representment rights available for NPCl Acquirer on
were available for NPCI chargebacks received.
12 Representmentrightson acquirer on Chargeback raised recourse,NPCl Acquirer shall raise
chargebacks under Signature based life Pre-arbitration for rejecting the
cycle and not available under Chargeback.
Pin based life cycle. If the Acquirer does not respond
to the Inquiry and Retrieval
request within time frame, then it
has no right to raise Pre-
arbitration.
