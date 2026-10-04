# Circular no.001 - Reorganizing NACH session

Circular/reference number: NPCI/2022-23/NACH/001

<!-- Page 1 -->

NPCL
NATIONALFAYMENTSCORPORATIONOFINDIA
NPCI/2022-23/NACH/001 April 08,2022
To,
AllNACHMemberBanks
RealignmentofNACHsessions
Refer may be taken from circular NPCl/2021-22/NACH/Circular No.11 dated February 28,2022 on
session linkage (copies enclosed), the technical specifications and FAQ for session linkage were also
released to the memberbanks. As a first step the session linkage functionality has been successfully
implemented for MUT sessions wherein2 settlements are generated for the return session enabling the
sponsor banks to provide multiple responses to the corporates.This will help the stakeholders to realize
funds faster.
As already communicated that with effect from April 15, 2022 the MUT return session timing will be
extended to 3 PM. There will be 2 settlements first at 12 PM and another settlement at final cut off at 3
PM. As per the technical specification document there will be changes in inward file name (this already
implemented) and the sponsor banks will receive partial response for each settlement and the final
response.
1. The sponsor banks should ensure that the response received at 12 PM is passed on to the
corporates so thatthe customers can receive same day NAV.
2. Destination bank should process and submit the responses before 12 PM cut - off, if there
any customer complaint due to delay in submission of response before cut off time then it will
be the responsibility of the destination banks to handle the complaint at their cost and
consequences.
In additiontothis witheffect from June 01,2022theNACH sessions will be realigned asdetailedbelow:
1. ACH Credit -Single presentation session for all the products and single return session with
multiple settlements.
2. APB Credit - Single presentation session for all the products and single return session with
multiple settlements.
3. ACH Debit -2presentation sessions (one for providing inward onT-1 basis and'another all
other products).
Note that there will be no change in TREDS related session till further notice. The session names are
provided in Annexure I along with tentative settlement schedule, the final settlement schedule will be
communicated separately

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
The memberbanks should take careof thefollowing:
1.Sponsorbanks:
a.Handling multiple settlements with reconciliation.
b. Responsefile:Settlement identifier in ledger folio
Change in response file names and within a day multiple response files for a single
input file.
2.Destinationbanks:
a. Handling the files with new names (indicators for session and settlement cycle
included).
b. Inwardfile-inwardgenerationdateintheheader(mandatory)
C. Returnfile-inwardgenerationdateintheheader (mandatory).
d..Handling multiple settlements with reconciliation.
Note: The list is only indicative, the member banks should go through technical specification document
and take all necessary actions accordingly.
implementation seamless. The information herein may please be disseminated to all the concerned.
Withwarmregards,
(GiridharGM)
Chief-Offlineproduct operations&technology
Registered Office-1001A,B wing 10thFloor,TheCapital,Bandra-Kurla Complex,Bandra(East),Mumbai-400051

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure 1:
Presentationsessiontimings:
T+0sessionswillbeoperatedforthedayfrom06:00AMto07:00PM
T-1 session presentation banks can able to present the transaction till evening 04:00 PM for the day
Settlement timings
Cycletype Cycle 1 Cycle 2 Cycle 3 Cycle4 Cycle5 Cycle6 Cycle7 Final Cycle
Timing 06:00 08:00 10:00 12:00 14:00 16:00 18:00 19:00
ACHCRPresent1 P1C1 P1C2 P1C3 P1C4 P1C5 P1C6 P1C7 P1FC
APBCRPresent1 P2C1 P2C2 P2C3 P2C4 P2C5 P2C6 P2C7 P2FC
ACHDRPresent1 P3C1 P3C2 P3C3 P3C4 P3C5 P3C6 P3C7 P3FC
Cycletype Cycle 1 Cycle FC
Timing 12:00 16:00
ACHDRPresent2(T-1sessionfornextdayvaluedateprocessingonlyforLEGandMUT)
Returns session timings:
T+0 sessions will be operated for the day from 08:00 to 20:00
T-1 session returns banks can able to submit the return files till evening 15:00 for the day with two
settlements
Settlement timings
Cycletype Cycle 1
Timing 08:00 10:00 12:00 14:00 16:00 18:00 20:00
ACHCRPresent1_R R1C1 R1C2 R1C3 R1C4 R1C5 R1C6 R1FC
APB CR Present 1 R R2C1 R2C2 R2C3 R2C4 R2C5 R2C6 R2FC
ACHDRPresent1_R R3C1 R3C2 R3C3 R3C4 R3C5 R3C6 R3FC
Cycletype Cycle 1 CycleFC
Timing 12:00 15:00
ACH DR Present 2 (T -1 session for next day value date processing only for LEG and MUT)
