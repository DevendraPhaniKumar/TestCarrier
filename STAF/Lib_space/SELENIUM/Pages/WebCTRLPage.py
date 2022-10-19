import os
import sys
from xml.dom.minicompat import NodeList

dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
from Lib_space.SELENIUM.BaseClass import *
from Lib_space.SELENIUM.Pages.WebCTRLPage import *
from Lib_space.SELENIUM.Page_locators.pagelocators import *

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
# from selenium.webdriver.common.by import By
# import time
# import datetime
import socket
import netifaces
import datetime
import configparser

driver = object
delay = 45
global IP_ADDRESS,SUBNET_MASK
IP_ADDRESS=[]
SUBNET_MASK=[]
CategoriesList=['Schedule', 'Alarm', 'Graphic', 'Property', 'Trend', 'Report']
#This is useful to define the login page parameters

DataParameter = configparser.ConfigParser()
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)
DataParameter.read(dirnameutils + '\\Data\\SELENIUM\\UIRegression\\UIRegressionData.ini')



class WebCTRL(Page):
    """ 
    This is a class All webCTRL actions like selecting Tabs and Navigating to other pages 
      
    Attributes: 
        Page (class): It holds all common functions like click_elemnt(), get_text() etc 
        
    """

    
    def getdriver(self, selenium_driver):
        """
        responsible for holding sleneium driver
        Parameters: 
            selenium_driver (String): driver instance
              
        
        """     

        global driver, delay
        driver = selenium_driver
  
    def loginWebCTRL(self,user,password):   
        """
        Login to WebCTRL using username and password
       
        Parameters: 
            user (String): Username of current user.
            passwords (String): passwords of current user. 
        
        Returns:
            Nothing
        
        """     
        self.send_keys(*LoginPageLocatars.EMAIL, value=user, clear_first=True,click_first=True)
        self.send_keys(*LoginPageLocatars.PASSWORD, value=password, clear_first=True,click_first=True)
        self.click_element(*LoginPageLocatars.SUBMIT)
        
        
    def logout(self):
        """
        Logout from WebCTRL
       
        Parameters: 
            
        
        Returns:
            Nothing
        
        """     
        print('Proceeding to Logout')        
        self.click_element(*LoginPageLocatars.logout)
        time.sleep(2)
        self.switch_to_frame(WebCTRLPageLocators.rightMenu_iFrame)
        self.click_element(*LoginPageLocatars.LogoutLink)
        print('Logout Success')
        self.switch_to_default_content()
        
    
    def selectTab(self,tabName):
        
        """
        This function will select the tab under the ActionBarManager eg: view, Manages, Actions, etc...
       
        Parameters: 
            tabName (String): Name of the tab
             
        
        Returns:
            Nothing
        
        """
        self.switch_to_frame(WebCTRLPageLocators.faceContentIframe)
        self.driver.find_element_by_xpath("//div[text()='"+tabName+"']").click()
        '''
        time.sleep(2)

        actionButtonContainer = self.find_element(*WebCTRLPageLocators.ActionButtonContainer)
        time.sleep(3)
        tabNames = actionButtonContainer.find_elements(*WebCTRLPageLocators.DivOfActionButton)
        for i in range(len(tabNames)):
            try:
                if (tabNames[i].text == tabName):
                    tabNames[i].click()
                    break
            except StaleElementReferenceException as exception:
                raise Exception
        '''
        self.driver.switch_to_default_content()
        
        
    def _acceptChanges(self):      
        
        """
        Selecting Accept Button
       
        Parameters: 
            
        Returns:
            Nothing
        
        """

        self.driver.switch_to_default_content()
        self.driver.find_element(*ConfigurePage.AcceptButton).click()  
        
        
    def _applyChanges(self):
        """
        Selecting Apply Button
       
        Parameters: 
            
        Returns:
            Nothing
        
        """
        self.driver.switch_to_default_content()
        self.driver.find_element(*ConfigurePage.ApplyButton).click()
        
    
    def _cancelChanges(self):
        """
        Selecting Cancel Button
       
        Parameters: 
            
        Returns:
            Nothing
        
        """
        self.driver.switch_to_default_content()
        self.driver.find_element(*ConfigurePage.cancelButton).click()    
      
    
    
    def selectNode(self,tree, nodeList):

        """ 
        Select node from geoTree and networkTree.
  
        Parameters: 
            nodeList (List): It is an array type, takes nodes name's as params eg: selectNode('GeotTree', ['Zone Applications', 'VAV Terminal ZS', 'OA Temp']) 
            tree (String): takes 'geotree', 'nettree'
        Returns: 
            Nothing
        """
        
        if(tree=='geotree'):
            self._navigateToGeoTree()
            time.sleep(3)
            self.switch_to_frame(WebCTRLPageLocators.networkIframe)
            self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)
            #rootNode = self.driver.find_element_by_id('geoTree_2')
            rootNode = self.find_element(*WebCTRLPageLocators.GeoTreeHead)
        elif(tree=='nettree'):
            self._navigateToNetworkTree()
            time.sleep(3)
            self.switch_to_frame(WebCTRLPageLocators.networkIframe)
            self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)        
            rootNode = self.find_element(*WebCTRLPageLocators.NetTreeHead)
        tempCount=len(nodeList)-1
        for j in range(len(nodeList)):
           element= self.elementSelection(rootNode,nodeList[j])
           if(j==tempCount):
               print("Dont click on arrow as it is Las element")
               try:
                   element.click()
               except ElementNotInteractableException as exception:
                    time.sleep(2)
                    self.driver.find_element_by_xpath("//nobr[text()='"+nodeList[j]+"']").click() 
               
           else:                
             
             self.driver.find_element_by_xpath("//nobr[text()='"+nodeList[j]+"']").click()
             self.imageArrowClick(element)
             
        self.driver.switch_to_default_content()        
        
    
    def selectingElement(self,elementText, nodeList):
        """ 
        It traverse through Geo tree and selects the given node
  
        Parameters: 
            nodeList (List): It is an array type, takes nodes name's as params eg: selectNode('GeotTree', ['Zone Applications', 'VAV Terminal ZS', 'OA Temp']) 
            elementText (String): Node text which you want to select
        Returns: 
            "treeElements" list
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
                    
                    
    def imageArrowClick(self,parentElement):
        """

        :param parentElement:
        """
        imgArrow = parentElement.find_element_by_xpath('../..')
        # actionButtonchildspan = actionButtonSpan.find_elements(*WebCTRLPageLocators.SpanOfActionButton)
        dropdownArrow = imgArrow.find_elements(*WebCTRLPageLocators.DropDownArrow)
        time.sleep(2)
        collapsedOrExpandedArrow=dropdownArrow[0].get_attribute('src')
        #print(collapsedOrExpandedArrow)
        substring="clean_collapsed.png"

        if (collapsedOrExpandedArrow.find(substring) == -1):
            print("arrow already expaded")
        else:
            self.driver.execute_script("arguments[0].click();", dropdownArrow[0])
                    
    def _navigateToNetworkTree(self):
        
        """ 
        It navigate to network tree
  
        Parameters: 
            
        Returns: 
            
        """
        
        self.switch_to_frame(WebCTRLPageLocators.networkIframe)

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
        Navigate to GeoTree
  
        Parameters: 
            
        Returns: 
           
        """        
        self.switch_to_frame(WebCTRLPageLocators.networkIframe)
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
  
        Parameters: 
            filename (String): Name of the file you want to upload 
            elementText (String): Node text which you want to select
        Returns: 
        
        """
        
        self.driver.switch_to_default_content()
        actionChains = ActionChains(self.driver)  # rightclick
        actionChains.context_click(element).perform()
        time.sleep(5)
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
        
        time.sleep(5)
        
        self.driver.find_element_by_xpath(
            '//*[@id="paddedDiv"]/table[3]/tbody/tr[2]/td/div/table[1]/tbody/tr[2]/td/span[3]/span').click()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(5)
        self.switch_to.frame(*ConfigurePage.actionframe)
        time.sleep(5)
        
        elem = self.find_element(*ConfigurePage.sourcePath)
        dirpath = dirnameutils+'\TouchFile'
        elem.send_keys(r''+dirpath+"\\"+filename)
        
        time.sleep(3)
        self.find_element(*WebCTRLPageLocators.ContinueButton).click()
        time.sleep(3)

        continueButton=self.check_exists_by_xpath()
        if(continueButton):

            self.click_element(*WebCTRLPageLocators.buttonAttach)

        else:
            
            print("TextVerification")

        filesuccessMessage = self.get_text(*WebCTRLPageLocators.fileSucessMessage)
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
    

    
    def downloadDevicee(self):
        """
         It will perform download activity.
             
         Args: "deviceName" name of the device
        
         
        """
        
        time.sleep(15)
        self.driver.switch_to_default_content()
        alert = self.selectFromSystemDropdownMenu('Manual Command')
        time.sleep(8)
        print(alert.text)
        #alert.send_keys("rnet here force")
        alert.send_keys("download")
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
        self.driver.close()  
         
        
        self.driver.switch_to.window(window_before)
        self.driver.switch_to_default_content()    
        self.switch_to.frame(*ConfigurePage.actionframe)

        try:
            ui.WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="TableWithoutData"]/td')))
            print("Download is success full")
        except TimeoutException:
                print("Download is failed")
        
        
        self.driver.switch_to_default_content() 
#         #self.driver.find_element_by_xpath('//*[@id="TableWithoutData"]/td').click()
#         self.driver.find_element_by_xpath('//*[@id="MainBarTR"]').click()
#         
#         self.selectFromSystemDropdownMenu('Log out Administrator')
#         
    
    def downloadDevice(self,deviceName):
        
        """ 
        It will perform download activity.
  
        Parameters: 
            deviceName (String): Name of the device 
          
        Returns: 
            
        """
        self.driver.switch_to_default_content()
        alert = self.selectFromSystemDropdownMenu('Manual Command')
        time.sleep(8)
        print(alert.text)
        #alert.send_keys("rnet here force")
        alert.send_keys("download")
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
        filesuccessMessage = self.get_text(*WebCTRLPageLocators.filesuccessMessage2)

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
  
        Parameters: 
            deviceName (String): Name of the device 
          
        Returns: 
            
        """        
        self.switch_to_frame(WebCTRLPageLocators.actionframe)        
        activityTable = self.find_element(*WebCTRLPageLocators.activityTable)
        deviceNames = activityTable.find_elements_by_tag_name('tr')
        for i in range(len(deviceNames)):
            
            if(deviceName in deviceNames[i].text):
                deviceNames[i].click()
                time.sleep(3)
                self.downloadDevice(deviceName)
                time.sleep(2)
                self.switch_to_frame(WebCTRLPageLocators.actionframe)
                time.sleep(2)
                self.click_element(*Downloadpage.startButton2)
                time.sleep(2)
        
        try:
            ui.WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="TableWithoutData"]/td')))
            print("Download is success full")
        except TimeoutException:
            print("Download is failed")
        self.driver.switch_to_default_content()   
        
    
    def selectActionIcon(self,iconName):
        """
        This function will selects Action icon items Time-Lapse, Print, Alarm, etc..
        :param iconName:
        :return:
        """
        
        table = self.find_element(*WebCTRLPageLocators.ActionBarMain)
        tableRow = table.find_elements(*WebCTRLPageLocators.ActionBarTable)
        for i in range(len(tableRow)):
            if (tableRow[i].get_attribute("class") == 'buttonSection barBg'):

                #self.driver.switch_to_frame("rightMenuiframe")

                #tableofDropDown = self.find_element(*WebCTRLPageLocators.PopupTable)
                iconNames = tableRow[i].find_elements(*WebCTRLPageLocators.DropDownArrow)

                for j in range(len(iconNames)):

                    if (iconNames[j].get_attribute("title") == iconName):

                        if (iconNames[j].get_attribute("title") == 'Time-lapse'):
                            iconNames[j].click()
                            return self.getTimeLapseWindow()

                        elif (iconNames[j].get_attribute("title") == 'Print'):
                            iconNames[j].click()
                            return self.getPrintDialog()

                        elif (iconNames[j].get_attribute("title") == 'System-Level Alarms'):
                            iconNames[j].click()

                            return self.getActionPane();

                        elif (iconNames[j].get_attribute("title") == 'Help'):
                            time.sleep(2)
                            iconNames[j].click()
                            #New tab handling code should be added here
                            



                        else:

                            return self.getActionPane()

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

                        elif (dropDownText[j].text == dropDownLink):
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
        This function will click on ActionBar buttons eg:  Alarms, Graphics, Schedules etc...

 
        :param buttonName:
        :return:
        """
        '''
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
        self.driver.switch_to_default_content()
        '''
        self.driver.find_element_by_xpath("//div[text()='"+buttonName+"']").click()
        





    def selectFromDropdownArrow(self, buttonName):
        """
        This function will  dropDown arrow items from actionBarManager tabs
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

                 self.switch_to_frame(WebCTRLPageLocators.actionCategoriesFrame)

                 table=self.find_element(*WebCTRLPageLocators.PopupTable)
                 tableRow=table.find_elements(*WebCTRLPageLocators.DivOfActionButton2)
                 #tableRow[1].click()
                 for i in range(len(tableRow)):


                     actualMenutext=tableRow[i].text
                     trimactualMenutext=actualMenutext.strip()

                     if(trimactualMenutext==buttonName[1]):
                         tableRow[i].click()
                         self.switch_to_default_content()
                         if(len(buttonName)==3):
                             self.switch_to_frame(WebCTRLPageLocators.actionInstancesFrame)

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
    
    def getColor(self,*locator):
        return self.driver.find_element(*locator).value_of_css_property('background-color')
        #return self.driver.find_element(*locator).text;
        
    def absenceOfElement(self,*locator): 
        with self.assertRaises(NoSuchElementException):
            self.page.click_element(*EndToEndGraphicsPage.FailedText)
            
            
            
        
    
    def selectNode_rightClick(self,nodeList):
        """
        Select node from networkTree

        Args: "nodeList" It is an array type, takes nodes name's as params eg: selectNode(['Zone Applications', 'VAV Terminal ZS', 'OA Temp'])
        
        """
        
        
        self._navigateToNetworkTree()
        time.sleep(3)
        self.switch_to_frame(WebCTRLPageLocators.networkIframe)
        self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)        
        frame = self.find_element(*WebCTRLPageLocators.NetTreeHead)
        tempCount=len(nodeList)-1
        for j in range(len(nodeList)):
            tree_elementsList = frame.find_element_by_xpath('../../..')
            time.sleep(2)
            treeElements=tree_elementsList.find_elements_by_tag_name('nobr')
            for i in range(len(treeElements)):
                print(treeElements[i].text)                    
                if(treeElements[i].is_displayed()):
                    if(treeElements[i].text == nodeList[j]):
                        if(j==tempCount):
                            time.sleep(2)
                            actionChains = ActionChains(self.driver)
                            time.sleep(2)                                
                            actionChains.context_click(treeElements[i]).perform()
                            self.switch_to_default_content()
                            try:
                                self.switch_to_frame(WebCTRLPageLocators.menuFrame)
                                return self.find_element(*WebCTRLPageLocators.MenuTable)
                            except NoSuchElementException:
                                self.switch_to_default_content()
                                time.sleep(3)
                                self.switch_to_frame(WebCTRLPageLocators.networkIframe)
                                self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)
                                time.sleep(2)
                                originalemelemetn=self.driver.find_element_by_xpath("//nobr[text()='"+nodeList[j]+"']")
                                time.sleep(2)
                                actionChains.context_click(originalemelemetn).perform()
                                self.switch_to_default_content()
                                self.switch_to_frame(WebCTRLPageLocators.menuFrame)
                                return self.find_element(*WebCTRLPageLocators.MenuTable)
                            time.sleep(2)
                            self.switch_to_default_content()
                            time.sleep(1)
                            self.switch_to_frame(WebCTRLPageLocators.menuFrame)
                            return self.find_element(*WebCTRLPageLocators.MenuTable)
                            
                        else:
                            treeElements[i].click()
                            imgArrow = treeElements[i].find_element_by_xpath('../..')
                            dropdownArrow = imgArrow.find_elements(*WebCTRLPageLocators.DropDownArrow)
                            time.sleep(2)
                            collapsedOrExpandedArrow=dropdownArrow[0].get_attribute('src')
                            substring="clean_collapsed.png"
                            if (collapsedOrExpandedArrow.find(substring) == -1):
                                print("arrow already expaded")
                            else:
                                self.driver.execute_script("arguments[0].click();", dropdownArrow[0])


    
    def configuring_Driver_version(self,filename):
        '''
        Driver file changing to new driver file.
        
        '''
        
        self.click_element(*WebCTRLPageLocators.Configure)
        parentWindow = self.driver.window_handles[0]
        time.sleep(1)
        childWindow = self.driver.window_handles[1]
        self.driver.switch_to_window(childWindow)
        time.sleep(3)
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        time.sleep(3)
        self.click_element(*WebCTRLPageLocators.AddButton)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(5)
        self.switch_to.frame(WebCTRLPageLocators.actionframe)
        time.sleep(5)
        elem = self.find_element(*WebCTRLPageLocators.PathElement)
        elem.send_keys(r''+dirnameutils+"\\Utility\\DriverFiles\\"+filename)
        time.sleep(3)
        self.click_element(*WebCTRLPageLocators.ContinueButton)
        time.sleep(3)
        filesuccessMessage = self.get_text(*WebCTRLPageLocators.Upload_Sucess)
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
        self.driver.switch_to.window(parentWindow)
        
                
        
        
    def changeDriverFile(self,nodeList, filename):
        '''
        it changes the driver file in given node.
        
        '''
        
        self.selectNode_rightClick(nodeList)        
        self.configuring_Driver_version(filename)
        
        self.downloadDevicee()
        
        
        
    
    def navigateTo_ConfigTree(self):
        """ 
         It Navigates to config Tree 
  
        Parameters: 
             
          
        Returns: 
             
        """
        time.sleep(3)
        self.switch_to_frame(WebCTRLPageLocators.networkIframe)
        self.click_element(*WebCTRLPageLocators.ConfigTree)
        self.switch_to_default_content()
        
    def navigateTo_CofingTree_Links(self,link):
        """ 
        Clicks on ConfigTree links 
  
        Parameters: 
            link (String): Link text of configTree items  
          
        Returns: 
             
        """
        time.sleep(1)
        self.switch_to_frame(WebCTRLPageLocators.networkIframe)
        self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)
        time.sleep(2)
        if link in CategoriesList:
            self.click_element(*ConfigurePage.expandCategories)
            
        #self.driver.find_element_by_xpath("//*[@id='configTree_1bb']").click()
        self.driver.find_element_by_xpath("//nobr[text()='"+link+"']").click()
        if link in CategoriesList:
            self.click_element(*ConfigurePage.expandCategories)
            
        self.driver.switch_to_default_content()
        
    def configuringServerIP(self):
        """ 
        This method is responsible for configuring IP in connections Tab 
  
        Parameters: 
             
          
        Returns: 
             
        """
        self.ipAddress()
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        self.click_element(*ConfigurePage.BacNetIPConnection)
        self.click_element(*ConfigurePage.stopButtonOrStart)
        
        alert=self.driver.switch_to.alert
        alert.accept()
               
        self.click_element(*ConfigurePage.iPAddressField)
        
        self.click_element(*ConfigurePage.subneMask)
        panelBacNetIP=self.find_element(*ConfigurePage.bacnetIPPanel)
        fields=panelBacNetIP.find_elements_by_xpath('//*[@id="undefined"]')
        print(len(fields))
        time.sleep(1)
        fields[0].clear()
        fields[0].send_keys(IP_ADDRESS[1])
        fields[1].clear()
        fields[1].send_keys(SUBNET_MASK[1])
        time.sleep(2)
        self.switch_to_default_content()
        self.find_element(*ConfigurePage.AcceptButton).click()
        
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        self.click_element(*ConfigurePage.stopButtonOrStart)
        
        self.switch_to_default_content()
        

    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        My_ip=s.getsockname()[0]
        s.close()
        return My_ip

    
    def ipAddress(self):
        for i in netifaces.interfaces():
            try:
               
                IP_ADDRESS.append(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
                SUBNET_MASK.append(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
            except:pass

   
        
        
    
    def addDeviceToDownload(self, nodeToPick, deviceName):
        '''
        Adds specific device to download.
        @nodeToPick
        @deviceName
        '''
        
        self.selectNode('nettree', nodeToPick)
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        self.click_element(*Downloadpage.addButton)
        parentWindow = self.driver.window_handles[0]
        time.sleep(1)
        childWindow = self.driver.window_handles[1]
        self.driver.switch_to_window(childWindow)
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        self.driver.find_element_by_xpath("//nobr[text()='"+deviceName+"']").click()
        self.click_element(*Downloadpage.addButtonOnPopup)
        self.driver.close()
        self.driver.switch_to_window(parentWindow)
        
        
        
    
    
    def downloadToDevice(self):
        '''
        Downloads the selected device
        '''
#         print('aaaaa')
#         self.selectNodeeNew('nettree', nodeToPick)
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        
        selectAllcheckBoxText=self.find_element(*Downloadpage.selectAllCheckBox)
        checkbox=selectAllcheckBoxText.find_element_by_xpath('..')
        #selectAllcheckBoxText.find_element_by_xpath('..')
        test=checkbox.find_elements_by_tag_name('img')
        
        test[10].click()
        self.click_element(*Downloadpage.startButton)
        try:
            ui.WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="TableWithoutData"]/td')))
            print("Download is success full")
        except TimeoutException:
                print("Download is failed")
        self.switch_to_default_content()
        
        
    def changeServerIPAddress(self):
        '''
        This function will change the IP address to current machine IP.
        
        '''
        self.navigateTo_ConfigTree()
        self.navigateTo_CofingTree_Links("Connections")
        self.selectTab('Configure')
        self.configuringServerIP()
        
        
    def generate_Alarms(self):
        """
        Generating Alarms using Alarm Generator
        """
        
        self.selectNodeeNew('geotree', ['Alarms','Alarm Generator'])
        time.sleep(2)
        self.selectActionButton('Properties')
        time.sleep(2)
        self.selectTab('Control Program')
        time.sleep(2)
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        self.click_element(*WebCTRLPageLocators.alarmGeneratorON_OF)
        
        #self.driver.find_element(*AlarmsTrendsActions.alarmGeneratorON_OF).click()
        self.click_element(*WebCTRLPageLocators.onLink)
        self._acceptChanges()
        time.sleep(5)
        popups=self.driver.window_handles
        if len(popups)==2:
            print('Need to enter passoword')
            print(dirnameutils + '\\Data\\SELENIUM\\UIRegression\\')
            self.switch_to_child_window()
            print(self.driver.title)
            self.switch_to_frame(WebCTRLPageLocators.actionframe)
            self.send_keys(*WebCTRLPageLocators.securityPassword, value=DataParameter.get( "Username_Password","password"), clear_first=True, click_first=True)
            self.send_keys(*WebCTRLPageLocators.commentBox, value="Generation Alarms", clear_first=True, click_first=True)
            time.sleep(2)
            self.click_element(*WebCTRLPageLocators.okButton)
        
            self.switch_to_parent_window()
            self.switch_to_default_content()
            
        time.sleep(6)
        self.selectTab('Control Program')
        time.sleep(2)
        self.driver.switch_to_frame("actionContent")
        self.click_element(*WebCTRLPageLocators.alarmGeneratorON_OF)
        self.click_element(*WebCTRLPageLocators.offLink)
        self._acceptChanges()
        time.sleep(5)
        popups=self.driver.window_handles
        if len(popups)==2:
            print('Need to enter passoword')
            print(dirnameutils + '\\Data\\SELENIUM\\UIRegression\\')
            self.switch_to_child_window()
            print(self.driver.title)
            self.switch_to_frame(WebCTRLPageLocators.actionframe)
            self.send_keys(*WebCTRLPageLocators.securityPassword, value=DataParameter.get( "Username_Password","password"), clear_first=True, click_first=True)
            self.send_keys(*WebCTRLPageLocators.commentBox, value="Generation Alarms", clear_first=True, click_first=True)
            time.sleep(2)
            self.click_element(*WebCTRLPageLocators.okButton)
        
            self.switch_to_parent_window()
            self.switch_to_default_content()
        
        
#         systemLevelAlarmIcon=self.find_element(*WebCTRLPageLocators.systemLevelAlarms)
#         print(systemLevelAlarmIcon.value_of_css_property('color'))
        
        
        
    def selectNodeeNew(self,tree, nodeList):
        if(tree=='geotree'):
            self._navigateToGeoTree()
            time.sleep(3)
            
            self.switch_to_frame(WebCTRLPageLocators.networkIframe)
            self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)
            rootNode = self.find_element(*WebCTRLPageLocators.GeoTreeHead)
