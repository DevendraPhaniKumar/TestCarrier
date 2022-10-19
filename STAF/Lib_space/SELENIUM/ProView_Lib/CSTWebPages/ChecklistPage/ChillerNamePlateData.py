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
from Page_locators.ChecklistPagelocators.ChillerNamePlateData_locators import ChillerNamePlateDataPageLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class ChillerNamePlateData(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(ChillerNamePlateData, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  17DA, 19PIC6, 19XL, 19XR, 19XRE, 19XRD, 19XRPIC5, 19XRV  ##########################################################
        self.M17_write = ["M17_compressor_volts", "M17_compressor_rla", "M17_compressor_olta", "M17_starter_mfg_15", "M17_starter_type_15",
                          "M17_starter_sno_15", "M17_oilpump_volts", "M17_oilpump_rla", "M17_oilpump_olta"]

        ##########################################################  23XRV  ##########################################################
        self.M23XRV_write = ["M23XRV_ciller_data_line_voltage", "M23XRV_ciller_data_line_amps", "M23XRV_ciller_data_trip_amps",
                             "M23XRV_vfd_data_input_rating", "M23XRV_vfd_data_trip_amps", "M23XRV_vfd_info_id_no_15", "M23XRV_vfd_info_s_no_15",
                             "M23XRV_vfd_info_mfct_in_15"]

        ##########################################################  32XR  ##########################################################
        self.M32XR_write = ["M32XR_compressor_volts", "M32XR_compressor_rla", "M32XR_compressor_olta", "M32XR_starter_mfg_15",
                            "M32XR_starter_type_15", "M32XR_starter_sno_15", "M32XR_oilpump_volts", "M32XR_oilpump_rla", "M32XR_oilpump_olta",
                            "M32XR_ref_type_15", "M32XR_ref_charge_15"]
        
        
    def write_postptart_info_data(self, Data):
        self.prefix = {'17DA':'M17', '19XR':'M17', '19PIC6': 'M17', '19XRPIC5':'M17', '19XRD': 'M17',
                       '19XL':'M17', '23XRV': 'M23XRV', '32XR': 'M32XR', '19XRE':'M17', '19XRV':'M17'}

        # try:
        #     xpath = eval("ChillerNamePlateDataPageLocators." + eval("self."+self.prefix[Data['Model']]+"_swrite[0]"))
        #     xpath = self.find_elements(*xpath)
        #     for i in range(len(eval("self."+self.prefix[Data['Model']]+"_swrite"))):
        #         if "_Default" not in eval("self."+self.prefix[Data['Model']]+"_swrite[i]"):
        #             self.checklist.write_similar_element(xpath= xpath, index= eval("ChillerNamePlateDataPageLocators." + eval("self."+self.prefix[Data['Model']]+"_swrite[i]")), Data= Data)
        #             print 'Written Chiller Name Plate Data data to ' + str(eval("self."+self.prefix[Data['Model']]+"_swrite[i]")) \
        #                    + ' =', Data['testdata']
        # except IndexError as e:
        #     print e.message

        # count = 0
        # for ele in range(len(xpath)):
        #     try:
        #         xpath[ele].send_keys(Data['testdata'])
        #         xpath[ele].send_keys(Keys.ENTER)
        #         print eval("self." + self.prefix[Data['Model']] + "_swrite[count]"), ele
        #         count = count + 1
        #     except:
        #         pass

        # for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_tog'))):
        #     if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'yes':
        #         xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
        #         self.checklist.click(xpath, page_locators="ChillerNamePlateDataPageLocators")
        #         print 'Written Chiller Name Plate Data data of ' + xpath + ' =', 'yes'

        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            xpath = eval("ChillerNamePlateDataPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
            self.checklist.write(xpath, Data)
            print(('Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_write[i]") + ' =', \
            Data['testdata']))


    def read_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("ChillerNamePlateDataPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="ChillerNamePlateDataPageLocators")
                if ele[-2:] == '15':
                    assertion.assertEqual(value == str(Data['testdata'][:15]), True)
                else:
                    assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:5]), True)
                print(('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value))

        # for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
        #     value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="ChillerNamePlateDataPageLocators")
        #     if ele[-3:] == 'yes':
        #         assertion.assertEqual(value == 'true', True)
        #     elif ele[-2:] == 'no':
        #         assertion.assertEqual(value == None, True)
        #     print 'Read Chiller Name Plate Data Information of '+ ele+' = ', value

        # for ele in eval("self."+self.prefix[Data['Model']]+"_writables"):
        #     value = self.checklist.read(ele, None, Data, 'read_normal', page_locators="ChillerNamePlateDataPageLocators")
        #     assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:5]), True)
        #     # assertion.assertEqual(value == Data['testdata'], True)
        #     print 'Read Prestart Information(' + ele + ')' + ' =', value

        # try:
        #     for ele in eval("self."+self.prefix[Data['Model']]+"_swrite_no_index"):
        #         common_xpath = eval("ChillerNamePlateDataPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
        #         common_xpath = self.find_elements(*common_xpath)
        #         value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="ChillerNamePlateDataPageLocators")
        #         assertion.assertEqual(value == Data['testdata'],True)
        #         print 'Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value
        # except:
        #     pass

    def read_reset_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_write"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("ChillerNamePlateDataPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal', page_locators="ChillerNamePlateDataPageLocators", index_assert=5)
                assertion.assertEqual(value == '', True)
                print(('Read Chiller Name Plate Data Information of ' + ele + ' = ', 'Null'))

        # for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
        #     value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="ChillerNamePlateDataPageLocators")
        #     if ele[-3:] == 'yes':
        #         assertion.assertEqual(value == None, True)
        #     elif ele[-2:] == 'no':
        #         assertion.assertEqual(value == 'true', True)
        #     print 'Read Chiller Name Plate Data Information of ' + ele + ' = ', value

    def chiller_name_plate_data_exit(self):
        self.find_element(*ChillerNamePlateDataPageLocators.chiller_name_plate_data_exit).click()

    def chiller_name_plate_data_save(self):
        self.find_element(*ChillerNamePlateDataPageLocators.chiller_name_plate_data_save).click()

    def chiller_name_plate_data_cancel(self):
        self.find_element(*ChillerNamePlateDataPageLocators.chiller_name_plate_data_cancel).click()

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