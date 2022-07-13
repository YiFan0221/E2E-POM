import logging
import time

import sys,os
sys.path.append('..')
sys.path.append(os.getcwd())
from base_locators import *
import beTestedPage.ProjectPage.Project_page_actions as ProjectAction
import beTestedPage.DetailPage.Detail_page_actions as DetailAction

#*** Test Cases ***

#region ===============================Logger===============================
logger = logging.getLogger()
logger.setLevel(logging.INFO)#設定顯示層級
formatter = logging.Formatter(
	'[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
	datefmt='%Y%m%d %H:%M:%S')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

#log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log") #按照時間命名
log_filename = "E2ETesting.log"

fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

#endregion ===============================Logger===============================

#各測試個別產生瀏覽器，或一個瀏覽器走到底
Flg_KeepBrowser = True
#False 個別開啟瀏覽器
#True  維持同個瀏覽器，則須從Testcase:test_turnOnBrowser()開始執行起

#使用chrome進介面

#region ===============================page1===============================
def test_turnOnBrowser():    
    if Flg_KeepBrowser==True:
        ProjectAction.Init_Project_page("chrome")
        Project_obj = ProjectAction.get_project_page_obj()
        ProjectAction.set_project_page_obj(Project_obj)
        Project_obj.get_Project_page() 
        assert True  
    else:
    #直接By Pass
        assert True 

def test_checkElemt():            
    #依序檢查每個Elemt是否能夠找到?

    Project_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Project_obj = ProjectAction.Init_Project_page("chrome")
        Project_obj.get_Project_page()
    else:
    ##setup 從過去取得網頁做控制
        Project_obj = ProjectAction.get_project_page_obj()
    
    #取出Locator容器中的大小
    
    number = len(Project_obj.UI_List)
    st = "List Size:"+str(number)
    logging.info(st)
    print(st)

    #巡訪所有元件
    for i in range(number):
        oLocatorsObj = Project_obj.UI_List[i]
        mInfoJson=json.loads(oLocatorsObj.InfoJson) #取Json
        mElemt = oLocatorsObj.elemt
        st = "["+str(i)+"]:"+mInfoJson["Name"]    
        
        if Project_obj.check(mElemt)==True:
            st="[O]"+st
            logging.info(st)
        else:
            st="[X]"+st
            logging.info(st)


#進入畫面二前抓取當下狀態
def test_ClicktoNextPage():

    Project_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Project_obj = ProjectAction.Init_Project_page("chrome")
        Project_obj.get_Project_page() 
    else:
    ##setup 從過去取得網頁做控制
        ProjectAction.setup_Project_page()
        Project_obj = ProjectAction.get_project_page_obj()
    try:               
        Project_obj.click("Project_radio_0")        
        Project_obj.click_Button_Next()   
    except Exception:
        assert False,Exception("Click to NextPage Fail.")              
    finally:
        ProjectAction.set_project_page_obj(Project_obj)

#endregion ===============================page1===============================



#region ===============================page2===============================
#等待讀取 跳頁後必須執行此
def test_WaitForLoading():
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        DetailAction.setup_Detail_page()
        Detail_obj = DetailAction.get_Detail_page_obj()
    
    DetailAction.set_Detail_page_obj(Detail_obj)

#切換播放/暫停
#點擊按鈕後再次抓取狀態比對得知是否切換成功
def test_PlayPause():   

    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Detail_page_obj()

    
    time.sleep(6)
    try:   
        Detail_obj.retry(2,Detail_obj.click,str("Button_PlayPause") )     
        CameraState = Detail_obj.GetText("Label_CameraState")        
        ButtonState = Detail_obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        Detail_obj.click("Button_PlayPause")        
        resault = Detail_obj.GetText("Label_CameraState")
        if(after==resault ):
            assert True
        else:
            assert False,Exception("resault defferent")        
    except Exception:
        assert False        
    finally:
        DetailAction.set_Detail_page_obj(Detail_obj)


#切換燈號
#進入畫面二展開摺疊介面
#滑動LED Mode拉條
def test_SwitchLED():    
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Detail_page_obj()
    
    time.sleep(6)
    try:               
        Detail_obj.click("Tab_CameraAcq_Settings")        
        Detail_obj.click("Tab_Lighting_Settings")       
        Detail_obj.MoveUp("Slider_Flash_LED_Mode",200,0)
    except Exception:
        assert False,Exception("WAIT_PAGE_LOADING_TIMEOUT")
    finally:        
        DetailAction.set_Detail_page_obj(Detail_obj)

#endregion ===============================page2===============================