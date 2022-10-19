import re
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
sys.path.append(dirnameutils+'\Selenium_Lib')
from Selenium_Lib.BaseClass import Page
from Page_locators.ChecklistPagelocators.RefrigerationLog_locators import ReflogPageLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest
import datetime
import re
driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class RefrigerationLogPage(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(RefrigerationLogPage, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        # 16JB,16JB locators
        self.M16_write = ["M16JB_EVAP_OPER_HRS_Val","M16JB_EVAP_EWT_Val","M16JB_EVAP_LWT_Val",
                          "M16JB_EVAP_RefTemp_Val","M16JB_EVAP_Refpump_Val","M16JB_EVAP_SpGrRef_Val","M16JB_EVAP_CycGrdValv_Val","M16JB_EVAP_CHWPD_Val","M16JB_EVAP_RefrLvlSen_Val","M16JB_EVAP_Usr1_Val","M16JB_EVAP_Usr2_Val","M16JB_ABSORB_CWInTemp_Val","M16JB_ABSORB_CWOutTemp_Val","M16JB_ABSORB_WkLvAbsTemp_Val","M16JB_ABSORB_WkLvAbsSampTemp_Val","M16JB_ABSORB_SpGrWkLvAbsSamp_Val","M16JB_ABSORB_WkLvAbsHiHX2Temp_Val","M16JB_ABSORB_WkLvAbsHiHXTemp_Val","M16JB_ABSORB_WkLvAbsHiHX1Temp_Val","M16JB_ABSORB_SolsprTemp_Val","M16JB_ABSORB_CoolWPD_Val","M16JB_ABSORB_PmpPres_Val","M16JB_ABSORB_SollvlLCD_Val","M16JB_COND_LWT_Val","M16JB_COND_VapCondTemp_Val","M16JB_COND_CWPD_Val","M16JB_COND_Usr3_Val","M16JB_GEN_StrLG1Temp_Val","M16JB_GEN_StrLHX1_Val","M16JB_GEN_StrLG2Temp_Val","M16JB_GEN_StrLHX2_Val","M16JB_GEN_CondTempG2_Val","M16JB_GEN_G1IntPres_Val","M16JB_GEN_StrmPresSupl_Val","M16JB_GEN_StrmPresChil_Val","M16JB_GEN_CapValvPerc_Val","M16JB_ADD_DATA_WkConc_Val","M16JB_ADD_DATA_WkSatTemp_Val","M16JB_ADD_DATA_StrConcG1_Val","M16JB_ADD_DATA_StrConcG2_Val","M16JB_ADD_DATA_AbsLos_Val","M16JB_ADD_DATA_EvapAproch_Val","M16JB_ADD_DATA_AbsAproch_Val","M16JB_ADD_DATA_CondAproch_Val","M16JB_ADD_DATA_CondAproch_Val"]
        # 17DA,17EX,19EX,19DV,19XL,19XR***
        self.M17_write = ["M17DA_Cooler_Pres_Val","M17DA_Cooler_Temp_Val","M17DA_Cooler_ShutLvl_Val","M17DA_Cooler_BrineTempIn_Val","M17DA_Cooler_BrineTempOut_Val","M17DA_Condenser_Pres_Val","M17DA_Condenser_Temp_Val","M17DA_Condenser_WaterTempIn_Val","M17DA_Condenser_WaterTempOut_Val","M17DA_Compressor_DampPos_Val","M17DA_Compressor_OilPresSuply_Val","M17DA_Compressor_OilPressealHous_Val","M17DA_Compressor_OilTempResv_Val","M17DA_Compressor_OilTemplvl_Val","M17DA_Compressor_BearTempThrustEnd_Val","M17DA_Compressor_BearTempSealEnd_Val","M17DA_Gearoil_Press_Val","M17DA_Gearoil_Temp_Val","M17DA_Prime_A_Val","M17DA_Prime_B_Val","M17DA_Prime_C_Val","M17DA_Prime_D_Val"]
        # 19XRD,19RDE,19XRV,19XRPIC5,23XL,32XR
        self.M19_write = ["M19XR_Cooler_Water_PressIn_Val","M19XR_Cooler_Refrig_Press_Val","M19XR_Cooler_Refrig_Press_Val","M19XR_Cooler_Refrig_Temp_Val","M19XR_Cooler_Water_PressOut_Val","M19XR_Cooler_Water_PressGPM_Val","M19XR_Cooler_Water_TempIn_Val","M19XR_Cooler_Water_TempOut_Val","M19XR_Cond_Refrig_Press_Val","M19XR_Cond_Refrig_Temp_Val","M19XR_Cond_Water_PressIn_Val","M19XR_Cond_Water_PressOut_Val","M19XR_Cond_Water_PressGPM_Val","M19XR_Cond_Water_TempIn_Val","M19XR_Cond_Water_TempOut_Val","M19XR_Compressor_BearingTemp_Val","M19XR_Compressor_OilPressDiff_Val","M19XR_Compressor_OilTempResv_Val","M19XR_Compressor_Oillvl_Val","M19XR_Compressor_MotorFLA_Val","M19XR_Compressor_MotorAmp_Val"]
        #23xl
        self.M23XL_write=["M19XR_Cooler_Water_PressIn_Val", "M19XR_Cooler_Refrig_Press_Val",
         "M19XR_Cooler_Refrig_Temp_Val", "M19XR_Cooler_Water_PressOut_Val", "M19XR_Cooler_Water_PressGPM_Val",
         "M19XR_Cooler_Water_TempIn_Val", "M19XR_Cooler_Water_TempOut_Val", "M19XR_Cond_Refrig_Press_Val",
         "M19XR_Cond_Refrig_Temp_Val", "M19XR_Cond_Water_PressIn_Val", "M19XR_Cond_Water_PressOut_Val",
         "M19XR_Cond_Water_PressGPM_Val", "M19XR_Cond_Water_TempIn_Val", "M19XR_Cond_Water_TempOut_Val",
         "M19XR_Compressor_BearingTemp_Val", "M19XR_Compressor_OilPressDiff_Val", "M19XR_Compressor_OilTempResv_Val",
         "M19XR_Compressor_Oillvl_Val","M19XR_Compressor_Oillvl23_Val","M19XR_Compressor_MotorFLA_Val",
         "M19XR_Compressor_MotorAmp_Val"]

        # 23XRv
        self.M23_write = ["M23XRV_Cooler_Refrig_Press_Val","M23XRV_Cooler_Refrig_Temp_Val","M23XRV_Cooler_Water_PressIn_Val","M23XRV_Cooler_Water_PressOut_Val","M23XRV_Cooler_Water_PressGPM_Val","M23XRV_Cooler_Water_TempIn_Val","M23XRV_Cooler_Water_TempOut_Val","M23XRV_Cond_Refrig_Press_Val","M23XRV_Cond_Refrig_Temp_Val","M23XRV_Cond_Water_PressIn_Val","M23XRV_Cond_Water_PressOut_Val","M23XRV_Cond_Water_PressGPM_Val","M23XRV_Cond_Water_TempIn_Val","M23XRV_Cond_Water_TempOut_Val","M23XRV_Concen_ReclaimDelta_Val","M23XRV_Concen_OilReclaimOP_Val","M23XRV_Concen_Oillvl_Val","M23XRV_Compressor_ReoilPresDeltaP_Val","M23XRV_Compressor_oilsumpTemp_Val","M23XRV_Compressor_CompDischTemp_Val","M23XRV_VFD_avgCurrent_Val","M23XRV_VFD_avgVolt_Val","M23XRV_VFD_lineKW_Val","M23XRV_VFD_avgLoadCurrent_Val","M23XRV_VFD_InvTemp_Val","M23XRV_VFD_RectifTemp_Val","M23XRV_VFD_CoolantFlw_Val"]
        # 30HX,30MP,30RAP,30RB,30XAXW,30XV,30XA
        self.M30_write = ["M30HX_CirA_btn","M30HX_CirA_OperHrs_Val","M30HX_CirA_Starts_Val","M30HX_CirA_Capacity_Val",
                          "M30HX_CirA_DischargePres_Val","M30HX_CirA_SatCondTemp_Val","M30HX_CirA_SuctTemp_Val",
                          "M30HX_CirA_SuperHeat_Val","M30HX_CirA_ChwDeltaP_Val","M30HX_CirA_Sst_Val",
                          "M30HX_CirA_OilPress_Val","M30HX_CirA_EXV_Val","M30HX_CirA_WaterIn_Val",
                          "M30HX_CirA_WaterOut_Val","M30HX_CirA_EconPress_Val","M30HX_CirA_IntFD_Val",
                          "M30HX_CirA_SGT_Val","M30HX_CirA_Usr1_val","M30HX_CirA_Usr2_val","M30HX_CirA_Usr3_val",
                          "M30HX_CirA_Usr4_val","M30HX_CirA_Comp1MotorAmpL1_Val","M30HX_CirA_Comp1MotorAmpL2_Val",
                          "M30HX_CirA_Comp1MotorAmpL3_Val","M30HX_CirA_Comp1MotorAmpL4_Val",
                          "M30HX_CirA_Comp2MotorAmpL1_Val","M30HX_CirA_Comp2MotorAmpL2_Val",
                          "M30HX_CirA_Comp2MotorAmpL3_Val","M30HX_CirA_Comp2MotorAmpL4_Val",
                          "M30HX_CirA_Comp3MotorAmpL1_Val","M30HX_CirA_Comp3MotorAmpL2_Val",
                          "M30HX_CirA_Comp3MotorAmpL3_Val","M30HX_CirA_Comp3MotorAmpL4_Val",
                          "M30HX_CirA_Comp4MotorAmpL1_Val","M30HX_CirA_Comp4MotorAmpL2_Val",
                          "M30HX_CirA_Comp4MotorAmpL3_Val","M30HX_CirA_Comp4MotorAmpL4_Val",
                          "M30HX_CirA_PMChecklistChkpump_val","M30HX_CirA_PMChecklistChkStrn_val",
                          "M30HX_CirA_PMChecklistChkCondCoil_val","M30HX_CirA_PMChecklistChkVSD_val",
                          "M30HX_CirA_PMChecklistChkCondFan_val","M30HX_CirA_PMChecklistChkSetpnt_val",
                          "M30HX_CirA_PMChecklistChkRefType_val","M30HX_CirB_btn","M30HX_CirB_OperHrs_Val",   "M30HX_CirB_Starts_Val",
                          "M30HX_CirB_Capacity_Val","M30HX_CirB_DischargePres_Val","M30HX_CirB_SatCondTemp_Val",
                          "M30HX_CirB_SuctTemp_Val","M30HX_CirB_SuperHeat_Val","M30HX_CirB_ChwDeltaP_Val",
                          "M30HX_CirB_Sst_Val","M30HX_CirB_OilPress_Val","M30HX_CirB_EXV_Val",
                          "M30HX_CirB_WaterIn_Val","M30HX_CirB_WaterOut_Val","M30HX_CirB_EconPress_Val",
                          "M30HX_CirB_IntFD_Val","M30HX_CirB_SGT_Val","M30HX_CirB_Usr1_val","M30HX_CirB_Usr2_val",
                          "M30HX_CirB_Usr3_val","M30HX_CirB_Usr4_val","M30HX_CirB_Comp1MotorAmpL1_Val",
                          "M30HX_CirB_Comp1MotorAmpL2_Val","M30HX_CirB_Comp1MotorAmpL3_Val",
                          "M30HX_CirB_Comp1MotorAmpL4_Val","M30HX_CirB_Comp2MotorAmpL1_Val",
                          "M30HX_CirB_Comp2MotorAmpL2_Val","M30HX_CirB_Comp2MotorAmpL3_Val",
                          "M30HX_CirB_Comp2MotorAmpL4_Val","M30HX_CirB_Comp3MotorAmpL1_Val",
                          "M30HX_CirB_Comp3MotorAmpL2_Val","M30HX_CirB_Comp3MotorAmpL3_Val",
                          "M30HX_CirB_Comp3MotorAmpL4_Val","M30HX_CirB_Comp4MotorAmpL1_Val",
                          "M30HX_CirB_Comp4MotorAmpL2_Val","M30HX_CirB_Comp4MotorAmpL3_Val",
                          "M30HX_CirB_Comp4MotorAmpL4_Val","M30HX_CirB_PMChecklistChkpump_val",
                          "M30HX_CirB_PMChecklistChkStrn_val","M30HX_CirB_PMChecklistChkCondCoil_val",
                          "M30HX_CirB_PMChecklistChkVSD_val","M30HX_CirB_PMChecklistChkCondFan_val",
                          "M30HX_CirB_PMChecklistChkSetpnt_val","M30HX_CirB_PMChecklistChkRefType_val","M30HX_CirC_btn",
                          "M30HX_CirC_OperHrs_Val","M30HX_CirC_Starts_Val","M30HX_CirC_Capacity_Val","M30HX_CirC_DischargePres_Val","M30HX_CirC_SatCondTemp_Val","M30HX_CirC_SuctTemp_Val","M30HX_CirC_SuperHeat_Val","M30HX_CirC_ChwDeltaP_Val","M30HX_CirC_Sst_Val","M30HX_CirC_OilPress_Val","M30HX_CirC_EXV_Val","M30HX_CirC_WaterIn_Val","M30HX_CirC_WaterOut_Val","M30HX_CirC_EconPress_Val","M30HX_CirC_IntFD_Val","M30HX_CirC_SGT_Val","M30HX_CirC_Usr1_val","M30HX_CirC_Usr2_val","M30HX_CirC_Usr3_val","M30HX_CirC_Usr4_val","M30HX_CirC_Comp1MotorAmpL1_Val","M30HX_CirC_Comp1MotorAmpL2_Val","M30HX_CirC_Comp1MotorAmpL3_Val","M30HX_CirC_Comp1MotorAmpL4_Val","M30HX_CirC_Comp2MotorAmpL1_Val","M30HX_CirC_Comp2MotorAmpL2_Val","M30HX_CirC_Comp2MotorAmpL3_Val","M30HX_CirC_Comp2MotorAmpL4_Val","M30HX_CirC_Comp3MotorAmpL1_Val","M30HX_CirC_Comp3MotorAmpL2_Val","M30HX_CirC_Comp3MotorAmpL3_Val","M30HX_CirC_Comp3MotorAmpL4_Val","M30HX_CirC_Comp4MotorAmpL1_Val","M30HX_CirC_Comp4MotorAmpL2_Val","M30HX_CirC_Comp4MotorAmpL3_Val","M30HX_CirC_Comp4MotorAmpL4_Val","M30HX_CirC_PMChecklistChkpump_val","M30HX_CirC_PMChecklistChkStrn_val","M30HX_CirC_PMChecklistChkCondCoil_val","M30HX_CirC_PMChecklistChkVSD_val","M30HX_CirC_PMChecklistChkCondFan_val","M30HX_CirC_PMChecklistChkSetpnt_val","M30HX_CirC_PMChecklistChkRefType_val"]
        # ***30XW, 30XWV,30MP
        self.M30X_write = ["M30XW_percCapacperCirA_Val","M30XW_percCapacperCirB_Val","M30XW_coolerRef_suctPressA_Val","M30XW_coolerRef_suctTempA_Val","M30XW_coolerRef_EconPressA_Val","M30XW_coolerRef_EXVA_Val","M30XW_coolerRef_SuctPressB_Val","M30XW_coolerRef_SatSuctTempB_Val","M30XW_coolerRef_EconPressB_Val","M30XW_coolerRef_EXVB_Val","M30XW_coolerWaterPressIn_Val","M30XW_coolerWaterPressOut_Val","M30XW_coolerWaterTempIn_Val","M30XW_coolerWaterTempOut_Val","M30XW_CondRef_DiscPressA_Val","M30XW_CondRef_SatCondTempA_Val","M30XW_CondRef_DiscPressB_Val","M30XW_CondRef_SatCondTempB_Val","M30XW_CondWater_PressIn_Val","M30XW_CondWater_PressOut_Val","M30XW_CondWater_TempOut_Val","M30XW_CondWater_TempIn_Val","M30XW_CondWater_OAT_Val","M30XW_CompA1_DischGasTemp_Val","M30XW_CompA1_oilpressDiff_Val","M30XW_CompA1_oilpress_Val","M30XW_CompA1_MotorTemp_Val","M30XW_CompA2_DischGasTemp_Val","M30XW_CompA2_oilpressDiff_Val","M30XW_CompA2_oilpress_Val","M30XW_CompA2_MotorTemp_Val","M30XW_CompB1_DischGasTemp_Val","M30XW_CompB1_oilpressDiff_Val","M30XW_CompB1_oilpress_Val","M30XW_CompB1_MotorTemp_Val","M30XW_CompB2_DischGasTemp_Val","M30XW_CompB2_oilpressDiff_Val","M30XW_CompB2_oilpress_Val","M30XW_CompB2_MotorTemp_Val"]

    def write_data(self, Data):
        self.prefix = {'16JB': 'M16', '16JT': 'M16', '17DA': 'M17', '17EX': 'M19', '19EX': 'M19', '19XL': 'M19',
                       '19XR': 'M19', '19XRV': 'M19', '19XRE': 'M19', '19XRD': 'M19', '19XRPIC5': 'M19',
                       '19PIC6': 'M19', '23XRV': 'M23', '23XL': 'M23XL', '30XA': 'M30', '30HX': 'M30', '30MP': 'M30X',
                       '30RAP': 'M30', '30RB': 'M30', '30XAXW': 'M30', '30XV': 'M30', '30XW': 'M30X', '30XWV': 'M30X',
                       '32XR': 'M19'}
      #   if 'M30' == self.prefix[Data['Model']]:
      #       self.find_element(*ReflogPageLocators.M30HX_CirA_btn).click()
      #       time.sleep(0.5)
      #       self.find_element(*ReflogPageLocators.M30HX_CirB_btn).click()
      #       time.sleep(0.5)
      #       self.find_element(*ReflogPageLocators.M30HX_CirC_btn).click()
      #       time.sleep(0.5)
        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            xpath = eval("ReflogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
            if '_Val' in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                self.checklist.write(xpath, Data)
                print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'Written data of ' + eval("self." +
                                                                                                   self.prefix[Data['Model']] + "_write[i]") + ' =', \
                    Data['testdata'])
            elif '_val' in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                self.checklist.write(xpath, Data)
                print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'Written data of ' + eval("self." +
                                                                                                   self.prefix[Data['Model']] + "_write[i]") + ' =', \
                    Data['testdata'])
            elif '_btn' in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                self.checklist.click(eval("self." + self.prefix[Data['Model']] + "_write[i]"), "ReflogPageLocators")
                print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Selected ' + eval("self."
                                                                                                   +self.prefix[\
                          Data['Model']] + "_write[i]"))


    def create_log(self):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Creating new log file")
        self.driver.maximize_window()
        self.wait_unit_visible(ReflogPageLocators.add_log_btn)
        self.find_element(*ReflogPageLocators.add_log_btn).click()
        self.driver.set_window_size('1024','768')
        self.wait_until_element(ReflogPageLocators.form_title)
        self.driver.maximize_window()
        self.driver.set_window_size('1024', '768')

    def edit_log(self,logid):
        self.driver.maximize_window()
        path = (ReflogPageLocators.del_log[-1])[:-9] + str(logid) + ']/div[4]/ul[1]/li[1]/a/i'
        self.find_element('xpath', path).click()
        self.driver.set_window_size('1024', '768')
        time.sleep(1.0)
        self.driver.maximize_window()
        self.driver.set_window_size('1024', '768')
        self.wait_until_element(ReflogPageLocators.form_title)

    def del_log(self, logid):
        path = (ReflogPageLocators.del_log[-1])[:-9] + str(logid) + ']/div[4]/ul[1]/li[2]/a/i'
        self.find_element('xpath',path).click()
    def reset_data(self):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," Resetting Ref Log data")
        self.wait_until_element(ReflogPageLocators.log_reset)
        self.find_element(*ReflogPageLocators.log_reset).click()

    def read_data(self, Data,reset ='none'):
        self.wait_until_element(eval("ReflogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]")))
        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            if '_btn' not in eval("self." + self.prefix[Data['Model']] + "_write[i]"):

                read_value = ''
                xpath = ((eval("ReflogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[i]")))[-1])[
                        :-5]+'a'
                read_value=self.find_element('xpath',xpath).get_attribute('text')
                print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'read data of ' + eval( \
                    "self." + \
                    self.prefix[
                        Data['Model']] + "_write[i]") + ' =', read_value)
                if(reset=='none'):
                    if '_val' in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                        assertion.assertEqual(read_value == str(Data['testdata']), True)
                    elif '_Val' in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                        assertion.assertEqual(read_value == '{0:.2f}'.format(float(re.sub("[^0123456789\.]", "",
                                                                                          str(Data['testdata'])[:8]))), True)
                else:
                    assertion.assertEqual(read_value == '', True)
                time.sleep(1)

    def reflog_form_cancel(self):
        self.find_element(*ReflogPageLocators.form_cancel).click()

    def reflog_form_reset(self):
        self.find_element(*ReflogPageLocators.log_reset).click()

    def reflog_form_exit(self):
        self.find_element(*ReflogPageLocators.form_exit).click()

    def ref_log_save(self):
        self.find_element(*ReflogPageLocators.log_save).click()
        time.sleep(1.0)

    def reflog_log_cancel(self):
        self.find_element(*ReflogPageLocators.log_cancel).click()

    def reflog_log_exit(self):
        self.find_element(*ReflogPageLocators.log_exit).click()

    def wait_until_element(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element[-1])))
        except TimeoutException:
            print("Loading took too much time!")

    def wait_unit_visible(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, element[-1])))
        except TimeoutException:
            print("Loading took too much time!")