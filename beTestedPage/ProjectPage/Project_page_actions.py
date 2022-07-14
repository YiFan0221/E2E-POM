#Project
import re
import sys,os

from numpy import NaN
sys.path.append(os.getcwd())

from base_page import *
from browser_drivers.browser_helper import *
from beTestedPage.ProjectPage.Project_page_locators import cProjectPageLocators

#==================================== Class =======================================
class cProjectPage(BasePage,cProjectPageLocators):
    
    def __init__(self,driver):
         BasePage.__init__(self,driver) 
         cProjectPageLocators.__init__(self)

    def get_Project_page(self):
        url = "http://172.17.12.25:5000/"
        self.get_page(url)
        #self.wait_for_browser_title("OOXX)

#================================== 跳頁方法 =========================================

    def click_Button_Next(self):
        self.find_element(self.Button_Next.elemt).click()
        self.wait_page_until_loading()
        #跳頁表示需換到另外一個類別進行控制
        Detail_driver = self.driver
        RobotDataStore.set_env_var("Detail_driver", Detail_driver)
        time.sleep(5)

#==================================== Delete Project =======================================    
    def delete_Specific_Project(self,ProjectNo):
        btnDel_Xpath = '/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[{}]/td[6]/div/div[1]/button'.format(ProjectNo)

        try:
            btnDelete = self.driver.find_element(By.XPATH,btnDel_Xpath)
            btnDelete.click()
            btnDel_Xpath = '/html/body/div[{}]/div/div[6]/button[1]'.format(ProjectNo)
            btnDelete = self.driver.find_element(By.XPATH,btnDel_Xpath)
            btnDelete.click()
            btnOK_Xpath = "/html/body/div[{}]/div/div[6]/button[1]".format(ProjectNo)
            btnOK = self.driver.find_element(By.XPATH,btnOK_Xpath)
            btnOK.click()
            return True
        except:
            logging.debug('GetTable warning.')
            return None
    
#==================================== Adapter & Launch =======================================

#Get&Set PageObj from env var
def set_project_page_obj(SrcObj):
    RobotDataStore.set_env_var("Project_page_obj",SrcObj)

def get_project_page_obj()->cProjectPage:
    try:
        project_page = RobotDataStore.get_env_var("Project_page_obj")        
        return project_page 
    except KeyError:
        return False

#Launch
def Init_Project_page(browser_type)->cProjectPage:
    browser_map = {
        "chrome": get_chrome_driver,
        "firefox": get_firefox_driver
    }
    if browser_type not in browser_map:
        raise ValueError("Browser type error")
    Project_driver = browser_map[browser_type]()
    Project_page_obj = cProjectPage(Project_driver)
    set_Browser_driver(Project_driver)
    set_project_page_obj(Project_page_obj)
    return Project_page_obj

#Adapter
#從driver植入一個物件存入RobotDataStore
def setup_Project_page():
    Project_driver = get_Browser_driver()
    Project_page_obj = cProjectPage(Project_driver)
    set_project_page_obj(Project_page_obj)    