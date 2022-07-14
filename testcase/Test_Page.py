import logging
import time

import sys,os

from numpy import NaN
sys.path.append(os.getcwd())
sys.path.append('..')
sys.path.append('..\\beTestedPage')


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
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

#log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log") #按照時間命名
log_filename = "E2ETesting.log"

fh = logging.FileHandler(log_filename)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

#endregion ===============================Logger===============================

#各測試個別產生瀏覽器，或一個瀏覽器走到底
Flg_KeepBrowser = True
#False : 個別開啟瀏覽器
#True  : 維持同個瀏覽器，則須從Testcase:test_turnOnBrowser()開始執行起

def get_Project_WebObject(): #寫成單例
    
    if ProjectAction.get_project_page_obj()==NaN or Flg_KeepBrowser==False:
        ProjectAction.Init_Project_page("chrome")
        
    Project_obj = ProjectAction.get_project_page_obj()    
    ProjectAction.set_project_page_obj(Project_obj)

    return Project_obj

#使用chrome進介面

#region ===============================page1===============================
def test_turnOnBrowser():    
    if Flg_KeepBrowser==True:
        Project_obj = get_Project_WebObject()         
        assert True  
    else:
    #直接By Pass
        assert True 

def test_checkElemt():     
           
    #依序檢查每個Elemt是否能夠找到?
    Project_obj = get_Project_WebObject()

    
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

    Project_obj = get_Project_WebObject()
        
    try:               
        Project_obj.click("Project_radio_0")        
        Project_obj.click_Button_Next()   
    except Exception:
        assert False,Exception("Click to NextPage Fail.")              
    finally:
        ProjectAction.set_project_page_obj(Project_obj)

#endregion ===============================page1===============================



#region ===============================page2===============================

def get_Detail_WebObject():
    if Flg_KeepBrowser==False:
        ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        DetailAction.setup_Detail_page()
        Detail_obj = DetailAction.get_Detail_page_obj()
    
    DetailAction.set_Detail_page_obj(Detail_obj)
    
    return Detail_obj

#等待讀取 跳頁後必須執行此
def test_WaitForLoading():
    Detail_obj = get_Detail_WebObject()    
    DetailAction.set_Detail_page_obj(Detail_obj)

#切換播放/暫停
#點擊按鈕後再次抓取狀態比對得知是否切換成功
def test_PlayPause():   

    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    
    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")
        
        Detail_obj.retry(2,Detail_obj.click,str("Button_PlayPause") )
        time.sleep(10)     
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
        result = Detail_obj.GetText("Label_CameraState")        
        if(after==result ):
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        DetailAction.set_Icam_Detail_page_obj(Detail_obj)


#Softtrigger Acquisition 
def test_SoftwareTriggerAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Connected"): 
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_CameraAcq_Settings")
        Detail_obj.click("Tab_Trigger_Mode_Settings")
        Detail_obj.click("Radio_SW_Trigger_Mode")

        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Button_PlayPause")
        Detail_obj.retry(10, Detail_obj.click,str("Button_SW_Trigger_Trigger"))

        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")  
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
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Radio_Continuous_Mode")
        Detail_obj.click("Tab_Trigger_Mode_Settings")
        Detail_obj.click("Tab_CameraAcq_Settings")

#Hardware Trigger
def test_HardwareTriggerAcq(): 
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_CameraAcq_Settings")
        Detail_obj.click("Tab_Trigger_Mode_Settings")
        Detail_obj.click("Radio_HW_Trigger_Mode")

        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_IO_Settings")
        Detail_obj.click("Tab_DO1")
        Detail_obj.click("Tab_DO1_Parameters")
        

        Detail_obj.click("Button_PlayPause")

        times = 10
        for i in range(times):
            Detail_obj.click("Button_DO1_Output_High")
            Detail_obj.click("Button_DO1_Output_Low")       
        
        
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Radio_Continuous_Mode")
        Detail_obj.click("Tab_Trigger_Mode_Settings")
        Detail_obj.click("Tab_CameraAcq_Settings")
        Detail_obj.click("Tab_DO1_Parameters")
        Detail_obj.click("Tab_DO1")
        Detail_obj.click("Tab_IO_Settings")

