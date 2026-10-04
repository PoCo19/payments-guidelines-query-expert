# UPI | OC No. 221 | FY 2025-26 | Implementation of L5C compliance penalty in URCS for lite L5 transactions

Circular/reference number: OC-221

<!-- Page 1 -->

NPCL
NATIONAL PAYMENTS CORPORATIONOF INDIA
NPCI/2025-26/UPI/221 Sep 12, 2025
To,
All Members of Unified Payment Interface (UPl)
Subject: Implementation of L5C compliance penalty in URcs for Lite L5 transactions
UPl Lite X allows users to make UPl payments offline, without internet, by utilizing Near Field
Communication (NFC) technology, building upon the existing UPI Lite feature.
If a UPI Lite X user uninstalls or reinstalls the app, or switch to the other device, the NPCl's
MCB (Mini Core Banking System) places a temporary hold on the last available balance for 5
days. This precaution is to ensure that any pending offline transactions are processed. If no
such transactions are received (online) within this timeframe, the hold is lifted, and the balance
is updated in the system with a specific response code on the 5th day.
When the payer bank receives an L5 transactions in the raw file with the balance amount
remaining. Payer bank is expected to reconcile these transactions, debit the UPI Lite X GL
account and credit the customer's CAsA account (Current and Savings Account). Basis the
followed by the banks resulting in complaints. Furthermore, only the Payer bank is aware of
the L5 transaction status, which prevents other parties (payee, payer, beneficiary bank, and
NPCl) from updating the end customers.
To provide the visibility to the action taken by the payer bank an option has been introduced
to enable the payer bank to update the L5C (L5 confirmation) in the URCS back-office system
after debiting the L5 amount from their Lite-x GL and crediting the CASA. This helps all other
parties of the transaction to respond customer complaints suitably (if any).
system within the specified timeframe on similar lines of TCC/RET, the process involves,
Setting up the process for the L5 status update flag i.e. L5C, use reason codes as
follows,
L5C - O01 for successful debits to the pool account and credits to the customer's CASA
L5C - 02 for instances where the customer's CASA cannot be credited.
'0otA, The Capital, B Wing, 1oth Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 O51.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCIV
NATIONAL PAYMENTS CORPORATION OF INDIA
A separate report will be provided to facilitate access to L5 transactions, enabling
banks to take necessary actions in CAsA post-reconciliation is done.
The deadline for updating L5C in URCS is before 24:00 hours on T+1, with T+0 being
the day the L5 is updated in the raw file.
Failure to update the L5 status with L5C by 24:00 hours on T+1 will result in the
Go-Live Date: The above process shall be implemented in URCS w.e.f. 21 st Oct 2025.
Warm Regards,
SD/-
GiridharGM
Chief - Customer Success
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex,Bandra (E), Mumbai 4oo O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NP1189067

<!-- Page 3 -->

