# Circular No. 53 - Revised Reject Reason Code

Circular/reference number: NPCI/2014-15/NACH/CircularNo.53

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2014-15/NACH/CircularNo.53 June24,2014
To,
AllNACHMemberBanks
RevisedRejectReasonCodesfor.NACHSystem
Member banks at the time of uploading the input files in NACH system might begetting a few
rejected transactions due to various reasons.Based on the reject reasons the member banks,
wherever possible,take corrective action and reprocess the data. In order to provide better
claritywehaverevised/addedtherejectreasoncodes.
2.The revised list is provided in the Annexure and the same will also be available as part of
themastersreportundertheMiStab.
3.This will be implementedwitheffect fromJuly 10, 2014.Member banks are requested to
take note of the same.
4.Forany queries/furtherhelp,pleaseget in touch withus atnachsupport@npci.org.in
WithWarmRegards,
(GIRIDHARG.M)
VP&Head-CTS&NACHOperations
C-9,8thFloor m/Phone:02226573150
RBIPremises a/Fax:02226571001
Bandra-Kurla Complex -/email:contact@npci.org.in
Bandra East aaws/Website:www.npci.org.in
400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

AnnexureA
RejectCode ISO_RES RejectDescription
21 ITEM_MANDATENOT_ACTIVE_RES InvalidUMRNorinactivemandate
22 ITEM MANDATE NOT FOR DEBIT RES MandatenotvalidforDebittransaction
23 ITEM MANDATEDBTRACC_MISMATCHRES Mismatchinmandatedebtoraccountnumber
24 ITEM MANDATEDBTR BANKCODEMISMATCH RES Mismatch inmandatedebtorbank
25 ITEM MANDATECURR MISMATCH RES Mismatch inmandatecurrency
26 ITEM MANDATE AMT EXCEEDSMND_RES Amountexceedsmandatemaxamount
27 ITEMMANDATEAMTMISMATCH RES Mandateamountmismatch
28 ITEM MANDATE TX BEFORE START DATE RES Dateis before mandatestart date
29 ITEMMANDATETXAFTER ENDDATERES Dateisaftermandateenddate
68 ITEMISO BADAMT RES Invalidamount
69 ITEM ISO DUPLICATE RES Duplicate ReferenceNumber
70 ITEM ISO BADDATE RES Invaliddate
71 ITEM UNWOUND RES Itemunwound
72 ITEM CANCELLEDRES Itemcancelled
73 ITEM ISO SETTLEMENT_FAILED RES Settlementfailed
74 ITEM ISO INV FILE FMTRES Invalid fileformat
75 ITEM ISO CUST_REQ RES Transactionhasbeencancelledbyuser
76 ITEM APBSWRONGAADHAAR RES Invalid AadhaarFormat
77 ITEM ISO_BAD CURRENCY RES Invalid currency
78 ITEMISO BAD BANK ID_RES InvalidBankIdentifier
78 ITEMPRTRYBADBIC RES Invalid Bank identifier
79 ITEMISOCUTOFFRES File sentafterEODandbeforeSOD
80 ITEM_APBS_WRONG_IIN_RES Wrong IIN
81 ITEM PRTRY CUSTGENRSNRES Product is missing
82 ITEMMARKPENDING_RES Itemmarkedpending
83 ITEMPRTRY UNSUPPORTEDFLD RES Unsupportedfield
84 ITEM _ISOINVITEMFMTRES Invaliddata format
85 ITEM ISO FORBIDDEN RES Participant not mappedto the product
86 ITEM BAD OP CODE RES Invalidtransactioncode
87 ITEM PRTRY INV ORGNL STS ACTION REQ RES Missing originaltransaction
88 ITEM PRTRY INV ORGNL STS NO ACTION REQ_RES Invalid originaltransaction
89 ITEM PRTRY INV ORGNL DTMISMATCHRES OriginaldateMismatch
90 ITEM PRTRY INV ORGNLAMTMISMATCH RES Amountdoesnotmatchwithoriginal
91 ITEM PRTRY INV ORGNL INFO MISMATCH RES Informationdoesnot match with original
92 ITEM PRTRY CORE RES Core error
93 ITEM INV SVCLVLCD RES Wrong clearing housename in SFG
94 ITEM ISO_ZEROAMT_RES Amount isZero
95 ITEM APBS INACTIVEAADHAAR RES InactiveAadhaar
96 ITEM APBS MISSING JIN RES Aadhaarmappingdoesnot exist/Aadhaarnumbernotmappedto lIN
96 ITEM_EBTMISSINGACCNO Aadhaarmappingdoesnot exist/Aadhaarnumbernotmappedto lIN
96 ITEM_APBSMISSING_UIDMAPPING Aadhaarmappingdoesnot exist/Aadhaarnumbernotmappedto llN
97 BATCH BAD CORPORATERES Badbatchcorporateusernumber/name
98 ITEM_BADCORPORATERES Bad itemcorporateusernumber/name
99 ITEM_TOOMANY MARKPENDINGRES Toomanymarkpendingreturns
