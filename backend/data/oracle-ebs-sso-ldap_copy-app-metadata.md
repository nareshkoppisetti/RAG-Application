Oracle EBS SSO (Single Sign-on) Options and Setup Guide

Learn about Oracle EBS SSO (Options and Setup) with a walk-through video to set up Oracle EBS SSO in 10 minutes. This does not require Oracle Access Manager, Oracle IDCS, or OID, or another SSO server. EBS SSO can be enabled with Active Directory, ADFS, Azure AD, PING, etc. (LDAP or SAML Identity Providers SSO) directly on EBS Server.

Oracle EBS SSO is an authentication solution that allows users to login with SSO logins, LDAP authentication, or AD passwords, instead of the EBS local password authentication. Oracle EBS SSO connector delegates the authentication to SSO Server, which performs the authentication on behalf of EBS.

By default, Oracle E-business Suite(EBS) authenticates users with FND_USER table internally, and this native authentication is known as EBS Local Authentication. As Single Sign-On (SSO) became popular, most organizations prefer to configure SSO for Oracle EBS, and enable logins with SSO credentials instead of the EBS local passwords. So, Oracle EBS SSO simply refers to SSO configuration in Oracle EBS 11i, R12.1, and R12.2.

Oracle EBS SSO is highly recommended for Improved Oracle EBS Security and Better User experience. SSO is a mandatory requirements for IT Security Audits in Oracle e-Business Suite.

Oracle EBS SSO is traditionally enabled with Oracle Access Manager – OAM and Oracle Internet Directory – OID. Prior to Oracle Access Manager (OAM), Oracle 10g Single Sign On (OSSO 10g) had been the traditional Single Sign On options for Oracle EBS from 11i to R1.1. Oracle EBS 12.2 does not support OSSO 10g any more, and it needs either OAM or modern SSO solutions such as Oracle Identity Cloud Services (IDCS) or SSOGEN.

Why is Oracle EBS SSO important?

Users don't have to remember dozens of passwords for Oracle e-Business Suite - 11i, 12.1, and 12.2.

Weak passwords in Applications are no longer allowed. Welcome123 and Oracle123 are the most popular weak passwords in Oracle EBS.

Access to Oracle EBS is terminated instantly, when an employee/contractor leaves. This is a requirement Audit requirement.

Passwords alone are not secure enough these days, multi-factor authentication is a must have for Oracle EBS today.

Enforce user to change SSO password periodically to follow security guidelines.

Users don’t have to login multiple times, resulting in a better productivity and better user experience.

EBS Password reset calls to Helpdesk would be greatly reduced, and Oracle EBS Support teams are relieved.

IT Security Audits such as SoX, HIPAA demand Single Sign On for Oracle EBS 11i, R12, and 12.2.

Users don’t have to remember Applications URLs anymore, as URLs change from time to time.

What is an Alternative SSO for EBS?

As traditional SSO solutions are not only expensive, but also complex in nature, and the typical SSO implementation takes about 6 months. An alternative SSO solution for Oracle EBS is SSOGEN, which is implemented under 10 minutes.

SSOGEN is a modern, and NextGen Single Sign On solution that offers many benefits, including free Multi Factor Authentication (MFA), and it integrates with about 300 SSO solutions in the market.

SSOGEN can either authenticate directly with LDAP servers such as Microsoft Active Directory or delegate authentication to your enterprise SSO solutions such as Azure AD, Okta, OneLogin, etc.

Completely Unique Solution that no other vendor offers in the market.

SSOGEN offers cost savings up to 70%, compared to Oracle OAM, OID, and IDCS.

SSOGEN is deployed in under 10 minutes, fully automated and simplified.

Customer centric support team brings in 25+ years of experience in Oracle SSO space.

Oracle EBS team has validated the SSOGEN integration and approved the certification.

Oracle EBS SSO: LDAP Authentication Options

EBS SSO - SSOGEN configuration supports Windows Native Authentication - WNA, Kerberos, Desktop Authentication (Zero Touch SSO), which enables User to access Oracle EBS without having to explicitly login to EBS. Desktop Authentication uses Network/Domain Login for Authentication. Kerberos is still secure and convenient for the users.

EBS SSO - SSOGEN configuration supports LDAP Authentication with the customer User Directory such as Microsoft Active Directory in real-time (i.e. no need to synchronize the users and passwords).

