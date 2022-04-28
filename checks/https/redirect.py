#! /usr/bin/env python3

from urllib import request
import requests
import sys

import urllib3

DOMAIN = sys.argv[1]
url = 'http://' + DOMAIN
HTTPS = "https"
urllib3.disable_warnings()

try:
    res = requests.get(url, verify=False)
except:
    print({})
else:
    new_url = res.url
    if HTTPS in new_url:
        print(f'{{"name": "Redirect HTTP", "score": 10, "message": "Redirection from http to https present: {url} to {new_url}.", "description": "redirect"}}')
    else:
        print(f'{{"name": "Redirect HTTP", "score": 0, "message": "No redirection from http to https present.", "description": "redirect"}}')
