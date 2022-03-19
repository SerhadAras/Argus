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
        print(f'{{"name": "redirect", "score": 10, "message": "Alle potentieel onveilige verkeer via {url}, wordt veilig doorgestuurd naar {new_url}"}}')
    else:
        print(f'{{"name": "redirect", "score": 0, "message": "Uw website {url} is bereikbaar via het onbeveiligde http, dit betekent dat in bepaalde gevallen bezoekers onversleuteld gegevens naar uw website kunnen doorsturen. Misschien kan u een redirectie naar https opzetten?"}}')
