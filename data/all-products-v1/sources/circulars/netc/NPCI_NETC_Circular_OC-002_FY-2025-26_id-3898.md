# NETC | OC 002 | FY 26-27 | Revision of arbitration deemed continuation stage, automation of daily NRP/PRD fee settlement and PRD workflow enablement in NRCS

Circular/reference number: NPCI/2026-27/NETC/002

<!-- Page 1 -->

 
NPCI/2026-27/NETC/002        
    
 
 
       
                              April 13, 2026 
 
To, 
All Members of NETC 
 
Subject – Revision of arbitration deemed continuation stage, automation of daily NRP/PRD 
fee settlement and PRD workflow enablement in NRCS. 
 
With reference to the Circular NPCI/2024-25/NETC/002 dated October 05, 2024, on dispute lifecycle, 
associated fees and general process provisions, the below system changes are being implemented in 
NRCS back office with effect from May 15, 2026. 
1. Revision in Arbitration workflow: To encourage banks to reconcile reports and proactively 
act on disputes within timelines, it has been decided that arbitration cases raised post May 15, 
2026 shall be deemed accepted instead of deemed continuation. If no action is taken by the 
acquiring bank within 10 days from Arbitration Raise and the corresponding settlement 
accounting entries will be posted accordingly. 
2. Automation of NRP and PRD fee settlement: Fees associated with NPCI Review panel 
(NRP) and the Panel for Resolution of Disputes (PRD) along with applicable GST, will be 
debited from the losing party and will reflect in the subsequent Cycle - 1 DSR report available 
in NRCS back office. The corresponding GST details will be included in the GST payable and 
receivable reports of the subsequent month. This will be applicable for all NRP and PRD 
verdicts issued post May 15,2026. Annexure 1 to be referred for report related changes. 
3. Enablement of PRD workflow: With effect from May 15, 2026, NRP losing party will be able 
to refer the dispute to PRD through the NRCS back office. Annexure 2 to be referred for the 
arbitration life cycle. 
Member banks are advised to implement the necessary changes across all relevant systems to 
accommodate the new changes. The information herein may please be disseminated to all the officials 
concerned. 
 
With warm regards, 
 
 
Sd/- 
Giridhar GM 
Chief – Customer Success

<!-- Page 2 -->

 
         Annexure – I 
A) New Line Items in cycle-wise DSR Report 
The following new line items are included in the Cycle – 1 DSR report which is made available in 
NRCS. 
S. 
No 
New Line 
Item 
Description 
DSR Line Item 
1 
NRP Verdict 
NRP charges of ₹500 + GST debited from 
losing party 
Mem Inc Fee Amt Dr 
2 
PRD 
Acceptance / 
PRD 
Deemed 
Acceptance 
PRD Accepted by counter party. The NRP 
fees will be reversed to the winning party 
& NRP charges shall be recovered from 
the PRD losing party. 
Mem Inc Fee Amt Dr / Mem Inc 
Fee Amt Cr 
3 
PRD Verdict 
PRD charges of ₹3000 + GST debited 
from losing party 
Oth Fee Amt DR Fee Amt Dr 
If the PRD verdict given is different from 
NRP verdict, the NRP fees will be 
reversed to the winning party & NRP 
charges shall be recovered from the PRD 
losing party. 
Mem Inc Fee Amt Dr / Mem Inc 
Fee Amt Cr 
 
B) Changes in Incoming Report / Acknowledgment reports 
S. 
No 
New Line Item 
Description 
Incoming / 
Acknowledgment 
reports Line Item 
1 
NRP Verdict 
NRP charges of ₹500 + GST debited from 
losing party 
Fee Amt 2 
2 
PRD Acceptance / 
PRD Deemed 
Acceptance 
PRD Accepted by counter party. The NRP 
fees will be reversed to the winning party & 
Fee Amt 2

