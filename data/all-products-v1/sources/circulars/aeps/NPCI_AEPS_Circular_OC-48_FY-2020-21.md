# AePS | OC 48| FY 19 20 | Implementation of Two settlements in a day for AEPS transactions – Effective from 09 January, 2020

Circular/reference number: NPCI/AePS/2019-20/011

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/AePS/2019-20/011 02ndJanuary,2020
To,
AllAePSMemberBanks
Madam/ DearSir,
Sub:Implementation of Two settlements in a day forAePS transactions-Effectivefrom ogth Jan.,2020
With references toour circulardated:13thNov2019,NPcl/AePS/2019-20/010,weare going livewith
Two Settlement Cycle w.e.f. 0gth Jan., 2020.
Two(2)Settlement cycles inaday
Please note that there will be two settlement cycles on all days (including RTGs holiday) and same will
be posted on next RTGS working day.The Raw data, DSR, Spool files for both the settlement cycles will
be placed in Bank folder post cut over and completion of the settlement cycle. The following Cut Off
timings are proposed:
AePSSettlementCycle Cut-off timing
RTGSSettlementCycle1 13:00hrs.Precedingdayto23:00hrs.Precedingday
RTGSSettlementCycle2 23:00hrs.Precedingdayto13:00hrs.Currentday
Please refer to Annexure A wherein the Settlement cut-off timings, Settlement day, etc. are explained
in detail with illustrations.
There shall be no change in the Raw data file, DsR file formats and other Settlement files and these
would be made available as per the cut-off time covering each Settlement cycle.However, there is
change in naming convention of file to identify the settlement cycle. (Please Refer Annexure B wherein
listoffilesandnewnamingconventionisgiven)
GST reports & NPCl Fee Invoice shall be provided settlement cycle wise and on monthly basis as per
existing process.
Changein Bulk Dispute uploadformat
upload to calculate the penalty. Transaction failed confirmation not received will be considered for
penalty calculation for credit adjustment and chargeback both. (Please refer Annexure C)
Page 1 of 5
1001A,TheCapital,BWing,10thFloor,

<!-- Page 2 -->

Dispute/AdjustmentSettlement
Please note that all disputes / adjustments shall be settled in both the settlement cycles (Cycle 1and
Cycle 2). Please find the below given illustration for more information.
Adjustment/DisputeFile Dispute Settlement Cycle RTGSPostingTime
Upload
23:00hrs.Precedingdayto RTGS Settlement Cycle 2 (23:00 to 13:00) 13:45 hrs. onwards
12:30 hrs. Current day
12:31 hrs. Current day to RTGSSettlementCycle1(13:00to23:00) 08:00amonwards
23:00 hrs.Current day&*
** Member banks to upload the dispute file well before the above mentioned settlement cycle cut
over.
Note:Customercompensationwill beapplicableand leviedifadjustment/disputes is raisedonorafter
2nd cycleof 5th calendar day from the transaction date.
Daily Limit
Presently, Net Debit Cap (NDC) limits are refreshed on daily basis at the time of cut off i.e. at 23:0o hrs.
With the implementation of two settlements, the daily limit shall be refreshed and restored at the time
of each Settlement cut off time given above. However, on RTGs holiday will have two settlement cycles
but limit would berefreshed onlyoncei.e.at 23:0ohrs.
Kindly make a note of the above and disseminate the instructions contained herein to the officials
concerned.
For any queries or clarification, please contact the following officials:
Name e-mail ID MobileNumber
Rajendra Maurya rajendra.maurya@npci.org.in 9820626159
Nayan Bhandarkar nayan.bhandarkar@npci.org.in 8108122829
Yours faithfully,
Saiprasad Nabar
Chief-OnlineProductOperations
Page 2 of 5

<!-- Page 3 -->

