# Circular 366 - Migration of NFS ATM back office system from Dispute Management System (DMS) to Bharat Clearing and Settlement (BCS) System

Circular/reference number: OC-366
Date: 28th April, 2020

<!-- Page 1 -->

NATIONALPAYMENTS CORPORATIONOFINDIA
NPCI/NFS/OC No.366/2020-21 28th April, 2020
TO,
All Members participating in NFS ATM Network
Madam/DearSir,
Sub: Migration of NFS ATM back office system from Dispute Management System (DMS) to Bharat Clearing and
Settlement (BCS) System.
NFS members access Dispute Management System (DMS) application for NFS ATM transactions including Inter-
operable Cash Deposit (1CD), DFS, JCB and CUP ATM transactions for daily operational activities such as Clearing
& Settlement, Dispute management, downloading settiement files, MiS reports, GsT reports, Switching Invoices,
etc.
In our constant endeavour to enabie members to efficiently use NFs Dispute Management System, we are pleased
to inform that NPCI will be migrating the NFS back office system from DMS to NFS-BCS from 01st June, 202o. After
migrationfromDMStoNFS-BCS, NFS-DMSwill bedecommissioned.
The migration of the settlement and dispute management process from DMS to NFS-BcS would result in following
benefits:
Enhanced security as members will be provided with Admin iDs. Admin user can create/delete User IDs
and reset passwords.
Greater operational convenience as members can view transaction and corresponding
disputes/adjustments (if any) in single window.
Continuous feed of transaction data from Online to back office system resulting in near real-time
settiement (i.e.) calculation of Switching and Interchange fees.
Please note that the members can access NFS-BCS by using the existing URL/iP, which was used for accessing
NFS-DMS.
Members are requested to take note that NFS-BCS has been developed similar to DMS and the file formats for all
settlement reports will remain same. This is to ensure that there is no impact in reconciliation process.
Please refer Annexure A for the detailed NFS-BCS User guide. After Go-Live, this document shall be made available
in the new NFS-BCS system through the path as follows:
Report Download >>> File Download >>> Participant ID >>> Manuals & Documents
1001A, The Capital, B Wing, 10th Floor,
BandraKurla Complex,Bandra(E), Mumbai4ooO51.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

Creation of Member Admin and by-default NFS User ID
With reference to NFS Operating Circular (OC) 361 dated 27th January, 2020, we have collected Admin details for
two officials from each NFS member. Basis these detais, we have created two Admin User IDs for each member.
This User ID shall act as a Member Administrator who can further create Maker and Checker User IDs within their
group for accessing NFS-BCS. Admin users are requested to create Maker and Checker immediately after their first
login in NFS-BCS.Additionally, for the smooth execution of daily activities such as downloading of settlement files,
reconciliation, dispute management, etc., by default we have created two user IDs (i.e. NFs Maker and NFs
Checker) from our end using the Admin details received from members. As an interim arrangement, members can
use these NFs Maker and NFS Checker user ID for carrying out their daily operational activities, till the time
Member Admin creates user IDs for their own institution's users. Please note that these by-default NFS User IDs
created by NPCl shall be deactivated automatically after one month
Please note that the User ID and Password will be given to the respective user's email ID, submitted as part of OC
361.
Steps to be followed by Admin User for creating Maker and Checker in NFS-BCS are provided in Section 8 -
Member Administrator Activities in NFS of Annexure A.
Dispute Management process
The following changes are shall be made in dispute management process:
1. In NFS-BCS, the amount to be entered while raising disputes/adjustments shall be the actual disputed
amount or adjustment amount claimed by the member, unlike in DMS where the received amount was
entered while raising chargeback or credit adjustment.
2. There is a maker checker process while raising any disputes/adjustments through front-end option. NFS
Checker has to ensure that all the disputes/adjustments raised by the NFS Maker has been verified by
them for the day. However, maker-checker option is not available for bulk file upload. Refer Section 5 -
Transaction Actions of Annexure A for the detailed process.
3.  The dispute raising through bulk upload option is divided into two new sub-processes as given below:
a)  Fite uploading - Bulk dispute file is uploaded for validating the basic file format.
b) File staging - Once the validation is completed, the user has to stage the bulk file for final submission
ofdisputes/adjustments.
Refer Section 3 - Working with files of Annexure A for the detailed process of bulk dispute raising.
4. If the disputes/adjustments are pending for verification (in front end option) or staging (in bulk upload
option) in a particular cycle, then it can be verified or staged in the subsequent cycles/days. However, the
adjustment date shall be the day when the disputes/adjustments is verified or staged successfully and this
might result into customer penalty, if applicable.
During settlement activity of NFS 1st cycle & 2nd cycle, bulk file upload of disputes shall be allowed, but the
staging of the file will not be concluded till completion of settlement. Similarly, user can raise dispute from
front end as maker, but the checker approval for the dispute will not be allowed till completion of
settlement activity. The system shall display the message as 'Request cannot be processed due to
settlement is in progress, please try later' on screen when the user shall verify a dispute through front end
or stage the files through bulk option during the settlement activity is under progress.

