# SSL/TLS Certificates


## What is SSL / TLS ?

Secure Socket Layer (SSL) was the original protocol that was used to provide encryption for HTTP traffic, in the style of HTTPS. There were two publicly released versions of SSL - versions 2 and 3. Both of these have serious cryptographic weaknesses and should no longer be used.

For various reasons the next version of the protocol (SSL 3.1) was named Transport Layer Security  version 1.0 (TLSv1.0). Subsequently TLS versions 1.1, 1.2 and 1.3 have been released.


## Why do I need a SSL/TLS Certificate?

TLS/SSL certificates are used to authenticate the website's organization identity to ensure users are interacting with legitimate website owners.
These certificates are similar to people having a passport or identity card.


### Encryption

SSL/TLS Certificates provide end-to-end-encryption with the TLS or the discontinued and unsafe SSL protocol.
In short this means that a server and an end-user can communicate with eachother without anyone else knowing what it is they send each other.
In short, with encryption an attacker cannot understand any of the communication between your server and clients.


## How do I make a valid certificate?

For an SSL certificate to be valid, domains need to obtain it from a certificate authority (CA). A CA is an external organization, a trusted third party, that generates and gives out SSL certificates. The CA will also digitally sign the certificate with their own private key, allowing client devices to verify it.

### Free vs Paid CA

|                    | Free CA                            | Paid CA                      |
|--------------------|:----------------------------------:|:----------------------------:|
| **Type**           | Only a Domain Validation option    | Domain Validation, Organization Validation and Extended Validation |
| **Level of validation**|Only identity of website owner  |in depth verification         |
| **Validity period**  | 30-90 days                       | 1-2 years                    |
| **Support**          | None                             | Chat, email, call...         |
| **Level of Trust**   | Very little, only Domain Validation| A lot, visible trust in URL|
| **Warranty**         | None                             | In case of catastrophy, get paid out between 10 thousand and 1.75 million |

With this comparison table, we recommend using a paid CA as it delivers more trust and certainty than an unpaid CA. However, for non e-commerce websites, using a free CA will suffice.

Free CA: letsencrypt, zerossl, cacert, sslforfree... <br>
paid CA: RapidSSL, Thawte SSL123, Sectigo SSL Certificate, GeoTrust QuickSSL Premium...



## Sources

[digicert - how tls ssl certificates work](https://www.digicert.com/how-tls-ssl-certificates-work#:~:text=TLS%2FSSL%20certificates%20are%20used,interacting%20with%20legitimate%20website%20owners.)

[cloudflare - what is an ssl certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/#:~:text=For%20an%20SSL%20certificate%20to,client%20devices%20to%20verify%20it.)

[SSL renewals - difference between free ssl certificate & paid ssl certificate](https://sslrenewals.com/blog/difference-between-free-ssl-certificate-and-paid-ssl-certificate)
