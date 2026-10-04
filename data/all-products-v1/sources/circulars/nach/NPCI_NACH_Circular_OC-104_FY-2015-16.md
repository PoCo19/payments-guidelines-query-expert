# Circular No. 104 - Process of One Day Extension

Circular/reference number: NPCI/2015-16/NACH/104

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/NACH/104
June 19,2015
To,
AllNACHMemberBanks
Process of One Day Extension
In the event of any destination bank not being able to complete processing of inward transactions
within the stipulated time line, NPCl upon receiving request from the member bank and merits of the
request, might provide extension for a day for submitting response/return files. Please find enclosed
the technical guidelines (Annexure I) for handling the extensions granted in NACH system, all the
sponsor banks are advised to take note and make necessary arrangements in their systems to handle
the extensions.
WithWarm.Regards,
(Giridhar G.M.)
VP&Head-CTS&NACHOperations
C-9,8thFloor
ara/Phone:02226573150
RBl Premises
gar/Fax:02226571001
Bandra-Kurla Complex
-可/email:contact@npci.org.in
Bandra East
-400051 aq/Website:www.npci.org.in
Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-1
Technical Detailson Bankextensions:
1. NPCl will grant one day extension and the bank can upload the return file on the next
business day.
2. On the first day, the response file received by the Sponsor Bank, will have the normal file
naming convention.
3. This response file will have the transactions pertaining to the destination banks, as pending
(Flag value will be 3, Reason code will be 98),
4. On the next working day, when the destination bank uploads the return file, then the
response file generated and sent to the Sponsor Bank (on Day 2) will have file name similar to
the normal response file, but, in addition, there will be a slight change in the sequence
number.For example,
On Day 1, Response File received by the Sponsor Bank will be like ECS-CR-HDFC-HDFC001-07062012-
000001-RES.txt
On Day 2, Second response File received by the Sponsor Bank will be like ECS-CR-HDFC-HDFCo01-
07062012-000001-02-RES.txt
The second response file will have all the transactions in the input file with their final status
(lncluding those of the destination banks which were not given extension.)
Success Flags in Response Files
Note: The flag value along with the reason code should be used for determining the actual status of
the transaction.
SuccessFlagsinResponsefilesforvarious status
Success Flag Description
Success Flag for Returned transaction
Success Flag for Accepted transaction
Success Fiag for Rejected transaction
SuccessFlagforBankExtensiontransaction
Unwinding
C-9, 8th Floor -rq/Phone:02226573150
RBI Premises r/Fax:02226571001
Bandra-Kurla Complex 专-/email:contact@npci.org.in
Bandra East
-400051 aa专/Website:www.npci.org.in
Mumbai 400051
CIN:U74990MH2008NPL189067
