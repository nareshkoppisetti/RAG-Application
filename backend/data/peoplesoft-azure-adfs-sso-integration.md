PeopleSoft and Azure ADFS SAML SSO Integration

As PeopleSoft does not natively support Azure ADFS SSO Authentication, PeopleSoft and Azure ADFS SSO Integration is highly sought after. This integration is simplified with SSOgen SSO Gateway.

SSOgen Gateway would be registered as a SAML 2.0 Application in Azure ADFS, as described in

Configure SSO for Applications not in Azure Active Directory

PeopleSoft would be registered with SSOgen, as described in

When a user enters into PeopleSoft, user is redirected to SSOGen for authentication. SSOgen in turn sends the user to Azure ADFS for SSO Login. Azure ADFS performs SSO Authentication using a login form, multi-factor authentication, or Desktop Authentication - Kerberos or Windows Native Authentication, WNA based on Azure ADFS SSO Configuration. Upon a successful authentication at Azure ADFS, the user is redirected back to PeopleSoft Home Page via SSOgen.

The end user login experience would be pretty much similar to other Applications SSO enabled by Azure ADFS. PeopleSoft Application can be added to Azure AD Application Gallery by Azure Admin, and end users can launch PeopleSoft Applications like another Azure AD Application.

User would access PeopleSoft Applications seamlessly from other Azure ADFS SSO enabled applications without having to re-login, and vice-versa.

SSOgen is fully transparent to the end user during both SSO login and logout flows.

How to enable SSO in PeopleSoft?

Please read more about PeopleSoft SSO Configuration and PS_TOKEN issues