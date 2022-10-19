import configparser
import os
import time

from Lib_space.SELENIUM.BaseClass import Page, WebDriver
from Automation_Suite.LibSpace.SELENIUM.Page_locators.CarrierSmart.Dashboard.Dashboard_PageLocators import \
    Login_PageLocators, Dashboard_PageLocators

dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TestParameters = configparser.ConfigParser()
print(dirnameutils + "\\Utilities\\parameters.ini")
TestParameters.read("D:\\Carrier Smart 2021\\Automation\\Automation_Suite\\Utilities\\parameters.ini")
chrome_driver_path = TestParameters.get("TEST_PARAMETERS", "chromedriver")
target_url = TestParameters.get("TEST_PARAMETERS", "target_url")
loginSleepTime = 5


class Login(Page):

    global delay
    #commonoper = CommonOperations(driver=driver)

    def __init__(self, driver):
        super(Login, self).__init__(WebDriver)
        self.driver = driver
        #commonoper = CommonOperations()

    def login(self):
        try:
            print("Entered sso login method from Login Class")
            email = TestParameters.get("TEST_PARAMETERS", "email")
            user = TestParameters.get("TEST_PARAMETERS", "user")
            passW = TestParameters.get("TEST_PARAMETERS", "passW")
            time.sleep(loginSleepTime)
            self.wait_until_element_visible_byId(self.driver, Login_PageLocators.sso_email[1])
            print(Login_PageLocators.sso_email)
            self.click_element(*Login_PageLocators.sso_email)
            self.send_keys(*Login_PageLocators.sso_email, value=email, clear_first=True, click_first=True)
            #self.wait_until_element_visible_byXpath(driver, Login_PageLocators.sso_next_button_id[1])
            time.sleep(loginSleepTime)
            self.click_element(*Login_PageLocators.sso_next_button_id)
            time.sleep(loginSleepTime)
            self.wait_until_element_visible_byId(self.driver, Login_PageLocators.sso_password[1])
            self.click_element(*Login_PageLocators.sso_password)
            self.send_keys(*Login_PageLocators.sso_password, value=passW,clear_first=True, click_first=True)
            time.sleep(loginSleepTime)
            self.wait_until_element_visible_byXpath(self.driver,Login_PageLocators.verify[1])
            self.click_element(*Login_PageLocators.verify)
            time.sleep(loginSleepTime)
            print("next step to click send code")
            time.sleep(loginSleepTime)
            #self.wait_until_element_visible_byXpath(driver,Login_PageLocators.sendcode[1])
            self.click_element(*Login_PageLocators.sendcode)
            time.sleep(10)
            #self.wait_until_element_visible_byXpath(driver,Login_PageLocators.verify[1])
            self.click_element(*Login_PageLocators.verify)
            time.sleep(loginSleepTime)
            self.click_element(*Login_PageLocators.verify)
        except Exception as e:
            print("exception block from SSO page")
            print(e.__class__, " SSO page is not displayed")
        try:
            print("Entered Carrier login method from Login Class")
            email = TestParameters.get("TEST_PARAMETERS", "email")
            print(email)
            user = TestParameters.get("TEST_PARAMETERS", "user")
            passw = TestParameters.get("TEST_PARAMETERS", "passW")
            print(Login_PageLocators.CarrierAD)
            time.sleep(loginSleepTime)
            self.wait_until_element_visible_byId(self.driver, Login_PageLocators.CarrierAD[1])
            self.click_element(*Login_PageLocators.CarrierAD)
            print("clicked carrier AD")
            time.sleep(loginSleepTime)
            self.wait_until_element_visible_byId(self.driver, Login_PageLocators.EMAIL[1])
            self.send_keys(*Login_PageLocators.EMAIL, value=email, clear_first=True, click_first=True)
            self.wait_until_element_visible_byId(self.driver, Login_PageLocators.NEXT_BUTTON[1])
            self.click_element(*Login_PageLocators.NEXT_BUTTON)
            time.sleep(loginSleepTime)
            # self.wait_until_element_visible_byId(self.driver, Login_PageLocators.PASSWORD[1])
            self.send_keys(*Login_PageLocators.PASSWORD, value=passw, clear_first=True, click_first=True)
            self.wait_until_element_visible_byId(self.driver, Login_PageLocators.NEXT_BUTTON[1])
            time.sleep(loginSleepTime)
            self.click_element(*Login_PageLocators.NEXT_BUTTON)
            self.wait_until_element_visible_byId(self.driver, Login_PageLocators.NEXT_BUTTON[1])
            time.sleep(loginSleepTime)
            self.click_element(*Login_PageLocators.NEXT_BUTTON)
        except Exception as e:
            print("exception block from SIGN IN")
            print(e.__class__, " attempt of LOGIN Failed")
