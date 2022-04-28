# Redirect


## What is HTTP
HTTP is a protocol for transmitting data between servers and clients. It describes a standardised order and syntax for presenting information.
The calls to a server are called "requests" because clients request data stored on a server.
The calls to a client are called "responses" because these calls contain the data the clients requested from the server.


## What is HTTPS

HTTPS is HTTP with encryption. The difference between the two protocols is that HTTPS uses TLS or SSL to encrypt normal HTTP requests and responses.
TLS and SSL are cryptographic protocols that provide the ability to set up a channel between server and client to send encrypted traffic.
As a result, HTTPS is far more secure than HTTP. A website that uses HTTP has http:// in its URL, while a website that uses HTTPS has https://.


## Why is a redirect necessary?

When a user visits a website over http, an attacker can read the unencrypted traffic sent between server and client.
This is why a redirect to HTTPS is necessary.
Using HTTPS, all trafic will be encrypted and the attacker will be unable to read this.


## Sources

[Venafi - what are the differences between http https](https://www.venafi.com/blog/what-are-differences-between-http-https-0#:~:text=HTTPS%20is%20HTTP%20with%20encryption,uses%20HTTPS%20has%20HTTPS%3A%2F%2F.)
