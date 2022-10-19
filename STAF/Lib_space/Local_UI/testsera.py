# from selenium import webdriver
# import configparser
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
# from selenium.common.exceptions import TimeoutException
import time
import unittest
import os
from Lib_space.PIC6_API import pic6_api_link

class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        pic6_api_link.Timer(120)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)



# dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# TestParameters = configparser.ConfigParser()
# TestParameters.read(dirnameutils + "\\Utilities\\parameter_connectedservice.ini")

# from Lib_Space.Connectivity.Sierra_Router import SierraConfiguration
#
#
#
# class PIC_6():
#         def ABC(self):
#                 obj = SierraConfiguration()
#                 data = obj.test_sierra_smart_configuration()
#                 print(data)
#                 IPAddress = data[0]
#                 Subnet_Mask = data[1]
#                 Gateway_IP = data[2]
#                 Gateway_Mask = data[3]
#                 DSN1 = data[4]
#                 DSN2 = data[5]
#
#                 print(IPAddress)
#                 print(Subnet_Mask)
#                 print(Gateway_IP)
#                 print(Gateway_Mask)
#                 print(DSN1)
#                 print(DSN2)



# time.sleep(5)


# A = PIC_6()
# A.ABC()

