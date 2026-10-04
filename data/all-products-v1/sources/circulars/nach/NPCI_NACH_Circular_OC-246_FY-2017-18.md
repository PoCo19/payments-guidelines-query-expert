# Circular No.246 Frequency tag and Mandate Start date validation in MMS

Circular/reference number: NPCI/2017-18/NACH/CircularNo.246

<!-- Page 1 -->

NPCD
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2017-18/NACH/CircularNo.246 September22,2017
To
AlltheNACHmemberbanks
Frequencytag&MandatestartdatevalidationinMMs
Refer to circular no: NPCI/2015-16/NACH/Circular No.123 dated August 26, 2015, on
implementation ofvalidation of start date & frequencytype in MMS presentation.Thefollowing
willbethechangesimplementedinthesystem
Start Date
“Start date”field willbemademandatoryforallmandatevariants.
ApplicableforbothGUI&XMLinitiation.
If start date is not captured the mandate will be rejected during initiation itself.
Frequencytype
Sequencetypeformandates withperiodicitylikedaily/bi-monthly/monthly/quarterly
/half-yearly/yearly/ Asand whenpresented shouldbecaptured as“RCUR"
Example:
<SeqTp>RCUR</SeqTp>
<Frqcy>MNTH</Frqcy>
When the sequence type is “OoFF". Frequency tag should not be captured.
Example:
<SeqTp>OOFF</SeqTp>
ApplicableformandateinitiationthroughXMLformatonly.
If not captured as per above validation, the mandate will be rejected during initiation.
TheabovechangeswillbeeffectfromOctober16,2017.
All thememberbanks are advised to take noteof thesameand makenecessarychanges in their
systemaccordingly. In-case of any clarification, please write to ach@npci.org.in
With warm regards,
(GiridharGM)
VP-NACH&CTSOperations
