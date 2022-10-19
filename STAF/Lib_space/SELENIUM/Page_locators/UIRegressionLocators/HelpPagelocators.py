'''
Created on Sep 7, 2020

@author: Automation
'''

from selenium.webdriver.common.by import By




class HelpPageLocators(object):
    '''
    classdocs
    '''
    propertiesPage=(By.XPATH,"//h3[text()='Properties pages']")
    helppageFrame='BODY'
    graphicHelppage=(By.XPATH,"//h3[text()='Graphics pages']")
    manualCommand=(By.XPATH,"//h3[text()='Manual commands']")
    rightClick=(By.ID, "cjOuter")
    helpText=(By.XPATH,"//td[text()='Help']")
    rightClickText=(By.XPATH,"//h3[text()='To view schedules']")
    analogOutput=(By.XPATH,"//span[text()='analog output']")
    
    popupHelppage=(By.XPATH,"//a[text()='Add a control program to a controller']")
    #configurePageText=(By.XPATH,"//h3[text()='Working with control programs in the WebCTRL® interface']")

    
