# Circular No.011 - MMS - Mandate Variant wise reason code

Circular/reference number: NPCI/2018-19/NACH/Circularno.011

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2018-19/NACH/Circularno.011 June 22, 2018
To,
AllNACHMemberbanks
MMS-Mandatesvariantwisereasoncode
Refer to circular no. 256 dated August 21, 2017 on “Reject reason codes for E-Mandate
variants.The validation of MMS variantwisereturn reasons willbe implemented witheffect
from July 16, 2018. If any of the member banks use incorrect return reason, NACH system
will reject such records. This is applicable to all variants of Mandate.
The list of variant wise reasons is provided in Annexure l.
Member banks are advised to take note and make necessary arrangements to capture proper
reason codes. The information herein may be disseminated to all the concerned.
For any clarification please write back toach@npci.org.in
Withwarm regards,
(Giridhar G.M)
SVP - NACH & CTS Operations
1001A,TheCapital,BWing.10thFlo0r,BandraKurlaComplex.Bandra(E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-l: Variant wise Reason Codes:
A. NACK Accept Reason
Sl. No. Code Name Normal Mandate eSign API
M003 Drawers signature differs Yes NA NA
M004 Drawers signature required Yes NA NA
M005 Drawers signature to operate account
not received Yes NA NA
M006 Drawers authority to operate account
not received Yes NA NA
Alterations require drawers
M007
authentication Yes NA NA
M008 Company for stamp required or Wrong Yes NA Yes
600W Mandate in old format Yes NA NA
M011 Payment stopped by attachment order Yes Yes NA
MO12 Payment stopped by court order Yes Yes NA
M013 Withdrawal stopped owing to death of NA
10 account holde Yes Yes
M014 Withdrawal stopped owing to lunacy of NA
account hold Yes Yes
M015 Withdrawal stopped owing to insolvency NA
12 of account Yes Yes
M021 Duplicate mandate_first presented
13 mandate already Yes Yes Yes
M022 Mandate presented in ACH as well as
14 ECS Yes NA NA
15 M023 Refer to the branch_KYC not completed Yes Yes NA
16 M024 Amount in words and figures differ Yes NA NA
17 M025 Present under proper mandate category Yes Yes NA
18 M026 Account frozen Yes Yes NA
19 M027 Image not clear Yes NA NA
M030 Mandateregistrationnot allowedforCC
20 account Yes Yes NA
Not a CBS act no.or old act
M031
no.representwithCBSno Yes Yes NA
22 M032 Rejected as per customer confirmation Yes Yes Yes
M033 InvalidmonthlyEMlamount.Fullloan
23 amt mentioned Yes NA NA
Amount of EMl more than limit allowed
M034
24 for the acct Yes Yes NA
25 M035 Corporate name mismatch Yes Yes NA
26 M037 Account closed Yes Yes NA
27 M038 No such account Yes Yes NA
28 M041 Account blocked Yes Yes NA
1001A,TheCapitat,BWing,10th Floor,Bandra Kurla Complex,Bandra (E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Sl. No. Code Name Normal Mandate eSign API
Drawers signature not updated in Bank
M049
29 CBS Yes NA NA
M050 Drawers signatureillegible inmandate
30 form Yes NA NA
31 M051 Mandate Not Registered_NREAccount Yes Yes NA
32 M052 Mandate Not Registered_Minor Account Yes Yes NA
Mandateregistrationnot allowedforPF
M053
33 account Yes Yes NA
Mandate registration not allowed for
M054
34 PPF account Yes Yes NA
35 M055 AccountInoperative Yes Yes NA
MandateNot Registered_not
M056
36 maintaining regbalanc Yes Yes NA
AccountHolderNameMismatchwith
M057
37 CBS Yes Yes NA
38 M060 Invalid frequency Yes Yes NA
39 M066 Joint signature required Yes NA NA
Thumb print in CBS but cust sign in
M067
40 mandviceversa Yes NA NA
Account type in mandate is different
M068
41 fromCBS Yes NA Yes
Data mismatch with image_account
M074
42 number Yes NA NA
43 M075 Data mismatch with image_account type Yes NA NA
44 M077 Data mismatch with image_frequency Yes NA NA
45 M078 Data mismatch with image_period Yes NA NA
46 M079 Data mismatch with image_debit type Yes NA NA
47 M080 Data mismatch with image_amount Yes NA NA
48 M081 Data mismatch with image_start date Yes NA NA
49 M082 Data mismatch with image_end date Yes NA NA
50 M083 Data mismatch with image_payer name Yes NA NA
Datamismatchwithimage_debtor bank
M084
51 name Yes NA NA
Data mismatch with image_more than
M085
52 onefield Yes NA NA
APIDatamismatchwithcust info and
M088
53 data mandate NA NA Yes
AadhaarNumbermismatchin
M089
54 X509certficand mandate NA Yes NA
AadhaarNumbermismatchinX509cert
060W
55 and bank CBS NA Yes NA
56 M091 eSign Signature is tampered or corrupt NA Yes NA
signed Content doesnot tally with data
M092
57 mandate NA Yes NA
58 M093 Aadhaar not mapped to account number Na Yes NA
1001A,TheCapitat,BWing.10thFloor,Bandra Kurla ComplexBandra(E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN：U74990MH2008NPL189067

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
B. ACK Accept Reason
Sl. No. Code Name Normal Mandate eSign API
ac01 ACKDefaultAcceptReason Yes Yes Yes
c. AmendmentReason
Sl. No. Code Name Normal Mandate eSign API
NotaCBsactno.oroldact
M036 Yes NA NA
no.representwithCBSno
M036 Not a CBS act no.or old act Yes NA NA
no.representwithCBS no
A001 On customer request Yes Yes Yes
D. MandateCancelReasons
Sl. No. Code Name Normal Mandate eSign API
C003 Account closed Yes Yes Yes
C004 Account frozen Yes Yes Yes
C005 Account inoperative Yes Yes Yes
C002 Cancellationoncorporaterequest Yes Yes Yes
C001 Cancellationoncustomerrequest Yes Yes Yes
1001A,The Capitat,BWing,10thFloor,Baandra KurlaCompiex,Bandra(E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067
