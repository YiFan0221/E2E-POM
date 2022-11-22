from enum import Enum, unique
from turtle import goto
from typing import Any, Tuple ,TypeVar ,Generic
from selenium.webdriver.common.by import By
import json
import logging
import sys,os
sys.path.append(os.getcwd())

@unique
class EnumUIType(Enum):
    Button  =0
    Input   =1
    InputBox=2    
    Tab     =3
    Slider  =4
    Switch  =5
    Radio   =6
    Label   =7
    ComboBox=8
    Table   =9
  
  
global RecvType 
RecvType = TypeVar('RecvType', str,Tuple)
  
def GetElementType(self,UIInput:Generic[RecvType])->(Tuple):
    #從傳遞進來的輸入取出element並回傳
    elemt = None
    #方法1.字串索引表檢索
    if isinstance(UIInput, str): 
        if UIInput in self.UI_dict:
            logging.warning('GetElementType: found '+UIInput+' elemt.') #修正記錄檔顯示文字
            elemt=self.UI_dict[UIInput].elemt
        else:
            logging.warning('GetElementType: elemt '+UIInput+' not found!') #修正記錄檔顯示文字
            return None
    #方法2.LocatorsObj物件檢索
    elif isinstance(UIInput,LocatorsObj): 
        elemt=UIInput.elemt
    #方法3.elemt物件本身檢索   
    elif isinstance(UIInput,Tuple):    
        elemt=UIInput            
    return elemt

class LocatorsObj():

    def elemt(self) -> (Tuple):
        #回傳用來找尋元件用的Elemt
        return self.elemt

    def InfoJson(self) -> (json):
        #直接回傳InfoJson本體
        return self.InfoJson

    #需要多載
    def __init__(self,UI_Dict,Name,ComponentType:EnumUIType,locatorStr,LocatorsType:By): 
        #關於定位器可以傳入什麼的說明
        #https://selenium-python.readthedocs.io/locating-elements.html

        #此函式範例:
        #(1)用X-PATH找
        #LocatorsObj(self.UI_List,"Project_radio_0",EnumUIType.Radio,'/html/body/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/label/span/input',By.XPATH)
        #(2)用ClassName找
        #LocatorsObj(self.UI_List,"Project_radio_0",EnumUIType.Radio,'ant-radio-input',By.CLASS_NAME)
        #(3)用id找
        #LocatorsObj(self.UI_List,"Project_radio_0",EnumUIType.Radio,'ant-radio-input',By.ID)

        self.elemt = (LocatorsType,locatorStr)

        obj= { #用Json方便擴充&傳遞屬性
            "Name":str(Name),
            "ComponentType":str(ComponentType.name),#定義元件種類     
            "locatorStr" :str(locatorStr),#定位器資料
            "LocatorsType":LocatorsType,
            "Necessary":str(""),#是否必要
            "Terminate":str(""), 
        }
        
        self.InfoJson = json.dumps(obj)#轉成Json格式儲存        
        #UI_Dict.setdefault(Name,self)
        UI_Dict.append(self)

    #Json中屬性的Getter 方便在加或加常用的就好~
    def Name(self) -> (str):
        Infodict=json.loads(self.InfoJson)
        return Infodict["Name"]
    
    def ComponentType(self) -> (str):
        Infodict=json.loads(self.InfoJson)
        return str(Infodict["ComponentType"])

    def locatorStr(self) -> (str):
        Infodict=json.loads(self.InfoJson)
        return Infodict["locatorStr"]

    def LocatorsType(self) ->(By):
        Infodict=json.loads(self.InfoJson)
        return Infodict["LocatorsType"]        

    #self.Infodict = json.loads(self.InfoJson) #也能用字典做搜尋