In addition to LDAP SSO, SSOGEN also performs multi factor authentication for Oracle EBS for critical environments. Here is a quick list of compatible LDAP Directory Servers for Oracle EBS.

Oracle EBS SSO: Delegated SSO Authentication Options

SSOGEN supports SSO Gateway, SAML Gateway, and OpenID Connect Gateway Solutions. With SSO Gateway, EBS SSO authenticates with CA Siteminder, IBM Tivoli Access Manager - TAM, Oracle Access Manager - OAM authentication to Oracle EBS.

EBS SSO - SSOGEN Configuration supports SSO authentication with Okta, Oracle Identity Cloud Services - IDCS, OneLogin, Azure SSO, Azure ADFS, Microsoft ADFS, PingFederate IdP SSO Solutions for Oracle EBS 11i, R12, and R12.2.

In addition to delegating the authentication to the other SSO systems, SSOGEN is capable of adding multi factor authentication - MFA for Oracle EBS on top of the delegated SSO Auth.

How to configure Oracle EBS SSO?

Here are the high level steps to enable SSO in Oracle EBS (for Azure AD use case):

Apply EBS AccessGate Patches, if EBS version is lower than 12.2.4.

Clean up prior SSO registration (if any): $ ./ ssogen cleanup

Deploy EBS AccessGate: $ ./ ssogen deployag

Configure SSO in EBS: $ ./ssogen reg

Add SSOGEN App in Azure AD - Enterprise Applications

Copy the Azure AD App metadata to EBS and restart EBS services

Oracle EBS SSO Integration is detailed here with step by step instructions. If this is the first time enabling SSO on EBS, the following patches need to be applied. Also, make sure that FS Clone is complete and online patching cycle is NOT active.

R12.2 EBS Patch | 20735848 |

EBS AccessGate | 24008856 | Check 2202932.1 for the latest patch

SSOGEN Support team sends out customer specific scripts for the registration. Please upload ssogen.zip and ssogen_modules.zip to $NE_BASE/sso, and unzip ssogen.zip

Oracle e-Business Suite AccessGate - EAG: fndauth.war deployment is now part of 12.2 WebLogic Domain itself, and it deployed to oaea_server1.

SSO Registration: Enable SSO on all Web Nodes

If there are DMZ/iSupplier nodes, please repeat the above step, with function dmzreg

Bounce all EBS Services on Web Tiers and test the SSO logins.

For deploying access gate, you may follow Oracle standard, adProvisionEBS.pl ebs-create-oaea_resources. However, deployag script does call the same script for your convenience

#2 Clean up prior SSO registration (if any)

Run Cleanup to register previous SSO/LDAP references in the databasae, FND_USER_PREFERENCES..etc

If there are multiple Web Nodes configured for High Availability, the above script has to be run on all Web Tiers, with the node no# matching oaea_server#. For example:

Please use -managedsrvport flag to specify port number explicitly. For example: .

If deploag fails for any reason, please run undeployag to clean up the previous deployment, and run deployag to complete the deployment. This post-clone step may be necessary in some cases.

SSO Registration is the process in which EBS URL is registered with SSO for logins.

Restart all Oracle EBS Services and test SSO Login at /OA_HTML/AppsLogin

EBS Local Logins continue to work with the URL: /OA_HTML/AppsLocalLogin.jsp

Non-SSO (Non-LDAP/AD) users such as SYSADMIN can still login through the Local Login URL: /OA_HTML/AppsLocalLogin.jsp

#5 Add SSOGEN App in Azure AD – Enterprise Applications

Search SSOGEN Gallery App by SSOGEN keyword, Add App, and Configure EBS URLs from SSOGEN Reg command, and download the app metadata

#6 Copy App Metadata and Restart EBS Services

Copy the Azure AD - App Metadata URL to ssogen folder as idp.xml & Restart EBS Services with adstpall.sh and adstrtal.sh

Now that SSO integration is complete, let's take a quick look at the EBS SSO Login flow:

User accesses EBS URL in the browser

EBS redirects to SAML IdP with SAML Request

SAML IdP/ADFS performs the authentication either by collecting username and password inputs or by network login/Kerberos, based on its configuration

