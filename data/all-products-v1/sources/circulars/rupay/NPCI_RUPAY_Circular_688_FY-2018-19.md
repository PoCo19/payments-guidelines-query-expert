# 23-Apr-2018 - NPCI/2018-19/RuPay/007 - Implementation of Two settlements in a day for RuPay PoS & e-Comm domestic transactions

Circular/reference number: NPCI/2018-19/RuPay/007

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2018-19/RuPay/007 April 23,2018
To,
All Members ofRuPay
Madam/ DearSir,
Sub:Implementationof Two settlements inadayfor RuPayPoS &e-Comm domestictransactions
network and arranges to process Inter-Bank Settlement entries to the respective members RTGS Settlement account with
RBI.
Presently, NPCl network cut-over time is 23:00 hours and transactions from previous day 23:00 hours to current day's 23:00
hours, are settled in a single cycle every day.RuPay Pos & e-Comm Transactions are settled and processed on all working
days in Bank's RTGS Settlement account. For Second and Fourth Saturdays, Sundays and RTGS holidays, the settlement
entries are posted on the next working day. Daily Settlement reports (DsR), along with Raw data files and Reports are made
available to members through RGCS.
Two Settlement cycles in a day
In the RuPay Steering Committee meeting held on September 22, 2016, members reviewed the existing Settlement process
and approved two Settlement cycles in a day. We are pleased to inform that RBl has approved commencement of two
settlementsperdayforRuPayPos&e-Commdomestictransactions.
The settlement cut-off details are provided below:
RGCS Settlement Cycle SMS Cut-off Timing DMS Presentments Cut-Off Timing
RTGSSettlement Cycle1 13:00 hrs preceding day to 23:00 hrs 12:00 hrs previous day to 05:00 hrs
preceding day current day
RTGS Settlement Cycle2 23:00 hrs preceding day to 13:00 hrs current 05:00 hrs current day to 12:00 hrs current
day day
RTGS Settlement Cycle 2 will be similar to RTGS Settlement Cycle 1 and will consider for clearing & settlement - SMS
transactions, DMs presentments, Disputes, Tip & Surcharge adjustments, Refunds raised/files uploaded by Member banks.
Effective May 14, 2018 we will be implementing Two Settlement cycles in a day for RuPay Pos & e-Comm domestic
transactions.
Please refer to Annexure A wherein the Settlement cut-off timings is explained in detail.
There shall be no change in the formats of DsR summary reports, Raw data, and other Settlement files and reports
generated in RGcS, and these would be made available to Member Banks for each Settlement cycle. As per existing process,
GSTreports&NPCIFeeInvoiceshall beprovidedonmonthlybasis.
Please refer to Annexure B for Naming convention for all Settlement files & reports (cycle wise) that will be generated in
RGCS.
Page1of6
1001A,TheCapital,BWing,10thFloor,BandraKurla Complex,Bandra(E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

LiquidityManager (LM)LimitapplicableforSub-memberBanks
settlements, the daily limit shall be refreshed and restored at the time of each Settlement cut off time.
Please note importantly that -
1.As per the existing menu option of Member File Download in RGcS all settlement files and reports shall be
availableseparatelyforboththecycles.
For transactions of second and fourth Saturday, all Sundays and RTGs holidays, there shall be only one settlement
perday(i.e.onlyonecycleforeach settlementday).
Kindly make a note of the above and disseminate the instructions contained herein to the officials concerned.
Foranyqueriesorclarification,pleasecontact:
Name e-mail ID Mobile Number
Vishal Patil vishal.patil@npci.org.in 8291847126
Pramila Shetty pramila.shetty@npci.org.in 8879772787
NayanBhandarkar nayan.bhandarkar@npci.org.in 8108122829
Yours faithfully,
RamSundaresan
SvP&Head-Operations
Page2of 6

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure A
MultipleSettlement-RuPay PoS&e-CommDomestictransaction
Settlem
ent Clearing-All life cycles(including
Timing Presentments）otherthan
Transaction Day Settlement Cut-Off Authorisation Authorisation
Settlement 05:00 From Sat23:00 hrs to Sun23:00 FromSun05:00hrsto Mon05:00
Cycle - 1 hrs hrs hrs
Settlement 13:00 FromSun23:00hrstoMon 13:00 FromMon05:0ohrstoMon
Monday Cycle - 2 hrs hrs 12:00hrs
Settlement 05:00 FromMon13:0ohrstoMon FromMon12:00hrstoTue05:00
Cycle - 1 hrs 23:00 hrs hrs
Settlement 13:00 From Mon 23:00 hrs to Tue 13:00 From Tue 05:00 hrsto Tue 12:00
Tuesday Cycle - 2 hrs hrs hrs
Settlement 05:00 From Tue 13:00 hrs to Tue 23:00 FromTue 12:00hrs to Wed05:00
Cycle - 1 hrs hrs hrs
Settlement 13:00 From Tue 23:00hrs to Wed From Wed 05:00 hrs to Wed
RTGS
Wednesday Cycle - 2 hrs 13:00 hrs 12:00hrs
Working
Settlement 05:00 FromWed13:00 hrsto Wed From Wed 12:00hrs to Thu05:00
Days Cycle - 1 hrs 23:00 hrs hrs
Settlement 13:00 From Wed23:00hrs to Thu 13:00 FromThu05:00hrs to Thu12:00
Thursday Cycle - 2 hrs hrs hrs
Settlement 05:00 FromThu 13:00hrs to Thu23:00 FromThu 12:00 hrs to Fri 05:00
Cycle - 1 hrs hrs hrs
Settlement 13:00 From Thu 23:00hrs to Fri 13:00 From Fri 05:00 hrstoFri 12:00
Friday Cycle - 2 hrs hrs hrs
Settlement 05:00 FromFri 13:00 hrsto Fri 23:00 From Fri 12:00 hrs to Sat 05:00
Cycle - 1 hrs hrs hrs
Settlement 13:00 From Fri 23:00hrs to Sat13:00 FromSat 05:00hrs to Sat 12:00
Saturday Cycle - 2 hrs hrs hrs
Settlement 05:00 From Fri 13:00 hrs to Fri 23:00 FromFri 12:00hrstoSat05:00
RTGS Saturday Cycle - 1 hrs hrs hrs
Holiday Settlement 05:00 FromFri 23:00hrs toSat23:00 FromSat05:00hrsto Sun05:00
Sunday Cycle - 1 hrs hrs hrs
Page 3 of 6

<!-- Page 4 -->

Annexure B
NewFile naming convention for bank as an Acquirer
FolderName Current File Naming Convention in Settle-
in RGCS RGCS ment
New File Naming Convention in RGCS Cycle
021ABCD24000011800905_xml.pgp Cycle 1
021ABCD24000011800905_xml.pgp 022ABCD24000011800905_xml.pgp
Cycle 2
041ABCD24000011800809_xml.pgp Cycle 1
Acknowledge 041ABCD24000011800809_xml.pgp 042ABCD24000011800809_xml.pgp
-ment Cycle 2
831ABCD24000011801002_xml.pgp Cycle 1
831ABCD24000011801002_xml.pgp 832ABCD24000011801002_xml.pgp
Cycle 2
871ABCD24000011801002_xml.pgp Cycle 1
871ABCD24000011801002_xml.pgp 872ABCD24000011801002_xml.pgp
Cycle 2
811NPCi99900011801000_dat.pgp Cycle 1
Daily Bin 810NPCI99900011801000_dat.pgp 812NPCI99900011801000_dat.pgp Cycle 2
821NPCI99900011801000_dat.pgp Cycle 1
820NPCI99900011801000_dat.pgp 822NPCI99900011801000_dat.pgp
Cycle 2
All_Disputes-1 Cycle 1
All_Disputes All_Disputes -2
Dispute Cycle 2
Presentment Report_ACQ OUT-1 Cycle 1
Report PresentmentReport_ACQ_OUT Presentment Report ACQ OUT-2
Cycle2
Total Outstanding TotalOutstanding Chargebacks_ACQ_INC-1
Cycle 1
Chargebacks_ACQ_INC TotalOutstandingChargebacks_ACQ_INC-2
Cycle 2
Incoming 011ABCD24000011801001_xml.pgp Cycle 1
011ABCD24000011801001_xml.pgp 012ABCD24000011801001_xml.pgp
Cycle 2
DSRSummaryReport_ABCDBANKLIMITEDACQUIRER-
2018-01-10-1 Cycle 1
DSRSummaryReport_ABCDBANK DSRSummaryReport_ABCDBANKLIMITEDACQUIRER-
LIMITEDACQUIRER-2018-01-10-1 2018-01-10-2
Cycle 2
DSRSummaryReport_SponsorBank_ABCD BANK LIMITED
DSRSummaryReport_SponsorBank_A ACQUIRER-2018-01-10-1 Cycle 1
BCD BANKLIMITEDACQUIRER-2018- DSRSummaryReport_SponsorBank_ABCDBANKLIMITED
01-10-1 ACQUIRER-2018-01-10-2
Cycle 2
Report InterchangeSummaryReport_ABCDBANKLIMITED
InterchangeSummaryReport_ABCD ACQUIRER_2018-01-10-1 Cycle 1.
BANKLIMITEDACQUIRER_2018-01- InterchangeSummaryReport_ABCDBANKLIMITED
10-1 ACQUIRER_2018-01-10-2
Cycle 2
NetSettlementReport_SponsorBank_ABCDBANKLIMITED
NetSettlementReport_SponsorBank ACQUIRER2018-01-10-1 Cycle 1
ABCD BANK LIMITED NetSettlementReport_SponsorBank_ABCDBANK LIMITED
ACQUIRER_2018-01-10-1 ACQUIRER_2018-01-10-2
Cycle 2
NPCIBillingSummary_ABCDBANK NPCIBillingSummary_ABCDBANKLIMITED Cycle 1
Page4of 6

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
LIMITEDACQUIRER2018-01-10-1 ACQUIRER2018-01-10-1
NPCIBillingSummary_ABCD BANKLIMITED
ACQUIRER2018-01-10-2 Cycle 2
NPCIBillingSummary_SponsorBank_ABCDBANKLIMITED
NPCIBillingSummary_SponsorBank ACQUIRER_2018-01-10-1 Cycle 1
ABCDBANKLIMITED NPCIBillingSummary_SponsorBank_ABCDBANKLIMITED
ACQUIRER_2018-01-10-1 ACQUIRER_2018-01-10-2 Cycle 2
RejectSummary_ABCDBANKLIMITEDACQUIRER_2018-
01-10-1 Cycle 1
RejectSummary_ABCDBANK
LIMITEDACQUIRER_2018-01-10-1 01-10-2 Cycle 2
851ABCD24000011801000_HDR_Ext 851ABCD24000011801000_HDR_Extended_dat.pgp Cycle 1
ended_dat.pgp 852ABCD24000011801000_HDR_Extended_dat.pgp Cycle 2
861ABCD24000011801000HDR_Ext 861ABCD24000011801000_HDR_Extended_dat.pgp Cycle 1
ended_dat.pgp 862ABCD24000011801000_HDR_Extended_dat.pgp Cycle 2
RawData OCT_ACQABCD24000011801000_CSV OCT_ACQABCD24000011801000-1_csv.Pgp Cycle 1
.pgp OCT_ACQABCD24000011801000-2_cSV.Pgp Cycle 2
OCT_ISSABCD24000011801000CSV. OCT ISSABCD24000011801000-1_csv.pgp Cycle 1
pgp OCT_ISSABCD24000011801000-2_csv.pgp Cycle 2
Web 031ABCD24000011801030_xml.pgp Cycle 1
Acknowled-
gement 031ABCD24000011801030_xml.pgp 032ABCD24000011801030_xml.pgp Cycle 2
New Filenaming convention for bank as an Issuer
Settle
FolderName Current File Naming Convention in ment
in RGCS RGCS New FileNaming Convention inRGCS Cycle
811NPCi99900011801000_dat.pgp Cycle 1
810NPCI99900011801000_dat.pgp 812NPCi99900011801000_dat.pgp Cycle 2
Daily Bin
821NPCI99900011801000_dat.pgp Cycle 1
820NPCI99900011801000_dat.pgp 822NPCI99900011801000_dat.pgp Cycle 2
All_Disputes-1 Cycle 1
All_Disputes All Disputes-2 Cycle 2
Dispute Presentment Report ISS INC-1 Cycle 1
Report PresentmentReportISS INC PresentmentReport IssINC-2 Cycle 2
TotalOutstanding Total Outstanding Chargebacks_Iss OUT-1 Cycle 1
Chargebacks_ISs_OUT Total OutstandingChargebacks_ISS_OUT-2 Cycle 2
011ABCD24000021801001_xml.pgp Cycle 1
011ABCD24000021801001_Xml.pgp 012ABCD24000021801001_xml.pgp Cycle2
Incoming 841ABCD24000021801001_xml.pgp Cycle 1
841ABCD24000021801001_xml.pgp 842ABCD24000021801001_xml.pgp Cycle 2
881ABCD24000021801001_xml.pgp 881ABCD24000021801001_xml.pgp Cycle 1
Page 5 of 6

<!-- Page 6 -->

882ABCD24000021801001_xml.pgp Cycle 2
DSRSummaryReport_ABCD BANKAS DSRSummaryReport ABCD BANKASISSUER-2018-01-10-1 Cycle 1
ISSUER-2018-01-10-1 DSRSummaryReport_ABCDBANKASISSUER-2018-01-10-2 Cycle 2
DSRSummaryReport_SponsorBank_ABCD BANK AS
ISSUER-2018-01-10-1 Cycle 1
DSRSummaryReport_SponsorBank_A DSRSummaryReport_SponsorBank_ABCD BANKAS
BCDBANKASISSUER-2018-01-10-1 ISSUER-2018-01-10-2 Cycle 2
InterchangeSummaryReport_ABCDBANKAS
ISSUER_2018-01-10-1 Cycle 1
InterchangeSummaryReport_ABCD InterchangeSummaryReport_ABCDBANKAS
BANKASISSUER_2018-01-10-1 ISSUER2018-01-10-2 Cycle 2
Report NetSettlementReport_SponsorBank_ABCDBANKAS
ISSUER2018-01-10-1 Cycle 1
NetSettlementReport_SponsorBank NetSettlementReport_SponsorBank_ABCD BANKAS
ABCDBANKASISSUER_2018-01-10-1 ISSUER 2018-01-10-2 Cycle 2
Cycle 1
NPCIBillingSummary_ABCD BANKAS NPCIBillingSummary_ABCDBANKASISSUER_2018-01-10-
ISSUER 2018-01-10-1 Cycle 2
NPCIBillingSummary_SponsorBank_ABCD BANKAS
ISSUER_2018-01-10-1 Cycle 1
NPCIBillingSummary_SponsorBank NPCIBillingSummary_SponsorBank_ABCDBANKAS
ABCDBANKASISSUER_2018-01-10-1 ISSUER_2018-01-10-2 Cycle 2
851ABCD24000021801000 HDR Ext 851ABCD24000021801000_HDR_Extended_dat.pgp Cycle 1
ended_dat.pgp 852ABCD24000021801000_HDR_Extended_dat.pgp Cycle 2
861ABCD24000021801000_HDR_Ext 861ABCD24000021801000_HDR_Extended_dat.pgp Cycle 1
RawData ended_dat.pgp 862ABCD24000021801000_HDR_Extended_dat.pgp Cycle 2
OCT_ACQABCD24000021801000_CSV OCT_ACQABCD24000021801000-1_cSv.pgp Cycle1
.pgp OCT_ACQABCD24000021801000-2_csv.pgp Cycle 2
OCT_ISSABCD24000021801000_CSV. OCT_ISSABCD24000021801000-1_csv.pgp Cycle 1
pgp OCT_ISSABCD24000021801000-2_csv.pgp Cycle 2
Web 031ABCD24000021801002_xml.pgp Cycle 1
Acknowledge
ment 031ABCD24000021801002_xml.pgp 032ABCD24000021801002_xml.pgp Cycle 2
Page6of6
