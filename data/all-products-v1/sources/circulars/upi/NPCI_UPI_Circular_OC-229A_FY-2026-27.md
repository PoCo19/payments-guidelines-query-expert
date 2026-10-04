# UPI OC-229A_ ISD GSTIN (Input Service Distributor) Option in UPI URCS Back-office system

Circular/reference number: NPCI/UPI/OCNo.229A/2026

<!-- Page 1 -->

NPCL
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/ UPI/OCNo.229A/2026 -2027 August 24, 2026
To,
All Members of Unified Payment Interface (UPl)
Subject: Implementation of Revised ISD-GsTIN (lnput Service Distributor) Option in URCS
Back-Office System
We refer to UPI OC No. 229/2025-2026 dated 12th Nov 2025, wherein it was communicated.
pursuant to detailed deliberations with member banks, that the Input Service Distributor
(ISD)/GSTIN option would be enabled in the URCS system for both payable and receivable
sections. Accordingly, NPCI has implemented the functionality in URCs on 17th Nov 2025.
Subsequent to the implementation, member banks opined that the IsD input is applicable solely to
the payable section and does not extend to the receivabie section. Based on this feedback, the
ISD functionality has been disabled in URCs on 28th Nov 2025, an email notification has been
issued on 28th Nov 2025 indicating that the changes will be carried out as per the feedback and
deployed upon completion of the development and testing activities.
In light of the above, please be informed that the following functional changes have been
incorporated:
a) The receivable section has been removed from the IsD functionality. Users will now be
able to update IsD details only for the payable section.
b) Upon updating from ISD to GsTiN or vice versa, any change in the state code will result in
URCS applying the applicable GST and processing settlements accordingly.
Users are permitted to update only one GSTIN or ISD per product per bank in a month.
d) ISD/GSTIN update should be submitted in URCS between the 15th and 31st or last day of
every month. This timeline ensures that the changes are reflected in the system and
incorporated into the reports generated on the 1st of the subsequent month. Back Office
system will not permit users to update ISD/GsTIN details between the 1st to 14th of
every month. This arrangement has been implemented to ensure the smooth
generation of monthly GsT reports, which are typically prepared and shared during
the first week of every month.
Note: GsTIN details of all member banks are pre-configured in the URCS system at the time of
onboarding. Members are advised to utilize the revised functionality only if opting for IsD. In all
other cases, the existing GsTIN-based reporting mechanism shall continue to apply.
Go-Live Date: Revised ISD-GSTIN functionality will be made live on Sep 15, 2026.
Member banks are requested to take note of the above and disseminate this information to the
officials concerned.
Warm Regards,
SD/w
Giridhar GM
Chief-Customer Success
Enclosed: Annexure - A Step-by-Step Maker-Checker User Guide. 1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Banara (E), Mumbai 400 051.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPE.189067

<!-- Page 2 -->