#Set Focus Acquisition
def test_SetFocusAcq(): 
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")
        
        Detail_obj.click("Button_PlayPause")
        Detail_obj.click("Tab_CameraAcq_Settings")
        Detail_obj.click("Tab_Focus_Settings")
        Detail_obj.SetInputBoxText("Input_Focus_Step_Distance", "300")
        Detail_obj.click("Button_ZoomIn")
        time.sleep(5)

        focusText = Detail_obj.GetInputBoxText("InputBox_Focus") 
        if( focusText == "300" ):
            logging.info( "Focus:" + focusText )
            assert True
        else:
            assert False,Exception("result different")      

        Detail_obj.click("Button_ZoomOut")
        time.sleep(5)

        focusText = Detail_obj.GetInputBoxText("InputBox_Focus") 
        if( focusText == "0" ):
            logging.info( "Focus:" + focusText )
            assert True
        else:
            assert False,Exception("result different")      

        Detail_obj.click("Button_PlayPause")  
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Focus_Settings")
        Detail_obj.click("Tab_CameraAcq_Settings")

#Reset Focus Acquisition
def test_ResetFocusAcq(): 
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")
        
        Detail_obj.click("Button_PlayPause")
        Detail_obj.click("Tab_CameraAcq_Settings")
        Detail_obj.click("Tab_Focus_Settings")
        Detail_obj.SetInputBoxText("Input_Focus_Step_Distance", "300")
        Detail_obj.retry(4,Detail_obj.click,str("Button_ZoomIn") )        
        time.sleep(5)

        focusText = Detail_obj.GetInputBoxText("InputBox_Focus") 
        if( focusText == "1200" ):
            logging.info( "Focus:" + focusText )
            assert True
        else:
            assert False,Exception("result different")      

        Detail_obj.click("Button_Reset_to_Zero_Position")
        time.sleep(5)
        focusText = Detail_obj.GetInputBoxText("InputBox_Focus") 
        if( focusText == "0" ):
            logging.info( "Focus:" + focusText )
            assert True
        else:
            assert False,Exception("result different")  
        Detail_obj.click("Button_PlayPause")  
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Focus_Settings")
        Detail_obj.click("Tab_CameraAcq_Settings")

#Set FPS and Acquisition
def test_SetFPSAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()
    time.sleep(6)

    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        Detail_obj.click("Tab_CameraAcq_Settings")
        Detail_obj.click("Tab_Trigger_Mode_Settings")
        Detail_obj.click("Radio_Continuous_Mode")   
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        setFPSValue = "10"
        Detail_obj.SetInputBoxText("Input_Sensor_Frame_Rate", setFPSValue)
        
        Detail_obj.click("Button_PlayPause")
        time.sleep(10)
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")      
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
        time.sleep(1)       
        result = Detail_obj.GetText("Label_CameraState")
        
        if(after==result and 0 < float(fpsText) <= float(setFPSValue) ):
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Trigger_Mode_Settings")
        Detail_obj.click("Tab_CameraAcq_Settings")

#Set ROI 1280*960 Acquisition
def test_SetROI1280Acq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_ROI_Settings_Output_Resolution")
        Detail_obj.click("Radio_1280x960")


        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_ROI_Settings_Output_Resolution")

#Set ROI 640*480 Acquisition
def test_SetROI640Acq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_ROI_Settings_Output_Resolution")
        Detail_obj.click("Radio_640x480")


        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_ROI_Settings_Output_Resolution")

#Set ROI 320*240 Acquisition
def test_SetROI320Acq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_ROI_Settings_Output_Resolution")
        Detail_obj.click("Radio_320x240")


        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_ROI_Settings_Output_Resolution")

def test_SetBrightnessMAXInputAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.SetInputBoxText("Input_Brightness","255")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetBrightnessMiniInputAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.SetInputBoxText("Input_Brightness","0")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetBrightnessAnyInputAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.SetInputBoxText("Input_Brightness","120")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetSharpnessMAXInputAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.SetInputBoxText("Input_Sharpness","100")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetSharpnessMiniInputAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.SetInputBoxText("Input_Sharpness","0")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetSharpnessAnyInputAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.SetInputBoxText("Input_Sharpness","75")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetGammaMAXInputAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.SetInputBoxText("Input_Gamma","0")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetGammaMiniInputAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.SetInputBoxText("Input_Gamma","400")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetGammaAnyInputAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.SetInputBoxText("Input_Gamma","333")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Button_DisconnectConnect")
        Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetBrightnessSliderAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        movePos = Detail_obj.GetCalSliderMovePos("Label_Brightness_Min","Label_Brightness_Max")
        Detail_obj.MoveUp("Slider_Brightness",movePos*50,0)        
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetSharpnessSliderAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        movePos = Detail_obj.GetCalSliderMovePos("Label_Sharpness_Min","Label_Sharpness_Max")
        Detail_obj.MoveUp("Slider_Sharpness",movePos*50,0)        
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetGammaSliderAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        movePos = Detail_obj.GetCalSliderMovePos("Label_Gamma_Min","Label_Gamma_Max")
        Detail_obj.MoveUp("Slider_Gamma",movePos*70,0)        
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetMirrorXAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Button_MirrorX")     
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetExposureTimeMaxAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        setExposureTimeValue = "10000"
        Detail_obj.SetInputBoxText("Input_Auto_Exposure_Time", setExposureTimeValue)  
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetExposureTimeMinAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        setExposureTimeValue = "50"
        Detail_obj.SetInputBoxText("Input_Auto_Exposure_Time", setExposureTimeValue)  
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetExposureTimeAnyValueAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        setExposureTimeValue = "650"
        Detail_obj.SetInputBoxText("Input_Auto_Exposure_Time", setExposureTimeValue)  
        time.sleep(1)
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetAutoExposureAcq(): 
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        Detail_obj.click("Switch_Auto_Exposure_Time") 
        setAEMinValue = "2000"
        setAEMaxValue = "8500"
        Detail_obj.SetInputBoxText("Input_Auto_Exposure_Time_Min", setAEMinValue)
        Detail_obj.SetInputBoxText("Input_Auto_Exposure_Time_Max", setAEMaxValue)
  
        Detail_obj.click("Button_Auto_Exposure_Time_Confirm")
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        Detail_obj.click("Tab_Generic_Settings")

def test_ResetAutoExposureAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        Detail_obj.click("Switch_Auto_Exposure_Time") 
        setAEMinValue = "3000"
        setAEMaxValue = "6000"
        Detail_obj.SetInputBoxText("Input_Auto_Exposure_Time_Min", setAEMinValue)
        Detail_obj.SetInputBoxText("Input_Auto_Exposure_Time_Max", setAEMaxValue)  
        Detail_obj.click("Button_Auto_Exposure_Time_Confirm")      
        Detail_obj.click("Button_PlayPause")

        time.sleep(5)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
        Detail_obj.click("Button_Auto_Exposure_Time_Reset")
        minText = Detail_obj.GetInputBoxText("Input_Auto_Exposure_Time_Min")
        maxText = Detail_obj.GetInputBoxText("Input_Auto_Exposure_Time_Max")
        Detail_obj.click("Button_PlayPause")  
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and minText == "50" and maxText == "10000" ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Auto_Exposure_Mode")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetGainMinAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Auto_Gain_Mode_Intensity")
        setGainValue = "0"
        Detail_obj.SetInputBoxText("Input_Auto_Gain_Mode_Intensity", setGainValue)  
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Auto_Gain_Mode_Intensity")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetGainMaxAcq():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Auto_Gain_Mode_Intensity")
        setGainValue = "24"
        Detail_obj.SetInputBoxText("Input_Auto_Gain_Mode_Intensity", setGainValue)  
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.SetInputBoxText("Input_Auto_Gain_Mode_Intensity", "0")  
        Detail_obj.click("Tab_Auto_Gain_Mode_Intensity")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetGainSliderAcq(): 
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制 
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Generic_Settings")
        Detail_obj.click("Tab_Auto_Gain_Mode_Intensity")
        movePos = Detail_obj.GetCalSliderMovePos("Label_Gain_Min","Label_Gain_Max")
        Detail_obj.MoveUp("Slider_Auto_Gain_Mode_Intensity",movePos*10,0)        
      
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Image_Adjustments")
        Detail_obj.click("Tab_Generic_Settings")

