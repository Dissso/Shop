# import self as self
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import time

from base.base_class import Base

""" Finish test"""
class Finish_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Methods
    def finish(self):
        self.get_current_url()
        self.assert_url('https://www.citilink.ru/order/checkout/') # assert finish url
        self.get_screenshot()









