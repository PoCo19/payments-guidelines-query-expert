# Circular no. 003 - API for getting account number linked to an Aadhaar number

Circular/reference number: OC-003

<!-- Page 1 -->

NipCl/2a21-22/NACH/Circuar No:3 dune 18, 2021
To
NACH Member Banks
Introductiotiofinew Apl service to get the.Accounit Numbe'r litked to.Aadhaar
Refer. 'to our circular NPCl/2019-20/NAGH/Circular No: 009. dated July 10. 2019 an
introduction of various APl services related ta.customer account.status and Aadhaar linking:
In' addition to:that; various Central and State Govemment departments have requested NpCi
to host an online (Apl based) facility to check:the'account number.to. which :the-Aadhaar of
the.bereflciary.js-linked.
Initialy 'the: facility witl be provided to Governiment departments only.. Only the last 4. digits'af
ithe account number will be :made. available'in response. For intemal use.to verify the'detaits
provided by:any'cifizen the departments can integrate: Apl directiy with NPcl and consume
the respanse, The.departments desiraus.of offering the.senvice to the.citizens shoufd ensure.
fhat the citizein js :duly.authenticated either: through Aadhaar & OTP.mechanismor any other
mechanism as'per the policies. of the :Government. It is the responsibilityrot the:entity usirng
this service to authenticate the .citizen before praviding the: account details: fetched through
Ap! request.
Scenaria wise input and autput for this.service is provided in Annexure I and the detailed
technical'specification. dacument'is. provided in Annexure. 2.. The below. table provides -the
input and respon'se.details forthe APl request:
APl sevice InnutReguest Response
Aadhaar Number
Accaunt Number
Bestination bank - Aadhaar Linkage Status
Get Linkage Status code. Account status
of Account Nuniber Customer.Cansent Subsidy. Account Flag
1:
for given Aadhaar (optional in case Account:Number.(only. last
Number input raised by 4 digits)
Government far  Accaunt:type
internal :use)

<!-- Page 2 -->

NAFIONAE-MTATENTRCORRORAFRNTODA
The APis as per the circular referred above and he new APl for praviding the details of
account tinked. to Aadhaar number are criticalifor DBT schemes.of Government .of India and
other State Gavernments: All the member banks are advised to take: immediate. measures.to
implement the APls as per :the specifications.and. get on-boarded at the eartiest.
The dietaits of switching fee and interchange wit be communicated.separately.
With warm regards,
SiridharG.dt
(Chief -: Offline.product operations:& run technolagy)

<!-- Page 3 -->

Angexure:l
cenarolnput Exjectationromibanks
iif.thereis.an account.linkedto.Aadhaar
numberreceived, thenithis .fliag has to.be
"y', Else it should be"N'.
. If Aadhaar inking statusis"y'i, then
the status of the. accountto be' captured.
as'per thie.master cata provided else the
remaining fields shouid be blank.
i. Aadhaar Ti. This.can.be "y' or "N 'ry! can.be
". Verhiceff
algorithm far linking status for receiving subsidy through'Aadhaar.
Aadhaar. i..Account
stafus flag. based. "N" can' be provided ifAadhaar
Aadhaar number il, Subsidy. riking is.ayail able but-not:a primary
number . .Routing.wil accouint far.receiving subsidy.
i. Bank bebasedon account'tag iv. If point'j" is "yi. then bank.should
the.bank code iy. :Account
nmber. .provide iast:4.digit:of the.account
provided from. riumber.
source v. Accaunt y. Account type.shauid.be only as.per the
lype
master data prouded. If goint ti"is:"y"
then'account iype should be:only.s..
PMJDY, BsBD, Loan.aecount: Ir any
other.account typejs provided-by bank.
tae 'same shouid be. relected.ff.account
enabied.for Feceivlng subsidy through
Aadhaar basedis "N"then the.account
type can be any from the master'data.
f, If the.account'provided is Jinked to
Aadhaar numberreceived, then thisfag
has:to.be y. .Ese:it should be "Nn
li. The'status.of account:should.be':
'provided.by the barik. This will be a
mandataryfield for'bank if the aceount
numberis.provided.
i. Aadhaar i'This.can be"" or'N", "can he
I. Verhoeff. given:if the accotnt.is primary.account
10 w!06e. inking statts.
Aadhaar it. Account for receiving'subsidy.thrpughAadhaar
number' .Aadhaar status flag based."N":can be providedif Aadhear
2. i. Bank number i. Routing.will I: Subsidy Iinking is available bu nat'a.primiary
cade: account flag account far teceivng sibsidy.
be.based on. iv; Agcount jv..If point "" Js Y", then bank shoutd
Account the bank.code rumber: provide last 4 digit af the accaunt
number 'Provided from w. Account. number:
'source v. Accounttypg should be only as'per the
type
master.data provided, tf point "t" is."y.
then account bype:should.be-only SB,
PM,DY, BSBD, Loan'account.If any.
other'account:type ts provided: by'bank,
the same should'be rejected,.f.account
énabled for receiving subsidy through
Aadhaar basedis"Nthen the account
type tan be.any from the. master data.
