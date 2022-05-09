import os
import sys
import json
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SELENIUM_URL = os.environ.get("SELENIUM_URL")

if SELENIUM_URL is None or SELENIUM_URL == "":
    print("{}")
    exit()

def checkCookies(driver, target, https = True):
    """
    Args:
        driver (selenium.webdriver.Remote): The selenium web driver
        target (str): The target to check
        https (bool): Use https
    """

    if https:
        url = 'https://' + target
    else:
        url = 'http://' + target

    try:
        driver.get(url)
    except:
        if not https:
            # If not https no connection can be made
            #   no results should be returned.
            print("{}")
            return
        else:
            # Try http
            return checkCookies(driver, target, False)


    time.sleep(5)
    cookies = driver.get_cookies()

    cookieDomain = driver.execute_script("return location.hostname")

    domains = []
    names = []

    for array in cookies:
        names.append(array.get("name"))
        domains.append(array.get("domain"))

    for domain in domains:
        if cookieDomain not in domain and domain not in cookieDomain:
            print(json.dumps({
                "name": "third party",
                "score": 0,
                "message": "The website loads third party cookies without consent.",
                "description": "third_party"
            }))
            return

    print(json.dumps({
        "name": "third party",
        "score": 10,
        "message": "The website does not load third party cookies.",
        "description": "third_party"
    }))

def main():
    """Main function
    """

    type = sys.argv[1]
    target = sys.argv[2]

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.set_capability("loggingPrefs", {'performance': 'ALL'})
    driver = webdriver.Remote(SELENIUM_URL + '/wd/hub', options=options)

    try:
        checkCookies(driver, target)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
