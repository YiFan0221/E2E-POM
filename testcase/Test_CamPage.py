import logging
import time

import sys,os
from turtle import goto

sys.path.append(os.getcwd())
sys.path.append('..')
sys.path.append('..\\beTestedPage')


from base_locators import *
#import beTestedPage.Overtime.Overtime_page_actions as TargetWebAction
import beTestedPage.ProjectPage.Project_page_actions as TargetWeb1Action
import beTestedPage.DetailPage.Detail_page_actions as TargetWeb2Action


#region ===============================Enable Function===============================
#各測試個別產生瀏覽器，或一個瀏覽器走到底
Flg_KeepBrowser =True
#False : 個別開啟瀏覽器
#True  : 維持同個瀏覽器，則須從Testcase:test_turnOnBrowser()開始執行起
def SleepAfterGetObj():
    time.sleep(4)
def SleepAfterPlayPause():
    time.sleep(3)
def SleepWaitForMachine():
    time.sleep(1)
    
def get_Web1Object(): #寫成單例 取得目前網頁資訊
    global obj;
    getOBJ_Success= TargetWeb1Action.get_page_obj()
    if getOBJ_Success==False or Flg_KeepBrowser==False:
        obj=TargetWeb1Action.Init_page("chrome")#使用chrome進介面
        try:               
            obj.get_page() 
        except Exception:
            TargetWeb1Action.set_page_obj(obj)
    else:
        obj = TargetWeb1Action.get_page_obj()                            
    TargetWeb1Action.set_page_obj(obj)
    return obj        

def get_Web2Object(): #寫成單例 取得目前網頁資訊
    global obj;
    getOBJ_Success= TargetWeb2Action.get_page_obj()
    if getOBJ_Success==False or Flg_KeepBrowser==False:
        obj=TargetWeb2Action.Init_page("chrome")#使用chrome進介面
        obj.get_page()
    else:
        obj=TargetWeb2Action.setup_page()
        obj=TargetWeb2Action.get_page_obj()           
                           
    TargetWeb2Action.set_page_obj(obj)
    return obj        

#endregion ===============================Enable Function===============================        

#region ===============================Logger===============================
logger = logging.getLogger()
logger.setLevel(logging.INFO)#設定顯示層級
formatter = logging.Formatter(
	'[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
	datefmt='%Y%m%d %H:%M:%S')


#輸出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

#輸出到檔案
#log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log") #按照時間命名
log_filename = "E2ETesting.log"
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


#endregion ===============================Logger===============================

#region ===============================page1===============================
def test_turnOnBrowser():    
    obj = get_Web1Object()             
    assert True  
    
# def test_checkElemt():                
#     #依序檢查每個Elemt是否能夠找到?
#     obj = get_Web1Object()
    
#     #取出Locator容器中的大小
#     number = len(obj.UI_List)
#     st = "List Size:"+str(number)
#     logging.info(st)
#     print(st)

#     #巡訪所有元件
#     for i in range(number):
#         oLocatorsObj = obj.UI_List[i]
#         mInfoJson=json.loads(oLocatorsObj.InfoJson) #取Json
#         mElemt = oLocatorsObj.elemt    
#         st = "["+str(i)+"]:"+mInfoJson["Name"]    
        
#         if obj.check(mElemt)==True:
#             st="[O]"+st
#         else:
#             st="[X]"+st
            
#         print(st)
#         logging.info(st)
#     assert True


#進入畫面二前抓取當下狀態
def test_ClicktoNextPage():

    obj = get_Web1Object()
        
    try:               
        obj.click("Project_radio_0")        
        obj.click_Button_Next()   
    except Exception:
        assert False,Exception("Click to NextPage Fail.")              
    finally:
        TargetWeb1Action.set_page_obj(obj)

#endregion ===============================page1===============================


import beTestedPage.DetailPage.Detail_page_actions as TargetWebAction
#region ===============================page2===============================

def test_checkElemt():     
           
    #依序檢查每個Elemt是否能夠找到?
    obj = get_Web2Object()

    #取出Locator容器中的大小
    number = len(obj.UI_List)
    st = "List Size:"+str(number)
    logging.info(st)
    print(st)

    #巡訪Locator容器所有元件
    for i in range(number):
        oLocatorsObj = obj.UI_List[i]
        mInfoJson=json.loads(oLocatorsObj.InfoJson) #取Json
        mElemt = oLocatorsObj.elemt
        st = "["+str(i)+"]:"+mInfoJson["Name"]    
        
        if obj.check(mElemt)==True:
            st="[O]"+st
            logging.debug(st)
        else:
            st="[X]"+st
            logging.debug(st)


