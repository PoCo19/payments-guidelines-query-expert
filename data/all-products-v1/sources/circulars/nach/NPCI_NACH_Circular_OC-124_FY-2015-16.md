# Circular No. 124 - Change in OAC INP file for account number field

Circular/reference number: NPCI/2015-16/NACH/CircularNo.124

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/NACH/CircularNo.124 August 27, 2015
To
AllNACHMemberBanks
ChangeinOACINPfileforaccountnumberfield
With referencetoourcircular No.:NPCI/2015-16/NACH/CircularNo107dated July01,2015
on conversion of old account numbers to new account numbers, please note that we have
added validation to the old account number filed to accept only the account numbers that
are equal to or less than 9 digits.The relevant technical specification is given below
Specification
In the record level of the INP file, between fields from 28 to 47 (old account number filed)
only9digits accountnumbercanbeupdated.
Sr. Field Length Field Mandatoryl Field Sample
No Description Type Optional Description Data Remarks
Maximum
Old Account ALP Customer Bank of 9
Number 20 NUM Mandatory account SB 1234 characters
number
are allowed
INp files having more than 9 digits in old account number field will be rejected with reason
"Old account number should not be more than 9 digits".
Memberbanks are requested to takea note of the same.
For National Payments Corporation of India
Giridhar GM
(VP& HeadOperations-CTSand NACH)
The Capital, mqT/Phone:02240009100
1001 Unit No. 1001A, B Wing. a/Fax:02240009101
1070 10th Floor,Plot No.C-70, -a/email:contact@npci.org.in
GBlock,BandraKurlaComplex, aa/Website:www.npci.org.in
400051 Bandra (E),Mumbai400051
CIN:U74990MH2008NPL189067
