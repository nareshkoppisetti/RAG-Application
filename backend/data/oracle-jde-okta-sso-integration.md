JDE Okta SSO Integration for Oracle JDE EnterpriseOne

Oracle JDE and Okta SAML SSO Integration

Oracle JDE and Okta SSO Integration is possible with a SSOgen SSO Gateway. SSOgen Gateway would be registered as a SAML 2.0 Application in Okta, as described in

. Oracle JDE would be registered with SSOgen using standard process, as described in

When a user enters into Oracle JDE EnterpriseOne, user is redirected to SSOGen for authentication. SSOgen in turn sends the user to Okta for SSO Login. Okta performs SSO Authentication using a login form, multi-factor authentication, or Desktop Authentication - Kerberos or Windows Native Authentication, WNA based on Okta SSO Configuration. Upon a successful authentication at Okta, the user is redirected back to Oracle JDE EnterpriseOne Home Page via SSOgen.

The end user login experience would be pretty much similar to other applications SSO enabled by Okta. Oracle JDE Application can be added to Okta Applications Dashboard by Okta Admin, and end users can launch Oracle JDE Applications like another Okta Application.

User would access Oracle JDE Applications seamlessly from other Okta SSO enabled applications without having to re-login, and vice-versa.

SSOgen is fully transparent to the end user during both SSO login and logout flows. No special licensing is necessary from Okta for this SAML Application Integration. Oracle Access Manager – OAM and Oracle Internet Directory – OID are NOT required for this SSO Integration.

How to enable SSO in JDE?

Please read more about JDE SSO Configuration.