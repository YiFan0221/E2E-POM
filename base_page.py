import time
import logging
import sys,os
sys.path.append(os.getcwd())

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from robot_data import RobotDataStore
from browser_drivers import *
from selenium.webdriver import ActionChains

#從RobotDataStore 存取Driver
def set_Browser_driver(driver):
    RobotDataStore.set_env_var("driver",driver)


def get_Browser_driver():
    driver = RobotDataStore.get_env_var("driver")
    return driver
class BasePage:

    def __init__(self, driver):
        self.wait = None
        self.driver = driver
        self.implicitly_wait_timeout = 0.5
        self.explicit_wait_timeout = 1 #60
        self.driver.implicitly_wait(self.implicitly_wait_timeout)
        self.set_explicit_wait_timeout(self.explicit_wait_timeout)
        self.driver.maximize_window()

    def set_explicit_wait_timeout(self, timeout: int):
        self.wait = WebDriverWait(self.driver, timeout)

    def get_page(self, url: str):
        logging.info("Open URL -> %s", url)
        self.driver.get(url)

    def quit_driver(self):
        logging.info("Quit driver")
        self.driver.quit()

    def find_element(self, locator: tuple):
        logging.debug("Find Element: %s", locator)
        _element = self.wait.until(ec.presence_of_element_located(locator))
        return _element

    def wait_for_browser_title(self, exp_title: str, timeout=60):
        for _ in range(timeout):
            logging.debug("Wait for browser title Exp: [%s], Act: [%s]", exp_title, self.driver.title)
            if self.driver.title == exp_title:
                break
            time.sleep(1)
        else:
            raise TimeoutError("Wait for browser title present timeout")

    def wait_for_browser_title_by_partial(self, partial_tital: str, timeout=60):
        for _ in range(timeout):
            logging.debug("Wait for browser title Exp: [%s], Act: [%s]", partial_tital, self.driver.title)
            if partial_tital in self.driver.title:
                break
            time.sleep(1)
        else:
            raise TimeoutError("Wait for browser title present timeout")

    def is_element_present(self, locator: tuple):
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(*locator)
            return True
        except Exception:
            return False
        finally:
            self.driver.implicitly_wait(self.implicitly_wait_timeout)

    def switch_to_frame(self, locator: tuple):
        logging.info("Switch to frame -> [%s]", locator)
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(locator))

    def is_page_load_complete(self):
        js_state = ''
        retry_times = 0
        while js_state == '':
            try:
                js_state = self.driver.execute_script('return window.document.readyState;')
            except Exception:
                js_state = ''
                retry_times += 1
                time.sleep(0.5)

            if retry_times > 5:
                js_state = 'complete'
                break

        return js_state == 'complete'

    def wait_page_until_loading(self):
        """ Wait page until loading """
        logging.info('>>> Wait for page until loading...')
        wait_time = 0.2
        start_t = time.time()

        load_st_timeout = 0
        while self.is_page_load_complete():
            logging.debug('Wait page status changed...')
            time.sleep(wait_time)
            load_st_timeout += 1
            if load_st_timeout > 5:  # 15 times (30 * 0.2 = 10 sec)
                logging.debug('Page status not changed')
                break
        else:
            logging.info('Start Page to loading')

        if not self.is_page_load_complete():
            # wait page loading after 15 sec get timeout
            logging.info('Wait page loading...')
            try:
                WebDriverWait(self.driver, 60).until(lambda driver: self.is_page_load_complete())
            except Exception:
                raise Exception("WAIT_PAGE_LOADING_TIMEOUT")
            else:
                logging.info('Wait page loading complete!')

        end_t = time.time()
        elapsedtime = round((end_t - start_t), 3)
        logging.info("<<< Wait page loading spend time %s", elapsedtime)


#==================================通用方法=========================================

    #CheckElemt方法
    def check(self,UIInput):
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:   
            obj = self.find_element(elemt)   
            if(obj!=None):
                return True
            else:
                return False
        except:
            logging.debug('Check warning.')
            return False
    
    #Click方法
    def click(self,UIInput):
        #判定檢索方式    
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:
            elemt = self.GetElementType(UIInput)
            self.find_element(elemt).click()
            self.wait_page_until_loading()        
            return True
        except:
            logging.debug('Click warning.')
            return False
    
    def MoveUp(self,UIInput,moveposX, moveposY):
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:
            move = ActionChains(get_Browser_driver())
            Slider = self.find_element(elemt)            
            move.click_and_hold(Slider).move_by_offset(moveposX, moveposY).release().perform()
            self.wait_page_until_loading()
            time.sleep(2)        
            return True
        except:
            logging.debug('MoveUp warning.')
            return False

    def GetText(self,UIInput):
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:
            text = self.find_element(elemt).text
            self.wait_page_until_loading()
            return text 
        except:
            logging.debug('GetText warning.')
            return None

    def retry(self,exectimes,function,*arg):        
        for i in range(0,int(exectimes)):
            time.sleep(1)
            function(arg[0])