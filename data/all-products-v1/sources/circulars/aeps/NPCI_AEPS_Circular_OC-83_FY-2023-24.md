# AePS | OC 83| FY 23 24 | Business Correspondent (BC) Agent/CSP details in AePS online transactions

Circular/reference number: NPCI/2022-23/AePS/083
Date: 23rd June, 2023

<!-- Page 1 -->

Circular No. 83 - NPCI/2022-23/AePS/083  
 
 
 
    23rd June, 2023
 
 
To, 
All Member Banks of AePS (Aadhaar Enabled Payment System)  
Dear Sir/Madam, 
Subject: Business Correspondent (BC) Agent/CSP details in AePS online transactions 
We refer to the Circular no. 64 – NPCI/2021-22/AePS/005 dated 27th October, 2021 on 
capturing correct card accepter identification code and card acceptor name. The member 
banks were advised to capture the unique terminal id which is allocated to individual BC 
Agent/CSP, including their correct name, address, and location details in DE#43 in earlier ISO 
messaging based technical specifications. 
With the migration of all AePS member banks to common code-based XML messaging 
interface, and in reference to the above circular, members are advised to pass the below given 
mandatory BC Agent/CSP related details in AePS online transaction:  
 
Members are advised to pass the aforementioned tag values in all AePS transactions including 
for ONUS and OFFUS (financial & non-financial) AePS transactions.  
List of APIs is given below: 
1) ReqPay ; 2) ReqBalEnq ; 3) ReqBioAuth ; 4) Reqchktxn & 5) ReqSigFetch 
Importantly, members to note that the location details passed in online transactions is of the 
BC Agent/CSPs outlet from where the transaction is initiated and not the Agent/CSP’s KYC 
location details. 
Members are requested to disseminate the information contained herein with the concerned 
department / officials for implementation.  
Sr No Tag Name 
Length 
Value 
Remarks  
1 
cardAccpTrId 
8 
register  
Static Value  
2 
cardAccIdCode 
15 
First 3 digits bank code + Unique 
Terminal ID 
Unique Terminal 
ID assigned to 
the agent / 
Terminal  
3 
LOCATION 
40 
Char 01-23 : BC Name & Address* 
Char 24-36 : City Name 
Char 37-38 : State 
Char 39-40 : Country Code (IN) 
*In case of BHIM 
Aadhaar Pay 
transactions – 
Merchant Name 
& Address 
4 
Type 
4 
INET  
Static Value  
5 
PosEntryCode 
3 
019  
Static Value  
6 
posServCdnCode 
2 
05/010 
Static Value  
7 
PinCode 
6 
Actual Pincode 
Pincode of BC 
agent outlet

<!-- Page 2 -->

Members are advised to pass the correct BC Agent/CSP details as mentioned herein and 
confirm adherence by 31st July, 2023 via email to the following NPCI officials – 
Name 
Email ID 
Contact Number 
Mudit Gadiya 
mudit.gadiya@npci.org.in  
8871043032 
Rishabh Kasera  
Rishabh.kasera@npci.org.in 
7000492688 
 
For more details or any queries, members may reach out to the above-mentioned NPCI 
officials or their Bank’s Relationship Managers (RMs). 
 
Your sincerely,  
SD/- 
Kunal Kalawatia  
Chief of Products
