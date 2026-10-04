# AePS | OC 32| FY 18 19 | Alignment of Member Bank switches towards AePS Online Technical Specifications

Circular/reference number: NPCI/2018-19/AEPS/002

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI:2018-19:AEPS:OC007 Oct 16, 2018
To,
All Membersof AEPS
Madam/ Dear Sir,
Sub:Alignmentofmemberbank switchestowardsAEPSOnlineTechnical Specification
AEPS switching system(AEPS Bharat Switch)supports ISO and XMLbased transactions.AEPS Online
Technical Specifications mandates certain compliances on the online messages exchanged between
member switch and AEPS Online switching platform.Currently in AEPS Online Switching System, it was
observed that many of the member banks are not fully compliant with AEps Online Technical
Specifications.
For e.g., Though some of the fields are mentioned as mandatory fields in the response message from
member switch OR to be echoed back with value as received in the request message OR to be populated
with allowed values specified for the field, it was observed that some of the member switches are not
strictly complying as a result of which AEPS switch at NPCl is made to ignore or accommodate such non-
compliances. Such scenarios lead to mismatch in data elements handling across the ecosystem with
In order to establish compliance for online messages with AEPs Online Switching Specifications, NPCI has
initiatedIMPS specificationalignment activitywithmemberbanks.
It is to be noted that NPClis NOTintroducing anynewcompliance rules but ONLYenforcing the compliance
rules as per the already existing AEpS specifications in order to align the member bank online switching
platform.
NOTE:
1. The mandate is only for Iso services member banks and is not applicable for XML services
member banks.
2. All acquirer compliances will be declined with Invalid Format (RC-3o).Transaction will not be
declinedincaseof Issuercompliance.
In this regard, NPCI has issued a circular - NPCl/2018-19/AEPS/002 dated 18th Apr 2018 for member banks to
certify using BOss simulator and comply by 16th Aug 2018. Subsequently, another circular - NPCl/2018-
19/AePs/011 dated 27th Aug 2018 had also been sent as a reminder with deadline extended to 30th Sep 2018.
Though few of the members are certified and enabled in production, others are yet to certify.
We are extending the deadline upto 31st Dec 2018 for pending banks to certify and comply in production.
Beyond this date, NPCl switch would startdeclining the non-compliant online requestmessages fromacquirer
member bank switch.
Page 1 of 2
1001A,The Capital,BWing.10thFloor,Bandra Kurla Complex,Bandra(E),Mumbai 400051.T:+912240009100 F:+912240009101www.npci.org.in

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Those who have already certified and enabled the compliance in production, kindly ignore this circular.
Kindly make a note of the above and disseminate the instructions contained herein to the officials concerned
inordertoverifythecomplianceofyouronlineswitchingapplication.
Foranyqueries orclarification,pleasecontact:
Name e-mail ID MobileNumber
Krishna Chaitanya krishna.chaitanya@npci.org.in 8978720088
Nayan Bhandarkar nayan.bhandarkar@npci.org.in 8108122829
Yours faithfully,
Dr.N.Rajendran
Chief TechnologyOfficer
Encl:1.Alignment of ISO memberbank switchestoAEPSonline specs (Circularno.002dtd.18.04.2018)
2.Aignment of isOmemberbank Switches toAePSonlinespecs (Circualr no.011dtd.27.08.2018)
Page 2 of 2

