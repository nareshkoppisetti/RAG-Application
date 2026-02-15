Oracle EBS SSO Integration with Azure AD Authentication

Azure Active Directory (AAD) SSO, Hybrid AAD SSO with On-premise ADFS

Do not build another SSO Solution just for EBS

MFA with Phone call or Text message

EBS Patching does not break SSO

EBS Upgrades do not break SSO

Oracle EBS can now be authenticated / SSO enabled with the Azure AD Authentication with an Azure Native App

Oracle E-Business Suite – EBS can be successfully integrated with Azure AD, Azure ADFS, Azure SSO, Azure Active Directory in Microsoft Azure Cloud with an SSO Gateway, SSOGEN. Azure SSO offers Active Directory Federation Services – ADFS SAML services for SSO Integrations. As Oracle E-Business Suite – EBS – Oracle Applications 11i, R12, and R12.2 does not support SAML directly, the need for a gateway raises.

SSOgen would act a gateway between Azure AD Authentication (Azure AD SSO) and Oracle EBS. Customer simply adds SSOGEN Gateway app to the Enterprise Applications in the customer tenant.

SSOgen adds more security such as Multi-Factor Authentication – MFA after a successful Azure ADFS SSO Login as well.

In addition to SAML integration with Azure ADFS, SSOgen is capable of integrating with Azure Active Directory - AD directory for LDAP lookup with a login form authentication or Kerberos - Windows Native Authentication.

The end user login experience would be pretty much similar to that of another Azure ADFS protected Application. There are no limitations on Azure ADFS Authentication Schemes for this. Oracle EBS can be protected with Azure ADFS Multi-Factor Logins as well. The SSOgen would be transparent to the end users.

Oracle APPS 11i, R12, and R12.2

Azure AD can be configured for Oracle EBS 11i, R12, and R12.2. Oracle EBS integrations such as OBIEE, Hyperion, EPM Suite, ADF Applications, WebCenter, OTM, Discoverer, and Agile PLM would also be SSO enabled seamlessly.

PeopleSoft, Siebel, JDE, and SAP can be SSO integrated with Azure ADFS SSO as well. But also, Cloud Applications such as Salesforce and Service-Now can be SSO registered with SSOgen as well.

OAM and OID are not necessary

Oracle Access Manager - OAM and Oracle Internet Directory - OID are not necessary for Oracle and Azure ADFS SSO Integrations with Oracle E-Business Suite - EBS versions 11i, R12, and R12.2.

Oracle EBS SSO is now Simplified and Automated

All it takes is two commands and 10 minutes: $ ssogen deployag & ssogen reg