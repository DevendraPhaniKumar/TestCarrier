from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import sys
import os
import time
import unittest
import pyodbc
import re
import datetime
from Lib_space.SELENIUM.BaseClass import WebDriver,Page
from Tests.CARRIER_SMART.lib_common_operations import CommonOperations

#from lib_common_operations import CommonOperations      # error red mark will be shown - not a issue - it works
#from test_rw_class_len_module import LenModule          # error red mark will be shown - not a issue - it works

#bacnet = ClassBacnetModule()

#len_p = LenModule()


class Alarms(unittest.TestCase, Page):

    global delay

    def __init__(self, webdriver):
        global driver
        super(Alarms, self).__init__(webdriver)
        driver = WebDriver

    def generate_alarm(self,mac_address_of_device="AlarmTest03052018Barman", alarm_point_name='BRGI_T',
                           cs_alarm_description='Sensor Fault - Economizer Pressure', alarm_point_value=200.0):

        # send alarm value to PIC6
        #len_p.vir_sim_instance.VirSim_Write(alarm_point_name, alarm_point_value)
        #temp = len_p.ccn_handle.CCN_ReadVarVal(alarm_point_name)
        #print("Alarm Point Value written to Device", temp)
        alarm_generation_date = datetime.date.today().strftime("%B %#d, %Y")
        print("alarm generated DATE in device = ", alarm_generation_date)
        alarm_generation_time = (datetime.datetime.now().strftime("%I:%M%p")[:-1].lstrip("0").replace("0", " ")).lower()
        print("alarm generated TIME in device = ", alarm_generation_time)

        #  open Carrier Smart
        #driver = CommonOperations.open_carrier_smart(self)
       # ClassLogin.Login(self, driver)

        # Searching for chiller based on MAC address
        serial_number_of_device = CommonOperations.search_chiller(mac_address_of_device)

        # Finding the serial number and correct chiller
        CommonOperations.click_and_open_chiller(driver, serial_number_of_device)

        alarm_type_selector_xpath = "//div[@class='alarmTypeSelector']"
        CommonOperations.locate_element(driver, alarm_type_selector_xpath)

        # locate the alarms block
        chiller_alarms_xpath = "//div[@class='alarmTypeSelector']/div[1]/div[1]"
        CommonOperations.locate_element(driver, chiller_alarms_xpath)
        chiller_alarms = self.driver.find_element_by_xpath(chiller_alarms_xpath)
        total_no_of_alarms = 0
        for i in range(2):
            try:
                chiller_alarms.click()
                y = re.split('(\d+)', chiller_alarms.text)
                total_no_of_alarms = int(y[1])
                print("total_no_of_alarms in string format = ", total_no_of_alarms)
            except StaleElementReferenceException as ex:
                print("Message: stale element reference: element 'chiller_alarms' is not attached to the page document", ex)
            print("for loop i =", i)

        # sort chiller alarms desc
        simple_grid_alarm_xpath = "(//*[@class ='simpleGrid'])[1]/div[1]/span[3]"
        CommonOperations.locate_element(driver, simple_grid_alarm_xpath)
        simple_grid_alarm = driver.find_element_by_xpath(simple_grid_alarm_xpath)
        #simple_grid_alarm.click()
        time.sleep(2)
        #simple_grid_alarm.click()
        # Get Alarm details Based on Alarm Text
        #   #  alarm_desc = driver.find_element_by_xpath("//span[contains(text(),'"+cs_alarm_description+"')]")
        cs_alarm_date, cs_alarm_time = CommonOperations.get_alarm_details(self, driver, total_no_of_alarms, cs_alarm_description)

        self.assertEqual(alarm_generation_date, cs_alarm_date)

        expected, actual = CommonOperations.get_date_time_split(self,alarm_generation_time, cs_alarm_time)
        self.assertEqual(expected[4], actual[4]) # verify AM - PM
        self.assertAlmostEqual(int(expected[1]), int(actual[1]), delta=1)  # verify the hours
        self.assertAlmostEqual(int(expected[3]), int(actual[3]), delta=8)  # verify the minutes
