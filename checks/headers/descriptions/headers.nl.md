# Headers

## Wat zijn headers?

Bij het bezoeken van een website, sturen de client en server heel wat extra informatie mee met de eigenlijke request (verzoek) of response (antwoord).
Deze extra informatie wordt aan de voorkant van het hele "pakket" verzonden, vandaar de naam "headers".
Hun doel is hoofdzakelijk de communicatie tussen server en client onderhouden zodat iedereen dezelfde regeltjes volgt.


## Over HTTP veiligheids-headers

Onder al de header-waarden, zijn bepaalde headers noodzakelijk om een goede beveiliging te bekomen.
Wanneer een client geconfronteerd wordt met bepaalde waarden in de headers, zal deze gedwongen worden de regels te volgen die door deze veiligheids-headers worden opgelegd. <br>
De meest voorkomende en meest kritieke HTTP veiligheids-headers die we controleren zijn:

### x-frame-options
Deze waarde zorgt ervoor dat een mogelijke aanvaller een gebruiker niet kan misleiden om op iets anders te klikken dan wat hij denkt te klikken. Dit wordt "clickjacking" genoemd omdat de aanvaller de gebruiker misleidt door op iets te klikken dat ogenschijnlijk betrouwbaar is, maar in werkelijkheid kwaadaardig is.

beste waardes: "**deny**" of "**sameorigin**"

### x-xss-protection
Deze header waarde weerhoudt de browser ervan extra code uit te voeren die in eerste instantie niet was aangevraagd.
Wanneer er wel "illegaal" code wordt uitgevoerd, spreken we van een "cross-site scripting attack". Deze aanval houdt in dat een aanvaller kwaadaardige code toevoegt aan een http-verzoek.

beste waarde: "**1 ; mode=block**"

### x-content-type-options
Wanneer we communiceren met een server, moeten de gegevens die we ontvangen en verzenden volgens een bepaalde standaard geformatteerd zijn zodat deze automatisch verwerkt en gelezen kunnen worden.
Deze header zorgt ervoor dat de manier vaststaat waarop de ontvangende partij te weten kan komen welk standaardtype gebruikt wordt om de gegevens te formatteren.
De enige veilige manier om deze header in te stellen is "nosniff", dit betekent dat de aanvaller geen cross-site scripting aanvallen kan uitvoeren (zie vorige header)

beste waarde: "**nosniff**"

### content-type
Deze header wordt gebruikt om aan te geven in welk formaat de gegevens geformatteerd worden voordat ze naar de client verstuurd worden.
Opgepast: wanneer geen x-content-type-options (vorige header) is ingesteld, kan deze header door de client genegeerd worden en bestaat nog steeds het gevaar van aan cross-site scripting aanval.

beste waarde: "**text/html ; charset=UTF-8**"

### referrer-policy
De referrer-policy header bepaalt hoeveel informatie over de oorspronkelijke website wordt meegestuurd in de request (verzoek) wanneer een gebruiker op een link klikt die hen naar een andere website doorverwijst.
Dit beleid kan zo streng of laks zijn als nodig is, respectievelijk variërend van helemaal geen informatie (een propere doorverwijzing) tot alle beschikbare informatie.

beste waarde: "**strict-origin-when-cross-origin**"

### strict-transport-security
Strict-transport-security, afgekort HSTS, voorkomt toegang tot de website via HTTP. Elke poging gebruik makende van HTTP zal worden omgezet naar HTTPS bij gebruik van deze beveiligingsheader.
HTTP is een protocol dat wordt gebruikt voor de communicatie tussen client en server.
Met HTTPS wordt het transport van gegevens versleuteld, waardoor het veel veiliger is dan HTTP.

beste waarde: "**max-age=... ; includeSubDomains ; preload**"

### access-control-allow-origin
In deze header kan men aangeven welke andere websites inhoud van uw website mogen ophalen.
Het wordt als onveilig beschouwd om deze header als "null" of als "*" in te stellen.

beste waardes: **niet "null" of "*"**

### server
Deze header wordt vooral gebruikt als prestatieverhogende header door mee te geven welke software de server draait.
Er is echter een groot nadeel aan de server header. Wanneer de server te gedetailleerde waarden in deze header deelt, is het voor een aanvaller mogelijk gemakkelijker om exploits in de gebruikte software te vinden.

beste waardes: "**cloudflare**", "**website**" of "**webserver**"

### x-powered-by
x-powered-by bevat gegevens over wat voor soort server de requests (verzoeken) van uw website afhandelt. In tegenstelling tot de server header, heeft deze geen werkelijk doel anders dan puur informatief.
Het is het veiligst om deze header uit te schakelen, omdat het anders voor een aanvaller alleen maar gemakkelijker wordt om exploits van een server te vinden.

beste waarde: **disable this header!**

### x-aspnet-version
x-aspnet-version is een header die alleen wordt gebruikt in ontwikkeling en moet worden uitgeschakeld bij het in productie brengen van de website.
Als deze is ingeschakeld, lekt deze informatie over de ASP.NET-versie die uw website gebruikt. ASP.NET is een web-framework om het bouwen van websites en webapplicaties te vergemakkelijken.

beste waarde: **disable this header!**

### x-aspnetmvc-version
Vergelijkbaar met x-aspnet-version, lekt deze header ook informatie over de versie van de ASP.NET MVC website.
Ook deze header moet worden uitgeschakeld wanneer de website in productie gezet wordt.Similar to x-aspnet-version, this header will also leak information about the version of the ASP.NET MVC website.
This header should also be disabled when in production.

beste waarde: **disable this header!**


## Bronnen

[loginradius - HTTP Security Headers](https://www.loginradius.com/blog/engineering/http-security-headers/#:~:text=Why%20HTTP%20Security%20Headers%20are,code%20injection%2C%20clickjacking%2C%20etc.)

[GeeksforGeeks - HTTP headers](https://www.geeksforgeeks.org/http-headers/)

[developer Mozilla - HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
