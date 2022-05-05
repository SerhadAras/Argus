# Redirect


## Wat is HTTP

HTTP is een protocol voor de overdracht van gegevens tussen server en client. Het beschrijft een gestandaardiseerde volgorde en syntax voor het presenteren van informatie.
De aanvragen naar een server worden "requests" genoemd omdat de clients gegevens opvragen die op een server zijn opgeslagen.
De aanvragen naar een client worden "responses" genoemd, omdat deze oproepen de gegevens bevatten die de clients aan de server hebben gevraagd.


## Wat is HTTPS

HTTPS is HTTP met encryptie. Het verschil tussen de twee protocollen is dat HTTPS een TLS of SSL tunnel gebruikt om normale HTTP-verzoeken en -antwoorden te coderen.
TLS en SSL zijn cryptografische protocollen die de mogelijkheid bieden om een kanaal op te zetten tussen server en client om gecodeerd verkeer te versturen.
HTTPS is bijgevolg veel veiliger dan HTTP. Een website die HTTP gebruikt, heeft http:// in zijn URL, terwijl een website die HTTPS gebruikt, https:// heeft.


## Waarom is een omleiding van HTTP naar HTTPS noodzakelijk

Wanneer een gebruiker een website bezoekt via http, kan een aanvaller het onversleutelde verkeer lezen dat tussen server en client wordt verzonden.
Daarom is een redirect naar HTTPS noodzakelijk.
Met HTTPS wordt al het verkeer versleuteld en kan de aanvaller dit niet lezen.


## Bronnen

[Venafi - what are the differences between http https](https://www.venafi.com/blog/what-are-differences-between-http-https-0#:~:text=HTTPS%20is%20HTTP%20with%20encryption,uses%20HTTPS%20has%20HTTPS%3A%2F%2F.)
