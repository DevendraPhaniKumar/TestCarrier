import os
import sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
sys.path.append(dirnameutils+'\Selenium_Lib')
from Selenium_Lib.BaseClass import Page
from Selenium_Lib.BaseClass import driver as D
from Page_locators.LoginPage_locatars import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import datetime

driver = object
delay = 45


class LoginPage(Page):

    def getdriver(self, webdriver):
        global driver, delay
        driver = webdriver

    def wait(self, element):
        try:
            try:
                WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element[-1])))
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Page loaded")
            except:
                new_session = D()
                new_session.open_newsession()
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Loading took too much time!")

    def enter_email(self, user):
        self.wait(LoginPageLocatars.EMAIL)
        try:
            self.find_element(*LoginPageLocatars.EMAIL).clear()
            self.find_element(*LoginPageLocatars.EMAIL).send_keys(user)
        except:
            self.logout()
            self.find_element(*LoginPageLocatars.EMAIL).clear()
            self.find_element(*LoginPageLocatars.EMAIL).send_keys(user)

    def enter_password(self, user):
        self.find_element(*LoginPageLocatars.PASSWORD).clear()
        self.find_element(*LoginPageLocatars.PASSWORD).send_keys(user)

    def click_login_button(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.SUBMIT))
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Loading took too much time!")
        time.sleep(0.5)
        self.find_element(*LoginPageLocatars.SUBMIT).click()
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",'Successfully logged in')

    def get_error_msg(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.SUBMIT))
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Loading took too much time!")
        time.sleep(3)
        return self.find_element(*LoginPageLocatars.invalid_user_error).text

    def logout(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.user_options))
            try:
                WebDriverWait(driver, delay).until(element_present)
            except:
                new_session = D()
                new_session.open_newsession()
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Loading took too much time!")
        time.sleep(1)
        self.find_element(*LoginPageLocatars.user_options).click()
        self.find_element(*LoginPageLocatars.logout).click()