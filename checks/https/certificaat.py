import datetime
import socket
import ssl
import sys
def getDays(hostname: str, port: str = '443') -> int:
    """
    Get number of days before an TLS/SSL of a domain expired
    """
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssl_info = ssock.getpeercert()
                expiry_date = datetime.datetime.strptime(ssl_info['notAfter'], '%b %d %H:%M:%S %Y %Z')
                delta = expiry_date - datetime.datetime.utcnow()
                if delta.days <= 50:
                    print(f'{{"name": "certificaat", "score": 5, "message": "De certificaat van {hostname} verloopt binnen {delta.days} dagen. Vervaldatum: {expiry_date}."}}')
                elif delta.days > 50:
                    print(f'{{"name": "certificaat", "score": 10, "message": "De certificaat van {hostname} verloopt binnen {delta.days} dagen. Vervaldatum: {expiry_date}."}}')
    except:
        print(f'{{"name": "certificaat", "score": 0, "message": "De certificaat van {hostname} is verlopen."}}')

if __name__ == '__main__':
    DOMEIN = sys.argv[1]
    getDays(DOMEIN)
