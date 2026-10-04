# IMPS | OC 129 | FY 25-26 | Generic Good Faith Credit adjustment option

Circular/reference number: NPCI/IMPS/OCNo.129/2025-2026
Date: 27th October 2025

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTSCORPORATION OF INDIA
NPCI/IMPS/OCNo.129/2025-2026 27th October 2025
To,
All Members of Immediate Payment system (IMPS)
Subject: Implementation of Generic Good Faith Credit Adjustments in IRCS
To manage exceptional transactions (viz. wrong credit amount recovered after the TAT,
similarly fraud chargebacks recovery etc.), member banks currenty send these requests
to NPCl along with debit consent for adjustment entries. NPCl then processes these
entries through its back-office system. We have now enabled a provision that allows
member banks to handle such exceptional adjustments directly through the IMPs back-
office system (IRCS -- IMPS Real Time Clearing System), eliminating the need for NPCI's
intervention.
Generic Good Faith Credit Adjustments in IRcS: Member banks are required to
implement the necessary process/system enhancements to ensure smooth daily
operations. Such adjustments should be raised strictly for handling exceptional
transactions or for recovery of funds after TAT expiry (as outlined above) only.
Key Points:
i) Unlike the current disputes process, where IRCs verifies all logical conditions
before either processing or rejecting a dispute. IRCS will not validate generic
good faith debit/credit adjustment entries raised by member banks. Therefore
it is the responsibility of member banks to conduct proper due diligence and
ensure the accuracy of all adjustments before submitting them in IRCS. The
system will validate only the bulk file format and mandatory data field
lengths/formats (refer to Section Bulk File Format in Annexure-1).
ii) Once adjustment is settled successfully, IRCs will store the adjustments in
repository and will not allow duplicate adjustments. IRCs will check the
duplicate executions through Remitting Bank Code, Beneficiary Bank Code
RRN, Adjustment Amount, Transaction Date, and Account Number fields. If
duplicate adjustments are identified, then IRCS will decline the same.
i) For RGGC and BGGC adjustments, no penalty is applicable. However, since
the bulk file format includes a dummy penalty flag, please ensure that the flag
is always set to "N". Selecting "y" will result in a system error stating "lnvalid
Penalty Flag".
iv) Banks must use the correct three-digit bank short code while raising
adjustments through the front-end or bulk, strictly as per the AUTH settlement
data as updated in raw file. For example, if the AUTH transaction is settled
between Remitting Bank - ABC and Beneficiary Bank - XYZ, the same data
must be used for raising credit adjustments. The three-digit code must not be
altered.
1001A, The Capital, B Wing, 10th Flo0r,
Bandra Kurla Complex, Bandra (E), Mumbai 4OQ O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
v) These Generic Good Faith transactions are also accessible through the
Transaction Search option.
vi) When raising manual adjustments through the front-end or bulk upload, it is
mandatory for banks to provide the account number. The account number
should belong to the customer or merchant of the other bank where the credit
or debit is to be applied, and the respective receiving bank will process the
generic good faith adjustment (Credit). Once the adjustment is successfully
settled, IRCS will update the account number in the adjustment report.
vi) For BGGC adjustments, the beneficiary bank must raise the adjustment along
with the remitting bank customer's account number. This account number will
be reflected in the adjustment report under the column "Rem_ Mobile_No".
Similarly, for RGGC adjustments, the remitting bank must raise the adjustment
with the beneficiary bank customer's account number, which will be reflected in
the adjustment report under the column "Ben_ Mobile_No".
The Generic Good Faith Credit Adjustment amount will be settled under
existing NTSL line item "Net Adjusted Amount'. Additionally, new fine items
will be made available in the IMPS NTSL report (Refer Annexure-1 for NTSL
line items).
viti) All the disputes have to be accepted or rejected within the TAT as defined for
BGGC & RGGC otherwise window will close on deemed acceptance basis.
ix) The above functionality shall be made available to the banks with effect from
Nov 27, 2025.
Warms Regards,
SD/-
Giridhar GM
Chief- Customer Success
Enclosed:
Annexure - 1 Process for handling generic good faith adjustments.
Annexure - 2 User Manual for generic good faith adjustments.
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E),Mumbai 4O0 051.
T: +9122 40009100 F: +9122 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 3 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-1
BGGC - BENEFICIARY BANK RAISING GENERIC GOOD FAITH CREDIT
ADJUsTMENT: The Beneficiary Bank may raise generic good-faith credit adjustments
after the TAT expiry of 25 days. Once such an adjustment is raised, the funds will be
settled immediately by debiting the Beneficiary Bank and crediting the Remitting Bank that
receives the adjustment. The Remitting Bank must either accept or represent the BGGC
within 3 calendar days; otherwise, the adjustment will be deemed accepted and the
dispute life cycle window will automatically close.
RGGC REMITTING BANK RAISING GENERIC GOOD FAITH CREDIT ADJUSTMENT:
The Remitting Bank may raise generic good-faith credit adjustments (RGGC) for P2P or
P2A transactions to transfer funds to a Beneficiary Bank. For example, if the Beneficiary
Bank fails to re-present a chargeback within the TAT and subsequently raises a good faith
request offline, the Remitting Bank may choose to accept this request by raising an RGGC
to provide the funds to the Beneficiary Bank. Once the RGGC is raised, the funds are
settled immediately by debiting the Remitting Bank and crediting the Beneficiary Bank.
The Beneficiary Bank must either accept or represent the credit adjustment within 3
calendar days; otherwise, the adjustment will be deemed accepted, and the window will
automatically close.
ADJUSTMENTS LIFE CYCLE: Life cycle for generic good faith adjustments are as
follows,
i) Raise - BGGC can be raised by the Beneficiary Bank, while RGGC can be
raised by the Remitting Bank.
i) Acceptance - The bank receiving the generic good faith adjustment must
accept it in IRCS.
ili) Re-presentment - The receiving bank may reject the adjustment (e.g., if
the customer account cannot be credited).
iv) Deemed Acceptance - If the receiving bank takes no action (acceptance
or re-presentment) within the TAT of 3 calendar days, the adjustment will be
considered deemed accepted, and the lifecycle will be closed.
NON -- COMPLIANCE: Banks must not raise adjustments for disputes that are still within
the TAT, as these must be either accepted or represented in IRCS, as applicable. Raising
generic good faith adjustments instead of following the prescribed acceptance or re-
presentment process within the TAT will be treated as non-compliance, and corresponding
bank should reject such cases.
TAT FOR GENERIC GOOD FAITH ADJUSTMENTS: All good faith adjustments must be
either accepted or represented within 3 calendar days from the day following the date on
which the adjustment is raised. If no action is taken within this period, the adjustment will
be treated as deemed accepted and the dispute lifecycle window will be closed.
VALIDATION OFADJUSTMENTS: IRCS will not validate BGGC and RGGC adjustments
against the original transaction or disputes. For these adjustments, only the file format will
be validated as per the prescribed specifications (refer to the file format details below)
1001A, The Capital, B Wing, 1oth Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 4 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Once a manual adjustment is processed successfully, it will be stored in the repository,
and any duplicate generic good faith adjustments (i.e., where all transaction details are
identical) will not be permitted.
INVALID THREE DIGITS CODE/PARTICIPANT ID: Member banks must use the correct
three-digit codes, i.e., sponsor bank codes and sub-member bank codes. If invalid codes
are used, the adjustment will be settled to the corresponding invalid banks. Therefore,
banks should ensure that the three-digit codes entered should match with the data of
AUTH settlement/raw file.
DUPLICATE BULK FILE CHECK: If a manual adjustment is submitted with a file name
that has already been processed (whether successfully or failed), IRCs wil reject the
entire file as a duplicate.
GENERIC GOOD FAITH ADJUSTMENT REPORT: All generic good faith adjustments
namely Beneficiary Generic Good Faith Credit Adjustment and Remitter Generic
Good Faith Credit Adjustment, categorized as Adjitype.
UNSETTLED TRANSACTIONS: Member banks should not raise any generic
adjustments in IRCs for unsettled transactions. Such instances should be reported to
NPCI.
MANUALADJUSTMENT BULK FILEFORMAT
Fields Format & Length Entity
TXN Date 20230604"YYYYMMDD" Bank
Numeric - 9 digits length including decimals (e.g.
Bank
TXN Amount 495495.75)
RRN 12 Numeric"422254321234" Bank
35Alpha Numeric
"ICladf12ada23423532sfgssfsfgs234256"(Not Bank
TRAN ID mandatory)
Remitting Bank Code
Bank
(three Digits) 3 digits Alpha Numeric "@@@
Beneficiary Bank Code
Bank
(three Digits) 3 digits Aipha Numeric "@@@"
Bank Adj Ref No As per current bulk file format specs Bank
IRCS Adi Ref No As per current bulk file format specs IRCS
Adjustment date As per current bulk file format specs IRCS
Penalty Flag Y/N 1 digit alpha "Y/N" Bank
Reason Code 4 digits Aipha Numeric "RGA1" IRCS
Dispute Flag 4 digits Alpha "RGGC" Bank
09 digits minimum and 30 digits maximum to
support both alpha & numeric Bank
Account number "111111115555555555"
Transaction Sub-Type 2 digitsF3/FC" Bank
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4O0 O51-
T: +91 22 40009100 F: +91 22 40009701
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
DISPUTES(RESPONSE)REASONCODES,DISPUTEFLAGS&DeScription
Dispute Base Reason
Adjustment Type Reason Code Description
Flag Dispute Codes
RGRC BGGC RGR1 Account closed
RGRC BGGC RGR2 Account does not exist
RGRC BGGC RGR3 Party instructions
Represented by
Remitter
RGRC BGGC RGR4 NRl account
(For BGGC
Adjustment)
RGRC BGGC RGR5 Account freeze
RGRC BGGC RGR6 Invalid Remitter details
RGRC BGGC RGR7 Any other reason
BGRC RGGC BGR1 Account closed
BGRC RGGC BGR2 Account does not exist
BGRC RGGC BGR3 Party instructions
Represented by
Beneficiary
BGRC RGGC BGR4 NRl account
(For RGGC
Adjustment)
BGRC RGGC BGR5 Account freeze
BGRC RGGC BGR6 Invalid beneficiary details
BGRC RGGC BGR7 Any other reason
Deemed Good faith Deemed Acceptance for
Acceptance BGCD RGGC BCA2 RGGC
(Deemed Flag to Good faith Deemed Acceptance for
be updated by the RGCD RGGC RCA2
BGGC
IRCS)
10oiA,TheCapital, BWing,1othFloor,
Bandra Kurla Complex,Bandra (E),Mumbai 4o0O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 6 -->

