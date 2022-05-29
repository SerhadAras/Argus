#! /usr/bin/env python3
import re
import sys
import json
import dns.resolver
import geoip2.database


def main(target, type):
    """main.

    Args:
        target (str): The target to check.
        type (str): The target type.
    """
    targets = []
    results = []

    if type == "domain":
        targets = resolve(target)
    elif type == "ip":
        targets.append(target)
    else:
        print("{}")
        exit()

    with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
        for ip in targets:
            results.append(checkIp(ip, reader))

    print(json.dumps(results))

def resolve(domain: str):
    """Resolve a domain to a set of ip addresses.
    """
    ips = []
    try:
        result = dns.resolver.resolve(domain)
        for ipVal in result:
            ips.append(ipVal.to_text())
        return ips
    except:
        print("{}")
        sys.exit(0)


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
            "message": "The ip address is hosted in the EU.",
            "info": [ip],
            "description": "geoIP"
        }
    elif not is_eu_land:
        return {
            "name": "GeoIP",
            "score": 0,
            "message": "The ip address is not hosted in the EU.",
            "info": [ip],
            "description": "geoIP"
        }

if __name__ == "__main__":
    main(sys.argv[2], sys.argv[1])
