# NACH | OC010 | FY 24-25 | Implementation of New Product and Transaction Code

Circular/reference number: NPCI/2024-25/NACH/010

<!-- Page 1 -->

NPCI
NATIONALPAYMENTS CORPORATION OF INDIA
NPCI/2024-25/NACH/010 March 26, 2025
To,
AllNACHMemberBanks
Subject: Implementation of New Product Type and Transaction Code for ACH/APB CR
Refer to our Circular No: NPCl/2024-25/NACH/004 dated November 16, 2024, regarding the
introduction of new transaction codes and product codes for processing DBT transactions. Tnere have
been certain proposais being discussed with governnent and regulators which require new transaction
codes to be introduced. In order to get the eco system prepared for this, we are communicating the
new codes that will be introduced shortly.
Product 1 : BDC
1.  APBs: Transaction code '83' with header code as '33"
2. ACH CR: Product type‘BDC'
Product 2 : LAU
1.  APBS: Tranisaction code ‘84' with header code as '33"
2.  ACH CR: Product type 'LAU'
Product 3 : COR
1. ACH CR: Product type 'COR'
The destination banks shall receive the inward transactions as per the transaction code (for APBs) and
product type (for ACH CR) as defined above. The inward file naming convention will be updated
The implementation of these transaction types will commence from April 1, 2025. The purpose of the
new codes shall be communicated once crystalized, before going live. All member banks are advised
to modify their systems accordingly to enable processing of transactions with the new transaction code
and product type as defined above.
This information may please be disseminated to ail concened parties for preparedness well
before March 31, 2025. For any queries, banks may use CRM or contact the NACH support team.
With wam regards,
SD/-
Giridhar G.M
Chief -Customer Succes
1001A,The Capital,BWing,10thFloor.
BandraKurlaComplex,Bandra(E),Mumbai 4ooo51.
T: +9122 40009100 F: +91 22 40009101
Togethen contact@npci.org.in www.npci.org.in
WeBuild CIN:U74990MH2008NPL189067

<!-- Page 2 -->

Annexure l:
Product Type - "BDc"
Applicable for ACH Credit only
Input file - Length: 262 to 264 at record level
Inward file - Length: 266 to 268 at record level
Transaction Code - "83" (APBS)
Header Code: 33
Input fle -- Length: 01 to 02 at record level
Inward file - Length: 01 to 02 at record level
Inward File Naming Convention:
APB Credit: APB-CR---TPZBDC-INW.txt
ACH Credit: ACH-CR---TPZBDC-INW.txt
Product Type - "LAu"
Applicable for ACH Credit only
input fle - Length: 262 to 264 at record level
Inward file - Length: 266 to 268 at record level
Transaction Code - "84" (APBS)
Header Code: 33
Input file - Length: 01 to 02 at record level
Inward file -- Length: 01 to 02 at record level
Inward File Naming Convention:
APB Credit: APB-CR--TPZLAU-INW.txt
ACH Credit: ACH-CR--TPZLAU-INW.txt
Product Type -"CoR"
Applicable for ACH Credit only
Input file - Length: 262 to 264 at record level
Inward file - Length:266 to 268 at record level
Inward File Naming Convention:
ACH Credit: ACH-CR---TPZCOR-INW.txt
For any further clarifications, please reach out via CRM or contact the NACH support team.
