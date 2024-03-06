#Project
import sys,os
sys.path.append(os.getcwd())
# import base_locators
from base_locators import GetElementType,LocatorsObj , EnumUIType , logging ,json , Tuple ,TypeVar ,Generic
from selenium.webdriver.common.by import By
#By 可以選擇要使用的篩選器 有NAME、ID、XPATH
#必須依照介面位置排放，以免找不到元件


#命名規則
# 元件種類(型別)_功能_細節
class cDemoLocators:

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
            
        
        self.user_name              = LocatorsObj(self.UI_List,"user-name",EnumUIType.Input,By.ID)
        self.password               = LocatorsObj(self.UI_List,"password",EnumUIType.Input,By.ID)
        self.login_button               = LocatorsObj(self.UI_List,"login-button",EnumUIType.Button,By.ID)
        
        
        self.ccb_productsort        = LocatorsObj(self.UI_List,"ccb_productsort",EnumUIType.ComboBox,By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select")
        self.bt_detail_BackToProduct= LocatorsObj(self.UI_List,"back-to-products",EnumUIType.Button,By.ID)
                        
        self.link_item0             = LocatorsObj(self.UI_List,"item_0_title_link",EnumUIType.Link,By.ID)
        self.image_item0            = LocatorsObj(self.UI_List,"item_0_img_link",EnumUIType.Link,By.ID)
        self.lab_price0             = LocatorsObj(self.UI_List,"lab_price0",EnumUIType.Label,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/text()[2]")
        self.bt_addToCart0          = LocatorsObj(self.UI_List,"bt_addToCart0",EnumUIType.Button,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button")
        
        self.lab_detail_item0       = LocatorsObj(self.UI_List,"lab_detail_item0",EnumUIType.Label,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div[2]/div[1]")
        self.lab_detail_item0_price = LocatorsObj(self.UI_List,"lab_detail_item0_price",EnumUIType.Label,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div[2]/div[3]")
        self.bt_detail_item0_add    = LocatorsObj(self.UI_List,"add-to-cart-sauce-labs-bike-light",EnumUIType.Button,By.ID)
        self.bt_detail_item0_remove = LocatorsObj(self.UI_List,"remove-sauce-labs-bike-light",EnumUIType.Button,By.ID)              
                
        self.link_item1             = LocatorsObj(self.UI_List,"item_1_title_link",EnumUIType.Link,By.ID)
        self.image_item1            = LocatorsObj(self.UI_List,"item_1_img_link",EnumUIType.Link,By.ID)
        self.lab_price1             = LocatorsObj(self.UI_List,"lab_price1",EnumUIType.Label,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/text()[2]")
        self.bt_addToCart1           = LocatorsObj(self.UI_List,"bt_addToCart1",EnumUIType.Button,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button")
        
        self.link_item2             = LocatorsObj(self.UI_List,"item_2_title_link",EnumUIType.Link,By.ID)
        self.image_item2            = LocatorsObj(self.UI_List,"item_2_img_link",EnumUIType.Link,By.ID)
        self.lab_price2            = LocatorsObj(self.UI_List,"lab_price2",EnumUIType.Label,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div/text()[2]")
        self.bt_addToCart2           = LocatorsObj(self.UI_List,"bt_addToCart2",EnumUIType.Button,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/button")
        
        self.link_item3             = LocatorsObj(self.UI_List,"item_3_title_link",EnumUIType.Link,By.ID)
        self.image_item3            = LocatorsObj(self.UI_List,"item_3_img_link",EnumUIType.Link,By.ID)
        self.lab_price3            = LocatorsObj(self.UI_List,"lab_price3",EnumUIType.Label,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/div/text()[2]")
        self.bt_addToCart3           = LocatorsObj(self.UI_List,"bt_addToCart3",EnumUIType.Button,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/button")
        
        self.link_item4             = LocatorsObj(self.UI_List,"item_4_title_link",EnumUIType.Link,By.ID)
        self.image_item4            = LocatorsObj(self.UI_List,"item_4_img_link",EnumUIType.Link,By.ID)
        self.lab_price4            = LocatorsObj(self.UI_List,"lab_price4",EnumUIType.Label,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/text()[2]")
        self.bt_addToCart4           = LocatorsObj(self.UI_List,"bt_addToCart4",EnumUIType.Button,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        
        self.link_item5             = LocatorsObj(self.UI_List,"item_5_title_link",EnumUIType.Link,By.ID)
        self.image_item5            = LocatorsObj(self.UI_List,"item_5_img_link",EnumUIType.Link,By.ID)
        self.lab_price5            = LocatorsObj(self.UI_List,"lab_price5",EnumUIType.Label,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/div/text()[2]")
        self.bt_addToCart5           = LocatorsObj(self.UI_List,"bt_addToCart5",EnumUIType.Button,By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button")
    
    
        # cart
        self.bt_Cart                = LocatorsObj(self.UI_List,"shopping_cart_container",EnumUIType.Button,By.ID)
        self.cart_badge             = LocatorsObj(self.UI_List,"shopping_cart_container",EnumUIType.Label,By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a/span")
        self.bt_continue_shopping   = LocatorsObj(self.UI_List,"continue-shopping",EnumUIType.Button,By.ID)
        

        #List轉Dict
        for i in range(len(self.UI_List)):
            jsonName=json.loads(self.UI_List[i].InfoJson)#讀取整個Json結構
            self.UI_dict.setdefault(jsonName['Name'],self.UI_List[i])#轉換到UI_dict途中
