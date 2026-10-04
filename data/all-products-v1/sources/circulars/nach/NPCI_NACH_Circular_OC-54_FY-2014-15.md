# Circular No. 54 - Process change in Mandate cancellation

Circular/reference number: NPCI/2014-15/NACH/CircularNo.54

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2014-15/NACH/CircularNo.54
September04,2014
To,
AllNACHMemberBanks
Process Changefor Mandate Cancellation
IncompliancewiththeRBlcircularDPSS(CO)EPPDNo.1918/04.03.01/2011-12datedApril
18,2012 and also based on the feedback received from member banks, the mandate
cancellation process has been altered accordingly.
2.With effect from September 10, 2014, a mandate will be immediately marked inactive on
the cancellation request submitted on the NACH platform by sponsor bank or destination bank.
In contrast to the current practice on NACH, where the cancellation request shall need
acceptance from the receiving bank.As soon as cancellation initiated through GUl and
approved by the checker of the initiating bank, the mandate status would be updated as
cancelled.In case of upload through XML, as soon as the ACK file is received, the status of the
mandate would be updated as cancelled.
3. Receiving bank would continue to receive the cancellation request as a cancellation Inward
file. But, no acceptance file is required to be uploaded by the mandate receiving bank. This
data would be onlyfor information purpose.
4. Mandates once cancelled cannot be revived. As soon as the status of a mandate is changed
to“inactive', no further transaction can be initiated for the said UMRN number.
5.Pending cancellation requests, at the time of process change will be marked as expired,
basedonTAT.These requests will have to bereinitiated bythebank.
6.For any queries/further help,please get in touch with us at nachsupport@npci.org.in
Thanking you
Yoursfaithfully,
(GfridharG.M.)
VP and Head-CTS & NACHOperations
C-9,8thFloor
srr/Phone:02226573150
RBIPremises
a/Fax:02226571001
Bandra-Kurla Complex
-/email:contact@npci.org.in
Bandra East
400051 aaw/Website:www.npci.org.in
Mumbai 400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
FAQto the Circular
(i)What will be the newprocess of mandate cancellation?
Theprocess flow of cancellation of themandate is explained herein below.
Mandate cancellation raised in GUl:
The initiator of a mandate cancellation request message can be either the debtor (Destination
Bank)orthecreditor (SponsorBank)throughGUl.
Thereare no changes in the process of submission of cancellation request on the GUl.
The maker shall submit the mandate cancellation request on the GUl and upon
confirmation of checker approver, the mandate will be marked as cancelled
immediately.The mandate will then be visible in the removed mandate list.
Transactions pertaining to any mandate marked as cancelled shall be declined on the
NACHplatform.
The INW and RES will continue to be generated as per the existing process flow. INW
and RES will be generated in their respective sessions ie. INW at MRC and RES at MARC
by NACH and posted in respective bank inbox.
If the bank receiving the INWfile uploads an ACCEPTfile (forthe InwardFile received),
then system will reject with the reason"Cancel operation automatically accepted by
the system".
Mandate cancellation raised in XML:
The initiator of a Mandate Cancellation Request message can be either the debtor (Destination
Bank)or thecreditor (SponsorBank)throughXML.
Uponupload ofMandatecancellationxml'fromthe debtor or thecreditorthe
mandate will be marked as cancelled immediately.
Transactions pertaining to any mandate marked as cancelled shall be declined on the
NACHplatform.
The INW and REs will continue to be generated as per the existing process flow. INw
and RES will be generated in their respective sessions ie.INW at MRC and RES at MARC
byNACHandposted in respectivebank inbox.
If the bank receiving the INW file uploads anACCEPT file (forthe Inward File received),
then system will reject with the reason"Cancel operation automatically accepted by
the system".
Mandate cancellationraised byDCA:
The mandate cancellation requests initiated bya DCA will continue as per the existing
process,i.e.therequest will await Creditor/Debtor checkerapproval.Once approved,
themandate will be cancelled.

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Description Table:
Sponsor Bank initiated Destination Bank initiated
cancellation cancellation
Mandate Image Optional.The sponsor Optional.The destination bank may
bank may choose not to choose not to submit mandate image
submitmandate image
Physical mandate Optional Thebankmayprovideoptions to
submissionbycustomer
customer to cancel a mandate by way
ofa physical mandate,phonebanking
or net banking
Standardized NPCI Standardized mandate
Standardized mandate required only in
mandate required only in case
casewhere bank is submitting scanned
where bank is submitting copy of mandateon NACH
scanned copy of mandate
on NACH
Cancellationreason OnCustomer OnCustomerrequest
available request OnBankrequest
OnCorporate Account
request closed/blocked/frozen/inopera
tive
XML file upload Available Available
GUI Available Available
Mandate category based Mandate from all Mandatefromall category is available
restriction on category is available for forcancellation
cancellation cancellation
Initiated (Receiving) NO NO
party approval required
TATfor receiving party Mandate cancellation Mandate cancellation doesn't require
to approve doesn't require approval approvalandmandateshallbemarked
and mandate shall be as inactiveimmediately upon
marked as inactive submissiononNACH.TATnot
immediatelyupon applicable.
submission on NACH.TAT
notapplicable.
Result of TATexpiryasa TAT not applicable. TAT not applicable.
result of no action by
recipient bank
Impactofcancellation Mandate cancellation Mandate cancellationdoesn'trequire
confirmation by doesn't requireapproval approvalandmandateshallbemarked
receiving party and mandate shall be as inactive immediately upon
marked as inactive submission on NACH.

<!-- Page 4 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
immediatelyupon
submission on NACH.
Impactofcancellation Mandate cancellation Mandate cancellation doesn't require
rejection byreceiving doesn't require approval approval and mandate shall be marked
party and mandate shall be as inactive immediately upon
marked as inactive submission on NACH.
immediatelyupon
submission on NACH.
(ii)What are reports available for mandate cancellation and in what format?
Tworeportswillbeavailableunder“MMs Reports"inMiSLink:
a.CancellationReport
b.CancellationAuditReport-InitiatingParty
Both thereports canbe downloaded by thebank in excel, csvorpdfformats.
