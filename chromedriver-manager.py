import os
import stat
import shutil
import locale
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

webdriver_path = ChromeDriverManager().install()

if not os.path.basename(webdriver_path) == 'chromedriver':
    webdriver_path = os.path.join(os.path.dirname(webdriver_path), 'chromedriver')

os.chmod(webdriver_path, stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

driver = webdriver.Chrome(service=Service(webdriver_path))

version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

destination_path = '/usr/local/bin/chromedriver'

shutil.move(webdriver_path, destination_path)

system_lang = locale.getlocale()[0]

if system_lang.startswith('zh'):
    print(f"已更新 ChromeDriver 至 {version} 版本")
else:
    print(f"ChromeDriver has been updated to version {version}")

driver.quit()
