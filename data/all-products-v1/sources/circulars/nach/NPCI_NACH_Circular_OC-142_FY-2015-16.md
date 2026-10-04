# Circular No.142 - Addition of Products in ACH credit session

Circular/reference number: OC-142

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPC1/2015-16/NACH/Circular No.  142
December 28, 2015
To
AllNACHMemberBanks
Additionof products inACHCredit Session
Productidentifierhasbeenintroduced fortheACHcredittransactions,Separateinward will
begeneratedforeachproductandthesamecanbeidentifiedbased ontheinwardfilename
in the sequence number. The product wise identifier can be used by the destination banks
for their internal processes if they desire so.
Action at Sponsor Bank: Sponsor Bank to provide product type in the input files under
columns 262-264 when an input file is uploaded, so that the files can be tagged to session
and inward generated to the destination bank with identifiers. The following are the product
types that will be accepted by the system
1. 10
2. DBT
3. DBL
4. PFM
Action at Destination Bank: Destination Bank can identify the different inward files based
on the inward file name as given below:
Product Type: "10 "
ACH-CR-ABCD-DDMMYYYY-000001-INW.txt
Product Type: "DBT"
ACH-CR-ABCD-DDMMYYYY-DBTO00001-INW.txt
Product Type: "DBL"
ACH-CR-ABCD-DDMMYYYY-DBLO00001-INW.tXt
Product Type:"PFM"
ACH-CR-ABCB-DDMMYYYY-PFMO00001-INW.tXt
The above changes will be effective from January 04, 2016. Member Banks are requested to
take a note of the same and make necessary changes in their system to handle multiple
inward files received under each sessions.
The member banks should put in place necessary controls to ensure that all the inward files
received for the day are reconciled with the settlement figures posted in their account with
RBl, credits/debits are accurately done in the core banking and returns are submitted on
time.
For any clarifications please write back to ach@npci.org.in
With warm regards,
(Giridhar G M)
VP and Head CTS & NACH Operations
1001A,TheCapital,BWing.10thFloor,BandraKurlaComplex,Bandra(E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067