<!-- Page 3 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
6. Few important points to note while uploading bulk disputes/adjustments file:
a.Amount field should not be Zero. This field should have the dispute amount claimed by the
cardholder or the member. If Zero is entered in the amount field, then that particular record shall
be rejected by the system.
b. The Date format shall be onlyYYYY-MM-DD.
C. Usage of space/special characters in file names is not allowed. The only allowed value is
(underscore), apart from alphanumeric characters for file names. if the special character is
entered in the file name, then the entire file shall be rejected by the system.
d. The header in bulk upload file is optional, i.e. user can upload bulk file with or without header.
7. After the re-presentment/debit adjustment is raised through bulk upload option, then the re-
presentment/debit adjustment pending for attaching document shall not be captured in the Pending
report. User shall search the re-presentment/debit adjustment pending for attaching documents using
transaction search option and attach the relevant documents.
The complete cycle of a transaction aiong with its associated disputes/adjustments will be made avaitable
in NFS-BCS transaction search area. Refer Section 4.1 - Common Transaction Search menu of Annexure
Afordetailed information.
9.  in case, the chargeback raised is accepted by the Acquirer before CB+2 days i.e. before the settlement of
chargeback, then the customer penalty, if applicable shall be visible in See Fees option in transaction
search only after chargeback is settled on CB+2 days.
10. In case, the re-presentment is raised against the chargeback before settlement date i.e. within CB+2 days,
then the system would not allow user to raise Pre-arbitration til the chargeback & re-presentment is
settledon CB+2 days.
11. The format of Adjustment report has been changed for NFS, ICD, JCB & CUP. Refer Annexure B for the
new Adjustment report format.
12. The GUl of SDMT has been changed. Refer Section 5.2 - How to Raise Single Dispute Multiple Chargeback
of AnnexureAfordetailed information.
Change in Late reversal settlement
In Online, if the original transaction is settled in one of the cycle, then the late reversal against that transaction
shal be settled in immediate succeeding cycle only, unlike the existing process of setting late reversai up to T+1
day ofthe originaltransaction.
For eg: If the original transaction is settled in NFs 1st cycle dated 0ist May'20 (i.e. between current day O1.00 pm
to current day 11.00 pm), then the late reversal received during NFS 2nd cycle dated 02nd May'20 (i.e. between
previous day 11.00 pm to current day 1.00 pm) shalt be settied in that cycle.
resolved in form of chargeback or credit adjustment.
Basis the above mentioned change, late reversal for ATM withdrawal transactions shall be settled in both NFs 1st
cycle and NFs 2nd cycte. The verification reversal file for late reversal settlement shall be made available in both
NFS cycles. During the late reversal settlement, if the chargeback raised is in open status within TAT or the credit
adjustment is raised, then the chargeback or credit adjustment shall be deleted and fate reversal shall be settled.
1001A,TheCapital, BWing,10thFloor
BandraKurla Complex, Bandra (E),Mumbai 4o0 O51.
T: +91 22 40009100 F: +9122 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

Please note importantly that -
1. The URL / iP address of the new back office system NFS-BCS will continue to remain the same. Hence, no
changes are required to be effected by NFS member's w.r.t IP whitelisting. Please inform your internal Ir
support team, in case any change in internal Natting or mapping of ip from your end.
2.  The BIN master flat file will be made available in NFS-BCS along with other settlement files on daily basis.
Refer Section 6.1 - Cycle Closure reports of Annexure A for the detailed BIN updation process and file
format.
3. Adhoc reports can be generated by providing a date range by member user. Refer Section 6.2 Adhoc
reports of Annexure A for detailed information.
4. There is no change in the existing dispute cyclie, TAT, customer penalty calculation as per Harmonisation
of TAT, etc.
The above changes are scheduled to go live with effect from 01st June, 2020.
For any queries orclarification, please contact:
Name e-mail ID Mobile Number
Sapna Gupta sapna.gupta@npci.org.in 7506446590
Sarit Sobhan Das sarit.das@npci.org.in 8108108694
Pankaj Samarth pankai.samarth@npci.org.in 8108122861
Avinash Kunnoth avinash.kunnoth@npci.org.in 8879772725
Yours faithfully,
Saiprasad Nabar
Chief - Online Products Operations
Encl: 1. Annexure A - NFS-BCS User Guide
2. Annexure B - Adjustment report format
3. Annexure C- NFS-BcS System requirements
4. Annexure D - Advantages and Important changes between DMS & NFS-BCS
