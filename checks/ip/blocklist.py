import sys
import json
import queue
import random
import threading
import dns.resolver

jobQueue = queue.Queue()
blocked = []

def main(target, type):
    """main.

    Args:
        target (str): The target to check.
        type (str): The target type.
    """

    targets = []

    if type == "domain":
        targets = resolve(target)
    elif type == "ip":
        targets.append(target)
    else:
        print("{}")
        exit()

    run(targets)

def resolve(domain: str):
    """Resolve a domain to a set of ip addresses.
    """
    ips = []
    try:
        result = dns.resolver.resolve(domain)
        for ipVal in result:
            ips.append(ipVal.to_text())
        return ips
    except:
        print("{}")
        sys.exit(0)

def run(targets: list):
    """main.

    Args:
        targets (list): A list of target ip addresses to check.
    """
    results = []
    threads = []

    blocklists = readBlocklists()

    # Enqueue target
    for blocklist in blocklists:
        for ip in targets:
            jobQueue.put((ip, blocklist))

    for i in range(100):
        threads.append(threading.Thread(target=checkThread, daemon=True))

    for thread in threads:
        thread.start()

    jobQueue.join()

    if len(blocked) > 0:
        blockedIps = {}
        for ip, blocklist in blocked:

            try:
                targets.remove(ip)
            except ValueError:
                pass

            if ip not in blockedIps:
                blockedIps[ip] = []
                blockedIps[ip].append(blocklist)
            else:
                blockedIps[ip].append(blocklist)

        for ip in blockedIps:
            results.append({
                "name": "Blocklists",
                "score": 0,
                "message": f"{ip} is found on a blocklist.",
                "value": blockedIps[ip],
                "description": "blacklist"
            })


    for ip in targets:
        results.append({
            "name": "Blocklists",
            "score": 10,
            "message": f"{ip} is not found on a blocklist.",
            "value": ip,
            "description": "blacklist"
        })

    print(json.dumps(results))

def readBlocklists() -> list:
    """Read the blocklists list from file.

    Returns:
        list: A list of blocklists.
    """
    with open("./blocklists.txt") as file:
        blocklists =  list(map(str.strip, file.readlines()))
        random.shuffle(blocklists)
        return blocklists

def checkThread():
    """Checking thread
    """
    while not jobQueue.empty():
        ip, blocklist = jobQueue.get()

        try:
            result = dns.resolver.resolve("%s.%s" % (ip, blocklist))
            for ipVal in result:
                if "127.0.0." in ipVal.to_text():
                    blocked.append((ip, blocklist))
        except:
            pass
        finally:
            jobQueue.task_done()

if __name__ == "__main__":
    main(sys.argv[2], sys.argv[1])
