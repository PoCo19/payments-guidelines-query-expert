# UPI | OC No. 231 | FY 2025-26 | Inclusion of purpose code and Lite reference number in adjustment report for UPI URCS Back-office System

Circular/reference number: NPCI/UPI/OCNo.231/2025-2026

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OCNo.231/2025-2026 March31,2026
To,
All Members of Unified Payment Interface (UPl)
Subiect: Inclusion of Purpose Code and Lite Reference Number in Adiustment Report.
We would like to inform you that as per member banks request, NPCl has included the
Purpose code' and 'LRN number' (Lite reference number) in adjustment report for the purpose
of reconciliation. Details of the changes are as follows:
Existing Header RevisedHeader Existing Length Revised Length
Chargeback Date
Purpose Code 10 (Numeric) 2 (Numeric)
"Chbdate"
ChargebackReference 35 (Alpha 35(AlphaNumeric)
LiteRefNo
Number"Chbref' Numeric) (No Change)
Note: The actual length of the Purpose Code in the URCs database will remain 10
characters. However, as per the technical specifications, the adjustment report will
display the Purpose Code as a 2-digit value. ln the future, if the length increases to 3
digits or more, it can be accommodated without any changes to the existing structure.
To accommodate these two additions, existing unused fields i.e. Chargeback Date and
Chargeback Reference Number have been replaced with Purpose Code' and “Lite Reference
Number" (refer Annexure - 1 for sample adjustment reports).
Note: Apart from the above two changes, the adjustment report ("csv" file format) remains
unchanged.
Go-Live Date: These changes shall be effective in URCS from May 15, 2026.
Member banks are hereby advised to make necessary changes and ensure all relevant
systems are updated to incorporate these changes prior to the go-live date.
The information herein may please be disseminated to all the officials concerned.
Yours Faithfully,
SDI
Giridhar GM
Chief-CustomerSuccess
1001A, The Capital, B Wing, 1Oth Floor
Bandra Kurla Compiex, Bandra (E), Mumbai 40o0 051.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONAL PAYMENTS CORPORATIONOFINDIA
Annexure -1
Existing Sample Adiustment Report Header
pinux! Adfdate Aditype Remitter Beneficiery Response Txnate Ixntime RRN Chhdate Chhret
41235711111824831744 45930 Chargeback Raise AAA 45915 0.67218 525816303062
4123571111 1830444544 45930 Chargeback Raise AAA RB 45915 0.67218 525816520274
8001222013 2016451584 年5930 Creft Adjustrnent AAA HHH 45915 0.67231 1525816301405
3453454385 238577408 45930 Fraudl Chargeback Hhh. AAA 45915 0.67219 525816829269
8001222013 249635072 45930|Credit Adjustment AAA 45915! 0.68113/5 1525816932678
Revised Adjustment Report Header
TXnLId Utd Adidate Adjtype Remitter Beneciery Respanse Tx的da健会 RRN Purpuse. LiteReNd
Coue
4123571111 1012217088 10-11-2025jCredlt Adjustmen CCC 23-10-202511:02:493 1529611825470 44101002004100635100166143239874700008
4123571111 119594137610-11-2025Re-presentment Raige CCC 23-10-2025 11:02:49 529611796950 44 01002004110535100166143239874700008
412357111|1474998016|10-11-2025chargebatkAcceptan HHH CCC 23-10-2025 11:02:49 529611590020 44101002004100535100166143239874700008
4123571111| 1859215104/ 10-11-2025|chargeback Paise CCC 23-10-2025/11:02:495 1529611796950 1401002004100585106166143269874700008
41235711111892302080 10-11-2025ChargebackRaise 23-10-202511:02:49529611596020 44 01002004100535100166143239874700008
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 400 051
