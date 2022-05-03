#!/usr/bin/env python3

import re
import sys
import json

import http.client
from urllib.parse import urlparse

import ssl

def main(target: str):
    """main.

    Args:
        domain (str): domain
    """
    headerPatterns = loadPatterns()
    headers = getHeaders("https://" + target)

    print(json.dumps(checkHeaders(headers, headerPatterns)))

def loadPatterns() -> dict:
    """Load header patterns from file.

    Returns:
        dict: A dictionary with all header patterns.
    """
    with open("./headers.json") as jsonFile:
        return json.load(jsonFile)

def getHeaders(url: str):
    """Get the headers from a web request.

    Args:
        url (str): The url to download from.
    """

    parsedUrl = urlparse(url)
    scheme = parsedUrl[0]
    hostname = parsedUrl[1]
    path = parsedUrl[2]

    if scheme == "https":
        ctx = ssl._create_stdlib_context()
        conn = http.client.HTTPSConnection(hostname, context = ctx)
    else:
        conn = http.client.HTTPConnection(hostname)
    try:
        conn.request("HEAD", path)
        res = conn.getresponse()
        headers = buildHeaderDict(res.getheaders())
    except ssl.SSLCertVerificationError:
        return getHeaders(url.replace("https://", "http://", 1))
    except Exception as err:
        print("{}")
        sys.exit(0)
        return {}

    if (res.status >= 300 and res.status < 400):
        return getHeaders(headers["location"])

    return headers

def buildHeaderDict(headers: list) -> dict:
    """Build a dictionary from a header list

    Args:
        headers (list): A list with headers.

    Returns:
        dict: The dictionary with headers.
    """
    headerDict = {}

    for header in headers:
        headerDict[header[0].lower()] = header[1]

    return headerDict

def checkHeaders(headers: dict, patterns: dict) -> list:
    """Check the headers against a header pattern.

    Args:
        headers (dict): Header map
        patterns (dict): Pattern map

    Returns:
        list: A list of results.
    """
    results = []

    for headerKey in patterns:
        pattern = patterns[headerKey]

        if headerKey not in headers and pattern["present"] is True:
            results.append({
                "name": headerKey,
                "score": 0,
                "message": f"{headerKey} should be present.",
                "description": "headers"
            })
        elif headerKey in headers:

            valueTest = False
            for value in pattern['values']:
                if len(re.findall(value['pattern'].lower(), headers[headerKey].lower())) > 0:
                    results.append({
                        "name": headerKey,
                        "score": value['score'],
                        "value": headers[headerKey],
                        "description": "headers"
                    })
                    valueTest = True
                    break

            if pattern['present'] is False and not valueTest:
                results.append({
                    "name": headerKey,
                    "score": 0,
                    "message": f"{headerKey} shoud be absent.",
                    "value": headers[headerKey],
                    "description": "headers"
                })
            elif not valueTest and pattern['present'] is None:
                results.append({
                    "name": headerKey,
                    "score": 10,
                    "value": headers[headerKey],
                    "description": "headers"
                })
            elif not valueTest:
                results.append({
                    "name": headerKey,
                    "score": 0,
                    "value": headers[headerKey],
                    "description": "headers"
                })

        elif headerKey not in headers and pattern["present"] is False:
            results.append({
                "name": headerKey,
                "score": 10,
                "description": "headers"
            })
        elif pattern['present'] is None:
            results.append({
                "name": headerKey,
                "score": 10,
                "description": "headers"
            })

    return results

if __name__ == "__main__":
    main(sys.argv[2])
