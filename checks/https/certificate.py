from datetime import datetime, timezone
import socket
import ssl
import sys
import OpenSSL
import json
import requests

headers = {
    'User-Agent': 'argus'
}

def main(hostname: str, port: str = '443') -> int:
    """
    Get the validity of a certificate (expiration & trusted).
    """
    results = []

    try:
        requests.get(f"https://{hostname}:{port}",headers=headers)
        results.append({
            "name": "valid",
            "score": 10,
            "message": "This website uses a valid certificate.",
            "description": "certificate"
        })
    except requests.exceptions.SSLError:
        results.append({
            "name": "valid",
            "score": 0,
            "message": "This website uses an invalid certificate.",
            "description": "certificate"
        })
    except:
        print("{}")
        return

    context = ssl._create_unverified_context()
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:

                raw_cert = ssock.getpeercert(True)
                raw_cert = ssl.DER_cert_to_PEM_cert(raw_cert)
                cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, raw_cert)

                expiry_date = datetime.strptime(cert.get_notAfter().decode('utf-8'), '%Y%m%d%H%M%S%z')

                days = (expiry_date - datetime.now(timezone.utc)).days

                if days > 0:
                    results.append({
                        "name": "expiration",
                        "score": 10,
                        "message": "Certificate is not expired.",
                        "description": "certificate"
                    })

                else:
                    results.append({
                        "name": "expiration",
                        "score": 0,
                        "message": f"Certificate is expired with {-1 * days}.",
                        "description": "certificate"
                    })

    finally:
        print(json.dumps(results))

if __name__ == '__main__':
    DOMAIN = sys.argv[1]
    main(DOMAIN)
