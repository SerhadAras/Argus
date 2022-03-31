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
                    print(f'{{"name": "Certificate", "score": 5, "message": "The certificate of {hostname} expires in less than 50 days: {delta.days}."}}')
                elif delta.days > 50:
                    print(f'{{"name": "Certificate", "score": 10, "message": "The certificate of {hostname} expires in {delta.days} days."}}')
    except:
        print(f'{{"name": "Certificate", "score": 0, "message": "The certificate of {hostname} is expired."}}')

if __name__ == '__main__':
    DOMEIN = sys.argv[1]
    getDays(DOMEIN)
