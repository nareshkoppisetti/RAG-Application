JDE ADFS Integration for Single Sign On

Oracle JDE and Microsoft ADFS SSO Integration

As Oracle JD Edwards EnterpriseOne does not natively support SAML authentication, the challenge of integrating Oracle JDE with SAML Providers such as Microsoft ADFS araises. Oracle JDE and ADFS SSO Integration is simplified greatly with SSOgen SSO Gateway. SSOgen Gateway would be registered as a SAML 2.0 Relaying Party with ADFS Claims Provider.

ADFS SSO Integration with Oracle JDE is discussed in

, while this article covers the on-prem or hosted Microsoft ADFS Services.

ADFS Registration of SSOgen Relying Party:

JDE would be registered with SSOgen, as described in

Oracle JDE SSO Integrations for JDE EnterpriseOne

When a user enters into JDE EnterpriseOne, user is redirected to SSOGen for authentication. SSOgen in turn sends the user to ADFS for SSO Login. ADFS performs SSO Authentication using a login form, multi-factor authentication, or Desktop Authentication - Kerberos or Windows Native Authentication, WNA based on ADFS SSO Configuration. Upon a successful authentication at ADFS, the user is redirected back to EnterpriseOne Home through SSOgen.

The end user login experience would be pretty much similar to other applications SSO enabled by ADFS.

User would access JDE EnterpriseOne seamlessly from other ADFS SSO enabled applications without having to re-login, and vice-versa.

SSOgen is fully transparent to the end user during both SSO login and logout flows.

How to enable SSO in JDE?

Please read more about JDE SSO Configuration