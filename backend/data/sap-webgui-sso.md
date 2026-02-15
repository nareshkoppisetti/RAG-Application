SAP WebGUI SSO - Single Sign On Implementation

SAP WebGUI SSO - Single Sign On Implementation

SAP WebGui SSO Integration strengthens security for SAP System and SAP Applications. Enabling SSOgen Single Sign On for SAP NetWeaver Portal would facilitate single password access, and secure and seamless access to SAP NetWeaver Applications - both Java and ABAP applications, SAP Hana Cloud Applications, SAP SaaS Applications such as Concur and SuccessFactors. SSOgen protects SAP on-premise applications using a SSO Client, and SAP Cloud Applications - SaaS Apps using SAML Protocol. Users would login to either SSOgen Portal or SAP NetWeaver Enterprise Portal, and then access both SAP on-premise and SAP Cloud applications without having to login multiple times or to remember multiple passwords. SSOgen offers a free multi-factor authentication to further secure SAP Authentication. SAP Authorization would still function normally, as SSO is involved in the authentication process only. For instance, Success Factors Login would be SSO enabled with multi-factor authentication, while internal SAP Applications are SSO enabled with Active Directory Authentication.

SSOgen Single Sing On Solution brings in many benefits for the end users. Users don't have to remember multiple passwords for multiple applications anymore. Users don't have to login multiple times during a work-day, thereby resulting an increased user productivity. SSO also reduces help-desk calls for password resets and lockout issues. SSO is not only mandatory for IT Security Audits, but also highly recommended as a part of SAP Security Best practices to fight against cyber-crime and data thefts.

How to enable SSO for SAP NetWeaver Portal?

SSO Configuration in SAP Portal 7.3 is simplified with SSOgen SSO Implementation. SSO Parameters in SAP need to be adjusted to read SSO Headers for authentication by adding HeaderVariableLoginModule in SAP NetWeaver SSO Configuration.

Install a Web Server such as Apache Web Server so that SAP Applications are proxied through a Web Server

Configure the proxy rules in the Web Server to forward the traffic to backend SAP Web Servers for SAP context /irj.

Install SSOGEN - SSO Client in the Web Server to protect the web resources.

Stop the SAP J2EE Dispatcher and server services

Backup SAP_Engine_Install_Dir\ume\authschemes.xml.bkp to authschemes.xml and open in a text editor to add SSO Scheme to read SSO User Token - HTTP Headers. OB_USER is the default header name for SSO header in SAP, however we recommend using SSOGEN_USER, which is available in SSOgen integrations by default.

Administration interface >> System Administration >> System Configuration >> Configuration >> Direct Editing and add the logoff URLs:

Update HeaderVariableLoginModule with the following variable

Add HeaderVariableLoginModule for each application to support SSO

Launch Visual Administrator tool >> Choose Policy Configurations >> Authentication

Add HeaderVariableLoginModule for each application to support SSO.

Restart the whole SAP System and SAP Applications.

SAP WebGUI SSO with LDAP Authentication

SSOgen supports authentication with many popular LDAP Directory Servers in the market today. With SSOgen, SAP can be SSO enabled with Windows Native Authentication - WNA (a.k.a Kerberos or Desktop Authentication or Zero Touch SSO) or SSO enabled with the following LDAP Directory Servers.

SAP WebGUI SSO with Active Directory Authentication

SAP WebGUI SSO with RadiantLogic Authentication

SAP WebGUI SSO with UnboundID Authentication

SAP WebGUI SSO with OpenDS Authentication

SAP WebGUI SSO with OpenDJ Authentication

SAP WebGUI SSO with CA Directory Authentication

SAP WebGUI SSO with IBM Directory Authentication

SAP WebGUI SSO with NetIQ Authentication

SAP WebGUI SSO with OpenLDAP Authentication

SAP WebGUI SSO with SLAPD Authentication

SAP WebGUI SSO with 389 Directory Server Authentication

SAP WebGUI SSO with Apache Directory Authentication

SAP WebGUI SSO with Oracle Unified Directory - OUD Authentication

SAP WebGUI SSO with Oracle Directory Server - ODS Authentication

SAP WebGUI SSO Integration with other SSO Solutions

SSOgen supports SAML IDP v1, SAML IDP v2, OpenID Providers for Single Sign-On delegation to other SSO Solutions. With SSOgen, SAP Applications would be easily integrated with other SSO Solutions such as Okta, Oracle Identity Cloud Services - IDCS, OneLogin, Azure SSO, Azure ADFS, Microsoft ADFS, PingFederate, Shibboleth, OpenID Providers, and other popular SSO Solutions such as CA Siteminder, IBM Tivoli Access Manager, and Oracle Access Manager, and many more.

SAP and Shibboleth SAML SSO Integration

SAP and PingFederate SAML SSO Integration

SAP and Oracle Identity Cloud Services – IDCS Integration

SAP and Azure ADFS - Azure SSO Integration

SAP and CA Siteminder SSO Integration

SAP and IBM Tivoli SSO Integration

Read more about SSOgen Unique Benefits