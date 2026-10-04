# Circular No.240 Reject Reason Codes For Emandate variants

Circular/reference number: NPCI/2016-17/NACH/CircularNo.240

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2016-17/NACH/CircularNo.240 August 21, 2017
To
AllNACHmemberbanks
Reject reason codes for eMandatevariants
On the introduction of eMandate variants in MMs it has become necessary to provide
additional reject reason codes to ensure receiving banks are choosing appropriate reason
variant are givenbelow.
Reason
S.No Variant ReasonDescription
code
API M088 APl-Datamismatchwithcustomerinfoanddatamandate
eSign M089 AadhaarnumbermismatchinX509certificateandmandate
eSign 060W Aadhaar numbermismatch inX509certificate and bankCBS
eSign M091 eSign signature is tampered or corrupt
eSign M092 Signed Content doesn't tally with data mandate
eSign M093 Aadhaarnotmappedtoaccount number
Comprehensive list of variant wise reject codes are provided in Annexure l.
Thenewcodes will beeffectivefromAugust 232017.
Member banks areadvised to take noteand update their internal systems accordingly and
useonlyappropriatereasoncodes specifiedforeachvariantforrejectionofmandates.The
information contained herein may be disseminated to the officials concerned.
For any clarifications pleasewriteback to ach@npci.org.in
Witkwarm regards,
(Giridhar G M)
VP &Head-NACH & CTS Operations
1001A,The Capital,BWing,10thFloor,BandraKurla Complex,Bandra(E),Mumbai 400051.T:+912240009100 F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-I
Variant wise rejection reason codes
S.No. Reject RejectDescription Normal eSign API
Code
M003 Drawers signature differs Yes
M004 Drawers signature required Yes
M005 Drawers signature to operate account not received Yes
M006 Yes
M007 Alterations require drawersauthentication Yes
M008 Companyforstamprequired Yes
600W Mandate in old format Yes
M010 Start date is mandatory Yes
MO11 Payment stopped by attachment order Yes Yes
10 M012 Payment stopped by court order Yes Yes
Withdrawal stopped owing to death of account Yes Yes
M013
holder
Withdrawal stopped owing tolunacy of account Yes Yes
12 M014
hold
13 MO15 Withdrawalstoppedowingtoinsolvencyofaccount Yes Yes
14 M020 Rejecteddue toduplicateUMRN Yes
15 M021 Duplicatemandatefirstpresentedmandatealready Yes Yes Yes
16 M022 Mandatepresented in ACH as well as ECS Yes
17 M023 RefertothebranchKYCnotcompleted Yes Yes
18 M024 Amount in words and figures differ Yes
19 M025 Present under proper mandatecategory Yes Yes
M026 Account frozen orInoperative Yes Yes
M027 Image not clear Yes
22 M030 Mandate registration not allowed for CC PF PPF act Yes Yes
23 M032 Rejected as per customer confirmation Yes Yes Yes
Invalid monthlyEMi amount.Full loanamt Yes Yes
24 M033
mentioned
25 M034 AmountofEMlmorethanlimitallowedfortheacct Yes Yes
26 M035 Corporatenamemismatch Yes
27 M037 Account closed Yes Yes
28 M038 No such account Yes Yes
M041 Account blocked Yes Yes
30 M042 Account descriptiondoes nottally Yes
M043 Nature of debit not allowed in account type Yes Yes
1001A,TheCapital,BWing,10thFloor,BandraKurla Complex,Bandra (E),Mumbai 400051.T:+912240009100 F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Reject Normal eSign API
S.No. Reject Description
Code
Mandate Not Registered_not maintaining req Yes Yes
32 M056
balance
33 M057 Payernamemismatch Yes
M058 Name of beneficiary not providedornot legible Yes Yes
Yes Yes
35 M060 Invalidfrequency
36 M061 Frequency of payment not mentioned on mandate Yes
37 M062 Periodofvaliditynotmentionedorinvalidenddate Yes
38 M063 tnvalidbankname Yes
Yes
39 M065 Fixed or maximum option not specified on mandate
40 M072 DatamismatchwithMandate Yes
Yes
41 M073 Mandate incomplete
42 M076 Data mismatch frequency and period Yes
43 M077 Data mismatch frequency and signature Yes
44 M078 Data mismatch period and signature Yes
Yes
45 M079 Datamismatch debit type and signature
Yes
46 M086 Customeridentifiermismatch
Yes Yes
47 M087 Incorrect amount
APl-Datamismatchwithcustomerinfoanddata Yes
48 M088 mandate
AadhaarnumbermismatchinX509 certificateand No Yes
48 M089 mandate
AadhaarnumbermismatchinX509certificateand No Yes
49 060W bank CBS
eSign signature is tampered or corrupt No Yes
50 M091
Signed Content doesn't tally with data mandate No Yes
51 M092
No Yes
52 M093 Aadhaar not mapped to account number
1001A,TheCapital,BWing,10thFloor,BandraKurla Complex,Bandra (E),Mumbai 400051.T:+912240009100 F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067
