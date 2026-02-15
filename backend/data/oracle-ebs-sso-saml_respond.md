Oracle EBS and SAML IdP SSO Integration

Oracle EBS and SAML IDP Integration for Single Sign On

SAML IDP SSO can now be integrated with Oracle EBS for both SAML 1.0 and SAML 2.0. As Oracle EBS does not talk SAML protocol, SSOGEN would bridge the gap between Oracle EBS and SAML IDP.

SSOGEN would be registered as a Service Provider with SAML IDP and Oracle EBS would be registered with SSOgen. When a user logs in to EBS, user is redirected to SSOgen, which in turn sends the user to SAML IDP Authentication. SAML IDP would either do Kerberos or Windows Native Authentication or form based login based on its configuration. Upon a successful authentication, user is sent back to Oracle EBS Home Page.

Oracle Access Manager (OAM), Oracle Internet Directory (OID), and Oracle Unified Directory (OUD) are not required for this SAML Integration with Oracle EBS.

The end user experience would be similar to that of other applications that are configured to use SAML Authentication. SSOgen is completely transparent during the login process in this case.

Oracle APPS 11i, R12, and R12.2

SAML SSO would be enabled for Oracle EBS - Oracle APPS 11i, R12, and R12.2. Oracle EBS integrations such as OBIEE, Hyperion/EPM Suite, ADF Applications, WebCenter, Agile would also be seamlessly SSO Integrated with SAML IDP SSO.

Other Oracle Products such as Peoplesoft, Siebel, and JD Edwards can be SSO enabled with SAML IDP SSO through SSOgen Gateway.

OAM and OID are not necessary

With SSOGEN Gateway Solution, Oracle Access Manager - OAM and Oracle Internet Directory - OID are not required for SAML and Oracle Integrations.

How to enable SSO in Oracle EBS?

Please read more about Oracle EBS SSO Integration the following link.

Read more about Oracle EBS SSO Integrations from the following links

Learn more about other SSO Integration options with Oracle EBS