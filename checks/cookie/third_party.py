import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SELENIUM_URL = os.environ.get("SELENIUM_URL")

if SELENIUM_URL is None or SELENIUM_URL == "":
    print("{}")
    exit()

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.set_capability("loggingPrefs", {'performance': 'ALL'})
driver = webdriver.Remote(SELENIUM_URL + '/wd/hub', options=options)

DOMAIN = sys.argv[1]
url = 'http://' + DOMAIN

driver.get(url)

time.sleep(5)

cookies = driver.get_cookies()

driver.close()
driver.quit()

domeinen = []
namen = []

for array in cookies:
    namen.append(array.get("name"))
    domeinen.append(array.get("domain"))

for domein in domeinen:
    if DOMAIN not in domein and domein not in DOMAIN:
        print('{{"name": "third party", "score": 0, "message": "Uw website %s maakt gebruik van third party cookies %s.}}' % (url, domein))
        exit()

print('{{"name": "third party", "score": 10, "message": "Uw website %s maakt GEEN gebruik van third party cookies.}}' % (url))
