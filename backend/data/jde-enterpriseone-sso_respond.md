Oracle JDE SSO Integrations for JDE EnterpriseOne

JDE SSO SAML Integrations for EnterpriseOne

JDE SSO implementation with SSOgen enables integrations with SAML IDP v1, SAML IDP v2, OpenID Providers for Single Sign On. EnterpriseOne SSO would be easily integrated with other SSO Solutions such as Okta, Oracle Identity Cloud Services - IDCS, OneLogin, Azure SSO, Azure ADFS, Microsoft ADFS, PingFederate, Shibboleth, OpenID Providers, and other popular SSO Solutions such as CA Siteminder, IBM Tivoli Access Manager, and Oracle Access Manager, and many more.

JDE EnterpriseOne and Okta SSO Integration

JDE EnterpriseOne and OneLogin SSO Integration

JDE EnterpriseOne and Shibboleth SAML SSO Integration

JDE EnterpriseOne and PingFederate SAML SSO Integration

JDE EnterpriseOne and Oracle Identity Cloud Services – IDCS Integration

JDE EnterpriseOne and Azure ADFS - Azure SSO Integration

JDE EnterpriseOne and Microsoft ADFS Integration

JDE EnterpriseOne and CA Siteminder SSO Integration

JDE EnterpriseOne and IBM Tivoli SSO Integration

JDE EnterpriseOne and NetIQ SSO Integration

Oracle JDE SSO Integration with LDAP Servers

JDE SSO Integration with SSOgen offers multiple authentication options. JDE EnterpriseOne would be SSO enabled with Windows Native Authentication - WNA (a.k.a Kerberos or Desktop Authentication or Zero Touch SSO) or authenticated against most of the popular LDAP Servers in the market today.

EnterpriseOne - 389 Directory Server Authentication

EnterpriseOne - Oracle Unified Directory - OUD Authentication

EnterpriseOne - Oracle Directory Server - ODS Authentication

How to enable JDE SSO - Single Sign On

Oracle JDE SSO Integration strengthens JDE System security, enhances user experience, and increases user productivity, and reduces help-desk calls for password resets and lockout issues. SSO is not only mandatory for IT Security audits, but also recommended as per JDE Security Best practices.

Here is a very high level procedure to implement SSO for EnterpriseOne:

Install a Web Server such Oracle HTTP Server or Apache Web Server (Linux httpd).

Configure the OHS/httpd Web Server to talk to backend EnterpriseOne WebLogic Servers for EnterpriseOne context /jde and port.

Install and configure SSO Client - Web Server Plug-in and protect JDE URLs.

Enable SSO for JDE URLs. Protect the JDE URI /jde

Open EnterpriseOne Server Manager from a browser.

Select your EnterpriseOne HTML Server instance.

Select Network Settings from the Configuration section.

In the Security Server Configuration section, select the Enable

Stop and restart the EnterpriseOne HTML Server.

EnterpriseOne SSO - User Login Flow

A user attempts to access an EnterpriseOne Application URL

SSOGEN SSO Client deployed on the EnterpriseOne HTTP Server intercepts the request.

SSO Client enforces the authentication by sending the user to SSOGEN

SSOGEN then performs the user authentication either by Kerberos or Windows Authentication, or LDAP Authentication with Active Directory, or delegating authentication to Azure ADFS, or Okta, or another SSO Provider.

Once SSO Authentication is successful, SSOGEN creates the response cookie and http header tokens for JDE.

Web Server would decrypt and read the message and then grants the access to protected /jde URIs.

EnterpriseOne Application identifies the authentication performed by the web server and grant the access by redirecting the user to EnterpriseOne Home Page.

JAS.INI parameter 'LogoutOnBrowserClose=true' when SSO is enabled

JDE with SSO enablement does not close the user session, when user closes the window without logging in. Before enabling SSO, JDE closes the session when user closes browser window. Sessions should be ended when browser is closed even if SSO is enabled.

Apparently, this seems to be a bug with JDE not closing JDE Sessions when user closes the browser window.

Closing browser without log out JDE first is not supported starting from tools release 9.1.4.

This is reported in enhancement Bug 20853997 - ENABLE LOGOUTONBROWSERCLOSE JAS SETTING WHEN USING OAM SINGLE SIGN ON. To monitor bug progress, refer to How to Monitor a Code or Enhancement Request (ER) Bug from My Oracle Support Document 1298390.1.

Unable To Access JDE Web Client With OAM SSO and Microsoft Edge Browser .. Is SSOGEN SSO compatible with Edge Browser

When JDE is SSO enabled with Oracle Access Manager (OAM), user SSO login in Microsoft Edge browser does not work. JDE direct link is working as expected in Microsoft Edge browser. OAM SSO Login for JDE is working well in other browsers such as IE, Chrome and Firefox.

Per OAM Certification Matrix, OAM is not supported with Edge browser.

SSOGEN Complete SSO Solution and SSO Gateway Solutions work seamlessly in all the browsers including Microsoft Edge.

SSOGEN SSO Gateway works great with Azure AD, Microsoft ADFS, CA Siteminder, IBM Tivoli Access Manager, Oracle Access Manager (OAM), Ping Federate SSO, OpenSSO, OpenID, Okta, and OneLogin.

SSOGEN free MFA Solution works well in Microsoft Edge browser as well.

What are the supported JDE versions for SSO

SSOGEN supports pretty much all versions of JDE that supports SSO. We have customers using SSOgen with

JDE 8.9, 9.0, 9.1, and 9.2

Read more about SSOgen Unique Benefits and more