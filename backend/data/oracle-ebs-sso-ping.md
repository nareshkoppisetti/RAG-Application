Oracle EBS and PingFederate SSO Integration without OID

Oracle EBS and PingFederate Single Sign On Integration

Oracle EBS and PING SSO integration is possible through SSOGEN Gateway. As Oracle EBS does not support SAML directly, SSOGen would be necessary to bridge the gap between PING SSO services and Oracle EBS. SSOGEN would be registered as a Service Provider in PING SAML IDP and Oracle EBS would be configured to talk to SSOGen.

When a user logs in to EBS, user is redirected to SSOgen, which in turn sends the user to PING SSO Authentication. PING would perform authentication process, and after a successful authentication, the user is redirected back to Oracle EBS Home Page via SSOgen. The end user experience would be similar to that of other applications that use PING SSO Logins. SSOgen is completely transparent during the login process in this case.

Oracle APPS 11i, R12, and R12.2

PING SSO can be enabled for Oracle EBS - Oracle APPS 11i, R12, and R12.2. Oracle EBS integrations such as OBIEE, Hyperion/EPM Suite, ADF Applications, WebCenter, Agile would also be seamlessly SSO Integrated with PING SAML.

Other Oracle Products such as Peoplesoft, Siebel, and JD Edwards can be SSO enabled with PING through SSOgen Gateway

OAM and OID are not necessary

With SSOGEN Gateway Solution, Oracle Access Manager - OAM and Oracle Internet Directory - OID are not required for PING SSO and Oracle Integrations.

How to enable SSO in Oracle EBS?

Please read more about Oracle EBS SSO Integration the following link.

Read more about Oracle EBS SSO Integrations from the following links

Learn more about other SSO Integration options with Oracle EBS