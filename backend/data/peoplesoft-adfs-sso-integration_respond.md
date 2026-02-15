PeopleSoft ADFS Integration for Single Sign On

PeopleSoft ADFS Single Sign On Integration

As PeopleSoft does not natively support SAML authentication, the challenge of integrating PeopleSoft with SAML Providers such as Microsoft ADFS araises. PeopleSoft and ADFS SSO Integration is simplified greatly with SSOgen SSO Gateway. SSOgen Gateway would be registered as a SAML 2.0 Relaying Party with ADFS Claims Provider - IdP.

Azure ADFS SSO Integration with PeopleSoft is discussed in

, while this article covers the on-prem or hosted Microsoft ADFS Services. This solution resolves the security vulnerability issue of PS_TOKEN – TokenChpoken Attack as well.

ADFS Registration of SSOgen Relying Party:

PeopleSoft would be registered with SSOgen using standard procedure:

When a user enters into PeopleSoft, she is redirected to SSOGen for Authentication. SSOgen in redirects the user to Microsoft ADFS for SSO Login. Microsoft ADFS authenticates the user. Upon a a success SSO Login at Microsoft ADFS , the user is redirected back to PeopleSoft Applications through SSOgen.

End-user SSO Login experience could be very much like other Applications, which are SSO protected by the Microsoft ADFS.

User would access PeopleSoft Applications seamlessly from other Microsoft ADFS SSO enabled Applications without having to re-login, and vice-versa.

SSOgen is completely transparent to the end user during both SSO login and logout flows.

How to enable SSO in PeopleSoft?

Please read more about PeopleSoft SSO Configuration and PS_TOKEN issues