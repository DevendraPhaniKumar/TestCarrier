from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions, ui
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException,NoAlertPresentException
    
from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os
import time
import configparser
import datetime
from datetime import datetime

from selenium.webdriver.common.by import By
from os.path import sys
from _overlapped import NULL

dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))



# This Base class is serving basic attributes for every single page inherited from Page class
# The below class is used to define the operations perform in the web application.

class Page(object):
    """
     Base class that all page models can inherit from
    
    
    """

    def __init__(self, selenium_driver, base_url=''):
        """ 
        The constructor for Page class. 
  
        Parameters: 
           selenium_driver (String): Driver instance 
           base_url (url): Base url of application    
        """
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
        
    def refreshbrowserPage(self):
        self.driver.refresh()
        

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
    
    def alert_accept(self):
        """
        Accept the alert
        """
        try:
            alert=self.driver.switch_to.alert
            alert.accept()
            
        except NoAlertPresentException as exception:
            print("No alert prasent: "+exception)
            
    
    def alert_dismiss(self):
        """
        Dimiss the alert
        """
        try:
            alert=self.driver.switch_to.alert
            alert.dismiss()
        except NoAlertPresentException as exception:
            print("No alert prasent: "+exception)
            
    def alert_send_keys(self,texttoEnter):
        """
        Enter text to the alert
        parameters:
            texttoEnter(String): Text to enter
        """
        try:
            alert=self.driver.switch_to.alert
            alert.send_keys(texttoEnter)
        except NoAlertPresentException as exception:
            print("No alert prasent: "+exception)
    
    def _get_alert_text(self):
        """
        Get the text of an alert the alert
        return:
            it returns the text
        """
        try:
            alert=self.driver.switch_to.alert
            alertTex=alert.text
            return alertTex
        except NoAlertPresentException as exception:
            print("No alert prasent: "+exception)

    
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
    
    def checkbox(self,*locator, check=True):
        """
        Check box check or uncheck depeding on locator and check parameter  
        """
        attributevalue=self.driver.find_element(*locator).get_attribute('src')
        try:
            if check:
                if("togglebox_wr_x" in attributevalue):
                    
                    print("Already checked")
                else:
                    self.click_element(*locator)
            
            else:
                if("togglebox_wr_x" in attributevalue):
                    
                   self.click_element(*locator)
                else:
                    print("Check box already uncheked")
            
        except NoSuchElementException as exception:
                    print("Element not found and test failed")
     
    def drag_and_drop(self,locator,x,y):
        """
        Drag and drop specified offset
        
        Paramenters:
           locator(locator): locator of specific element to find
           x(int), y(int): offset values
        """
        el = self.driver.find_element_by_xpath(locator)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(el,x,y).perform()
    
    def dragandrop(self,sourceloc,destinationloc):
        """
        Drag and drop using element depending on locator provided

        """
        try:
            source_element = self.driver.find_element_by_name(sourceloc)
            dest_element = self.driver.find_element_by_name(destinationloc)
            ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()
        except Exception as error:
            print(str(error))

    def Right_click_element(self, *locator):
        """
        Right Clicking on element depending on locator provided

        """
        actionChains = ActionChains(self.driver)

        actionChains.context_click(*locator).perform()
        #self.driver.find_element(*locator).click()

    def Scroldownwithclick(self,*Locator):
        """
                Scroll down using element depending on locator provided

                """
        count = 0
        while count < 100:
            self.driver.find_element_by_xpath(*Locator).click()
            count += 1

                
    def get_attribute_value(self, *locator, attribute):
        """
        Get attribute value by passing locator and attribute you want to fetch
        """
        return self.driver.find_element(*locator).get_attribute(attribute)
    
    def get_attribute_on_webelement(self,webElement, attribute):
        """
        Get attribute value by passing WebElement and attribute you want to fetch
        """
        return webElement.get_attribute(attribute)
        
           
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
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print ('%s page does not have "%s" locator' % (self, loc))
            
            
    def currenttime(self):
        time = str(datetime.now().time())
        ctime = time.split(":")
        currenttime = ctime[0]
        currenttimet = int(currenttime)
        return currenttimet
    
    
    
    
    
    def switch_to_child_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        
    
    def switch_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
    
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



