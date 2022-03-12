#! /usr/bin/env python3

import os
import sys
import requests
import urllib.request
from optparse import OptionParser
import socket

# define exit codes
ExitOK = 0
ExitWarning = 1
ExitCritical = 2
ExitUnknown = 3
default = "8.8.8.8"


def testdnssec(domain):
    """Test if DNSSEC is enabled for a specific domain.

    Args:
        domain (str): Input options.
    """
    if domain:
        try:
            socket.gethostbyname_ex(domain)
            num = True
        except:
            num = False
        if not num:
            try:
                domain = ("www.%s"%domain)
                socket.gethostbyname_ex(domain)
            except:
                print("Unable to resolve %s"%domain, file=sys.stderr)
                sys.exit(ExitUnknown)

        dig_requests = os.popen('dig @%s %s +noall +comments +dnssec'%(default, domain)).read()
        if "ad;" in dig_requests:
            ad_flag = 1
        else:
            ad_flag = 0
        if "SERVFAIL," in dig_requests:
            status_error = 1
        else:
            status_error = 0
        if "NOERROR," in dig_requests:
            status_noerror = 1
        else:
            status_noerror = 0

        if ad_flag == 1 and status_noerror == 1:
            print('{"name": "DNSSEC", "score": 10/10, "message": "The domain %s is safe because it use a valid DNSSEC."}'%domain)
            sys.exit(ExitOK)
        elif status_error == 1:
            print('{"name": "DNSSEC", "score": 5/10, "message": "The domain %s uses DNSSEC, but this is invalid or misconfigured."}'%domain)
            sys.exit(ExitWarning)
        elif status_noerror == 1 and ad_flag == 0:
            print('{"name": "DNSSEC", "score": 0, "message": "Domain %s does not use DNSSEC"}'%domain)
            sys.exit(ExitCritical)
        else:
            print('{"name": "DNSSEC", "score": 0, "message": "Cannot read the result"}')
            sys.exit(ExitUnknown)
    else:
        print ('{"name": "DNSSEC", "score": 0, "message": "Impossible to check domains"}')
        sys.exit(ExitUnknown)

def main():
    """Main function
    """
    domain = sys.argv[1]
    testdnssec(domain)


if __name__ == '__main__':
    main()
