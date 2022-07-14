#Project
import sys,os
sys.path.append(os.getcwd())
from base_locators import LocatorsObj , EnumUIType , logging ,json , Tuple ,TypeVar ,Generic
#By 可以選擇要使用的篩選器 有NAME、ID、XPATH
#必須依照介面位置排放，以免找不到元件


#命名規則
# 元件種類(型別)_功能_細節
class cProjectPageLocators:

    RecvType = TypeVar('RecvType', LocatorsObj, str,Tuple)

    def GetElementType(self,UIInput:Generic[RecvType])->Tuple:
        #從傳遞進來的輸入取出element並回傳
        elemt = None
        if isinstance(UIInput, str): #字串索引表檢索
            if UIInput in self.UI_dict:
                logging.warning('GetElementType: '+UIInput+'is none.')
                elemt=self.UI_dict[UIInput].elemt
            else:
                print( "height not found" )
                return None
        # #運作異常 取消    
        # elif isinstance(UIInput,LocatorsObj.elemt): #element檢索
        #     elemt=UIInput
        elif isinstance(UIInput,LocatorsObj): #定位器物件本身檢索
            elemt=UIInput.elemt
        elif isinstance(UIInput,Tuple):                
            elemt=UIInput
        return elemt

    #存放LocatorsObj容器
    UI_dict ={}
    UI_List =[]

    def __init__(self):#建構式
    #介面元件
        self.UI_List.clear()
        self.UI_dict.clear()
        
        self.Project_radio_0                 = LocatorsObj(self.UI_List,"Project_radio_0",EnumUIType.Radio,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/label/span/input')
        self.Project_Name_0                  = LocatorsObj(self.UI_List,"Project_Name_0",EnumUIType.Label,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]')
        self.Project_Date_0                  = LocatorsObj(self.UI_List,"Project_Date_0",EnumUIType.Label,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[3]')    
        self.Project_Description_0           = LocatorsObj(self.UI_List,"Project_Description_0",EnumUIType.Label,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]')    
        self.Project_StatusIcon_0            = LocatorsObj(self.UI_List,"Project_StatusIcon_0",EnumUIType.Label,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/span/svg')
        self.Delete_button_0                 = LocatorsObj(self.UI_List,"Delete_button_0",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div[1]/button')
        self.Modify_button_0                 = LocatorsObj(self.UI_List,"Modify_button_0",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div[2]/button')
        self.Disconnect_button_0             = LocatorsObj(self.UI_List,"Disconnect_button_0",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div[3]/button')
        
        self.Project_radio_1                 = LocatorsObj(self.UI_List,"Project_radio_1",EnumUIType.Radio,'/html/body/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[1]/label/span/input')
        
        #Main button        
        self.Button_Global_Settings          = LocatorsObj(self.UI_List,"Button_Global_Settings",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[1]/div[3]/span/button[1]/span/svg/path')
        #class ClsGlobal_Settings:
        
        #class Device_IP_Settings:      
        self.Tab_Device_IP_Settings          = LocatorsObj(self.UI_List,"Tab_Device_IP_Settings",EnumUIType.Tab,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]')
        self.Radio_Static_IP                 = LocatorsObj(self.UI_List,"Radio_Static_IP",EnumUIType.Radio,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/label[1]/span[2]')
        self.Radio_DHCP                      = LocatorsObj(self.UI_List,"Radio_DHCP",EnumUIType.Radio,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/label[2]/span[2]')
        self.Input_IP_Address                = LocatorsObj(self.UI_List,"Input_IP_Address",EnumUIType.Input,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/input')
        self.Input_Subnet_Mask               = LocatorsObj(self.UI_List,"Input_Subnet_Mask",EnumUIType.Input,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/input')    
        self.Button_Device_IP_Apply          = LocatorsObj(self.UI_List,"Button_Device_IP_Apply",EnumUIType.Button,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/button[1]/span')
        self.Button_Device_IP_Cancel         = LocatorsObj(self.UI_List,"Button_Device_IP_Cancel",EnumUIType.Button,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/button[2]/span')
        #class ClsFirmware:          
        self.Tab_Firmware                    = LocatorsObj(self.UI_List,"Tab_Firmware",EnumUIType.Tab,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]')
        self.Button_Load_FW_File             = LocatorsObj(self.UI_List,"Button_Load_FW_File",EnumUIType.Button,' /html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/span/div[1]/span/button')

        self.Button_Global_Cancel            = LocatorsObj(self.UI_List,"Button_Global_Cancel",EnumUIType.Button,'/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]')
        self.Button_Global_OK                = LocatorsObj(self.UI_List,"Button_Global_OK",EnumUIType.Button,'/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]')

        #New Project button
        self.Button_New_Project              = LocatorsObj(self.UI_List,"Button_New_Project",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/span')
        #class ClsNew_Project:   
        self.Input_ProjectName               = LocatorsObj(self.UI_List,"Input_ProjectName",EnumUIType.Input,'/html/body/div[10]/div/div[2]/div/div[2]/div[2]/div/div[1]/input')
        self.Input_Description               = LocatorsObj(self.UI_List,"Input_Description",EnumUIType.Input,'/html/body/div[10]/div/div[2]/div/div[2]/div[2]/div/div[2]/input')
        self.List_Camera                     = LocatorsObj(self.UI_List,"List_Camera",EnumUIType.Button,'/html/body/div[10]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/span[2]')
        self.List_Camera_Select              = LocatorsObj(self.UI_List,"List_Camera_Select",EnumUIType.ComboBox,'/html/body/div[11]/div/div/div/div[2]/div[1]/div/div/div/div')
        self.List_Output_Resolutions         = LocatorsObj(self.UI_List,"List_Output_Resolutions",EnumUIType.Button,'/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[4]/div')
        self.List_Output_Resolutions_Select0 = LocatorsObj(self.UI_List,"List_Output_Resolutions_Select0",EnumUIType.ComboBox,'/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]/div')        
        self.List_Output_Resolutions_Select1 = LocatorsObj(self.UI_List,"List_Output_Resolutions_Select1",EnumUIType.ComboBox,'/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[2]/div')
        self.List_Output_Resolutions_Select2 = LocatorsObj(self.UI_List,"List_Output_Resolutions_Select2",EnumUIType.ComboBox,'/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[3]/div')
        self.List_Trigger_Mode               = LocatorsObj(self.UI_List,"List_Trigger_Mode",EnumUIType.Button,'/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[5]/div/div/span[2]')
        self.List_Trigger_Mode_Select0       = LocatorsObj(self.UI_List,"List_Trigger_Mode_Select0",EnumUIType.ComboBox,'/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[1]/div')
        self.List_Trigger_Mode_Select1       = LocatorsObj(self.UI_List,"List_Trigger_Mode_Select1",EnumUIType.ComboBox,'/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[2]/div')
        self.List_Trigger_Mode_Select2       = LocatorsObj(self.UI_List,"List_Trigger_Mode_Select2",EnumUIType.ComboBox,'/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[3]/div')
        self.Button_New_Project_Cancel       = LocatorsObj(self.UI_List,"Button_New_Project_Cancel",EnumUIType.Button,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[1]')
        self.Button_New_Project_Comfirm      = LocatorsObj(self.UI_List,"Button_New_Project_Comfirm",EnumUIType.Button,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]/span')    
        self.Button_Next                     = LocatorsObj(self.UI_List,"Button_Next",EnumUIType.Button,'/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[4]/button')

        #List轉Dict
        for i in range(len(self.UI_List)):
            jsonName=json.loads(self.UI_List[i].InfoJson)#讀取整個Json結構
            self.UI_dict.setdefault(jsonName['Name'],self.UI_List[i])#轉換到UI_dict途中
