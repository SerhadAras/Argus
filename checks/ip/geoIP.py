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
        print("No IP address found for this domain.", file=sys.stderr)
        sys.exit()

    with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
        try:
            response = reader.city(ip)
        except:
            print("IP address not found in the database.", file=sys.stderr)
            sys.exit()

        country = response.country.iso_code
        eu_country = ["BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES", "FR", "HR", "IT", "CY",
                      "LV", "LT", "LU", "HU", "MT", "NL", "AT", "PL", "PT", "RO", "SI", "SK", "FI", "SE", "UK"]

        is_eu_land = False
        for i in eu_country:
            if i == country:
                is_eu_land = True
        if is_eu_land:
            print(f'{{"name": "GeoIP", "score": 10, "message": "Website hosted inside Europe, country: {country}."}}')

        elif not is_eu_land:
            print(f'{{"name": "GeoIP", "score": 0, "message": "Website not hosted inside Europe, country: {country}."}}')

if __name__ == "__main__":
    domain = sys.argv[1]
    main(domain)