#等待讀取 跳頁後必須執行此
def test_WaitForLoading():
    obj = get_Web2Object()    
    TargetWebAction.set_page_obj(obj)

#切換播放/暫停
#點擊按鈕後再次抓取狀態比對得知是否切換成功
def test_PlayPause():   
    obj = get_Web2Object()
    SleepAfterGetObj()
    
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")
        
        obj.retry(2,obj.click,str("Button_PlayPause") )
        SleepAfterPlayPause()
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")        
        result = obj.GetText("Label_CameraState")        
        if(after==result ):
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        TargetWebAction.set_page_obj(obj)

#Softtrigger Acquisition 
def test_SoftwareTriggerAcq():
    obj = get_Web2Object()
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Connected"): 
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_CameraAcq_Settings")
        obj.click("Tab_Trigger_Mode_Settings")
        obj.click("Radio_SW_Trigger_Mode")

        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Button_PlayPause")
        obj.retry(10, obj.click,str("Button_SW_Trigger_Trigger"))

        fpsText = obj.GetInputBoxText("InputBox_FPS")  
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

    
        obj.click("Button_PlayPause")  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Radio_Continuous_Mode")
        obj.click("Tab_Trigger_Mode_Settings")
        obj.click("Tab_CameraAcq_Settings")

#Hardware Trigger
def test_HardwareTriggerAcq(): 
    obj = get_Web2Object()
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_CameraAcq_Settings")
        obj.click("Tab_Trigger_Mode_Settings")
        obj.click("Radio_HW_Trigger_Mode")

        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_IO_Settings")
        obj.click("Tab_DO1")
        obj.click("Tab_DO1_Parameters")
        

        obj.click("Button_PlayPause")

        times = 10
        for i in range(times):
            obj.click("Button_DO1_Output_High")
            obj.click("Button_DO1_Output_Low")       
        
        
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Radio_Continuous_Mode")
        obj.click("Tab_Trigger_Mode_Settings")
        obj.click("Tab_CameraAcq_Settings")
        obj.click("Tab_DO1_Parameters")
        obj.click("Tab_DO1")
        obj.click("Tab_IO_Settings")

#Set Focus Acquisition
def test_SetFocusAcq(): 
    obj = get_Web2Object()
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")
        
        obj.click("Button_PlayPause")
        obj.click("Tab_CameraAcq_Settings")
        obj.click("Tab_Focus_Settings")
        obj.SetInputBoxText("Input_Focus_Step_Distance", "300")
        obj.click("Button_ZoomIn")
        SleepWaitForMachine()

        focusText = obj.GetInputBoxText("InputBox_Focus") 
        if( focusText == "300" ):
            logging.info( "Focus:" + focusText )
            assert True
        else:
            assert False,Exception("result different")      

        obj.click("Button_ZoomOut")
        SleepWaitForMachine()

        focusText = obj.GetInputBoxText("InputBox_Focus") 
        if( focusText == "0" ):
            logging.info( "Focus:" + focusText )
            assert True
        else:
            assert False,Exception("result different")      

        obj.click("Button_PlayPause")  
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Focus_Settings")
        obj.click("Tab_CameraAcq_Settings")

#Reset Focus Acquisition
def test_ResetFocusAcq(): 
    obj = get_Web2Object()
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")
        
        obj.click("Button_PlayPause")
        obj.click("Tab_CameraAcq_Settings")
        obj.click("Tab_Focus_Settings")
        obj.SetInputBoxText("Input_Focus_Step_Distance", "300")
        obj.retry(4,obj.click,str("Button_ZoomIn") )        
        SleepWaitForMachine()

        focusText = obj.GetInputBoxText("InputBox_Focus") 
        if( focusText == "1200" ):
            logging.info( "Focus:" + focusText )
            assert True
        else:
            assert False,Exception("result different")      

        obj.click("Button_Reset_to_Zero_Position")
        SleepWaitForMachine()
        focusText = obj.GetInputBoxText("InputBox_Focus") 
        if( focusText == "0" ):
            logging.info( "Focus:" + focusText )
            assert True
        else:
            assert False,Exception("result different")  
        obj.click("Button_PlayPause")  
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Focus_Settings")
        obj.click("Tab_CameraAcq_Settings")

