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
from Page_locators.ChecklistPagelocators.PrestartPage_locators import PreStartPageLocators
from Page_locators.ChecklistPagelocators.ConfigLog_locators import ConfigLogPageLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class ConfigLogSheet_16JT(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(ConfigLogSheet_16JT, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  16JT  ##########################################################
        ##########################################################  SET Config table  ##########################################################
        self.M16JT_set_write = ["M16JT_SPT_COOLSP_Val_05", "M16JT_SPT_COOLSP_Desc", "M16JT_SPT_PC6400_val_20", "M16JT_SPT_PC6400_Desc", "M16JT_SPT_LIDSOFT_val_20", "M16JT_SPT_LIDSOFT_Desc", "M16JT_SPT_PC6400BUS_val_20",
                                "M16JT_SPT_PC6400BUS_Desc", "M16JT_SPT_PC6400ADD_val_20", "M16JT_SPT_PC6400ADD_Desc", "M16JT_SPT_LIDBUS_val_20", "M16JT_SPT_LIDBUS_Desc", "M16JT_SPT_LIDADD_val_20", "M16JT_SPT_LIDADD_Desc"]

        ##########################################################  PIC Config table  ##########################################################
        self.M16JT_pic_write = ["M16JT_CONFIG_DEGRESET20_Val_05", "M16JT_CONFIG_DEGRESET20_Desc", "M16JT_CONFIG_REMTEMPNO_Val_05", "M16JT_CONFIG_REMTEMPNO_Desc", "M16JT_CONFIG_REMTEMPFULL_Val_05", "M16JT_CONFIG_REMTEMPFULL_Desc",
                                "M16JT_CONFIG_DEGRESET1_Val_05", "M16JT_CONFIG_DEGRESET1_Desc", "M16JT_CONFIG_CHWNO_Val_05", "M16JT_CONFIG_CHWNO_Desc", "M16JT_CONFIG_CHWFULL_Val_05", "M16JT_CONFIG_CHWFULL_Desc",
                                "M16JT_CONFIG_DEGRESET2_Val_05", "M16JT_CONFIG_DEGRESET2_Desc", "M16JT_CONFIG_SERESET_Val_05", "M16JT_CONFIG_SERESET_Desc", "M16JT_CONFIG_CHWINOPT_drop", "M16JT_CONFIG_CHWINOPT_Desc",
                                "M16JT_CONFIG_REMOTEOPT_drop", "M16JT_CONFIG_REMOTEOPT_Desc", "M16JT_CONFIG_TEMPPULL_Val_05", "M16JT_CONFIG_TEMPPULL_Desc", "M16JT_CONFIG_CCNOCCNUM_Val_05", "M16JT_CONFIG_CCNOCCNUM_Desc",
                                "M16JT_CONFIG_CCNOCCOPT_drop", "M16JT_CONFIG_CCNOCCOPT_Desc"]

        ##########################################################  PIC SERVICE1 Config table  ##########################################################
        self.M16JT_ser1_write = ["M16JT_SERV1_REFTP_Val_05", "M16JT_SERV1_REFTP_Desc", "M16JT_SERV1_REFOD_Val_05", "M16JT_SERV1_REFOD_Desc", "M16JT_SERV1_WFVT_Val_05", "M16JT_SERV1_WFVT_Desc",
                                "M16JT_SERV1_REFRD_Val_05", "M16JT_SERV1_REFRD_Desc", "M16JT_SERV1_REFSD_Val_05", "M16JT_SERV1_REFSD_Desc", "M16JT_SERV1_SAMRAN_Val_05", "M16JT_SERV1_SAMRAN_Desc",
                                "M16JT_SERV1_WLLAA_Val_05", "M16JT_SERV1_WLLAA_Desc", "M16JT_SERV1_VAPCO_Val_05", "M16JT_SERV1_VAPCO_Desc", "M16JT_SERV1_GENSO_Val_05", "M16JT_SERV1_GENSO_Desc",
                                "M16JT_SERV1_GENOA_Val_05", "M16JT_SERV1_GENOA_Desc", "M16JT_SERV1_DESTIME_Val_05", "M16JT_SERV1_DESTIME_Desc", "M16JT_SERV1_CONLOWLevel_Val_05", "M16JT_SERV1_CONLOWLevel_Desc",
                                "M16JT_SERV1_VOLLOWLevel_Val_05", "M16JT_SERV1_VOLLOWLevel_Desc", "M16JT_SERV1_CONHIGHLevel_Val_05", "M16JT_SERV1_CONHIGHLevel_Desc", "M16JT_SERV1_VOLHIGHLevel_Val_05",
                                "M16JT_SERV1_VOLHIGHLevel_Desc", "M16JT_SERV1_CGLA_Val_05", "M16JT_SERV1_CGLA_Desc", "M16JT_SERV1_LFS_Val_05", "M16JT_SERV1_LFS_Desc"]

        ##########################################################  PIC SERVICE2 Config table  ##########################################################
        self.M16JT_ser2_write = ["M16JT_SERV2_CHWSTE_Val_05", "M16JT_SERV2_CHWSTE_Desc", "M16JT_SERV2_CHWSTA_Val_05", "M16JT_SERV2_CHWSTA_Desc", "M16JT_SERV2_CHWRTE_Val_05", "M16JT_SERV2_CHWRTE_Desc",
                                "M16JT_SERV2_CHWRTA_Val_05", "M16JT_SERV2_CHWRTA_Desc", "M16JT_SERV2_RTE_Val_05", "M16JT_SERV2_RTE_Desc", "M16JT_SERV2_RTA_Val_05", "M16JT_SERV2_RTA_Desc"]

        ##########################################################  PIC SERVICE3 Config table  ##########################################################
        self.M16JT_ser3_write = ["M16JT_SERV3_CPDEAD_Val_05", "M16JT_SERV3_CPDEAD_Desc", "M16JT_SERV3_PIBAND_Val_05", "M16JT_SERV3_PIBAND_Desc", "M16JT_SERV3_PDBAND_Val_05", "M16JT_SERV3_PDBAND_Desc",
                                "M16JT_SERV3_PROPGAIN_Val_05", "M16JT_SERV3_PROPGAIN_Desc", "M16JT_SERV3_GENSTB_Val_05", "M16JT_SERV3_GENSTB_Desc", "M16JT_SERV3_WARTL_Val_05", "M16JT_SERV3_WARTL_Desc",
                                "M16JT_SERV3_RUNTL_Val_05", "M16JT_SERV3_RUNTL_Desc", "M16JT_SERV3_LINVT_Loe_drop", "M16JT_SERV3_LINVT_Desc", "M16JT_SERV3_PNEVT_Loe_drop", "M16JT_SERV3_PNEVT_Desc",
                                "M16JT_SERV3_ONTIME_Val_05", "M16JT_SERV3_ONTIME_Desc", "M16JT_SERV3_STARTS_Val_05", "M16JT_SERV3_STARTS_Desc"]

        ##########################################################  BROADCAST Config table  ##########################################################
        self.M16JT_broad_write = ["M16JT_BROAD_TIMEBE_Loe_drop", "M16JT_BROAD_TIMEBE_Desc", "M16JT_BROAD_STATMONT_Val_05", "M16JT_BROAD_STATMONT_Desc", "M16JT_BROAD_STATDAYWEK_Val_05", "M16JT_BROAD_STATDAYWEK_Desc",
                                    "M16JT_BROAD_STATTIME_Val_05", "M16JT_BROAD_STATTIME_Desc", "M16JT_BROAD_STATADV_Val_05", "M16JT_BROAD_STATADV_Desc", "M16JT_BROAD_STOPMONT_Val_05", "M16JT_BROAD_STOPMONT_Desc",
                                    "M16JT_BROAD_STOPDAYWEK_Val_05", "M16JT_BROAD_STOPDAYWEK_Desc", "M16JT_BROAD_STOPTIME_Val_05", "M16JT_BROAD_STOPTIME_Desc", "M16JT_BROAD_STOPBAC_Val_05", "M16JT_BROAD_STOPBAC_Desc"]

        ##########################################################  HOILDAY Config table  ##########################################################
        self.M16JT_holiday_write = ["M16JT_HOLDAY_HOLSM_Val_05", "M16JT_HOLDAY_HOLSM_Desc", "M16JT_HOLDAY_STATDAY_Val_05", "M16JT_HOLDAY_STATDAY_Desc", "M16JT_HOLDAY_DURATION_Val_05", "M16JT_HOLDAY_DURATION_Desc"]

        ##########################################################  Time Schedule Config table  ##########################################################
        self.M16JT_timeschd_write = ["M16JT_TIMESCHD_SELTSHEET_Loe_drop", "M16JT_TIMESCHD_SELTSHEET_Desc", "M16JT_TIMESCHD_OCC1_SUN_CheckBox", "M16JT_TIMESCHD_OCC1_SUN_Desc", "M16JT_TIMESCHD_OCC1_MON_CheckBox", "M16JT_TIMESCHD_OCC1_MON_Desc",
                                        "M16JT_TIMESCHD_OCC1_TUE_CheckBox", "M16JT_TIMESCHD_OCC1_TUE_Desc", "M16JT_TIMESCHD_OCC1_WED_CheckBox", "M16JT_TIMESCHD_OCC1_WED_Desc", "M16JT_TIMESCHD_OCC1_THU_CheckBox", "M16JT_TIMESCHD_OCC1_THU_Desc",
                                        "M16JT_TIMESCHD_OCC1_FRI_CheckBox", "M16JT_TIMESCHD_OCC1_FRI_Desc", "M16JT_TIMESCHD_OCC1_SAT_CheckBox", "M16JT_TIMESCHD_OCC1_SAT_Desc", "M16JT_TIMESCHD_OCC1_HOL_CheckBox", "M16JT_TIMESCHD_OCC1_HOL_Desc",
                                        "M16JT_TIMESCHD_OCC1_OCCTIME_Val_time ", "M16JT_TIMESCHD_OCC1_OCCTIME_Desc", "M16JT_TIMESCHD_OCC1_UNOCCTIME_Val_time", "M16JT_TIMESCHD_OCC1_UNOCCTIME_Desc", "M16JT_TIMESCHD_OCC1_ADDPERIOD_Btn",
                                        "M16JT_TIMESCHD_OCC1_RESET_Btn", "M16JT_TIMESCHD_OCC1_MINMISEPERIOD1_Btn"]

    def write_data(self, Data):
        self.prefix = {'set_point': 'M16JT_set', 'pic': 'M16JT_pic', 'service1': 'M16JT_ser1', 'service2': 'M16JT_ser2', 'service3': 'M16JT_ser3', 'broadcast': 'M16JT_broad',
                       'holiday': 'M16JT_holiday', 'time_schedule': 'M16JT_timeschd'}

        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            if "Val_" in eval("self." + self.prefix[Data['Model']] + "_write[i]") or "val_" in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                xpath = eval("ConfigLogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
                self.checklist.write(xpath, Data)
                print(('Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_write[i]") + ' =', \
                Data['testdata']))

    def read_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("ConfigLogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="ConfigLogPageLocators")
                if 'Val_' in ele[-6:]:
                    try:
                        assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]), True)
                        print(('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value))
                    except Exception as e:
                        print("********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        print((e.message))
                        print(('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value))
                elif 'val_' in ele[-6:]:
                    try:
                        assertion.assertEqual(value == str(Data['testdata'][:eval(ele[-2:])]), True)
                        print(('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value))
                    except Exception as e:
                        print("********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        print((e.message))
                        print(('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value))
                elif 'drop' in ele[-4:]:
                    pass
                elif 'Desc' in ele[-4:]:
                    pass
                elif 'Val' in ele[-3:]:
                    assertion.assertEqual(value == str(Data['testdata'][:eval(ele[-2:])]), True)
                elif 'CheckBox' in ele[-8:]:
                    pass
                elif 'time' in ele[-4:]:
                    pass
                elif 'Btn' in ele[-3:]:
                    pass

    def read_reset_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("ConfigLogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="ConfigLogPageLocators", index_assert=5)
                if 'drop' in ele[-4:]:
                    pass
                elif 'CheckBox' in ele[-8:]:
                    pass
                elif 'Val_' in ele[-6:] or 'val_' in ele[-6:]:
                    try:
                        assertion.assertEqual(value == '', True)
                    except Exception as e:
                        print("********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        print((e.message))

                print(('Read Chiller Name Plate Data Information of ' + ele + ' = ', 'Null' if value == '' else value))

    def configlog_exit(self):
        self.find_element(*ConfigLogPageLocators.configlog_exit).click()

    def configlog_save_submenu(self):
        self.find_element(*ConfigLogPageLocators.configlog_savesubmenu).click()

    def configlog_save_mainmenu(self):
        self.find_element(*ConfigLogPageLocators.configlog_savemainmenu).click()

    def configlog_save(self):
        self.find_element(*ConfigLogPageLocators.configlog_save).click()

    def configlog_cancel(self):
        self.find_element(*ConfigLogPageLocators.configlog_cancel).click()

    def startup_form_cancle(self):
        self.find_element(*ChecklistPageLocators.startup_page_cancel).click()

    def startup_form_reset(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()

    def startup_form_exit(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()

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