NATIONAL PAYMENTS CORPORATION OF INDIA
Annexure -A
Procedure for Updating ISD-GSTIN in the Back Office System
1. Login and Navigation
To begin, the user must log in to the back-office system. From the home page, select the
"Update ISD-GsTIN" option in the main menu. The system will display the definition of
IsD details and prompt for confirmation. Click "click to Proceed" to continue.
2. Selecting Report Type and Updating ISD
After proceeding, the system prompts the user to select Payable Report. Upon selection,
two options are displayed: IsD and GsTIN. The user should choose the appropriate option
based on the requirement and then submit the request.
Once submitted, the request moves from the Maker Tray to the Checker Tray. The
checker is responsible for reviewing and verifying the details entered by the maker. Upon
approval, the system updates the ISD information and generates the monthly GsT reports
accordingly.
3. Timeline for ISD-GSTIN Updates
Updates to the ISD/GSTIN should be submitted between the 15th to 31st of every month to
ensure that the changes are reflected in the system and that the corresponding reports are
generated on the 1st of the following month. Back Office system will not permit users to
update ISD/GsTIN details between the 1st to 14th of every month. This arrangement
has been implemented to ensure the smooth generation of monthly GsT reports,
which are typically prepared and shared during the first week of every month.
entire reporting month. For example, if a bank updates the ISD on 20 August, the GsT
report generated on 5 September for August month transactions will reflect the revised IsD
for all transactions processed during August-2026, rather than only for transactions
processed from a specific date within the month.
1001A, The Capital, B Wing, 10h Floor.
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 O51.
T: +91 22 40009100 F: --91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
User Manual-For Updating the ISD GsTIN
Maker Process
Log in to the URCS Back Office system and navigate to update IsD → Update IsD.
Enter the required information in all mandatory fields and click Submit. Once
further processing.
NPC tast Login:17-Sop-2515:44:10 Walcomet hdivarshinimk
Update ISD
DESCRIPTION
User tManagement Fadltatesadditicon andmodicationofmemberBankUsers.
Fie Upicad FacllatosbulkuploadofAdfustmenils andDispules
Following screen shotappeared for maker user click on proceed.
GsTChange InputServiceDistrloutor(isD)
As ber the amandment in the GsT laweffoctive trom 1st Aprll 2o2s, the provisions with reepoct to tsD (input Sorvice Distributor) rogistration
havo bocome mardatory for ontitieg having a preenice In matlpie stahos n india Tha sald mechaniasm reguirea entities to distribyate inpuat tax
Aorxardirngly, mamterm can now sutarnn GsT ctalrd aing tha IsD ophon Sot cantralized alaim diatriDuticn borows tmaimn Ta comply wi wsa
law,banik can choose to have aither ths isD ar GtiN printed in thair montsly GsT reperts.Artar clicking"proos, usgru will bp premptad
to maluet IsD or CsriN for both Payibla nd Recvables eports. Bated on the aalechion, the syubam wil aanawmte tra oorrauconding CsT
Thit ls  checkercontroflad ootivity Approved charnges wilt rehoce in GsT reports from me naxf monty
ChcRto Pioceed
EnterISDdetails
Enter IsD Details
OATIN
O FBC *
1001A, "The Capital, B Wing, 1oth Floor.
Bandra Kurla Complex, Bandra (E), Murrbai 4oo Qs1.
T: 491 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL.189067

<!-- Page 4 -->