#             time.sleep(1)            
#             aaa,treeelementszero = self.selectingElement(frame, nodeList[0])
#             self.imageArrowClick(treeelementszero)
        elif(tree=='nettree'):
            self._navigateToNetworkTree()
            time.sleep(3)
            self.switch_to_frame(WebCTRLPageLocators.networkIframe)
            self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)     
            rootNode = self.find_element(*WebCTRLPageLocators.NetTreeHead)
        tempCount=len(nodeList)-1
        for j in range(len(nodeList)):
           element= self.elementSelection(rootNode,nodeList[j])
           if(j==tempCount):
               print("Dont click on arrow as it is Las element")
               try:
                   element.click()
               except ElementNotInteractableException as exception:
                    time.sleep(2)
                    self.driver.find_element_by_xpath("//nobr[text()='"+nodeList[j]+"']").click() 
               
           else:                
             
             self.driver.find_element_by_xpath("//nobr[text()='"+nodeList[j]+"']").click()
             self.imageArrowClick(element)
             
        self.switch_to_default_content()
            
                                
                                
                                
    def elementSelection(self,rootNode,nodeList):
        tree_elementsList = rootNode.find_element_by_xpath('../../..')
        time.sleep(2)
        treeElements=tree_elementsList.find_elements_by_tag_name('nobr')
        
        for i in range(len(treeElements)):
            if(treeElements[i].is_displayed()):
                if(treeElements[i].text == nodeList): 
                    #self.imageArrowClick(treeElements[i])  
                    time.sleep(2)                                           
                    #treeElements[i].click() 
                    return treeElements[i]
                    
            else:
                try:

                    self.driver.execute_script("arguments[0].scrollIntoView();", treeElements[i])
                    
                    
                except NoSuchElementException as exception:
                    print(exception)
        return treeElements[i]
                    
                    
                    
    
    
            

                                                  
                                    
                                    
                                    
                                    
    def rightclick_on_Node(self,tree, nodeList):
        """
        Select node from geoTree and networkTree and right click on node

        Args: 
            nodeList(List): "nodeList" It is an list type, takes nodes name's as params eg: selectNode('GeotTree', ['Zone Applications', 'VAV Terminal ZS', 'OA Temp'])
            tree(String): Takes geotree, and nettree as arguments
        returns:
            returns menu table webElwment
        
        """

        if(tree=='geotree'):
            self._navigateToGeoTree()
            time.sleep(3)
            self.switch_to_frame(WebCTRLPageLocators.networkIframe)
            self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)
            rootNode = self.find_element(*WebCTRLPageLocators.GeoTreeHead)
        
        elif(tree=='nettree'):
            self._navigateToNetworkTree()
            time.sleep(3)
            self.switch_to_frame(WebCTRLPageLocators.networkIframe)
            self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)     
            rootNode = self.find_element(*WebCTRLPageLocators.NetTreeHead)
            
            
        tempCount=len(nodeList)-1
        for j in range(len(nodeList)):
           element= self.elementSelection(rootNode,nodeList[j])
           if(j==tempCount):
              time.sleep(2)
              actionChains = ActionChains(self.driver)
              time.sleep(2)                                
              actionChains.context_click(element).perform()
              self.switch_to_default_content()
              try:
                 time.sleep(2)
                 self.switch_to_frame(WebCTRLPageLocators.menuFrame)
                 return self.find_element(*WebCTRLPageLocators.MenuTable)
              except NoSuchElementException:
                self.switch_to_default_content()
                time.sleep(3)
                self.switch_to_frame(WebCTRLPageLocators.networkIframe)
                self.switch_to_frame(WebCTRLPageLocators.navContent_Frame)
                time.sleep(2)
                originalemelemetn=self.driver.find_element_by_xpath("//nobr[text()='"+nodeList[j]+"']")
                time.sleep(2)
                actionChains.context_click(originalemelemetn).perform()
                self.switch_to_default_content()
                self.switch_to_frame(WebCTRLPageLocators.menuFrame)
                return self.find_element(*WebCTRLPageLocators.MenuTable)
                time.sleep(2)
                self.switch_to_default_content()
                time.sleep(1)
                self.switch_to_frame(WebCTRLPageLocators.menuFrame)
                return self.find_element(*WebCTRLPageLocators.MenuTable) 
               
           else:                
             
                self.driver.find_element_by_xpath("//nobr[text()='"+nodeList[j]+"']").click()
                self.imageArrowClick(element)
             
        self.switch_to_default_content()
        
        
        
    def clicking_On_RightMenuTable(self,tree,nodeList,menuOption):
       
        """ 
        Clicks on right menu Table 
  
        Parameters: 
            tree (String): Takes 'geotree', 'nettree'  as arguments
            nodeList(List): List of node arguments
            menuOption(String): menu option text
          
        Returns: 
            nothing 
        """
        self.rightclick_on_Node(tree,nodeList)
        self.driver.find_element_by_xpath("//td[text()='"+menuOption+"']").click()
            
        
        
        
    
    def _acknowledgeAll(self,password, comment):
        """
        Acknowledting all Alarms from advance optiopn
        
        """
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        #self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_xpath("//div[text()='Advanced']"))
        self.click_element(*AlarmsPage.advanced)
        #self.driver.find_element_by_xpath("//div[text()='Advanced']").click()
        self.switch_to_child_window()
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        self.selectActionButton('Acknowledge All')
#         alert=self.driver.switch_to.alert
#         alert.accept()
        self.alert_accept()
        time.sleep(2)
        popups=self.driver.window_handles
        if len(popups)==2:
            print(popups[1].title)
            self.switch_to_child_window()
            if self.driver.title=="Acknowledge All Alarms Reason":
                self.switch_to_frame(WebCTRLPageLocators.actionframe)
                self.send_keys(*WebCTRLPageLocators.securityPassword, value=password, clear_first=True, click_first=True)
                self.send_keys(*WebCTRLPageLocators.commentBox, value=comment, clear_first=True, click_first=True)
                time.sleep(2)
                self.click_element(*WebCTRLPageLocators.okButton)
                
            
        
        self.switch_to_parent_window()
        self.switch_to_default_content()
        
        
        
    def _delete_All_Acknowledged(self):
        """
        Delete all acknowledged alarms
        
        """
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        #self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_xpath("//div[text()='Advanced']"))
        self.click_element(*AlarmsPage.advanced)
        #self.driver.find_element_by_xpath("//div[text()='Advanced']").click()
        self.switch_to_child_window()
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        self.selectActionButton('Delete All Acknowledged')
        alert=self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
