# Circular no. 063 Annexure I-SOP for Bank Administration ADFS and Work Group configuration - All

Circular/reference number: OC-063

<!-- Page 1 -->

 
Confidential   
 
 
 
1  
 
 
 
 
 
 
 
 
 
SOP for Bank ADFS & Work Group Configuration

<!-- Page 2 -->

 
Confidential   
 
 
 
2  
Contents 
Introduction: .......................................................................................................................... 3 
Chapter I – Configuring CCH UI access using active directory:..................................... 3 
Step-1: Configuration changes at active directory: ............................................................ 3 
Step-2: Configuring relying party endpoint at ADFS: ......................................................... 3 
Step-3: Configuring administrator User: ............................................................................. 5 
Step-4: Configuring operations users for CCH:.................................................................. 6 
Step-5: Configuration changes at CCH: ............................................................................. 6 
Step-6: Configuring user groups at CCH:........................................................................... 7 
Step-7: Mapping tasks to user groups at CCH:.................................................................. 7 
Step-8: Verifying bank operator login: ................................................................................ 7 
Chapter II – Work Group user & roles creation: ............................................................... 9 
Step-1: Configuring administrator user:.............................................................................. 9 
Step-2: Configuring operations users in Work Group: ....................................................... 9 
Step-3:  Configuration changes at CCH : ......................................................................... 10 
Step-6: Configuring user groups at CCH:......................................................................... 10 
Step-7: Mapping tasks to user groups at CCH:................................................................ 10 
Step-8: Verifying bank operator login: .............................................................................. 10 
Chapter III – Common Steps: ............................................................................................ 10 
Steps to configure user groups at CCH............................................................................ 10 
Steps to map tasks to user groups: .................................................................................. 13 
Steps to verify bank operator Login:................................................................................. 15

<!-- Page 3 -->

 
Confidential   
 
 
 
3  
Introduction: 
NPCI has hosted a centralized UI for banks migrating from Clearing House Interface (CHI) 
to Data Exchange Module (DEM). The banks can access this UI to monitor processing at 
CH and to retrieve reports.  
In order to access the centralized UI, banks need to carry user management locally. The 
user management can be done with either of the options: 
1. In bank’s corporate Active Directory (AD) with Active Directory Federation Services 
(ADFS)  
2. By creating work group for DEM. This option can be used if bank does not have 
corporate AD or does not have access to corporate AD from DEM network or cannot 
provide ADFS due to any other reason. 
Note: The ADFS can be configured on the AD server as additional role or can be installed 
as a service on a server which can access corporate AD.  
For configuration details of ADFS with Active Directory, please refer Chapter-1 
For configuration details of work group, please refer Chapter-2 
Chapter I – Configuring CCH UI access using active directory: 
Banks need to execute following steps to configure user authentication and management 
using active directory and ADFS 
 
Step-1: Configuration changes at active directory: 
Banks are required to configure following user attributes in the Active Directory: 
1. Routing number: This will be used to store the routing number of the bank for which 
the user can see the data. The routing number should be nine digit MICR code of 
the bank. 
2. User role: This attribute is used to identify administrators for the bank. 
a. User role: WEBCHI_ADMIN. 
Note: The names of the user attributes are required to be exactly same as above. 
Please refer section “Steps to configure user attributes in Active Directory” for details 
of how to configure the user attributes 
 
Step-2: Configuring relying party endpoint at ADFS: 
 
Pre-requisites:  
Bank is required to have ADFS role installed and configured. The ADFS role can be 
configured on the active directory itself or can be configured as a service on a different

<!-- Page 4 -->

 
Confidential   
 
 
 
4  
machine (e.g. on the DEM machine). However, it is required to have only one ADFS 
service active in one VLAN. 
Follow below steps to configure relying party endpoint: 
1. Navigate to ADFS Management. 
2. Select relying party trusts. 
3. In the middle pane, select the relying party trust created for APTRA Clear application. 
4. Double Click on the relying party trust. 
5. A pop-up window appears. Select endpoints Tab. 
 
 
6. Now select the SAML assertion consumer endpoints. 
 
7. Click on Edit Button.

<!-- Page 5 -->

 
Confidential   
 
 
 
5  
                   
 
  
