# Circular No.184 Processing of returns for deemed transactions

Circular/reference number: OC-184

<!-- Page 1 -->

NATIONAL PAYMENTS CORPORATION OF INDIA
NACH Project
Processing of Returns for Deemed Accepted
Transactions
Bank specification Documeint
Version 1.0
NAT'ONAL AUTCMATED CLEARING HOUSE
September, 2016

<!-- Page 2 -->

NPCI NACH Processing of Returns forDeemed AcceptedTransactions Bank Specification Document_V1.0
DOCUMENT RELEASE NOTE
Document Details
Name Version Date Description
No.
Bank Specifications 1.0 1st Sep 2016 Provides operations and technical details for
Document
the change - A feature in ACH for Processing
of . Returns for Deemed Accepted
Transactions:
This document and any revised pages are subject to document control. Please keep them up
to-date using the release notices from the distributor of the document.
NPCI Confidential
Page 2 of 10

<!-- Page 3 -->

NPCI NACH Processing of Returns for Deemed Accepted Transactions Bank Specification Document_V1.0
Tabie cf Contents
1. INTRODUCTION
1.1 MARKING DEEMED ACCEPTANCE IN RES AND PROCESSING THE RETURNS .
1.2 FILE PROCESSING & FILE NAMING CONVENTION .
1.3 HANDLING MULTIPLE EXTENSION AND RESPONSE FILE NAMING CONVENTION
2.1 SCENARIO DESCRIPTION
10
NPCI Confidential
Page 3 of 10

<!-- Page 4 -->

NPCI NACH Processing of Returns for Deemed Accepted Transactions Bank Specification Document_V1.0
1. Introduction
This document details 'the mechanism of incorporating a new feature in ACH for providing
separate identifier for the transactions for which no response has been received from the
destination banks and the process of generation of response files for incremental records. In
ACH application RES file will be sent to Sponsor bank after ending the return session containing
all the transactions as per the corresponding INp file along with the status code for accepted,
returned, pending for response and extended.
1.1 Marking Deemed Acceptance in REs and Processing the Returns
Success
Returned
Extended
Transactions for which response is not received are considered to be accepted and the
relevant response code is provided.
NPCl will enable a new flag "3" and reason code "g9" for the transactions that are
pending for response. This feature will be made available only for specific products viz
APB Credit & ACH Credit i.e. DBT (including PFM) & DBTL.
The destination bank can upload the return files in the subsequent available session (on
subsequent day or after) in case of the transactions that are marked with flag *3' and
.66,
In the initial response file i:e. on Day 0 NACH system will provide full response files with
the following flags
Success
Return
Extended
Pending for response
On subsequent days when the destination bank uploads the return file NACH system will
provide either full response file or response file with only the updated records. This is
configurable in NACH system. By default only incremental files will be provided. The
configuration.
NPCI Confidential Page 4 of 10

<!-- Page 5 -->

NPCI NACH Processing of Returns for Deemed Accepted Transactions Bank Specification Document_V1.0
The flag indicating records pending for response is similar to extension, only difference
being extension is always given for one day whereas pending for response flag will keep
the item open for defined number of days and accept the return file uploaded.
After the predefined number of days for pending for response flag, if destination bank/s
fait to upload return transactions then the final response file will be generated with Flag
"7" and Code "oo" to Sponsor Bank.
After the final response is updated as "7' and 'oo' the record is deemed to have been
accepted by the destination bank. System will not accept return files for which final
response has been updated.
The member banks and the government department should not send Ss for the
records with the status as *extension' (3,98), ‘pending for confirmation3,99) (" or
deemed accepted (7,00)
Responsibility:
Sponsor Bank - Handle multiple response files generated
Government departments/Corporate - Handle multiple response   files
generated and not to send SMs for (3,98) and (7,00)
1.2 File processing & File Naming Convertion
There will be no change from current file format / naming convention for inward / return file.
For Sponsor banks based on their request, response file will be generated & provided in one of
the following way i.e.
1. Regular response file
2. Only for extended records
3. Both
Regular response file denotes current response file being generated in production
environment for sponsor bank. There is no change in file naming convention / file fornat
for regular response file.
Extended response file will contain only those records that were successfully processed
by destination bank & uploaded to NPCl on that business date subsequent to the date of
presentation. File format for extended response file remains the same however file
naming convention is.different. The naming convention is given below:
NPCI Confidential Page 5 of 10

