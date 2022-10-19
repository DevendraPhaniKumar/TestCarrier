import os
import sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
from Lib_space.SELENIUM.BaseClass import *
from Lib_space.SELENIUM.Pages.WebCTRLPages.WebCTRLPage import *
from Lib_space.SELENIUM.Page_locators.WebCTRLPageLocators.Webctrl_pagelocators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import datetime

driver = object
delay = 45

#This is useful to define the login page parameters
class WebCTRL(Page):

    # Actions
    def getdriver(self, selenium_driver):
        global driver, delay
        driver = selenium_driver
  
    def loginWebCTRL(self,user,password):   
        """
        Login to WebCTRL  
        """     
        self.send_keys(*LoginPageLocatars.EMAIL, value=user, clear_first=True,click_first=True)
        self.send_keys(*LoginPageLocatars.PASSWORD, value=password, clear_first=True,click_first=True)
        self.click_element(*LoginPageLocatars.SUBMIT)
        
        
    def logout(self):
        print('Proceeding to Logout')        
        self.click_element(*LoginPageLocatars.logout)
        time.sleep(2)
        self.switch_to_frame('rightMenuiframe')
        self.click_element(*LoginPageLocatars.LogoutLink)
        print('Logout Success')
        self.switch_to_default_content()
        
    
    def selectNode(self,tree, nodeList):
        """
        Select node from geoTree and networkTree

        Args: "nodeList" It is an array type, takes nodes name's as params eg: selectNode(['Zone Applications', 'VAV Terminal ZS', 'OA Temp'])
        
        """
        
        if(tree=='geotree'):
            self._navigateToGeoTree()
            time.sleep(3)
            self.driver.switch_to_frame("navTableFrame")
            self.driver.switch_to_frame("navContent")
            frame = self.driver.find_element_by_id('geoTree_2')
            time.sleep(1)            
            aaa,treeelementszero = self.selectingElement(frame, nodeList[0])
            self.imageArrowClick(treeelementszero)
        elif(tree=='nettree'):
            self._navigateToNetworkTree()
            time.sleep(3)
            self.driver.switch_to_frame("navTableFrame")
            self.driver.switch_to_frame("navContent")
            
            frame = self.driver.find_element_by_id('netTree_1c')

            time.sleep(2)
            
            aaa, treeelementszero = self.selectingElement(frame, nodeList[0])
            self.imageArrowClick(treeelementszero)

        for j in range(1, len(aaa)):
            try:
                ccc, treeelementszerodd = self.selectingElement(treeelementszero, nodeList[j])
                self.imageArrowClick(treeelementszerodd)
            except  (AttributeError, TypeError, IndexError)  as exception:
                pass
        self.driver.switch_to_default_content()
    
    def selectingElement(self,elementText, nodeList):
        """
         It traverse through Geo tree and selects the given node
             
         Args: "elementText" Node text which you want to select
        
        return: "treeElements" list
        """
        elementslistsss=[]
        tree_elementsList = elementText.find_element_by_xpath('../../..')
        
        treeElements=tree_elementsList.find_elements_by_tag_name('nobr')


        for i in range(len(treeElements)):
            
            if (treeElements[i].is_displayed()):
                if(treeElements[i].text == nodeList):
                    treeElements[i].click()
                    
                    return treeElements,treeElements[i]
                    

            else:
                try:

                    self.driver.execute_script("arguments[0].scrollIntoView();", treeElements[i])


                except NoSuchElementException as exception:
                    print("Element not found and test failed")
                    
    def _navigateToNetworkTree(self):
        
        """
         It traverse through Network tree and selects the given node
             
         Args: "elementText" Node text which you want to select
        
        return: "treeElements" list
        """
        
        self.driver.switch_to_frame("navTableFrame")

        frame = self.driver.find_elements_by_tag_name('img')
        for k in range(len(frame)):
                try:
                    if (frame[k].get_attribute("title") == 'Network'):
                        print(frame[k].get_attribute("title"))
                        frame[k].click()
                        self.driver.switch_to_default_content()
                        break
                except StaleElementReferenceException as exception:
                    pass

    def _navigateToGeoTree(self):
       
        """
         Navigates to GeoTree
             
             
        """
        self.driver.switch_to_frame("navTableFrame")

        frame = self.driver.find_elements_by_tag_name('img')
        for k in range(len(frame)):
            try:
                if (frame[k].get_attribute("title") == 'Geographic'):
                    print(frame[k].get_attribute("title"))
                    frame[k].click()
                    self.driver.switch_to_default_content()
                    break
            except StaleElementReferenceException as exception:
                pass

    def _clickingOn_Configure(self,element,filename):
        
        """
         It will perform rightclick on element given and uploads file.
             
         Args: "elementText" Node text which you want to select
        
        return: "treeElements" list
        """
        
        self.driver.switch_to_default_content()
        actionChains = ActionChains(self.driver)  # rightclick
        actionChains.context_click(element).perform()
        time.sleep(5)
        self.driver.switch_to_frame('menu1')
        time.sleep(5)
        menutable=self.driver.find_element_by_id("menutable")
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
        
        self.driver.switch_to_frame('actionContent')
        
        time.sleep(5)
        
        self.driver.find_element_by_xpath(
            '//*[@id="paddedDiv"]/table[3]/tbody/tr[2]/td/div/table[1]/tbody/tr[2]/td/span[3]/span').click()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(5)
        self.driver.switch_to.frame("actionContent")
        time.sleep(5)
        
        elem = self.driver.find_element_by_xpath(".//*[@id='sourcePath']")
        dirpath = dirnameutils+'\TouchFile'
        elem.send_keys(r''+dirpath+"\\"+filename)
        
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="addform"]/table/tbody/tr[4]/td/span').click()
        time.sleep(3)

        continueButton=self.check_exists_by_xpath()
        if(continueButton):

            self.driver.find_element_by_xpath('//*[@id="paddedDiv"]/div[2]/span[1]').click()

        else:
            
            print("TextVerification")

        filesuccessMessage = self.driver.find_element_by_xpath('//*[@id="paddedDiv"]/div').text
        if (filesuccessMessage == 'File added successfully.'):
            self.driver.close()
        else:
            print("TestFailed")
        time.sleep(5)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        
        time.sleep(3)
        self.driver.close()
        time.sleep(3)
        self.driver.switch_to.window(window_before)


    def check_exists_by_xpath(self):
       
        try:
            self.driver.find_element_by_xpath('//*[@id="paddedDiv"]/div[2]/span[1]')
        except NoSuchElementException:
            return False
        return True


    def downloadDevice(self,deviceName):
        """
         It will perform download activity.
             
         Args: "deviceName" name of the device
        
         
        """
        self.driver.switch_to_default_content()
        alert = self.selectFromSystemDropdownMenu('Manual Command')
        time.sleep(8)
        print(alert.text)
        alert.send_keys("rnet here force")
        time.sleep(3)
        alert.accept()
        time.sleep(8)
        self.driver.switch_to_default_content()
        time.sleep(8)
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        time.sleep(5)
        self.driver.switch_to.window(window_after)
        time.sleep(5)
        filesuccessMessage = self.driver.find_element_by_xpath('//*[@id="msgField"]/pre').text

        if ('Current module address' in filesuccessMessage):   
            self.driver.close()          
        else:
            self.driver.close()
            print("TestFailed")
        self.driver.switch_to.window(window_before)
        self.driver.switch_to_default_content()


    def downloadDevicefromDownloadPage(self,deviceName):
        """
         It will perform download activity.
             
         Args: "deviceName" name of the device
        
         
        """
        
        self.driver.switch_to_frame("actionContent")
        activityTable = self.driver.find_element_by_id("activityTable")
        deviceNames = activityTable.find_elements_by_tag_name('tr')
        for i in range(len(deviceNames)):
            
            if(deviceName in deviceNames[i].text):
                deviceNames[i].click()
                time.sleep(3)
                self.downloadDevice(deviceName)
                time.sleep(2)
                self.driver.switch_to_frame("actionContent")
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="cjOuter"]/table[1]/tbody/tr/td[1]/span[2]/span[1]/span').click()
                time.sleep(2)
        
        try:
            ui.WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="TableWithoutData"]/td')))
            print("Download is success full")
        except TimeoutException:
            print("Download is failed")
        self.driver.switch_to_default_content()        
        
    
    def selectFromSystemDropdownMenu(self,dropDownLink):
        """
        This function will  select items from system dropdown menu Manual Command, Log out, etc.. 
         param: "dropDownLink" text of dropdownlink
         return: default content
        """

        table = self.find_element(*WebCTRLPageLocators.ActionBarMain)
        tableRow = table.find_elements(*WebCTRLPageLocators.ActionBarTable)
        for i in range(len(tableRow)):
            if(tableRow[i].get_attribute("class")=='menuSection barBg'):
                tableRow[i].click()
                self.driver.switch_to_frame('rightMenuiframe')

                tableofDropDown=self.find_element(*WebCTRLPageLocators.PopupTable)
                dropDownText = tableofDropDown.find_elements(*WebCTRLPageLocators.DivOfActionButton2)

                for j in range(len(dropDownText)):

                    if (dropDownText[j].text == dropDownLink):


                        if (dropDownText[j].text == 'Manual Command'):
                            dropDownText[j].click()
                            return self.getManualCommandDialog()


                        elif (dropDownText[j].text == 'Set up Tree'):
                            dropDownText[j].click()

                            return self.getSetUpTreeDialog()

                        elif (dropDownText[j].text == 'About WebCTRL'):
                            dropDownText[j].click()

                            return self.getAboutWebCTRLDialog();

                        elif (dropDownText[j].text == 'Log out'):
                            dropDownText[j].click()

                            return self.driver

                        else:

                            return self.getActionPane()

        self.driver.switch_to_default_content()

    def getManualCommandDialog(self):

        return self.driver.switch_to.alert

    def getSetUpTreeDialog(self):
        """
         This will open setup tree dialog. 
         
         
        """
       
        window_after = self.driver.window_handles[1]
        
        self.driver.switch_to.window(window_after)
        str2 = self.driver.title
        

    def getAboutWebCTRLDialog(self):
        """
        This will open About dialog

        """
        window_after = self.driver.window_handles[1]
        
        self.driver.switch_to.window(window_after)
        str2 = self.driver.title
        

    def getActionPane(self):
        """
        It will locate action pane popup

        return: webElement
        """
        return self.find_element(*WebCTRLPageLocators.ActionContainer)

    def selectActionButton(self, buttonName):
        """

        :param buttonName:
        :return:
        """
        time.sleep(3)
        actionButtonSpan = self.find_element(*WebCTRLPageLocators.ActionButtonSpan)
        time.sleep(3)
        bttonsNames = actionButtonSpan.find_elements(*WebCTRLPageLocators.DivOfActionButton)
        for i in range(len(bttonsNames)):
            try:
             if (bttonsNames[i].text == buttonName):
                 bttonsNames[i].click()
                 return self.getActionPane()

            except StaleElementReferenceException as exception:
                pass

        #return self.getActionPane()
        #self.driver.switch_to_default_content()





    def selectFromDropdownArrow(self, buttonName):
        """

        :param buttonName:
        :return:
        """
        time.sleep(1)
        actionButtonSpan = self.find_element(*WebCTRLPageLocators.ActionButtonSpan)

        bttonsNames = actionButtonSpan.find_elements(*WebCTRLPageLocators.DivOfActionButton)
        for i in range(len(bttonsNames)):
            try:
             if (bttonsNames[i].text == buttonName[0]):
                 imgArrow=bttonsNames[i].find_element_by_xpath('../..')
                 #actionButtonchildspan = actionButtonSpan.find_elements(*WebCTRLPageLocators.SpanOfActionButton)
                 dropdownArrow = imgArrow.find_elements(*WebCTRLPageLocators.DropDownArrow)
                 dropdownArrow[2].click()

                 self.driver.switch_to_frame("actioncategories")

                 table=self.find_element(*WebCTRLPageLocators.PopupTable)
                 tableRow=table.find_elements(*WebCTRLPageLocators.DivOfActionButton2)
                 #tableRow[1].click()
                 for i in range(len(tableRow)):


                     actualMenutext=tableRow[i].text
                     trimactualMenutext=actualMenutext.strip()

                     if(trimactualMenutext==buttonName[1]):
                         tableRow[i].click()
                         self.driver.switch_to_default_content()
                         if(len(buttonName)==3):
                             self.driver.switch_to_frame("actioninstances")

                             table2 = self.find_element(*WebCTRLPageLocators.PopupTable)
                             tableRow2 = table2.find_elements(*WebCTRLPageLocators.DivOfActionButton2)
                             # tableRow[1].click()
                             for i in range(len(tableRow2)):


                                 actualMenutext = tableRow2[i].text
                                 trimactualMenutext = actualMenutext.strip()

                                 if (trimactualMenutext == buttonName[2]):
                                     tableRow2[i].click()
                                     self.driver.switch_to_default_content()
                 self.driver.refresh()
                 return self.getActionPane()

                 break
            except StaleElementReferenceException as exception:
                pass
        
        