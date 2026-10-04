# IMPS IRCS - OC - 133_Revision of Wrong Payment Reversal Request (WP) and Introduction of Deferred Fraud Chargeback (DFC) in IMPS IRCS.

Circular/reference number: OC-133
Date: 21st July 2026

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPC!/IMPS/OCNo,133/2026-2027 21st July 2026
To,
All Members of Immediate Payment service (IMPS)
Subiect: Revision of Wrong Payment Reversal Reguest (WP). and Introduction of
Deferred Fraud Chargeback (DFC) in IMPS IRCS.
Based on feedback and enhancement requests received from member banks, certain
changes have been introduced in the IMPs IRCs dispute management module relating to
Wrong Payment Reversal Requests (WP) and Fraud Chargebacks.
Currently, the IMPS IRCS does not support the initiation of Deferred Wrong Credit and
Deferred Fraud Chargeback disputes in cases where a Transaction Credit Confirmation (TCC)
has already been raised for deemed approved transactions. To address this requirement, the
system has now been enhanced to allow the initiation of these dispute types as detailed below.
Deferred Wrong Payment Reversal Request (WP) and Deferred Fraud Chargeback
adjustments can now be raised even when a TCC has already been raised by beneficiary
bank for deemed approved transactions. (Refer Annexure A for detailed functionality.)
dedicated dispute category, similar to fraud chargebacks. Previously, these cases
were handled under the standard chargeback category (deemed approved) with only
a separate reason code. The enhanced setup now includes unique dispute types,
new reason codes, and specific flags, enabling wrong credit chargebacks to be
managed under a distinct dispute category (Refer Annexure B for detailed changes.)
New line items have been introduced in NTSL for the following three types of disputes
(Refer Annexure C for detailed changes),
i) Wrong payment reversal request (WP)
Deferred wrong payment reversal request
ii) Deferred fraud chargebacks.
Note: Other than the enhancements detailed in Annexure A, B & C, there are no changes to
the existing dispute management processes in IMPs IRCS. All other dispute types, workflows,
and processing rules shall continue to operate as currently implemented.

<!-- Page 2 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
15, 2026.
Member banks are requested to review the changes and ensure that the necessary updates
are made in all applicable systems and operational processes prior to the go-live date to
facilitate smooth adoption of the revised functionality. Kindly disseminate the information
contained herein to the officials concerned.
Warm Regards,
SDI-
Giridhar GM
Chief - Customer Success
Enclosed:
Annexure-A:Introducing Deferred Fraud &Deferred Wrong Payment-Reversal Request
Feature in IRCS
Annexure - B: Introducing a dedicated Wrong Payment Reversal Request process, separate
from the standard P2P chargeback workflow.
Annexure - C: New line items in NTSL

<!-- Page 3 -->

IOLN
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure - A
Introducing Deferred Fraud & Wrong Payment - Reversal Reguest Feature in IRCS
Dispute Type Flag Reason Reason Code Description TAT
Code
Deferred Fraud Chargeback Chargeback on TCC 45 Days
DFC 128
Raised Fraudulent Transaction from TXN
The amount has been
Deferred Fraud Chargeback
DFCA 129 recovered successfully from the 15
Accept
fraudulent customer's account
Lienmarkedhowevercustomer
Deferred Fraud Chargeback
DFCR 130 accaunts do not have sufficient 15
Representment
balance to debit
The amount has been
Deemed Deferred Fraud
DFCA 129 recovered successfully from the 15
Chargeback Accept
fraudulent customer's account
Deferred Fraud Chargeback FIR Copy not provided for the
DFCR 131 15
Representment disputed transaction
Deferred Fraud Chargeback
DFCR 132 Others 15
Representment
Deferred Wrong Payment - Customer transferred funds to 45 days
DWC DWC1
Reversal Request unintended beneficiary a/c from TXN
The amount has been
Deferred Wrong Payment -
DWCA DWC6 recovered successfully from the 25
Reversal Request Acceptance
customer's account
Deemed Deferred Wrong The amount has been
Payment - Reversal Request DWCA DWC6 recovered successfully from the 25
Acceptance customer's account

