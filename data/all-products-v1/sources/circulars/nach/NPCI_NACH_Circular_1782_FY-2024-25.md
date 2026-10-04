# NACH | 004 | FY 24-25 | Introduction of new transaction code and product code for processing DBT transactions of government departments

Circular/reference number: NPCI/2024-25/NACH/004

<!-- Page 1 -->

                                                                                                      
 
1 
Registered Office - 1001A, B wing 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), 
Mumbai - 400 051 
 
NPCI/2024-25/NACH/004 
 
 
 
 
 
    November 16, 2024 
 
To, 
All NACH Member banks. 
Introduction of new transaction code and product code for processing DBT transactions 
of government departments 
Reference may be taken from our Circular No: NPCI/2014-15/NACH Circular No. 83 dated 
January 20, 2015 on bank readiness to follow new type of transactions.  In this regard it has been 
decided to implement a new product type   for APB as well as ACH as defined below: 
1. APBS: Transaction code ‘95’ with header code as ‘33’ 
2. ACH: Product type ‘DBG’ 
It may please be noted that State and Central Government departments shall be participating in 
NACH with RBI as sponsor bank for presenting the transaction.  The departments shall be 
connecting directly to NACH for presenting the transactions.  The destination banks shall receive 
the inward transactions as per the transaction code (in case of APB) and Product type )in case of 
ACH) as defined above. There will be change in the inward file naming accordingly, the technical 
specifications for the new product code are provided in Annexure I.  
A sperate session shall be operated for facilitating these transactions, the details of the new 
session shall be communicated separately before going live.  
All the member banks are advised to modify their systems to enable processing the transaction 
with new transaction code and product type as defined below.  The sessions shall be likely to be 
commenced from November 23, 2024. Banks may make necessary arrangements accordingly to 
facilitate processing of inward transactions. 
The information herein may please be disseminated to all the concerned for preparedness well 
before November 23, 2024.  CRM may be used to raise queries, if any. 
 
With warm regards, 
 
 
SD 
Giridhar G.M 
Chief – Customer Success

<!-- Page 2 -->

                                                                                                      
 
2 
Registered Office - 1001A, B wing 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), 
Mumbai - 400 051 
 
Annexure I: 
• 
Product type – “95” 
o Applicable for APB Credit only 
o Input file – Length 01 to 02 at record level. 
o Inward file – Length 01 to 02 at record level. 
o Session Name: APB CR Present 2. 
 
• 
Product type – “DBG” 
o Applicable for account-based credit only. 
o Input file – Length 262 to 264 at record level. 
o Inward file – Length 266 to 268 at record level. 
o Session Name: ACH CR Present 2 
 
Inward file naming convention for Inward: 
• 
APB Credit: APB-CR-<bank code>-<date>-TPZDBG<sequence no>-INW.txt 
• 
ACH Credit: ACH-CR-<bank code>-<date>-TPZDBG<sequence no>-INW.txt
