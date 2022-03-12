#! /usr/bin/env python3
import string
import geoip2.database
import sys
import dns.resolver
import re



def main(domain):
    """Check if a domain is hosted in the EU.

    Args:
        domain (str): The domain to check.
    """
    try:
        result = dns.resolver.resolve(domain)
        for ipval in result:
            ip = ipval.to_text()
    except:
        print("Er werd geen IP gevonden voor dit domein.", file=sys.stderr)
        sys.exit()

    with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
        try:
            response = reader.city(ip)
        except:
            print("IP werd niet gevonden in database", file=sys.stderr)
            sys.exit()

        country = response.country.iso_code
        eu_country = ["BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES", "FR", "HR", "IT", "CY",
                      "LV", "LT", "LU", "HU", "MT", "NL", "AT", "PL", "PT", "RO", "SI", "SK", "FI", "SE", "UK"]

        is_eu_land = False
        for i in eu_country:
            if i == country:
                is_eu_land = True
        if is_eu_land:
            print(f'{{"name": "geoIP", "score": 10, "message": "Uw website wordt gehost binnen de EU, meer bepaald in {country}"}}')

        elif not is_eu_land:
            print(f'{{"name": "geoIP", "score": 0, "message": "Uw website wordt niet gehost binnen de EU, meer bepaald in {country}, indien je persoonsgegevens verwerkt via je site kan dit problemen rond o.a. GDPR met zich meebrengen. Indien er geen persoonsgegevens verwerkt worden op je site, dan kan je deze score nuanceren."}}')

if __name__ == "__main__":
    domain = sys.argv[1]
    main(domain)
