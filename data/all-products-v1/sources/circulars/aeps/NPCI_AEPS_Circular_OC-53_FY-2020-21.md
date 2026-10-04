# AePS | OC 53| FY 20 21 | Supporting functionality of multiple issuer ports in round robin manner

Circular/reference number: NPCI/AePS/202021/006
Date: 2nd July, 2020

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/AePS/202021/006 August 24, 2020
To,
All AePs Member Banks
Dear Madam / Sir,
Sub: Supporting functionality of multiple Issuer Ports in round robin manner
AePs have experienced muiti-fold increase in transaction volume. Considering the future
growthr in AePs volume and to enable banks to handle the further increase in volume
effectively, AePs Technical Task Force Committee at the meeting held on 2nd July, 2020 has
recommended to have the functionality extended to all member banks to process the
transactions in muitiple ports with round-robin functionality. This has been approved in 2gth
AePs Steering Committee meeting held on 16th July, 2020.
The number of Ports Issuing banks need to implement will depend on the basis of the
member bank's volume and processing capacity. Member banks are expected to Go Live on
this functionality by 31st October, 2020 as decided in the aforesaid Steering Committee
meeting.
Please refer Annexure A for details on implementation of multiple issuer ports in round robin
manner.
Ail member banks are requested to take a note of the above and ensure to put in place
processes to be future ready
Name E-mail
Bunty Godhwani bunty.godhwani@npci.org.in
Nayan Bhandarkar nayan.bhandarkar@npci.org.in
Yours faithfully,
SmW.
Saiprasad Nabar
Chief - Online Products Operations
Encl: Annexure-A
1001A, The CaRagt, Bof/Big, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4oo Q51.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

Annexure A
IssuerRoundRobin
1. Requirement:
In the view of increasing volumes in AEPs transactions and to process the same
more effectively and without any issues, Issuer Banks need to implement issuer
round robin. In this way transaction load witl be distributed by all the Ports connected
to the corresponding banks as issuer.
2. Current Architecture (llN wise load sharing):
TCP Layer
NPCI Switch Bank Switch
Port 1
IN-
IIN - Request
Financial
Financial
Response
IIN-Non Port 2
JIN-Non
Financial Financial
3.  Multiple Ports with Round Robin Solution:
Bank connects to NpCl with multiple ports to process issuer transactions.
NPCl to impiement load balancing mechanism through round robin logic.
NPCl will route the issuer transactions of respective bank through any Port based on
the band width availability of port.
Page 2 of 3

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
TCP Layer
NPCt Switch BankSwitch
Port 1
IN- IN - Financial Request
Financial Financial
Non Financial Response
Port 2
IIN- Non UON- NII
Financial Financial
Port3
Port 4
A. Advantages:
Bank will receive equal traffic on all Ports(all network connections)
Bank status will be turned to offline only if all Port connections dropped
Cut over message is sent to alf the ports connected or to only one Port based on the
bank requirement.
The original request and subsequent communications (reversals) need not to be port
specific. It can be routed through any Port. If original transaction sent to Port 1,
reversal may go to Port 1,2 or 3 and bank has to process the reversal and respond to
NPCI
B. Implementation:
Basic flow of the transaction remains intact after implementation on new logic
Bank should not validate IlIN and Port combination.
Network messages (0800) should be port specific to maintain the heartbeat.
C. Certification:
Banks would be on boarded after successful compietion of certification.
1001A, The Carage,3of/ng, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4OO O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067
