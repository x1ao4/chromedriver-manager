import os
import stat
import shutil
import locale
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 获取当前 Chrome 浏览器版本
def get_chrome_version():
    options = Options()
    options.add_argument("--headless")  # 避免启动 GUI
    service = Service(ChromeDriverManager().install())  # 先用默认 chromedriver 运行
    browser = webdriver.Chrome(service=service, options=options)
    chrome_version = browser.capabilities['browserVersion']
    browser.quit()
    return chrome_version

# 自动下载匹配的 ChromeDriver 版本
chrome_version = get_chrome_version().split('.')[0]  # 获取主版本号
webdriver_path = ChromeDriverManager().install()  # 让 webdriver-manager 自动选择最佳匹配版本

# 确保路径指向 chromedriver
if not os.path.basename(webdriver_path) == 'chromedriver':
    webdriver_path = os.path.join(os.path.dirname(webdriver_path), 'chromedriver')

destination_path = '/usr/local/bin/chromedriver'

# 删除旧的 chromedriver（如果有）
if os.path.exists(destination_path):
    os.remove(destination_path)

# 赋予执行权限并移动到系统路径
os.chmod(webdriver_path, stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
shutil.move(webdriver_path, destination_path)

# 检查是否更新成功
system_lang = locale.getlocale()[0]
driver = webdriver.Chrome(service=Service(destination_path))
version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
driver.quit()

if system_lang.startswith('zh'):
    print(f"已更新 ChromeDriver 至 {version} 版本")
else:
    print(f"ChromeDriver has been updated to version {version}")
