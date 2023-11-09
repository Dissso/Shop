import pytest
from selenium import webdriver
import self as self
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

def test_buy_product(set_up, set_group):
    g = Service('/Users/alexlub/Resoucre/chromedriver')
    driver = webdriver.Chrome(service=g)


    print("Start Test ")

    login = Login_page(driver)
    login.enter_site()

    mp = Main_page(driver)
    mp.select_menus()
    mp.select_products()
    mp.select_iphone()
    mp.select_cart()

    p = Payment_page(driver)
    p.click_finish_button()
    p.assert_price()
    #
    f = Finish_page(driver)
    f.finish()
    print("Finish Test ")
    time.sleep(5)
    driver.quit()

