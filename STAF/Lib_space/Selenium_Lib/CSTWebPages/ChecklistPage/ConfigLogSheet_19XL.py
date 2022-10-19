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


class ConfigLogSheet_19XL(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(ConfigLogSheet_19XL, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  16JB  ##########################################################
        ##########################################################  SET Config table  ##########################################################
        self.M19XL_set_write = ["M119XL_SP_BDL_Val_05", "M119XL_SP_BDL_Desc", "M119XL_SP_LCW_Val_05", "M119XL_SP_LCW_Desc", "M119XL_SP_ECW_Val_05", "M119XL_SP_ECW_Desc", "M119XL_SP_ICEBS_Val_05", "M119XL_SP_ICEBS_Desc",
                                "M119XL_SP_PSIOSVN_Val_21", "M119XL_SP_PSIOSVN_Desc", "M119XL_SP_LIDSVN_Val_21", "M119XL_SP_LIDSVN_Desc", "M119XL_SP_PSIOCIBUS_Val_21", "M119XL_SP_PSIOCIBUS_Desc", "M119XL_SP_PSIOCIADD_Val_21",
                                "M119XL_SP_PSIOCIADD_Desc", "M119XL_SP_ICVCCIBUS_Val_21", "M119XL_SP_ICVCCIBUS_Desc", "M119XL_SP_ICVCCIADD_Val_21", "M119XL_SP_ICVCCIADD_Desc"]

        self.M19XL_ismct_write = ["M19XL_CONFIG_DEGRESET20_Val_05", "M19XL_CONFIG_DEGRESET20_Desc", "M19XL_CONFIG_REMTEMPNO_Val_05", "M19XL_CONFIG_REMTEMPNO_Desc", "M19XL_CONFIG_REMTEMPFULL_Val_05", "M19XL_CONFIG_REMTEMPFULL_Desc",
                                "M19XL_CONFIG_DEGRESET1_Val_05", "M19XL_CONFIG_DEGRESET1_Desc", "M19XL_CONFIG_CHWNO_Val_05", "M19XL_CONFIG_CHWNO_Desc", "M19XL_CONFIG_CHWFULL_Val_05", "M19XL_CONFIG_CHWFULL_Desc",
                                "M19XL_CONFIG_DEGRESET2_Val_05", "M19XL_CONFIG_DEGRESET2_Desc", "M19XL_CONFIG_SERESET_Val_05", "M19XL_CONFIG_SERESET_Desc", "M19XL_CONFIG_ECWCO_Loe", "M19XL_CONFIG_ECWCO_Desc", "M19XL_CONFIG_DEMLIM20_Val_05",
                                "M19XL_CONFIG_DEMLIM20_Desc", "M19XL_CONFIG_20DLO_Loe", "M19XL_CONFIG_20DLO_Desc", "M19XL_CONFIG_ARO_Loe", "M19XL_CONFIG_ARO_Desc", "M19XL_CONFIG_RCO_Loe", "M19XL_CONFIG_RCO_Desc", "M19XL_CONFIG_TEMPPULL_Val_05",
                                "M19XL_CONFIG_TEMPPULL_Desc", "M19XL_CONFIG_LOADPULL_Val_05", "M19XL_CONFIG_LOADPULL_Desc", "M19XL_CONFIG_SELRAMPT_Val_05", "M19XL_CONFIG_SELRAMPT_Desc", "M19XL_CONFIG_LGN_Val_05", "M19XL_CONFIG_LGN_Desc",
                                "M19XL_CONFIG_LDD_Val_05", "M19XL_CONFIG_LDD_Desc", "M19XL_CONFIG_MLT_Val_05", "M19XL_CONFIG_MLT_Desc", "M19XL_CONFIG_CCNSN_Val_05", "M19XL_CONFIG_CCNSN_Desc", "M19XL_CONFIG_CCNBO_Loe", "M19XL_CONFIG_CCNBO_Desc",
                                "M19XL_CONFIG_ICEBO_Loe", "M19XL_CONFIG_ICEBO_Desc", "M19XL_CONFIG_ICEBT_Val_05", "M19XL_CONFIG_ICEBT_Desc", "M19XL_CONFIG_ICEBRO_Loe", "M19XL_CONFIG_ICEBRO_Desc"]

        self.M19XL_leadlag_write = ["M19XL_LEADLAG_LLSEL_Val_05", "M19XL_LEADLAG_LLSEL_Desc", "M19XL_LEADLAG_LBO_Loe", "M19XL_LEADLAG_LBO_Desc", "M19XL_LEADLAG_CSO_Loe", "M19XL_LEADLAG_CSO_Desc", "M19XL_LEADLAG_LAGPC_Val_05",
                                    "M19XL_LEADLAG_LAGPC_Desc", "M19XL_LEADLAG_LAGADD_Val_05", "M19XL_LEADLAG_LAGADD_Desc", "M19XL_LEADLAG_LAGSTATTIM_Val_05", "M19XL_LEADLAG_LAGSTATTIM_Desc", "M19XL_LEADLAG_LAGSTOPTIM_Val_05",
                                    "M19XL_LEADLAG_LAGSTOPTIM_Desc", "M19XL_LEADLAG_PREFT_Val_05", "M19XL_LEADLAG_PREFT_Desc", "M19XL_LEADLAG_STANDCO_Loe", "M19XL_LEADLAG_STANDCO_Desc", "M19XL_LEADLAG_STANDCAP_Val_05",
                                    "M19XL_LEADLAG_STANDCAP_Desc", "M19XL_LEADLAG_STANDADD_Val_05", "M19XL_LEADLAG_STANDADD_Desc"]

        self.M19XL_service1_write = ["M19XL_SERVICE1_MTO_Val_05", "M19XL_SERVICE1_MTO_Desc", "M19XL_SERVICE1_CONDPO_Val_05", "M19XL_SERVICE1_CONDPO_Desc", "M19XL_SERVICE1_REFODT_Val_05", "M19XL_SERVICE1_REFODT_Desc",
                                    "M19XL_SERVICE1_CHILLMED_Val_05", "M19XL_SERVICE1_CHILLMED_Desc", "M19XL_SERVICE1_BRT_Val_05", "M19XL_SERVICE1_BRT_Desc", "M19XL_SERVICE1_CDA_Val_05", "M19XL_SERVICE1_CDA_Desc",
                                    "M19XL_SERVICE1_BTA_Val_05", "M19XL_SERVICE1_BTA_Desc", "M19XL_SERVICE1_WFVT_Val_05", "M19XL_SERVICE1_WFVT_Desc", "M19XL_SERVICE1_OPVT_Val_05", "M19XL_SERVICE1_OPVT_Desc",
                                    "M19XL_SERVICE1_W_BD_Val_05", "M19XL_SERVICE1_W_BD_Desc", "M19XL_SERVICE1_RRDT_Val_05", "M19XL_SERVICE1_RRDT_Desc", "M19XL_SERVICE1_RSDT_Val_05", "M19XL_SERVICE1_RSDT_Desc",
                                    "M19XL_SERVICE1_SURGELIM_Val_05", "M19XL_SERVICE1_SURGELIM_Desc", "M19XL_SERVICE1_SURGEDELT1_Val_05", "M19XL_SERVICE1_SURGEDELT1_Desc", "M19XL_SERVICE1_SURGEDELP1_Val_05",
                                    "M19XL_SERVICE1_SURGEDELP1_Desc", "M19XL_SERVICE1_SURGEDELT2_Val_05", "M19XL_SERVICE1_SURGEDELT2_Desc", "M19XL_SERVICE1_SURGEDELP2_Val_05", "M19XL_SERVICE1_SURGEDELP2_Desc",
                                    "M19XL_SERVICE1_SURGEDEADBAND_Val_05", "M19XL_SERVICE1_SURGEDEADBAND_Desc", "M19XL_SERVICE1_SDPA_Val_05", "M19XL_SERVICE1_SDPA_Desc", "M19XL_SERVICE1_STP_Val_05", "M19XL_SERVICE1_STP_Desc",
                                    "M19XL_SERVICE1_DLSA_Val_05", "M19XL_SERVICE1_DLSA_Desc", "M19XL_SERVICE1_ACF_Val_05", "M19XL_SERVICE1_ACF_Desc", "M19XL_SERVICE1_MRLA_Val_05", "M19XL_SERVICE1_MRLA_Desc",
                                    "M19XL_SERVICE1_MRLV_Val_05", "M19XL_SERVICE1_MRLV_Desc", "M19XL_SERVICE1_MRLKW_Val_05", "M19XL_SERVICE1_MRLKW_Desc", "M19XL_SERVICE1_LINFREQ_Val_05", "M19XL_SERVICE1_LINFREQ_Desc",
                                    "M19XL_SERVICE1_CST_Val_05", "M19XL_SERVICE1_CST_Desc", "M19XL_SERVICE1_CFP_Val_05", "M19XL_SERVICE1_CFP_Desc", "M19XL_SERVICE1_SSAT_Val_05", "M19XL_SERVICE1_SSAT_Desc"]

        self.M19XL_service2_write = ["M19XL_SERVICE2_RESET20_Val_05", "M19XL_SERVICE2_RESET20_Desc", "M19XL_SERVICE2_DEMAND20_Val_05", "M19XL_SERVICE2_DEMAND20_Desc", "M19XL_SERVICE2_CHWSTE_Val_05", "M19XL_SERVICE2_CHWSTE_Desc",
                                    "M19XL_SERVICE2_CHWSTA_Val_05", "M19XL_SERVICE2_CHWSTA_Desc", "M19XL_SERVICE2_CHWRTE_Val_05", "M19XL_SERVICE2_CHWRTE_Desc", "M19XL_SERVICE2_CHWRTA_Val_05", "M19XL_SERVICE2_CHWRTA_Desc",
                                    "M19XL_SERVICE2_RTE_Val_05", "M19XL_SERVICE2_RTE_Desc", "M19XL_SERVICE2_RTA_Val_05", "M19XL_SERVICE2_RTA_Desc", "M19XL_SERVICE2_ST1E_Val_05", "M19XL_SERVICE2_ST1E_Desc", "M19XL_SERVICE2_ST1A_Val_05",
                                    "M19XL_SERVICE2_ST1A_Desc", "M19XL_SERVICE2_ST2E_Val_05", "M19XL_SERVICE2_ST2E_Desc", "M19XL_SERVICE2_ST2A_Val_05", "M19XL_SERVICE2_ST2A_Desc", "M19XL_SERVICE2_ST3E_Val_05", "M19XL_SERVICE2_ST3E_Desc",
                                    "M19XL_SERVICE2_ST3A_Val_05", "M19XL_SERVICE2_ST3A_Desc", "M19XL_SERVICE2_SP1PS_Val_05", "M19XL_SERVICE2_SP1PS_Desc", "M19XL_SERVICE2_SP2PS_Val_05", "M19XL_SERVICE2_SP2PS_Desc", "M19XL_SERVICE2_ST4E_Val_05",
                                    "M19XL_SERVICE2_ST4E_Desc", "M19XL_SERVICE2_ST4A_Val_05", "M19XL_SERVICE2_ST4A_Desc", "M19XL_SERVICE2_ST5E_Val_05", "M19XL_SERVICE2_ST5E_Desc", "M19XL_SERVICE2_ST5A_Val_05", "M19XL_SERVICE2_ST5A_Desc",
                                    "M19XL_SERVICE2_ST6E_Val_05", "M19XL_SERVICE2_ST6E_Desc", "M19XL_SERVICE2_ST6A_Val_05", "M19XL_SERVICE2_ST6A_Desc", "M19XL_SERVICE2_ST7E_Val_05", "M19XL_SERVICE2_ST7E_Desc", "M19XL_SERVICE2_ST7A_Val_05",
                                    "M19XL_SERVICE2_ST7A_Desc", "M19XL_SERVICE2_ST8E_Val_05", "M19XL_SERVICE2_ST8E_Desc", "M19XL_SERVICE2_ST8A_Val_05", "M19XL_SERVICE2_ST8A_Desc", "M19XL_SERVICE2_ST9E_Val_05", "M19XL_SERVICE2_ST9E_Desc",
                                    "M19XL_SERVICE2_ST9A_Val_05", "M19XL_SERVICE2_ST9A_Desc"]

        self.M19XL_service3_write = ["M19XL_SERV3_PIBAND_Val_05", "M19XL_SERV3_PIBAND_Desc", "M19XL_SERV3_PDBAND_Val_05", "M19XL_SERV3_PDBAND_Desc",
                                    "M19XL_SERV3_PEG_Val_05", "M19XL_SERV3_PEG_Desc", "M19XL_SERV3_GVTL_Val_05", "M19XL_SERV3_GVTL_Desc"]

        self.M19XL_brodef_write = ["M19XL_BROD_ACTIVATE_Desc","M19XL_BROD_ACTIVATE_loe","M19XL_BROD_OATCTRLN_Val_05","M19XL_BROD_OATCTRLN_Desc","M19XL_BROD_OATBusN_Desc","M19XL_BROD_OATBusN_Val_05","M19XL_BROD_OATEleN_Val_05",
                                    "M19XL_BROD_OATEleN_Desc","M19XL_BROD_OARHCTRLN_Val_05","M19XL_BROD_OARHCTRLN_Desc","M19XL_BROD_OARHBusN_Desc","M19XL_BROD_OARHBusN_Val_05","M19XL_BROD_OARHEleN_Val_05","M19XL_BROD_OARHEleN_Desc",
                                    "M19XL_BROD_DSSTR_MNT_Val_05","M19XL_BROD_DSSTR_MNT_Desc","M19XL_BROD_DSSTR_DAY_Desc","M19XL_BROD_DSSTR_DAY_Val_05","M19XL_BROD_DSSTRTIME_Val_05","M19XL_BROD_DSSTRTIME_Desc","M19XL_BROD_DSSTR_MIN_Val_05",
                                    "M19XL_BROD_DSSTR_TIME_Desc","M19XL_BROD_DSSTP_MNT_Val_05","M19XL_BROD_DSSTP_MNT_Desc","M19XL_BROD_DSSTP_DAY_Desc","M19XL_BROD_DSSTP_DAY_Val_05","M19XL_BROD_DSSTP_TIME_Val_05","M19XL_BROD_DSSTP_TIME1_Desc",
                                    "M19XL_BROD_DSSTP_MIN_Val_05","M19XL_BROD_DSSTP_TIME2_Desc"]

        self.M19XL_holiday_write = ["M19XL_HOLI_STRT_MNT_Val_05","M19XL_HOLI_STRT_MNT_Desc","M19XL_HOLI_STRT_Day_Val_05",
                                    "M19XL_HOLI_STRT_day_Desc","M19XL_HOLI_DUR_Val_05","M19XL_HOLI_DUR_Desc"]

        self.M19XL_tempctl_write = ["M19XL_TIMESCHD_STSHEET_Loe","M19XL_TIMESCHD_STSHEET_Desc","M19XL_TIMESCHD_OCC1_SUN_CheckBox","M19XL_TIMESCHD_OCC1_SUN_Desc","M19XL_TIMESCHD_OCC1_MON_CheckBox","M19XL_TIMESCHD_OCC1_MON_Desc",
                                    "M19XL_TIMESCHD_OCC1_TUE_CheckBox","M19XL_TIMESCHD_OCC1_TUE_Desc","M19XL_TIMESCHD_OCC1_WED_CheckBox","M19XL_TIMESCHD_OCC1_WED_Desc","M19XL_TIMESCHD_OCC1_THU_CheckBox","M19XL_TIMESCHD_OCC1_THU_Desc",
                                    "M19XL_TIMESCHD_OCC1_FRI_CheckBox","M19XL_TIMESCHD_OCC1_FRI_Desc","M19XL_TIMESCHD_OCC1_SAT_CheckBox","M19XL_TIMESCHD_OCC1_SAT_Desc","M19XL_TIMESCHD_OCC1_HOL_CheckBox","M19XL_TIMESCHD_OCC1_HOL_Desc",
                                    "M19XL_TIMESCHD_OCC1_OCCTIME_Val_05","M19XL_TIMESCHD_OCC1_OCCTIME_Desc","M19XL_TIMESCHD_OCC1_UNOCCTIME_Val_05","M19XL_TIMESCHD_OCC1_UNOCCTIME_Desc","M19XL_TIMESCHD_OCC1_ADDPERIOD_Btn",
                                    "M19XL_TIMESCHD_OCC1_RESET_Btn","M19XL_TIMESCHD_OCC1_MINMISEPERIOD1_Btn"]

    def write_data(self, Data):
        self.prefix = {'set': 'M19XL_set', 'ismct': 'M19XL_ismct', 'service1':'M19XL_service1',
                       'service2':'M19XL_service2', 'service3':'M19XL_service3', 'leadlag': 'M19XL_leadlag',
                       'holiday': 'M19XL_holiday', 'brodef': 'M19XL_brodef'}

        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            if "Val_" in eval("self." + self.prefix[Data['Model']] + "_write[i]") or "val_" in eval(
                    "self." + self.prefix[Data['Model']] + "_write[i]"):
                xpath = eval("ConfigLogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
                self.checklist.write(xpath, Data)
                print(('Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_write[i]") + ' =', \
                    Data['testdata']))

    def read_data(self, Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_write"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "ConfigLogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                if 'Desc' not in ele[-4:] or 'Loe' not in ele[-3:]:
                    value = self.checklist.read(ele, common_xpath, Data, 'read_normal',
                                            page_locators="ConfigLogPageLocators")
                if 'Val_' in ele[-6:]:
                    try:
                        assertion.assertEqual(float(value) == float(
                            ''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]), True)
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
        for ele in eval("self." + self.prefix[Data['Model']] + "_write"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "ConfigLogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal',
                                            page_locators="ConfigLogPageLocators", index_assert=5)
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