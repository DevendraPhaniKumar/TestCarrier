from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
#from Lib_space.SELENIUM.Page_locators.WebCTRLPageLocators.Webctrl_pagelocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions, ui
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os
import time
import configparser

from selenium.webdriver.common.by import By
from os.path import sys
from _overlapped import NULL

dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# this Base class is serving basic attributes for every single page inherited from Page class
# The below class is used to define the operations perform in the web gui.

class Page(object):
    """
    Base class that all page models can inherit from
    """

    def __init__(self, selenium_driver, base_url=''):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def _open(self, url):
        """
        To access the URL
        """
        url = self.base_url + url

    def find_element(self, *locator):
        """
        Finding an webelemnt depending on locator provided  
        """
        return self.driver.find_element(*locator)
    
    def click_element(self, *locator):
        """
        Clicking on element depending on locator provided  
        """
        self.driver.find_element(*locator).click()

    def find_elements(self, *locator):
        """
        Finding List of elements depending on locator provided  
        """
        return self.driver.find_elements(*locator)

    def get_text(self, *locator):
        """
        Getting text depending on locator  
        """
        return self.driver.find_element(*locator).text

    def switch_to_frame(self, *locator):
        """
        Switch to frame depending on locator  
        """
        return self.driver.switch_to_frame(*locator)
   
    def switch_to_default_content(self):
        """
        Switch to default content  
        """
        return self.driver.switch_to_default_content()

    
    def get_title(self):
        """
        Get the title of page  
        """
        return self.driver.title

    def get_url(self):
        """
        Get the current page URL  
        """
        return self.driver.current_url
    
    def checkbox_check(self,*locator, check=True):
        """
        Check box clicking on depeding on locator and check parameter  
        """
        attributevalue=self.driver.find_element(*locator).get_attribute('src')
        if("togglebox_wr_x" in attributevalue):
            if check:
                print("Already checked")
            else:
                pass
            
    def Verify_body_text_gui(self,*locator,text='',succ_str='',raise_str=''):
        """
        Verifying body text on UI  depending on Locator
        """
        #time.sleep(1)
        body_text = self.find_element(*locator, eval(*locator)[-1]).text
        print (body_text)
        if body_text == text :
              print (succ_str)
        else:
              raise Exception(raise_str)                
            
    def hover(self, *locator):
        """
        Mouse hover on element depending on locator  
        """
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def send_keys(self, *loc, value, clear_first=True, click_first=True):
        """
        Enter the text into textField  
        """
        try:
            #loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print ('%s page does not have "%s" locator' % (self, loc))
    
    
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



class WebDriver_test:
    """
    WebDriver is the object responsible for Initiate new webdriver session 
    and use same session if already exists for further tests execution.
    Support added for firefox ,chrome and IE browsers.
    """

    TestParameters = configparser.ConfigParser()
    TestParameters.read(dirnameutils + '\\Utilities\\parameters.ini')
    executor_url = TestParameters.get("TEST_PARAMETERS", "executor_url")
    session_id = TestParameters.get("TEST_PARAMETERS", "session_id")
    browserName=TestParameters.get("TEST_PARAMETERS", "browser")
    capabilities = {'chromeOptions': {'useAutomationExtension': False}}
    base_url = TestParameters.get("TEST_PARAMETERS", "Base_URL")

    try:     
        same_driver = webdriver.Remote(command_executor=executor_url,desired_capabilities=capabilities)
        if browserName=="Chrome":
            same_driver.close()
        print(same_driver.session_id)
        print(same_driver.command_executor._url)
        same_driver.session_id = session_id
        time.sleep(4)
        print(session_id)           
                    
    except:
        pass

    if browserName=="Chrome":                       
        try:
            same_driver.get(base_url)
        except:
            same_driver = webdriver.Chrome(dirnameutils + '\\Utilities\\WEB_Drivers\\chromedriver.exe',desired_capabilities=capabilities)
            same_driver.get(base_url)
    
    elif browserName=="Firefox":
            try:
                same_driver.get(base_url)
            except:        
                print("Firefox Driver") 
                firefox_capabalities = DesiredCapabilities.FIREFOX
                firefox_capabalities["marionette"] = False
                firefox_capabalities['acceptSslCerts'] = True
                same_driver =webdriver.Firefox(capabilities=firefox_capabalities,executable_path=dirnameutils + '\\Utilities\\WEB_Drivers\\geckodriver.exe')
                same_driver.get(base_url)

    elif browserName=="IE":
            try:
                same_driver.get(base_url)
            except:        
                print("IE Driver")
                Ie_Capabilities = DesiredCapabilities.INTERNETEXPLORER
                Ie_Capabilities['ignoreProtectedModeSettings'] = True
                same_driver = webdriver.Ie(capabilities=Ie_Capabilities,executable_path=dirnameutils + '\\Utilities\\WEB_Drivers\\IEDriverServer.exe')
                same_driver.get(base_url)
                
    executor_url = same_driver.command_executor._url 
    session_id = same_driver.session_id
    print(executor_url)
    print(session_id)
    same_driver.maximize_window()
    TestParameters['TEST_PARAMETERS']['session_id'] = same_driver.session_id
    TestParameters['TEST_PARAMETERS']['executor_url'] = same_driver.command_executor._url
    with open(dirnameutils + '\\Utilities\\parameters.ini', 'w') as configfile:  # save
        TestParameters.write(configfile)              
