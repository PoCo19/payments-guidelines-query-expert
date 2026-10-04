# AePS | OC 47| FY 19 20 | Implementation of Two Settlement cycles for AePS

Circular/reference number: NPCI/AePS/2019-20/010
Date: 12th July, 2018

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/AePS/2019-20/010
13thNovember, 2019
To,
AllAePSMemberBanks
Madam / Dear Sir
Sub:Implementation of Two settlements in a day forAePs transactions
Presently, AePS network cut-over time is 23:00 hours and transactions from previous day 23:00 hours
to current day's 23:00 hours, are settled in a single cycle every day. The AePS settlement is processed
on all working days at 09:30 am in Bank's RTGS Settlement account. For second and fourth Saturdays,
Sundays and RTGS holidays, the settlement entries are posted on the next working day. Daily
Settlement reports (DSR), STL and spool files are made available to members through BCS system.
Two (2) Settlement cycles in a day
The existing settlement process was reviewed in the 23rd AePs Steering Committee meeting held on
12th July, 2018 and it was decided to have multiple settlement cycles. Accordingly we are proposing to
haveTwoSettlement CyclesforAePStransactions.
Please note that there will be two settlement cycles on all RTGS holidays as well and same will be
posted on next RTGS working day. Separate Raw data, DSR, Spool files for each settlement cycle will be
placed in Bank folder post cut over and completion of settlement cycles. The following Cut Off timings
are proposed:
AePSSettlementCycle Cut-off timing
RTGS Settlement Cycle 1 13:00 hrs. Preceding day to 23:00 hrs. Preceding day
RTGS Settlement Cycle 2 23:00 hrs. Preceding day to 13:00 hrs. Current day
Please refer to Annexure A wherein the Settlement cut-off timings, Settlement day, etc. are explained
in detail with illustrations.
There shall be no change in the Raw data file, DsR file formats and other Settlement files and these
would be made available as per the cut-off time covering each Settlement cycle. However, there is
change in naming convention of file to identify the settlement cycle. (Please Refer Annexure B
wherein list offiles and new naming convention isgiven)
GsT reports & NPCl Fee Invoice shall be provided settlement cycle wise and on monthly basis as per
existing process.
Page 1 of 5

<!-- Page 2 -->

Change in Bulk Disputeupload format
We have introduced chargeback reason code as mandatory field for Aadhaar Pay transaction in bulk
dispute upload to calculate the penalty. Transaction failed confirmation not received will be
considered for penalty calculation for credit adjustment and chargebacks. (Please refer Annexure C)
Dispute/AdjustmentSettlement
Please note that all disputes /adjustments shall be settled in both the settlement cycles (Cycle 1 and
Cycle 2). Please find the below given illustration for more information.
Settlement Cycle RTGS Posting Time
Adjustment/DisputeFile
Upload
RTGS Settlement Cycle 2 (23:00 to 13:00) 16:30 hrs.
23:00 hrs. Preceding day to
12:30 hrs. Current day
RTGS Settlement Cycle 1 (13:00 to 23:00) 09:30am
12:31 hrs. Current day to
23:00 hrs. Current day
Note: Penalty will be applicable and levied if adjustment/disputes is raised after 2nd cycle of 5th
calendar day from the transaction date.
Daily Limit
Presently, Net Debit Cap (NDC) limits are refreshed on daily basis at the time of cut off i.e. at 23:0o hrs.
With the implementation of two settlements, the daily limit shall be refreshed and restored at the time
of each Settlement cut off time given above. However, on RTGs holidays there will be two settlement
cycles but limit shall be refreshed only once i.e. at 23:0o hrs.
Kindly make a note of the above and disseminate the instructions contained herein to the officials
concerned.
We shall communicate the effective date of implementation of two settlement cycles through a
separate circular.
For any queries or clarification, please contact the following officials:
Name e-mail ID MobileNumber
Rajendra Maurya rajendra.maurya@npci.org.in 9820626159
Nayan Bhandarkar nayan.bhandarkar@npci.org.in 8108122829
Yours faithfully,
Saiprasad Nabar
Chief-Online Product Operations
Page 2 of 5

<!-- Page 3 -->