8. Select the binding type as ‘post’ 
9. Update the trusted URL with aptra clear URL which is shared by NPCI. 
10.  Now click on ok. 
               
 
11. Click on apply. 
12. Restart ADFS services. 
 
Step-3: Configuring administrator User: 
 
To provide administrator access to any user, following changes are required: 
1. Ensure that the user is active in the active directory and is able to login from the 
machine where CCH access is required.

<!-- Page 6 -->

 
Confidential   
 
 
 
6  
2. Set following user attributes for the user: 
Routing number: nine digit MICR code for the bank 
User role: WEBCHI_ADMIN 
Note:  
1. The user role attribute value is required to be exactly same as given above. 
2. Please refer section “Steps to configure user attributes in Active Directory” for 
details  
 
Step-4: Configuring operations users for CCH: 
As a pre-requisite, bank needs to define the user roles to be permitted to access 
the system. E.g.: WEBCHI_OPERATOR can be used for normal operator. 
After finalizing the user role name, follow steps below to configure access for the 
users: 
3. Login to CCH UI using the WEBCHI_ADMIN user credentials 
4. Define the user roles finalized as the perquisite step. 
Note:  Please refer section “Steps to Configure User Groups at CCH” for details. 
5. Map the screen access to a given user role. 
6. Ensure that following attributes are set in active directory for all operations users: 
a. Routing number: Nine digit micr code for the bank 
b. User role: Any of the user roles finalized as pre-requisite step. 
Note: For detailed steps, please refer section “Steps to configure operations users in 
APTRA Clear as Bank Admin user” 
 
Step-5: Configuration changes at CCH: 
 Before requesting configuration changes at CCH, bank must validate the ADFS 
configuration using following steps: 
1. Open the ADFS URL in browser.  
https://[ADFS server IP]/adfs/ls/IdpInitiatedSignon.aspx 
2. Select the relying party and login to the Bank AD. Once after successful login, 
ADFS page will be redirected to APTRA Clear URL which is shared by NPCI. 
3. If URL re-direction is appearing in browser, which means AD Login is successful.

<!-- Page 7 -->

 
Confidential   
 
 
 
7  
4. Banks must share above ADFS URL with NPCI to configure the bank ADFS URL 
in APTRA Clear. This is last step to enable the CCH access for administrator and 
operations users. 
5. After confirmation from NPCI, bank needs to follow further steps. 
 
 
Step-6: Configuring user groups at CCH: 
Please refer steps detailed in Chapter-3: Steps to Configure User Groups at CCH 
 
Step-7: Mapping tasks to user groups at CCH: 
Please refer steps detailed in Chapter-3: Steps to Map Tasks to User Groups 
 
Step-8: Verifying bank operator login: 
Please refer steps detailed in Chapter-3: Steps to Verify Bank Operator Login 
Steps to configure user attributes in Active Directory 
1. Navigate to Active Directory Users and Computers. 
2. Select Users in left pane. 
3. Select a User and double click on it.

<!-- Page 8 -->

 
Confidential   
 
 
 
8  
      
4.  Navigate to Attribute Editor Tab. 
 
 
 
 
5. Update user Role as ‘WEBCHI_ADMIN’ and Routing Number as ‘bank routing number’. 
6. Click on ok button.

<!-- Page 9 -->

 
Confidential   
 
 
 
9  
Chapter II – Work Group user & roles creation: 
Member banks can do the user management using Work Group, in the absence of active 
directory, usage of Work Group is supported. Bank has to create the users in their Work 
Group module and assign rights to the respective user groups to access the Aptra clear 6.0 
application 
Bank must create following roles in the Work Group to map their users to enable the access 
to the users for the above web pages to monitor/ manage. 
1. WEBCHI_ADMIN 
2. WEBCHI_Operator 
 
Step-1: Configuring administrator user:  
Bank need to create WEBCHI_ADMIN group and then assign existing user to the 
WEBCHI_ADMIN group. This user will act as bank administrator and below mentioned 
steps to be followed. 
a) To open Workgroup module, go to Run Dialog ,enter lusrmgr.msc and press 
Enter 
b) On the left pane click groups. 
c) The system will list all the groups. 
d) Click action and create new group 
e) In new group specify the following details 
f) group name: WEBCHI_ADMIN 
g) Specify the group description 
h) Members: click Add to locate and Add members in the group 
i) Click create in the specified group 
j) Click close in the dialog box 
 
