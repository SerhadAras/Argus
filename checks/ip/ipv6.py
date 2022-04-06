import sys
import json
import dns.resolver

DOMAIN = sys.argv[1]

try:
    result = dns.resolver.resolve(DOMAIN, 'AAAA')
except:
    print(f'{{"name": "IPv6", "score": 0, "message": "Domain: {DOMAIN} does not have an IPv6 address."}}')
    exit()

ips = []
for ipVal in result:
    ips.append(str(ipVal))


print(json.dumps({
    "name": "IPv6",
    "score": 10,
    "message": f"Domain: {DOMAIN} has one or more IPv6 addresses.",
    "value": ips
}))
