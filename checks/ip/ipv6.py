import dns.resolver
import sys

DOMAIN = sys.argv[1]

try:
    result = dns.resolver.resolve(DOMAIN, 'AAAA')
except:
    print(f'{{"name": "IPv6", "score": 0, "message": "Domain: {DOMAIN} does not have an IPv6 address."}}')
    exit()

for ipval in result:
    print(ipval)
    print(f'{{"name": "IPv6", "score": 10, "message": "Domain: {DOMAIN} has an IPv6 address: {ipval}."}}')
