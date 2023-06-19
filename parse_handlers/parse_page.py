import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

service = Service(
    executable_path="/Users/dinar/the-AutoBook/parse_handlers/chromedriver")

options = webdriver.ChromeOptions()
options.add_argument(
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(
    options=options,
    service=service
)

try:
    data = driver.get(
        'https://auto.ru/cars/used/sale/byd/yangwang_u8/1119044316-af02ad39/?')
    time.sleep(20)
    print(data)
except Exception as error:
    print(error)
finally:
    driver.close()
    driver.quit()

# print(year)
