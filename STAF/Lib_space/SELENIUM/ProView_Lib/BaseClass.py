from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import warnings
import os
import configparser
import datetime
import time
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this Base class is serving basic attributes for every single page inherited from Page class


class Page(object):
    def __init__(self, driver, base_url='http://localhost:8081'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
    def screen_capture(self,name):
        filename = name + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot('./../Results/Screenshots/' + str(filename) + '.png')

class WebDriver:
    # capabilities = {}
    TestParameters = configparser.ConfigParser()
    TestParameters.read(dirnameutils + "\\Utilities\parameters.ini")
    chromedriver = TestParameters.get("TEST_PARAMETERS", "chromedriver")
    executor_url = TestParameters.get("TEST_PARAMETERS", "executor_url")


    options = webdriver.ChromeOptions()
    prefs = {"profile.defaullt_content_setting_values.notifications": 2}
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("prefs", prefs)

    # options.add_argument('--profile-directory=Default')
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars" )
    capabilities = {'chromeOptions': {'useAutomationExtension': False}}

    capabilities = options.to_capabilities()


    def launch_application(self):
        try:
            session_id = WebDriver.TestParameters.get("TEST_PARAMETERS", "session_id")
            executor_url = WebDriver.TestParameters.get("TEST_PARAMETERS", "executor_url")
            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
            web_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=WebDriver.capabilities,options=self.options)
            web_driver.switch_to.window(web_driver.current_window_handle)
            web_driver.close()
            web_driver.session_id = session_id
            # web_driver.quit()
            return web_driver
        except:
            # web_driver = webdriver.Chrome(WebDriver.chromedriver, desired_capabilities=WebDriver.capabilities)
            web_driver = webdriver.Chrome(WebDriver.chromedriver, options=self.options)
            session_id = web_driver.session_id
            executor_url = web_driver.command_executor._url
            WebDriver.TestParameters['TEST_PARAMETERS']['session_id'] = session_id
            WebDriver.TestParameters['TEST_PARAMETERS']['executor_url'] = executor_url
            with open(dirnameutils + "\\Utilities\parameters.ini", 'w') as configfile:  # save
                WebDriver.TestParameters.write(configfile)
                web_driver.get('http://localhost:8081')
                time.sleep(5)
            web_driver.switch_to.window(web_driver.current_window_handle)
            return web_driver

    def open_newsession(self):
        web_driver = webdriver.Chrome(WebDriver.chromedriver, options=self.options)
        session_id = web_driver.session_id
        executor_url = web_driver.command_executor._url
        WebDriver.TestParameters['TEST_PARAMETERS']['session_id'] = session_id
        WebDriver.TestParameters['TEST_PARAMETERS']['executor_url'] = executor_url
        with open(dirnameutils + "\\Utilities\parameters.ini", 'w') as configfile:  # save
            WebDriver.TestParameters.write(configfile)
            web_driver.get('http://localhost:8081')
        return web_driver
    def close_session(self):
        session_id = WebDriver.TestParameters.get("TEST_PARAMETERS", "session_id")
        executor_url = WebDriver.TestParameters.get("TEST_PARAMETERS", "executor_url")
        web_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=WebDriver.capabilities,options=self.options)
        web_driver.close()
        web_driver.session_id = session_id
        WebDriver.TestParameters['TEST_PARAMETERS']['session_id'] = session_id
        WebDriver.TestParameters['TEST_PARAMETERS']['executor_url'] = ""
        with open(dirnameutils + "\\Utilities\parameters.ini", 'w') as configfile:  # save
            WebDriver.TestParameters.write(configfile)
        web_driver.quit()



