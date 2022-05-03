#!/usr/bin/python3
import sys
import json
import dns.resolver
import os

def main(domain: str):
    """main.

    Args:
        domain (str): domain
    """
    if os.environ.get("MX") is None:
        print("{}")
        return

    print(json.dumps(dmarcTest(domain)))

def dmarcTest(domain: str) -> dict:
    """Test if a DMARC record is found for a specific domain.

    Returns:
        dict: A result object.
    """
    try:
        test_dmarc = dns.resolver.resolve('_dmarc.' + domain , 'TXT')

        for dns_data in test_dmarc:

            if 'DMARC1' in str(dns_data):
                result = {"name": "Mail: DMARC", "score": 10, "message": "DMARK record found.", "description": "DMARC"}
                return result

    except:
        result = {"name": "Mail: DMARC", "score": 0, "message": "No DMARC record found.", "description": "DMARC"}
        return result

if __name__ == "__main__":
    main(sys.argv[2])
