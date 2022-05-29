import sys
import json
import dns.resolver


def main(target: str, type: str):
    """main.

    Args:
        target (str): The target to check.
        type (str): The target type.
    """

    if type == "ip":
        print(json.dumps({
            "name": "IPv6",
            "score": 0,
            "message": "This ip address is not a IPv6 address.",
            "description": "ipv6"
        }))
        return
    elif type == "ipv6":
        print(json.dumps({
            "name": "IPv6",
            "score": 10,
            "message": "This ip address is an IPv6 address.",
            "description": "ipv6"
        }))
        return

    try:
        result = dns.resolver.resolve(target, 'AAAA')
    except:
        print(json.dumps({
            "name": "IPv6",
            "score": 0,
            "message": "This ip address is not a IPv6 address.",
            "description": "ipv6"
        }))
        return

    ips = []
    for ipVal in result:
        ips.append(str(ipVal))

    print(json.dumps({
        "name": "IPv6",
        "score": 10,
        "message": "The domain has one or more IPv6 addresses.",
        "info": ips,
        "description": "ipv6"
    }))


if __name__ == "__main__":
    type = sys.argv[1]
    target = sys.argv[2]
    main(target, type)
