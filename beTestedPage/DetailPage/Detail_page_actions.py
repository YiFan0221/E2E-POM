#Detail
import sys,os
sys.path.append(os.getcwd())

from base_page import *
from browser_drivers.browser_helper import *
from beTestedPage.DetailPage.Detail_page_locators import cDetailPagelocators

#==================================== Class =======================================
class cDetailPage(BasePage,cDetailPagelocators):

    def __init__(self,driver):
         BasePage.__init__(self,driver) 
         cDetailPagelocators.__init__(self)

    def get_Detail_page(self):
        url = "http://172.17.12.25:5000/camera/settings"
        self.get_page(url)
        #self.wait_for_browser_title("OOXX")

#================================== 跳頁方法 =========================================

    def click_Button_HomePage(self):
        self.find_element(self.Button_HomePage.elemt).click()
        self.wait_page_until_loading()
        #跳頁表示需換到另外一個類別進行控制
        RobotDataStore.set_env_var("Project_driver", self.driver)
        time.sleep(5)
        
#==================================== Adapter & Launch =======================================
#Get&Set PageObj from env var
def set_Detail_page_obj(SrcObj):
    RobotDataStore.set_env_var("Detail_page_obj",SrcObj)

def get_Detail_page_obj()->cDetailPage:
    
    try:
        Detail_page = RobotDataStore.get_env_var("Detail_page_obj")
        return Detail_page
    except KeyError:
        return False
    
#Launch
def Init_Detail_page(browser_type)->cDetailPage:
    browser_map = {
        "chrome": get_chrome_driver,
       "firefox": get_firefox_driver
    }
    if browser_type not in browser_map:
        raise ValueError("Browser type error")
    Detail_driver = browser_map[browser_type]()
    Detail_page_obj = cDetailPage(Detail_driver)
    set_Browser_driver(Detail_driver)
    set_Detail_page_obj(Detail_page_obj)
    return Detail_page_obj

#Adapter
#從driver植入一個物件存入RobotDataStore
def setup_Detail_page():
    Detail_driver = get_Browser_driver()
    Detail_page_obj = cDetailPage(Detail_driver)
    RobotDataStore.set_env_var("Detail_page_obj", Detail_page_obj)