NPCI
NATIONAL PAYMENTS CORPORATIONOF INDIA
Annexure -1
L5C Compliance and Penalty Rules
TAT Compliance Rules
T+0 Mon L5 updated date in raw file (1st Aug'25)
Payer bank is expected to update the status with L5C -01 or 02 before 24 hrs.
T+1 Tue
(2nd Aug'25)
Penalty will be processed with Rs.25 in 1C everyday (i.e. 21 hrs to 2. hrs business
T+2 Wed cutover of previous day (Tuesday) and RTGS posting done on Wed in the first.
(2nd Aug'25 - 1C)
NOTE: GST is NOT applicable for the L5C penalty amount.
Sample table for understanding penalty settlement with rules
TAT Date Compliance Rules Penalty
T+o Mon 01-Aug-25 L5 updated date in raw file (1st Aug'25) NIL
Payer bank is expected to update the status with L5C -
T+1 Tue 02-Aug-25
Reason Code - 01 or 02 before 24 hrs. Nil.
TAT expires and Penalty will be levied (File dtd:2-Aug-25
T+2 Wed 03-Aug-25
1C) Rs.25
T+3 Thu 04-Aug-25 TAT expires and Penalty wil be levied Rs.50
T+4 Fri 05-Aug-25 TAT expires and Penalty will be levied Rs.100
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E). Mumbai 4oo O51.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NPCIN
NATIONALPAYMENTS CORPORATIONOFINDIA
L5C Pernalty Report
Netional Payments Corporatlon of Indla
PanaltyRaportforthebankCSBBank Limltedforthe perlodfrom29/06/2025to12:00AM
[UTXNtD] [RRN] [RC] [TXnt [Remtte] (Banaficlarv]  [Payer [Payen [Amount] [Penality [Txn/Ad] Date]  [CalendarDay] [PanaltySettledData]
ype] PSPI PSP Amount)
79 4b5e18005ec54b55a24d27d3a7c33814 10 12 17 13 15 B360368d817c45bdbe4dff8d5b4e0857 330973426545 Bb8ba17de81d447aad07ce828dod:21a 622586150277 Ob0c815daeb74n3e9004d18697ee42bs861238710365 a551eb3e177f45b5b31821d9e321679 ee732775fa394e87ace58c9db0b12362 622586159277 9e6b7db04764402a8cd097t9a4da47fb622586159277 e732775fa394e87ace58c9db0b12362 ee732775fa394e87ace58c9db0b12362 ba64e9ff326e454482c8bc81383ae775522586159277 9e7b6rb4e05c4a740eaecbe9f078c272483175838594 92058fef06384e40a28c9b5507824704622585159277 ab99152fdf21454181a8071a5c8fo812 ab99161fdf21454182a8071a5c8fe81a 622586159277 622586159277 622586159277 884370915755 122586159277 622586159277 L5 L5 L5 L5 LS U3 U3 U3 U3 U3 U3 U3 U3 HDF HDF HDF HDF HDF HDF HOF JOH HDF HDF HDF JOH HDF HDF HDF HOF HDF HDF HDF HDF HDF HDF HDF HDF NDF HDF HDF HOF HDF HDF HDF HDF HDF HOF HDE HDF HDF HDF HOF HDF HDF HDF HDF HOF Hof HDF HDF HDF HDF HDF 337 231 426 26 25 25 25 25 25 50 25 25 25 50 50 50 50 30-12-2024 15:57:33 26-D5-202S 00:00 23-02-2025 11:20:05 26-05-2025 00:00 23-02-2025 11:21:42 26-05-2025 00:00 23-02-2025 11:21:42 26-05-2025 00:00 23-02-202S 11:20:0S 26-05-202S 00:00 30-12-2024 15:57:32 26-05-2025 0D:00 30-12-2024 15:57:32 26-05-2025 0D:00 30-12-2024 16:51:37 26-05-2025 00:00 30-12-2024 19:07:40 26-05-2025 00:00 Z3-02-2025 11:20:0S 2G-D5-2025 0D:00 15-03-2025 12:18:09 26-05-2025 0D:00 30-12-2024 16:05:07 26-05-2025 0D:00 15-03·2025 12:26:31 26-05·2025 00:00 23-02-2025 11:17:35 26-05-2025 00:00 30-12-2024 25:57:33 26-05-2025 00:00 26-05-2025 00:00 26-05-2025 00:00 2G-05-2025 00:00 26-05-2025 00:00 26-05-2025 00;00 2G-05-202S 00:00 26-05-2025 00:00 26-05-2025 00:00 26-05-2025 00:00 26-05-2025 00:00 26-05-2025 00:00 26-05-7.07.5 00:00 26-0S-2D2.5 00:00 Z6-05-2025 00:00 26-05-2025 00:00
L5 PenaltyReportPayable.CSB-ISS
L5C Separate Report
NPCl will provide a separate L5C report to the Payer bank with following columns for member
banks to use it with ease for daily reconciliation purpose.
S. No COLUMN HEADER S. No COLUMN HEADER
Payer Bank - Remitting Bank (3-digit short
IFSC
code)
Payee Bank -Beneficiary Bank (3-digit
TXN Type
short code)
TXN Date Remitter Number
TXN Time 11 Amount
CRT Date 12 LRN
Response Code 13 Payer PsP (3-digit short code)
RRN 14 Payee PsP (3-digit short code)
DSR/NTSL Line Items (Narration)
L5C Penalty debit for not updating the status Penalty payable
36 L.5C penalty debit for not updating the status penaity payable (T+1) (T+2) (T+3) 575
1001A. The Capital, B Wing, 10th F1oor,
Bandra Kurla Complex. Bandra (E), Mumbai 4oo O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067