<!-- Page 4 -->

NPCI
NATIONAL PAYMENTS CORPORATIONOF INDIA
Lien marked; however,
Deferred Wrong Payment -
DWCR DWC7 customer accounts do not have 25
Reversal Request Rejection
sufficient balance to debit
Deferred Wrong Payment -
DWCR DWC8 Others 25
Reversal Request Rejection
If Deferred Wrong chargeback
is not accepted nor rejected
Deferred Wrong Payment -
DWDA DWC9 within TAT, then same must be
Reversal Request Acceptance
settled on deemed acceptance
basis.

<!-- Page 5 -->

NPCIN
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure - B
Introducing a dedicated Wrong Payment Reversal Request process, separate from the
standard P2P chargeback workflow.
ExistingDispute FlagReasoncode Proposed dispute flagand reason code
Flag
Dispute Flag & Reason Code Dispute Reason Code
Description TAT Description Description Description
TAT
Customer
Wrong
transferred funds to Customer transferred
Payment - WP..
Chargeback B - 45 unintended funds to unintended
Reversal 45
beneficiary alc - beneficiary a/c - WC1
Request
WC1
Lien marked Wrong
Lien marked customer
Representment customer accounts Payment -
WPR accounts do not have
R- 25 do not have Reversal
WC3 - 25 sufficient balance to
sufficient balance Request
debit - WC3
to debit - Wc3 Rejection
Customer cannot Wrong
Customer cannot be
Representment be contacted to Payment -
WPR contacted to obtain
R - 25 obtain debit Reversal
WC4 - 25 debit confirmation -
confirmation - Request
Wc4
WC4 Rejection
WPA successfully Wrong
WPA successfully
Chargeback from the Payment - WPA- from the unintended
A- 25 unintended Reversal
acceptance 25 customer account -
customer account Request
Wc2
- WC2 Acceptance
Wrong
Wrong Payment - Payment - Wrong Payment -
Chargeback Reversal Request Reversal WPD Reversal Request
A- 25
acceptance Deemed Request A-25 Deemed Acceptance
Acceptance - Wc5 Deemed - WC5
Acceptance

<!-- Page 6 -->

NPCIN
NATIONAL PAYMENTS CORPORATION OF INDIA
Annexure - C
New line items in NTSL
Dispute Adjustments
Description Ref. No I RRN I date
Deferred Fraud Chargeback Accept
FROM NT1 bank/604314808369/2026-02-12/FC 45004
Deferred Fraud Chargeback Accept TO NPC/26May2026130000/614516471748/2026-
HBK 05-25/F3 10
Total Deferred Fraud Chargeback Accept Amount 10 45014
Deferred Wrong Payment -Reversal Request Acceptance FROM NT1 bank/604314201194/2026-02-12/FC 10
Deferred Wrong Payment - Reversal NPCI26May2026130000/614516761307/2026-
Request Acceptance TO HBK 05-25/F3 10
Total Deferred Wrong Payment - Reversal Request Acceptance Amount 10 10
Wrong Payment - Reversal Request TO
NT1 bank/604314715439/2026-02-12/F3 45004
Wrong Payment-Reversal Request TO bank/604314495640/2026-02-12/FC
NT1 10
Total WrongPayment-Reversal RequestAmount 45014
Rejection FROM NT1 Wrong Payment - Reversal Request bank/604314495640/2026-02-12/FC 10
Wrong Payment - Reversal Reguest
Rejection FROM NT1 bank/604314715439/2026-02-12/F3 45004
Total Wrong Payment -Reversal Request Rejection Amount 45014
Adjustment Sub Total 45034 90038
Net Adjustment Amount 45004
Note: Raise and rejection/re-presentment of "Deferred Wrong Payment Reversal Request
(WP) and Deferred Fraud Chargeback (DFC)" are non-financial. Therefore, their line items are
not applicable in NTSL.
Deemed Deferred Fraud Chargeback Accept and Deemed Deferred Wrong Payment
implemented in NTSL (refer above NTSL. table for details).
