import logging
import time
import sys,os
from turtle import goto

sys.path.append(os.getcwd())
sys.path.append('..')
sys.path.append('..\\beTestedPage')

from base_locators import *
import beTestedPage.Demo.Demo_actions as TargetWeb1Action
import beTestedPage.Demo.Demo_locators as locators

#region ===============================Enable Function===============================
    
def get_Web1Object(): #寫成單例 取得目前網頁資訊
    global obj;
    getOBJ_Success= TargetWeb1Action.get_page_obj()
    if getOBJ_Success==False:
        obj=TargetWeb1Action.Init_page("chrome")#使用chrome進介面
        obj.get_page()
    else:
        obj=TargetWeb1Action.setup_page()
        obj=TargetWeb1Action.get_page_obj()    
    TargetWeb1Action.set_page_obj(obj)   
    return obj

def CheckAndlogin():
    if obj.Check(obj.bt_login_button):
        TargetWeb1Action.login()
    else:
        return
        
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
#endregion ===============================Logger===============================

#region ===============================page1===============================
def test_turnOnBrowser():
    obj = get_Web1Object()
    assert True

def test_login_and_logout():
    obj = get_Web1Object()
    obj.SetInputBoxText(obj.user_name,"standard_user")
    obj.SetInputBoxText(obj.password, "secret_sauce")
    obj.Click("login-button")
    assert True

#Products page operations
def test_products_page():
    obj = get_Web1Object()
    CheckAndlogin()
    text = obj.GetText(obj.link_item0)
    assert text == "Sauce Labs Bike Light"
    obj.Click(obj.bt_addToCart0)
    assert "Remove" == obj.GetText(obj.bt_addToCart0)
    assert "1" == obj.GetText(obj.lab_cart_badge)
    
    obj.Click(obj.bt_addToCart1)
    assert "Remove" == obj.GetText(obj.bt_addToCart1)
    assert "2" == obj.GetText(obj.lab_cart_badge)
    
    obj.Click(obj.bt_addToCart0)
    assert "Add to cart" == obj.GetText(obj.bt_addToCart0)
    obj.Click(obj.bt_addToCart1)
    assert "Add to cart" == obj.GetText(obj.bt_addToCart1)
    # prev page
    
def test_detail_page():
    obj = get_Web1Object()
    CheckAndlogin()
    obj.Click(obj.link_item0)
    assert "Sauce Labs Bike Light" == obj.GetText(obj.lab_detail_item0)
    assert "$9.99" == obj.GetText(obj.lab_detail_item0_price)
    if obj.Check(obj.bt_detail_item0_add):
        obj.Click(obj.bt_detail_item0_add)
        assert "Remove" == obj.GetText(obj.bt_detail_item0_remove)
        obj.Click(obj.bt_detail_item0_remove)
    else:
        obj.Click(obj.bt_detail_item0_remove)
        assert "Add to cart" == obj.GetText(obj.bt_detail_item0_add)
        obj.Click(obj.bt_detail_item0_add)
    obj.Click(obj.bt_detail_BackToProduct)
    
    
    
#cart and buy
def test_add_item_to_cart():
    obj = get_Web1Object()
    CheckAndlogin()
    obj.Click(obj.bt_addToCart0)
    obj.Click(obj.bt_addToCart1)
    obj.Click(obj.bt_addToCart2)
    obj.Click(obj.bt_addToCart3)
    obj.Click(obj.bt_addToCart4)
    obj.Click(obj.bt_addToCart5)
    obj.Click(obj.bt_Cart)
    obj.Click(obj.bt_cart_checkout)
    # Checkout: Your Information
    obj.SetInputBoxText(obj.tb_checkout_FirstName,"YiFan")
    obj.SetInputBoxText(obj.tb_checkout_LastName,"Hsu")
    obj.SetInputBoxText(obj.tb_checkout_PostalCode,"123")
    obj.Click(obj.bt_checkout_Continue)
    # Checkout: Overview
    assert "Total: $140.34" == obj.GetText(obj.lab_overview_TotalPrice)
    assert "Item total: $129.94" == obj.GetText(obj.lab_overview_TaxItemTotal)
    obj.Click(obj.bt_overview_Finish)
    # Checkout: Complete!
    assert "Thank you for your order!" == obj.GetText(obj.lab_complete_Itemtotal)
    obj.Click(obj.bt_complete_back_products)