Once SAML IdP/ADFS successfully performed the authentication, it redirects the user to EBS with a SAM Response, which includes a signature, NameID, etc.

EBS Server reads SAML Response and creates its own EBS session

EBS identifies the FND Responsibilities (Authorizations)

User lands in EBS Home Page

Oracle EBS SSO Login Trace with SAML Tracer and HTTP requests

Lets take a look at the EBS SSO login trace with SAML Tracer and HTTP requests:

is the SAML IdP URL in this case

The first SAML request is the SAMLRequest, and the second is the SAML Response

There is no third party between EBS and SAML IdP

Browser acts as a channel between the EBS and SAML IdP

No direct communication between EBS Server to SAML IdP

Oracle EBS Single Sign On Profiles that matter most for Oracle EBS SSO Integration are shown below.

Applications SSO Type | SSWA w/SSO

Applications SSO Auto Link User | Enabled

Application SSO LDAP Synchronization | Disabled

Applications Override SSO Server Language | Override SSO Server Language

Applications SSO User Creation and Updation Allowed | Enabled

Applications SSO Login Types | BOTH

Oracle EBS SSO: Troubleshooting and Fixes

ORA-20001: Unable to call fnd_ldap_wrapper.create_user due to following reason: Oracle Internet Directory is not registered correctly.

Application SSO LDAP Synchronization profile may impact user creation process.

Please make sure that system profile

. Also, ensure other SSO profiles are set as suggested above and that the system is not previously registered with another sso such as Oracle OAM, Oracle SSO, and Oracle OID/OUD. Please cleanup SSO preferences as documented above.

Error: Unable to link account. This E-Business Suite user account is marked as a

Your Oracle E-Business Suite account has not been linked with the Single Sign-On account that you just entered. Please enter you Oracle E-Business Suite information. The next time you sign on with your Single Sign-On account, it will automatically sign you on to the Oracle E-Business Suite using the following account information.

Applications SSO Login Types is set to Local for this user, 502662611. Profile "Applications SSO Login Types" should be set to either BOTH or SSO for SSO login to work. This profile is typically set to BOTH at Site Level, and it's NOT set at the user level.

"Applications SSO Login Types" is typically set to Local to reset EBS Local password (in FND_USER table). If this profile "Applications SSO Login Types" is set to BOTH, Password change is not allowed. User Password field is greyed out in User Form. If this is the case, after password is reset, remove the user level value for this profile.

Your Oracle E-Business Suite account has not been linked with the Single Sign-On account.

Your Oracle E-Business Suite account has not been linked with the Single Sign-On account.

Your Oracle E-Business Suite account has not been linked with the Single Sign-On account that you just entered. Please enter your Oracle E-Business Suite information. The next time you sign on with your Single Sign-On account, it will automatically sign you on to the Oracle E-Business Suite using the following account information.

This Autolink page is thrown when EBS can not find the user name by the GUID sent by the SSO Server. EBS instance has previously been registered with another SSO or user has manually linked to another user by submitting another user name and password in this page. SSS User SSO7 has got previous GUID value in FND_USER table. This user has to be unlinked, by updating GUID null, which enables EBS Autolink feature to populate the right GUID value during the next SSO login.

SQL> select user_name,end_date,user_guid from fnd_user where user_name='SSO7';

SQL>update fnd_user set user_guid = null where user_name='SSO7' ;

SQL> select user_name,end_date,user_guid from fnd_user where user_name='SSO7' ;

Please suggest the user to re-try the sso login

SQL> select user_name,end_date,user_guid from fnd_user where user_name='SSO7' ;

The following profiles are very important for EBS SSO Functionality:

from apps.fnd_profile_options fpo, apps.fnd_profile_options_tl fpot, apps.fnd_profile_option_values fpov, apps.fnd_user fu

Make sure that the output matches to the following profile values:

Applications SSO Linking Source of Truth

Applications SSO User Creation and Updation Allowed

Check EBS User for end date

select user_name,end_date,user_guid from fnd_user where user_name='&EBS_SSO_USER_NAME';

When in doubt, update the GUID to null so that it gets set during the SSO login:

update fnd_user set user_guid=null where user_name='&EBS_SSO_USER_NAME' ;

Check User Level profile options for any suspicious profiles:

