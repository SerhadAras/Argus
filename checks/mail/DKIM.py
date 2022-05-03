#!/usr/bin/python3
import sys
import dns.resolver
import json
import os

def main(domain: str):
    """main.

    Args:
        domain (str): domain
    """
    if os.environ.get("MX") is None:
        print("{}")
        return

    # Load possible selectors
    with open("./dkim-selectors.txt") as file:
        selectorList = list(map(str.strip, file.readlines()))

    # Append domain specific selectors
    selectorList.append(domain.replace(".", ""))
    selectorList.extend(domain.split(".")[:-1])

    # Print test results
    print(json.dumps(dkimTest(domain, selectorList)))

def dkimTest(domain: str , selectorList: list) -> dict:
    """Test if a DKIM record is found for a specific domain.

    Returns:
        dict: A result object.
    """

    # Check if a DKIM selector is found
    hasDKIM = False
    for selector in selectorList:
        try:
            test_dkims = dns.resolver.resolve(selector + '._domainkey.' + domain , 'TXT')
            hasDKIM = True
            break
        except:
            pass

    if hasDKIM:
        result = {"name": "Mail: DKIM", "score": 10, "message": "DKIM record found.", "description": "DKIM"}
    else:
        result = {"name": "Mail: DKIM", "score": 0, "message": "No DKIM record found.", "certain": False, "description": "DKIM"}

    return result

if __name__ == "__main__":
    main(sys.argv[2])
