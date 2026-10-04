# Circular 354 - Retrieval Reference Number (RRN) format in raw data & settlement files

Circular/reference number: NPCI/NFS/OCNo.354

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/NFS/OCNo.354 28thNovember2019
To.
All Members participating in NPCI Online products
Madam / Sir,
Sub: Retrieval Reference Number(RRN) format in raw data & settlement files
We refer to Retrieval Reference Number (RRN) sent in online transaction message and also in
raw data / settiement files of various NPCl online products (NFS, IMPS, UPl, RuPay PoS & e-
Com). RRN is one of the important parameter for reconciliation.
The first 4 characters of the RRN represents the date in Julian format such that the first
character of the RRN is the last digit of the year followed by the Julian date. The RRN format is
given below forreference:
RRN 10 12
Example Year
Date Year Last Julian Date Hour STAN
Digit
25-NoV-2019 2019 329 15:56 873254
07-Jan-2020 2020 007 15:57 892361
In view of the above, it should be noted that, for the next calendar year i.e. 2o20, the RRN shall
start with the digit 'o' (Zero) for all online products.
Members are requested to ensure that RRN is populated with zero (numeric) as the first digit for
all online request, response and reversal messages for transactions of year 2020. While
generating & forwarding/responding the messages, the first digit of RRN i.e. zero for year 2o20
should not be ignored/truncated to avoid reconciliation issues. Further, kindly ensure all your
settlement and reconciliation systems, complaints handling systems, etc. also adhere to RRN
specification.
Please make note of the above and disseminate the information contained herein to the officials
concerned / vendors handling switching technology, customer complaints, reconciliation, etc. for
the all the online products
For any queries or clarification, please contact:
Mobile
NPCI product Name e-mail ID
Number
NFS Nilesh Bhoir nilesh.bhoir@npci.org.in 9152085796
AePS RajendraMaurya raiendra.maurya@npci.org.in 9820626159
RuPay MurleshamMithapalli murlesham.mithapalli@npci.org.in 8291847122
IMPS &UPI Krishna Chaitanya krishna.chaitanya@npci.org.in 8978720088
Yours truly,
S.m-Nb
1001A,TheCapital,BWing,1othFloor,
SaiprasadNabar BandraKurlaComplex,Bandra(E),Mumbai4ooO51.
Chief - Online Products Operations T:+912240009100F:+912240009101www.npci.0rg.in
FII.IITAOAAMLDAAOAIDI1OOC7