from apps.fnd_profile_options fpo, apps.fnd_profile_options_tl fpot, apps.fnd_profile_option_values fpov, apps.fnd_user fu,apps.fnd_user fu1

Oracle e-Business Suite AccessGate - EAG Troubleshooting

Verify the AccessGate version from http://demoebs.ssogen.com:8000

Check 2202932.1 for the latest patch if any AccessGate issues are observed

Enable Debug at the AccessGate and restart oaea_serverx

How To Collect E-Business Suite 12.2 AccessGate LogFiles (Doc ID 1683163.1)

HTTP 400 - Bad Request Errors after enabling SSO

As SSO adds many cookies, you would see HTTP 400 in R12.1 & R12.2 when the apache request limits are reached.

Please suggest the customer to set the following limits in $CONTEXT_FILE , run autoconfig, and restart all services.

EBS requests fail with "Size of a request header field exceeds server limit" [ID 1370626.1]

Lengthy Configurator URL : CZ Does Not Launch [ID 1374444.1]

Url Causes Http 400 Error [ID 1374260.1]

Check the following timeout variables in $CONTEXT_FILE:

Check the following EBS profile options

Refer to the following Oracle Notes for more info:

R12: Forms Timeout More Than 2 Hrs Is Not Working After R12 Upgrade [ID 734077.1]

How to Change User Session Timeout in e-Business Suite R12 [ID 1067115.1]

User Sessions Get Timed Out Before Idle Time Parameter Values Are Reached [ID 1306678.1]

Self-Service Pages Are Failing After Changing the s_oc4j_sesstimeout [ID 780612.1]

How AutoConfig sets ICX: Session Timeout [ID 307149.1]

11i/R12 How to Debug "Transaction Context Is Lost" or "You are trying to access a page that is no longer active" [ID 456906.1]

Random error Your login session has expired when using Load Balancing [ID 387306.1]

The following context variables should be set correctly for the load balancer URL to function:

egrep 's_web|s_active_webport|s_login_page|s_enable_sslterminator|s_url_protocol|s_local_url_protocol|s_login' $CONTEXT_FILE egrep 's_web' $CONTEXT_FILE

When SSL is terminated at the load balancer, the following values are needed in EBS:

Oracle EBS - SSO Login throws HTTP 500 after authentication

Oracle e-Business Suite EBS AccessGate - EAG Log files show: java.lang.NoClassDefFoundError: oracle/ias/cache/ObjectNotFoundException

<26-Oct-2018 17:06:34 o'clock BST> <Error> <ServletContext-/ebsauth_payptt> <BEA-000000> <Context intialization failed

Truncated. see log file for complete stacktrace

Truncated. see log file for complete stacktrace

: EAG WebLogic Domain does not have JRF (Java Required Files) enabled during the initial creation. oracle/ias/cache libraries are included in Oracle JRF Jar files.

: Recreate the WebLogic Domain with JRF included.

Oracle iSupplier DMZ Configuration - SSO Login is not working for Oracle iSupplier DMZ

Make sure that EBS DMZ is properly set up, as documented in

Oracle E-Business Suite R12 Configuration in a DMZ (Doc ID 380490.1)

3. Check the context values in DMZ Context file and run auto config.

