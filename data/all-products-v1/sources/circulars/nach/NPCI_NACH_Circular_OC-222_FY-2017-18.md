# Circular No.222 - Change in the inward file naming format Revised

Circular/reference number: NPCI/2017-18/NACH/CircularNo.222

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2017-18/NACH/CircularNo.222 April 12, 2017
To
AllNACHmemberbanks
Change in the inward file naming format (Revised)
NAcCH system undergoes continues process improvement and as an outcome of the recent
system changes, the inward files received by the destination banks will have a change in
the file naming format.
The product wise new inward file naming format is given below,
ForNACHDebit (156format)
Existing inward file naming format:
NACH Debit - ECS-DR-<bank code>-<date>-<sub product><sequence No.>-INW.txt
New inward file naming format:
NACH Debit - ECS-DR-<bank code>-<date>-TMO<sequence No.>-INW.txt
Example:ECS-DR-ICIC-12042017-TMO00000123456-INW.txt
The letterTMO'will be prefixed in the sequence number
ForACHCredit
Existing inward filenaming format:
ACH Credit - ACH-CR-<bank code>-<date>-<sub product><sequence No.>-INW.txt
ACH Credit - ACH-CR-<bank code>-<date>-<sequence No.>-INW.txt
New inward file naming format:
ACH Credit - ACH-CR-<bank code>-<date>-TPZ<sequence No.>-INW.txt
Example:ACH-CR-ICIC-12042017-TPZ000123456-INW.txt
ACH Credit DBTL"ACH-CR-<bank code>"<date>-TPZ<DBL><sequenceNo.>-INW.txt
Example: ACH-CR-ICIC-12042017-TPZDBL123456-INW.txt
Example: ACH-CR-ICIC-12042017-TPZDBT123456-INW.txt
1001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051. T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Example:ACH-CR-ICIC-12042017-TPZECS123456-INW.txt
ACH CreditPEN-ACH-CR-<bank code>-<date>-TPZ<PEN><sequenceNo.>-INW.txt
Example: ACH-CR-ICIC-12042017-TPZPEN123456-INW.txt
ACH Credit SAL-ACH-CR-<bank code>-<date>-TPZ<SAL><sequence No.>-INW.txt
Example:ACH-CR-ICIC-12042017-TPZSAL123456-INW.txt
Example:ACH-CR-ICIC-12042017-TPZPFM123456-INW.txt
ACH Credit WAL -ACH-CR-<bank code>-<date>-TPZ<WAL><sequence No.>-INW.txt
Example:ACH-CR-ICIC-12042017-TPZWAL123456-INW.txt
ACH Credit PUN- ACH-CR-<bank code>-<date>-TPZ<PUN><sequence No.>-INW.txt
Example: ACH-CR-ICIC-12042017-TPZPUN123456-INW.txt
ACH Credit TReDS - ACH-CR-<bank code>-<date>-TPZ<TRE><sequence No.>-INW.txt
Example:ACH-CR-ICIC-12042017-TPZTRE123456-INW.txt
The letterTPz'will be prefixed in the sequence number
ForACHDebit
Existing inward file naming format:
ACH Debit-ACH-DR-<bank code>-<date>-<sequence No.>-INW.txt
ACH Debit RPN-ACH-DR-<bank code>-<date>-<RPN><sequence No.>-INW.txt
New inward file naming format:
ACH Debit -ACH-DR-<bank code>-<date>-TPZ<sequence No.>-INW.txt
Example: ACH-DR-ICIC-12042017-TPZ000123456-INW.txt
ACH Debit RPN - ACH-DR-<bank code>-<date>-TPZ<RPN><sequence No.>-INW.txt
Example: ACH-DR-ICIC-12042017-TPZRPN123456-INW.txt
The letterTPz'will beprefixed in the seguence number
ForAPBCredit
Existing inward file naming format:
APB Credit DBTL- APB-CR-<bank code>-<date>-<DBL><sequence No.>-INW.txt
New inward file naming format:
APB Credit DBTL- APB-CR-<bank code>-<date>-TPZ<DBL><sequence No.>-INW.txt
Example: APB-CR-ICIC-12042017-TPZDBL123456-INW.txt
APB Credit DBT - APB-CR-<bank code>-<date>-TPZ<APB><sequence No.>-INW.txt
Example: APB-CR-ICIC-12042017-TPZAPB123456-INW.txt
The letter TPz'will be prefixed in the sequence number
1001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051. T: +91 22 40009100 F:+91 22 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NewsessionvariantforACHCredit/ACHDebit/APBCredit
We will be coming out with a new NACH session variant. The naming convention of the
filefor new sessionvariant is providedbelow.
ACH Credit - ACH-CR-<bank code>-<date>-TPO<sub product><sequence No.>-INW.txt
ACH Debit - ACH-DR-<bank code>-<date>- TPO<sub product><sequence No.>-INW.txt
APBS credit - APB-CR-<bank code>-<date>-TPO<sub product><sequence No.>-INW.txt
Theletter‘TPo'will beprefixed in the sequence number
There will be a detailed communication sent during the time of implementation of this
new session variant. Member banks are advised to create provision for handling the
In case of any clarifications please write back to ach@npci.org.in
The new change of introducing prefix letters in inward files with“TMo"&“TPz"will be
effective from May 01, 2017.All the member banks are advised to take a note of this
change and do necessary changes in the respective internal system.
Withwarmregards,
(GiridharGM)
VP & Head-NACH & CTS Operations
1001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051. T: +9122 40009100 F: +91 22 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067
