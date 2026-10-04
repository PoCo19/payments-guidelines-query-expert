# Circular No.215 - Return file generator tool

Circular/reference number: NPCI/2016-17/NACH/215

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2016-17/NACH/215 March 13, 2017
To
AllNACHMemberBanks
Returnfilegeneratortool-Offline
NPCIhas come out with return filegenerator tool for following products APBCredit, ACH
Credit & AcH Debit.Since the tool is offline, the same can be run in any standalone
computers which satisfies hardware and software requirement specified in the user
The return file generator tool and user manual can be downloaded from the NPCl website
through path below:
a) Products & Services → National Automated Clearing House → Return file generator
tool & user manual
b) NPCI NACH Landing page > FAQs → Return file generator tool & user manual
Member banks who are willing to use the tool has to take note of the following points:
If there is any change in the version, NPCI will provide the latest version to the
member banks. It is the responsibility of the banks to use the latest version of
the tool.
ii.
file in NACH system. Member banks have to upload the file & approve it in the
NACH system.
It is desirable that the banks should have their own application for processing the NACH
files and generate response files. The tool is intended only to be a stop gap arrangement
that too for banks with small volume. Banks should not create entire dependency on the
tool, NPcl should in no way be held responsible if the banks could not process the files
using this tool on any given day due to internal training issues or version control issues.
Banks are advised to take note and take steps to build their own systems for processing
the files. Please refer Annexure -I for points to be take care while processing the inwards.
1001A,The Capital, B Wing,10th Floor,Bandra Kurla Complex, Bandra (E),Mumbai 400 051.T:+91 22 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
The returngenerator tool & user manual will be made available in abovepath from March
14, 2017.
Foranyfurtherclarifications,pleasewritetoach@npci.org.in
Yours.faithfully,
GiridharGM
VP&Head-NACH&CTSOperations
1001A.The Capital,B Wing.10th Floor, Bandra Kurla Complex,Bandra (E),Mumbai 400051.T:+912240009100 F:+912240009101www.npci.org.in
CIN：U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-I
Points to be noted while processing inward files
APB inward files processing:
1. Beneficiary Name and account number is mandatory for all success transactions.
2. Partial return file is not entertained and tool will only give full return file for each
and every inward uploaded.
3. Tool will not support giving two return files for single inward uploaded.
4. Beneficiary name should not contain
a.Only spaces
b.First three characters cannot be consecutive
C. Name should be more than 3 characters.
5. Account number should not contain
a. Only spaces
b.Special characters.
ACH Credit inward files processinq:
1. Partial return file is not entertained and tool will only give full return file for each
and every inward uploaded.
2. Tool will not support giving two return files for single inward uploaded.
3. User defined return description is allowed only for transactions returned with
reasoncodeO4-“MiscellaneousOthers"
4. Return description should have below criteria
a. To not start with special characters, space and numbers
b. It should be alpha numeric.
Custom return description should not have text like"Others"and
“Miscellaneous"anywhere the in the given description.
5. Specifically for Digidhan inwards, banks should update the account number in
return file while processing it as a success transaction.
6. System should expect mandatorily to input the reason code in the first control
character whichishaving 15 lengths and second control filed will be the optional.
In case user wants to input the reason beyond 15 characters then user will make
use of second control field.
ACH Debit inward files processinq:
1. Partial return file is not entertained and tool will only give full return file for each
and every inward uploaded.
2. Tool will not support giving two return files for single inward uploaded.
1001A,The Capital, BWing.10th Floor,Bandra Kurla Complex,Bandra (El,Mumbai 400 051.T:+912240009100 F:+9122 40009101 www.npci.org.in
CIN：U74990MH2008NPL189067
