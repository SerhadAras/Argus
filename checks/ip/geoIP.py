#! /usr/bin/env python3
import re
import sys
import json
import dns.resolver
import geoip2.database

def main(domain):
    """Check if a domain is hosted in the EU.

    Args:
        domain (str): The domain to check.
    """
    ips = []
    results = []

    try:
        result = dns.resolver.resolve(domain)
        for ipval in result:
            ips.append(ipval.to_text())
    except:
        print("No IP address found for this domain.", file=sys.stderr)
        sys.exit()

    with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
        for ip in ips:
            results.append(checkIp(ip, reader))

    print(json.dumps(results))


def checkIp(ip: str, reader: geoip2.database.Reader) -> dict:
    """Check if an ip is in the EU.

    Args:
        ip (str): The ip to check
        reader (geoip2.database.Reader): The GeoIP list reader.

    Returns:
        dict: A result.
    """
    try:
        response = reader.city(ip)
    except:
        print("IP address not found in the database.", file=sys.stderr)
        return {}

    country = response.country.iso_code
    eu_country = ["BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES", "FR", "HR", "IT", "CY",
                  "LV", "LT", "LU", "HU", "MT", "NL", "AT", "PL", "PT", "RO", "SI", "SK", "FI", "SE", "UK"]

    is_eu_land = False
    for i in eu_country:
        if i == country:
            is_eu_land = True
    if is_eu_land:
        return {
            "name": "GeoIP",
            "score": 10,
            "message": f"{ip} is hosted in the EU.",
            "value": ip,
            "description": "geoIP"
        }
    elif not is_eu_land:
        return {
            "name": "GeoIP",
            "score": 0,
            "message": f"{ip} is not hosted in the EU.",
            "value": ip,
            "description": "geoIP"
        }

if __name__ == "__main__":
    domain = sys.argv[1]
    main(domain)
