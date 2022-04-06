import sys
from subprocess import Popen, DEVNULL
import json

VERSIONS = ["1.3", "1.2", "1.1", "1.0"]

def main(domain: str):
    """main.

    Args:
        domain (str): domain
    """
    acceptedVersions = []

    for version in VERSIONS:
        curl = Popen(["curl", "-k", "-L", "--tls-max", version, "--tlsv" + version, domain], stdout=DEVNULL, stderr=DEVNULL)
        code = curl.wait()

        if code == 0:
            acceptedVersions.append(version)

    if "1.0" in acceptedVersions:
        print(json.dumps({
            "name": "supported protocols",
            "score": 0,
            "message": "TLSv1.0 is supported, capped at 0/10."
        }))
    elif "1.1" in acceptedVersions:
        print(json.dumps({
            "name": "supported protocols",
            "score": 7,
            "message": "TLSv1.1 is supported, capped at 7/10."
        }))
    else:
        print(json.dumps({
            "name": "supported protocols",
            "score": 10,
            "message": "Only TLSv1.3 and/or TLSv1.2 are supported."
        }))

if __name__ == "__main__":
    main(sys.argv[1])