Step-2: Configuring operations users in Work Group:  
 
1. In Workgroup module go to Run Dialog, type lusrmgr.msc and press Enter 
2. On the left pane click groups. 
3. The system will list all the groups. 
4. Click action and create new group 
5. In new group specify the following details 
6. Group name for Ex: ‘Bank_Operator’

<!-- Page 10 -->

 
Confidential   
 
 
 
10  
7. Specify the group description 
8. Members: click Add to locate and Add members in the group 
9. Click create in the specified group 
10. Repeat step 4 to 10 if you wish to configure multiple user groups (e.g. bank_operator 
for normal data view and bank_super_operator to view critical data) 
11. Click close in the dialog box 
 
Step-3:  Configuration changes at CCH : 
1. Banks must inform NPCI to configure the authentication type as ‘Work Group’ in 
APTRA Clear for the bank. This is last step to enable the CCH access for 
administrator and operations users. 
2. After confirmation from NPCI, bank needs to follow further steps. 
 
Step-6: Configuring user groups at CCH: 
Please refer steps detailed in Chapter-3: Steps to Configure User Groups at CCH 
 
Step-7: Mapping tasks to user groups at CCH: 
Please refer steps detailed in Chapter-3: Steps to Map Tasks to User Groups 
 
Step-8: Verifying bank operator login: 
Please refer steps detailed in Chapter-3: Steps to Verify Bank Operator Login 
Chapter III – Common Steps: 
Steps to configure user groups at CCH 
1. Open web browser and enter APTRA Clear URL. 
https://<IPADDRESS>:<Port>/ecpix/servlet/ecpix?brandName=en&routingNumber
=<BankRoutingNumber> 
Note: IP address will be shared through mail. 
2. If bank login details are updated at CCH, following ADFS Login screen/windows 
credentials pop-up will appear. 
With ADFS Authentication is enabled at bank:

<!-- Page 11 -->

 
Confidential   
 
 
 
11  
 
 
 
With Windows Workgroup Authentication is enabled at bank: 
 
 
. 
3. Please provide admin user credentials, who belongs to WEBCHI_ADMIN Group. 
Once after successful login, following page appear.

<!-- Page 12 -->

 
Confidential   
 
 
 
12  
 
4. Bank admin user need to create different user groups using the administration 
module.  
a. Login using administration credentials 
b. On the administration module screen, click Add/Edit Groups. 
c. click add user group 
5. Now click on add user group button to create new bank group and permission. 
 
6. Now click on add user group button.

<!-- Page 13 -->

 
Confidential   
 
 
 
13  
7. Click on save. 
 
 
8. Now click on back button. 
 
Steps to map tasks to user groups: 
The mapping of user groups involves 3 steps: 
a) Selecting user group 
b) Mapping tasks to the groups 
c) Confirm and save the data 
1. Select the recently created group in group name drop down.

<!-- Page 14 -->

 
Confidential   
 
 
 
14  
2. Click on set permissions button, then following screen will appear. The map tasks 
to group screen enables the mapping of user groups to available tasks. 
 
3. Now select the tasks to the respective group. 
 
4. Click next button.

<!-- Page 15 -->

 
Confidential   
 
 
 
15  
5. Now click on save. 
6. Now select the role again and click on view group mapping. 
 
 
7. Make sure all selected tasks associated for newly created user role 
‘Bank_Operator’. 
8. Now, Login to Active Directory and update all users with routing number as Bank 
Routing Number and user role as ‘Bank_Operator’. 
 
Steps to verify bank operator Login: 
1. Open web browser and try the below URL to login to APTRA Clear as Bank user: 
https://<IPADDRESS>:<Port>/ecpix/servlet/ecpix?brandName=en&routingNumber
=<BankRoutingNumber> 
Note: IP address will be shared by NPCI through mail. 
2. Enter the user credentials for operations user. 
Once after successful authentication APTRA Clear bank page will be opened.

<!-- Page 16 -->

 
Confidential   
 
 
 
16
