#!/usr/bin/python3
import argparse
import dns.resolver
import json
import os

parser = argparse.ArgumentParser(description = 'Simple DKIM quick test.')
parser.add_argument('domain', help = 'Domain name to test')
args = parser.parse_args()
domain = args.domain

listselectors = ["selector1","selector2","google","everlytickey1","everlytickey2","eversrv","k1","mxvault","dkim","default"]

listselectors.append(domain.replace(".", ""))
listselectors.extend(domain.split(".")[:-1])

for selector in listselectors:
    try:
        test_dkims = dns.resolver.resolve(selector + '._domainkey.' + domain , 'TXT')
        break
    except:
        pass

def dkimTest():
    """Test if a DKIM record is found for a specific domain.

    Returns:
        dict: A result object.
    """
    try:
        test_dkim = test_dkims
        for dns_data in test_dkim:

            if 'DKIM1' in str(dns_data):
                result = {"name": "Mail: DKIM", "score": 10, "message": "DKIM record found."}
                return result

    except:
        result = {"name": "Mail: DKIM", "score": 0, "message": "No DKIM record found.", "certain": False}
        return result

envvar = os.environ.get("MX")
if envvar is not None:
    result = dkimTest()
    jsonresult = json.dumps(result)
else:
    jsonresult = {}
print(jsonresult)
