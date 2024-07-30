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

destination_path = '/usr/local/bin/chromedriver'

if os.path.exists(destination_path):
    system_lang = locale.getlocale()[0]
    driver = webdriver.Chrome(service=Service(destination_path))
    version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
    driver.quit()
    
    if system_lang.startswith('zh'):
        print(f"ChromeDriver {version} 已是最新版本")
    else:
        print(f"ChromeDriver {version} is up to date")

else:
    os.chmod(webdriver_path, stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    system_lang = locale.getlocale()[0]
    driver = webdriver.Chrome(service=Service(webdriver_path))
    version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
    shutil.move(webdriver_path, destination_path)
    driver.quit()

    if system_lang.startswith('zh'):
        print(f"已更新 ChromeDriver 至 {version} 版本")
    else:
        print(f"ChromeDriver has been updated to version {version}")
