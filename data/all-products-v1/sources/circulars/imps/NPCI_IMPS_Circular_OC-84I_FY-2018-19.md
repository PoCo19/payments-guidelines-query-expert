# IMPS I OC 84 I FY 18-19 I Alignment of Member bank switches towards IMPS Online Technical Specification

Circular/reference number: OC-84I
Date: 24th April, 2018

<!-- Page 1 -->

 
 
  
 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
 
 
NPCI/IMPS/OC No. 84/2018-19 
 
 
 
 
 
 
                     24th April, 2018 
 
To, 
 
All Members of IMPS 
 
Madam/ Dear Sir, 
Sub: Alignment of member bank switches towards IMPS Online Technical Specification 
IMPS switching system (IMPS Bharat Switch) supports P2P, P2A, P2U and FIR based transactions. IMPS Online 
Technical Specifications mandates certain compliances on the online messages exchanged between member 
switch and IMPS Online switching platform. Currently in IMPS Online Switching System, it was observed that 
many of the member banks are not fully compliant with IMPS Online Technical Specifications. E.g. though 
some of the fields are mentioned as mandatory fields in the response message from member switch OR to be 
echoed back with value as received in the request message OR to be populated with allowed values specified 
for the field, it was observed that some of the member switches are not strictly complying as a result of which 
IMPS switch at NPCI is made to ignore or accommodate such non-compliances. Such scenarios lead to 
mismatch in data elements handling across the ecosystem with cascading effect onto other banks and 
subsequent clearing & settlement and dispute processing. 
At a high level, this mandate addresses the following key aspects: 
1. Request / Response received from member bank switch must contain all the mandatory fields, conditional data 
and valid values in fields as per IMPS Online Switching Specifications. 
2. Member bank switch must not reject transactions basis the absence of optional fields in the message received 
from NPCI IMPS Switch. 
3. Response from member bank switch must echo back certain fields (as per IMPS Online Switching 
Specifications) with values as sent by IMPS Switch in the request. 
In order to establish compliance for online messages with IMPS Online Switching Specifications, NPCI has 
initiated IMPS specification alignment activity with member banks. 
It is to be noted that NPCI is NOT introducing any new compliance rules but ONLY enforcing the compliance 
rules as per the already existing IMPS specifications in order to align the member bank online switching 
platform. 
NOTE: All acquirer compliances will be declined with Invalid Transaction (RC-12). Transaction will not be 
declined in case of Issuer compliance. 
Please refer the matrix as per Annexure A attached herewith for the IMPS online mandates to be implemented 
by 16th August 2018. Member banks must share the mandate document with their ASPs/Product vendors for 
their perusal and take necessary action in order to make their switch compliant with the mandate.

<!-- Page 2 -->

1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
Introduction of Bharat Online Switching Simulator (BOSS): 
In order to simplify the certification process, NPCI will be providing banks with Bharat Online Switching 
Simulator which is a Windows based standalone simulator. The member banks will be able to install the same 
at their own premises (in case of banks served by ASPs, it will be installed by ASPs in their premises) and 
connect with their switch. Member bank (in liaison with their vendor/ASP) has to perform the online 
transaction by connecting their switch to simulator for the applicable test scripts and submit the logs 
(generated from simulator) to NPCI. NPCI certification team will verify the logs and confirm the compliance to 
Member Bank.  
Activity 
Timeline 
NPCI Provides BOSS simulator installable to member bank (or their ASP 
in case of hosted member banks) 
15th May 2018 
Date for submitting the simulator logs to NPCI 
Start : 1st June 2018 
End : 31st July 2018 
Please make a note of the above and disseminate the instructions contained herein to the officials concerned 
in order to verify the compliance of your online switching application and take necessary action. 
For any queries or clarification, please contact: 
Name 
e-mail ID
Sarthak Choudhary 
sarthak.choudhary@npci.org.in 
Bharat Nanawati 
bharat.nanawati@npci.in 
Yours faithfully, 
Ram Sundaresan 
SVP & Head – Operations 
Encl:   1. Annexure A – IMPS_Mandate_2018_Version_1.0.pdf 
SD/-
