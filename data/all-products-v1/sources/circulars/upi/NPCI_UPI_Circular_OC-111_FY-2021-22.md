# OC 111 - Process to handle UPI Transactions for bank who has completed the amalgamation/merger process.

Circular/reference number: OC-111

<!-- Page 1 -->

I 
/ 
' 
'\ 
N~
U~
2020-21/~ 
N?C/1 
'J1ffiftzl 
prc,Ff 
NATIONAL PAYMENTS CORPORATION OF IND/A 
June 07, 2021 
To, 
\ 
) 
All Mem~Jrs of Unified Payments Interface (UPI) 
Maf 
Dear Sir, 
Subject: Process t handle UPI Transactions for banks who has completed the amalgamation/ 
/' 
. 
merge process 
· 
In case of '1ustomer of any bank can on board themselves on any UPI enabled App of any PSP 
Banks, T~Ps etc. In case of merged banks, the customers shall use the revised_account details in 
order j6 process UPI transactions. In UPI system, once the merger process 1s completed, the 
bank.s' which cease to exist shall be off-boarded from the UPI system. 
ere shall be customers who have registered themselves before merger activity and hence in 
the PSP database, old account number and IFS codes shall be present. In such cases, transaction 
request with old account details at Payer/Payee PSP (in case of Pay, Payer PSP initiates the 
transactions and in case of Collect, Payee PSP initiates the transaction), are expected to be 
declined at Payee/Payer PSP end with response code B3 (Transaction not permitted to the 
account - Business Decline) during the address resolution leg. In such cases NPCI will send U29-
Address Resolution Failed-Business Dedine to the originator as error code as well. 
However, it ha~ been observed that few PSPs are sending the old account details in the response 
for ReqAuth leg to NPCI and since such IFSCs/Banks are off-boarded from the UPI Systems, UPI 
sends negative acknowledgement (U17-PSP is not registered) to respective PSPs. In such cases 
NPCI will also send U09-ReqAuth Time out for Pay-Technical decline to the originator as error 
code. For handling such cases, it is recommended that PSPs / Banks to make use of List Account 
Provider APls on a daily basis, to update the list of Active Issuer Banks (Remitter and Beneficiary 
Bank) live on UPI so that PSPs c·an decline transaction with appropriate response codes (B3) as 
mentioned in paragraph 2. 
I 
Also to avoid such declines, notification / messages should be sent to the customers on regula1/' 
basis by the bank/PSPs/TPAPs to register with updated/new account details. Please provide a/i e 
of confirmation in this matter that notification/messages shall be sent to such customers. 
Please make note of the above and disseminate the instructions contained herein to the offt als 
concerned. 
/ 
I 
l/ 
/ 
/ 
::i::a::i:h::l~:r 
,~ 
Chief - Online Product Operations 
1001A, The Capital, S Wing, 10th Floor, 
Sandra Kurla Complex, Sandra (E), Mumbai 400 051• 
T: +91 22 40009100 F: +91 22 40009101 
contact@npci.org.in www.npci.org.in 
CIN: U74990MH2008NPL189067
