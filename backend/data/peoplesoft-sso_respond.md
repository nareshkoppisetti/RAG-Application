PeopleSoft SSO - Single Sign On Solution

PeopleSoft SSO is most desired for PeopleSoft Portal implementations, as PeopleSoft Portal is the central and unified interface to access other PeopleSoft Applications, such as HCM or CRM.

PeopleSoft SSO authenticates the user during the first login to PeopleSoft Portal, then allows the user to access other PeopleSoft Applications without forcing the user to login to the each application over and over. Therefore, SSO is a must have for PeopleSoft Applications.

Security Concerns with PS_TOKEN - TokenChpoken Attack

Oracle PeopleSoft offers Single Sign On – SSO out of the box to offer the better user experience for its customers. This out of the box PeopleSoft SSO uses PS_TOKEN cookie to store the user or session information to pass from PeopleSoft Application to another.

PS_TOKEN cookie stores confidential information such as UserID - Name of the Authenticated User, Node Name – Node Name Authenticated the user, Date And Time – when the PS_TOKEN was issued, and SHA Signature in base64 encoded.

According to ERPScan report about Oracle PeopleSoft vulnerabilities, PeopleSoft Applications are susceptible to the TokenChpoken attack, which affects systems that use Single Sign On SSO, is possible because an PS_TOKEN Authentication cookie used by PeopleSoft Applications can be forged. When the PS_TOKEN is identified by a "brute force" TokenChpoken attack, it is possible to log in under a system account and gain access to all data from the compromised system. Read more at:

ERPScan Security Report about PeopleSoft Security Vulnerabilities

Solution for PS_TOKEN TokenChpoken Attack Vulnerability

Disable out of the box SSO from PeopleSoft to eliminate PS_TOKEN completely.

Enable External SSO for PeopleSoft with solutions such Microsoft Azure, CA Siteminder, Okta, Oracle Access Manager, and SSOGEN.

Enable Multi Factor Authentication - MFA for PeopleSoft Applications

Enable External SSO for all PeopleSoft Applications for seamless access

How to enable PeopleSoft Single Sign On?

Configure Web Server or Apache or HTTPD Server to front-end the PeopleSoft Servers and enable SSO protection for all PeopleSoft URLs.

Ensure that all the traffic is routed through the web server and SSO protected. Disable any direct access to PeopleSoft URLs.

Enable SSO at Web Server and Configure SSO in PeopleSoft. Header Injection and Cookie forgery are completely eliminated.

PeopleSoft SSO Integration with LDAP Servers

PeopleSoft SSO Integration with SSOGEN opens up multiple options. Through SSOgen, PeopleSoft is SSO enabled with Windows Native Authentication - WNA or Kerberos or Desktop Authentication or Zero Touch SSO, and most of the Directory Servers - LDAP Version 2 and LDAP Version 3 servers. A quick list of PeopleSoft LDAP SSO Integration possibilities with SSOgen:

SSOGEN supports SAML IDP v1, SAML IDP v2, OpenID Providers for PeopleSoft Applications. With SSOgen Integration, PeopleSoft would be easily integrated with other SSO Solutions such as Okta, Oracle Identity Cloud Services - IDCS, OneLogin, Azure SSO, Azure ADFS, Microsoft ADFS, PingFederate, Shibboleth, OpenID Providers, and other popular SSO Solutions such as CA Siteminder, IBM Tivoli Access Manager, and Oracle Access Manager, and many more.

PeopleSoft Integration with IBM Tivoli AM

PeopleSoft - Okta, Azure ADFS, and SAML Integrations

Read more about PeopleSoft SSO Integrations from the following links:

PeopleSoft Okta Single Sign On Integration

PeopleSoft ADFS Integration for Single Sign On

PeopleSoft SAML 2.0 Integration for Single Sign On

Learn more about the only FREE Multi-Factor Authentication for PeopleSoft Applications

Step by step instructions to enable SSO for PeopleSoft are described below. This SSO integration follows Oracle Standard Guidelines to enable SSO for PeopleSoft.

Logon to PeopleSoft Console http://ps.example.com:8000/psp/ps/?cmd=start using Admin credentials(Example: PS/PS).

PeopleTools >> Security >> User Profiles >> User Profiles

to create a new user profile

Web Profile to configure SSO user for the Public Access

PeopleTools >> Web Profile >> Web Profile Configuration >> Search >> PROD >> Security

**** Input the User ID and password created earlier and Save.

Edit Signon PeopleCode to enable SSOGEN Authentication

PeopleTools >> Security >> Security Objects >> Signon PeopleCode

Enable the Check Box as shown below.

Test PeopleSoft SSO logins at /psp/ps/?cmd=start

Optionally, update index.html in PORTAL.war with the SSO Login Redirect.

Test PeopleSoft SSO logins without cmd=start explicit parameters.