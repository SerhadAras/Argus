#!/usr/bin/python3
import argparse
import json
import dns.resolver
import os

parser = argparse.ArgumentParser(description = 'Simple DMARC quick test.')
parser.add_argument('domain', help = 'Domain name to test')
args = parser.parse_args()
domain = args.domain

def dmarcTest(domain):
    """Test if a DMARC record is found for a specific domain.

    Returns:
        dict: A result object.
    """
    try:
        test_dmarc = dns.resolver.resolve('_dmarc.' + domain , 'TXT')

        for dns_data in test_dmarc:

            if 'DMARC1' in str(dns_data):
                result = {"name": "Mail: DMARC", "score": 10, "message": "DMARK record found."}
                return result

    except:
        result = {"name": "Mail: DMARC", "score": 0, "message": "No DMARC record found."}
        return result

envvar = os.environ.get("MX")
if envvar is not None:
    result = dmarcTest(domain)
    jsonresult = json.dumps(result)
else:
    jsonresult = {}
print(jsonresult)
