# DNSSEC

## What is DNS?

The Domain Name System is a system used with every interaction on the internet. It allows us to visit a website using a human-friendly name. DNS will translate these names to IP addresses. Servers need these IP addresses to be able to communicate with each other and thus retrieve the required content from the right server.


## What is DNSSEC?

Because DNS is not safe, an encryption authentication standard has been developed; the Domain Name system Security Extensions. This means the DNS data is signed by the owner of the data using a digital signature. Comparable to signing an email with your personal signature.


## Why do I need DNSSEC?

This standard ensures the retrieved data came from the origin it states and that the retrieved data wasn't modified in transit.
The added security of DNSSEC means that "spoofing" is no longer possible.
Spoofing occurs when an attacker intercepts the requested data, modifies it and forwards it again to the victim. The victim will then be redirected to an identical website of the attacker where he or she can receive the credentials the victim unknowingly enters on this website.


## How do I enable DNSSEC?

How to enable DNSSEC depends on the used DNS registrar.
Please look up how to enable dnssec in the documentation of your DNS registrar. <br>
Some commonly used registrars and their guides on how to enable DNSSEC:
* [Cloudflare](https://developers.cloudflare.com/dns/additional-options/dnssec/)
* [Google](https://support.google.com/domains/answer/6387342)
* [Amazon](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-configure-dnssec.html)
* [Combell](https://www.combell.com/en/blog/from-now-on-you-can-enable-dnssec-for-your-domain-name-yourself/)


## Sources

[Realhosting - wat is dnssec](https://realhosting.nl/helpdesk/wat-is-dnssec/)

[ICANN - DNSSEC what is it and why is it important](https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en)