# Circular No 027 Implementation Mutual funds product type

Circular/reference number: OC-027

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCl/2020-21/NACH/CircularNo.027 February25,2021
To
AllNACHMemberbanks
Implementation-Mutualfund producttype
Referencemaybetakentocircularno.023datedDec30,2020.Asperthecircularthe
producttype“MUT"wastobe introduced effectivefromFeb15,2021howeveronrequestof
afewmemberbankstheimplementationwas postponedtoMarch01,2021.
Member banks are hereby advised to capture“MUT" in the file name and in product type at
recordlevel (Length262to264)forall mutualfundtransactions.EffectivefromMarch01,
2021 if the mutual transactions are not presented as per the specifications, the same would
not beprocessed intheMUT session.Pleasenotethat thesponsorbanks should arrangeto
Destination banks should take all measures to ensure thatthe transactions are processed
and responsesubmitted before11:30am.
Input, InwardandResponsefilenamestructureisprovidedinAnnexurel.
The informationhereinmaybedisseminatedtoall the concerned.
With warmregards,
GiridharG.M
(Chief- Offline product operations & technology)

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexurel
FileNamingConvention:
Inputfile
ACH-DR-<BANKCODE>-<USERID>-<DDMMYYYY>-MUT<XXXXXX>-INP.txt
Inwardfile
ACH-DR-<BANKCODE>-<DDMMYYYY>-MUT<XXXXXX>-INW.txt
Returnfile
No change in naming convention.Bank canfollowexisting process.
Responsefile
No change in naming convention.Existing process (as currently being shared by
NPCl)will continue.