#Set FPS and Acquisition
def test_SetFPSAcq():
    obj = get_Web2Object()
    SleepAfterGetObj()

    try:   
        CameraState = obj.GetText("Label_CameraState")
        obj.click("Tab_CameraAcq_Settings")
        obj.click("Tab_Trigger_Mode_Settings")
        obj.click("Radio_Continuous_Mode")   
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        setFPSValue = "10"
        obj.SetInputBoxText("Input_Sensor_Frame_Rate", setFPSValue)
        
        obj.click("Button_PlayPause")
        SleepWaitForMachine()
        fpsText = obj.GetInputBoxText("InputBox_FPS")      
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")
        SleepAfterPlayPause()  
        result = obj.GetText("Label_CameraState")
        
        if(after==result and 0 < float(fpsText) <= float(setFPSValue) ):
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Trigger_Mode_Settings")
        obj.click("Tab_CameraAcq_Settings")

#Set ROI 1280*960 Acquisition
def test_SetROI1280Acq():
    obj = get_Web2Object()
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_ROI_Settings_Output_Resolution")
        obj.click("Radio_1280x960")


        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
      
        obj.click("Button_PlayPause")
        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_ROI_Settings_Output_Resolution")

#Set ROI 640*480 Acquisition
def test_SetROI640Acq():
    obj = get_Web2Object()
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_ROI_Settings_Output_Resolution")
        obj.click("Radio_640x480")


        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_ROI_Settings_Output_Resolution")

#Set ROI 320*240 Acquisition
def test_SetROI320Acq():
    obj = get_Web2Object()
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Connected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_ROI_Settings_Output_Resolution")
        obj.click("Radio_320x240")


        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_ROI_Settings_Output_Resolution")

def test_SetBrightnessMAXInputAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.SetInputBoxText("Input_Brightness","255")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetBrightnessMiniInputAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.SetInputBoxText("Input_Brightness","0")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetBrightnessAnyInputAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.SetInputBoxText("Input_Brightness","120")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetSharpnessMAXInputAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.SetInputBoxText("Input_Sharpness","100")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetSharpnessMiniInputAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.SetInputBoxText("Input_Sharpness","0")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetSharpnessAnyInputAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.SetInputBoxText("Input_Sharpness","75")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetGammaMAXInputAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.SetInputBoxText("Input_Gamma","0")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetGammaMiniInputAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.SetInputBoxText("Input_Gamma","400")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetGammaAnyInputAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.SetInputBoxText("Input_Gamma","333")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Button_DisconnectConnect")
        obj.click("Button_Popup_Window_Ok")
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetBrightnessSliderAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        movePos = obj.GetCalSliderMovePos("Label_Brightness_Min","Label_Brightness_Max")
        obj.MoveUp("Slider_Brightness",movePos*50,0)        
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetSharpnessSliderAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        movePos = obj.GetCalSliderMovePos("Label_Sharpness_Min","Label_Sharpness_Max")
        obj.MoveUp("Slider_Sharpness",movePos*50,0)        
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetGammaSliderAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        movePos = obj.GetCalSliderMovePos("Label_Gamma_Min","Label_Gamma_Max")
        obj.MoveUp("Slider_Gamma",movePos*70,0)        
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetMirrorXAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Image_Adjustments")
        obj.click("Button_MirrorX")     
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetExposureTimeMaxAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Auto_Exposure_Mode")
        setExposureTimeValue = "10000"
        obj.SetInputBoxText("Input_Auto_Exposure_Time", setExposureTimeValue)  
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Auto_Exposure_Mode")
        obj.click("Tab_Generic_Settings")

def test_SetExposureTimeMinAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Auto_Exposure_Mode")
        setExposureTimeValue = "50"
        obj.SetInputBoxText("Input_Auto_Exposure_Time", setExposureTimeValue)  
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Auto_Exposure_Mode")
        obj.click("Tab_Generic_Settings")

def test_SetExposureTimeAnyValueAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Auto_Exposure_Mode")
        setExposureTimeValue = "650"
        obj.SetInputBoxText("Input_Auto_Exposure_Time", setExposureTimeValue)  
        SleepWaitForMachine()
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Auto_Exposure_Mode")
        obj.click("Tab_Generic_Settings")

def test_SetAutoExposureAcq(): 
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Auto_Exposure_Mode")
        obj.click("Switch_Auto_Exposure_Time") 
        setAEMinValue = "2000"
        setAEMaxValue = "8500"
        obj.SetInputBoxText("Input_Auto_Exposure_Time_Min", setAEMinValue)
        obj.SetInputBoxText("Input_Auto_Exposure_Time_Max", setAEMaxValue)
  
        obj.click("Button_Auto_Exposure_Time_Confirm")
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Auto_Exposure_Mode")
        obj.click("Tab_Generic_Settings")