<!-- Page 6 -->

NPCI NACH Processing of Returns for Deemed Accepted Transactions Bank Specification Document_V1.0
<ProcessName>-<TransType>-<Bank Short Code>-<Loginld>-<ACH Business Date>-<nnnnnn>-
EXT02-RES.txt
ProcessName -ACH
Trans Type -CR
Bank Identifier - 4 Char Unique Bank Identifier in System
Loginld - User Login Id
ACH Business Date -ddmmyyyy
nnnnnn -Runnirg sequence number for each zip file
E.g. “ACH-CR-SBIN-SBIN001-01092016-000001-EXTC2-RES.txt"
EXTO2 clearly describes that the file is for extended RES file,
Whereas the Regular RES file will be ACH-CR-SBIN-SBIN001-01092016-000c01-02-RES.txt.
The same file naming convention is applicable for xml format.
USE CASES FOR RESPCNSE FILE GE:!ERAT'ON
Case 01:
Regular RES file
Bank A has presented ACH CR INP file, which has multiple destination banks, out of
which Bank B has not responded. Only Regular RES file will be generated and sent
whenever the destination bank responds to the pending transactions.
If all transactions get settled before the final TAT expiry date, then the FINAL RES
(Regular RES) will be sent 'on the day when all transactions reached FINAL state.
If all the transactions aren't settled till the final TAT expiry date, then the FINAL RES
will be generated on the last date with status change from 399 to 700 for deemed
transactions.
NPCI Confidential Page 6 of 10

<!-- Page 7 -->

NPCI NACH Processing of Returns for Deemed Accepted Transactions Bank Specification Document_V1.0
Case 02:
Extended RES file
Bank A has presented ACH CR INP file, which has multiple destination banks, out of
which Bank B has not responded. Only Additional RES file whenever the destination
bank responds to the pending transactions. If all transactions get settled before the
final TAT expiry date, then the FINAL RES (Regular RES) will be sent on that day along
with the Additional RES file.
If all the transactions aren't settled'till the final TAT expiry date, then the FINAL RES
will be generated on the last date with status change from 399 to 700 for deemed
transactions.
Case 03:
Both
Bank A has presented ACH DR INP file, which has multiple destination banks, out of
which Bank B has not responded. Both regular RES and Additional RES file will be sent
whenever the destination bank responds to the pending transactions.
If all transactions get settled before the final TAT expiry date, then the FINAL RES:
(Regular RES) will be sent on that day along with the Additional RES file.
If all the transactions aren't settled till the final TAT expiry date, then the FINAL RES
will be generated on the last date with all the transactions and extended REs file with
status change from 399 to 700 for deemed transactions
1.3  Hardling irultiple extensior ard Response file naming convention
(1) Type of Response File = Botin; Maximum Return Acceptance.Days = 6
transactions and rest 8 transactions extended: Only one REs file with 10 transactions
generated on day 1(2 returned and 8 transaction with code 398)
Regular RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-RES.txt
NPCI Confidential
Page 7 of 10

<!-- Page 8 -->

