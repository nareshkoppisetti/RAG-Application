PeopleSoft SAML 2.0 Integration for Single Sign On

PeopleSoft and SAML 2.0 SSO Integration

PeopleSoft and SAML SSO Integration is feasible with a SSOgen SSO Gateway. SSOgen Gateway would be registered as a SAML 2.0 SP application with SAML IdP such as Shibboleth IdP, as defined in

. PeopleSoft would be registered with SSOgen using standard procedure, as described in

Whilst a user enters into PeopleSoft, she is redirected to SSOGen for Authentication. SSOgen in redirects the user to SAML IdP for SSO Login. SAML IdP authenticates the user. Upon a a success SSO Login at SAML IdP , the user is redirected back to PeopleSoft Applications through SSOgen.

End-user SSO Login experience could be very much like other Applications, which are SSO protected by the SAML IdP.

User would access PeopleSoft Applications seamlessly from other SAML IdP SSO enabled applications without having to re-login, and vice-versa.

SSOgen is completely transparent to the end user during both SSO login and logout flows.

How to enable SSO in PeopleSoft?

Please read more about PeopleSoft SSO Configuration and PS_TOKEN issues