# Circular no.011 - NACH Session Linkage

Circular/reference number: NPCI/2021-22/NACH/011

<!-- Page 1 -->

NPCI
NATIONALBAIMENTSCORPORATIOWONDIA
NPCI/2021-22/NACH/011 Feb28,2022
To,
AllNACHMemberbanks
NACH session linkage
NACH systems works on session linkage wherein eachpresentation session islinkedtoa return
session.In order to bring in more efficiency in providing the finality of the transactions and settling
thefunds ithas been decidedtomodifythe session linkagewiththefollowing changes:
1.Multiplepresentationstobelinked toa singlereturnsession.
2. Multiple settlements within a presentation or retum session.
In orderto facilitate the banks to handle themultiple inward files (destinationbanks),response
files (sponsor banks)the system is designed to provide the indicators in the file names,
accordingly file naming convention for inward and response file names have been modified.
Further a new field is introduced in the response file that will include the cycle identifier in the
LedgerFolioNumberfield. Thetechnical specification document isenclosed.
Banks will get the response files for accepted or returned records that are tagged to a settlement
cycle. Settlement cycle wise response files will help bank to reconcile the returned / accepted
transaction with minimum time to release their funds to customer utilization. Additionally, at the
end of the sessionfinal response willbegenerated with all therecords.
NPCl shall go live technicallyonMarch05,2022 andthe pilot sessionforthebankswill be
conducted on March 13,2022 by allowingmultiple settlements for'MUT"product return session.
Modification for other products will be carried out in a phased manner to complete the
implementation beforeMarch31,2022.
Memberbanks are advised to take note and disseminate the information to all the concerned and
completethe developmentas perthespecificationprovidedfor smooth implementation.
With warm regards,
GiridharGM
(Chief-Offline product operations &run technology)

<!-- Page 2 -->

NPCI
NAYIOWNALIMENTSCORFORATION OFINCLA
Annexure1 (specification document):
Changes at the Bank Side:
Presentation and Return Session: -
generate the settlement file, Inward Generation and Response generation as per session
processing.
Inward Generation: -
File naming convention of Inward file will be changed; session cycle will be included in the file
name, which will signifythe cycle numberofthepresentation session.
1.FileNaming Convention of the inward filewill be ACH-CR-HDFC-08042020-
TPZ000758511-P1C1-INW.txt; here theP1will signifythePresentationSession ldentifier
and C1 will signify the Settlement cycle of that presentation session. Here each
presentation session can have n settlement cycle so the cyclenumber will rangefrom C1
to CN.
2. During the final settlement cycle of the presentation session; the file naming convention
of the inward file willbeACH-CR-HDFC-08042020-TPZ000758514-P1FC-INW.txt;here
the P1 will signify the Presentation Session ldentifier and FC will signify the Final
Settlement cycle of that presentation session.
3.New value i.e.Inward Generation Date will bepopulated in both txt and xml file at header
level; in order to signify in which date the inward is being generated. Bank needs to be
included the same value without changing in the return file for the corresponding Inward
file.
ResponseGeneration:
File naming convention of the response file will be changed; the presentation session identifier
and return session cycle identifierwill be included inthe filename.
1.FileNaming conventionof theresponsewillbeACH-CR-SBIN-SBINH2H-26082021-
00001-P1C1-RES.txt;heretheP1will signifythePresentationSessionldentifierinwhich
the original INP was presented and C1 will signify the Settlement cycle of that retum
session; in which the transaction where returned. Here each return session can have n
settlementcyclesothecyclenumberwill rangefromC1to CN.
2.FinalresponsefilenamingconventionwillbeACH-CR-SBIN-SBINH2H-26082021-00001-
P1FC-RES.txt; here the P1 will signify the Presentation Session Identifier in which the

<!-- Page 3 -->

NPCI
NATIONALAIMENTSCORFORATIONONDIA
original INPwaspresented andFCwill signifythefinal settlement cycle inwhichthelast
transaction wasreturned fromdestination bank or it was deemedaccepted by NPClafter
the TAT period. Once the sponsor bank receives the FC response, which will signify that
this will be last, and final response file for the INP file presented by the sponsor bank.
3.At each settlement cycle, the system will generate the incremental response file.
4.After every cut off response file should be generated only for the records for which the
update is received from the destination bank during the time window for that session/
settlement.
New field introduction in response file at detail level:
In addition to the final response date, the system will include the cycle identifier in the Ledger
Folio Number field of the response file in bothTXT and XML.This field value will help bank to
reconcile the returned transaction in the response file in each cycle with respect to the settlement
file generated in that respective settlement cycle of the return session.
New field to be introduced in theTXTand XMLforcapturing the Inward Generation Dateis
as below:
1.TXT file - Placement of the Inward generation date in txt file will be at the header level
after the settlement date field, starting from 134 character till next 8 characters.
2.XML file-Placement of the Inward generation date inXMLfile willbe at theheaderlevel;
thetagpositionwillbeSttlmMtd/SttlmAcct/ld/Othr/ld
prefix with 0.As this field length as per specification is 3 characters.
Sample Files:
ACH-CR-SBIN-SBINH ACH-CR-HDFC-0804
2H-26082021-00001 2020-TPZ000758511-

<!-- Page 4 -->

NPCI
New tags.introdticed:
Inward tag:
<Sttiminf>
<SttlmAcct>
Aldy
<Othr?
<[d>2021-06-02</d>
<1Othr>
A/ld>
</SttlmAcct>
</Sttimlnf>
Response tage
<Dbtr>
Ady
<Prvtd?
Othr
<lssr>0C1</lsst>
<1othr>
</Prvtld>
A/lds
</Dbtr>