<!-- Page 3 -->

 
S. 
No 
New Line Item 
Description 
Incoming / 
Acknowledgment 
reports Line Item 
NRP charges shall be recovered from the 
PRD losing party. 
3 
PRD Verdict 
PRD charges of ₹3000 + GST debited from 
losing party 
Fee Amt 3 
If the PRD verdict given is different from 
NRP verdict, the NRP fees will be reversed 
to the winning party & NRP charges shall be 
recovered from the PRD losing party. 
Fee Amt 2 
 
C) New Line Items in Monthly GST Report 
S. No. 
New Column
Description 
GST report 
1 
NRP Verdict
Verdict Amount 
Monthly Payable Report 
2 
NRP Verdict Service Fee
Service Fee 
3 
NRP Verdict GST
GST 
4 
NRP Verdict Total
Sum of fee and GST 
5 
NRP Fee
NRP Fee charges 
6 
NRP GST
NRP Fee GST 
7 
NRP Total
Sum of fee and GST 
8 
PRD Acceptance
Acceptance Amount 
9 
PRD Acceptance Service Fe
Service fee 
10 
PRD Acceptance GST
GST 
11 
PRD Acceptance Total
Sum of fee and GST 
12 
PRD Verdict
PRD Verdict Amount 
13 
PRD Verdict Service Fee
Service fee 
14 
PRD Verdict GST
GST 
15 
PRD Verdict Total
Sum of fee and GST 
16 
PRD Fee
PRD Fee charges 
17 
PRD GST
PRD Fee GST 
18 
PRD Total
Sum of fee and GST

<!-- Page 4 -->

 
 
S. No.
New Column
Description
GST Reports
1 
NRP Fee
NRP Fee charges 
reversed
 
Monthly Receivable 
Report 
 
 
 
 
  
2 
NRP GST
NRP Fee GST
3 
NRP Total
Sum of fee and GST
4 
PRD Acceptance 
Acceptance Amount 
5 
PRD Acceptance Service Fe 
Service fee 
6 
PRD Acceptance GST
GST 
7 
PRD Acceptance Total
Sum of fee and GST 
8 
PRD Verdict
PRD Verdict Amount 
9 
PRD Verdict Service Fee
Service fee 
10 
PRD Verdict GST 
GST 
11 
PRD Verdict Total 
Sum of fee and GST 
12 
PRD Fee
PRD Fee charges 
13 
PRD GST
PRD Fee GST 
14 
PRD Total
Sum of fee and GST 
15 
NRP Verdict
Verdict Amount 
16 
NRP Verdict Service Fee
Service Fee reversal due 
to PRD 
Acceptance/Verdict
17 
NRP Verdict GST
GST 
18 
NRP Verdict Total
Sum of fee and GST 
 
D) Rejection reason codes: Member banks to take note of the following rejections codes from NRCS: 
 
S. No. 
Rejection reason code & description 
Explanation 
1 
5226, The PRD raise function can only be raised by 
who has lost the NRP verdict. 
PRD dispute can be raised only 
by NRP losing party. 
2 
5227, PRD should be raised only after the go live date 
PRD dispute can be raised only 
for disputes post go live of the 
PRD life cycle.

<!-- Page 5 -->

 
 Annexure – II  
B. Arbitration Lifecycle 
 
Funct
ion 
code 
Dispute 
Name 
Pre-
requisite 
Disputed Amount 
TAT 
Initiating 
Member 
Finan
cial / 
Non-
Finan
cial 
F/P 
New 
Eviden
ce 
submis
sion 
479 
Arbitration 
Raise 
Pre-
arbitration 
Declined 
Pre-arbitration 
raise amount 
10 Days from 
Pre-
Arbitration 
Declined 
Issuer 
Member 
N 
- 
- 
482 
Arbitration 
Withdrawal 
Arbitration 
Raise 
Arbitration Raise 
Amount 
10 Days from 
Arbitration 
Raise 
Issuer Bank 
N 
- 
- 
480 
Arbitration 
Acceptance 
Arbitration 
Raise 
Arbitration Raise 
Amount 
10 Days from 
Arbitration 
Raise 
Acquirer 
Bank 
F 
- 
- 
481 
Arbitration 
Continuation 
Arbitration 
Raise 
Arbitration Raise 
Amount 
10 Days from 
Arbitration 
Raise 
Acquirer 
Bank 
F 
- 
-