NPCI
NATIONAL PAYMENTSCORPORATIONOFINDIA
DISPUTES (RAISE)REASONCODES,DISPUTEFLAGS &Description
Dispute Reason
Entity Reason Code Description
Flag Codes
RGGC RGA1 Good faith request from another bank
RGGC RGA2 TAT expire disputes
Raised by
RGGC RGA3 Technical issues by bank
Remitter
RGGC RGA4 Dispute incorrectly accepted/represented
RGGC RGA5 Any other reason
Amount recovered for wrong credit charge back after
BGGC BGA1
expiry of TAT
Amount recovered for fraud charge back after expiry
BGGC BGA2
of TAT
Raised by BGGC BGA3 Good faith request from another bank
Beneficiary TAT expire disputes (e.g. Accept/ Reject of the
BGGC BGA4 Dispute lifecycle, Beneficiary refund (Credit
Adjustment / RET)
BGGC BGA5 Technical issues by bank
BGGC BGA6 Dispute incorrectly accepted/represented
BGAC BCA1 Good faith Acceptance for Credit RGGC
Acceptance
RGAC RCA1 Good faith Acceptance for Credit BGGC
Sample NTSL for details & reference:
17  Het Ad sted Amount 594 76
1& Het Adjusted Fe2 vith Tax
1g Net Deba Adusinent Swichiang Fee wah Tax
20 Net Non Compiancs Penailty
21 adiustmert on wreng dispute
23 Final SetienentAmotmt 405.24
24
25 Dispute Adjustments
20
27 Description Ref. Noi RRNI dato
28 Benesciary Genetic Good Faith Credit Adjustmen
29 Beneiciany Genanc Good Faith Credit Adjustrment TO HT1 506913253945/50591325394572016-19-28T3 506 0.
30 Beneiciary Genenic Good Faith Credit Adjustment FROM Ht1 5069132539451506913253945/2020-04-14/3 978.34
31 Total Benefictafy Generic Goed Falth CreditAdjustmentAmount 506 1978.34
32
Beneficiary Genaric Good Fath Credt Adfistment Rapresentnent
34 Beresciay Genetic Good Fath Credr Adjustrmen Represerdment FROm NTT 100287654321/100267654325/2018-01-13/FC 100.76
35 Benefciary Genetic Good Falh Credet Adjustment Represertment FROlf NT1 506913253945/306913253957/2017-07-04/FC 78
36 BeneFciery Genaric Goos Faith Credit Adjustment Repesentment FROm T! 506913253789/506913253739/2015-04-15/FC 7838 09
37 Total Beneficiary Generic Good Faith Credi Adjustment Representment Amoun! 8076.85
43 RemiGGFCreditAdRepresentment
44 Reminter Generic Good Faith Credl Adjusiment Represaatnent TO NT1 5069132539451506913253945/2020-04-11/F3
45 TotalRemiGGFCreditadjRepresentmentAmount 978.34
47 Remitter Generic Good Fath Credt Adjustment
48 Remitler Generic GoodFaith CredtAdjustmert TO it1 5065913253915/50691325395712017-07-04FC 78
49 Reriter Generic Good Faith Credit Adjustment TO tff1 506913253769/50691325378972015-04-15/FC 7698.09
50 Total Remltter Generic Good Falh Credit Adjustnent Arnount 7916.09
52 Adjustnent Sub Tota! 9460-43 10055.19
54 Het Adjustment Amotnt 594.76
IMPSNTSLND10104Z5_5C
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4O0 O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067
