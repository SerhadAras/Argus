# Mailcheck - DKIM


## What is DKIM and why do I need it?

When receiving an email, how certain are we that its original sender really is the stated sender?
the answer on that question is: if there is no DKIM signature, we don't know.

DKIM, Domainkeys Identified Mail, is an email authentication technique that enables the sender to digitally sign the email. This way, the receiver can verify the email was sent and authorized by the owner of the domain. The signature however is not visible to end-users and will be checked automatically.
The digital signature will also guarantee that the email was not modified in transit.


## How do I get DKIM?

**Before you set up DKIM**
<ol>
  <li>Get the sign-in information for your domain registrar</li>
  <li>Find out if your domain registrar supports 2048-bit DKIM keys</li>
  <li>Check outbound gateway settings</li>
  <li>(Optional) Check for an existing DKIM key for your domain</li>
</ol>

**Turn on DKIM for your domain**
<ol>
  <li>Get your DKIM key in your Admin console</li>
  <li>Add your DKIM key at your domain registrar</li>
  <li>Turn on DKIM in your Admin console</li>
  <li>Verify DKIM signing is on</li>
</ol>


## Source

[wikipedia - DomainKeys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)

[Mimecast - everything you need to know about DKIM](https://www.dmarcanalyzer.com/dkim/)