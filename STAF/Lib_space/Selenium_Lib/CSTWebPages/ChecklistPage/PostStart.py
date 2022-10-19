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
from Page_locators.ChecklistPagelocators.PostStartPage_locators import PostStartPageLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class PostStart(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(PostStart, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        """Post Start Page locators"""
        ##########################################################  16JB & 16JT  ##########################################################
        self.M16JB_JT_tog = ["M16JB_JT_under_control_section_yes", "M16JB_JT_under_control_section_no", "M16JB_JT_readings_records_yes", "M16JB_JT_readings_records_no",
                        "M16JB_JT_add_alochol_yes", "M16JB_JT_add_alochol_no", "M16JB_JT_chiller_startup_yes", "M16JB_JT_chiller_startup_no"]

        self.M16JB_JT_swrite = ["M16JB_JT_Default", "M16JB_JT_operating_hrs"]

        self.M16JB_JT_txt = ["M16JB_JT_under_control_section_txt", "M16JB_JT_readings_records_txt", "M16JB_JT_add_alochol_txt", "M16JB_JT_chiller_startup_txt",
                        "M16JB_JT_operating_hrs_txt"]
        ###################################################################################################################################
        ##############################################################  17DA  #############################################################
        self.M17DA_tog = ["M17DA_trim_charge_yes", "M17DA_trim_charge_no", "M17DA_control_yes", "M17DA_control_no", "M17DA_readings_yes", "M17DA_readings_no",
                    "M17DA_shutdown_yes", "M17DA_shutdown_no", "M17DA_instructions_yes", "M17DA_instructions_no", "M17DA_factory_yes", "M17DA_factory_no"]

        self.M17DA_swrite = ["M17DA_Default", "M17DA_final_charge"]

        self.M17DA_txt = ["M17DA_hours", "M17DA_hours_txt", "M17DA_final_charge_txt", "M17DA_trim_charge_txt", "M17DA_control_txt", "M17DA_readings_txt",
                    "M17DA_shutdown_txt", "M17DA_instructions_txt", "M17DA_factory_txt"]
        ###################################################################################################################################
        #############################################################  19PIC6  ############################################################
        self.M19PIC6_tog = ["M19PIC6_trim_charge_yes", "M19PIC6_trim_charge_no", "M19PIC6_control_yes", "M19PIC6_control_no", "M19PIC6_readings_yes", "M19PIC6_readings_no",
                        "M19PIC6_shutdown_txt", "M19PIC6_shutdown_yes", "M19PIC6_shutdown_no", "M19PIC6_instructions_yes", "M19PIC6_instructions_no", "M19PIC6_factory_yes",
                        "M19PIC6_factory_no"]

        self.M19PIC6_swrite = ["M19PIC6_Default", "M19PIC6_final_charge", "M19PIC6_hours"]

        self.M19PIC6_txt = ["M19PIC6_trim_charge_txt", "M19PIC6_hours_txt", "M19PIC6_final_charge_txt",
                            "M19PIC6_control_txt", "M19PIC6_readings_txt", "M19PIC6_shutdown_txt", "M19PIC6_instructions_txt", "M19PIC6_factory_txt"]
        ###################################################################################################################################
        ##############################################################  19XL  #############################################################
        self.M19XL_tog = ["M19XL_trim_charge_yes", "M19XL_trim_charge_no", "M19XL_control_yes", "M19XL_control_no", "M19XL_readings_yes", "M19XL_readings_no",
                    "M19XL_shutdown_yes", "M19XL_shutdown_no", "M19XL_factory_yes", "M19XL_factory_no"]

        self.M19XL_swrite = ["M19XL_Default", "M19XL_hours"]

        self.M19XL_txt = ["M19XL_trim_charge_txt",
                    "M19XL_control_txt", "M19XL_readings_txt", "M19XL_shutdown_txt", "M19XL_factory_txt", "M19XL_hours_txt"]
        ###################################################################################################################################
        ##############################################################  19XR  #############################################################
        self.M19XR_tog = ["M19XR_trim_charge_yes", "M19XR_trim_charge_no", "M19XR_control_yes", "M19XR_control_no", "M19XR_readings_yes", "M19XR_readings_no",
                    "M19XR_shutdown_yes", "M19XR_shutdown_no", "M19XR_instructions_yes", "M19XR_instructions_no", "M19XR_factory_yes", "M19XR_factory_no"]

        self.M19XR_swrite = ["M19XR_Default", "M19XR_final_charge", "M19XR_hours"]

        self.M19XR_txt = ["M19XR_trim_charge_txt", "M19XR_control_txt", "M19XR_readings_txt", "M19XR_shutdown_txt",
                    "M19XR_instructions_txt", "M19XR_factory_txt", "M19XR_final_charge_txt", "M19XR_hours_txt"]
        ###################################################################################################################################
        #############################################################  19XRD  #############################################################
        self.M19XRD_tog = ["M19XRD_trim_charge_yes", "M19XRD_trim_charge_no", "M19XRD_control_yes", "M19XRD_control_no", "M19XRD_readings_yes", "M19XRD_readings_no",
                    "M19XRD_shutdown_yes", "M19XRD_shutdown_no", "M19XRD_instructions_yes", "M19XRD_instructions_no", "M19XRD_factory_yes", "M19XRD_factory_no"]

        self.M19XRD_swrite = ["M19XRD_Default", "M19XRD_final_charge", "M19XRD_hours"]

        self.M19XRD_txt = ["M19XRD_trim_charge_txt", "M19XRD_control_txt", "M19XRD_readings_txt", "M19XRD_shutdown_txt",
                    "M19XRD_instructions_txt", "M19XRD_factory_txt", "M19XRD_final_charge_txt", "M19XRD_hours_txt"]
        ###################################################################################################################################
        #############################################################  19XRE  #############################################################
        self.M19XRE_tog = ["M19XRE_trim_charge_yes", "M19XRE_trim_charge_no", "M19XRE_control_yes", "M19XRE_control_no", "M19XRE_readings_yes", "M19XRE_readings_no",
                    "M19XRE_shutdown_yes", "M19XRE_shutdown_no", "M19XRE_instructions_yes", "M19XRE_instructions_no", "M19XRE_factory_yes", "M19XRE_factory_no"]

        self.M19XRE_swrite = ["M19XRE_Default", "M19XRE_final_charge", "M19XRE_hours"]

        self.M19XRE_txt = ["M19XRE_trim_charge_txt", "M19XRE_control_txt", "M19XRE_readings_txt", "M19XRE_shutdown_txt",
                    "M19XRE_instructions_txt", "M19XRE_factory_txt", "M19XRE_hours_txt", "M19XRE_final_charge_txt"]
        ###################################################################################################################################
        ##########################################################  19XRPIC5  #############################################################
        self.M19XRPIC5_tog = ["M19XRPIC5_trim_charge_yes", "M19XRPIC5_trim_charge_no", "M19XRPIC5_control_yes", "M19XRPIC5_control_no", "M19XRPIC5_readings_yes",
                        "M19XRPIC5_readings_no", "M19XRPIC5_shutdown_yes", "M19XRPIC5_shutdown_no", "M19XRPIC5_instructions_yes", "M19XRPIC5_instructions_no",
                        "M19XRPIC5_factory_yes", "M19XRPIC5_factory_no"]

        self.M19XRPIC5_swrite = ["M19XRPIC5_Default", "M19XRPIC5_final_charge", "M19XRPIC5_hours"]

        self.M19XRPIC5_txt = ["M19XRPIC5_trim_charge_txt", "M19XRPIC5_control_txt", "M19XRPIC5_readings_txt", "M19XRPIC5_shutdown_txt", "M19XRPIC5_instructions_txt",
                              "M19XRPIC5_factory_txt", "M19XRPIC5_final_charge_txt", "M19XRPIC5_hours_txt"]
        ###################################################################################################################################
        #############################################################  19XRV  #############################################################
        self.M19XRV_tog = ["M19XRV_trim_charge_yes", "M19XRV_trim_charge_no", "M19XRV_control_yes", "M19XRV_control_no", "M19XRV_VFD_yes", "M19XRV_VFD_no",
                        "M19XRV_reading_yes", "M19XRV_reading_no", "M19XRV_shutdown_yes", "M19XRV_shutdown_no", "M19XRV_instructions_yes", "M19XRV_instructions_no",
                        "M19XRV_factory_yes", "M19XRV_factory_no"]

        self.M19XRV_swrite = ["M19XRV_Default", "M19XRV_final_charge", "M19XRV_hours"]

        self.M19XRV_txt = ["M19XRV_hours_txt", "M19XRV_factory_txt",
                        "M19XRV_final_charge_txt", "M19XRV_instructions_txt", "M19XRV_shutdown_txt", "M19XRV_reading_txt", "M19XRV_VFD_txt", "M19XRV_control_txt",
                        "M19XRV_trim_charge_txt"]
        ###################################################################################################################################
        #############################################################  23XL  ##############################################################
        self.M23XL_tog = ["M23XL_trim_charge_yes", "M23XL_trim_charge_no", "M23XL_control_yes", "M23XL_control_no", "M23XL_readings_yes", "M23XL_readings_no",
                    "M23XL_shutdown_yes", "M23XL_shutdown_no", "M23XL_factory_yes", "M23XL_factory_no"]

        self.M23XL_swrite = ["M23XL_Default", "M23XL_instructions"]

        self.M23XL_txt = ["M23XL_trim_charge_txt",
                        "M23XL_control_txt", "M23XL_readings_txt", "M23XL_shutdown_txt", "M23XL_instructions_txt", "M23XL_factory_txt"]
        ###################################################################################################################################
        #############################################################  23XRV  #############################################################
        self.M23XRV_tog = ["M23XRV_trim_charge_yes", "M23XRV_trim_charge_no", "M23XRV_inspect_yes", "M23XRV_inspect_no", "M23XRV_control_yes", "M23XRV_control_no",
                    "M23XRV_readings_yes", "M23XRV_readings_no", "M23XRV_shutdown_yes", "M23XRV_shutdown_no", "M23XRV_factory_yes", "M23XRV_factory_no",
                    "M23XRV_rockwell_yes", "M23XRV_rockwell_no", "M23XRV_email_yes", "M23XRV_email_no"]

        self.M23XRV_swrite = ["M23XRV_Default", "M23XRV_final_charge", "M23XRV_hours"]

        self.M23XRV_txt = ["M23XRV_trim_charge_txt", "M23XRV_inspect_txt", "M23XRV_control_txt", "M23XRV_readings_txt", "M23XRV_shutdown_txt", "M23XRV_factory_txt",
                    "M23XRV_rockwell_txt", "M23XRV_email_txt", "M23XRV_final_charge_txt", "M23XRV_hours_txt"]
        ###################################################################################################################################
        ##############################################################  32XR  #############################################################
        self.M32XR_tog = ["M32XR_trim_charge_yes", "M32XR_trim_charge_no", "M32XR_control_yes", "M32XR_control_no", "M32XR_vfd_yes", "M32XR_vfd_no", "M32XR_readings_yes",
                    "M32XR_readings_no", "M32XR_shutdown_yes", "M32XR_shutdown_no", "M32XR_instructions_yes", "M32XR_instructions_no", "M32XR_factory_yes",
                    "M32XR_factory_no"]

        self.M32XR_swrite = ["M32XR_Default", "M32XR_final_charge"]

        self.M32XR_txt = ["M32XR_trim_charge_txt", "M32XR_control_txt", "M32XR_vfd_txt", "M32XR_readings_txt",
                        "M32XR_shutdown_txt", "M32XR_instructions_txt", "M32XR_factory_txt", "M32XR_final_charge_txt"]
        ###################################################################################################################################

    def write_postptart_info_data(self, Data):
        self.prefix = {'16JT':'M16JB_JT', '16JB':'M16JB_JT', '17DA':'M17DA', '19XR':'M19XR', '19PIC6': 'M19PIC6', '19XRPIC5':'M19XRPIC5',
                       '19XL':'M19XL', '23XL':'M23XL', '23XRV': 'M23XRV', '32XR': 'M32XR', '19XRD':'M19XRD', '19XRE':'M19XRE', '19XRV':'M19XRV'}

        try:
            xpath = eval("PostStartPageLocators." + eval("self."+self.prefix[Data['Model']]+"_swrite[0]"))
            xpath = self.find_elements(*xpath)
            for i in range(len(eval("self."+self.prefix[Data['Model']]+"_swrite"))):
                if "_Default" not in eval("self."+self.prefix[Data['Model']]+"_swrite[i]"):
                    self.checklist.write_similar_element(xpath= xpath, index= eval("PostStartPageLocators." + eval("self."+self.prefix[Data['Model']]+"_swrite[i]")), Data= Data)
                    print('Written Post Start data to ' + str(eval("self."+self.prefix[Data['Model']]+"_swrite[i]")) \
                           + ' =', Data['testdata'])
        except IndexError as e:
            print(e.message)

        # count = 0
        # for ele in range(len(xpath)):
        #     try:
        #         xpath[ele].send_keys(Data['testdata'])
        #         xpath[ele].send_keys(Keys.ENTER)
        #         print eval("self." + self.prefix[Data['Model']] + "_swrite[count]"), ele
        #         count = count + 1
        #     except:
        #         pass

        for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_tog'))):
            if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'yes':
                xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
                self.checklist.click(xpath, page_locators="PostStartPageLocators")
                print('Written Poststart data of ' + xpath + ' =', 'yes')

        # for i in range(len(eval("self." + self.prefix[Data['Model']] + "_writables"))):
        #     xpath = eval("PreStartPageLocators." + eval("self." + self.prefix[Data['Model']] + "_writables[i]"))
        #     self.checklist.write(xpath, Data)
        #     print 'Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_writables[i]") + ' =', \
        #     Data['testdata']


    def read_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("PostStartPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="PostStartPageLocators", index_assert=5)
                assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:5]), True)
                print('Read Poststart Information(' + ele + ')' + ' =', value)

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="PostStartPageLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == 'true', True)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value == None, True)
            print('Read Poststart Information of '+ ele+' = ', value)

        # for ele in eval("self."+self.prefix[Data['Model']]+"_writables"):
        #     value = self.checklist.read(ele, None, Data, 'read_normal', page_locators="PreStartPageLocators")
        #     assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:5]), True)
        #     # assertion.assertEqual(value == Data['testdata'], True)
        #     print 'Read Prestart Information(' + ele + ')' + ' =', value

        try:
            for ele in eval("self."+self.prefix[Data['Model']]+"_swrite_no_index"):
                common_xpath = eval("PostStartPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="PostStartPageLocators")
                assertion.assertEqual(value == Data['testdata'],True)
                print('Read Poststart Information(' + ele + ')' + ' =', value)
        except:
            pass

    def read_reset_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("PostStartPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'reset_read', page_locators="PostStartPageLocators", index_assert=5)
                assertion.assertEqual(value == '', True)
                print('Read Poststart Information of ' + ele + ' = ', 'Null')

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="PostStartPageLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == None, True)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value == 'true', True)
            print('Read Poststart Information of ' + ele + ' = ', value)

    def poststart_exit(self):
        self.find_element(*PostStartPageLocators.poststart_exit).click()

    def poststart_save(self):
        self.find_element(*PostStartPageLocators.poststart_save).click()

    def poststart_cancel(self):
        self.find_element(*PostStartPageLocators.poststart_cancel).click()

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