NPCI NACH Processing' of Returns for Deemed Accepted Transactions Bank Specification Document_V1.0
Day 2.: On second day, 2 more RTN transactions uploaded and rest 6 extended. Two
REs files, first one with 10 transactions (4 returned and § transaction with 398) and
second RES file with two transactions.
Regular RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-02-RES.txt
Additional RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-EXT02-RES.txt
Day 3. Third day Bank didn't upload any returns and no extension granted.
Regular RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-03-RES.txt
Additional RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-EXT03-RES.txt
Day 4. Fourth day Bank didn't upload any returns. And thus no response files will be
sent.
Day 5.  Fifth day 2 more Return transactions uploaded (2 of 6 deemed). Two RES files,
Additional REs file with two transactions as returned will be generated.
Regular RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-04-RES.txt
Additional RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-EXT04-RES.txt
 Day S. Sixth day Bank didn't upload any returns. And thus no response files will be
sent.
Day 7. Seventh day Bank didn't upload two transactions. As per the above given TAT,
on the 6th day post the original value date Final RES file with details of all 10 transactions
and an additional file with two transaction will be generated.
Regular Fina: RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-05-RES.txt
Additional RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-EXT05-RES.txt
(2) Type oi Response File = Extended; Maximum Return Acceptance Days = 6
Day. 1. INP file from sponsor with 10 transactions, destination uploaded 2 RTN
transactions and rest 8 transactions extended. Only one REs file with 10 transactions
generated. on day 1(2 returned and 8 transaction with code 398)
Regular RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-RES.txt
NPCI Confidential
Page 8 of 10

<!-- Page 9 -->

NPCI NACH Processing of Returns for Deemed Accepted Transactions
Bank Specification Document_V1.0
Day 2. Second day 2 more RTN transactions uploaded and rest 6 extended. Two RES
files, first one with 10 transactions (4 returned and 6 transaction with 398) and second
RES file with two transactions.
Additional RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-EXT02-RES.txt
Day 3. Third day Bank didn't upload any returns and no extension granted.
Additional RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-EXT03-RES.txt
Day 4.  Fourth day Bank didn't upload any returns. And thus no response files will be
sent.
Day 5. Fifth day 2 more Return transactions uploaded (2 of 6 deemed). Two RES files,
Additional REs file with two transactions as returned will be generated.
Additional RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-EXT04-RES.txt
Day 6. Sixth day Bank didn't upload any returns. And thus no response files will be
sent.
 Day 7. Seventh day Bank didn't upload two transactions. As per the above given TAT,
on the 6th day post the original value date Final RES file with details of all 10 transactions
and an additional file with two transaction will be generated.
Regular Final RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-02-RES.txt
Additional RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-EXT05-RES.txt
(3) Type of Response File = Regular; Maximum Return Acceptance Days = 6
transactions and rest 8 transactions extended. Only one REs file with 10 transactions
generated on day 1(2 returned and 8 transaction with code 398)
Regular RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-RES.txt
Day 2. Second day 2 more RTN transactions uploaded and rest 6 extended. Two RES
files, first one with 10 transactions (4 returned and 6 transaction with 398) and second
RES file with two transactions,
NPCI Confidential
Page 9 of 10

<!-- Page 10 -->

NPCI NACH Processing of Returns for Deemed Accepted Transactions
Bank Specification Document_V1.0
Regular RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-02-RES.txt
Day 3.
 Third day Bank didn't upload any returns and no extension granted. Regular
RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-03-RES.txt
Day 4.
Fourth day Bank didn't upload any returns. And thus no response files will be
sent.
Day 5.  Fifth day 2 more Return transactions uploaded (2 of 6 deemed). Two RES files,
Additional REs file with two transactions as returned will be generated.
Regular RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-04-RES.txt
Day §. Sixth day Bank didn't upload any returns. And thus no response files wilt be
sent.
Day 7. Seventh day Bank didn't upload two transactions. As per the above given TAT,
on the 6th day post the original value date Final RES file with details of all 10 transactions
and an additional file with two transaction will be generated.
Regula" Final RES: ACH-CR-SBIN-SBIN001-DDMMYYYY-000001-05-RES.txt
2.1 Scenario Description
Below attachment will explains the Response file generation scenarios with transaction types.
RES file
generations Scenari
NPCI Confidential
Page 10 of 10
