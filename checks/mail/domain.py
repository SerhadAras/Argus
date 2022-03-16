#!/usr/bin/python3
import argparse
import json
import requests

parser = argparse.ArgumentParser(description='start sub domain lookup.')
parser.add_argument('domain', help='Domain name to test')
args = parser.parse_args()
domain = args.domain
subdomarr=[]
discsubdom=[]
with open("subdomain.txt") as bestand:
    for line in bestand:
        word=line.strip()
        subdomarr.append(word)
for sub in subdomarr:
    urlpath=f"http://{sub}.{domain}"
    print(f"[+]deze path word vertaald naar: {urlpath}")
    try:
        requests.get(urlpath)
    except requests.ConnectionError:
        pass
    else:
        discsubdom.append(urlpath)
print(discsubdom)