def test_SetStrobeMode():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_CameraAcq_Settings")
        Detail_obj.click("Tab_Lighting_Settings")
        movePos = Detail_obj.GetCalSliderMovePos("Label_Flash_LED_Mode_Min","Label_Flash_LED_Mode_Max")
        Detail_obj.MoveUp("Slider_Flash_LED_Mode",movePos*5,0)        
        time.sleep(1)
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Lighting_Settings")
        Detail_obj.click("Tab_CameraAcq_Settings")
    
def test_SetStrobeGainMode():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_CameraAcq_Settings")
        Detail_obj.click("Tab_Lighting_Settings")
        movePos = Detail_obj.GetCalSliderMovePos("Label_Flash_LED_Mode_Min","Label_Flash_LED_Mode_Max")
        Detail_obj.MoveUp("Slider_Flash_LED_Mode",movePos*5,0)        
        movePos = Detail_obj.GetCalSliderMovePos("Label_Flash_LED_Gain_Min","Label_Flash_LED_Gain_Max")
        Detail_obj.MoveUp("Slider_Flash_LED_Gain",movePos*10,0)        
        time.sleep(1)
        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_Lighting_Settings")
        Detail_obj.click("Tab_CameraAcq_Settings")

#Set LED Color Green
def test_SetLEDColorGreen():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Platform_LED")
        Detail_obj.click("Switch_SYSLED")
        Detail_obj.click("Radio_SYSLED_Green")

        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Switch_SYSLED")
        Detail_obj.click("Tab_Platform_LED")
        #Detail_obj.click("Button_DisconnectConnect")
        #Detail_obj.click("Button_Popup_Window_Ok")


#Set LED Color Orange
def test_SetLEDColorOrange():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Platform_LED")
        Detail_obj.click("Switch_SYSLED")
        Detail_obj.click("Radio_SYSLED_Orange")

        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        #Detail_obj.click("Button_DisconnectConnect")
        #Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Switch_SYSLED")
        Detail_obj.click("Tab_Platform_LED")

#Set LED Color Yellow
def test_SetLEDColorYellow():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_Platform_LED")
        Detail_obj.click("Switch_SYSLED")
        Detail_obj.click("Radio_SYSLED_Yellow")

        Detail_obj.click("Button_PlayPause")

        time.sleep(10)
                
        fpsText = Detail_obj.GetInputBoxText("InputBox_FPS")   
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
  
        result = Detail_obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        #Detail_obj.click("Button_DisconnectConnect")
        #Detail_obj.click("Button_Popup_Window_Ok")
        Detail_obj.click("Switch_SYSLED")
        Detail_obj.click("Tab_Platform_LED")


#DIO Setting
def test_DO0UserOutput():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_IO_Settings")
        Detail_obj.click("Tab_DI1")
        Detail_obj.click("Tab_DO1")
        Detail_obj.click("Tab_DO1_Parameters")
        
        Detail_obj.click("Button_DO1_Output_High")
        time.sleep(1)
        diStatus = Detail_obj.GetText("Label_DI1_Status")
        if( diStatus ==  '(H)' ):
            logging.info( "DI0 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")

        Detail_obj.click("Button_DO1_Output_Low")
        time.sleep(1)
        diStatus = Detail_obj.GetText("Label_DI1_Status")
        if( diStatus ==  '(L)' ):
            logging.info( "DI0 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")        
           
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_DO1_Parameters")
        Detail_obj.click("Tab_DI1")
        Detail_obj.click("Tab_DO1")
        Detail_obj.click("Tab_IO_Settings")

