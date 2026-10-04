# Circular No. 65 - Clarification on MMS File Format

Circular/reference number: NPCI/2014-15/NACH/Circular
Date: 1st December, 2014

<!-- Page 1 -->

 
Registered Office: C-9, 8th Floor, Reserve Bank of India Premises,  
Bandra-Kurla Complex, Bandra East, Mumbai 400 05 
NPCI/2014-15/NACH/Circular 65               
 
 
 
1st December, 2014 
 
To, 
All NACH Debit Participating Banks 
 
Clarification on the MMS file format  
Madam/Dear Sir, 
With reference to the MMS file formats as shared with the banks in the ‘Bank 
Specification Document (BSD), we would like to provide further clarification to banks on 
the handling of ‘Occurrence’ tag in the MMS XML file. 
2. NPCI has taken various initiatives to educate the member banks on standardising the  
understanding of mandate processing in order to minimize the mandate rejection rate. In 
this effort a Mandate processing guideline (Circular 58) has been issued on 5th November 
2014.  
3. This circular has been issued to provide clarification on the syntax and nomenclature of 
the xml tag to be used in the ‘pain’ file formats for creation/amendment of the mandate. 
The details of the tags are provided in the annexure attached. Sponsor and destination 
banks are expected to adhere to the standard syntax as provided in the annexure for 
representing the respective frequencies and period in the mandate.  
3. All ACH Debit participating banks are requested to make note of the same and ensure 
compliance. 
With Warm Regards, 
 
(Vipin Surelia) 
SVP– Product Development

<!-- Page 2 -->

 
Registered Office: C-9, 8th Floor, Reserve Bank of India Premises,  
Bandra-Kurla Complex, Bandra East, Mumbai 400 05 
Annexure 
List of frequency available on NACH and its description: 
Sr. 
no. 
Frequency 
Code 
Description 
Expected occurrence Tag in xml pain file 
1 
As and When 
presented 
ADHO 
No restriction on the 
number of debits. Will 
allow multiple debits 
during a 
day/week/month/any 
period 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>ADHO</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>  
2 
Intra day 
INDA 
Multiple successful 
debits within a 
business day 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>INDA</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>  
3 
Daily 
DAIL 
One successful debit in 
a business day 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>DAIL</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>  
4 
Weekly 
WEEK 
One successful debit in 
7 days 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>WEEK</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>

<!-- Page 3 -->

 
Registered Office: C-9, 8th Floor, Reserve Bank of India Premises,  
Bandra-Kurla Complex, Bandra East, Mumbai 400 05 
Sr. 
no. 
Frequency 
Code 
Description 
Expected occurrence Tag in xml pain file 
5 
Monthly 
MNTH 
One successful debit in 
a calendar month 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>MNTH</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>  
6 
Bi-Monthly 
BIMN 
Two successful debits 
in a calendar month 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>BIMN</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>  
7 
Quarterly 
QURT 
One successful debit in 
three calendar months 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>QURT</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>  
8 
Semi Annually 
MIAN 
One successful debit in 
six months 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>MIAN</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>  
9 
Yearly 
YEAR 
One successful debit in 
12 months 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>YEAR</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>

<!-- Page 4 -->

 
Registered Office: C-9, 8th Floor, Reserve Bank of India Premises,  
Bandra-Kurla Complex, Bandra East, Mumbai 400 05 
Sr. 
no. 
Frequency 
Code 
Description 
Expected occurrence Tag in xml pain file 
10 
One Off 
Payment 
OOFF 
One successful debit in 
the lifecyle of the 
mandate 
<Ocrncs>  
    <SeqTp>OOFF</SeqTp>  
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>

<!-- Page 5 -->

 
Registered Office: C-9, 8th Floor, Reserve Bank of India Premises,  
Bandra-Kurla Complex, Bandra East, Mumbai 400 05 
Options in defining the validity period of the mandate: 
For all the below scenario Frequency of mandate is considered as ‘Monthly’ 
 
Sr. 
no. 
Validity Period 
Expected occurrence Tag in xml pain file 
1 
Period with Time Zone 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>MNTH</Frqcy> 
    <FrstColltnDt>2012-01-17+05:30</FrstColltnDt>  
     <FnlColltnDt>2012-05-17+05:30</FnlColltnDt>  
</Ocrncs>  
2 
Period without  
Time Zone 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>MNTH</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
     <FnlColltnDt>2012-05-17</FnlColltnDt>  
</Ocrncs>  
3 
Period starts from First 
Collection Date to 
‘Until Cancelled’. 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>MNTH</Frqcy> 
    <FrstColltnDt>2012-01-17</FrstColltnDt>  
</Ocrncs>  
4 
Period is  
‘Until Cancelled’. 
<Ocrncs>  
    <SeqTp>RCUR</SeqTp>  
    <Frqcy>MNTH</Frqcy> 
 </Ocrncs>
