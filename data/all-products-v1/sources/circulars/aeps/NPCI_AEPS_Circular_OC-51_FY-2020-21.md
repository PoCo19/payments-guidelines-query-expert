# AePS | OC 51| FY 20 21 | Implementation of Third settlements in a day for AePS transaction

Circular/reference number: NPCI/AePS/2020-21/002

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/AePS/2020-21/002 13thJuly,2020
To,
AllAePSMemberBanks
Madam / Dear Sir,
Sub:Implementationof Third settlements ina dayforAePstransactions-Effectivefrom25th July2020
With references to our previous communication, we are going live with Third Settlement Cycle w.e.f.
25th Jul., 2020.
Third (2) Settlement cycles in a day
Please note that there will be three settlement cycles on all days (including RTGS holiday) and same will
be posted on next RTGS working day.The Raw data, DSR, for all three settlement cycles will be placed in
Bank folder post cut over and completion of the settlement cycle. The following Cut Off timings are
proposed:
AePSSettlementCycle Cut-off timing
RTGS Settlement Cycle1 16:31 hrs. Current day to 23:00 hrs. Current day
RTGSSettlement Cycle2 23:01hrs.Precedingdayto13:00hrs.Currentday
RTGSSettlementCycle3 13:01hrs.Currentdayto16:30hrs.Currentday
Please refer to Annexure A wherein the Settlement cut-off timings, Settlement day, etc.are explained
in detail with illustrations.
There shall be no change in the Raw data file, DsR file formats and other Settlement files and these
would be made available as per the cut-off time covering each Settlement cycle. However,there is
change in naming convention of file to identify the settlement cycle.(Please Refer Annexure B wherein
listof filesandnew naming conventionisgiven)
GST reports & NPCI Fee Invoice shall be provided settlement cycle wise and on monthly basis as per
existing process.
Page1of 4
1001A,TheCapital,BWing,10thFloor
BandraKurlaComplex,Bandra(E),Mumbai4OOO51.
T:+912240009100F:+912240009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Dispute/Adiustment Settlement
Please note that all disputes / adjustments shall be settled in all three settlement cycles. Please find
thebelowgivenillustrationformoreinformation.
Adjustment/DisputeFile Dispute Settlement Cycle RTGSPostingTime
Upload**
23:00 hrs. Preceding day to RTGS Settlement Cycle 2 (23:00 to 13:00) 13:45hrs.onwards
12:30 hrs. Current day
13:30 hrs. Current day to RTGS Settlement Cycle 3 (13:01 to 16:30) 17:45hrs.onwards
16:00hrs.Current day
17:31 hrs.Current day to RTGS Settlement Cycle 1 (13:00 to 23:00) 08:00 am onwards
23:00 hrs.Current day
** Member banks to upload the dispute file well before the above mentioned settlement cycle cut
over.
As per RBl circular, RBI/2019-20/251 DPSS.CO.PD.No.1897/02.14.003/2019-20 we will be
implementing customer compensation calculation basis working days along with third settlement
cycle.
Daily Limit
Presently, Net Debit Cap (NDC) limits are refreshed on daily basis at the time of cut off i.e. at 23:0o hrs.
With the implementation of third settlements, the daily limit shall be refreshed and restored at the time
of each Settlement cut off time given above. However, on RTGS holiday will have three settlement
cycles but limit would be refreshed only once i.e. at 23:o hrs.
Kindly make a note of the above and disseminate the instructions contained herein to the officials
concerned.
Foranyqueries orclarification,pleasecontact thefollowing officials:
Name e-mail ID Mobile Number
Rajendra Maurya rajendra.maurya@npci.org.in 9820626159
Nayan Bhandarkar nayan.bhandarkar@npci.org.in 8108122829
Yours faithfully,
Sm"a
Saiprasad Nabar
Chief-OnlineProduct Operations
Page 2 of 4
1001A,TheCapital,BWing,10thFloor
BandraKurlaComplex,Bandra(E),Mumbai4ooo51.
T:+912240009100F:+912240009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureA
Settlement Settlement Settlement
Transaction TD-Time-Settlement time Transaction TD-Time Settlement time Transaction TD-Time- Settlement time
Day in hrs. day (Cycle 1) Day -in hrs. day (Cycle 2) Day in hrs. day (Cycle 3)
Monday
16:30:01- +Tuesday 23:00:01 13:00:01-
Monday 23:00:00 Tuesday 9:30AM 13:00:00 Tuesday 4:30PM Tuesday 16:30:00 Tuesday 6:30PM
Tuesday +
16:30:01- Wednesday 23:00:01 13:00:01
Tuesday 23:00:00 Wednesday 9:30AM 13:00:00 Wednesday 4:30.PM Wednesday 16:30:00 Wednesday 6:30 PM
16:30:01 - Wednesday+ 23:00:01 13:00:01-
Wednesday2 23:00:00 Thursday 9:30AM Thursday 13:00:00 Thursday 4:30PM Thursday 16:30:00 Thursday 6:30 PM
16:30:01- Thursday + 23:00:01 13:00:01-
Tnursday 23:00:00 Friday 9:30AM Friday 13:00:00 Friday 4:30PM Friday 16:30:00 Friday 6:30PM
16:30:01- Friday + 23:00:01 13:00:01-
Fnday 23:00:00 Saturday 9:30AM Saturday 13:00:00 Saturday 4:30PM Saturday 16:30:00 Saturday 6:30 PM
Saturday 16:30:01- Saturday + 23:00:01 9:30AM 13:00:01- 9:30AM
(2nd &4th) 23:00:00 Sunday 13:00:00 Monday Sunday 16:30:00 Monday
Monday 9:30 AM
16:30:01- Sunday + 23:00:01 13:00:01-
Sunday 23:00:00 Monday 13:00:00 Monday 4:30PM Monday 16:30:00 Monday 6:30PM
Page 3 of 4

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure B-List of files and their Naming convention
Settlement
File Type Acquirer File-Naming convention IssuerFile-Naming convention
RAW Data (Financial) ACQRPDMM2110191C.mDMM SSRPDMM211019_1C.mDMM
RAW Data (Non-Financial) ACQRPDMM211019_MW_1C.mDMM 1SSRPDMM211019_MW_1C.mDMM
NTSL/DSR AEPSNTSLDMM211019_1C.XSX
Dispute &Adjustment File(EMs) DMM20191021_1C.x5X
10 GST_Bankwise B_DMM-PAY-GST-2019-20-21102110-10AEPS_1C.XISX B_DMM-REV-GST-2019-20-21102110-10AEPS_1C.XISX
GST_Dawise DMM-PAY-GST-2019-20-21102110-10AEP5_1C.XI5X DMM-REV-GST-2019-20-21102110-10AEPS_1C.XISX
GST_Payabie PAYABLE DMMGST211019_1C.XI5X
GST_Receivable RECEIVABLE_DMMGST2110191C.XISX
Late Reversal Reports ReversalTransDMM090420 1C.xIsx
Raw Data (Financial) ACQRPDMM211019_2C.mDMM SSRPDMM211019_2C.mDMM
RAw Data (Non-Financal) ACQRPDMM211019_MW_2C.mDMM SSRPDMM211019_MW_2C.mDMM
NTSL/DSR AEPSNTSLOMM211019_2C.XISX
Dispute&AdjustmentFife(EMs) DMIM20191021_2C.X5X
GsT_Bankwise B_DMM-PAY-GST-2019-20-21102110-10AEPS_2C.X15X B_DMM-REV-GST-2019.20-21102110-10AEPS_2C.X5X
GST_Daywise DMM-PAY-GST-2019-20-21102110-10AEPS_2C.X5X DMM-REV-GST-2019-20-21102110-10AEPS_2C.X5X
GST_Payable PAYABLE_DMMGST211019_2C.XISX
GsT_Receivable RECEIVABLE_DMMGST211019_2C.XSX
RAW Data (Financial) ACQRPDMM211019_3C.mDMM SSRPDMM2110193C.mDMM
RAW Data (Non-Financial) ACQRPDMM211019_MW_3C.mDMM ISSRPDMM211019_MW_3C.mDMM
NTSL/DSR AEPSNTSLDMM211019_3C.X5X
Dispute&AdjustmentFile(EMs) DMM20191021_3C.x15X
3C GST_Bankwise B_DMM-PAY-GST-2019-20-21102110-10AEPS_3C.XISX B_DMM-REV-GST-2019-20-21102110-10AEPS_3C.XISX
GsT_Dawise DMM-PAY-GST-2019-20-21102110-10AEPS_3C.XI5X DMM-REV-GST-2019-20-21102110-10AEPS_3C.XI5X
GST_Payable PAYABLE DMMGST2110193C.XISX
GST_Receivabie RECEIVABLE_DMMGST2110193C.XISX
Late Reversal Reports ReversalTransDMM090420_3C.xisx
Page4of4
