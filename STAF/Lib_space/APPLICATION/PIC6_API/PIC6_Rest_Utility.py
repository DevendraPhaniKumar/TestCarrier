import os
import sys
from Lib_space.APPLICATION.PIC6_API import PIC6_Rest_API
Rest = PIC6_Rest_API.Rest_API()
import time
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# print(dirnameutils)

import unittest
assertions = unittest.TestCase('__init__')
import configparser

TestParameters = configparser.ConfigParser()
TestParameters.read(dirnameutils + "\\Data\\APPLICATION\\Test_Parameters.ini")


# Factory = TestParameters.get("TEST_PARAMETERS", "Factory")

class Rest_Utility():

    def setup(self):
        Rest.init('https://169.254.1.1')
        TestParameters.read(dirnameutils + "\\Data\\APPLICATION\\Test_Parameters.ini")
        password = TestParameters.get("TEST_PARAMETERS", "factory")
        # print(password)
        status = Rest.login('factory', password)
        return status

    def ss_rest_read(self, pointname):
        self.setup()
        pntVal = Rest.read(pointname)
        self.teardown()
        return pntVal

    def ss_rest_read_check(self, pointname, expected):
        self.setup()
        pntVal = Rest.read(pointname)
        assertions.assertEqual(pntVal, expected)
        print(pointname + ":  verification done")
        self.teardown()
        return pntVal

    def ss_rest_read_check_until(self, pointname, expected):
        self.setup()
        timer = 0
        while True:
            pntVal = Rest.read(pointname)
            if pntVal == expected:
                assertions.assertEqual(pntVal, expected)
                print(pointname + ":  verification done")
                break
            else:
                time.sleep(1)
                timer = timer + 1
                if timer >= 300:
                    assertions.assertEqual(pntVal, expected)
                    break
                else:
                    pass
        self.teardown()
        return pntVal

    def ss_rest_read_Neg_check(self, pointname, expected):
        self.setup()
        pntVal = Rest.read(pointname)
        assertions.assertNotEqual(pntVal, expected)
        self.teardown()
        return pntVal

    def ss_rest_write(self, pointname, value):
        # global value_w
        value_w = value
        self.setup()
        pntVal = Rest.write(pointname, value)
        self.teardown()
        return pntVal

    def monitor_req_time(self):
        self.setup()
        try:
            pntVal = Rest.get_monitor_task()
            e_time = pntVal["date_time"]
            dt = datetime.utcfromtimestamp(e_time)
        except:
            time.sleep(2)
            pntVal = Rest.get_monitor_task()
            e_time = pntVal["date_time"]
            dt = datetime.utcfromtimestamp(e_time)
        self.teardown()
        return dt

    def offset_Time(self):
        self.setup()
        try:
            pntVal = Rest.get_monitor_task()
            offset = pntVal["time_offset"]
        except:
            pntVal = Rest.get_monitor_task()
            offset = pntVal["time_offset"]
        self.teardown()
        return offset

    def teardown(self):
        Rest.logout()
        return "tear down success"


# Z = Rest_Utility()
# print(Z.ss_rest_write("PLTSPRT_eth1_dhcp_sel","1"))
# time.sleep(5)
# print(Z.ss_rest_read("TEMP_SPACETMP"))
