# Circular no.003 - Disaster recovery setup and Active-Active setup

Circular/reference number: NPCI/2020-21/CTS/003

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2020-21/CTS/003 September20,2020
To
All theCTS memberbanks,
DisasterRecoverysetupandActive-Activesetup(DEM)
Pleaserefertovarious RBlcircularson disaster recovery set upforbanks and alsoour circular
No.NPCl/2019-20/CTS/38dated23rdJanuary,2020onthecaptionedsubject.AsperRBl
Guide linesbanksshall have PR &DRSetup in placeandbanks should conduct
disasterrecovery (DR) drills ona periodic basis.
CentralisedClearingHouse(CCH)andData ExchangeModule(DEM)architecture
supportsmultipleDEMsprocessingthetransactionsinactive,activemode.TheDEM
architectureprovidesfor
Connecting to CCH in active,activemodewith primary and disasterrecovery sites.
Utilizing the redundant MPLS link efficiently.
In light of above all the member banks are advised to ensure that disaster recovery siteis in
place and if the bank is using DEM the DR site should be in active mode. The Banks should
ensurethat
1. Dataisreplicatedbetweenthesitesandtheyarealwaysinsync(CHl&DEM)
Presentationvolume is logically segregated and routed through the respective DEMs
so that both the set ups are in ready state (DEM).
II. Eachset up iscapableof handlingthe entirevolumeof thebank independently(CHl
& DEM).
IV. Building capability to change therouting of transactions to any DEM or CHl.
It is mandatoryforall the banks to have DR set up and execute drills on periodic basis.All
banksusing DEM should havetheDRsetup inactive stateas detailed aboveso that thebank
will always be in ready sate for DR and the infrastructure providedfor DR set up can be
optimallyutilised.Banks mayrefertoDEM specifications and otherrelated circularsforfurther
information.
Member banks are advised to ensure compliance to DR requirements.The information herein
may please be disseminated to all the concerned.
WithWarmregards
GiridharGM
Chief - Offline Product Operations & Technology
