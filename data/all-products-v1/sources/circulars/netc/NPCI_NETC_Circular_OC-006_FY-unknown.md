# NETC | OC 006 | FY 26-27 | Implementation of Duplicate Transaction Validation for NETC Transactions

Circular/reference number: NPCI/2025-26/NETC/006

<!-- Page 1 -->

 
NPCI/2025-26/NETC/006 
Jun 24, 2026 
To, 
All NETC Member Banks 
Subject: Implementation of Duplicate Transaction Validation for NETC Transactions 
This 
is 
with 
reference 
to 
IHMCL 
circular 
(Ref. 
No. 
IHMCL/Duplicate-Transaction-
Logic/2023/203661/213 dated May 17, 2023) regarding the check and prevention of duplicate 
FASTag transactions and the required controls to be implemented by acquiring systems. However, 
it has been observed that duplicate transactions are still being routed to the NETC system by certain 
entities, resulting in increased customer grievances and instances of duplicate debits. To address 
the aforesaid issue, IHMCL has directed NPCI to implement secondary validation for NETC 
transactions to identify and decline duplicate transactions. 
Under this validation logic, debit transactions will be validated against transactions processed during 
the preceding 48 hours, and duplicate transactions shall be identified and declined where the 
transaction meets any of the following conditions with reference to a previously accepted or deemed 
accepted transaction: 
Rules 
Plaza Type 
Transaction 
ID 
Tag 
ID 
Plaza ID 
Reader Read Time 
(RRT) 
Lane 
Direction 
1 
National, State, 
Parking 
Same 
Same 
Same 
Same 
Same 
2 
National, State, 
Parking 
Different 
Same 
Same 
Same 
Same 
3 
National 
Different 
Same 
Same 
Within 10 minutes 
of the earlier 
accepted or 
deemed accepted 
transaction 
Different 
4 
National 
Different 
Same 
Same 
Within 15 minutes 
of the earlier 
accepted or 
deemed accepted 
transaction 
Same

<!-- Page 2 -->

 
Any special configuration plaza deviating from the aforesaid validation logic, or requiring whitelisting, 
shall require written approval from IHMCL/NHAI and prior notice of at least 15 days to NPCI. Non-
financial and credit transactions shall remain excluded from the above duplicate validation checks.  
We would like to inform you that the development and testing of this duplicate transaction validation 
logic have been completed, and the feature is planned to be deployed in the NETC production 
environment on June 30, 2026. 
Please note that the primary responsibility for ensuring that only valid and unique transactions are 
processed and submitted to NETC system, in line with IHMCL technical specifications and 
guidelines, will continue to remain with the originating (acquiring) banks. The secondary validation 
implemented by NPCI is an additional control and shall not be treated as a substitute for the controls 
required to be implemented by member banks/participants. For all approved transactions, acquiring 
banks shall monitor for duplicate transactions in accordance with the above referenced IHMCL 
circular and shall raise appropriate credit adjustments, wherever applicable. 
For further details, please refer to Annexure I. 
Warm regards, 
 
Sd/- 
Giridhar GM 
Chief – Customer Success 
National Payments Corporation of India

<!-- Page 3 -->

 
Annexure – 1 
Rule 1: A transaction shall be identified as duplicate and declined where the second transaction 
carries the same Transaction ID, same Tag ID, same Plaza ID, same Reader Read Time, and same 
Lane Direction as the first accepted or deemed accepted transaction, provided the transaction 
timestamp is within the last 48 hours.  
NETC rejection error code: 394 – Duplicate transaction presented for a tag with same transaction 
ID with same RRT from same plaza. 
RespPay Decline risk score: 961 
Exclusion: Non-financial and credit transactions. 
Transacti
on No. 
Directio
n 
Tag ID 
Plaza 
ID 
Reader 
Read 
Time 
Acq
uirer 
Ban
k 
Txn 
Initi
ated 
Tim
e 
Transacti
on Status 
ABCDXX1 
N 
3416XXXXXXXXXXXXXXX
XX15A0 
12345
6 
10-05-
2026 
16:02 
10-
05-
2026 
16:0
4 
Accepted 
ABCDXX1 
N 
3416XXXXXXXXXXXXXXX
XX15A0 
12345
6 
10-05-
2026 
16:02 
10-
05-
2026 
16:1
0 
Declined 
 