AnnexureA
AePSMultiple Settlement Calendar
Transaction TD-Time Settlement Settlemen Transaction TD-Time- Settlement Settlement
Day in hrs. day t time Day in hrs. day time
(Cycle - 1) (Cycle - 2)
Monday 13:00:01 - Tuesday 09:30 am Monday 23:00:01 -
23:00:00 + Tuesday 13:00:00 Tuesday 04:30 pm
Tuesday 23:00:00 13:00:01 - Wednesday 09:30 am +Wednesday Tuesday 23:00:01 - 13:00:00 Wednesday 04:30 pm
Wednesday 13:00:01 - Thursday 09:30 am Wednesday 23:00:01
23:00:00 + Thursday 13:00:00 Thursday 04:30 pm
Thursday 23:00:00 13:00:01 - Friday 09:30 am + Friday Thursday 13:00:00 23:00:01 - Friday 04:30 pm
Friday 13:00:01 - Saturday 09:30 am Friday 23:00:01 -
23:00:00 + Saturday 13:00:00 Saturday 04:30 pm
13:00:01 -
Saturday
23:00:00
23:00:01-
13:00:00 Monday 09:30 am Sunday 23:00:01 -
Saturday + Monday 13:00:00 Monday 04:30 pm
and
+ Sunday
13:00:01 -
23:00:00
Page3of 5

<!-- Page 4 -->

AnnexureB-ListoffilesandtheirNamingconvention
Settlement Cycle File Type Acquirer File-Naming convention IssuerFileNaming convention
RAW Data (Financial) ACQRPDMM211019.mDMM1C ISSRPDMM211019.mDMM1C
RAW Data (Non-Financial) ACQRPDMM211019MW.mDMM_1C ISSRPDMM211019_MW.mDMM_1C
NTSL/DSR AEPSNTSLDMM211019_1C.xls
Dispute&Adjustment File (EMS) DMM20191021 1C.xls
1C GSTBankwise B DMM-PAY-GST-2019-20-21102110-10AEPS 1C.xIsB DMM-REV-GST-2019-20-21102110-10AEPS_1C.xls
GST_Daywise DMM-PAY-GST-2019-20-21102110-10AEPS1C.xls DMM-REV-GST-2019-20-21102110-10AEPS_1C.xIs
GST Payable PAYABLEDMMGST211019_1C.xls
GSTReceivable RECEIVABLEDMMGST2110191C.xIs
Spool Reports ACQUPDMM211019_1C.txt ISSUPDMM2110191C.txt
RAWData (Financial) ACQRPDMM211019.mDMM2C JSSRPDMM211019.mDMM2C
RAW Data (Non-Financial) ACQRPDMM211019_MW.mDMM_2C ISSRPDMM211019MW.mDMM2C
NTSL/ DSR AEPSNTSLDMM2110192C.xls
Dispute &Adjustment File (EMS) DMM201910212C.xls
2C GSTBankwise BDMM-PAY-GST-2019-20-21102110-10AEPS2C.xIs BDMM-REV-GST-2019-20-21102110-10AEPS2C.xls
GSTDaywise DMM-PAY-GST-2019-20-21102110-10AEPS2C.xIs DMM-REV-GST-2019-20-21102110-10AEPS_2C.xls
GSTPayable PAYABLEDMMGST2110192C.xIs
GSTReceivable RECEIVABLEDMMGST2110192C.xIs
Spool Reports ACQUPDMM211019_2C.txt ISSUPDMM2110192C.txt
Page 4 of 5

<!-- Page 5 -->

AnnexureC-RevisedBulk UploadFileFormat (ReasonCodeMandatory)
FollowingChargebacks and Good-faithChargebacks reasoncodes,tobe used for AADHAR
PAYtransactions-
1061- Credit not processed for Goods/Services returned to Merchant/BC
1062- Goods and Services not as described or customer received defective goods or
services
1063-Paid by other means and account is also debited for the transaction
1064-Duplicate Transaction
1065-Transaction Failed-Confirmation not received at micro ATM
FollowingCreditAdiustmentreason codes,tobeusedforAADHARPAYtransactions-
1061-Creditprocessed for Goods whichare defectiveor returned toMerchant/BC.
1065-TransactionFailed-Confirmationnot receivedat microATM
Bulk Upload Format:
Header Description Length
Bankadjref BankAdjustmentReferenceNumber Length - 100 (AN)
Flag DRC/B/ C Length -03 (A)
YYYY-MM-DD(N)
Shtdat Transaction Date
Adjamt TransactionAmount (N)
Shser RRN Length - 50 (N)
Shcrd 19 Digit (PAN Number) Length - 53 (AN)
Filename .csvfile Name Length - 50 (AN)
Reason Reason Code Length - 05 (AN)
URN Unique Reference Number Length - 35 (AN)
Reason Code ReasonCode-toidentify&Calculatepenalty Length -04 (N)
Reason code is mandatory only for Aadhaar Pay transaction type. For other than Aadhaar Pay
transactionsthe sameto beblank.
** Either Shcrd or URN to be used by bank in Bulk upload format.
Page 5 of 5