class WebDriver:
    """
    WebDriver is the object responsible for Initiate new webdriver session 
    and use same session if already exists for further tests execution.
    Support added for firefox ,chrome and IE browsers.
    """

    TestParameters = configparser.ConfigParser()
    TestParameters.read(dirnameutils + '\\Utility\\parameters.ini')    
    executor_url = TestParameters.get("TEST_PARAMETERS", "executor_url")
    session_id = TestParameters.get("TEST_PARAMETERS", "session_id")
    browserName=TestParameters.get("TEST_PARAMETERS", "browser")
    capabilities = {'chromeOptions': {'useAutomationExtension': False}}
    base_url = TestParameters.get("TEST_PARAMETERS", "Base_URL")
    print(base_url)
    
    #Below code is useful to overcome "loading of unpacked extensions is disabled by the administrator Pop-up Message"
    #Use Chrome options instead desired_capabilities
    options = webdriver.ChromeOptions()
    options.add_experimental_option('useAutomationExtension', False)
      
    try:
   
        #same_driver = webdriver.Remote(command_executor=executor_url,desired_capabilities=capabilities)
        same_driver = webdriver.Remote(command_executor=executor_url,options=options)   
        same_driver.implicitly_wait(30)     
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

            """
            #chromeOptions = webdriver.ChromeOptions()
            #chrome_options = Options()
            #chromeOptions.add_argument("--disable-extensions")
            #same_driver = webdriver.Chrome(dirnameutils + '\\Utility\\WEB_Drivers\\chromedriver.exe',desired_capabilities=capabilities,chrome_options=chrome_options)
            
            #chromeOptions.add_experimental_option('useAutomationExtension', False)
            #same_driver = webdriver.Chrome(dirnameutils + '\\Utility\\WEB_Drivers\\chromedriver.exe',chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities()) 
            #options = webdriver.ChromeOptions()
            #options.add_argument('--disable-extensions')
            # Update your desired_capabilities dict withe extra options.
            #same_driver = webdriver.Remote(dirnameutils + '\\Utility\\WEB_Drivers\\chromedriver.exe',desired_capabilities=options.to_capabilities()) 
            """
            #driverpath = r'C:\\DAYA_WORK\\Automation\\Eclipse_python\\STAF\\Utility\\WEB_Drivers\\chromedriver.exe'
            #same_driver = webdriver.Chrome(executable_path = driverpath, options=options)
            print("The dirnameutils is:"+dirnameutils)
            #Below code is useful to overcome "loading of unpacked extensions is disabled by the administrator Pop-up Message"
            same_driver = webdriver.Chrome(dirnameutils + '\\Utility\\WEB_Drivers\\chromedriver.exe',options=options)
            
            #same_driver = webdriver.Chrome(dirnameutils + '\\Utility\\WEB_Drivers\\chromedriver.exe',desired_capabilities=capabilities)
            same_driver.get(base_url)
    
    elif browserName=="Firefox":
            try:
                same_driver.get(base_url)
            except:        
                print("Firefox Driver") 
                firefox_capabalities = DesiredCapabilities.FIREFOX
                firefox_capabalities["marionette"] = False
                firefox_capabalities['acceptSslCerts'] = True
                same_driver =webdriver.Firefox(capabilities=firefox_capabalities,executable_path=dirnameutils + '\\Utility\\WEB_Drivers\\geckodriver.exe')
                same_driver.get(base_url)

    elif browserName=="IE":
            try:
                same_driver.get(base_url)
            except:        
                print("IE Driver")
                Ie_Capabilities = DesiredCapabilities.INTERNETEXPLORER
                Ie_Capabilities['ignoreProtectedModeSettings'] = True
                same_driver = webdriver.Ie(capabilities=Ie_Capabilities,executable_path=dirnameutils + '\\Utility\\WEB_Drivers\\IEDriverServer.exe')
                same_driver.get(base_url)
                
    executor_url = same_driver.command_executor._url 
    session_id = same_driver.session_id
    print(executor_url)
    print(session_id)
    same_driver.maximize_window()
    TestParameters['TEST_PARAMETERS']['session_id'] = same_driver.session_id
    TestParameters['TEST_PARAMETERS']['executor_url'] = same_driver.command_executor._url
    with open(dirnameutils + '\\Utility\\parameters.ini', 'w') as configfile:  # save
        TestParameters.write(configfile)              
