from Lib_space.SELENIUM.Page_locators import pagelocators 
from Lib_space.SELENIUM.BaseClass import Page
import time
'''
Created on Nov 29, 2019
@author: gaddams
'''
class ConfigDesignOps(Page):

    def click_ConfigDesignBtn(self):
        Str = self.find_element(*pagelocators.ACT.configDesignBtn).text
        if(Str == 'Configuration & Design'):
            self.find_element(*pagelocators.ACT.configDesignBtn).click()

    #Change AHU/RTU reference name accordingly based on DB     
    def verifyAddressReferences(self, addRef):
        time.sleep(2) 
        ahuRefLbl = self.find_element(*pagelocators.ACT.ahuRefLbl).text
        if(ahuRefLbl == 'AHU reference'):
            print('AHU reference lable was displayed on screen')
        else:
            print('Wrong/Invalid AHU reference lable is displayed on screen')  
        self.find_element(*pagelocators.ACT.ahuRefParam).clear()  
        self.find_element(*pagelocators.ACT.ahuRefParam).send_keys(addRef)
     
    #Load autoDetect data by clicking on Ok button    
    def loadAutoDetectData(self):
        btnTxt = self.find_element(*pagelocators.ACT.okBtn).text
        if(btnTxt == 'OK'):
            print( btnTxt +'Text displayed')
            self.find_element(*pagelocators.ACT.okBtn).click()
        else:
            print('Wrong OK Button text/No button present')
            
    
    def LoadFileOps(self,loadData):
        self.find_element(*pagelocators.ACT.uploadBtn).click()
        if(self.find_element(*pagelocators.ACT.uploadXBtn)):
            print('X symbol present on pop-up window')           
        if(loadData == 'Load existing file'):
            txt = self.find_element(*pagelocators.ACT.loadExistingFileBtn).text
            if(txt == 'Load existing file'):
                print('\n')
                print( txt + 'button presented on screen')
                self.find_element(*pagelocators.ACT.loadExistingFileBtn).click()  
        elif(loadData == 'Auto-detect devices'):
            time.sleep(2)
            txt1 = self.find_element(*pagelocators.ACT.autoDetectBtn).text
            if(txt1 == loadData):
                print(txt1 + 'button presented on screen')
                self.find_element(*pagelocators.ACT.autoDetectBtn).click()
            '''
            Verify the default device parameters
            ''' 
            damperPosOverrideLbl = self.find_element(*pagelocators.ACT.damperPosOverrideLbl).text
            if(damperPosOverrideLbl == 'Damper position override'):
                print('Damper position override lable was displayed on screen')
            else:
                print('Wrong/Invalid Damper position override lable is displayed on screen')     
            damperPosOverride = self.find_element(*pagelocators.ACT.damperPosOverride).get_attribute('value')
            if(damperPosOverride == '/act_dmp_ov_val'):
                print('Default parameter is displaying for damperPosOverride is' + damperPosOverride)
            else:
                print('Wrong/Invalid parameter is displaying for damperPosOverride') 
                
            time.sleep(2) 
            damperPosOverEnableLable = self.find_element(*pagelocators.ACT.damperPosOverEnablelableLbl).text
            if(damperPosOverEnableLable == 'Damper position override enable'):
                print('Damper position override enable lable was displayed on screen')
            else:
                print('Wrong/Invalid Damper position override enable lable is displayed on screen')    
            damperPosOverEnable = self.find_element(*pagelocators.ACT.damperPosOverEnablelable).get_attribute('value')    
            if(damperPosOverEnable == '/act_dmp_ov_en'):
                print('Default parameter is displaying for damperPosOverrideEnable is' + damperPosOverEnable)
            else:
                print('Wrong/Invalid parameter is displaying for damperPosOverrideEnable') 
                 
            time.sleep(2) 
            rhPosOverrideLbl = self.find_element(*pagelocators.ACT.rhPosOverrideLbl).text
            if(rhPosOverrideLbl == 'RH valve position override'):
                print('Reheat Position override lable was displayed on screen')
            else:
                print('Wrong/Invalid Reheat Valve Position override lable is displayed on screen')    
            rhPosOverrideParam = self.find_element(*pagelocators.ACT.rhPosOverrideParam).get_attribute('value')    
            if(rhPosOverrideParam == '/act_rhv_ov_val'):
                print('Default parameter is displaying for reheat position override is' + rhPosOverrideParam)
            else:
                print('Wrong/Invalid parameter is displaying for reheat position override') 
                
            time.sleep(2) 
            rhPosOverrideEnableLbl = self.find_element(*pagelocators.ACT.rhPosOverEnableLbl).text
            if(rhPosOverrideEnableLbl == 'RH valve position override'):
                print('Reheat position override enable lable was displayed on screen')
            else:
                print('Wrong/Invalid Reheat Valve Position override enable lable is displayed on screen')    
            rhPosOverrideEnableParam = self.find_element(*pagelocators.ACT.rhPosOverEnableParam).get_attribute('value')    
            if(rhPosOverrideEnableParam == '/act_rhv_ov_en'):
                print('Default parameter is displaying for damperPosOverrideEnable is' + rhPosOverrideEnableParam)
            else:
                print('Wrong/Invalid parameter is displaying for damperPosOverrideEnable')
                
            time.sleep(2) 
            damperPosCmdTrndLbl = self.find_element(*pagelocators.ACT.damperPosCmdTrndLbl).text
            if(damperPosCmdTrndLbl == 'Damper position command (Trend)'):
                print('Damper position command (Trend) lable was displayed on screen')
            else:
                print('Wrong/Invalid Damper position command (Trend) lable is displayed on screen')    
            damperPosCmdTrndParam = self.find_element(*pagelocators.ACT.damperPosCmdTrndParam).get_attribute('value')    
            if(damperPosCmdTrndParam == '/act_dmp_cmd_tn'):
                print('Default parameter is displaying for damperPosCmdTrndParam is' + damperPosCmdTrndParam)
            else:
                print('Wrong/Invalid parameter is displaying for damperPosCmdTrndParam') 
                
            time.sleep(2) 
            damperPosFdbkTrnd = self.find_element(*pagelocators.ACT.damperPosFdbkTrnd).text
            if(damperPosFdbkTrnd == 'Damper position feedback (Trend)'):
                print('Damper position feedback (Trend) lable was displayed on screen')
            else:
                print('Wrong/Invalid Damper position feedback (Trend) lable is displayed on screen')    
            damperPosFdbkTrndParam = self.find_element(*pagelocators.ACT.damperPosFdbkTrndParam).get_attribute('value')    
            if(damperPosFdbkTrndParam == '/act_dmp_pos_tn'):
                print('Default parameter is displaying for Damper position feedback (Trend)) is' + damperPosFdbkTrndParam)
            else:
                print('Wrong/Invalid parameter is displaying for VDamper position feedback (Trend)')
            
            time.sleep(2) 
            rhPosCmdTrndLbl = self.find_element(*pagelocators.ACT.rhPosCmdTrndLbl).text
            if(rhPosCmdTrndLbl == 'RH valve position command (Trend)'):
                print('RH valve position command (Trend) lable was displayed on screen')
            else:
                print('Wrong/Invalid RH valve position command (Trend) lable is displayed on screen')    
            rhPosCmdTrndParam = self.find_element(*pagelocators.ACT.rhPosCmdTrndParam).get_attribute('value')    
            if(rhPosCmdTrndParam == '/act_rhv_cmd_tn'):
                print('Default parameter is displaying for RH valve position command (Trend) is' + damperPosCmdTrndParam)
            else:
                print('Wrong/Invalid parameter is displaying for DRH valve position command (Trend)')  
                
            time.sleep(2) 
            vavFlowTrndLbl = self.find_element(*pagelocators.ACT.vavFlowTrndLbl).text
            if(vavFlowTrndLbl == 'VAV flow (Trend)'):
                print('VAV flow (Trend) lable was displayed on screen')
            else:
                print('Wrong/Invalid VAV flow (Trend) lable is displayed on screen')    
            vavFlowTrndParam = self.find_element(*pagelocators.ACT.vavFlowTrndParam).get_attribute('value')    
            if(vavFlowTrndParam == '/act_airflow_tn'):
                print('Default parameter is displaying for VAV flow (Trend) is' + vavFlowTrndParam)
            else:
                print('Wrong/Invalid parameter is displaying for VAV flow (Trend)')    
            
            time.sleep(2) 
            vavDisTempTrndLbl = self.find_element(*pagelocators.ACT.vavDisTempTrndLbl).text
            if(vavDisTempTrndLbl == 'VAV discharge temperature (Trend)'):
                print('VAV discharge temperature (Trend)lable was displayed on screen')
            else:
                print('Wrong/Invalid VAV discharge temperature (Trend) lable is displayed on screen')    
            vavDisTempTrndParam = self.find_element(*pagelocators.ACT.vavDisTempTrndParam).get_attribute('value')    
            if(vavDisTempTrndParam == '/act_vav_dat_tn'):
                print('Default parameter is displaying for VAV discharge temperature (Trend) is' + vavDisTempTrndParam)
            else:
                print('Wrong/Invalid parameter is displaying for VAV discharge temperature (Trend)')
                
            time.sleep(2) 
            ahuSplyTmpTrndLbl = self.find_element(*pagelocators.ACT.ahuSplyTmpTrndLbl).text
            if(ahuSplyTmpTrndLbl == 'AHU supply temperature (Trend)'):
                print('AHU supply temperature (Trend) lable was displayed on screen')
            else:
                print('Wrong/Invalid AHU supply temperature (Trend) lable is displayed on screen')    
            ahusplyTmpTndParam = self.find_element(*pagelocators.ACT.ahusplyTmpTndParam).get_attribute('value')    
            if(ahusplyTmpTndParam == '/act_ahu_sat_tn'):
                print('Default parameter is displaying for AHU supply temperature (Trend) is' + ahusplyTmpTndParam)
            else:
                print('Wrong/Invalid parameter is displaying for AHU supply temperature (Trend)')
            
            time.sleep(2) 
            ahufanStsLbl = self.find_element(*pagelocators.ACT.ahufanStsLbl).text
            if(ahufanStsLbl == 'AHU fan status (Eval)'):
                print('AHU fan status (Eval) lable was displayed on screen')
            else:
                print('Wrong/Invalid AHU fan status (Eval) lable is displayed on screen')    
            ahufanStsParam = self.find_element(*pagelocators.ACT.ahufanStsParam).get_attribute('value')    
            if(ahufanStsParam == '/sf_status'):
                print('Default parameter is displaying for AHU fan status (Eval) is' + ahufanStsParam)
            else:
                print('Wrong/Invalid parameter is displaying for AHU fan status (Eval)')
                
            time.sleep(2) 
            vavMinAirFlowLbl = self.find_element(*pagelocators.ACT.vavMinAirFlowLbl).text
            if(vavMinAirFlowLbl == 'VAV min air flow'):
                print('VAV min air flow lable was displayed on screen')
            else:
                print('Wrong/Invalid VAV min air flow lable is displayed on screen')    
            vavMinAirFlowParam = self.find_element(*pagelocators.ACT.vavMinAirFlowParam).get_attribute('value')    
            if(vavMinAirFlowParam == '/act_min_airflow'):
                print('Default parameter is displaying for AHU fan status (Eval) is' + vavMinAirFlowParam)
            else:
                print('Wrong/Invalid parameter is displaying for AHU fan status (Eval)')
                
            time.sleep(2) 
            vavMaxAirFlowLbl = self.find_element(*pagelocators.ACT.vavMaxAirFlowLbl).text
            if(vavMaxAirFlowLbl == 'VAV max air flow'):
                print('VAV max air flow lable was displayed on screen')
            else:
                print('Wrong/Invalid VAV max air flow lable is displayed on screen')    
            vavMaxAirFlowParam = self.find_element(*pagelocators.ACT.vavMaxAirFlowParam).get_attribute('value')    
            if(vavMaxAirFlowParam == '/act_max_airflow'):
                print('Default parameter is displaying for VAV max air flow is' + vavMaxAirFlowParam)
            else:
                print('Wrong/Invalid parameter is displaying for VAV max air flow')
                
                
            