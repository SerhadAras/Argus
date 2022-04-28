# Mailcheck - DKIM


## Wat is DKIM en waarom heb ik dit nodig?

Wanneer we een e-mail ontvangen, hoe zeker zijn we er dan van dat de oorspronkelijke afzender ook echt de vermelde afzender is?
Het antwoord op die vraag is: als er geen DKIM-handtekening is, weten we het niet.

DKIM, Domainkeys Identified Mail, is een e-mailverificatietechniek waarmee de afzender de e-mail digitaal kan ondertekenen. Op deze manier kan de ontvanger controleren of de e-mail is verzonden en geautoriseerd door de eigenaar van het domein. De handtekening is echter niet zichtbaar voor de eindgebruikers en wordt automatisch gecontroleerd.
De digitale handtekening garandeert ook dat de e-mail onderweg niet werd gewijzigd.


## Hoe verkrijg ik DKIM?

**Voordat u DKIM instelt**
<ol>
  <li>Verkrijg de aanmeldingsgegevens voor uw domeinregistrar</li>
  <li>Zoek uit of uw domeinregistrar 2048-bit DKIM sleutels ondersteunt</li>
  <li>Controleer de instellingen van de "outbound gateway"</li>
  <li>(Optioneel) Controleer of er een bestaande DKIM sleutel voor uw domein bestaat</li>
</ol>

**Zet DKIM aan voor uw domein**
<ol>
  <li>Haal uw DKIM sleutel op in uw Admin console</li>
  <li>Voeg uw DKIM sleutel toe bij uw domeinregistrar</li>
  <li>Zet DKIM aan in uw beheerconsole</li>
  <li>Controleer of DKIM ondertekening aan staat</li>
</ol>


## Bronnen

[wikipedia - DomainKeys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)

[Mimecast - everything you need to know about DKIM](https://www.dmarcanalyzer.com/dkim/)