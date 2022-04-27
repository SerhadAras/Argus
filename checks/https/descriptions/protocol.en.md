# Protocol


## SSL vs TLS

Secure Socket Layer (SSL) was the original protocol that was used to provide encryption for HTTP traffic, in the style of HTTPS. There were two publicly released versions of SSL - versions 2 and 3. Both of these have serious cryptographic weaknesses and should no longer be used.

For various reasons the next version of the protocol (SSL 3.1) was named Transport Layer Security  version 1.0 (TLSv1.0). Subsequently TLS versions 1.1, 1.2 and 1.3 have been released.


## what version should I use?

The SSL protocols have a large number of weaknesses, and should not be used in any circumstances.
The newer versions of TLS almost always patch a previous weakness, it is recommended to use the last released version of TLS.
At this moment, TLSv1.3 is the most secure option. Not all browsers are yet switched to the newest version, TLSv1.2 will also suffice because, security wise, there are no differences between the two versions.

## Sources

[Owasp - Transport layer protection cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)