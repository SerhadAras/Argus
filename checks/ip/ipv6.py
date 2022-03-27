import dns.resolver
import sys

DOMAIN = sys.argv[1]

try:
    result = dns.resolver.resolve(DOMAIN, 'AAAA')
except:
    print(f'{{"name": "ipv6", "score": 0, "message": "Uw domein {DOMAIN} heeft GEEN ipv6-adres."}}')
    exit()

for ipval in result:
    print(ipval)
    print(f'{{"name": "ipv6", "score": 10, "message": "Uw domein {DOMAIN} heeft een ipv6-adres: {ipval}"}}')
