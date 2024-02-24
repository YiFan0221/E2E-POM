import os
import platform
import pathlib
import sys,os
sys.path.append(os.getcwd())

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config_helper import ConfigHelper

def get_this_path():
    return str(pathlib.Path(__file__).parent.absolute())


def Get_chrome_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def Get_firefox_driver():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver
