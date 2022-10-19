from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import unittest
import pyodbc
import re
import os
import sys
#import cympy
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils + "\LibSpace")
sys.path.append(dirnameutils + "\LibSpace\Connectivity")
from lib_common_operations import CommonOperations
from test_IoT_Module import IotModule                   # error red mark will be shown - not a issue - it works
from test_rw_class_len_module import LenModule          # error red mark will be shown - not a issue - it works
# from test_rw_class_ccn_module import CcnModule          # error red mark will be shown - not a issue - it works

iot = IotModule()
len_p = LenModule()
# ccn_p = CcnModule()


class ParameterWrite(unittest.TestCase):

    def setup(self):
        pass

    def p_write(self, mac_address_of_device="00:02:52:02:17:9F", ccn_point_name='lcdw_sp', cs_point_name='Heating LCDW Setpoint', cs_point_value=40.0):

        driver = CommonOperations.open_carrier_smart(self)

        # Searching for chiller based on MAC address
        serial_number_of_device = CommonOperations.search_chiller(self, driver, mac_address_of_device)

        # Finding the serial number
        # Finding the serial number and correct chiller
        CommonOperations.click_and_open_chiller(self, driver, serial_number_of_device)

        CommonOperations.click_and_open_section_details(self, driver)

        CommonOperations.open_configuration_section(self, driver)

        CommonOperations.set_analog_metric_value(self, driver, cs_point_name, cs_point_value)

        success_save_message_xpath = driver.find_element_by_xpath("(//*[@class ='messages'])/ul/li")
        close_button = driver.find_element_by_xpath("//div[@class='buttonContainer']//div//button[@id='btn_Close']")

        success_save_message_text = success_save_message_xpath.text
        print("Message - ", success_save_message_text)
        close_button.click()

        # No CCN point hence this method need to tried later only....

        #ccn_point_value = len_p.ccn_handle.CCN_ReadTablePoint(ccn_point_name)
        #print(ccn_point_name, "  -  ", ccn_point_value)
        self.assertEqual('Point updated successfully.', success_save_message_text,
                         "Comparing the strings for POINT UPDATE")
        #self.assertEqual(ccn_point_value, cs_point_value, "Comparism of value in PIC6 and value updated from Carrier Smart")

    def tearDown(self):
        #driver.close()
        pass

