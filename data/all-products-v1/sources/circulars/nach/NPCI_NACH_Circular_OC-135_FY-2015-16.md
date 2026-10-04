# Circular No.135 - ECS Debit City Wise Inward Generation

Circular/reference number: NPCI/2015-16/NACH/135

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/NACH/135 November03,2015
To
All NACH Member banks
ECSDebit-CityWiseInwardGeneration
Madam/Dear Sir,
Reference to the Circular no 111 dated July 21, 2015 on the EcsDebit product migration to
NACH. We are ready with the functionality for generating the ECS center/region-wise inwards
to the destination Banks based on mapping of the city code available in MICR to the respective
RECS cities. Note that there is no change in the file format.
Please refer the Annexure I for region wise EcS naming convention. This facility will be
enabled to the member banks on a specific request. Once it is enabled the member banks will
receive city wise inward in a zipped format which will be pushed to the banks SFG from where
it can be downloaded and extracted for further processing. If the member Banks would like to
discontinue this facility then they can send a request to ach@npci.org.in.
Please refer to Annexure Il for the list of EcS centers and the corresponding city codes mapped
against the respective centers. In case of any other locations to be added, please write back to
ach@npci.org.in.
Member banks are advised to note that there is no change in the existing process of the
settlement entries posting as consolidated entry per bank.
In case of any further clarifications please write to ach@npci.org.in or nachsupport@npci.org.in
For National Payments Corporationof India
(GiridharGM)
VP&Head -NACH&CTSOperations
The Capital, raT/Phone:02240009100
. 1001 , , Unit No. 1001A, B Wing, /Fax:02240009101
1070 10th Floor, Plot No. C-70, 专-/ email:contact@npci.org.in
, f , G Block, BandraKurla Complex, aansc/Website:www.npci.org.in
-400051 Bandra (E), Mumbai 400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexurel
If the Bank has 4 Ecs inward files which contains transactions of 2 regions each namely Chennai
and Mumbai. The convertor will generate only 2 inward files one for Chennai region and other
of Mumbai region.
A separate file will be generated for the transactions with the city codes which are not
mapped to any regions.
Region wise inward file will contain maximum of 2o,o00 records. In case a region is
having more than 20000 transactions then multiple file will be generated for a same
region.
Header and Trailer of the inward file will be same as the original INW file, only the
total item and total amount will change according to the generated file.
Regionwise inward file name will be formed as below
ECS-(CR/DR)-<BankShortCode>-<BusinessDate>-<RegionName><SeqNo>-INW.txt
Example:
ECS-DR-HDFC-13102015-CHENNAI00001-INW.txt
ECS-DR-HDFC-13102015-CHENNAI00002-INW.txt
Others:
ECS-DR-HDFC-13102015-UNMAPPED00001-INW.txt
The converted files will be signed and a zip file will be created based on the region
withthefile name as
ECS-(CR/DR)-<BankShortCode>-<BusinessDate>-<RegionName>-INW.Zip
Example: ECS-DR-HDFC-13102015-CHENNAI-INW.Zip
All the region's zip files will be combined for a destination bank with the file name as
ECS-<CR/DR>-<Bank Code>-<Business Date>-INW.zip
Example:ECS-DR-HDFC-13102015-INW.zip
The Combined zip file will be sent to destination bank SFG mailbox.
A summary report which shows the set of input files processed and output files
generated with the Item Count per file and Amount per file will be sent to destination
Bank SFG mailbox.
-9,8
C-9, 8th Floor rq/Phone:02226573150
RBlPremises /Fax:02226571001
a-f ar,
Bandra-Kuria Complex 专-/ email:contact@npci.org.in
Bandra East
- 400 051 aasc/Website:www.npci.org.in
Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexurell
List of Centers
Sr.
No City Name Mode of
Clearing City code mapped
Trivandrum RECS 670,671,673,676,678,679,680,682,683,685,686,688,689,
690,691,695
Chandigarh RECS
140,160,141,142,147,148,143,151,152,145,144,146
301,302,303,304,305,306,307,311,312,313,314,321,322,
Jaipur RECS
323,324,325,326,327,328,331,332,333,334,335,341,342,3
43,344,345
Ahmedabad RECS 360,361,362,363,364,365,370,380,382,383,384,385,387,
388,389,390,391,392,393,394,395,396
Hyderabad RECS 500,501,502,503,504,505,506,507,508,509,515,516,517,
518,520,521,522,523,524,530,531,532,533,534,535
Bangalore RECS 560,562,561,587,591,590,583,585,586,580,581,582,584,
577,573,571,563,574,575,576,570,572
600,601,602,603,604,605,606,607,608,609,610,611,612,
Chennai RECS
613,614,620,621,622,623,624,625,626,627,628,629,630,6
31,632,635,636,637,638,639,641,642,643
Kolkata RECS 700,711,712,713,721,722,723,731,732,733,734,735,736,
737,741,742,743,744
Bhubaneshwar RECS 751,752,753,754,755,756,757,758,759,760,761,762,763,
764,765,766,767,768,769,770
10 Guwahati RECS
781,782,783,784,785,786,787,788
11 Delhi ECS 110
12 Jammu ECS 180
13 Kanpur ECS 208
14 Allahabad ECS 211
15 Varanasi ECS 221
16 Lucknow ECS 226
Dehradun ECS 248
The Capital, TqT / Phone:02240009100
1001 Unit No. 1001A, B Wing,
a/Fax:02240009101
10,-70, 10th Floor, Plot No. C-70,
专-/email:contact@npci.org.in
G Block, Bandra Kurla Complex, aa专/Website: www.npci.org.in
400051 Bandra (E), Mumbai 400051
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Sr.
No City Name Mode of
Clearing Citycodemapped
18 Gorakhpur ECS 273
19 Agra ECS 282
20 Mumbai ECS 400
21 Panjim ECS 403
22 Pune ECS 411
23 Solapur ECS 413
24 Kolhapur ECS 416
25 Nasik ECS 422
26 Aurangabad ECS 431
27 Nagpur ECS 440
28 Indore ECS 452
29 Bhopal ECS 462
30 Gwalior EcS 474
31 Jabalpur ECS 482
32 Raipur ECS 492
33 Patna ECS 800
34 Dhanbad ECS 826
35 Jamshedpur ECS 831
36 Ranchi EcS 834
Note: - In case of any other locations to be added, please write back to ach@npci.org.in.
The Capital, 7-TqT/Phone:02240009100
.1001, Unit No. 1001A, B Wing, a/Fax:02240009101
1070, 10th Floor, Plot No. C-70, -a/email:contact@npci.org.in
 , af a, GBlock,BandraKurlaComplex, aaw /Website: www.npci.org.in
Bandra (E), Mumbai 400051
CIN:U74990MH2008NPL189067