s_enable_sslterminator= { remove # ; if SSL is terminated in load balancer}

4. Verify the following profile options for the products installed in EBS:

Self Registered New User Default Responsibility

5. Verify Hierarchy Type for the following profiles. Hierarchy type should be properly set by txkChangeProfH.sql SERVRESP from the first step.

User Profile Name | Internal Name

1. Applications Web Agent | APPS_WEB_AGENT

2. Applications Servlet Agent | APPS_SERVLET_AGENT

3. Applications JSP Agent | APPS_JSP_AGENT

4. Applications Framework Agent | APPS_FRAMEWORK_AGENT

6. ICX: Oracle Discoverer Launcher | ICX_DISCOVERER_LAUNCHER

7. ICX: Oracle Discoverer Viewer Launcher | ICX_DISCOVERER_VIEWER_LAUNCHER

8. Applications Help Web Agent | HELP_WEB_AGENT

10. BOM:Configurator URL of UI Manager | CZ_UIMGR_URL

11. QP: Pricing Engine URL | QP_PRICING_ENGINE_URL

OAEA error message after 12.2.6 upgrade

Error message in the browser: URL Validation Failed

oracle.apps.fnd.ext.sso.FndSsoException: Exception while updating user session.

Caused by: java.lang.IllegalArgumentException: Illegal empty string argument

Cause: EBS has been upgraded to 12.2.6 and latest EAG patch wasn't applied.

Solution: Issue has been fixed after applying

and performing undeploy and deploy of accessgate.

: We have seen similar issues, when previous 12.1 SSO registration is not cleaned up before upgrading to 12.2.

In this case, we have to run

to remove previous SSO/LDAP registration and proceed with SSOGen Registration

How does this profile work? Applications SSO Login Types - APPS_SSO_LOCAL_LOGIN

After enabling SSO in Oracle EBS, default EBS URL, /OA_HTML/AppsLogin is SSO enabled. Backdoor URL / Local Login for Non-SSO users such as SYSADMIN is still allowed through Local Login URL /OA_HTML/AppsLocalLogin.jsp. However, some of the user logins are not working through Backdoor URL / Local Login URL.

System Profile, Applications SSO Login Types, APPS_SSO_LOCAL_LOGIN, is set to SSO.

System Profile, Applications SSO Login Types, APPS_SSO_LOCAL_LOGIN should be set to BOTH or LOCAL for local login to succeed at User Level (for example SYSADMIN). Applications SSO Login Types: LOCAL allows that only Local Logins through /OA_HTML/AppsLocalLogin.jsp. SSO allows SSO logins through /OA_HTML/AppsLogin only. BOTH allows both SSO logins and Local Logins.

Unable to change EBS Password in Password Field in FND User Form - Grayed out

Unable to set the EBS Local Passwords after enabling SSO. EBS Passwords are typically stored in FND_USER table.

System Profile, Applications SSO Login Types, APPS_SSO_LOCAL_LOGIN, is set to SSO.

System Profile, Applications SSO Login Types, APPS_SSO_LOCAL_LOGIN should be set to BOTH or LOCAL to set EBS password at user Level or site level. We recommend BOTH at site level, which allows password changes, and local logins.

Read more about Oracle EBS SSO Integrations from the following links

Here are the Frequently Asked Questions and common questions about Oracle EBS SSO.

Once EBS is SSO enabled, Oracle EBS will delegate the authentication to Single Sign On server, which authenticates the users and redirects the user back to Oracle EBS. Oracle EBS recognizes the SSO server authentication and creates EBS Session (ICX and FND sessions). SSO Client/ERP connectors sits on the EBS Web Server and enforces the SSO authentication.

Oracle EBS does NOT natively, out of the box support SAML authentication. To enable SAML SSO Authentication for Oracle EBS, it needs to be integrated with Oracle Access Manager(OAM), IDCS, or SSOGEN.

No, Oracle EBS Asserter is only needed for Oracle Identity Cloud Services (IDCS), and not for SSOGEN, as SSOGEN uses out of the box EBS AccessGate (fndauth.war out of FND_TOP).

What is Oracle E-business Suite AccessGate?

EBS AccessGate is the fndauth.war in FND_TOP, and its primary function is to manage the EBS sessions during the SSO login process.

Do we need OAM and OID?

No, we do not need Oracle Access Manager(OAM) or Oracle Internet Directory(OID), or Oracle Identity Cloud Services(IDCS) to enable SSO with SSOGEN.

Does it work with Oracle EBS 11i or R12.1?

Yes, SSOGEN works with Oracle EBS 11i, R12.1, and R12.2 versions.

Does it work with Oracle EBS on-prem or hosted in OCI?

Yes, SSOGEN works seamlessly with Oracle EBS hosted on-premises or hosted in the cloud (OCI, AWS, GCP, or Azure).

Do we need to sync users to the cloud?

No. Unlike Oracle IDCS, which requires EBS users to be synchronized to Oracle Cloud, SSOGEN does not require the user sync. SSOGEN is a completely on-premises (on EBS Servers) solution and it does not have any cloud components or network dependencies.

No, SSOGEN is a complete on-premises solution and it does not have any cloud components.

Does SSOGEN support Non-SSO/Local Logins for Oracle EBS?

Yes, Non-SSO users (such as SYSADMIN) will continue to login with /OA_HTML/AppsLogin.jsp EBS Link.

We appreciate your feedback. Click to rate this product/article.