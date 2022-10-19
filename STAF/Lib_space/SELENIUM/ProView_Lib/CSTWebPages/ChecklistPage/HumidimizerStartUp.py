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
from Page_locators.ChecklistPagelocators.HumidimizerStartUp_locators import HumidimizerStartUpLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class HumidimizerStartUp(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(HumidimizerStartUp, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  48HC  ##########################################################
        self.M48HC_write = ["M48HC_Obsrv_rec_suction_05", "M48HC_Obsrv_rec_dischrge_05", "M48HC_Obsrv_rec_enter_air_05", "M48HC_Obsrv_rec_outlet_05"]

        self.M48HC_tog = ["M48HC_step_cbt_yes", "M48HC_step_cbt_no", "M48HC_step_humidstat_yes", "M48HC_step_humidstat_no", "M48HC_step_cooling_yes", "M48HC_step_cooling_no",
                            "M48HC_Obsrv_rec_rotatin_yes", "M48HC_Obsrv_rec_rotatin_no", "M48HC_Obsrv_rec_rampup_yes", "M48HC_Obsrv_rec_rampup_no", "M48HC_Obsrv_rec_charge_yes",
                            "M48HC_Obsrv_rec_charge_no", "M48HC_Obsrv_rec_latent_yes", "M48HC_Obsrv_rec_latent_no", "M48HC_obsrv_suction_yes", "M48HC_obsrv_suction_no",
                            "M48HC_obsrv_discharge_yes", "M48HC_obsrv_discharge_no", "M48HC_obsrv_temp_drop_yes", "M48HC_obsrv_temp_drop_no", "M48HC_obsrv_lsv_yes",
                            "M48HC_obsrv_lsv_no", "M48HC_obsrv_dehumid_yes", "M48HC_obsrv_dehumid_no", "M48HC_OBSRV_suction_yes", "M48HC_OBSRV_suction_no",
                            "M48HC_OBSRV_discharge_yes", "M48HC_OBSRV_discharge_no", "M48HC_OBSRV_temp_drop_yes", "M48HC_OBSRV_temp_drop_no", "M48HC_OBSRV_lsv_yes",
                            "M48HC_OBSRV_lsv_no", "M48HC_OBSRV_dsv_yes", "M48HC_OBSRV_dsv_no", "M48HC_OBSRV_dehumid_yes", "M48HC_OBSRV_dehumid_no", "M48HC_OBSRV_w1_yes",
                            "M48HC_OBSRV_w1_no", "M48HC_OBSRV_humidstat_yes", "M48HC_OBSRV_humidstat_no", "M48HC_OBSRV_restore_yes", "M48HC_OBSRV_restore_no"]

        ##########################################################  48TC  ##########################################################
        self.M48TC_write = ["M48TC_Obsrv_rec_suction_05", "M48TC_Obsrv_rec_dischrge_05", "M48TC_Obsrv_rec_enter_air_05", "M48TC_Obsrv_rec_outlet_05"]

        self.M48TC_tog = ["M48TC_step_cbt_yes", "M48TC_step_cbt_no", "M48TC_step_humidstat_yes", "M48TC_step_humidstat_no", "M48TC_step_cooling_yes", "M48TC_step_cooling_no",
                            "M48TC_Obsrv_rec_rotatin_yes", "M48TC_Obsrv_rec_rotatin_no", "M48TC_Obsrv_rec_rampup_yes", "M48TC_Obsrv_rec_rampup_no", "M48TC_Obsrv_rec_charge_yes",
                            "M48TC_Obsrv_rec_charge_no", "M48TC_Obsrv_rec_latent_yes", "M48TC_Obsrv_rec_latent_no", "M48TC_obsrv_suction_yes", "M48TC_obsrv_suction_no",
                            "M48TC_obsrv_discharge_yes", "M48TC_obsrv_discharge_no", "M48TC_obsrv_temp_drop_yes", "M48TC_obsrv_temp_drop_no", "M48TC_obsrv_lsv_yes",
                            "M48TC_obsrv_lsv_no", "M48TC_obsrv_dehumid_yes", "M48TC_obsrv_dehumid_no", "M48TC_OBSRV_suction_yes", "M48TC_OBSRV_suction_no",
                            "M48TC_OBSRV_discharge_yes", "M48TC_OBSRV_discharge_no", "M48TC_OBSRV_temp_drop_yes", "M48TC_OBSRV_temp_drop_no", "M48TC_OBSRV_lsv_yes",
                            "M48TC_OBSRV_lsv_no", "M48TC_OBSRV_dsv_yes", "M48TC_OBSRV_dsv_no", "M48TC_OBSRV_dehumid_yes", "M48TC_OBSRV_dehumid_no", "M48TC_OBSRV_w1_yes",
                            "M48TC_OBSRV_w1_no", "M48TC_OBSRV_humidstat_yes", "M48TC_OBSRV_humidstat_no", "M48TC_OBSRV_restore_yes", "M48TC_OBSRV_restore_no"]

        ##########################################################  48LC  ##########################################################
        self.M48LC_write = ["M48LC_Obsrv_rec_suction_05", "M48LC_Obsrv_rec_dischrge_05", "M48LC_Obsrv_rec_enter_air_05", "M48LC_Obsrv_rec_outlet_05"]

        self.M48LC_tog = ["M48LC_step_humidstat_yes", "M48LC_step_humidstat_no", "M48LC_step_cooling_yes", "M48LC_step_cooling_no",
                            "M48LC_Obsrv_rec_rotatin_yes", "M48LC_Obsrv_rec_rotatin_no", "M48LC_Obsrv_rec_rampup_yes", "M48LC_Obsrv_rec_rampup_no", "M48LC_Obsrv_rec_charge_yes",
                            "M48LC_Obsrv_rec_charge_no", "M48LC_Obsrv_rec_latent_yes", "M48LC_Obsrv_rec_latent_no", "M48LC_obsrv_suction_yes", "M48LC_obsrv_suction_no",
                            "M48LC_obsrv_discharge_yes", "M48LC_obsrv_discharge_no", "M48LC_obsrv_temp_drop_yes", "M48LC_obsrv_temp_drop_no", "M48LC_obsrv_lsv_yes",
                            "M48LC_obsrv_lsv_no", "M48LC_obsrv_dehumid_yes", "M48LC_obsrv_dehumid_no", "M48LC_OBSRV_suction_yes", "M48LC_OBSRV_suction_no",
                            "M48LC_OBSRV_discharge_yes", "M48LC_OBSRV_discharge_no", "M48LC_OBSRV_temp_drop_yes", "M48LC_OBSRV_temp_drop_no", "M48LC_OBSRV_lsv_yes",
                            "M48LC_OBSRV_lsv_no", "M48LC_OBSRV_dsv_yes", "M48LC_OBSRV_dsv_no", "M48LC_OBSRV_dehumid_yes", "M48LC_OBSRV_dehumid_no", "M48LC_OBSRV_w1_yes",
                            "M48LC_OBSRV_w1_no", "M48LC_OBSRV_humidstat_yes", "M48LC_OBSRV_humidstat_no", "M48LC_OBSRV_restore_yes", "M48LC_OBSRV_restore_no"]

    def write_humidstartup_info_data(self, Data):
        self.prefix = {'48HC':'M48HC', '48LC':'M48LC', '48TC':'M48TC'}

        for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_tog'))):
            if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'yes':
                xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
                self.checklist.click(xpath, page_locators="HumidimizerStartUpLocators")
                print('Written Humidimizer Start-Up data of ' + xpath + ' =', 'yes')

        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            xpath = eval("HumidimizerStartUpLocators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
            self.checklist.write(xpath, Data)
            print('Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_write[i]") + ' =', Data['testdata'])

    def read_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="HumidimizerStartUpLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value, 'true')
            elif ele[-2:] == 'no':
                assertion.assertEqual(value, None)
            print('Read Humidimizer Start-Up Information of '+ ele+' = ', value)

        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            common_xpath = eval("HumidimizerStartUpLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
            value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="HumidimizerStartUpLocators")
            if 'click' not in ele:
                if eval(ele[-2:]) <= 5:
                    assertion.assertEqual(float(value), float(''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]))
                else:
                    assertion.assertEqual(value, Data['testdata'][:eval(ele[-2:])])
                print('Read Humidimizer Start-Up Information(' + ele + ')' + ' =', value)

    def read_reset_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            if 'click' not in ele:
                common_xpath = eval("HumidimizerStartUpLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="HumidimizerStartUpLocators", index_assert=5)
                assertion.assertEqual(value, '')
                print('Read Humidimizer Start-Up Information of ' + ele + ' = ', 'Null')

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="HumidimizerStartUpLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value, None)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value, 'true')
            print('Read Humidimizer Start-Up Information of ' + ele + ' = ', value)

    def humidstartup_exit(self):
        self.find_element(*HumidimizerStartUpLocators.humidstartup_exit).click()

    def system_startup_save_submenu(self):
        self.find_element(*HumidimizerStartUpLocators.humidstartup_savesubmenu).click()

    def system_startup_save_mainmenu(self):
        self.find_element(*HumidimizerStartUpLocators.humidstartup_savemainmenu).click()

    def humidstartup_save(self):
        self.find_element(*HumidimizerStartUpLocators.humidstartup_save).click()

    def humidstartup_cancel(self):
        self.find_element(*HumidimizerStartUpLocators.humidstartup_cancel).click()

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
