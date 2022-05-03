#!/usr/bin/python3

import os
import sys
import json
import dns.resolver

def mxTest(domain: str) -> dict:
    """Test if MX record found to start new stage

    Args:
        domain (str): The domain to check.

    Returns:
        dict: Output object
    """
    try:
        for x in dns.resolver.resolve(domain, 'MX'):
            res = {"output":{"MX":"TRUE"}}
            return res
    except:
        res = {}

    return res

if __name__ == "__main__":
    print(json.dumps(mxTest(sys.argv[2])))
