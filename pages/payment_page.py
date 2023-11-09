# import self as self
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import time

from base.base_class import Base


class Payment_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    finish_button = "//button[@class='e4uhfkv0 css-ch34l1 e4mggex0']"
    price = '//span[@class="e1j9birj0 e106ikdt0 css-1f8xctp e1gjr6xo0"]'
    button_order = '//button[@class="e1jq023s0 css-tc9rhz e4mggex0"]'
    # Getters
    def get_finish_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    def get_finish_price(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_button_order(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.button_order)))


    # Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish_button")

    def assert_price(self):
        price = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.price)))
        value_price = price.text
        print(value_price)
        assert value_price == "150 890"
        print("Success Price")

    # Methods
    def payment(self):
        self.get_current_url()
        self.get_screenshot()
        self.click_finish_button()






