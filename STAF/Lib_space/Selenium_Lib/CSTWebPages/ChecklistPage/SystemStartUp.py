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
from Page_locators.ChecklistPagelocators.SystemStartUp_locators import SystemStartupLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class SystemStartUp(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(SystemStartUp, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        """Post Start Page locators"""
        ##########################################################  38AP  ##########################################################
        self.M38AP_prestart_check_write = []

        self.M38AP_prestart_check_swrite = ["M38AP_prestart_check_Default", "M38AP_prestart_check_trans1_05", "M38AP_prestart_check_trans2_05", "M38AP_prestart_check_imbalanceAB_05", "M38AP_prestart_check_imbalanceAC_05",
                                            "M38AP_prestart_check_imbalanceBC_05", "M38AP_prestart_check_imbalance_max_divi_05", "M38AP_prestart_check_imbalance_05"]

        self.M38AP_prestart_check_tog = ["M38AP_prestart_check_valves_open_yes", "M38AP_prestart_check_valves_open_no", "M38AP_prestart_check_oil_level_yes", "M38AP_prestart_check_oil_level_no",
                                        "M38AP_prestart_check_mounting_bolt_yes", "M38AP_prestart_check_mounting_bolt_no", "M38AP_prestart_check_nameplate_yes", "M38AP_prestart_check_nameplate_no",
                                        "M38AP_prestart_check_trans_primary_yes", "M38AP_prestart_check_trans_primary_no", "M38AP_prestart_check_imbalance_yes", "M38AP_prestart_check_imbalance_no",
                                        "M38AP_prestart_check_fan_switch_yes", "M38AP_prestart_check_fan_switch_no", "M38AP_prestart_check_con_rotation_yes", "M38AP_prestart_check_con_rotation_no",
                                        "M38AP_prestart_check_evap_rotation_yes", "M38AP_prestart_check_evap_rotation_no", "M38AP_prestart_check_date_set_yes", "M38AP_prestart_check_date_set_no",
                                        "M38AP_prestart_check_software_ver_yes", "M38AP_prestart_check_software_ver_no"]

        self.M38AP_software_version_info_swrite = []

        self.M38AP_software_version_info_tog = []

        self.M38AP_software_version_info_write = ["M38AP_software_version_info_mbb_20", "M38AP_software_version_info_mbb_cesr_20", "M38AP_software_version_info_aux_20", "M38AP_software_version_info_aux_cesr_20", "M38AP_software_version_info_cxb_20",
                                        "M38AP_software_version_info_cxb_cesr_20", "M38AP_software_version_info_emm1_20", "M38AP_software_version_info_emm1_cesr_20", "M38AP_software_version_info_emm2_20", "M38AP_software_version_info_emm2_cesr_20",
                                        "M38AP_software_version_info_navi_20", "M38AP_software_version_info_navi_cesr_20"]

        self.M38AP_start_operate_swrite = []

        self.M38AP_start_operate_tog = ["M38AP_start_operate_comp_test_yes", "M38AP_start_operate_comp_test_no", "M38AP_start_operate_ref_oil_yes", "M38AP_start_operate_ref_oil_no", "M38AP_start_operate_ref_chart_yes",
                                            "M38AP_start_operate_ref_chart_no", "M38AP_start_operate_full_load_yes", "M38AP_start_operate_full_load_no"]

        self.M38AP_start_operate_write = ["M38AP_start_operate_cir_a_prelim_05", "M38AP_start_operate_cir_a_trim_05",
                                            "M38AP_start_operate_cir_a_total_05", "M38AP_start_operate_cirb_click", "M38AP_start_operate_cir_b_prelim_05", "M38AP_start_operate_cir_b_trim_05", "M38AP_start_operate_cir_b_total_05", "M38AP_start_operate_comp_A1_L1_05",
                                            "M38AP_start_operate_comp_A1_L2_05", "M38AP_start_operate_comp_A1_L3_05", "M38AP_start_operate_comp_A2_click", "M38AP_start_operate_comp_A2_L1_05", "M38AP_start_operate_comp_A2_L2_05", "M38AP_start_operate_comp_A2_L3_05",
                                            "M38AP_start_operate_comp_A3_click", "M38AP_start_operate_comp_A3_L1_05", "M38AP_start_operate_comp_A3_L2_05", "M38AP_start_operate_comp_A3_L3_05", "M38AP_start_operate_comp_B1_L1_05", "M38AP_start_operate_comp_B1_L2_05",
                                            "M38AP_start_operate_comp_B1_L3_05", "M38AP_start_operate_comp_B2_click", "M38AP_start_operate_comp_B2_L1_05", "M38AP_start_operate_comp_B2_L2_05", "M38AP_start_operate_comp_B2_L3_05", "M38AP_start_operate_comp_B3_click", "M38AP_start_operate_comp_B3_L1_05",
                                            "M38AP_start_operate_comp_B3_L2_05", "M38AP_start_operate_comp_B3_L3_05", "M38AP_start_operate_fan_FM1_L1_05", "M38AP_start_operate_fan_FM1_L2_05", "M38AP_start_operate_fan_FM1_L3_05",
                                            "M38AP_start_operate_fan_FM2_click", "M38AP_start_operate_fan_FM2_L1_05", "M38AP_start_operate_fan_FM2_L2_05", "M38AP_start_operate_fan_FM2_L3_05", "M38AP_start_operate_fan_FM3_click", "M38AP_start_operate_fan_FM3_L1_05", "M38AP_start_operate_fan_FM3_L2_05",
                                            "M38AP_start_operate_fan_FM3_L3_05", "M38AP_start_operate_fan_FM4_click", "M38AP_start_operate_fan_FM4_L1_05", "M38AP_start_operate_fan_FM4_L2_05", "M38AP_start_operate_fan_FM4_L3_05", "M38AP_start_operate_fan_FM5_click", "M38AP_start_operate_fan_FM5_L1_05",
                                            "M38AP_start_operate_fan_FM5_L2_05", "M38AP_start_operate_fan_FM5_L3_05", "M38AP_start_operate_fan_FM6_click", "M38AP_start_operate_fan_FM6_L1_05", "M38AP_start_operate_fan_FM6_L2_05", "M38AP_start_operate_fan_FM6_L3_05",
                                            "M38AP_start_operate_fan_FM7_click", "M38AP_start_operate_fan_FM7_L1_05", "M38AP_start_operate_fan_FM7_L2_05", "M38AP_start_operate_fan_FM7_L3_05", "M38AP_start_operate_fan_FM8_click", "M38AP_start_operate_fan_FM8_L1_05", "M38AP_start_operate_fan_FM8_L2_05",
                                            "M38AP_start_operate_fan_FM8_L3_05"]

        self.M38AP_rec_config_swrite = []

        self.M38AP_rec_config_tog = []

        self.M38AP_rec_config_write = ["M38AP_rec_config_lang_91", "M38AP_rec_config_ccna_91", "M38AP_rec_config_ccnb_91", "M38AP_rec_config_baud_91", "M38AP_rec_config_pgan_91",
                        "M38AP_rec_config_igan_91", "M38AP_rec_config_dgan_91", "M38AP_rec_config_mins_91"]

        self.M38AP_rec_operate_swrite = []

        self.M38AP_rec_operate_tog = []

        self.M38AP_rec_operate_write = ["M38AP_rec_operate_out_air_temp_05", "M38AP_rec_operate_space_temp_05", "M38AP_rec_operate_dis_gas_temp_91", "M38AP_rec_operate_liq_pres_temp_91"]

        self.M38AP_rec_oil_swrite = []

        self.M38AP_rec_oil_write = []

        self.M38AP_rec_oil_tog = []

        self.M38AP_rec_oil_click = ["M38AP_rec_oil_A1_full", "M38AP_rec_oil_A1_34", "M38AP_rec_oil_A1_12", "M38AP_rec_oil_A114", "M38AP_rec_oil_A1_null", "M38AP_rec_oil_A2_click", "M38AP_rec_oil_A2_full", "M38AP_rec_oil_A2_34",
                                "M38AP_rec_oil_A2_12", "M38AP_rec_oil_A2_14", "M38AP_rec_oil_A2_null", "M38AP_rec_oil_A3_click", "M38AP_rec_oil_A3_full", "M38AP_rec_oil_A3_34", "M38AP_rec_oil_A3_12", "M38AP_rec_oil_A3_14",
                                "M38AP_rec_oil_A3_null", "M38AP_rec_oil_B1_full", "M38AP_rec_oil_B1_34", "M38AP_rec_oil_B1_12", "M38AP_rec_oil_B1_14", "M38AP_rec_oil_B1_null", "M38AP_rec_oil_B2_click", "M38AP_rec_oil_B2_full",
                                "M38AP_rec_oil_B2_34", "M38AP_rec_oil_B2_12", "M38AP_rec_oil_B2_14", "M38AP_rec_oil_B2_null", "M38AP_rec_oil_B3_click", "M38AP_rec_oil_B3_full", "M38AP_rec_oil_B3_34", "M38AP_rec_oil_B3_12",
                                "M38AP_rec_oil_B3_14", "M38AP_rec_oil_B3_null"]

        self.M38AP_operating_instract_write = []

        self.M38AP_operating_instract_tog = ["M38AP_operating_instract_yes", "M38AP_operating_instract_no", "M38AP_operating_instract_20_yes", "M38AP_operating_instract_20_no"]

        self.M38AP_operating_instract_swrite = ["M38AP_operating_instract_Default", "M38AP_operating_instract_time_05"]

    def write_system_startup_info_data(self, Data):
        self.prefix = {'prestart_check':'M38AP_prestart_check', 'software_version_info':'M38AP_software_version_info', 'start_operate':'M38AP_start_operate',
                       'rec_config':'M38AP_rec_config', 'rec_operate':'M38AP_rec_operate', 'rec_oil': 'M38AP_rec_oil', 'operating_instract': 'M38AP_operating_instract'}

        try:
            xpath = eval("SystemStartupLocators." + eval("self."+self.prefix[Data['Model']]+"_swrite[0]"))
            xpath = self.find_elements(*xpath)
            for i in range(len(eval("self."+self.prefix[Data['Model']]+"_swrite"))):
                if "_Default" not in eval("self."+self.prefix[Data['Model']]+"_swrite[i]"):
                    self.checklist.write_similar_element(xpath= xpath, index= eval("SystemStartupLocators." + eval("self."+self.prefix[Data['Model']]+"_swrite[i]")), Data= Data)
                    print('Written Post Start data to ' + str(eval("self."+self.prefix[Data['Model']]+"_swrite[i]")) \
                           + ' =', Data['testdata'])

            # count = 0
            # for ele in range(len(xpath)):
            #     try:
            #         xpath[ele].send_keys(Data['testdata'])
            #         xpath[ele].send_keys(Keys.ENTER)
            #         print eval("self." + self.prefix[Data['Model']] + "_swrite[count]"), ele
            #         count = count + 1
            #     except:
            #         pass
        except IndexError as e:
            pass

        try:
            for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_click'))):
                xpath = eval('self.' + self.prefix[Data['Model']] + '_click')[y]
                self.checklist.click(xpath, page_locators="SystemStartupLocators")
                print('Written SystemStartup data of ' + xpath + ' =', eval('self.' + self.prefix[Data['Model']] + '_click')[y][-4:])
        except:
            pass

        for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_tog'))):
            if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'yes':
                xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
                self.checklist.click(xpath, page_locators="SystemStartupLocators")
                print('Written SystemStartup data of ' + xpath + ' =', 'yes')

        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            xpath = eval("SystemStartupLocators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
            if eval("self." + self.prefix[Data['Model']] + "_write[i]")[-5:] == "click":
                self.checklist.click(eval("self." + self.prefix[Data['Model']] + "_write[i]"), "SystemStartupLocators")
            else: self.checklist.write(xpath, Data)
            print('Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_write[i]") + ' =', Data['testdata'])

    def read_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("SystemStartupLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="SystemStartupLocators")
                assertion.assertEqual(float(value), float(''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]))
                print('Read SystemStartup Information(' + ele + ')' + ' =', value)

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="SystemStartupLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value, 'true')
            elif ele[-2:] == 'no':
                assertion.assertEqual(value, None)
            print('Read SystemStartup Information of '+ ele+' = ', value)

        # for ele in eval("self."+self.prefix[Data['Model']]+"_writables"):
        #     value = self.checklist.read(ele, None, Data, 'read_normal', page_locators="SystemStartupLocators")
        #     assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:5]), True)
        #     # assertion.assertEqual(value == Data['testdata'], True)
        #     print 'Read Prestart Information(' + ele + ')' + ' =', value


        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            common_xpath = eval("SystemStartupLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
            # common_xpath = self.find_elements(*common_xpath)
            value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="SystemStartupLocators")
            if 'click' not in ele:
                if eval(ele[-2:]) <= 5:
                    assertion.assertEqual(float(value), float(''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]))
                else:
                    assertion.assertEqual(value, Data['testdata'][:eval(ele[-2:])])
                print('Read SystemStartup Information(' + ele + ')' + ' =', value)

    def read_reset_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("SystemStartupLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'reset_read', page_locators="SystemStartupLocators", index_assert=5)
                assertion.assertEqual(value, '')
                print('Read SystemStartup Information of ' + ele + ' = ', 'Null')

        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            if 'click' not in ele:
                common_xpath = eval("SystemStartupLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="SystemStartupLocators", index_assert=5)
                assertion.assertEqual(value, '')
                print('Read SystemStartup Information of ' + ele + ' = ', 'Null')

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="SystemStartupLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value, None)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value, 'true')
            print('Read SystemStartup Information of ' + ele + ' = ', value)

    def systemstartup_exit(self):
        self.find_element(*SystemStartupLocators.systemstartup_exit).click()

    def system_startup_save_submenu(self):
        self.find_element(*SystemStartupLocators.systemstartup_savesubmenu).click()

    def system_startup_save_mainmenu(self):
        self.find_element(*SystemStartupLocators.systemstartup_savemainmenu).click()

    def systemstartup_save(self):
        self.find_element(*SystemStartupLocators.systemstartup_save).click()

    def systemstartup_cancel(self):
        self.find_element(*SystemStartupLocators.systemstartup_cancel).click()

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