NPCI
rehat a enm fy
NATIONAL PAYMENTS CORPORATION OF INDIA
Once the maker clicks the submit button, an acknowledgment message stating
"Submitted for approval" will be displayed on the screen.
Submitedforapproval
EnterISD Details
&ST Report Preference
Payablas'
E 1D Registratbon
IBD Adctrass Ino 1" ISDAdbrosine2 ISDAddrssn3
LogalAdreis Legaul Adcrous LegalAdtress
B)CheckerProcess withapproval option
1) Checker should login to the back-office system and Navigate to: IsD →> Member IsD,
details entered by the maker > Checker will be provided with two options “Approve or
Reject" > User has to click on Approve > back-office system will ask for confirmation
"Are you sure you want to approve this ISD/GsTIN" > Ok / Cancel > User to click on
Ok > back-office system provides the acknowledgement as “Action completed
successfully".
a) URcs Back-office checker userselectISD-> MemberISD
127.0.0.1687268/upVaachloginm
LastLooin:D3-Awg-2617:53-11 Winicamatanbvarsh
Menibor1so
DESCRIPTON
Usor Alansgomon! Facliestes additionandmodification olmembes Bark Ueor
Fle Uplcad Facilitates Osfk upioad of Adjustments and Disputins
Transaeson Soovch Facieatos trarvocion sosrch,
Fle Dxrnioad Facinitales downloadirig ot Sellernerit Flosbxoith Indvidunlly anid Buk
Roparis Faciltatosdownloediog otfoports limitodtomemborBlarska,
FacilaaloeAdatonandModicationorBroademtMoaasrgos,E-Libotaryhod EeealationMlarik.
Flo Apecr FacilitalesAuthertieationafAdustments/CnputioainBulk
Trarsaction Aporoval Facilitstos Aunorcadon df Caputat adjusuroris ar transaction tevet individuany.
b) URCs Back-office checker approval
1001A, The Capital, B Wing, 10th Floor
Bandra Kurla Complex, Bandra (E),Mumbai 4oo Os1.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.1r
CIN: U74990MH2008NP189067

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
t CT Rapoet Pretorenon
Ppyables"
to Regatration
ISDAddreseine2*
L,agwl Addru Lagul:Addrons
Chenn
BO$STAXCOOS IGDGGTIN- GDFEC
33AACH2702-C2Z HOFCOS90O
ravod
127.0.0.1195718/up/isdApproval
127.0.0.119:5718cays
Al vou fiure you want to apprDve tiis IsD etry?
Submit the changes ISD GSTIN details available in URcS back-office system for
checker approval.
NPCI
Lost Login:17-Sep-2515:51:09 Wolcomet
UserMinagemertFleAppoveTrangacteon Apptoval-FileDownbadReportsCommunicatonLueDsabe-GenencGoodFathAdjus
Aconmpietedsuoss
2) Checker process
The Checker is provided with two options: Approve or Reject.
a) Approval Process: When the Checker selects the Approve option in the URcs Back
approve this IsD entry?" with OK and Cancel options.
i) If the Checker clicks Cancel, the system redirects the user back to the previous
page, where the Approve and Reject options remain available for further action.
'o01A, The Capital, B Wing, 1oth ploar.
Bandra Kuria Complex, Bandra (E), Mumbai 4oo Os1.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 6 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
127.0.0,126;S961/uPVisdApproval
Payoblos *
ISD
st.Koglstrauon
ISDAddregs Iine 2 * ISD Addresa Ilno 3 *
Iad addrgna3 Iod addroaa3 Isc addren3
IBD Ginte rco Clly * IS0 Pineode*
Maharanhtra maharashtra ZOOEO
SDSTAXCODE ISD GSTIN * ISD FEC *
27AAACPD16BG1ZS ANDBODO0001
Kojecfed
i) if the checker clicks OK, the URcs system displays a confirmation message
stating,"Action completed successfully"
Actian completad auooessflly.
Enter ISD Details
E GsTRaportPreference
Psyablea *
G9TN
1S ISD Reglatradon
悠Addrass llne 1  CD Addreaa line 2 * 16DAddresn fino @ *
ISDSt* ISD Clty' ISo PIncode*
b) Rejection Process: When the Checker selects the Reject option in the URcs Back Office
entry?" with oK and Cancel options.
i) If the Checker clicks Cancel, the system redirects the user back to the previous
page, where the Approve and Reject options remain available for further action.
ii) If the Checker clicks OK, the rejection is processed successfully, and the IsD
GSTIN details are not updated in the URcS system and the request is rejected.
1001A, The Capital, B Wing, 1oth Floor,
Bandra Kurla Complex, Bandra (E). Mumbai 4oo o51.
T: +9122 40009100 F: +91 22 40009101
contact@npci.ara.in www.npci.org.in
CIN: U74990MH2008NPL18$067

<!-- Page 7 -->

NPCI
arey e rrey far
NATIONALPAYMENTSCORPORATIONOFINDIA
ISb Form
127,0.0.126:$961/UPl/isdApproval
127.0.0.126;5961 says
Art you sure you wint to reject thls ISD entry?
cana!
ili) If the Checker user rejects the IsD update request, the Maker user will retain
access to the IsD GsTIN Update functionality in the URcs system. The Maker
can then modify the IsD details as required and resubmit the ISD GsTIN update
request for approval.
Submitted forapproval
EnterISDDetails
 GST Repor Pruterence
Psyables'
 Isp Registration
ISDAddress Ine1" 1SDAddress Iie2" ISDAddress ine 3"
LogalAddress LogalAddrous Linpel Addrens
1001A, The Capital, B Wing, 10th Floar.
Bandra Kurla Complex, Bandra (E), Mumbai 4oo O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067
