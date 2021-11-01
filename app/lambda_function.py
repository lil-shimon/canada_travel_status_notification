"""app/lambda_function.py
"""
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def lambda_handler(event, context):
    """lambda_handler
    """
    print('event: {}'.format(event))
    print('context: {}'.format(context))

    headless_chromium = os.getenv('HEADLESS_CHROMIUM', '')
    chromedriver = os.getenv('CHROMEDRIVER', '')

    options = Options()
    options.binary_location = headless_chromium
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.get('https://info.finance.yahoo.co.jp/fx/')
    usd_jpy = driver.find_element(By.ID, 'USDJPY_top_bid').text
    driver.close()
    driver.quit()

    return {
        'status_code': 200,
        'usd_jpy': usd_jpy
    }


if __name__ == '__main__':
    print(lambda_handler(event=None, context=None))