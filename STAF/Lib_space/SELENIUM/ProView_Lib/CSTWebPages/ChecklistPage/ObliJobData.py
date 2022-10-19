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
from Page_locators.ChecklistPagelocators.ObliJobData_locators import ObliJobDataPageLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class ObliJobData(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(ObliJobData, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  16JB & 16JT & 23XL ##########################################################
        self.M16JB_JT_swrite = ["M16JB_JT_Default", "M16JB_JT_carrier_obli_operating_hrs_05"]

        self.M16JB_JT_tog = ["M16JB_JT_carrier_obli_assemble_yes", "M16JB_JT_carrier_obli_assemble_no", "M16JB_JT_carrier_obli_leak_test_yes", "M16JB_JT_carrier_obli_leak_test_no", "M16JB_JT_carrier_obli_dehydrate_yes",
                                "M16JB_JT_carrier_obli_dehydrate_no", "M16JB_JT_carrier_obli_charging_yes", "M16JB_JT_carrier_obli_charging_no", "M16JB_JT_carrier_job_install_yes", "M16JB_JT_carrier_job_install_no",
                                "M16JB_JT_carrier_job_assemble_yes", "M16JB_JT_carrier_job_assemble_no", "M16JB_JT_carrier_job_details_yes", "M16JB_JT_carrier_job_details_no", "M16JB_JT_carrier_job_design_yes",
                                "M16JB_JT_carrier_job_design_no", "M16JB_JT_carrier_job_diags_yes", "M16JB_JT_carrier_job_diags_no"]
        ##########################################################  19PICC6, 19XL, 19XRD, 19XRE, 19XRPIC5, 19XRV, 23XRV, 17DA, 32XR, 19XR ##########################################################
        self.M32XR_swrite = ["M32XR_Default", "M32XR_carrier_obli_operating_hrs_05"]

        self.M32XR_tog = ["M32XR_carrier_obli_assemble_yes", "M32XR_carrier_obli_assemble_no", "M32XR_carrier_obli_leak_test_yes", "M32XR_carrier_obli_leak_test_no", "M32XR_carrier_obli_dehydrate_yes",
                            "M32XR_carrier_obli_dehydrate_no", "M32XR_carrier_obli_charging_yes", "M32XR_carrier_obli_charging_no", "M32XR_carrier_job_install_yes", "M32XR_carrier_job_install_no",
                            "M32XR_carrier_job_assemble_yes", "M32XR_carrier_job_assemble_no", "M32XR_carrier_job_details_yes", "M32XR_carrier_job_details_no", "M32XR_carrier_job_design_yes",
                            "M32XR_carrier_job_design_no", "M32XR_carrier_job_diags_yes", "M32XR_carrier_job_diags_no"]

    def write_obj_job_data(self, Data):
        self.prefix = {'16JT': 'M16JB_JT', '16JB': 'M16JB_JT', '17DA': 'M32XR', '19XR': 'M32XR', '19PIC6': 'M32XR',
                       '19XRPIC5': 'M32XR', '19XL': 'M32XR', '23XL': 'M16JB_JT', '23XRV': 'M32XR', '32XR': 'M32XR',
                       '19XRD': 'M32XR', '19XRE': 'M32XR', '19XRV': 'M32XR'}

        try:
            xpath = eval("ObliJobDataPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
            xpath = self.find_elements(*xpath)
            # for i in range(len(eval("self." + self.prefix[Data['Model']] + "_swrite"))):
            #     if "_Default" not in eval("self." + self.prefix[Data['Model']] + "_swrite[i]"):
            #         self.checklist.write_similar_element(xpath=xpath, index=eval(
            #             "ObliJobDataPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[i]")),
            #                                              Data=Data)
            #         print 'Written Post Start data to ' + str(eval("self." + self.prefix[Data['Model']] + "_swrite[i]")) \
            #               + ' =', Data['testdata']
        except IndexError as e:
            print(e.message)

        count = 0
        for ele in range(len(xpath)):
            try:
                xpath[ele].send_keys(Data['testdata'])
                xpath[ele].send_keys(Keys.ENTER)
                print(eval("self." + self.prefix[Data['Model']] + "_swrite[count]"), ele)
                count = count + 1
            except:
                pass

        for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_tog'))):
            if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'yes':
                xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
                self.checklist.click(xpath, page_locators="ObliJobDataPageLocators")
                print('Written oblijobdata data of ' + xpath + ' =', 'yes')

        # for i in range(len(eval("self." + self.prefix[Data['Model']] + "_writables"))):
        #     xpath = eval("PreStartPageLocators." + eval("self." + self.prefix[Data['Model']] + "_writables[i]"))
        #     self.checklist.write(xpath, Data)
        #     print 'Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_writables[i]") + ' =', \
        #     Data['testdata']

    def read_data(self, Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_swrite"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval("ObliJobDataPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="ObliJobDataPageLocators", index_assert=5)
                assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]), True)
                print('Read oblijobdata Information(' + ele + ')' + ' =', value)

        for ele in eval("self." + self.prefix[Data['Model']] + "_tog"):
            value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="ObliJobDataPageLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == 'true', True)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value == None, True)
            print('Read oblijobdata Information of ' + ele + ' = ', value)

        # for ele in eval("self."+self.prefix[Data['Model']]+"_writables"):
        #     value = self.checklist.read(ele, None, Data, 'read_normal', page_locators="PreStartPageLocators")
        #     assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:5]), True)
        #     # assertion.assertEqual(value == Data['testdata'], True)
        #     print 'Read Prestart Information(' + ele + ')' + ' =', value

        try:
            for ele in eval("self." + self.prefix[Data['Model']] + "_swrite_no_index"):
                common_xpath = eval(
                    "ObliJobDataPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="ObliJobDataPageLocators")
                assertion.assertEqual(value == Data['testdata'], True)
                print('Read oblijobdata Information(' + ele + ')' + ' =', value)
        except:
            pass

    def read_reset_data(self, Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_swrite"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "ObliJobDataPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'reset_read',
                                            page_locators="ObliJobDataPageLocators", index_assert=5)
                assertion.assertEqual(value == '', True)
                print('Read oblijobdata Information of ' + ele + ' = ', 'Null')

        for ele in eval("self." + self.prefix[Data['Model']] + "_tog"):
            value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="ObliJobDataPageLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == None, True)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value == 'true', True)
            print('Read oblijobdata Information of ' + ele + ' = ', value)

    def oblijobdata_exit(self):
        self.find_element(*ObliJobDataPageLocators.oblijobdata_exit).click()

    def oblijobdata_save(self):
        self.find_element(*ObliJobDataPageLocators.oblijobdata_save).click()

    def oblijobdata_cancel(self):
        self.find_element(*ObliJobDataPageLocators.oblijobdata_cancel).click()

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