<!-- Page 3 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2018-19/AEPS/002 18thApril, 2018
To,
All Members ofAadhaar Enabled PaymentSystem (AePS)
Madam/Dear Sir,
Sub:Alignment of ISO member bank switches towards AEPS Online Technical Specification
AEPS switching system (AEPS Bharat Switch) supports ISO and XMLbased transactions.AEPS Online
Technical Specifications mandates certain compliances on the online messages exchanged between
member switch and AEPS Online switching platform.Currently inAEPS Online Switching System,it was
observed that many of the member banks are not fully compliant with AEps Online Technical
Specifications. E.g.though some of thefields are mentioned as mandatory fields in the response message
from member switch OR to be echoed back with value as received in the request message OR to be
populated with allowed values specified for the field, it was observed that some of the member switches
are not strictly complying as a result of which AEPS switch at NPClis made to ignore or accommodate such
non-compliances.Such scenarios lead to mismatch in data elements handling across the ecosystem with
At a high level, this mandate addresses the following key aspects:
Request/Responsereceivedfrommemberbank switchmustcontainall themandatoryfields,conditional
data and valid values in fields as per AEPS Online Switching Specifications.Member bank switch must not
reject transactions basis the absence ofoptional fields in the message received from NpCl AEPs Switch.
Response from member bank switch must echo back certain fields (as per AEPS Online Switching
Specifications)withvaluesassentbyNPCIAEPsSwitchintherequest.
Inordertoestablish complianceforonlinemessageswithAEPsOnlineSwitching Specifications,NPCihas
initiated AEPS specification alignment activity with member banks,It is to be noted that NPCI is NOT
introducing any new compliance rules but ONLY enforcing the compliance rules as per the already existing
AEPS specifications inordertoalignthememberbankonlineswitchingplatform.
NOTE: The mandate is only for ISO services member banks and is not applicable for XML services
member banks.All acquirer compliances will be declined with Invalid Format (R-3o).Transaction will
not be declined in caseof Issuer compliance.
Please refer the matrix as per Annexure A attached herewith for the AEps online mandates to be
implemented by 16th August 2018.Member banks must share the mandate document with their
AsPs/Productvendorsfortheirperusal and necessaryactioninordertomaketheirswitchcompliantwith
the mandate.
Page 1 of 2

<!-- Page 4 -->

Introduction of Bharat Online Switching Simulator (Boss):
In order to simplify the certification process,NPCI will be providing banks with Bharat Online Switching
Simulator which is a Windows based standalone simulator.The member banks will be able to install the
and connect with their switch,Memberbank (in liaison withtheirvendor/Asp)has to perform the online
transaction by connecting their switch to simulator for the applicable test scripts and submit the logs
(generated from simulator) to NPCl. NPCl certification team will verify the logs and confirm the
complianceto Member Bank.
Activity Timeline
NPCl will provides BosS simulatorinstallabletomemberbank(or
theirAsp incaseofhostedmemberbanks) 15thMay2018
Start:1stJune2018
Date for submitting the simulatorlogs to NPCl
End:31st July2018
Please make a note of the above and disseminate the instructions contained herein to the officials
action.
Forany queries or clarification, please contact:
Name E-mail Contact Number
Mr.Krishna Chaitanya krishna.chaitanya@npci.org.in 040-33026354/8978720088
Mr.Ajit Goswami ajit.goswami@npci.org.in 022-40508538/8291847150
Yours faithfully
Ram Sundaresan
SVP& Head-Operations
Encl:1.AnnexureA-AEPs_Mandate_2018_Version_1.0.pdf
Page 2 of 2

<!-- Page 5 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2018-19/AePS/011 August27,2018
To,
All Members of AadhaarEnabled PaymentSystem(AePS)
Madam/Dear Sir,
Sub:Alignment of Iso member bank switches towards AePs Online Technical
specification
We refer toourCircular-NPCl/2018-19/AePS/002dated18th April,2018Sub:Alignment of
ISOmemberbank switchestowardsAePSOnlineTechnical Specification.
In order to establish compliancefor onlinemessages,NPCl has initiated AePS specification
alignment activity with member Banks.
Please note that NPCI is NOT introducing any new compliance rules but ONLY enforcing the
compliance rules already existing in AePS specification.
services memberbanks.
To help and assist member Banks who have not completed this certification process we have
extended the date for the AePS Online Technical Specifications mandate implementation to
September30,2018.
mentioned target date.
Kindly disseminate the information contained herein to officials concerned so as to ensure
compliance of youronline switchingapplication.
For any queriesorclarification,pleasecontact:
Name E-mail Mobile Number
Krishna Chaitanya krishna.chaitanya@npci.org.in 8978720088
Nayan Bhandarkar nayan.bhandarkar@npci.ora.in 8108122829
Yours faithfully,
RamSandaresan
SVP &Head-Operations
Encl:
AnnexureA:NPCICircular:NPCl/2018-19/AePS/002
