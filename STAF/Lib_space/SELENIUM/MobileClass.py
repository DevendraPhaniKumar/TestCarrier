'''
Created on Aug 12, 2019

@author: vadlan
'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from Lib_space.SELENIUM.Page_locators.EQTPageLocators.EQTpagelocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions, ui
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium import webdriver


import os
import time
import configparser

from selenium.webdriver.common.by import By
from os.path import sys
from _overlapped import NULL

dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

print(dirnameutils)

class MobileDriver(object):

    global webctrl, appiumServerURL
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'EmulatroTest'
    driver = None



    TestParameters = configparser.ConfigParser()
    TestParameters.read(dirnameutils + '\\Utility\\parameters.ini')
    appiumServerURL = TestParameters.get("TEST_PARAMETERS", "AppiumServerURL")
    DataParameter = configparser.ConfigParser()
    DataParameter.read(dirnameutils + '\\Selenium\\DataFolder\\TestData.ini')
    dc['reportDirectory'] = reportDirectory
    dc['reportFormat'] = reportFormat
    dc['udid'] = TestParameters.get("TEST_PARAMETERS", "androidDevice")
    dc['platformName'] = TestParameters.get("TEST_PARAMETERS", "typeofOS")
    selenium_driver= webdriver.Remote(appiumServerURL, dc)


class MobilePage(object):
    """
        Android page related functions class

    """

    def __init__(self, selenium_driver):

        self.driver = selenium_driver
        self.timeout = 30

    def find_element(self, *locator):
        """
            Finding a WebElement in the given page
            :param locator: WebElement Locator Eg: Xpath, id, CSS Locator etc..
            :return:returns Given WebElemtns

        """

        try:
            return self.driver.find_element(*locator)

        except NoSuchElementException as exception:            
            print(exception)
            

    def find_elements(self, *locator):
        """
            Finds elements of given locator
        :param locator: WebElement Locator Eg: Xpath, id, CSS Locator etc..
        :return: list of WebElements
        """
        return self.driver.find_elements(*locator)

    def click_On_element(self,*locator):
        """
            Clicks on the given WebElement
        :param locator: WebElement Locator Eg: Xpath, id, CSS Locator etc..
        """
        try:
            self.driver.find_element(*locator).click()
        except NoSuchElementException as exception:
            print("Element not found and test failed")

    def text_verification(self,*locator, expectedText):
        """
        Text comparision of the given Webelement locator
        :param locator: WebElement Locator Eg: Xpath, id, CSS Locator etc..
        :param expectedText: Expected text string
        :return: Returns True if string is matched False if not
        """
        actualText = self.driver.find_element(*locator).text
        
        #self.assertEqual(self.driver.find_element(*locator).text, expectedText)
        if(actualText==expectedText):
            print("Passed")
            return True
        else:
            print("Failed")
            return False

    def screenShot(self,testmethodName):
        """
        Get the ScreenShot as file while script executing.

        Args:
            testmethodName: Testmethod name in unittest class.

        Returns:
            Screenshot .png file generate in the Results--><TestFolder>Screenshots 
        """
        timestamp= format(time.strftime("%Y-%m-%d-%H-%M-%S"))
        opdir = testmethodName.split("\\")
        print(opdir)
        if not os.path.exists(dirnameutils+"\\Results\\"+opdir[0]):
            os.mkdir(dirnameutils+"\\Results\\"+opdir[0])
        if not os.path.exists(dirnameutils+"\\Results\\"+opdir[0]+"\\Screenshots"):     
            os.mkdir(dirnameutils+"\\Results\\"+opdir[0]+"\\Screenshots")
        print(opdir[1])                
        self.driver.get_screenshot_as_file(dirnameutils+"\\Results\\"+opdir[0]+"\\Screenshots\\"+opdir[1]+"_"+timestamp+'.png')
    
    
    
    def _drop_down_Selection(self,type,linkText):
        """
        Dropdown elements selection
        :param type: Type of dropdwon[its name] Eg: burgerIcon, authCountry, subnavlinks
        :param linkText: Element you need to click on
        """
        if(type=="burgerIcon"):
            self._burger_icon_Dropdown(linkText)

        elif(type=="authCountry"):
            self._mobileCodeDropdown(linkText)

        elif(type=="subnavlinks"):
            self._sub_Nav_linksClick(linkText)


    





    def EnterTextTo_TextField(self, *loc,value):

        try:
            self.driver.find_element(*loc).send_keys(value)
            #textField.clear()
            #textField.send_keys(value)
            #return  textField

        except AttributeError:
            print("Attribute Error")


    def checkBox(self,*locator,check=True):
        """
        Check box check and uncheck
        :param locator: WebElement Locator Eg: Xpath, id, CSS Locator etc..
        :param check: Boolean type, True-- check, False -- uncheck
        """
        #print(self.driver.find_element(*locator).get_attribute("checked"))


        if check:
            if (self.driver.find_element(*locator).get_attribute("checked")=="true"):
                print("Checkbox is checked")
            else:
                self.click_On_element(*locator)
        else:

            if (self.driver.find_element(*locator).get_attribute("checked")=="true"):
                self.click_On_element(*locator)
            else:
                print("Checkbox is unchecked")
    
    
    def waitFor_Element(self,locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator)))
        except AttributeError:
            print("Attribute Error")
