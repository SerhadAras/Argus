#!/usr/bin/python3
import argparse
import dns.resolver
import json
import os

parser = argparse.ArgumentParser(description = 'Simple MX quick test.')
parser.add_argument('domain', help = 'Domain name to test')
args = parser.parse_args()
domain = args.domain

def mxTest(domain):
    """Test if MX record found to start new stage

    Args:
        domain (any): you need give domain to the check
    Returns:

        json: decide to start other checks
    """
    try:
        for x in dns.resolver.resolve(domain, 'MX'):
            res = {"output":{"MX":"TRUE"}}
            return res
    except:
        res = {}
    return res

response = mxTest(domain)
jsonresult = json.dumps(response)
print(jsonresult)