<!-- Page 6 -->

 
Funct
ion 
code 
Dispute 
Name 
Pre-
requisite 
Disputed Amount 
TAT 
Initiating 
Member 
Finan
cial / 
Non-
Finan
cial 
F/P 
New 
Eviden
ce 
submis
sion 
510 
Arbitration 
Deemed 
Acceptance 
Arbitration 
Raise 
Arbitration Raise 
Amount 
After 10 
Days from 
Arbitration 
Raise 
NRCS 
System 
F 
- 
- 
483 
NRP Verdict 
Arbitration 
Continuatio
n / Deemed 
Continuatio
n 
Settled transaction, 
(or) 
Settled transaction 
+ DA, 
(or) 
Settled transaction 
- CA 
60 days from 
Arbitration 
continuation / 
Deemed 
continuation 
NPCI 
F 
F/P 
- 
484 
PRD Raise 
NRP 
Verdict 
NRP verdict 
Amount 
10 days from 
NRP Verdict 
NRP Losing 
Member 
N 
- 
No 
485 
PRD 
Acceptance 
PRD Raise 
PRD Raise Amount
10 days from 
PRD Raise 
PRD 
Receiving 
Member 
F 
- 
No 
486 
PRD 
Continue 
PRD Raise 
PRD Raise Amount
10 days from 
PRD Raise 
PRD 
Receiving 
Member 
N 
- 
No 
487 
PRD 
Withdraw 
PRD Raise 
PRD Raise Amount
10 days from 
PRD Raise 
PRD 
Raising 
Member 
N 
- 
No 
511 
PRD 
Deemed 
Acceptance 
PRD Raise 
PRD Raise Amount
10 days from 
PRD Raise 
NRCS 
System 
F 
- 
NA

<!-- Page 7 -->

 
Funct
ion 
code 
Dispute 
Name 
Pre-
requisite 
Disputed Amount 
TAT 
Initiating 
Member 
Finan
cial / 
Non-
Finan
cial 
F/P 
New 
Eviden
ce 
submis
sion 
488 
PRD Verdict 
PRD 
Continue 
PRD Continue 
Amount 
90 days from 
PRD 
Continue 
NPCI 
F 
- 
NA 
 
Note:  
 
If the PRD request is accepted, deemed accepted or if the verdict given by PRD is different 
from NRP verdict, the NRP fees will be reversed to the PRD winning party after recovering 
from the losing party. 
 
NRP fee reversal (if applicable) shall be reflected within the NRP Fee / NRP GST / NRP Total 
columns of the respective Payable/Receivable GST reports based on the direction of 
settlement (debit/credit). 
o Cycle-1 DSR: NRP fee (including reversal) shall be reflected in Mem Inc Fee Amt Dr / 
Mem Inc Fee Amt Cr; PRD fee shall be reflected in Oth Fee Amt Dr.  
 
o Incoming/Acknowledgment: NRP fee (including reversal) shall be reflected in Fee Amt 
2 with applicable DR/CR indicator; PRD fee shall be reflected in Fee Amt 3. 
 
o Monthly GST: NRP and PRD fee GST impacts shall be reflected in the Monthly Payable 
and Monthly Receivable GST reports based on debit/credit direction. 
 
 
PRD fee will be charged post approvals from the competent authority.

<!-- Page 8 -->

 
Annexure – III 
Sample reports 
Reports.zip  
1. DSR Reports 
2. Incoming report 
3. Acknowledgment report 
4. GST reports
