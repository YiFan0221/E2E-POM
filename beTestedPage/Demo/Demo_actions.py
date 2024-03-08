#Project
import sys,os
sys.path.append(os.getcwd())

from base_page import *
from browser_drivers.browser_helper import *
from beTestedPage.Demo.Demo_locators import cDemoLocators
from selenium.webdriver.common.by import By

#==================================== Class =======================================
class cDemoPage(BasePage,cDemoLocators):
    
    def __init__(self,driver):
         BasePage.__init__(self,driver) 
         cDemoLocators.__init__(self)

    def get_page(self):#一定要建置後並透過物件呼叫
        url = "https://www.saucedemo.com/"
        self.basefunc_get_page(url)
        #self.wait_for_browser_title("OOXX)

#==================================== Adapter & Launch =======================================

#Get&Set PageObj from env var
def set_page_obj(SrcObj):
    RobotDataStore.set_env_var("DemoPage_obj",SrcObj)

def get_page_obj()->(cDemoPage):
    try:
        test_page = RobotDataStore.get_env_var("DemoPage_obj")
        return test_page
    except KeyError:
        return False

#Launch
def Init_page(browser_type)->(cDemoPage):
    browser_map = {
        "chrome": Get_chrome_driver,
        "firefox": Get_firefox_driver
    }
    if browser_type not in browser_map:
        raise ValueError("Browser type error")
    Project_driver = browser_map[browser_type]()
    DemoPage_obj = cDemoPage(Project_driver)
    set_Browser_driver(Project_driver)
    set_page_obj(DemoPage_obj)
    return DemoPage_obj

#Adapter
#從driver植入一個物件存入RobotDataStore
def setup_page():
    Project_driver = get_Browser_driver()
    DemoPage_obj = cDemoPage(Project_driver)
    set_page_obj(DemoPage_obj)    

def login():
    obj = get_page_obj()
    if obj.Check(obj.login_logo):
        obj.SetInputBoxText(obj.user_name, "standard_user")
        obj.SetInputBoxText(obj.password, "secret_sauce")
        obj.Click(obj.bt_login_button)
    else:
        return