import sys
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import ssl


class SSLAdapter(HTTPAdapter):
    """The built-in HTTP Adapter for urllib3."""

    def __init__(self, sslVersion=None, **kwargs):
        self.sslVersion = sslVersion
        super(SSLAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        # pylint: disable=all
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=self.sslVersion)


DOMAIN = "http://" + sys.argv[1]
VERSIONS = [ssl.PROTOCOL_TLSv1, ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2]
badSSL = False

for version in VERSIONS:
    s = requests.Session()
    s.mount("https://", SSLAdapter(version))
    try:
        res = s.get(DOMAIN)
        print(res)
        if version == ssl.PROTOCOL_TLSv1 or version == ssl.PROTOCOL_TLSv1_1:
            badSSL = True
    except requests.exceptions.SSLError:
        print(f'{{"name": "supported Protocol", "score": 0, "certain": false, "message": "No SSL-version found on domain {DOMAIN}." }}')
        quit()
    except:
        print({})
        quit()

if badSSL:
    print(f'{{"name": "Supported Protocol", "score": 0, "message": "Domain {DOMAIN} supports TLS 1.0 or TLS 1.1." }}')
elif not badSSL:
    print(f'{{"name": "Supported Protocol", "score": 10, "message": "Domain {DOMAIN} does not support TLS 1.0 of TLS 1.1"}}')
