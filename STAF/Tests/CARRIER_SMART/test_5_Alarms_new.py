from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import os
import time
import unittest
import re
import datetime
import pyodbc
#from test_rw_class_len_module import LenModule          # error red mark will be shown - not a issue - it works
from Automation_Suite.LibSpace.Connectivity.ClassAlarms_new import Alarms
from Automation_Suite.LibSpace.SELENIUM.BaseClass import WebDriver
from Automation_Suite.LibSpace.Connectivity.ClassLogin import Login
#from Automation_Suite.LibSpace.SELENIUM.BaseClass import WebDriver
#from Automation_Suite.LibSpace.SELENIUM.Pages_Actions.CarrierSmart.Connectivity.Connectivty_PageAction import Connectivity
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils + "\LibSpace")
sys.path.append(dirnameutils + "\LibSpace\Connectivity")

#len_p = LenModule()


class TestCases(unittest.TestCase):

    #global driver
    #driver= WebDriver.same_driver
    #webpagedriver = Login(driver)
    #webpagedriver.login(webpagedriver)

    def setup(self):
        print("*** 1. Choose/Change correct device Mac Address ***")
        print("*** 2. Choose/Change correct database name in database connection and get_serial_number function ***")
        print("*** 3. Choose/Change the correct URL/Environment of Carrier Smart ***")
        print("*** 4. Chooses/Change correct user login credentials in Login function***")
        driver = WebDriver.same_driver
        webpagedriver = Login(driver)
        webpagedriver.login(webpagedriver)

    def test_generate_alarm(self):
        for x in range(10):
            Alarms.generate_alarm(mac_address_of_device="A0F6FD296CCA", alarm_point_name='COOL_EWT',
                           cs_alarm_description='OAT Thermistor', alarm_point_value=250.0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
