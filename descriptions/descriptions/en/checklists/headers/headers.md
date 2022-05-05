# Headers

## What are headers?

Upon visiting a website, the client and server send some extra information along with the actual request or response.
This extra information is sent at the front of the whole "package", thus called headers.
Their purpose is mainly maintaining proper communication between the server and client with the same rules.


## HTTP security headers

Among all the headers are certain header values that are necessary for a good security practice. When a client is confronted with certain values in the headers, it will be forced to follow the rules imposed by these security headers. <br>
Most common and critical HTTP security headers we check:

### x-frame-options
this value ensures a possible attacker cannot trick a user into clicking something different than what they think they are clicking. This attack is called "clickjacking" because the attacker misleads the user into clicking something seemingly trustworthy, but is actually malicious.

best values: "**deny**" or "**sameorigin**"

### x-xss-protection
this header value stops the browser from executing additional code which were not initially requested. When this happens, we speak of a "cross-site scripting attack". This attack consist of an attacker adding malicious code into an http request.

best value: "**1 ; mode=block**"

### x-content-type-options
When communicating with a server, the data we receive and send should be formatted in a certain standard so it can be automatically read and processed.
This header provides the way the receiving party is allowed to learn which standard type was used to format the data.
The only safe way to set this header is "nosniff", this means the attacker can't perform cross-site scripting attacks (look previous header).

best value: "**nosniff**"

### content-type
This header is used to indicate which format is used for the data sent to the client. When no x-content-type-options is set, this header may be ignored by the client and there will be still danger of a cross site scripting attack.

best value: "**text/html ; charset=UTF-8**"

### referrer-policy
The referrer-policy header controls how much information about the original website will be included in the request when a user clicks on a link that redirects them to another website. This policy can be as strict or lax as intended, respectively varying from no information at all (this is a clean redirect) to every piece of information available.

best value: "**strict-origin-when-cross-origin**"

### strict-transport-security
Strict-transport-security, abbreviated HSTS, will prevent access to the website using HTTP. Every attempt with HTTP will be converted to HTTPS when using this security header.
HTTP is a protocol used for communication between client and server.
With HTTPS, the transportation of data will be encrypted, thus is much safer than plain HTTP.

best value: "**max-age=... ; includeSubDomains ; preload**"

### access-control-allow-origin
In this header you can specify which other websites can fetch content from your website.
It is considered unsafe to set this header as "null" or as "*".

best value: **not "null" or "*"**

### server
This header is mostly performance enhancing by passing along which software is used by the server.
There is however one caveat to this header. When the server shares overly-detailed values in this header, it is possibly easier for an attacker to find exploits in the used software.

best value: "**cloudflare**", "**website**" or "**webserver**"

### x-powered-by
x-powered-by contains data about what kind of server handles the requests of your website. Unlike the server header, it has no real purpose other than purely informational.
For safety measures, it is better to unset this header as this makes it only easier for an attacker to find exploits of a server.

best value: **disable this header!**

### x-aspnet-version
x-aspnet-version is a header only used in developing and should be disabled in production.
When enabled, it will leak information about the ASP.NET version your website uses. ASP.NET is a web framework to make it easier to build websites and web applications.

best value: **disable this header!**

### x-aspnetmvc-version
Similar to x-aspnet-version, this header will also leak information about the version of the ASP.NET MVC website.
This header should also be disabled when in production.

best value: **disable this header!**


## Sources

[loginradius - HTTP Security Headers](https://www.loginradius.com/blog/engineering/http-security-headers/#:~:text=Why%20HTTP%20Security%20Headers%20are,code%20injection%2C%20clickjacking%2C%20etc.)

[GeeksforGeeks - HTTP headers](https://www.geeksforgeeks.org/http-headers/)

[developer Mozilla - HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
