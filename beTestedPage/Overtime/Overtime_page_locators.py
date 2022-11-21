#Detail
import sys,os
sys.path.append(os.getcwd())
from base_locators import LocatorsObj , EnumUIType ,logging ,json ,Tuple ,TypeVar ,Generic
from selenium.webdriver.common.by import By
#By 可以選擇要使用的篩選器 有NAME、ID、XPATH
#必須依照介面位置排放，以免找不到元件

#命名規則
# 元件種類(型別)_功能_細節
class cOverTimePagelocators:

    RecvType = TypeVar('RecvType', LocatorsObj, str,Tuple)

    # def GetElementType(self,UIInput:Generic[RecvType])->(Tuple):
    #     #從傳遞進來的輸入取出element並回傳
    #     elemt = None
    #     #方法1.字串索引表檢索
    #     if isinstance(UIInput, str): 
    #         if UIInput in self.UI_dict:
    #             logging.warning('GetElementType: '+UIInput+'is be found.') #修正記錄檔顯示文字
    #             elemt=self.UI_dict[UIInput].elemt
    #         else:
    #             logging.warning('GetElementType: '+UIInput+'not found!') #修正記錄檔顯示文字
    #             return None
    #     #方法2.LocatorsObj物件檢索
    #     elif isinstance(UIInput,LocatorsObj): 
    #         elemt=UIInput.elemt
    #     #方法3.elemt物件本身檢索   
    #     elif isinstance(UIInput,Tuple):    
    #         elemt=UIInput
            
    #     return elemt

    #存放LocatorsObj容器
    UI_dict ={}
    UI_List =[]

    def __init__(self):#建構式
    #介面元件
        self.UI_List.clear()
        self.UI_dict.clear()    
        self.Button_HomePage                         = LocatorsObj(self.UI_List,"Button_HomePage",EnumUIType.Button,'/html/body/div/div/div[1]/img')
        self.Button_PlayPause                        = LocatorsObj(self.UI_List,"Button_PlayPause",EnumUIType.Button,'/html/body/div/div/div[2]/div/div/div[1]/div/div/div/ul/li/span/span/button[1]')
        self.Button_Save                             = LocatorsObj(self.UI_List,"Button_Save",EnumUIType.Button,'/html/body/div/div/div[2]/div/div/div[1]/div/div/div/ul/li/span/span/button[2]')
        self.Button_DisconnectConnect                = LocatorsObj(self.UI_List,"Button_DisconnectConnect",EnumUIType.Button,'/html/body/div/div/div[2]/div/div/div[1]/div/div/div/ul/li/span/span/button[3]')
        self.InputBox_FPS                            = LocatorsObj(self.UI_List,"InputBox_FPS",EnumUIType.InputBox,'/html/body/div/div/div[2]/div/div/div[1]/div/div/div/ul/li/span/span/span[1]/input')
        self.InputBox_Focus                          = LocatorsObj(self.UI_List,"InputBox_Focus",EnumUIType.InputBox,'/html/body/div/div/div[2]/div/div/div[1]/div/div/div/ul/li/span/span/span[2]/input')
        self.Label_CameraState                       = LocatorsObj(self.UI_List,"Label_CameraState",EnumUIType.Label,'/html/body/div/div/div[2]/div/div/div[1]/div/div/p/span')
            
        self.Tab_CameraAcq_Settings                  = LocatorsObj(self.UI_List,"Tab_CameraAcq_Settings",EnumUIType.Tab,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[1]')
        
        #Class Popup Window Button:
        self.Button_Popup_Window_Ok                  = LocatorsObj(self.UI_List, "Button_Popup_Window_Ok", EnumUIType.Button, '/html/body/div[2]/div/div[6]/button[1]')
        self.Button_Popup_Window_Ok2                 = LocatorsObj(self.UI_List, "Button_Popup_Window_Ok2", EnumUIType.Button, '/html/body/div[3]/div/div[6]/button[1]')
        
        #class ClsCameraAcq_Settings:    
        self.Tab_Trigger_Mode_Settings               = LocatorsObj(self.UI_List,"Tab_Trigger_Mode_Settings",EnumUIType.Tab,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[1]/div[1]')
        #class ClsTrigger_Mode_Settings:            
        self.Radio_HW_Trigger_Mode                   = LocatorsObj(self.UI_List,"Radio_HW_Trigger_Mode",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/label/span[1]/input')
        self.Radio_SW_Trigger_Mode                   = LocatorsObj(self.UI_List,"Radio_SW_Trigger_Mode",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/span[1]/label/span[1]/input')
        self.Button_SW_Trigger_Trigger               = LocatorsObj(self.UI_List,"Button_SW_Trigger_Trigger", EnumUIType.Button, "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/span[1]/button")
        self.Radio_Continuous_Mode                   = LocatorsObj(self.UI_List,"Radio_Continuous_Mode",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/span[2]/label/span[1]/input')
        self.Input_Sensor_Frame_Rate                 = LocatorsObj(self.UI_List,"Input_Sensor_Frame_Rate",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/span[2]/span/span/input')
    
        self.Tab_Focus_Settings                      = LocatorsObj(self.UI_List,"Tab_Focus_Settings",EnumUIType.Tab,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[2]/div[1]')
        #class ClsFocus_Settings:        
        self.Button_ZoomIn                           = LocatorsObj(self.UI_List,"Button_ZoomIn",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div/button[1]')
        self.Button_ZoomOut                          = LocatorsObj(self.UI_List,"Button_ZoomOut",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div/button[2]')
        self.Input_Focus_Step_Distance               = LocatorsObj(self.UI_List,"Input_Focus_Step_Distance",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/span/span/span/input')
        self.Button_Reset_to_Zero_Position           = LocatorsObj(self.UI_List,"Button_Reset_to_Zero_Position",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/button')
    
        self.Tab_Lighting_Settings                   = LocatorsObj(self.UI_List,"Tab_Lighting_Settings",EnumUIType.Tab,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[1]')
        #class ClsLighting_Settings:
        self.Button_StrobeOrNot                      = LocatorsObj(self.UI_List,"Button_StrobeOrNot",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/button')
        self.Slider_Flash_LED_Mode                   = LocatorsObj(self.UI_List,"Slider_Flash_LED_Mode",EnumUIType.Slider,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[4]')        
        self.Slider_Flash_LED_Gain                   = LocatorsObj(self.UI_List,"Slider_Flash_LED_Gain",EnumUIType.Slider,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div[3]')
        self.Input_Delay                             = LocatorsObj(self.UI_List,"Input_Delay",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[3]/div/div[1]/span/div/div[2]')
        self.Input_Duration                          = LocatorsObj(self.UI_List,"Input_Duration",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[3]/div/div[2]/span/div/div[2]')
        self.Label_Flash_LED_Mode_Min                = LocatorsObj(self.UI_List, "Label_Flash_LED_Mode_Min", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[5]/span[1]')
        self.Label_Flash_LED_Mode_Max                = LocatorsObj(self.UI_List, "Label_Flash_LED_Mode_Max", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[5]/span[2]')
        self.Label_Flash_LED_Gain_Min                = LocatorsObj(self.UI_List, "Label_Flash_LED_Gain_Min", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div[5]/span[1]')
        self.Label_Flash_LED_Gain_Max                = LocatorsObj(self.UI_List, "Label_Flash_LED_Gain_Max", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div[5]/span[2]')



        self.Tab_Generic_Settings                    = LocatorsObj(self.UI_List,"Tab_Generic_Settings",EnumUIType.Tab,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[1]')
        #class ClsGeneric_Settings:
        self.Tab_Pixel_Format                        = LocatorsObj(self.UI_List,"Tab_Pixel_Format",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[1]/div[1]')
        #class ClsPixel_Format:
        self.Radio_GRAY8                            = LocatorsObj(self.UI_List,"Radio_GRAY8",EnumUIType.Radio,'')
        self.Radio_YUV2                               = LocatorsObj(self.UI_List,"Radio_YUV2",EnumUIType.Radio,'')
    
        self.Tab_Image_Parameters                   = LocatorsObj(self.UI_List,"Tab_Image_Parameters",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[1]')
        #class ClsImage_Parameters:
        #ColorHue
        #ColorSaturation
        
        self.Slider_Brightness                       = LocatorsObj(self.UI_List,"Slider_Brightness",EnumUIType.Slider,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[4]')
        self.Slider_Sharpness                        = LocatorsObj(self.UI_List,"Slider_Sharpness",EnumUIType.Slider,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[4]')
        self.Slider_Gamma                            = LocatorsObj(self.UI_List,"Slider_Gamma",EnumUIType.Slider,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div[1]/div[4]')
        self.Slider_Contrast                         = LocatorsObj(self.UI_List,"Slider_Contrast",EnumUIType.Slider,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/div/div[1]/div[4]')
        self.Slider_Saturation                       = LocatorsObj(self.UI_List,"Slider_Saturation",EnumUIType.Slider,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div/div[1]/div[4]')
        self.Input_Brightness                        = LocatorsObj(self.UI_List,"Input_Brightness",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div[2]/input')
        self.Input_Sharpness                         = LocatorsObj(self.UI_List,"Input_Sharpness",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/input')
        self.Input_Gamma                             = LocatorsObj(self.UI_List,"Input_Gamma",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/input')
        self.Input_Contrast                          = LocatorsObj(self.UI_List,"Input_Contrast",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div[2]/input')
        self.Input_Saturation                        = LocatorsObj(self.UI_List,"Input_Saturation",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div/div[2]/div[2]/input')
        self.Button_MirrorX                          = LocatorsObj(self.UI_List,"Button_MirrorX",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[6]/button')
        self.Label_Brightness_Min                    = LocatorsObj(self.UI_List, "Label_Brightness_Min", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[5]/span[1]')
        self.Label_Brightness_Max                    = LocatorsObj(self.UI_List, "Label_Brightness_Max", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[5]/span[2]')
        self.Label_Sharpness_Min                     = LocatorsObj(self.UI_List, "Label_Sharpness_Min", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[5]/span[1]')
        self.Label_Sharpness_Max                     = LocatorsObj(self.UI_List, "Label_Sharpness_Max", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[5]/span[2]')
        self.Label_Gamma_Min                         = LocatorsObj(self.UI_List, "Label_Gamma_Min", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div[1]/div[5]/span[1]')
        self.Label_Gamma_Max                         = LocatorsObj(self.UI_List, "Label_Gamma_Max", EnumUIType.Label, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div[1]/div[5]/span[2]')



        self.Tab_Auto_Exposure_Mode                  = LocatorsObj(self.UI_List,"Tab_Auto_Exposure_Mode",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[3]/div[1]')
        #class ClsAuto_Exposure_Mode:
        self.Input_Auto_Exposure_Time                = LocatorsObj(self.UI_List,"Input_Auto_Exposure_Time",EnumUIType.Input,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/span/div/div[2]/input')
        self.Switch_Auto_Exposure_Time               = LocatorsObj(self.UI_List,"Switch_Auto_Exposure_Time",EnumUIType.Switch,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/button')
        self.Input_Auto_Exposure_Time_Min            = LocatorsObj(self.UI_List,"Input_Auto_Exposure_Time_Min",EnumUIType.Input,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]/input')
        self.Input_Auto_Exposure_Time_Max            = LocatorsObj(self.UI_List,"Input_Auto_Exposure_Time_Max",EnumUIType.Input,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[3]/div/div[2]/input')
        self.Button_Auto_Exposure_Time_Confirm        = LocatorsObj(self.UI_List,"Button_Auto_Exposure_Time_Confirm",EnumUIType.Button,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[4]/button[1]')
        self.Button_Auto_Exposure_Time_Reset         = LocatorsObj(self.UI_List,"Button_Auto_Exposure_Time_Reset",EnumUIType.Button,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[4]/button[2]')

        self.Tab_Auto_Gain_Mode_Intensity            = LocatorsObj(self.UI_List,"Tab_Auto_Gain_Mode_Intensity",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[1]')
        #class ClsAuto_Gain_Mode_Intensity:
        self.Slider_Auto_Gain_Mode_Intensity         = LocatorsObj(self.UI_List,"Slider_Auto_Gain_Mode_Intensity",EnumUIType.Slider,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/div/div[1]/div[4]')
        self.Label_Gain_Min                          = LocatorsObj(self.UI_List,"Label_Gain_Min",EnumUIType.Label,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/div/div[1]/div[5]/span[1]')
        self.Label_Gain_Max                          = LocatorsObj(self.UI_List,"Label_Gain_Max",EnumUIType.Label,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/div/div[1]/div[5]/span[2]')
        self.Input_Auto_Gain_Mode_Intensity          = LocatorsObj(self.UI_List,"Input_Auto_Gain_Mode_Intensity",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/input')
        self.Switch_Auto_Gain_Mode_Intensity         = LocatorsObj(self.UI_List,"Switch_Auto_Gain_Mode_Intensity",EnumUIType.Switch,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[2]/div/div/button')
        self.Input_Auto_Gain_Mode_Intensity_Min      = LocatorsObj(self.UI_List,"Input_Auto_Gain_Mode_Intensity_Min",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/input')
        self.Input_Auto_Gain_Mode_Intensity_Max      = LocatorsObj(self.UI_List,"Input_Auto_Gain_Mode_Intensity_Max",EnumUIType.Input,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[3]/input')
        self.Button_Auto_Gain_Mode_Intensity_Enable  = LocatorsObj(self.UI_List,"Button_Auto_Gain_Mode_Intensity_Enable",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[4]/button[1]')
        self.Button_Auto_Gain_Mode_Intensity_Reset   = LocatorsObj(self.UI_List,"Button_Auto_Gain_Mode_Intensity_Reset",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[4]/button[2]')


        self.Tab_ROI_Settings_Output_Resolution      = LocatorsObj(self.UI_List,"Tab_ROI_Settings_Output_Resolution",EnumUIType.Tab,'/html/body/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[3]/div[1]')
        self.Radio_1280x960                          = LocatorsObj(self.UI_List,"Radio_1280x960",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[3]/div[2]/div/div/div/div[2]/label[1]/span[1]/input')
        self.Radio_640x480                           = LocatorsObj(self.UI_List,"Radio_640x480",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[3]/div[2]/div/div/div/div[2]/label[2]/span[1]/input')
        self.Radio_320x240                           = LocatorsObj(self.UI_List,"Radio_320x240",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div[3]/div[2]/div/div/div/div[2]/label[3]/span[1]/input')
        
        #Platform Settings
        self.Tab_IO_Settings                         = LocatorsObj(self.UI_List,"Tab_IO_Settings",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]')
        #class ClsIO_Settings:
        self.Tab_DI1                                 = LocatorsObj(self.UI_List,"Tab_DI1",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div')
        self.Tab_DI2                                 = LocatorsObj(self.UI_List,"Tab_DI2",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div')
        self.Tab_DO1                                 = LocatorsObj(self.UI_List,"Tab_DO1",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div')
        self.Tab_DO1_Parameters                      = LocatorsObj(self.UI_List,"Tab_DO1_Parameters", EnumUIType.Tab, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div')
        self.Tab_DO2                                 = LocatorsObj(self.UI_List,"Tab_DO2",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div')
        self.Tab_DO2_Parameters                      = LocatorsObj(self.UI_List,"Tab_DO2_Parameters", EnumUIType.Tab, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div')
        
        #DI Parameters
        #DI1
        self.Label_DI1_Status                       = LocatorsObj(self.UI_List, "Label_DI1_Status", EnumUIType.Label, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[1]/p[2]')
        self.Switch_DI1_Invert                      = LocatorsObj(self.UI_List, "Switch_DI1_Invert", EnumUIType.Switch, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[3]/button')
        self.Switch_DI1_Interrupt                   = LocatorsObj(self.UI_List, "Switch_DI1_Interrupt", EnumUIType.Switch, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[4]/button')
        self.Input_DI1_Debounce_Time                = LocatorsObj(self.UI_List, "Input_DI1_Debounce_Time", EnumUIType.Input, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[5]/span/div/div[2]/input')
        self.Radio_DI1_Edge_Trigger_Rising_Edge     = LocatorsObj(self.UI_List, "Radio_DI1_Edge_Trigger_Rising_Edge", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[7]/label[1]/span[1]/input')
        self.Radio_DI1_Edge_Trigger_Falling_Edge    = LocatorsObj(self.UI_List, "Radio_DI1_Edge_Trigger_Falling_Edge", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[7]/label[2]/span[1]/input')
        self.Radio_DI1_Edge_Trigger_Both            = LocatorsObj(self.UI_List, "Radio_DI1_Edge_Trigger_Both", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[7]/label[3]/span[1]/input')
        #DI2
        self.Label_DI2_Status                       = LocatorsObj(self.UI_List, "Label_DI2_Status", EnumUIType.Label, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/p[2]')
        self.Switch_DI2_Invert                      = LocatorsObj(self.UI_List, "Switch_DI2_Invert", EnumUIType.Switch, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[3]/button')
        self.Switch_DI2_Interrupt                   = LocatorsObj(self.UI_List, "Switch_DI2_Interrupt", EnumUIType.Switch, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[4]/button')
        self.Input_DI2_Debounce_Time                = LocatorsObj(self.UI_List, "Input_DI2_Debounce_Time", EnumUIType.Input, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[5]/span/div/div[2]/input')
        self.Radio_DI2_Edge_Trigger_Rising_Edge     = LocatorsObj(self.UI_List, "Radio_DI2_Edge_Trigger_Rising_Edge", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[7]/label[1]/span[1]/input')
        self.Radio_DI2_Edge_Trigger_Falling_Edge    = LocatorsObj(self.UI_List, "Radio_DI2_Edge_Trigger_Falling_Edge", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[7]/label[2]/span[1]/input')
        self.Radio_DI2_Edge_Trigger_Both            = LocatorsObj(self.UI_List, "Radio_DI2_Edge_Trigger_Both", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[7]/label[3]/span[1]/input')
        
        #DO Parameters
        #DO1
        self.Label_DO1_Status                        = LocatorsObj(self.UI_List, "Label_DO1_Status", EnumUIType.Label, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[1]/p/text()[2]')
        self.Button_DO1_Output_High                  = LocatorsObj(self.UI_List, "Button_DO1_Output_High", EnumUIType.Button, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/button')
        self.Button_DO1_Output_Low                   = LocatorsObj(self.UI_List, "Button_DO1_Output_Low", EnumUIType.Button, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/button')
        self.Radio_DO1_Mode_Direct_Output            = LocatorsObj(self.UI_List, "Radio_DO1_Mode_Direct_Output", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[4]/label[1]/span[1]/input')
        self.Radio_DO1_Mode_ByPassDI1                = LocatorsObj(self.UI_List, "Radio_DO1_Mode_ByPassDI1", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[4]/label[2]/span[1]/input')
        self.Radio_DO1_Reverse_On                    = LocatorsObj(self.UI_List, "Radio_DO1_Reverse_On", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[6]/label[2]/span[1]/input')
        self.Radio_DO1_Reverse_Off                   = LocatorsObj(self.UI_List, "Radio_DO1_Reverse_Off", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[6]/label[1]/span[1]/input')
        self.Input_DO1_Delay_Time                    = LocatorsObj(self.UI_List, "Input_DO1_Delay_Time", EnumUIType.Input, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[7]/span/div/div[2]/input')
        #DO2
        self.Label_DO2_Status                        = LocatorsObj(self.UI_List, "Label_DO1_Status", EnumUIType.Label, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[1]/p/text()[2]')
        self.Button_DO2_Output_High                  = LocatorsObj(self.UI_List, "Button_DO2_Output_High", EnumUIType.Button, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/button')
        self.Button_DO2_Output_Low                   = LocatorsObj(self.UI_List, "Button_DO2_Output_Low", EnumUIType.Button, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/button')
        self.Radio_DO2_Mode_Direct_Output            = LocatorsObj(self.UI_List, "Radio_DO2_Mode_Direct_Output", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div[2]/div/div[4]/label[1]/span[1]/input')
        self.Radio_DO2_Mode_ByPassDI1                = LocatorsObj(self.UI_List, "Radio_DO2_Mode_ByPassDI1", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div[2]/div/div[4]/label[2]/span[1]/input')
        self.Radio_DO2_Reverse_On                    = LocatorsObj(self.UI_List, "Radio_DO2_Reverse_On", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div[2]/div/div[6]/label[2]/span[1]/input')
        self.Radio_DO2_Reverse_Off                   = LocatorsObj(self.UI_List, "Radio_DO2_Reverse_Off", EnumUIType.Radio, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div[2]/div/div[6]/label[1]/span[1]/input')
        self.Input_DO2_Delay_Time                    = LocatorsObj(self.UI_List, "Input_DO2_Delay_Time", EnumUIType.Input, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div[2]/div/div[7]/span/div/div[2]/input')



        self.Tab_Platform_LED                        = LocatorsObj(self.UI_List,"Tab_Platform_LED",EnumUIType.Tab,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]')
        #class ClsPlatform_LED:
        self.Switch_SYSLED                           = LocatorsObj(self.UI_List,"Switch_SYSLED",EnumUIType.Switch,'/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/button')
        self.Radio_SYSLED_Green                      = LocatorsObj(self.UI_List,"Radio_SYSLED_Green",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/label[1]/span[1]/input')
        self.Radio_SYSLED_Orange                     = LocatorsObj(self.UI_List,"Radio_SYSLED_Orange",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/label[2]/span[1]/input')
        self.Radio_SYSLED_Yellow                     = LocatorsObj(self.UI_List,"Radio_SYSLED_Yellow",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/label[3]/span[1]/input')

        #List轉Dict
        for i in range(len(self.UI_List)):
            jsonName=json.loads(self.UI_List[i].InfoJson)#讀取整個Json結構
            self.UI_dict.setdefault(jsonName['Name'],self.UI_List[i])#轉換到UI_dict途中

