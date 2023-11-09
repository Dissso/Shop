import self as self
import urllib3
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import time

from base.base_class import Base


class Login_page(Base):

    # url = 'https://www.mvideo.ru/'
    url = 'https://www.citilink.ru/'
    # url = 'https://www.dns-shop.ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def enter_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()