def test_ResetAutoExposureAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Auto_Exposure_Mode")
        obj.click("Switch_Auto_Exposure_Time") 
        setAEMinValue = "3000"
        setAEMaxValue = "6000"
        obj.SetInputBoxText("Input_Auto_Exposure_Time_Min", setAEMinValue)
        obj.SetInputBoxText("Input_Auto_Exposure_Time_Max", setAEMaxValue)  
        obj.click("Button_Auto_Exposure_Time_Confirm")      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")
        obj.click("Button_Auto_Exposure_Time_Reset")
        minText = obj.GetInputBoxText("Input_Auto_Exposure_Time_Min")
        maxText = obj.GetInputBoxText("Input_Auto_Exposure_Time_Max")
        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and minText == "50" and maxText == "10000" ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Auto_Exposure_Mode")
        obj.click("Tab_Generic_Settings")

def test_SetGainMinAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Auto_Gain_Mode_Intensity")
        setGainValue = "0"
        obj.SetInputBoxText("Input_Auto_Gain_Mode_Intensity", setGainValue)  
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Auto_Gain_Mode_Intensity")
        obj.click("Tab_Generic_Settings")

def test_SetGainMaxAcq():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Auto_Gain_Mode_Intensity")
        setGainValue = "24"
        obj.SetInputBoxText("Input_Auto_Gain_Mode_Intensity", setGainValue)  
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.SetInputBoxText("Input_Auto_Gain_Mode_Intensity", "0")  
        obj.click("Tab_Auto_Gain_Mode_Intensity")
        obj.click("Tab_Generic_Settings")

def test_SetGainSliderAcq(): 
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Generic_Settings")
        obj.click("Tab_Auto_Gain_Mode_Intensity")
        movePos = obj.GetCalSliderMovePos("Label_Gain_Min","Label_Gain_Max")
        obj.MoveUp("Slider_Auto_Gain_Mode_Intensity",movePos*10,0)        
      
        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Image_Adjustments")
        obj.click("Tab_Generic_Settings")

def test_SetStrobeMode():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_CameraAcq_Settings")
        obj.click("Tab_Lighting_Settings")
        movePos = obj.GetCalSliderMovePos("Label_Flash_LED_Mode_Min","Label_Flash_LED_Mode_Max")
        obj.MoveUp("Slider_Flash_LED_Mode",movePos*5,0)        
        SleepWaitForMachine()
        
        obj.click("Button_PlayPause")
        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Lighting_Settings")
        obj.click("Tab_CameraAcq_Settings")
    
def test_SetStrobeGainMode():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_CameraAcq_Settings")
        obj.click("Tab_Lighting_Settings")
        movePos = obj.GetCalSliderMovePos("Label_Flash_LED_Mode_Min","Label_Flash_LED_Mode_Max")
        obj.MoveUp("Slider_Flash_LED_Mode",movePos*5,0)        
        movePos = obj.GetCalSliderMovePos("Label_Flash_LED_Gain_Min","Label_Flash_LED_Gain_Max")
        obj.MoveUp("Slider_Flash_LED_Gain",movePos*10,0)        
        SleepWaitForMachine()
        
        obj.click("Button_PlayPause")
        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Tab_Lighting_Settings")
        obj.click("Tab_CameraAcq_Settings")

#Set LED Color Green
def test_SetLEDColorGreen():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Platform_LED")
        obj.click("Switch_SYSLED")
        obj.click("Radio_SYSLED_Green")

        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        obj.click("Switch_SYSLED")
        obj.click("Tab_Platform_LED")
        #obj.click("Button_DisconnectConnect")
        #obj.click("Button_Popup_Window_Ok")


#Set LED Color Orange
def test_SetLEDColorOrange():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Platform_LED")
        obj.click("Switch_SYSLED")
        obj.click("Radio_SYSLED_Orange")

        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        #obj.click("Button_DisconnectConnect")
        #obj.click("Button_Popup_Window_Ok")
        obj.click("Switch_SYSLED")
        obj.click("Tab_Platform_LED")

#Set LED Color Yellow
def test_SetLEDColorYellow():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_Platform_LED")
        obj.click("Switch_SYSLED")
        obj.click("Radio_SYSLED_Yellow")

        obj.click("Button_PlayPause")

        SleepAfterPlayPause()
                
        fpsText = obj.GetInputBoxText("InputBox_FPS")   
        CameraState = obj.GetText("Label_CameraState")        
        ButtonState = obj.GetText("Button_PlayPause")
        before = CameraState
        after  = ''
        if("Playing"==before and ButtonState=="Pause"):
            after  =  "Paused"
        elif(("Paused"==before  or "Connected"==before )and ButtonState=="Play"):
            after  =  "Playing"
        else:
            logging.warning("按鈕與設備狀態不匹配")

        obj.click("Button_PlayPause")  
  
        result = obj.GetText("Label_CameraState")
        
        if( after == result and fpsText != '' ):
            logging.info( "FPS:" + fpsText )
            assert True
        else:
            assert False,Exception("result different")                
    except Exception:
        assert False        
    finally:
        #obj.click("Button_DisconnectConnect")
        #obj.click("Button_Popup_Window_Ok")
        obj.click("Switch_SYSLED")
        obj.click("Tab_Platform_LED")


