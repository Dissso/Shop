# import self as self
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import time

from base.base_class import Base


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_menu = '//a[@class=" css-15x7smt enj50b10"]'
    select_product = '(//span[@class="e1n70abf0 css-1xdhyk6 exlytbk0"])[2]'
    iphone = '(//span[@class="app-catalog-19y4hmw e1fnp08x0"])[1]'
    price = '//button[@class="e4uhfkv0 css-gh3izc e4mggex0"]'


    # Getters

    def get_select_menu(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_menu)))
    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product)))

    def get_select_iphone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.iphone)))

    #
    def get_select_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price)))
    #
    #
    #
    #
    # # Actions
    #
    def click_select_menu(self):
        self.get_select_menu().click()
        print("Click select menu")

    def click_select_product(self):
        self.get_select_product().click()
        print("Click select product")

    def click_iphone(self):
        self.get_select_iphone().click()
        print("Click iphone")
    #
    def click_cart(self):
        self.get_select_cart().click()
        print("Click cart")
    #
    #
    #
    #
    # # Methods
    def select_menus(self):
        self.click_select_menu()
        # self.click_cart()

    def select_products(self):
        self.click_select_product()
        # self.click_cart()

    def select_iphone(self):
        self.click_iphone()
        # self.click_cart()

    def select_cart(self):
        self.get_current_url()
        self.click_cart()