Rule 2: A transaction shall be identified as duplicate and declined where the second transaction 
carries a different Transaction ID but the same Tag ID, same Plaza ID, same Reader Read Time, 
and same Lane Direction as the first accepted or deemed accepted transaction, provided the 
transaction timestamp is within the last 48 hours.  
NETC Rejection error code: 395 - Duplicate transaction presented for a tag with different 
transaction ID with same RRT from same plaza. 
RespPay Decline risk score: 962 
Exclusion: Non-financial and credit transactions.

<!-- Page 4 -->

 
Transacti
on No. 
Directio
n 
Tag ID 
Plaza 
ID 
Read
er 
Read 
Time 
Acquir
er 
Bank 
Txn 
Initiate
d Time 
Transacti
on Status 
ABCDXX1 
N 
3416XXXXXXXXXXXXXXXXX
15A0 
12345
6 
10-05-
2026 
16:02 
10-05-
2026 
16:04 
Accepted 
ABCDXX2 
N 
3416XXXXXXXXXXXXXXXXX
15A0 
12345
6 
10-05-
2026 
16:02 
10-05-
2026 
16:10 
Declined 
 
Rule 3: A transaction shall be identified as duplicate and declined where the second transaction 
carries a different Transaction ID but the same Tag ID and same Plaza ID, and its Reader Read 
Time falls within 10 minutes of the first accepted or deemed accepted transaction with Lane Direction 
being different, provided Merchant Sub Type = National and the transaction timestamp is within the 
last 48 hours.  
NETC Rejection error code: 396 - Duplicate transaction presented for a tag in opposite direction 
with RRT within 10 minutes of 1st transaction from same plaza. 
RespPay Decline risk score: 963 
Exclusion: Non-financial and credit transactions 
Transacti
on No. 
Directio
n 
Tag ID 
Plaza 
ID 
Read
er 
Read 
Time 
Acquir
er 
Bank 
Txn 
Initiate
d Time 
Transacti
on Status 
ABCDXX1 
N 
3416XXXXXXXXXXXXXXX
XX15A0 
12345
6 
10-05-
2026 
16:02 
10-05-
2026 
16:04 
Accepted 
ABCDXX2 
S 
3416XXXXXXXXXXXXXXX
XX15A0 
12345
6 
10-05-
2026 
16:10 
10-05-
2026 
16:12 
Declined 
ABCDXX3 
S 
3416XXXXXXXXXXXXXXX
XX15A0 
12345
6 
10-05-
2026 
16:14 
10-05-
2026 
16:16 
Accepted

<!-- Page 5 -->

 
Rule 4: A transaction shall be identified as duplicate and declined where the second transaction 
carries a different Transaction ID but the same Tag ID and same Plaza ID, and its Reader Read 
Time falls within 15 minutes of the first accepted or deemed accepted   transaction with Lane 
Direction being the same, provided Merchant Sub Type = National and the transaction timestamp is 
within the last 48 hours.  
NETC Rejection error code: 397- Duplicate transaction presented for a tag in same direction with 
RRT within 15 minutes of 1st transaction from same plaza. 
RespPay Decline risk score: 964 
Exclusion: Non-financial and credit transactions. 
Transacti
on No. 
Directio
n 
Tag ID 
Plaza 
ID 
Read
er 
Read 
Time 
Acquir
er 
Bank 
Txn 
Initiate
d Time 
Transacti
on Status 
ABCDXX1 
N 
3416XXXXXXXXXXXXXXXXX
15A0 
12345
6 
10-05-
2026 
16:02 
10-05-
2026 
16:04 
Accepted 
ABCDXX2 
N 
3416XXXXXXXXXXXXXXXXX
15A0 
12345
6 
10-05-
2026 
16:14 
10-05-
2026 
16:16 
Declined 
ABCDXX3 
N 
3416XXXXXXXXXXXXXXXXX
15A0 
12345
6 
10-05-
2026 
16:18 
10-05-
2026 
16:20 
Accepted 
 
Note: Existing duplicate validations for scenarios involving the same Transaction ID and the same 
Merchant ID within the preceding 7 days shall continue, and such transactions shall be declined with 
the existing response code 201. It may further be noted that, at present, banks/plazas receive risk 
scores (Txn.RiskScores) only in Accepted and Deemed Accepted transaction responses. Pursuant 
to this implementation, transactions declined under the duplicate transaction validation rules 
specified in this Annexure shall also carry the applicable risk score details in the RespPay message.
