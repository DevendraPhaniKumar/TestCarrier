'''
Created on Sep 7, 2020

@author: Automation
'''

import os
import sys

from selenium.webdriver import *
#from notebook.tests.selenium.conftest import selenium_driver
from Lib_space.SELENIUM.Pages.WebCTRLPage import WebCTRL
from Lib_space.SELENIUM.BaseClass import WebDriver, Page
from Lib_space.SELENIUM.Page_locators.pagelocators import *
from Lib_space.SELENIUM.Page_locators.UIRegressionLocators.AlarmsTrendsActionLocators import AlarmsTrendsActions
from Lib_space.SELENIUM.Page_locators.UIRegressionLocators.HelpPagelocators import *
from Lib_space.SELENIUM.Page_locators.pagelocators import *
#from bs4 import element
from builtins import list
from _ast import List
from datetime import datetime as dt_time
from datetime import timedelta

dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
from Lib_space.SELENIUM.BaseClass import *
from Lib_space.SELENIUM.Pages.WebCTRLPage import *
from Lib_space.SELENIUM.Page_locators.pagelocators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

import time
import datetime
import socket
import netifaces
import unittest
import webcolors
import pywinauto

driver = object
delay = 45

DataParameter = configparser.ConfigParser()
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)


class HelpPage(Page):
    '''
    classdocs

    '''

    def __init__(self, selenium_driver):
        global driver, delay
        self.webctrlpage = WebCTRL(selenium_driver)
        self.driver = selenium_driver
        
        
        
        
        
    def main_help_page(self):
        '''
        Help page check from main page
        '''
        self.webctrlpage.selectActionIcon('Help')

        self.switch_to_child_window()
        self.switch_to_frame(HelpPageLocators.helppageFrame)
        textOnHelppage=self.get_text(*HelpPageLocators.propertiesPage)
        
        self.driver.close()
        self.switch_to_parent_window()
        self.switch_to_default_content()
        return textOnHelppage
        
        
    def graphics_help_page(self):
        '''
        Help page check from Graphics page
        '''
        self.webctrlpage.selectNode('geotree',['ColorMap'])
        time.sleep(2)
        self.webctrlpage.selectActionButton('Graphics')
        time.sleep(2)
        self.webctrlpage.selectActionIcon('Help')

        self.switch_to_child_window()
        self.switch_to_frame(HelpPageLocators.helppageFrame)
        textOnHelppage=self.get_text(*HelpPageLocators.graphicHelppage)
        
        self.driver.close()
        self.switch_to_parent_window()
        self.switch_to_default_content()
        return textOnHelppage
        
        
    def manual_command_help(self):
        '''
        Help page check from Manual command
        '''
        alert = self.webctrlpage.selectFromSystemDropdownMenu('Manual Command')
        time.sleep(3)
       
        alert.send_keys("help")
        time.sleep(1)
        alert.accept()
        time.sleep(3)
        self.switch_to_child_window()
        self.switch_to_frame(HelpPageLocators.helppageFrame)
        textOnHelppage=self.get_text(*HelpPageLocators.manualCommand)
        
        self.driver.close()
        self.switch_to_parent_window()
        self.switch_to_default_content()
        return textOnHelppage   
        
        
    
    def rightClick_help(self):
        '''
        Help page through right click
        '''
        self.webctrlpage.selectActionButton('Schedules')
        self.webctrlpage.selectTab('View')
        time.sleep(2)
        self.switch_to_default_content()
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        time.sleep(2)
        actionChains = ActionChains(self.driver)
        time.sleep(2)                                
        actionChains.context_click(self.driver.find_element_by_id('cjOuter')).perform()
        self.switch_to_default_content()
        self.switch_to_frame(WebCTRLPageLocators.menuFrame)
        self.find_element(*WebCTRLPageLocators.MenuTable)
        self.click_element(*HelpPageLocators.helpText)
        self.switch_to_child_window()
        self.switch_to_frame(HelpPageLocators.helppageFrame)
        textOnHelppage=self.get_text(*HelpPageLocators.rightClickText)
        
        self.driver.close()
        self.switch_to_parent_window()
        self.switch_to_default_content()
       
        
        return textOnHelppage   
    
    
    
    """
    def microBlock_help(self):
        '''
        Help page check from Microblock popup
        '''
        print("dsfjlsd")
        #self.webctrlpage.selectNode('geotree',['Zone Applications', 'VAV Teminal ZS'])
        self.webctrlpage.selectNode('geotree',['Home'])
        time.sleep(3)
        self.webctrlpage.selectActionButton('Logic')
        time.sleep(3)
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        time.sleep(20)
        actionChains = ActionChains(self.driver)
        time.sleep(2) 
        print(self.get_text(*HelpPageLocators.analogOutput))   
        #self.click_element(*HelpPageLocators.analogOutput)
        eleme=self.driver.find_elements_by_xpath('//img[@src="home_copy%40152026.png"]')
        
        self.driver.execute_script("arguments[0].click();", eleme[1])
        element=self.driver.find_element_by_xpath('//*[@class="Point-WidgetTextDisplay-base " and text()="analog output"]')
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.execute_script("arguments[0].click();", element)
                                    
        #actionChains.context_click(self.driver.find_element_by_id('logicgraphic')).perform()
        
# #         //div[@class="Div5px"
# #         self.click_element(*HelpPageLocators.analogOutput)
#         element=self.driver.find_element_by_xpath('//*[@class="Point-WidgetTextDisplay-base " and text()="analog output"]')
#         self.driver.execute_script("arguments[0].click();", element)
#         self.driver.execute_script("arguments[0].click();", element)
#         self.driver.execute_script("arguments[0].click();", element)
#         self.driver.execute_script("arguments[0].click();", element)
  
#         element=self.find_element(*HelpPageLocators.analogOutput)
#         element = self.driver.find_element_by_xpath("//*[@class="Point-WidgetTextDisplay-base " and text()='analog output']")
#         self.driver.execute_script("arguments[0].click();", element)
        
#         time.sleep(2)
#         element=self.find_element(*HelpPageLocators.analogOutput)
#         #element = self.driver.find_element_by_xpath("//button[@role='button']")
#         self.driver.execute_script("arguments[1].click();", element)

      """  
        
    def each_tab_help(self):
        
        
        print("dsfjlsd")
        
        
        
    def configure_popup_help(self):
        '''
        self.webctrlpage.rightclick_on_Node('geotree',['Zone Applications' ])
        self.switch_to_frame(WebCTRLPageLocators.menuFrame)
        time.sleep(5)
        menutable=self.find_element(*WebCTRLPageLocators.menuTableid)
        tableData=menutable.find_elements_by_tag_name('td')
        for j in range(len(tableData)):
            
            if(tableData[j].text=='Configure ...'):
                tableData[j].click()
                time.sleep(5)

        self.driver.switch_to_default_content()
        time.sleep(5)
        
        window_before = self.driver.window_handles[0]
        
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        
        self.switch_to.frame(ConfigurePage.actionframe)
        '''
        self.webctrlpage._clickingOn_right_MenuTable('geotree',['Alarms','Alarm Generator'],"Configure ...")
        time.sleep(2)
        print(len(self.driver.window_handles))
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        
        self.webctrlpage.selectActionIcon('Help')
        time.sleep(4)
        popups=self.driver.window_handles
        print(len(popups))
        #self.driver.switch_to.window(self.driver.window_handles[2])
        self.switch_to_child_window()
        self.driver.close()
        self.switch_to_parent_window()
        time.sleep(3)
        self.switch_to_child_window()
        
        time.sleep(2)
        
        self.switch_to_frame(HelpPageLocators.helppageFrame)
        #textOnHelppage=self.driver.find_element_by_xpath("//h3[text()='Working with control programs in the WebCTRL® interface']").text
        time.sleep(2)
        #textOnHelppage=self.get_text(*HelpPageLocators.configurePageText)
        time.sleep(2)
        self.driver.close()
        self.switch_to_parent_window()
 #         print(textOnHelppage)
        self.switch_to_default_content()
        #return textOnHelppage
          
        
        
    def help_function(self,tree,nodeList,textonpage):
        self.webctrlpage.selectNode(tree,nodeList)
        time.sleep(2)
        self.webctrlpage.selectActionIcon('Help')

        self.switch_to_child_window()
        self.switch_to_frame(HelpPageLocators.helppageFrame)
        textOnHelppage=self.driver.find_element_by_xpath("//h3[text()='"+textonpage+"']").text
        
        self.driver.close()
        self.switch_to_parent_window()
        self.switch_to_default_content()
        return textOnHelppage

        