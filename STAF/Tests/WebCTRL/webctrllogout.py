'''
Created on Jul 25, 2019

@author: vadlan
'''
import unittest
from Lib_space.SELENIUM.BaseClass import WebDriver,Page

#from Lib_space.SELENIUM.Pages.WebCTRL_Pages.WebCTRLPage import WebCTRL
#from Lib_space.SELENIUM.Page_locators.pagelocators import WebCTRLPageLocators,LoginPageLocatars
from Lib_space.SELENIUM.Page_locators.WebCTRL_Locators.pagelocators import *
import configparser
import os,sys,time
import unittest as unittest
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)


class WebCTRLogout(unittest.TestCase):
    
    #=======================================================================
    # Setup for WebDriver instance Creation 
    #=======================================================================
    def setUp(self):
        print("Starting WebCTRL Test")
        self.driverinstance = WebDriver.same_driver
 #       self.webpagedriver = WebCTRL(self.driverinstance)

    def test_A(self):
        
        print("WebCTRLLogout")
        self.webpagedriver.logout()         
        
        
    def tearDown(self): 
        test_method_name = self._testMethodName
        self.webpagedriver.screenShot(foldername+"\\"+test_method_name)
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\"+foldername))
            