Annexure A
AePSMultipleSettlementCalendar
Transaction TD-Time Settlement Settlemen Transaction TD-Time --- Settlement Settlement
Day in hrs. day t time Day in hrs. day time
(Cycle - 1) (Cycle - 2)
13:00:01 - Monday 23:00:01 -
Monday Tuesday 09:30 am Tuesday 04:30 pm
23:00:00 + Tuesday 13:00:00
13:00:01- Tuesday 23:00:01-
Tuesday Wednesday 09:30 am Wednesday 04:30 pm
23:00:00 + Wednesday 13:00:00
13:00:01 - Wednesday 23:00:01 -
Wednesday Thursday 09:30 am Thursday 04:30 pm
23:00:00 + Thursday 13:00:00
13:00:01 - Thursday 23:00:01-
Thursday Friday 09:30 am Friday 04:30 pm
23:00:00 + Friday 13:00:00
13:00:01 - Friday 23:00:01 -
Friday Saturday 09:30 am Saturday 04:30 pm
23:00:00 + Saturday 13:00:00
13:00:01 -
Saturday
23:00:00 Sunday 23:00:01 -
Monday 09:30 am Monday 04:30 pm
Saturday 23:00:01 - + Monday 13:00:00
+ Sunday 13:00:00
Annexure B-List offiles and theirNaming convention
Settlement Cycle File Type Acquirer File-Naming convention Issuer File-Naming convention
RAW Data (Financial) ACQRPDMM2110191C.mDMM ISSRPDMM2110191C.mDMM
RAW Data (Non-Financial) ACQRPDMM211019MW1C.mDMM ISSRPDMM211019MW1C.mDMM
NTSL/DSR AEPSNTSLDMM211019_1C.xls
Dispute&AdjustmentFile (EMS) DMM20191021_1C.xls
10 GST Bankwise BDMM-PAY-GST-2019-20-21102110-10AEPS1C.xIs BDMM-REV-GST-2019-20-21102110-10AEPS1C.xIs
GST_Daywise DMM-PAY-GST-2019-20-21102110-10AEPS1C.xIs DMM-REV-GST-2019-20-21102110-10AEPS1C.xIs
GST Payable PAYABLEDMMGST2110191C.xIs
GST Receivable RECEIVABLEDMMGST2110191C.xIs
Spool Reports ACQUPDMM2110191C.txt ISSUPDMM211019 1C.txt
RAW Data (Financial) ACQRPDMM2110192C.mDMM ISSRPDMM2110192C.mDMM
RAW Data (Non-Financial) ACQRPDMM211019MW2C.mDMM ISSRPDMM211019MW2C.mDMM
NTSL/DSR AEPSNTSLDMM2110192C.xls
Dispute&AdjustmentFile (EMS) DMM201910212C.xls
GST Bankwise BDMM-PAY-GST-2019-20-21102110-10AEPS2C.xIs BDMM-REV-GST-2019-20-21102110-10AEPS2C.xIs
GST Daywise DMM-PAY-GST-2019-20-21102110-10AEPS2C.xIs DMM-REV-GST-2019-20-21102110-10AEPS2C.xIs
GST_Payable PAYABLEDMMGST211019_2C.xIs
GST_Receivable RECEIVABLE_DMMGST2110192C.xIs
Spool Reports ACQUPDMM2110192C.txt ISSUPDMM2110192C.txt
Page 3 of 5

<!-- Page 4 -->

AnnexureC-RevisedBulkUploadFileFormat(ReasonCodeMandatory)
Following are the reason codes, which will be enabled for AADHAR PAY related Chargeback
and Good-faith Chargeback:
1061-Credit not processed for Goods/Services returned toMerchant/BC
1062 - Goods and Services not as described or customer received defective goods or
services
1063-Paid by othermeans and account is also debited for the transaction
1064-Duplicate Transaction
1065-TransactionFailed-Confirmationnot receivedatmicroATM
Following are thereason codes,which will be enabledforAADHARPAYrelated Credit
Adjustment:
1061-Credit processedforGoods whicharedefectiveorreturned toMerchant/BC.
1065-TransactionFailed-Confirmationnot received atmicroATM
Header Description Length
BankAdjustment Reference
Bankadjref Number Length - 100 (AN)
Flag DRC/B/C Length - 03 (A)
Shtdat TransactionDate YYYY-MM-DD (N)
Adjamt Transaction Amount (N)
Shser RRN Length - 50 (N)
Shcrd 19Digit (PANNumber) Length - 53 (AN)
Filename .csv file Name Length - 50 (AN)
Reason Reason (by default 1) Length - 05 (AN)
URN UniqueReference Number Length - 35 (AN)
Chargeback/Credit
Adjustment Reason Code (as
Reason Code mentioned above) Length - 04 (N)
Page4of5
