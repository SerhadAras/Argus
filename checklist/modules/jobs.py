import os
import json
import requests

URL = os.environ.get("SEQUENCER_URL") + "/api/v1/"
TLS = os.getenv("TLS_ENABLED", "TRUE").lower() == "true"

CERT = os.environ.get("CERT_PATH")
KEY = os.environ.get("KEY_PATH")
CA = os.environ.get("CA_PATH")

def requestJob(name: str, flowTags) -> dict | None:
    """Request a job from a sequencer server.

    Args:
        name (str): The checklist name.
        flowTags : the tags of the current flow

    Returns:
        dict: The job request or None when no jobs are available.
    """
    if TLS:
        res = requests.get(URL + f"job/{name}", cert=(CERT, KEY), verify=CA)
    else:
        res = requests.get(URL + f"job/{name}")

    if res.status_code == 200:
        return json.loads(res.text)

    return None

def pushResults(results: dict) -> bool:
    """Push flow results to a sequencer server.

    Args:
        results (dict): The dict to push to the server.

    Returns:
        bool: Has the push been successfull.
    """
    if TLS:
        res = requests.post(URL + "results", json=results, cert=(CERT, KEY), verify=CA)
    else:
        res = requests.post(URL + "results", json=results)

    return req.status_code == 201

def pushBack(check: dict):
    """"
    push job back in the reddis queue
    """
    if TLS:
        res = requests.post(URL + "pushback", json=check, cert=(CERT, KEY), verify=CA)
    else:
        res = requests.post(URL + "pushback", json=check)

def advertise(advert: dict):
    """"
    push advertisements in redis queue
    """
    if TLS:
        res = requests.post(URL + "advertise", json=advert, cert=(CERT, KEY), verify=CA)
    else:
        res = requests.post(URL + "advertise", json=advert)

    return res.status_code == 201