#         popups=self.driver.window_handles
#         if len(popups)==2:
#             print(popups[1].title)
#             self.switch_to_child_window()
#             if self.driver.title=="Acknowledge All Alarms Reason":
#                 self.switch_to_frame(WebCTRLPageLocators.actionframe)
#                 self.send_keys(*WebCTRLPageLocators.securityPassword, value=password, clear_first=True, click_first=True)
#                 self.send_keys(*WebCTRLPageLocators.commentBox, value=comment, clear_first=True, click_first=True)
#                 time.sleep(2)
#                 self.click_element(*WebCTRLPageLocators.okButton)
                
            
        
        self.switch_to_parent_window()
        self.switch_to_default_content()
        
        
    def _delete_Closed_Incidents(self):
        """
        Delete all closed incidents 
        
        """
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        
        self.click_element(*AlarmsPage.advanced)
        #self.driver.find_element_by_xpath("//div[text()='Advanced']").click()
        self.switch_to_child_window()
        self.switch_to_frame(WebCTRLPageLocators.actionframe)
        self.selectActionButton('Delete All Acknowledged')
        alert=self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
    
            
        
        self.switch_to_parent_window()
        self.switch_to_default_content()
    
    
    def deleteAll_Alarms(self,password,comment):
        """
        Delete Alarms
        parameters:
            password(String): Enter valid password
            comment(String): Enter valid string in comment box
        """
        self.selectActionButton("Alarms")
        self._acknowledgeAll(password, comment)
        self._delete_All_Acknowledged()
        self._delete_Closed_Incidents()
        
        
    def security_popup(self,password,comment):
        """
        Handles security popup
        parameters:
            password(String): Enter valid password
            comment(String): Enter valid string in comment box
        """
        popups=self.driver.window_handles
        if len(popups)==2:
            print(popups[1].title)
            self.switch_to_child_window()
            print(self.driver.title)
            #if self.driver.title=="Acknowledge Alarm Reason":
            self.switch_to_frame(WebCTRLPageLocators.actionframe)
            self.send_keys(*WebCTRLPageLocators.securityPassword, value=password, clear_first=True, click_first=True)
            self.send_keys(*WebCTRLPageLocators.commentBox, value=comment, clear_first=True, click_first=True)
            time.sleep(2)
            self.click_element(*WebCTRLPageLocators.okButton)
        self.switch_to_parent_window()
        self.switch_to_default_content()
    
    
    
    def _clickingOn_right_MenuTable(self,tree,nodeList,option):
                
        """ 
        It will perform rightclick on element given and returns the child popup
  
        Parameters: 
            Args: 
            nodeList(List): "nodeList" It is an list type, takes nodes name's as params eg: selectNode('GeotTree', ['Zone Applications', 'VAV Terminal ZS', 'OA Temp'])
            tree(String): Takes geotree, and nettree as arguments
            option (String): Node text which you want to select
        Returns: 
            child popup window
        
        """
        menutable=self.rightclick_on_Node(tree, nodeList)
        time.sleep(2)
        
        tableData=menutable.find_elements_by_tag_name('td')
        print(len(tableData))
        for j in range(len(tableData)):
            print(tableData[j].text)
            
            if(tableData[j].text==option):
                tableData[j].click()
                break

        #self.driver.switch_to_default_content()
        #self.switch_to_child_window()
        time.sleep(2)
        return self.driver.window_handles[1]
       
    
    
    