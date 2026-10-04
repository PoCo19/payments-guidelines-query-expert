# NPCI/2017-18/CTS/003 National Archival services - API - All

Circular/reference number: NPCI/2017-18/CTS/003

<!-- Page 1 -->

NPC
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2017-18/CTS/003 May 16, 2017
To
AllCTSMemberBanks
ChequeTruncationSystem(CTS)
NationalArchival Services-APl(ApplicationsProgramInterface)
Refertoour letter #NPCI/2-13-14/CTS/2755 onNationalArchivalServices(NAS).As on
date 222 banks are availing this facility. We are further extending the value added services
by allowing the banksto retrieve the CTS cheque images from NAS using APl.Inthe first
phase, banks connected through NPClnet will be allowed to connect through APl.
Thetechnical specification document(TSD)"Archival Content Services IFs-RevF5"is
provided in AnnexureI.Banks can build APls as per the TSD and use the images retrieved
for internal use as well as for displaying the image to the end customer that are using
internet banking.Banks should authenticate the customer on the internet banking channel
orbyanyothermeansbeforedisplayingtheimagestothem.Pleasenotethat
1.UsingAPl oneimagecanberetrievedatatime.
2. Bank should send all mandatory fields as per technical specification document along
with UDK in the retrieval request. For this purpose banks should start storing unique
identificationnumber(UDK)alongwiththeinstrument numberandotherdetailsso
thatretrievalwill becomeseamless.Bankneedto frameUDKforbothoutwardand
inward instruments. Specification for framing UDk is provided in Annexure 1, also
may please refer to Appx 4.1.3.3 of CHl specification document version 2.5 Page
no.82.
3.In any instance duplicate entries (cheque number,payor branch routing number,
amount are the validation fields) are found then bank should not display any image
to the customer, the APl should provide appropriate text expressing inability to
show the image. To avoid such scenario of duplicate images retrieval banks should
necessarily provide UDK in all the retrieval request initiated by the customers.
4. Only for internal usage, i.e. retrieval of image by staff for resolution of
queries/complaints, the bank may display all the images retrieved from NAS. It is
advisedto useUDKforinternal retrieval request aswell.
5.The facility will bemadeavailableonly tothe banks that have executed the SLA
withNPCl.
Banks are advised to strictly adhere to the work flow of not displaying duplicate images to
the customer (refer to point 3 above). Banks will be solely liable for costs and
consequencesof anybreachbywayofprovidingtheimages of chequeissued/depositedby
onecustomertoanother.
1001A,The Capital, B Wing,10th Floor,Bandra Kurla Complex,Bandra (E),Mumbai 400 051.T:+912240009100 F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
In the second phase,banks connecting through internet will be allowed to retrieve images
through APl. A separate communication will be sent to the banks on this. All the member
banks are advised to use the facility and provide value added service to the customer. If
anyfurther clarificationis required youmay reachout to:
Sankar -044-28160740-sankar.muthupandi@npci.org.in
Sundarganesh-044-28160735-sundar.ganesh@npci.org.in
SarathyM -044-28160707-sarathy.muralidharan@npci.org.in
SridharV -040-33026315-sridhar.vedula@npci.org.in
Thanks&Regards
GiridharGM
(VP&HeadOperations-CTSandNACH)
Encl:ArchivalContentServicesIFS-RevF5
Annexure1-UDKspecificationwithexample

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexurel
UniqueDocument Key (UDK)for that item and consists of
<PresentmentDate><PresentingBankRoutNo><CycleNo><ltemSeqNo>
AttributesofItems
Attributename Description/Format Type Size Usage
PresentmentDate Dateofcaptureofchecks Date
PresentingBankRoutNo Routingnumberofthepresentingbank NS
CycleNo Capturecycleno. NS
This is a uniqueidentifier for the bank fora
"PresentmentDate"Suggested
ItemSeqNo NS 14
combination:<SorterlD(6)><Run
No(2)><Sequence No(6)>
Example:
PresentmentDate 16052017
PresentingBankRoutNo 600002000
CycleNo 17
ItemSeqNo 21272112123456
If any outward/inward instrument received withabovedetails,then UDK forthischeque
numbershouldbederivedasbelow
UDK 160520176000020001721272112123456
