import time
import logging
import sys,os
sys.path.append(os.getcwd())

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from robot_data import RobotDataStore
from browser_drivers import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

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

    def basefunc_get_page(self, url: str):
        logging.info("Open URL -> %s", url)
        self.driver.get(url)

    def basefunc_quit_driver(self):
        logging.info("Quit driver")
        self.driver.quit()

    def basefunc_find_element(self, locator: tuple):
        logging.debug("Find Element: %s", locator)
        _element = self.wait.until(ec.presence_of_element_located(locator))
        return _element

    def basefunc_wait_for_browser_title(self, exp_title: str, timeout=60):
        for _ in range(timeout):
            logging.debug("Wait for browser title Exp: [%s], Act: [%s]", exp_title, self.driver.title)
            if self.driver.title == exp_title:
                break
            time.sleep(1)
        else:
            raise TimeoutError("Wait for browser title present timeout")

    def basefunc_wait_for_browser_title_by_partial(self, partial_tital: str, timeout=60):
        for _ in range(timeout):
            logging.debug("Wait for browser title Exp: [%s], Act: [%s]", partial_tital, self.driver.title)
            if partial_tital in self.driver.title:
                break
            time.sleep(1)
        else:
            raise TimeoutError("Wait for browser title present timeout")

    def basefunc_is_element_present(self, locator: tuple):
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(*locator)
            return True
        except Exception:
            return False
        finally:
            self.driver.implicitly_wait(self.implicitly_wait_timeout)

    def basefunc_switch_to_frame(self, locator: tuple):
        logging.info("Switch to frame -> [%s]", locator)
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(locator))

    def basefunc_is_page_load_complete(self):
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

    def basefunc_wait_page_until_loading(self):
        """ Wait page until loading """
        logging.info('>>> Wait for page until loading...')
        wait_time = 0.2
        start_t = time.time()

        load_st_timeout = 0
        while self.basefunc_is_page_load_complete():
            logging.debug('Wait page status changed...')
            time.sleep(wait_time)
            load_st_timeout += 1
            if load_st_timeout > 5:  # 15 times (30 * 0.2 = 10 sec)
                logging.debug('Page status not changed')
                break
        else:
            logging.info('Start Page to loading')

        if not self.basefunc_is_page_load_complete():
            # wait page loading after 15 sec get timeout
            logging.info('Wait page loading...')
            try:
                WebDriverWait(self.driver, 60).until(lambda driver: self.basefunc_is_page_load_complete())
            except Exception:
                raise Exception("WAIT_PAGE_LOADING_TIMEOUT")
            else:
                logging.info('Wait page loading complete!')

        end_t = time.time()
        elapsedtime = round((end_t - start_t), 3)
        logging.info("<<< Wait page loading spend time %s", elapsedtime)


#==================================通用方法=========================================
    
    # #CheckElemt方法
    def check(self,UIInput):
        
        elemt = self.GetElementType(UIInput) #先看是某有此型態的元件
        if elemt== None:
            return False
        
        #若有，則開始查找元件
        try:   
            obj = self.basefunc_find_element(elemt)   
            if(obj!=None):
                return True
            else:
                return False
        except:
            print("Check fail. Unexpected error:", sys.exc_info()[0])
            logging.debug("Check fail. Unexpected error:", sys.exc_info()[0])
            return False
    
    #Click方法
    def click(self,UIInput):
        #判定檢索方式    
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            
            return False
        try:            
            elemt = self.GetElementType(UIInput)
            self.basefunc_find_element(elemt).click()
            self.basefunc_wait_page_until_loading()        
            return True
        except:
            logging.debug('Click fail.')
            return False
    
    def GetCalSliderMovePos(self,UI_Min,UI_Max)->(int):
        #取出Min & Max的X位置，並取得兩者之間的值作為分母
        #算出位於每一個解析度下的距離位置
        Min_elemt       = self.GetElementType(UI_Min)
        Max_elemt       = self.GetElementType(UI_Max)
        Min_text        = self.basefunc_find_element(Min_elemt).text
        Max_text        = self.basefunc_find_element(Max_elemt).text
        Min_location    = self.basefunc_find_element(Min_elemt).location
        Max_location    = self.basefunc_find_element(Max_elemt).location        

        if Min_elemt == None or Min_elemt == None or Min_text == None or Max_text==None:
            return False
        try:                       
            sum = (float(Max_text)-float(Min_text)) 
            if sum == 0 :
                return 0
            else:
                maxpos = Max_location['x']
                minpos = Min_location['x']
                MoveSize = ((float(maxpos) - float(minpos)) / sum )+1
                return int(MoveSize)
            

        except:
            logging.debug('GetCalSliderMovePos fail.')
            return 0
    
    def MoveUp(self,UIInput,moveposX, moveposY):
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:
            move = ActionChains(get_Browser_driver())
            Slider = self.basefunc_find_element(elemt)            
            move.click_and_hold(Slider).move_by_offset(moveposX, moveposY).release().perform()
            self.basefunc_wait_page_until_loading()
            time.sleep(2)        
            return True
        except:
            logging.debug('MoveUp warning.')
            return False

    def GetText(self,UIInput)->str:
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:
            text = self.basefunc_find_element(elemt).text
            self.basefunc_wait_page_until_loading()
            return text 
        except:
            logging.debug('GetText warning.')
            return None

    def retry(self,exectimes,function,*arg):        
        for i in range(0,int(exectimes)):
            time.sleep(1)
            function(arg[0])

    def GetInputBoxText(self,UIInput):
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:
            text = self.basefunc_find_element(elemt).get_attribute('value')
            self.basefunc_wait_page_until_loading()
            return text
        except:
            logging.debug('GetInputBoxText warning.')
            return None

    def SetInputBoxText(self, UIInput, text):
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:           
            inputtext = self.basefunc_find_element(elemt)
            inputtext.send_keys(Keys.CONTROL+'a')
            #inputtext.send_keys(Keys.DELETE)
            inputtext.send_keys(text)
            inputtext.send_keys(Keys.ENTER)
            self.basefunc_wait_page_until_loading()
            return True
        except:
            logging.debug('SetInputBoxText warning.')
            return None

    def GetTableRows(self,UIInput):
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:
            rows = self.driver.find_elements_by_xpath(elemt[1]+'/tr')
            cols = self.driver.find_elements_by_xpath(elemt[1]+'/tr[1]/td')
            # rows = len(table)
            self.basefunc_wait_page_until_loading()
            return rows
        except:
            logging.debug('GetTable warning.')
            return None

    def MouseClick(self,PosX, PosY):
        if self== None:
            return False
        try:
            move = ActionChains(get_Browser_driver())      
            move.move_by_offset(PosX, PosX)
            move.click().release().perform()
            self.basefunc_wait_page_until_loading()
            time.sleep(2)        
            return True
        except:
            logging.debug('Mouse Click warning.')
            return None

    def SelectList(self, UIInput, index):
        elemt = self.GetElementType(UIInput)
        if elemt== None:
            return False
        try:           
            lstSelect = self.basefunc_find_element(elemt)
            lstSelect.select_by_index(index)
            
            self.basefunc_wait_page_until_loading()
            return True
        except:
            logging.debug('SetInputBoxText warning.')
            return None

    