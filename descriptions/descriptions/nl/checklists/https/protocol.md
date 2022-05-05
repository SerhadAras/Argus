# Protocol


## SSL vs TLS


Secure Socket Layer (SSL) was het oorspronkelijke protocol dat werd gebruikt voor de versleuteling van HTTP-verkeer, dus in de stijl van HTTPS. Er zijn twee publiek uitgebrechte versies van SSL: versies 2 en 3. Beide hebben ernstige cryptografische tekortkomingen en mogen niet langer gebruikt worden.

Om verschillende redenen werd de volgende versie van het protocol (versie 3.1) Transport Layer Security versie 1.0 (TLSv1.0) genoemd.
Hierna zijn TLS-versies 1.1, 1.2 en 1.3 uitgebracht.


## Welke versie moet ik gebruiken?

De SSL-protocollen hebben een groot aantal zwakke punten, en mogen in geen geval worden gebruikt. Gebruik in de plaats daarvan de TLS protocollen.
De nieuwere versies van TLS patchen bijna altijd een eerdere zwakte, het is aanbevolen om de laatst uitgebrachte versie van TLS te gebruiken.
Op dit moment is TLSv1.3 de meest veilige optie. Omdat nog niet alle browsers zijn overgeschakeld op de nieuwste versie, TLSv1.2 zal ook volstaan omdat er veiligheidstechnisch gezien geen grote verschillen zijn tussen beide versies.


## Bronnen

[Owasp - Transport layer protection cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)