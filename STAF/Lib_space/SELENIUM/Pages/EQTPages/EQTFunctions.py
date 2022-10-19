import os
import sys
import _elementtree
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Lib_space.SELENIUM.MobileClass import *
from Lib_space.SELENIUM.Pages.EQTPages.EQTFunctions import *
from Lib_space.SELENIUM.Page_locators.EQTPageLocators.EQTpagelocators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import datetime

driver = object
delay = 45

#This is useful to define the login page parameters
class EQTFunctionsPage(MobilePage):

    # Actions
    def getdriver(self, selenium_driver):
        global driver, delay
        driver = selenium_driver
    
    
    
    def ip_page_Entries(self,ipNtwrk,IP,subnetMask,gateway,port):
        ipPage=self.driver.find_element(By.XPATH,"//*[@class='android.view.View' and ./*[@contentDescription='IP']]")
        lenghtOftextfields=ipPage.find_elements(By.CLASS_NAME,'android.widget.EditText')
        time.sleep(2)
        
        
        lenghtOftextfields[0].click()
        time.sleep(2)
        self.enteringValuesToIP(ipNtwrk)
        
             # same as result = result + 1
                
        
        
        

#         self.driver.find_element_by_xpath("//*[@contentDescription='IP Network:' and @class='android.widget.EditText']").send_keys(ipNtwrk)
#         time.sleep(3)
#         self.driver.find_element_by_xpath("//*[@contentDescription='IP']").click()
#         self.driver.find_element_by_xpath("//*[@contentDescription='IP']").click()
        '''
        #self.driver.press_keycode(4)
        #time.sleep(5)
        self.driver.find_element_by_xpath("//*[@contentDescription='IP']").click()
        #self.driver.find_element_by_xpath("//*[@contentDescription='IP']").click()        
        time.sleep(5)
        #self.driver.find_element_by_xpath("//*[@contentDescription='IP Network:' and @class='android.widget.EditText']").click()
        self.driver.find_element_by_xpath("//*[@contentDescription='IP Network:' and @class='android.widget.EditText']").send_keys(ipNtwrk)
        '''
        
        #self.driver.getKeyboard().sendKeys(ipNtwrk);
        #lenghtOftextfields[0].send_keys(ipNtwrk)
        time.sleep(2)
        lenghtOftextfields[1].send_keys(IP)
        time.sleep(2)
        lenghtOftextfields[2].send_keys(subnetMask)
        time.sleep(2)
        lenghtOftextfields[3].send_keys(gateway)
        time.sleep(2)
        lenghtOftextfields[4].click()
        time.sleep(2)
        self.enteringValuesToPort(port)
        
        
        
    def enteringValuesToIP(self,textToEnter):
        for i in range(5) :
            print(i)
            self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Delete']").click()
        
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@contentDescription='IP']").click()
        self.driver.find_element_by_xpath("//*[@contentDescription='IP']").click()
        
        
        self.driver.find_element_by_xpath("//*[@contentDescription='IP Network:' and @class='android.widget.EditText']").click()
        time.sleep(3)
        i=0

        while i < len(textToEnter):
            print(textToEnter[i])
            
            self.driver.find_element_by_xpath('//*[@contentDescription='+textToEnter[i]+']').click();
            i += 1
        
        self.driver.find_element_by_xpath("//*[@contentDescription='IP']").click()
        self.driver.find_element_by_xpath("//*[@contentDescription='IP']").click()
        
        
    def enteringValuesToPort(self,textToEnter):
        for i in range(5) :
            print(i)
            self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Delete']").click()
        
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@class='android.view.View' and ./*[@contentDescription='Assigned Subnet Mask:']]").click()
        
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@contentDescription='Assigned UDP Port:' and @class='android.widget.EditText']").click()
        time.sleep(3)
        i=0

        while i < len(textToEnter):
            print(textToEnter[i])
            
            self.driver.find_element_by_xpath('//*[@contentDescription='+textToEnter[i]+']').click();
            i += 1
            
        time.sleep(3)
        
        self.driver.find_element_by_xpath("//*[@class='android.view.View' and ./*[@contentDescription='Assigned Subnet Mask:']]").click()
        
    
    
    ipPageValues = []
    
    def ip_page_Entries_read(self):
        time.sleep(5)
        ipPage=self.driver.find_element(By.XPATH,"//*[@class='android.view.View' and ./*[@contentDescription='IP']]")
        lenghtOftextfields=ipPage.find_elements(By.CLASS_NAME,'android.widget.EditText')
        time.sleep(2)  
        
        i=0
        for i in range(len(lenghtOftextfields)):
             
            ipPageValues=lenghtOftextfields[i].get_attribute('content-desc')
        print(len(ipPageValues))
        return ipPageValues
#         ipnetwork=lenghtOftextfields[0].get_attribute('content-desc')
#         print(ipnetwork)
#          
#         time.sleep(2)
#         assingnedIp=lenghtOftextfields[1].get_attribute('content-desc')
#         print(assingnedIp)
#         time.sleep(2)
#         subnetmask=lenghtOftextfields[2].get_attribute('content-desc')
#         time.sleep(2)
#         gatewayip=lenghtOftextfields[3].get_attribute('content-desc')
#         time.sleep(2)
#         udpport=lenghtOftextfields[4].get_attribute('content-desc')
#         time.sleep(2)
        #self.enteringValuesToPort(port)
         
        
    
    
    
    def router_page_Entries(self,ps1,ps2, ethernet):
        time.sleep(3)
        router=self.driver.find_element(By.XPATH,"//*[@class='android.view.View' and ./*[@contentDescription='Router']]")
        lenghtOftextfields=router.find_elements(By.CLASS_NAME,'android.widget.EditText')
        time.sleep(2) 
        
        lenghtOftextfields[2].click()
        for i in range(5):
            print(i)
            self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Delete']").click()
        
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@contentDescription='Settings']").click()
#         time.sleep(3)
#         self.driver.find_element_by_xpath("//*[@class='android.view.View' and ./*[@contentDescription='BACnet Network Number']]").click()    
        time.sleep(5)
        #self.driver.find_element_by_xpath("//*[@contentDescription='Port S1:' and @class='android.widget.EditText']").click()
        time.sleep(4)
        #self.driver.find_element_by_xpath("//*[@contentDescription='Port S1:' and @class='android.widget.EditText']").send_keys(ps1)
        self.driver.find_element_by_xpath("//*[@contentDescription='Ethernet:' and @class='android.widget.EditText']").click()
        
        #self.driver.find_element_by_xpath("//*[@contentDescription='Ethernet:' and @class='android.widget.EditText']")
        time.sleep(4)
        i=0
        while i < len(ps1):
            print(ps1[i])
            
            self.driver.find_element_by_xpath('//*[@contentDescription='+ps1[i]+']').click();
            i += 1
        
        
#         time.sleep(3)
        
            
          
       