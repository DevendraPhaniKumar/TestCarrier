import os
import sys

dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)

# sys.path.append(dirnameutils+'\\Selenium_Lib')
from Lib_Space.Selenium_Lib.BaseClass import Page
from Lib_Space.Selenium_Lib.BaseClass import Page
from Lib_Space.Selenium_Lib.Page_locators.LoginPage_locatars import LoginPageLocatars
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import datetime
import time

driver = object
delay = 120


class LoginPage(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(LoginPage, self).__init__(webdriver)
        driver = webdriver

    def wait(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element[-1])))
            return 0
        except Exception as e:
            print("Exception occurred: ", e.message)
            print(datetime.datetime.now().strftime("%Y:%m:%d-%H:%M:%S"), "Loading took too much time!")
            filename1 = "LoginErr"
            self.screen_capture(filename1)
            return 1

    def wait_until_visible(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, element[-1])))
            return 0
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Loading took too much time!")
            return 1

    def enter_email(self, user):
        #self.wait(LoginPageLocatars.EMAIL)
        try:
            self.find_element(*LoginPageLocatars.EMAIL).clear()
            self.find_element(*LoginPageLocatars.EMAIL).send_keys(user)
        except Exception as e:
            print("Exception occurred: ", e)
            print("Reattempting login")
            self.logout()
            self.find_element(*LoginPageLocatars.EMAIL).clear()
            self.find_element(*LoginPageLocatars.EMAIL).send_keys(user)
        print("Logging in with user: ", user)

    def enter_password(self, user):
        self.find_element(*LoginPageLocatars.PASSWORD).clear()
        self.find_element(*LoginPageLocatars.PASSWORD).send_keys(user)

    def login(self,offline =0):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.SUBMIT))
            #WebDriverWait(driver, delay).until(element_present)
        except Exception as e:
            print("Exception occurred: ", e)
            print("Loading took too much time!")

        time.sleep(0.5)
        if offline:
            self.find_element(*LoginPageLocatars.offline_btn).click()
        self.find_element(*LoginPageLocatars.SUBMIT).click()
        WebDriverWait(driver, delay).until(element_present)
        time.sleep(3)

        if self.wait_until_visible(LoginPageLocatars.user_title)==0:
            print('*' * 12, 'Login is successful', '*' * 12)
        else:
            print("Login Failed")
    def tool_update_info(self,download=0):
        try:
            if self.wait(LoginPageLocatars.toolupdate_btn) == 0:
                self.find_element(*LoginPageLocatars.toolupdate_btn).click()
                if self.find_element(*LoginPageLocatars.tool_update_title).is_displayed():
                    print(self.find_element(*LoginPageLocatars.tool_update_title).text, "- ", \
                        self.find_element(*LoginPageLocatars.tool_updated_ver).text)
                    self.find_element(*LoginPageLocatars.tool_update_close).click()
            else:
                print("No update button available")
        except:
            print("Tool update dialog not available")

    def get_status(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.SUBMIT))
            WebDriverWait(driver, delay).until(element_present)
        except Exception as e:
            print("Exception occurred: ", e)
            print("Loading took too much time!")
        time.sleep(3)
        return self.find_element(*LoginPageLocatars.invalid_user_error).text
    def get_error_msg(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.SUBMIT))
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Loading took too much time!")
        time.sleep(3)
        return self.find_element(*LoginPageLocatars.invalid_user_error).text

    def get_email_status(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.SUBMIT))
            WebDriverWait(driver, delay).until(element_present)
        except Exception as e:
            print("Exception occurred: ", e)
            print("Loading took too much time!")
        time.sleep(3)
        return self.find_element(*LoginPageLocatars.Email_msg).text

    def logout(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.user_options))
            try:
                WebDriverWait(driver, delay).until(element_present)
            except Exception as e:
                print("Exception occurred: ", e)
                print("Loading took too much time!")
        except Exception as e:
            print("Exception occurred: ", e)
            print("Loading took too much time!")
        time.sleep(1)
        self.find_element(*LoginPageLocatars.user_options).click()
        self.find_element(*LoginPageLocatars.logout).click()
        time.sleep(2)
        obj1 = self.driver.switch_to.alert
        print("Logout blocker: ", obj1.text)
        obj1.accept()
        time.sleep(2)
        obj2 = self.driver.switch_to.alert
        print("Logout blocker: ", obj2.text)
        obj2.accept()
        time.sleep(5)