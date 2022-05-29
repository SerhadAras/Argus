import json
import socket, sys, ssl

target = sys.argv[2]
context = ssl._create_unverified_context()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslSocket = context.wrap_socket(s, server_hostname = target)

try:
    sslSocket.connect((target, 443))
except:
    print({})
    sslSocket.close()

else:
    versie = sslSocket.version()
    if "TLSv1.2" in versie or "TLSv1.3" in versie:
        print(json.dumps(
            {   "name": "Protocol",
                "score": 10,
                "message": "This domain uses version: "+ str(versie)+".",
                "description": "protocol"
            }))
    else:
        print(json.dumps(
            {
                "name": "Protocol",
                "score": 0,
                "message": "This domain uses version: "+str(versie)+", TLS version 1.2 or up required.",
                "description": "protocol"
            }))
    sslSocket.close()
