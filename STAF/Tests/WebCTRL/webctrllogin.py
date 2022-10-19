'''
Created on Jul 25, 2019

@author: vadlan
'''
import configparser
import os,sys
import unittest as unittest
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from Lib_space.SELENIUM.Pages.WebCTRLPage import WebCTRL
from Lib_space.SELENIUM.BaseClass import WebDriver,Page
from Lib_space.SELENIUM.Page_locators.pagelocators import WebCTRLPageLocators, LoginPageLocatars

DataParameter = configparser.ConfigParser()
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)


class WebCTRLOGIN(unittest.TestCase):
    
    #=======================================================================
    # Setup for WebDriver instance Creation 
    #=======================================================================
    def setUp(self):
        print("Starting WebCTRL Test")       
        self.driverinstance = WebDriver.same_driver
        self.webpagedriver = WebCTRL(self.driverinstance)
        
    def test_z(self):        
        print("WebCTRLLogin")        
        self.webpagedriver.loginWebCTRL('admin', "password")
        
        
  
    def test_x(self):      
        print("EquipmentTest2 x method")

    def test_y(self):
        print("EquipmentTest2 y method")
    
    def tearDown(self): 
        test_method_name = self._testMethodName
        self.webpagedriver.screenShot(foldername+"\\"+test_method_name)
                        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\"+foldername))
    