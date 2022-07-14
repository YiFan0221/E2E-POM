#OverTime Project
import sys,os
sys.path.append(os.getcwd())

from base_page import *
from browser_drivers.browser_helper import *
from beTestedPage.Overtime.Overtime_page_locators import cOverTimePagelocators

#==================================== Class =======================================
class cPage(BasePage,cOverTimePagelocators):

    def __init__(self,driver):
         BasePage.__init__(self,driver) 
         cOverTimePagelocators.__init__(self)

    def get_page(self):
        url = "https://employeezone.advantech.com.tw/net/Account/Login?ReturnUrl=%2fnet"
        self.get_page(url)
        #self.wait_for_browser_title("OOXX")

#================================== 跳頁方法 =========================================

    def click_Button_HomePage(self):
        self.find_element(self.Button_HomePage.elemt).click()
        self.wait_page_until_loading()
        #跳頁表示需換到另外一個類別進行控制
        RobotDataStore.set_env_var("OverTime_driver", self.driver)
        time.sleep(5)
        
#==================================== Adapter & Launch =======================================
#Get&Set PageObj from env var
def set_page_obj(SrcObj):
    RobotDataStore.set_env_var("OverTime_page_obj",SrcObj)

def get_page_obj()->cPage:
    
    try:
        rtn_page = RobotDataStore.get_env_var("OverTime_page_obj")
        return rtn_page
    except KeyError:
        return False
    
#Launch
def Init_page(browser_type)->cPage:
    browser_map = {
        "chrome": get_chrome_driver,
       "firefox": get_firefox_driver
    }
    if browser_type not in browser_map:
        raise ValueError("Browser type error")
    Page_driver = browser_map[browser_type]()
    Page_obj = cPage(Page_driver)
    set_Browser_driver(Page_driver)
    set_page_obj(Page_obj)
    return Page_obj

#Adapter
#從driver植入一個物件存入RobotDataStore
def setup_page():
    Page_driver = get_Browser_driver()
    Page_obj = cPage(Page_driver)
    set_page_obj(Page_obj)