#DIO Setting
def test_DO0UserOutput():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_IO_Settings")
        obj.click("Tab_DI1")
        obj.click("Tab_DO1")
        obj.click("Tab_DO1_Parameters")
        
        obj.click("Button_DO1_Output_High")
        SleepWaitForMachine()
        
        diStatus = obj.GetText("Label_DI1_Status")
        if( diStatus ==  '(H)' ):
            logging.info( "DI0 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")

        obj.click("Button_DO1_Output_Low")
        SleepWaitForMachine()
        
        diStatus = obj.GetText("Label_DI1_Status")
        if( diStatus ==  '(L)' ):
            logging.info( "DI0 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")        
           
    except Exception:
        assert False        
    finally:
        obj.click("Tab_DO1_Parameters")
        obj.click("Tab_DI1")
        obj.click("Tab_DO1")
        obj.click("Tab_IO_Settings")

def test_DO1UserOutput():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_IO_Settings")
        obj.click("Tab_DI2")
        obj.click("Tab_DO2")
        obj.click("Tab_DO2_Parameters")
        
        obj.click("Button_DO2_Output_High")
        SleepWaitForMachine()
        
        diStatus = obj.GetText("Label_DI2_Status")
        if( diStatus ==  '(H)' ):
            logging.info( "DI1 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")

        obj.click("Button_DO2_Output_Low")
        SleepWaitForMachine()
        
        diStatus = obj.GetText("Label_DI2_Status")
        if( diStatus ==  '(L)' ):
            logging.info( "DI1 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")        
           
    except Exception:
        assert False        
    finally:
        obj.click("Tab_DO2_Parameters")
        obj.click("Tab_DI2")
        obj.click("Tab_DO2")
        obj.click("Tab_IO_Settings")

def test_DO0InvertUserOutput():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_IO_Settings")
        obj.click("Tab_DI1")
        obj.click("Tab_DO1")
        obj.click("Tab_DO1_Parameters")
        obj.click("Radio_DO1_Reverse_On")
        
        obj.click("Button_DO1_Output_High")
        SleepWaitForMachine()
        
        diStatus = obj.GetText("Label_DI1_Status")
        if( diStatus ==  '(L)' ):
            logging.info( "DI0 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")

        obj.click("Button_DO1_Output_Low")
        SleepWaitForMachine()
        
        diStatus = obj.GetText("Label_DI1_Status")
        if( diStatus ==  '(H)' ):
            logging.info( "DI0 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")        
           
    except Exception:
        assert False        
    finally:
        obj.click("Radio_DO1_Reverse_Off")
        obj.click("Tab_DO1_Parameters")
        obj.click("Tab_DI1")
        obj.click("Tab_DO1")
        obj.click("Tab_IO_Settings")

def test_DO1InvertUserOutput():
    obj = get_Web2Object()
    
    
    SleepAfterGetObj()
    try:   
        CameraState = obj.GetText("Label_CameraState")
        if(CameraState == "Disconnected"):
            obj.click("Button_DisconnectConnect")
            obj.click("Button_Popup_Window_Ok")

        obj.click("Tab_IO_Settings")
        obj.click("Tab_DI2")
        obj.click("Tab_DO2")
        obj.click("Tab_DO2_Parameters")
        obj.click("Radio_DO2_Reverse_On")
        obj.click("Button_DO2_Output_High")
        SleepWaitForMachine()
        
        diStatus = obj.GetText("Label_DI2_Status")
        if( diStatus ==  '(L)' ):
            logging.info( "DI1 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")

        obj.click("Button_DO2_Output_Low")
        SleepWaitForMachine()
        
        diStatus = obj.GetText("Label_DI2_Status")
        if( diStatus ==  '(H)' ):
            logging.info( "DI1 Status:" + diStatus )
            assert True
        else:
            assert False,Exception("result different")        
    except Exception:
        assert False        
    finally:
        obj.click("Radio_DO2_Reverse_Off")
        obj.click("Tab_DO2_Parameters")
        obj.click("Tab_DI2")
        obj.click("Tab_DO2")
        obj.click("Tab_IO_Settings")
#endregion ===============================page2===============================