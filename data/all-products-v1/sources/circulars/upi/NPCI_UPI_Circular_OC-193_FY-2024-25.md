# UPI | OC 193 | FY 23-24 | Compliance to UPI Technical specification – TRAN ID

Circular/reference number: OC-193

<!-- Page 1 -->

NPCL
NATIONAL PAYMENTSCORPORATIONOFINDIA
NPCI/UP1/OC N0.193/2023-24 March 28, 2024
To:
All Members of Unified Payments Interface (UPl)
Sub: Compliance to UPI technical specifications -TRAN ID
As per UPI technical specification transaction ID (TXNID) length must be 35 digits alpha
numeric. On analyzing the data, the following anomalies are observed:
1. Length of the transaction IDs: PsPs are not using consistent length of transaction ids
(current transaction ids (TXNID) are ranging from 4 digits to 35 digits) which is
inconsistent with the technical specifications of UPl.
2. Duplicate transaction Ids: Duplicate transaction Ids are used by PsPs while
originating the transactions.
1. Length of transaction ids:
a. In order to bring in standardization, it is mandated that the participating entities should
use the transaction ID with a length of 35 characters (alphanumeric) only.
b. Validation of field length should be implemented in the central system, any transaction
with transaction id not in compliance with the specification shall be rejected by the
system with appropriate reason. The exact date of implementation of validation in
central system shall be communicated separately however all the participants are
advised to take immediate measures to comply with technical specification to avoid
last minute rush.
2. Duplicate transaction Ids:
a. Validation is already in place, duplicate records are already validated and rejected.
Such rejections due to duplicate TXNID are causing immense customer dissatisfaction.
involved, a few transactions with duplicate IDs are getting processed in online system
however the same is getting rejected in the back office leading to settlement issues.
b. In the event of such duplicate transactions getting processed by the central system
leading to settlement issues, it may be noted that the liability will be shifted (defaulting
PsP shall be debited) to such originating entity as duplicate transaction ld is not in
compfiance with the technical specifications.
3. Additionally in a scenario wherein the banks have successful transactions in their switch /
internal system however such transaction/s are not present in the raw file provided then:
a) Remitting banks should not reverse the funds to the customer's account.
b) Beneificiary banks should hold funds in the beneficiary account.
Such cases should be reported to NPCl immediately for further course of action.
All participating entities are advised to take note and ensure compliance. The information
herein may please be disseminated to all the concerned officials for compliance.
With arm regards
1001A, The Capital, B Wing, 1oth Floor
Giridhar G M Bandra Kurla Complex, Bandra (E), Mumbai 4o0 O51
Chief - Customer Success & Govt Relations T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN: U74990MH2008NPL189067
