'''
Created on Jan 7, 2020

@author: gaddams
'''
from Lib_space.SELENIUM.Page_locators import pagelocators 
from Lib_space.SELENIUM.BaseClass import Page
import time

class RunTest(Page):
    
    def dataSource(self,ds):
        time.sleep(2)
        self.click_element(*pagelocators.ACT.dataSrcBtn)
        #select = Select(self.driver.find_element_by_id('dataSource_select'))
        #select.select_by_value(ds)
        chooseDataSource =  self.driver.find_element_by_id('dataSource_select')
        chooseDataSource.send_keys(ds)
        btnTxt = self.get_text(*pagelocators.ACT.okDataSrcBtn)
        if(btnTxt == 'OK'):
            print( btnTxt +'Text displayed')
            self.click_element(*pagelocators.ACT.okDataSrcBtn)
        else:
            print('Wrong OK Button text/No button present')
     
    def groupEquipment(self):
        time.sleep(2)
        self.click_element(*pagelocators.ACT.groupEqBtn) 
        self.click_element(*pagelocators.ACT.allFwdBtn) 
        # Verify damper check box status & Check 
        result = self.driver.find_element_by_id('checkbox_damper_globe').is_selected()
        if result:
            print(' damper check box already selected')
        else:
            self.driver.find_element_by_id("checkbox_damper_globe").click()
            print(' damper check box selected')
        time.sleep(1)
        # Verify valve check box status & Check
        result = self.driver.find_element_by_id('checkbox_valve_globe').is_selected()
        if result:
            print('valve check box already selected')
        else:
            self.driver.find_element_by_id("checkbox_valve_globe").click()
            print('valve check box selected')
        time.sleep(1) 
        self.click_element(*pagelocators.ACT.okBtnGrpEqup)  