# Circular No. 001 - Validity of mandate date

Circular/reference number: NPCI/2023-24/NACH/001

<!-- Page 1 -->

NACH
NATIONALAUTOMATEDCLEARINGHOUSE
NPCI/2023-24/NACH/001 May 04, 2023
To,
All NACH Member banks,
Validity of mandate
In order to further improve the process discipline in mandate processing through NACH, it has
been decided to limit the validity of the mandate to a period of 120 working days from the date
of the mandate. The member banks and other stakeholders should ensure that they present
the mandates within 120 working days from the date of the mandate.
Validation of the mandate date provided in the mandate data shall be implemented and stale
mandates that are more than 120 days shall be rejected.
Tag:
A new tag has been introduced; the date of the mandate shall be provided in this tag at the
time of creating or amending mandate.
This date can be captured in the below tags for the pain.009 (create / re-initiate) and pain.010
(Amend) file formats.
<Ocrncs>
<SeqTp> </SeqTp>
<Drtn><FrDt>dateOfMandate</FrDt></Drtn>
The following are the scenarios with appropriate rejection reasons:
1. At the time of creation/amendment/re-initiation of a mandate MMS system will validate
the range between the business date of a mandate reguest and date of the mandate
if the gap is more than 120 days then such mandates shall be rejected by the system
with the reason:
Creation/Amendment of Mandate: "Range between mandate date and current
business date exceeds limit days defined"
Representation of Mandate:“"Mandate representation is not allowed! max allowed
limitexceeded".
Note: only working days to be considered for calculation.
current business date. If the date is beyond the current business date, then such

<!-- Page 2 -->

NACH
NATIONAL AUTOMATED CLEARING HOUSE
mandate shall be rejected by the system with the reason ""date of mandate should
be before current business date."
3. Apart from the above, if for any reason, the entity presenting a mandate (whose date
is beyond 120 days) with incorrect mandate date, the processing bank shall reject such
mandate with the reason -"Instrument out dated, stale -Mo96".
Representation of mandate:
It has been decided to restrict the representation of mandates that were rejected for various
reasons. The number of times a mandate can be represented will be linked to the reason for
which it got rejected. Mandates that are presented beyond permissible number of times shall
be rejected with reason “Mandate Representation is not allowed! max allowed limit
provided in Annexure I1.
For the purpose of identifying a mandate uniquely the following fields will be considered:
1.  Date of Mandate
2. Debtor account number
3. Debtor bank
4. Utility code
5. Amount
disseminate the information herein to all the concerned.
With warm regards,
Giridhar G.M
(Chief Offline Products Operations & Technology

<!-- Page 3 -->

NACH
NATIONALAUTOMATED CLEARING HOUSE
Annexure I:
Sr. no. Return reason Code No of
representations
Account is closed M037 Zero
Account holder name mismatch with CBS M057 Zero
Alterations in mandate require drawer's authentication M007 Zero
Amount in words and figures differ M024 Zero
Amount of EMl more than limit allowed for the account M034 Zero
Appropriate NACH Mandate not uploaded M094 Zero
Drawer's authority to operate a/c not received M006 Zero
Mandate is duplicate; already accepted earlier M021 Zero
Invalid frequency of mandate M060 Zero
10 Mandate is stale1 M096 Zero
Mandate not in standard format 600W Zero
12 Mandate not registered due to NRE a/c M051 Zero
13 Mandate registration not allowed for PPF account M054 Zero
14 No such account present with bank M038 Zero
15 Account number is not present in CBS M036 Zero
16 Payment from account stopped by attachment order M011 Zero
17 Payment for account stopped by court order M012 Zero
18 Thumb Impression in CBs but customer sign in mandate M067 Zero
19 Withdrawal stopped owing to death of account holder M013 Zero
20 Withdrawal stopped owing to insolvency of account M015 Zero
21 Withdrawal stopped owing to lunacy of account holder M014 Zero
22 Account is frozen or blocked M026 Two
23 Account is inoperative M055 Two
24 Company stamp not present or wrong M008 Two
25 Data mismatch with image - account number M074 Two
Data mismatch with image - account type M075 Two
Data mismatch with image - amount M080 Two
28 Data mismatch with image - corporate name mismatch M035 Two
29 Data mismatch with image - debit type M079 Two
30 Data mismatch with image - debtor bank name M084 Two
31 Data mismatch with image - end date M082 Two
32 Data mismatch with image - frequency M077 Two
33 Data mismatch with image - more than one field M085 Two
34 Data mismatch with image - payer name M083 Two
35 Data mismatch with image - period M078 Two
36 Data mismatch with image - start date M981 Two
1 New return reason added

<!-- Page 4 -->

NACH
NATIONALAUTOMATEDCLEARINGHOUSE
Sr. no. Return reason Code No of
representations
Drawer's signature illegible in mandate form M050 Two
38 Drawer's signature not updated in Bank CBS M049 Two
39 Joint signature required M066 Two
40 Mandate not registered due to minor account M052 Two
41 Mandate registration not allowed for CC account M030 Two
42 Presented under incorrect mandate category M025 Two
43 Refer to the branch as KYC not completed M023 Two
44 Rejected as per customer confirmation M032 Two
