SSOGEN OpenID Gateway enables delegated authentication to OpenID Providers for OAUTH authentication.

OpenID Gateway extends OpenID Provider authentication to applications that do not support OpenID Connect.

OpenID Gateway would be configured with OpenID Connect and its registered with OpenID Provider. User application is SSO configured with SSOgen OpenID Gateway with a web server plugin, similar to CA Siteminder WebAgent. While OpenID Gateway acts as a openid connect with OpenID Provider, Web Server plug-in enforces policies and SSO authentication for the user application.

SSOgen OpenID Gateway also offers additional security such as free multi factor authentication, after a successful authentication by OpenID Provider.

require user stores such as Oracle Internet Directory - OID for Oracle EBS SSO Integration.

When a user enters into the user application, user is redirected to OpenID Gateway for authentication. OpenID Gateway in turn sends the user to OpenID provider for authentication. OpenID provider collects the credentials from the user using a SSO Login form and performs SSO Authentication. Upong a successful authentication, the user is then redirected back to application via OpenID Gateway.

OpenID Connect is configured on OpenID Gateway.

Install and Configure SSO Agent, Web Server Plug-in to protect Application URIs.

Optionally enable step up, multi factor authentication at OpenID Gateway.

Complete SSO and a flexible SSO and SAML Gateway

SSOgen is a complete SSO Solution with MFA that works with many LDAP Servers. SSOgen is also a flexible SSO Gateway, IdP SAML Gateway, SP SAML Gateway, Okta SPGW, and OpenID Gateway with most of the popular SSO solutions.

We appreciate your feedback. Click to rate this product/article.