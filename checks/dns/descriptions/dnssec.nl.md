# DNSSEC

## Wat is DNS?

DNS, Domain Name System, is een systeem dat wordt gebruikt bij elke interactie met het internet. Het laat ons toe om een verstaanbare naam te gebruiken bij het bezoeken van een website. DNS zal deze namen achterliggend vertalen naar IP adressen. Servers hebben deze IP adressen nodig om met elkaar te kunnen communiceren om zo de gevraagde inhoud te verkrijgen van de juiste server.


## Wat is DNSSEC?

Omdat DNS op zich niet veilig is, heeft men een encryptie standaard hiervoor ontwikkeld; de "Domain Name System Security Extensions".
Dit zorgt ervoor dat de DNS data wordt ondertekend door de eigenaar van de data door een digitale handtekening. Dit is vergelijkbaar met het ondertekenen van een email met uw persoonlijke handtekening.


## Waarom heb ik DNSSEC nodig?

Deze standaard waarborgt dat de verkregen data van de bron komt dat het vermeldt en dat het niet aangepast was tijdens het vervoer.
Door de extra beveiliging van DNSSEC zal "spoofing" niet meer mogelijk zijn.
Spoofing komt voor wanneer een aanvaller het pakketje data onderschept, aanpast en opnieuw doorstuurt naar het slachtoffer.
Het slachtoffer zal hierdoor omgeleid worden naar een identieke website van de aanvaller waar deze de gegevens kan verkrijgen die het slachtoffer onbewust op de website heeft ingegeven.


## Hoe moet ik DNSSEC aanzetten?

Hoe men DNSSEC aanzet, hangt af van de DNS registrar.
Dit zoekt u best op in de documentatie en handleidingen van uw DNS registrar. <br>
Een paar vaak gebruikte registrars en hun handleidingen over DNSSEC:
* [Cloudflare](https://developers.cloudflare.com/dns/additional-options/dnssec/)
* [Google](https://support.google.com/domains/answer/6387342)
* [Amazon](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-configure-dnssec.html)
* [Combell](https://www.combell.com/en/blog/from-now-on-you-can-enable-dnssec-for-your-domain-name-yourself/)


## Bronnen

[Realhosting - wat is dnssec](https://realhosting.nl/helpdesk/wat-is-dnssec/)

[ICANN - DNSSEC what is it and why is it important](https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en)