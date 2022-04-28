import socket, sys, ssl

DOMAIN = sys.argv[1]
context = ssl._create_unverified_context()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslSocket = context.wrap_socket(s, server_hostname = DOMAIN)

try:
    sslSocket.connect((DOMAIN, 443))
except:
    print({})
    sslSocket.close()

else:
    versie = sslSocket.version()
    if "TLSv1.2" in versie or "TLSv1.3" in versie:
        print(f'{{"name": "Protocol", "score": 10, "message": "Domain {DOMAIN} uses version: {versie}.", "description": "protocol"}}')
    else:
        print(f'{{"name": "Protocol", "score": 0, "message": "Domain {DOMAIN} uses version: {versie}, TLS version 1.2 or up required.", "description": "protocol" }}')
    sslSocket.close()
