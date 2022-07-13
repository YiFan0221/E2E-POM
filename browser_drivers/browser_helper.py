import os
import platform
import pathlib
import sys,os
sys.path.append(os.getcwd())

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options

from config_helper import ConfigHelper



def get_this_path():
    return str(pathlib.Path(__file__).parent.absolute())


def get_chrome_driver():
    #https://chromedriver.chromium.org/home
    #可以針對三種OS去取用
    driver_bin_map = {
        "Windows": "chromedriver.exe",
        "Darwin": "chromedriver",
        "Linux": "chromedriver"
    }
    #driver_path = os.path.join(get_this_path(), driver_bin_map[platform.system()])
    
    driver_path = os.path.join(get_this_path(), driver_bin_map[platform.system()])
    chrome_options = Options()
    chrome_options.add_argument("--lang=zt")
    #加上讀取本地端的cookie
    #chrome_options.add_argument(r'--user-data-dir=C:\\Users\\gary021.hsu\\AppData\\Local\\Google\\Chrome\\User Data')
    #關閉部分警告
    #chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    driver = Chrome(executable_path=driver_path, service_args=["--verbose"], options=chrome_options)
    return driver


def get_firefox_driver():
    driver_bin_map = {
        "Windows": "geckodriver.exe",
        "Darwin": "geckodriver",
        "Linux": "geckodriver"
    }
    driver_path = os.path.join(get_this_path(), driver_bin_map[platform.system()])
    firefox_bin = ConfigHelper().get_firefix_binary_path()
    driver = Firefox(firefox_binary=firefox_bin, executable_path=driver_path)
    return driver
