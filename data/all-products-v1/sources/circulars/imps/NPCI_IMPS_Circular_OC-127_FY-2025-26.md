# IMPS | OC 127 | FY 25-26 | Auto Acceptance & Rejection of Chargeback

Circular/reference number: OC-127

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
NPC1/ IMPS/OC No. 127/2025 - 2026 Jul 10, 2025
To,
All Members of Immediate Payment service (IMPS)
Subiect: Auto acceptance & reiection of chargeback basis the TCC & Returns
Chargebacks are often initiated by remitting banks before beneficiary banks can act on IMPS deeimed
onwards for above 25,000 Rs transaction in IMPS IRCS system, due to which beneficiary banks are not
getting sufficient time to reconcile and process returns (RET/TCC) proactively before a dispute is taking
shape of chargeback. Currently in such cases where charge back is already raised the TCC/RET records
are rejected by the system, if the banks do not handle such rejections the chargeback will get deemed
accepted along with RBI penalty.
To address these challenges and improve the efficiency of dispute resolution, we are implementing auto
acceptance/rejection of chargeback basis the TCC/RET raised by the beneficiary bank in next settlement
cycle after the chargeback is already raised. Note, this revised process is applicable only for bulk upload
option & ODIR not in front end option.
Key Points: -
Auto acceptance of the chargebacks is applicable only for deemed approved P2P chargeback
not applicable for Deferred chargebacks.
Auto acceptance/Re-presentment is applicable for bulk upload and ODIR based RET & TCC
(102/103) only.
Not Applicable for front end option, because if chargeback is already raised then IRCs will
show the chargeback accept/Reject option to beneficiary bank, not the RET & TCC (102/103).
Other than above mentioned points there are no changes in any of the dispute rules/process such
as TAT, penalties, compensation, cutovers, settlement, fees, GST, reports/files etc.
Member banks should ensure to raise correct TCC (102/103) to avoid moving the chargebacks
life cycle to pre-arbitration/arbitration.
TAT for all disputes viz. raise Chargeback, TCC, RET is 45 days, thus, auto
acceptance/rejection also follows the same TAT.
Note: Refer Annexure-l for rules and process set for auto acceptance/rejection of the chargeback.
The above functionality will be implemented in IRCS with effect from Aug 27, 2025.
Member banks are advised to take a note of the above and disseminate the information contained herein
to the officials concerned.
Warm Regards.
SD/-
Giridhar GM
Chief - Customer Success

<!-- Page 2 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-1
Refer below the table for rules and process set for auto acceptance/rejection of the chargeback.
TYPE TXN TXN RC Remitter Raised Settlement Same/Next Beueflciary Raised Settlement Same/Next Functionality IRCS Dispute New Reason New Acceptance! Auto
Cycle Cycle Flag. Code Rejection Status
c.g. 5C
Deemed (Same IRCS will reject chargeback
P2P-F3-FC (RC-08) Chargeback e.g. 5C RET Settlement and process RET (Existing NA NA Na
cycle) Functionality - No change)
e.g. 6C IRCSwillrejectRETanddo
P2P-F3-FC Deemed (RC-08) Chargeback e.g. 5C RET Settlement (Next chargeback (New the atto acceptance of 9886 Acceptance will Auto Chargeback
cycle) Functionality) be done by IRCS
e.g. 5C
Deened (Same IRCS will reject clhargeback
P2P-F3-FC (RC-08) Chargeback e.g. 5C TCC Settlement and process TCC (Existing NA Na
cycle) Functionality - No change)
e.g. 6C IRCS will do auto Auto Chargeback
P2P-F3-FC Deemed (RC-08) Chargeback e.g.sC TCC Settlenent (Next chargeback (New Representnext the 9887 wil be done by Representment
cycle) Fuctionality) IRCS
