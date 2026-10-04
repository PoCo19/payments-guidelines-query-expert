# NFS OC 134 RBI Circular on Rationalisation of Number of Free transactions

Circular/reference number: NPCI/2014-15/NFS/134
Date: 14th August 2014

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Note:NPCI/2014-15/NFS/134 18thSeptember2014
To
AllMembersofNationalFinancialSwitch
RBl circularonRationalisationofnumberoffreetransactions
We refer to RBl circular RB1/2014-15/179 dated 14th August 2014 on the above subject. As instructed therein,
effective 1st November2o14, the number of mandatory freeATM transactions for savings bank account customers at
other banks'ATMs is reduced from the present five to three transactions per month (inclusive of both financial and
non-financial transactions) for transactions done at the ATMs located in the six metro centers, viz. Mumbai, New
Delhi, Chennai, Kolkata, Bengaluruand Hyderabad.
InordertofacilitatebankstoidentifysuchATMtransactions,wesuggestasfollows:
Responsibility as anAcquirer
i) Acquiring Banks/WhiteLabel ATM Operators (WLAOs)are required topopulatean identifier i.e.a special
character‘+'(plus)asthefirstcharacterinDateElement (DE)43oftheonlinemessage.This istobedone
onlyforATMslocatedintheaforementionedsixcitiesspecifiedbyRBl.
E.g.foranATMlocatedat lITMainGate,Powai,Mumbai,Maharashtra,thedetails inDE43shouldbeas
follows:
DE43
Position Length FieldName Description
01-23 23 TerminalAddress +llTMainGate,Powai
24-36 13 TerminalCity/District Mumbai
37-38 TerminalState MH
39-40 TerminalCountry IN
i) Populate the correct PIN codeof the ATM in DE 61 of the onlinemessage.This isas per extant NFS
guidelines.KindlyreferOC69(copyenclosed)formoredetailsonthesame.
iii) Acquirers will be responsible formaintainingthe correctness of the identifiers (point i)and the PiN code
being populated in the online message since this will have a direct impact on the charging to the
customers.
iv) In case of any change due to ATM relocation etc., acquirers must update wherever necessary to ensure
thatanycharges leviedbyIssuingBanktothecustomeriscorrect.
C-9, 8th Floor r3q/Phone:02226573150
RBlPremises q/Fax:02226571001
Bandra-KurlaComplex 专-/ email: contact@npci.org.in
BandraEast a/Website:www.npci.org.in
q - 400 051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
ResponsibilityasanIssuer:
Issuing Banks will have the option of either referring the identifier in DE 43 or the PIN Code in DE 61 or a
combinationofbothfordeterminingthechargeabilityasperRBlmandate.
Issuingbank can liaisewiththeAcquirertoascertainthelocationof theparticularATM.
NPCIwill betakingthefollowingstepstofacilitateoperationalizationof theRBlcircular:
1) Following up with banks for populating the identifier in DE 43 and PIN code in DE 61 of the online message.
2) Publishing escalation matrix for each bank which can be referred by banks in case of any discrepancy in the
details populated in the online message.This information will be sought via mail and the consolidated list will
bereviewedatregularfrequency.
Please feel free to contact the below mentioned officials for any further clarifications or assistance on this:
Mr.AmitShetty(amit.shetty@npci.org.in/8108108674)
Mr.GururajRao(gururaj.rao@npci.org.in/8879772795)
Thanking You.
Yours faithfully,
DilipAsbe
ChiefOperatingOfficer
Encl
