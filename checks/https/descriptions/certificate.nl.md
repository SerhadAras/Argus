 SSL/TLS Certificaten


## Wat is SSL / TLS ?

Secure Socket Layer (SSL) was het oorspronkelijke protocol dat werd gebruikt voor de versleuteling van HTTP-verkeer, dus in de stijl van HTTPS. Er zijn twee publiek uitgebrechte versies van SSL: versies 2 en 3. Beide hebben ernstige cryptografische tekortkomingen en mogen niet langer gebruikt worden.

Om verschillende redenen werd de volgende versie van het protocol (versie 3.1) Transport Layer Security versie 1.0 (TLSv1.0) genoemd.
Hierna zijn TLS-versies 1.1, 1.2 en 1.3 uitgebracht.


## waarom heb ik een SSL/TLS Certificaat nodig?

TLS/SSL-certificaten worden gebruikt om de identiteit van de organisatie van de website te verifiëren, zodat gebruikers er zeker van kunnen zijn dat ze met legitieme website-eigenaren communiceren.
Deze certificaten zijn vergelijkbaar met het hebben van een paspoort of identiteitskaart.


### Encryptie

SSL/TLS certificaten bieden end-to-end encryptie met het TLS of het stopgezette en onveilige SSL protocol.
In het kort betekent dit dat een server en een eindgebruiker met elkaar kunnen communiceren zonder dat iemand anders de inhoud kan lezen.
Kortom, met encryptie kan een aanvaller niets begrijpen van de communicatie tussen server en client.


## Hoe verkrijg ik een geldig certificaat?

Om geldig te zijn, moeten domeinen een SSL-certificaat aanvragen bij een certificeringsinstantie (CA). Een CA is een externe organisatie, een vertrouwde derde partij, die SSL-certificaten genereert en afgeeft. De CA ondertekent het certificaat ook digitaal met hun eigen privésleutel, zodat clientapparaten het kunnen verifiëren.


### Free vs Paid CA

|                    | Free CA                            | Paid CA                      |
|--------------------|:----------------------------------:|:----------------------------:|
| **Type**           | Alleen een domein validatie optie    | Domein validatie, organisatie validatie en uitgebreide validatie |
| **Validatieniveau**|Alleen identiteit van de website eigenaar|uitgebreide verificatie |
| **Geldigheidsperiode**  | 30-90 dagen                       | 1-2 jaar                   |
| **Ondersteuning**          | Geen                             | Chat, email, bellen...        |
| **Niveau van vertrouwen**   | Zeer weinig, alleen domein validatie| veel, zichtbaar vertrouwen in URL|
| **Garantie**         | Geen                             | In geval van een ramp, uitbetaald tussen 10 duizen en 1.75 miljoen |

Met deze vergelijkingstabel raden wij het gebruik van een betaalde CA aan, aangezien deze meer vertrouwen en zekerheid biedt dan een onbetaalde CA. Echter, voor niet e-commerce websites, zal het gebruik van een gratis CA vaak volstaan.

Gratis CA: Letsencrypt, zerossl, cacert, sslforfree... <br>
betaalde CA: RapidSSL, Thawte, SSL123, Sectigo, Geotrust, QuickSSL premium


## Bronnen

[digicert - how tls ssl certificates work](https://www.digicert.com/how-tls-ssl-certificates-work#:~:text=TLS%2FSSL%20certificates%20are%20used,interacting%20with%20legitimate%20website%20owners.)

[cloudflare - what is an ssl certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/#:~:text=For%20an%20SSL%20certificate%20to,client%20devices%20to%20verify%20it.)

[SSL renewals - difference between free ssl certificate & paid ssl certificate](https://sslrenewals.com/blog/difference-between-free-ssl-certificate-and-paid-ssl-certificate)
