Oracle EBS Shibboleth SSO Implementation for 11i, R12, and 12.2

Oracle EBS - Shibboleth SAML IDP SSO Integration

Shibboleth SAML IDP SSO is integrated with Oracle EBS through SSOGEN SAML Gateway. As Oracle EBS does not support SAML IDP SSO Such as Shibboleth, SSOgen would be necessary to bridge the gap between SAML and Oracle EBS. SSOGEN would be registered as a Service Provider with Shibboleth IDP and Oracle EBS would be configured to delegate authentication to SSOgen. When a user logs in to EBS, user is redirected to SSOgen, which in turn sends the user to Shibboleth SSO. After a successful authentication by Shibboleth IDP, user is sent back to Oracle EBS Home Page via SSOgen gateway.

Oracle Access Manager – OAM and OID is the default solution for Oracle EBS (Oracle Applications), and other Oracle Products such as Oracle Portal, WebCenter, Discover, and Oracle BI – OBIEE. However, if your organization chose Shibboleth as the strategic enterprise SSO solution, then you would want to enable Shibboleth for Oracle products as well. SSOgen offers a simplified and flexible solution for this integration.

The end user experience would be similar to that of another Shibboleth SSO protected Application. SSOgen is completely transparent during the login process in this case.

Oracle APPS 11i, R12, and R12.2

Shibboleth SSO can be enabled for Oracle EBS - Oracle APPS 11i, R12, and R12.2. Oracle EBS integrations such as OBIEE, Hyperion/EPM Suite, ADF Applications, WebCenter, Agile would also be seamlessly SSO Integrated with Shibboleth IDP.

Other Oracle Products such as Peoplesoft, Siebel, and JD Edwards can be SSO enabled with Shibboleth IDP through SSOgen Gateway

OAM and OID are not necessary

With SSOGEN Gateway Solution, Oracle Access Manager - OAM and Oracle Internet Directory - OID are not required for Shibboleth IDP and Oracle Integrations.

How to enable SSO in Oracle EBS?

Please read more about Oracle EBS SSO Integration the following link.

Read more about Oracle EBS SSO Integrations from the following links

Learn more about other SSO Integration options with Oracle EBS