import unittest
import time
import os
import sys
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils + "\Lib_space")
sys.path.append(dirnameutils + "\Lib_space\Connectivity")

from Lib_space.Connectivity.lib_common_operations import CommonOperations      # error red mark will be shown - not a issue - it works
from Lib_space.Connectivity.test_rw_class_len_module import LenModule          # error red mark will be shown - not a issue - it works
#from Lib_Space.Connectivity.test_rw_class_ccn_module import CcnModule          # error red mark will be shown - not a issue - it works

#bacnet = ClassBacnetModule()

len_p = LenModule()
#ccn_p = CcnModule()


class Telemetry(unittest.TestCase):

    def setup(self):
        pass

    def periodic_telemetry(self, mac_address_of_device="00:02:52:02:17:9F", vs_point_name='ECW', cs_point_name='Entering Chilled Water', vs_point_value=40.0, vs_point_reset_value=80.0, periodicity=1):

        len_p.vir_sim_instance.VirSim_Write(vs_point_name, vs_point_value)

        driver = CommonOperations.open_carrier_smart(self)

        # Searching for chiller based on MAC address
        serial_number_of_device = CommonOperations.search_chiller(self, driver, mac_address_of_device)

        # Finding the serial number and correct chiller
        CommonOperations.click_and_open_chiller(self, driver, serial_number_of_device)

        CommonOperations.click_and_open_section_details(self, driver)

        #CommonOperations.click_and_open_evaporator_section(self, driver)
        print("Waiting for telemetry time period - ", periodicity)
        time.sleep(periodicity)

        metric_name, metric_value = CommonOperations.get_analog_metric_name_value(self, driver, cs_point_name)

        len_p.vir_sim_instance.VirSim_Write(vs_point_name, vs_point_reset_value)

        self.assertEqual(cs_point_name, metric_name, "Comparing the point name")
        #self.assertEqual(vs_point_value, metric_value, "Comparing of point telemetry value")

    def cov_telemetry(self, mac_address_of_device="00:02:52:02:17:9F", vs_point_name='ECW', cs_point_name='Entering Chilled Water', vs_point_value=40.0, vs_point_reset_value=80.0):
        # update value to PIC6 device
        #len_p.vir_sim_instance.VirSim_Write(vs_point_name, vs_point_value)

        driver = CommonOperations.open_carrier_smart(self)

        # Searching for chiller based on MAC address
        serial_number_of_device = CommonOperations.search_chiller(self, driver, mac_address_of_device)

        # Finding the serial number and correct chiller
        CommonOperations.click_and_open_chiller(self, driver, serial_number_of_device)

        CommonOperations.click_and_open_section_details(self, driver)

        #CommonOperations.click_open_condenser_section(self, driver)

        time.sleep(10)

        metric_name, metric_value = CommonOperations.get_analog_metric_name_value(self, driver, cs_point_name)

        # Reset value so that can be used in subsequent tests
        #len_p.vir_sim_instance.VirSim_Write(vs_point_name, vs_point_reset_value)

        self.assertEqual(metric_name, cs_point_name, "Comparing the point name")
        self.assertEqual(vs_point_value, metric_value, "Comparing of point telemetry value")

    def temp_cov_telemetry(self):
         # pre condition write to point this point is having telemetry period of 1 min
        vs_point_1_name = 'ECDW'
        cs_point_1_name = 'Entering Condenser Water'
        vs_point_1_test_value = 55.0
        vs_point_1_reset_value = 54.0
        vs_point_2_name = 'LCDW'
        cs_point_2_name = 'Leaving Condenser Water'
        vs_point_2_test_value = 75.0
        vs_point_2_reset_value = 73.0
            # update value to PIC6 device
        len_p.vir_sim_instance.VirSim_Write(vs_point_1_name, vs_point_1_test_value)
        len_p.vir_sim_instance.VirSim_Write(vs_point_2_name, vs_point_2_test_value)

        driver = CommonOperations.open_carrier_smart(self)

        # Searching for chiller based on MAC address
        mac_address_of_device, serial_number_of_device = CommonOperations.search_chiller(self, driver)

        # Finding the serial number and correct chiller
        CommonOperations.click_and_open_chiller(self, driver, serial_number_of_device)

        CommonOperations.click_and_open_section_details(self, driver)

        CommonOperations.click_open_condenser_section(self, driver)
        CommonOperations.locate_element(self, driver, xpath="(//*[@class ='metricStick'])[50]")
        metric_name, metric_value = CommonOperations.get_metric_name_value(self, driver, xpath ="(//*[@class ='metricStick'])[50]/div")

        self.assertEqual(cs_point_1_name, metric_name, "Comparing the first point name")
        self.assertEqual(vs_point_1_test_value, metric_value, "Comparing of first point telemetry value")

        CommonOperations.locate_element(self, driver, xpath="(//*[@class ='metricStick'])[53]")
        metric_name, metric_value = CommonOperations.get_metric_name_value(self, driver, xpath="(//*[@class ='metricStick'])[53]/div")

        self.assertEqual(cs_point_2_name, metric_name, "Comparing the second point name")
        self.assertEqual(vs_point_2_test_value, metric_value, "Comparing of second point telemetry value")

        #test post condition to reset values in points
        len_p.vir_sim_instance.VirSim_Write(vs_point_1_name, vs_point_1_reset_value)
        len_p.vir_sim_instance.VirSim_Write(vs_point_2_name, vs_point_2_reset_value)

    def both_telemetry(self, mac_address_of_device="00:02:52:02:17:9F", vs_point_name='ECW', cs_point_name='Entering Chilled Water', vs_point_value=40.0, vs_point_reset_value=80.0, periodicity=60):

        # update value to PIC6 device
        len_p.vir_sim_instance.VirSim_Write(vs_point_name, vs_point_value)
        print("Point value written to PIC and wait for 30 seconds")
        time.sleep(periodicity/2)
        cnn = CommonOperations.establish_database_connection(self)
        cursor = cnn.cursor()

        my_query = "SELECT DEVICEID FROM DEVICE WHERE RAWMAC = '{0}'"
        cursor.execute(my_query.format(mac_address_of_device))
        device_id = 0
        for device_id in cursor.fetchall():
            print("Device ID = ", device_id[0])
            print("Device ID Type = ", type(device_id[0]))
        device_id = device_id[0]
        print(device_id)

        my_query = "SELECT MODELID FROM DEVICE WHERE RAWMAC = '{0}'"
        cursor.execute(my_query.format(mac_address_of_device))
        model_id = 0
        for model_id in cursor.fetchall():
            print("Model ID = ", model_id[0])
            print("Model ID type = ", type(model_id[0]))
        model_id = model_id[0]
        print(model_id)

        my_query = "SELECT METRICID FROM METRIC WHERE MODELID = {0} and METRICNAME = '{1}'"
        #  '{1}' denotes string and goes as 'abcd'
        print(my_query.format(model_id, cs_point_name))
        # my_query_with_parameters = (my_query.format(model_id, cs_point_name))
        cursor.execute(my_query.format(model_id, cs_point_name))
        metric_id = 0
        for metric_id in cursor.fetchall():
            print("Metric ID = ", metric_id[0])
            print("Metric ID type = ", type(metric_id[0]))
        metric_id = metric_id[0]
        print("Metric ID = ", metric_id)

        #  verifying CoV change value from database
        my_query = "SELECT TOP 1 VALUE FROM HISTORICALVALUE WHERE DEVICEID = {0} AND METRICID = {1} ORDER BY EVENTDATETIME DESC"
        cursor.execute(my_query.format(device_id, metric_id))
        value = 0
        for value in cursor.fetchall():
            print("CoV Value = ", value[0])
            print("CoV Value type = ", type(value[0]))
        value = value[0]
        print("CoV Value = ", value)
        self.assertEqual(value,vs_point_value, "CoV data is received")

        # fetch value after 7 times of periodic telemetry
        print("Waiting for 7 Minutes")
        print(datetime.now())
        time.sleep(periodicity*7)

        my_query = "SELECT TOP 5 EVENTDATETIME FROM HISTORICALVALUE WHERE DEVICEID = {0} AND METRICID = {1} ORDER BY EVENTDATETIME DESC"
        #cursor.execute("SELECT TOP 5 EVENTDATETIME FROM HISTORICALVALUE WHERE DEVICEID = 2299 AND METRICID = 16547 ORDER BY EVENTDATETIME DESC")
        cursor.execute(my_query.format(device_id, metric_id))
        dataList = []  # data is a list and for iteration it gets all 5 datetime
        for data in cursor.fetchall():
            print("EVENTDATETIME = ", data[0])
            print("EVENTDATETIME type = ", type(data[0]))
            dataList.append(data[0][:-7])
        i = 0

        # Reset value so that can be used in subsequent tests
        len_p.vir_sim_instance.VirSim_Write(vs_point_name, vs_point_reset_value)

        # verification of telemetry received
        while i < len(dataList) - 1:
            print(dataList[i])
            sub = datetime.strptime(dataList[i], "%Y-%m-%d %H:%M:%S") - datetime.strptime(dataList[i + 1],
                                                                                          "%Y-%m-%d %H:%M:%S")
            print(sub)
            print(type(sub))
            expected_value = re.sub("[0:]", "", str(sub))
            actual_value = str(int(periodicity/60))
            if expected_value == actual_value: # periodicity is received in seconds
                print("Telemetry data is received")
            i = i + 1
            print("i = ", i)
            self.assertEqual(expected_value,actual_value, "ASSERTION FAIL : Telemetry data is NOT received")

    def tearDown(self):
        pass


