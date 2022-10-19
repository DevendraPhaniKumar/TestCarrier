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
from Page_locators.ChecklistPagelocators.StartUp_locators import StartUpPageLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class StartUp(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(StartUp, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()


    def locator_name(self):
        ##########################################################  38MN  ##########################################################
        self.M39MN_tog = ["M39MN_option_wiring_yes", "M39MN_option_wiring_no", "M39MN_option_vfd_yes", "M39MN_option_vfd_no", "M39MN_option_rotation_yes", "M39MN_option_rotation_no",
                            "M39MN_option_pulleys_yes", "M39MN_option_pullyes_no", "M39MN_option_sheaves_yes", "M39MN_option_sheaves_no", "M39MN_option_assembly_yes", "M39MN_option_assembly_no",
                            "M39MN_option_condensate_yes", "M39MN_option_condensate_no", "M39MN_option_pitch_yes", "M39MN_option_pitch_no", "M39MN_option_vibration_yes", "M39MN_option_vibration_no",
                            "M39MN_option_airflow_yes", "M39MN_option_airflow_no"]

        self.M39MN_swrite = ["M39MN_Default", "M39MN_option_rpm_05", "M39MN_option_db_temp_05", "M39MN_option_wb_temp_05", "M39MN_option_leave_db_temp_05", "M39MN_option_leave_wb_temp_05", "M39MN_option_enter_temp_05", "M39MN_option_leave_temp_05"]

        self.M39MN_write = []

        ##########################################################  38MW  ##########################################################
        self.M39MW_tog = ["M39MW_option_wiring_yes", "M39MW_option_wiring_no", "M39MW_option_vfd_yes", "M39MW_option_vfd_no", "M39MW_option_rotation_yes", "M39MW_option_rotation_no", "M39MW_option_pulleys_yes",
                            "M39MW_option_pullyes_no", "M39MW_option_sheaves_yes", "M39MW_option_sheaves_no", "M39MW_option_assembly_yes", "M39MW_option_assembly_no", "M39MW_option_condensate_yes", "M39MW_option_condensate_no",
                            "M39MW_option_pitch_yes", "M39MW_option_pitch_no", "M39MW_option_vibration_yes", "M39MW_option_vibration_no", "M39MW_option_airflow_yes", "M39MW_option_airflow_no"]

        self.M39MW_swrite = ["M39MW_Default", "M39MW_option_rpm_05", "M39MW_option_db_temp_05", "M39MW_option_wb_temp_05", "M39MW_option_leave_db_temp_05", "M39MW_option_leave_wb_temp_05", "M39MW_option_enter_temp_05","M39MW_option_leave_temp_05"]

        self.M39MW_write = []

        ##########################################################  48A2  ##########################################################
        self.M48A2_tog = [ "M48A2_pre_gas_ref_chrge_yes", "M48A2_pre_gas_ref_chrge_no"]

        self.M48A2_write = ["M48A2_ele_sup_volts_L12_05", "M48A2_ele_sup_volts_L23_05", "M48A2_ele_sup_volts_L31_05", "M48A2_ele_comp1_amps_L1_05", "M48A2_ele_comp1_amps_L2_05", "M48A2_ele_comp1_amps_L3_05",
                            "M48A2_ele_comp2_amps_L1_05", "M48A2_ele_comp2_amps_L2_05", "M48A2_ele_comp2_amps_L3_05", "M48A2_ele_sup_fan_amps_SAV_05", "M48A2_ele_sup_fan_amps_VAV_05", "M48A2_ele_exh_fan_amps_05",
                            "M48A2_temp_out_air_temp_05", "M48A2_temp_ret_air_temp1_05", "M48A2_temp_ret_air_temp2_05", "M48A2_temp_cool_sup_air_05", "M48A2_temp_heat_sup_air_05", "M48A2_temp_ele_sup_air_05",
                            "M48A2_pre_gas_inlet_05", "M48A2_pre_gas_manifold1_05", "M48A2_pre_gas_manifold2_05", "M48A2_pre_gas_ref_suction1_05", "M48A2_pre_gas_ref_suction2_05", "M48A2_pre_gas_ref_dischrge1_05",
                            "M48A2_pre_gas_ref_dischrge2_05"]

        self.M48A2_swrite = []

        ##########################################################  48A3  ##########################################################
        self.M48A3_tog = ["M48A3_pre_gas_ref_chrge_yes", "M48A3_pre_gas_ref_chrge_no"]

        self.M48A3_write = ["M48A3_ele_sup_volts_L12_05", "M48A3_ele_sup_volts_L23_05", "M48A3_ele_sup_volts_L31_05", "M48A3_ele_comp1_amps_L1_05", "M48A3_ele_comp1_amps_L2_05", "M48A3_ele_comp1_amps_L3_05",
                            "M48A3_ele_comp2_amps_L1_05", "M48A3_ele_comp2_amps_L2_05", "M48A3_ele_comp2_amps_L3_05", "M48A3_ele_sup_fan_amps_SAV_05", "M48A3_ele_sup_fan_amps_VAV_05", "M48A3_ele_exh_fan_amps_05",
                            "M48A3_temp_out_air_temp_05", "M48A3_temp_ret_air_temp1_05", "M48A3_temp_ret_air_temp2_05", "M48A3_temp_cool_sup_air_05", "M48A3_temp_heat_sup_air_05", "M48A3_temp_ele_sup_air_05",
                            "M48A3_pre_gas_inlet_05", "M48A3_pre_gas_manifold1_05", "M48A3_pre_gas_manifold2_05", "M48A3_pre_gas_ref_suction1_05", "M48A3_pre_gas_ref_suction2_05", "M48A3_pre_gas_ref_dischrge1_05",
                            "M48A3_pre_gas_ref_dischrge2_05"]

        self.M48A3_swrite = []

        ##########################################################  50A3  ##########################################################
        self.M50A3_tog = ["M50A3_pre_gas_ref_chrge_yes", "M50A3_pre_gas_ref_chrge_no"]

        self.M50A3_swrite = []

        self.M50A3_write = ["M50A3_ele_sup_volts_L12_05", "M50A3_ele_sup_volts_L23_05", "M50A3_ele_sup_volts_L31_05", "M50A3_ele_comp1_amps_L1_05", "M50A3_ele_comp1_amps_L2_05", "M50A3_ele_comp1_amps_L3_05",
                            "M50A3_ele_comp2_amps_L1_05", "M50A3_ele_comp2_amps_L2_05", "M50A3_ele_comp2_amps_L3_05", "M50A3_ele_sup_fan_amps_SAV_05", "M50A3_ele_sup_fan_amps_VAV_05", "M50A3_ele_exh_fan_amps_05",
                            "M50A3_temp_out_air_temp_05", "M50A3_temp_ret_air_temp1_05", "M50A3_temp_ret_air_temp2_05", "M50A3_temp_cool_sup_air_05", "M50A3_temp_heat_sup_air_05", "M50A3_temp_ele_sup_air_05",
                            "M50A3_pre_gas_inlet_05", "M50A3_pre_gas_manifold1_05", "M50A3_pre_gas_manifold2_05", "M50A3_pre_gas_ref_suction1_05", "M50A3_pre_gas_ref_suction2_05", "M50A3_pre_gas_ref_dischrge1_05",
                            "M50A3_pre_gas_ref_dischrge2_05"]

        ##########################################################  48HC  ##########################################################
        self.M48HC_tog = ["M48HC_pre_cm_blow_rotation_yes", "M48HC_pre_cm_blow_rotation_no", "M48HC_pre_cm_comp_rotation_yes", "M48HC_pre_cm_comp_rotation_no", "M48HC_pre_cm_ref_charge_yes",
                            "M48HC_pre_cm_ref_charge_no", "M48HC_pre_hp_ref_chrg_yes", "M48HC_pre_hp_ref_chrg_no", "M48HC_pre_hp_ref_smoke_yes", "M48HC_pre_hp_ref_smoke_no", "M48HC_gen_eco_min_yes", "M48HC_gen_eco_min_no"]

        self.M48HC_swrite = []

        self.M48HC_write = ["M48HC_ele_sup_volts_L12_05", "M48HC_ele_sup_volts_L23_05", "M48HC_ele_sup_volts_L31_05", "M48HC_ele_comp1_amps_L1_05", "M48HC_ele_comp1_amps_L2_05", "M48HC_ele_comp1_amps_L3_05",
                            "M48HC_ele_comp2_amps_L1_05", "M48HC_ele_comp2_amps_L2_05", "M48HC_ele_comp2_amps_L3_05", "M48HC_ele_infan_amps_L1_05", "M48HC_ele_infan_amps_L2_05", "M48HC_ele_infan_amps_L3_05",
                            "M48HC_ele_outfan_amps_L1_05", "M48HC_ele_outfan_amps_L2_05", "M48HC_ele_outfan_amps_L3_05", "M48HC_pre_ret_static_05", "M48HC_pre_sup_static_05", "M48HC_pre_blower_rpm_05",
                            "M48HC_temp_outair_db_05", "M48HC_temp_outair_wb_05", "M48HC_temp_retair_db_05", "M48HC_temp_retair_wb_05", "M48HC_temp_coolair_db_05", "M48HC_temp_coolair_wb_05", "M48HC_temp_heatair_db_05",
                            "M48HC_pre_cm_inlet_05", "M48HC_pre_cm_manifold_Low_05", "M48HC_pre_cm_manifold_Hi_05", "M48HC_pre_cm_ref_suct1_05", "M48HC_pre_cm_ref_suct1_temp_05", "M48HC_pre_cm_ref_suct2_05",
                            "M48HC_pre_cm_ref_suct2_temp_05", "M48HC_pre_cm_dischrge1_05", "M48HC_pre_cm_dischrge1_temp_05", "M48HC_pre_cm_dischrge2_05", "M48HC_pre_cm_dischrge2_temp_05",
                            "M48HC_pre_hp_ref_suctA_05", "M48HC_pre_hp_ref_suctB_05", "M48HC_pre_hp_ref_dischrgA_05", "M48HC_pre_hp_ref_dischrgB_05"]

        ##########################################################  48TC  ##########################################################
        self.M48TC_tog = ["M48TC_pre_cm_blow_rotation_yes", "M48TC_pre_cm_blow_rotation_no", "M48TC_pre_cm_comp_rotation_yes", "M48TC_pre_cm_comp_rotation_no", "M48TC_pre_cm_ref_charge_yes", "M48TC_pre_cm_ref_charge_no",
                            "M48TC_pre_hp_ref_chrg_yes", "M48TC_pre_hp_ref_chrg_no", "M48TC_pre_hp_ref_smoke_yes", "M48TC_pre_hp_ref_smoke_no", "M48TC_gen_eco_min_yes", "M48TC_gen_eco_min_no"]

        self.M48TC_swrite = []

        self.M48TC_write = ["M48TC_ele_sup_volts_L12_05", "M48TC_ele_sup_volts_L23_05", "M48TC_ele_sup_volts_L31_05", "M48TC_ele_comp1_amps_L1_05", "M48TC_ele_comp1_amps_L2_05", "M48TC_ele_comp1_amps_L3_05",
                            "M48TC_ele_comp2_amps_L1_05", "M48TC_ele_comp2_amps_L2_05", "M48TC_ele_comp2_amps_L3_05", "M48TC_ele_infan_amps_L1_05", "M48TC_ele_infan_amps_L2_05", "M48TC_ele_infan_amps_L3_05",
                            "M48TC_ele_outfan_amps_L1_05", "M48TC_ele_outfan_amps_L2_05", "M48TC_ele_outfan_amps_L3_05", "M48TC_pre_ret_static_05", "M48TC_pre_sup_static_05", "M48TC_pre_blower_rpm_05",
                            "M48TC_temp_outair_db_05", "M48TC_temp_outair_wb_05", "M48TC_temp_retair_db_05", "M48TC_temp_retair_wb_05", "M48TC_temp_coolair_db_05", "M48TC_temp_coolair_wb_05",
                            "M48TC_temp_heatair_db_05", "M48TC_pre_cm_inlet_05", "M48TC_pre_cm_manifold_Low_05", "M48TC_pre_cm_manifold_Hi_05", "M48TC_pre_cm_ref_suct1_05", "M48TC_pre_cm_ref_suct1_temp_05",
                            "M48TC_pre_cm_ref_suct2_05", "M48TC_pre_cm_ref_suct2_temp_05", "M48TC_pre_cm_dischrge1_05", "M48TC_pre_cm_dischrge1_temp_05", "M48TC_pre_cm_dischrge2_05", "M48TC_pre_cm_dischrge2_temp_05",
                            "M48TC_pre_hp_ref_suctA_05", "M48TC_pre_hp_ref_suctB_05", "M48TC_pre_hp_ref_dischrgA_05", "M48TC_pre_hp_ref_dischrgB_05"]

        ##########################################################  48LC  ##########################################################
        self.M48LC_tog = ["M48LC_pre_ref_charge_yes", "M48LC_pre_ref_charge_no", "M48LC_gen_eco_min_yes", "M48LC_gen_eco_min_no", "M48LC_gen_smoke_yes", "M48LC_gen_smoke_no"]

        self.M48LC_swrite = []

        self.M48LC_write = ["M48LC_ele_sup_volts_L12_05", "M48LC_ele_sup_volts_L23_05", "M48LC_ele_sup_volts_L31_05", "M48LC_ele_comp1_amps_L1_05", "M48LC_ele_comp1_amps_L2_05", "M48LC_ele_comp1_amps_L3_05",
                            "M48LC_ele_comp2_amps_L1_05", "M48LC_ele_comp2_amps_L2_05", "M48LC_ele_comp2_amps_L3_05", "M48LC_ele_infan_amps_L1_05", "M48LC_ele_infan_amps_L2_05", "M48LC_ele_infan_amps_L3_05",
                            "M48LC_temp_outair_db_05", "M48LC_temp_retair_db_05", "M48LC_temp_retair_wb_05",
                            "M48LC_temp_coolair_db_05", "M48LC_temp_heatair_db_05", "M48LC_pre_inlet_05", "M48LC_pre_manifold1_05", "M48LC_pre_manifold2_05", "M48LC_pre_ref_suctA_05", "M48LC_pre_ref_suctB_05",
                            "M48LC_pre_dischrgeA_05", "M48LC_pre_dischrgeB_05"]

        ##########################################################  50HC  ##########################################################
        self.M50HC_tog = ["M50HC_pre_ref_chrg_yes", "M50HC_pre_ref_chrg_no", "M50HC_pre_ref_rot_direction_yes", "M50HC_pre_ref_rot_direction_no", "M50HC_pre_smoke_yes", "M50HC_pre_smoke_no"]

        self.M50HC_swrite = []

        self.M50HC_write = ["M50HC_ele_sup_volts_L12_05", "M50HC_ele_sup_volts_L23_05", "M50HC_ele_sup_volts_L31_05", "M50HC_ele_comp_amps_L1_05", "M50HC_ele_comp_amps_L2_05", "M50HC_ele_comp_amps_L3_05",
                            "M50HC_ele_fan_amps_L1_05", "M50HC_ele_fan_amps_L2_05", "M50HC_ele_fan_amps_L3_05", "M50HC_temp_outair_db_05", "M50HC_temp_outair_wb_05", "M50HC_temp_retair_db_05",
                            "M50HC_temp_retair_wb_05", "M50HC_temp_coolair_db_05", "M50HC_temp_coolair_wb_05", "M50HC_temp_heatair_db_05", "M50HC_pre_inlet_05", "M50HC_pre_manifold_low_05",
                            "M50HC_pre_manifold_hi_05", "M50HC_pre_ref_suct_05", "M50HC_pre_ref_suct_temp_05", "M50HC_pre_ref_dischrg_05", "M50HC_pre_ref_dischrg_temp_05"]

        ##########################################################  50PCPS  ##########################################################
        self.M50PCPS_tog = ["M50PCPS_fan_comp_yes", "M50PCPS_fan_comp_no", "M50PCPS_rotation_yes", "M50PCPS_rotation_no", "M50PCPS_control_volt_yes", "M50PCPS_control_volt_no"]

        self.M50PCPS_swrite = ["M50PCPS_Default", "M50PCPS_unit_AB1_05", "M50PCPS_unit_BC1_05", "M50PCPS_unit_CA1_05", "M50PCPS_unit_AB2_05", "M50PCPS_unit_BC2_05", "M50PCPS_unit_CA2_05", "M50PCPS_coaxial_cc_liq_line_05",
                                "M50PCPS_coaxial_cc_fluid_in_05", "M50PCPS_coaxial_cc_fluid_out_05", "M50PCPS_coaxial_cc_press_in_05", "M50PCPS_coaxial_cc_press_out_05", "M50PCPS_coaxial_cc_flow_rate_05",
                                "M50PCPS_coaxial_hc_liq_line_05", "M50PCPS_coaxial_hc_fluid_in_05", "M50PCPS_coaxial_hc_fluid_out_05", "M50PCPS_coaxial_hc_press_in_05", "M50PCPS_coaxial_hc_press_out_05",
                                "M50PCPS_coaxial_hc_flow_rate_05", "M50PCPS_coil_cc_air_in_05", "M50PCPS_coil_cc_air_out_05", "M50PCPS_coil_hc_air_in_05", "M50PCPS_coil_hc_air_out_05", "M50PCPS_flow_rate_05",
                                "M50PCPS_temp_diff_05", "M50PCPS_fluid_fac_05", "M50PCPS_suct_temp_05", "M50PCPS_suct_sat_temp_05", "M50PCPS_super_heat_05", "M50PCPS_dischrg_suct_temp_05", "M50PCPS_liq_line_temp_05",
                                "M50PCPS_subcool_05"]

        self.M50PCPS_write = []

    def write_startupmenu_info_data(self, Data):
        self.prefix = {'39MN':'M39MN', '39MW':'M39MW', '48A2':'M48A2', '48A3':'M48A3', '48HC': 'M48HC', '48LC':'M48LC',
                       '48TC':'M48TC', '50A3':'M50A3', '50PC/PS': 'M50PCPS', '50HC': 'M50HC'}

        try:
            xpath = eval("StartUpPageLocators." + eval("self."+self.prefix[Data['Model']]+"_swrite[0]"))
            xpath = self.find_elements(*xpath)
            for i in range(len(eval("self."+self.prefix[Data['Model']]+"_swrite"))):
                if "_Default" not in eval("self."+self.prefix[Data['Model']]+"_swrite[i]"):
                    self.checklist.write_similar_element(xpath= xpath, index= eval("StartUpPageLocators." + eval("self."+self.prefix[Data['Model']]+"_swrite[i]")), Data= Data)
                    print(( 'Written Post Start data to ' + str(eval("self."+self.prefix[Data['Model']]+"_swrite[i]")) \
                           + ' =', Data['testdata']))
            # count = 0
            # for ele in range(len(xpath)):
            #     try:
            #         xpath[ele].send_keys(Data['testdata'])
            #         xpath[ele].send_keys(Keys.ENTER)
            #         print eval("self." + self.prefix[Data['Model']] + "_swrite[count]"), ele
            #         count = count + 1
            #     except:
            #         pass
        except Exception as e:
            print((e.message))

        for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_tog'))):
            if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'yes':
                xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
                self.checklist.click(xpath, page_locators="StartUpPageLocators")
                print(('Written Start-Up data of ' + xpath + ' =', 'yes'))

        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            xpath = eval("StartUpPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
            self.checklist.write(xpath, Data)
            print(('Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_write[i]") + ' =', \
            Data['testdata']))


    def read_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("StartUpPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="StartUpPageLocators", index_assert=5)
                assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:5]), True)
                print(('Read Start-Up Information(' + ele + ')' + ' =', value))

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="StartUpPageLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == 'true', True)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value == None, True)
            print(('Read Start-Up Information of '+ ele+' = ', value))

        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            common_xpath = eval("StartUpPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
            value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="StartUpPageLocators")
            if 'click' not in ele:
                if eval(ele[-2:]) <= 5:
                    assertion.assertEqual(float(value), float(''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]))
                else:
                    assertion.assertEqual(value, Data['testdata'][:eval(ele[-2:])])
                print(('Read Start-Up Information(' + ele + ')' + ' =', value))

    def read_reset_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("StartUpPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'reset_read', page_locators="StartUpPageLocators", index_assert=5)
                assertion.assertEqual(value == '', True)
                print(('Read Start-Up Information of ' + ele + ' = ', 'Null'))

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="StartUpPageLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == None, True)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value == 'true', True)
            print(('Read Start-Up Information of ' + ele + ' = ', value))

        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            if 'click' not in ele:
                common_xpath = eval("StartUpPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="StartUpPageLocators", index_assert=5)
                assertion.assertEqual(value, '')
                print(('Read Start-Up Information of ' + ele + ' = ', 'Null'))

    def startupmenu_exit(self):
        self.find_element(*StartUpPageLocators.startupmenu_exit).click()

    def startupmenu_save(self):
        self.find_element(*StartUpPageLocators.startupmenu_save).click()

    def startupmenu_cancel(self):
        self.find_element(*StartUpPageLocators.startupmenu_cancel).click()

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
            print ("Loading took too much time!")

    def wait_unit_visible(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, element[-1])))
        except TimeoutException:
            print ("Loading took too much time!")