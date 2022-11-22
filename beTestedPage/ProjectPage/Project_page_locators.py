#Project
import sys,os
sys.path.append(os.getcwd())
from base_locators import GetElementType,LocatorsObj , EnumUIType , logging ,json , Tuple ,TypeVar ,Generic
from selenium.webdriver.common.by import By
#By 可以選擇要使用的篩選器 有NAME、ID、XPATH
#必須依照介面位置排放，以免找不到元件


#命名規則
# 元件種類(型別)_功能_細節
class cProjectPageLocators:

    RecvType = TypeVar('RecvType', LocatorsObj, str,Tuple)

    def GetElementType(self,UIInput:Generic[RecvType])->(Tuple):        
        return GetElementType(self,UIInput)

    #存放LocatorsObj容器
    UI_dict ={}
    UI_List =[]

    def __init__(self):#建構式
    #介面元件
        self.UI_List.clear()
        self.UI_dict.clear()
                
        self.Project_radio_0                 = LocatorsObj(self.UI_List,"Project_radio_0",EnumUIType.Radio,By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/label/span/input')
        self.Project_Name_0                  = LocatorsObj(self.UI_List,"Project_Name_0",EnumUIType.Label,By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]')
        self.Project_Date_0                  = LocatorsObj(self.UI_List,"Project_Date_0",EnumUIType.Label,By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[3]')
        self.Project_Description_0           = LocatorsObj(self.UI_List,"Project_Description_0",EnumUIType.Label,By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]')    
        self.Project_StatusIcon_0            = LocatorsObj(self.UI_List,"Project_StatusIcon_0",EnumUIType.Label,By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/span/svg')
        self.Delete_button_0                 = LocatorsObj(self.UI_List,"Delete_button_0",EnumUIType.Button,By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div[1]/button')
        self.Modify_button_0                 = LocatorsObj(self.UI_List,"Modify_button_0",EnumUIType.Button,By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div[2]/button')
        self.Disconnect_button_0             = LocatorsObj(self.UI_List,"Disconnect_button_0",EnumUIType.Button,By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div[3]/button')
    
        
        #Main button        
        self.Button_Global_Settings          = LocatorsObj(self.UI_List,"Button_Global_Settings",EnumUIType.Button,By.ID)
        #class ClsGlobal_Settings:
        
        #class Device_IP_Settings:      
        self.Tab_Device_IP_Settings          = LocatorsObj(self.UI_List,"Tab_Device_IP_Settings",EnumUIType.Tab,By.ID)
        self.Radio_Static_IP                 = LocatorsObj(self.UI_List,"Radio_Static_IP",EnumUIType.Radio,By.ID)
        self.Radio_DHCP                      = LocatorsObj(self.UI_List,"Radio_DHCP",EnumUIType.Radio,By.ID)
        self.Input_IP_Address                = LocatorsObj(self.UI_List,"Input_IP_Address",EnumUIType.Input,By.ID)
        self.Input_Subnet_Mask               = LocatorsObj(self.UI_List,"Input_Subnet_Mask",EnumUIType.Input,By.ID)
        self.Button_Device_IP_Apply          = LocatorsObj(self.UI_List,"Button_Device_IP_Apply",EnumUIType.Button,By.ID)
        self.Button_Device_IP_Cancel         = LocatorsObj(self.UI_List,"Button_Device_IP_Cancel",EnumUIType.Button,By.ID)
        
        #class ClsFirmware:          
        self.Tab_Firmware                    = LocatorsObj(self.UI_List,"Tab_Firmware",EnumUIType.Tab,By.ID)
        self.Button_Load_FW_File             = LocatorsObj(self.UI_List,"Button_Load_FW_File",EnumUIType.Button,By.ID)
        self.Button_StartUpload              = LocatorsObj(self.UI_List,"Button_StartUpload",EnumUIType.Button,By.ID)      
        self.Tab_Reset                       = LocatorsObj(self.UI_List,"Tab_Reset",EnumUIType.Tab,By.ID)
        self.Button_Reboot                   = LocatorsObj(self.UI_List,"Button_Reboot",EnumUIType.Button,By.ID)
        
        self.Button_Global_OK                = LocatorsObj(self.UI_List,"Button_Global_OK",EnumUIType.Button,By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]')
        self.Button_Global_Cancel            = LocatorsObj(self.UI_List,"Button_Global_Cancel",EnumUIType.Button,By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]')
        
        #New Project button
        self.Button_New_Project              = LocatorsObj(self.UI_List,"Button_New_Project",EnumUIType.Button,By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/span')
        
        #class ClsNew_Project:   
        self.Input_ProjectName               = LocatorsObj(self.UI_List,"Input_ProjectName",EnumUIType.Input,By.ID)
        self.Input_Description               = LocatorsObj(self.UI_List,"Input_Description",EnumUIType.Input,By.ID)
        self.List_Camera                     = LocatorsObj(self.UI_List,"List_Camera",EnumUIType.Button,By.ID)
        self.List_Camera_Select              = LocatorsObj(self.UI_List,"List_Camera_Select",EnumUIType.ComboBox,By.ID)
        self.List_Output_Resolutions         = LocatorsObj(self.UI_List,"List_Output_Resolutions",EnumUIType.Button,By.ID)
        self.List_Output_Resolutions_Select0 = LocatorsObj(self.UI_List,"List_Output_Resolutions_Select0",EnumUIType.ComboBox,By.ID)
        self.List_Output_Resolutions_Select1 = LocatorsObj(self.UI_List,"List_Output_Resolutions_Select1",EnumUIType.ComboBox,By.ID)
        self.List_Output_Resolutions_Select2 = LocatorsObj(self.UI_List,"List_Output_Resolutions_Select2",EnumUIType.ComboBox,By.ID)
        self.List_Output_Resolutions_Select3 = LocatorsObj(self.UI_List,"List_Output_Resolutions_Select3",EnumUIType.ComboBox,By.ID)
        self.List_Pixel_Format               = LocatorsObj(self.UI_List,"List_Pixel_Format",EnumUIType.Button,"List_Pixel_Format",By.ID)
        self.List_Pixel_Format_Select0       = LocatorsObj(self.UI_List,"List_Pixel_Format_Select0",EnumUIType.ComboBox,By.ID)
        self.List_Pixel_Format_Select1       = LocatorsObj(self.UI_List,"List_Pixel_Format_Select1",EnumUIType.ComboBox,By.ID)
        self.List_Pixel_Format_Select2       = LocatorsObj(self.UI_List,"List_Pixel_Format_Select2",EnumUIType.ComboBox,By.ID)
                
        self.List_Trigger_Mode               = LocatorsObj(self.UI_List,"List_Trigger_Mode",EnumUIType.Button,By.ID)
        self.List_Trigger_Mode_Select0       = LocatorsObj(self.UI_List,"List_Trigger_Mode_Select0",EnumUIType.ComboBox,By.ID)
        self.List_Trigger_Mode_Select1       = LocatorsObj(self.UI_List,"List_Trigger_Mode_Select1",EnumUIType.ComboBox,By.ID)
        self.List_Trigger_Mode_Select2       = LocatorsObj(self.UI_List,"List_Trigger_Mode_Select2",EnumUIType.ComboBox,By.ID)
        
        self.Button_New_Project_Cancel       = LocatorsObj(self.UI_List,"Button_New_Project_Cancel",EnumUIType.Button,By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[1]')
        self.Button_New_Project_Comfirm      = LocatorsObj(self.UI_List,"Button_New_Project_Comfirm",EnumUIType.Button,By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]/span')    
        self.Button_Next                     = LocatorsObj(self.UI_List,"Button_Next",EnumUIType.Button,By.ID)

        #List轉Dict
        for i in range(len(self.UI_List)):
            jsonName=json.loads(self.UI_List[i].InfoJson)#讀取整個Json結構
            self.UI_dict.setdefault(jsonName['Name'],self.UI_List[i])#轉換到UI_dict途中
