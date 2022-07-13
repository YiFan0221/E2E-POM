from enum import Enum, unique
from typing import Any, Tuple ,TypeVar ,Generic
from selenium.webdriver.common.by import By
import json
import logging

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
  
def GetElementType(self,UIInput):
    #從傳遞進來的輸入取出element並回傳
    elemt = None
    if isinstance(UIInput, str): #字串索引表檢索
        if UIInput in self.UI_dict:
            elemt=self.UI_dict[UIInput].elemt
        else:
            logging.debug('GetElementType: '+UIInput+'is none.')
            return None            
    ##運作異常 取消
    #elif isinstance(UIInput,LocatorsObj.elemt): #element檢索
    #    elemt=UIInput                
    elif isinstance(UIInput,LocatorsObj): #定位器物件本身檢索
        elemt=UIInput.elemt    
    else:                
        elemt=UIInput
    return elemt
class LocatorsObj():

    def elemt(self) -> Tuple:
        return self.elemt

    def InfoJson(self) -> json:
        return self.InfoJson

    def __init__(self,UI_Dict,Name,ComponentType,locators): 

        self.elemt = (By.XPATH,locators) #定義定位器
        obj= { #用Json方便擴充&傳遞屬性
            "Name":str(Name),
            "ComponentType":ComponentType.value,#定義元件種類     
            "Necessary":str(""),
            "Terminate":str("") 
        }
        self.InfoJson = json.dumps(obj)#轉成Json格式儲存
        #UI_Dict.setdefault(Name,self)
        UI_Dict.append(self)
        
        #self.Infodict = json.loads(self.InfoJson) #也能用字典做搜尋

