# IMPS I OC 86 I FY 18-19 I Alignment of member bank switches towards IMPS online technical specification

Circular/reference number: NPCI/IMPS/0CNo.84/2018-19
Date: 24th April, 2018

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI:2018-19:IMPS:0C86 Oct 16, 2018
To,
All MembersofIMPS
Madam/ Dear Sir,
Sub:Alignmentof memberbank switchestowards IMPsOnlineTechnical Specification
IMPS switching system (IMPSBharat Switch)supports P2P,P2A,P2Uand FIRbased transactions.IMPS
OnlineTechnical Specificationsmandatescertaincompliancesontheonlinemessagesexchangedbetween
member switch and IMPS Online switching platform.Currently in IMPs Online Switching System, it was
Specifications.
For e.g., Though some of the fields are mentioned as mandatory fields in the response message from
member switch ORto beechoedbackwithvalueas received intherequest message ORtobepopulated
with allowed values specified forthe field, it was observed that some of the member switches are not
strictly complying as a result of which IMPs switch at NPCl is made to ignore or accommodate such non-
compliances. Such scenarios lead to mismatch in data elements handling across the ecosystem with
Inordertoestablishcomplianceforonlinemessages withIMPsOnline Switching Specifications,NPCihas
initiated IMPS specification alignment activitywith member banks.
It is to be noted that NPClis NOTintroducing any new compliance rules but ONLYenforcing the compliance
rules as per the already existing IMps specifications in order to align the member bank online switching
platform.
NOTE:
All acquirer compliances will be declined with Invalid Transaction (Rc-12). Transaction will not be
declined incaseof issuercompliance.
In this regard, NPCI has issued a circular - NPCl/iMPS/0c No 84/2018-19 dated 24th Apr 2018 for member
banks to certify using BosS simulatorand comply by 16th Aug 2018.Though most of the members are certified
and enabled inproduction,fewofthememberbanksareyettocertify.
Beyondthis date,NPCI switch would start decliningthenon-compliantonlinerequest messages from acquirer
memberbank switch.
Page 1 of 2
1001A,The Capital,BWing.10thFloor,Bandra Kurla Complex,Bandra(E),Mumbai 400051.T:+912240009100F:+912240009101www.npci.org.in
CIN.1174990MH2008NPI189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Those who have already certified and enabled the compliance in production, kindly ignore this circular.
Kindly make a note of the above and disseminate the instructions contained herein to the officials concerned
inordertoverifythecomplianceof youronlineswitchingapplication.
Foranyqueriesorclarification,pleasecontact:
Name e-mail ID Mobile
Number
Sarthak Choudhary sarthak.choudhary@npci.org.in 9022077266
Bharat Nanavati bharat.nanawati@npci.org.in 8879760297
Yours faithfully,
SD/-
Dr. N. Rajendran
Chief Technology Officer
Encl:1.Alignmentof memberbank switchestowardsIMPSOnlineTechnical Specification (Circularno.
84dtd.24.04.2018)
Page2of2

<!-- Page 3 -->

NPCI
NATIONAL PAYMENTS CORPORATIONOF INDIA
NPCI/IMPS/0CNo.84/2018-19 24th April, 2018
AllMembersofIMps
Madam/Dear Sir,
Sub:Alignment of member bank switches towards IMps Online Technical Specification
Technical Specifications mandates certain compliances on the online messages exchanged between member
switch and IMPs Online switching platform.Currently in IMps Online Switching System,it was observed that many
of the memberbanks are not fully compliant with IMps Online Technical Specifications. E.g.though some of the
fields are mentioned as mandatory fields in the response message from member switch OR to be echoed back
with value as received in the request message OR to be populated with allowed values specified for the field, it
was observed that some of the member switches are not strictly complying as a result of which IMPs switch at
NpClis madeto ignore or accommodate suchnon-compliances.Such scenarios lead to mismatch in data elements
handling across the ecosystem with cascading effect onto otherbanks and subsequent clearing & settlement and
dispute processing.
Atahighlevel,thismandateaddresses thefollowingkeyaspects:
1.Request/ Responsereceivedfrom member bank switchmust contain all the mandatory fields, conditional
data and valid values in fields as per IMpS Online Switching Specifications.
2. Member bank switch must not reject transactions basis the absence of optional fields in the message
receivedfromNPCIIMPSSwitch.
Specifications)withvaluesassentbyIMpsSwitchintherequest.
In ordertoestablishcomplianceforonlinemessages withIMPsOnlineSwitching Specifications,NPClhas initiated
IMPSspecificationalignmentactivitywithmemberbanks.
It is to be noted that NPCI is NOT introducing any new compliance rules but ONLY enforcing the compliance rules
as perthealready existing iMps specifications in order to align the memberbank online switchingplatform.
declined in case of Issuer compliance.
Please referthe matrix as per Annexure A attached herewith for the IMpS online mandates to be implemented by
16th August 2018. Member banks must share the mandate document with their AsPs/Product vendors for their
perusal and take necessary action in order to make their switch compliant with the mandate.

<!-- Page 4 -->

NPCI
NATIOWALMYMENTSCORPORATIONONOA
Introduction of Bharat Online Switching Simulator (BOsS):
In ordertosimplify the certification process, NPcl will be providing banks with Bharat Online Switching Simulator
which is a Windows based standalone simulator.The member banks will be able to install the same at their own
premises (in case of banks served by AsPs, it will be installed by ASPs in their premises) and connect with their
switch.Memberbank (in liaison with their vendor/AsP) hasto perform the online transaction by connecting their
switch to simulator for the applicable test scripts and submit the logs (generated from simulator) to NPCl. NPCi
certification team will verify the logs and confirm the compliance to MemberBank.
Activity Timeline
NPClProvidesBOSSsimulatorinstallabletomemberbank(ortheirASP
15thMay2018
incaseofhosted member banks)
Start:1"June2018
Dateforsubmitting the simulatorlogsto NPCl
End:31July2018
Please make a note of the above and disseminate the instructions contained herein to the officials concerned in
ordertoverify the complianceof your online switching application and take necessary action.
Forany queries or clarification, please contact:
Name e-mailID
Sarthak Choudhary sarthak.choudhary@npci.org.in
Bharat Nanawati Bharat.nanawati@npci.org.in
Yours faithfully,
SD/-
Ram Sundaresan
SVP&Head-Operations
Encl: 1.Annexure A-IMPS_Mandate_2018 Version 1.0.pdf