def test_DO1UserOutput():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_IO_Settings")
        Detail_obj.click("Tab_DI2")
        Detail_obj.click("Tab_DO2")
        Detail_obj.click("Tab_DO2_Parameters")
        
        Detail_obj.click("Button_DO2_Output_High")
        time.sleep(1)
        diStatus = Detail_obj.GetText("Label_DI2_Status")
        if( diStatus ==  '(H)' ):
            logging.info( "DI1 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")

        Detail_obj.click("Button_DO2_Output_Low")
        time.sleep(1)
        diStatus = Detail_obj.GetText("Label_DI2_Status")
        if( diStatus ==  '(L)' ):
            logging.info( "DI1 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")        
           
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Tab_DO2_Parameters")
        Detail_obj.click("Tab_DI2")
        Detail_obj.click("Tab_DO2")
        Detail_obj.click("Tab_IO_Settings")

def test_DO0InvertUserOutput():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_IO_Settings")
        Detail_obj.click("Tab_DI1")
        Detail_obj.click("Tab_DO1")
        Detail_obj.click("Tab_DO1_Parameters")
        Detail_obj.click("Radio_DO1_Reverse_On")
        
        Detail_obj.click("Button_DO1_Output_High")
        time.sleep(1)
        diStatus = Detail_obj.GetText("Label_DI1_Status")
        if( diStatus ==  '(L)' ):
            logging.info( "DI0 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")

        Detail_obj.click("Button_DO1_Output_Low")
        time.sleep(1)
        diStatus = Detail_obj.GetText("Label_DI1_Status")
        if( diStatus ==  '(H)' ):
            logging.info( "DI0 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")        
           
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Radio_DO1_Reverse_Off")
        Detail_obj.click("Tab_DO1_Parameters")
        Detail_obj.click("Tab_DI1")
        Detail_obj.click("Tab_DO1")
        Detail_obj.click("Tab_IO_Settings")

def test_DO1InvertUserOutput():
    Detail_obj = None
    if Flg_KeepBrowser==False:
    ##Init 直接對取得物件做控制
        Detail_obj = DetailAction.Init_Icam_Detail_page("chrome")
        Detail_obj.get_Detail_page()
    else:
    ##setup 從過去取得網頁做控制
        Detail_obj = DetailAction.get_Icam_Detail_page_obj()

    time.sleep(6)
    try:   
        CameraState = Detail_obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            Detail_obj.click("Button_DisconnectConnect")
            Detail_obj.click("Button_Popup_Window_Ok")

        Detail_obj.click("Tab_IO_Settings")
        Detail_obj.click("Tab_DI2")
        Detail_obj.click("Tab_DO2")
        Detail_obj.click("Tab_DO2_Parameters")
        Detail_obj.click("Radio_DO2_Reverse_On")
        Detail_obj.click("Button_DO2_Output_High")
        time.sleep(1)
        diStatus = Detail_obj.GetText("Label_DI2_Status")
        if( diStatus ==  '(L)' ):
            logging.info( "DI1 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")

        Detail_obj.click("Button_DO2_Output_Low")
        time.sleep(1)
        diStatus = Detail_obj.GetText("Label_DI2_Status")
        if( diStatus ==  '(H)' ):
            logging.info( "DI1 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")        
           
    except Exception:
        assert False        
    finally:
        Detail_obj.click("Radio_DO2_Reverse_Off")
        Detail_obj.click("Tab_DO2_Parameters")
        Detail_obj.click("Tab_DI2")
        Detail_obj.click("Tab_DO2")
        Detail_obj.click("Tab_IO_Settings")
