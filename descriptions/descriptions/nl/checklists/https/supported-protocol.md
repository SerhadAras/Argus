# Supported Protocols


## SSL vs TLS

Secure Socket Layer (SSL) was het oorspronkelijke protocol dat werd gebruikt voor de versleuteling van HTTP-verkeer, dus in de stijl van HTTPS. Er zijn twee publiek uitgebrechte versies van SSL: versies 2 en 3. Beide hebben ernstige cryptografische tekortkomingen en mogen niet langer gebruikt worden.

Om verschillende redenen werd de volgende versie van het protocol (versie 3.1) Transport Layer Security versie 1.0 (TLSv1.0) genoemd.
Hierna zijn TLS-versies 1.1, 1.2 en 1.3 uitgebracht.



## Alleen sterke protocollen ondersteunen

De SSL-protocollen hebben een groot aantal zwakke punten, en zouden in geen geval mogen worden gebruikt.
Webapplicaties voor algemeen gebruik zouden standaard TLS 1.3 moeten gebruiken (en indien nodig TLS 1.2), waarbij alle andere protocollen zijn uitgeschakeld.
Wanneer een client verbinding probeert te maken met een zwakkere versie van TLS, moet dit worden geweigerd omdat u niet wilt dat er informatie uitlekt via een zwakke verbinding.


## Bronnen

[Owasp - Transport layer protection cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
