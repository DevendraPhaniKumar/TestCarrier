import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils + "\Lib_space")
sys.path.append(dirnameutils + "\Lib_space\Selenium_Lib")
'''
import unittest
from Lib_space.Selenium_Lib.CSTWebPages.LoginPageAPI import *
from Lib_space.Selenium_Lib.CSTWebPages.HomePageAPI import *
from Lib_space.Selenium_Lib.CSTWebPages.ChillerSettingsPage import *
from Lib_space.Selenium_Lib.BaseClass import WebDriver
import time
import datetime
from ddt import ddt,data,unpack,file_data
from Lib_space.Excel2Json import csv2json
import json
file_data_path = os.path.dirname(os.path.abspath(__file__)) + "\\TestData\\"

data_files = ['pic6_restore']


for data_file in data_files:
    csv2json.convert(file_data_path + data_file +r'.csv')

@ddt
class RestoreTest(unittest.TestCase):
    def setUp(self):
        print("\n********************************************************************************")
        print("Setup Function - START")
        print("********************************************************************************")

        # self.driver = WebDriver(sec_Enable =0)
        self.driver = WebDriver()
        self.driver = self.driver.launch_application()
        self.driver.maximize_window()
        loginPage = LoginPage(self.driver)
        loginPage.enter_email('udayabhaskar.challa@fs.utc.com')
        loginPage.enter_password('Uday@1234')
        loginPage.login(0)

        print("********************************************************************************")
        print("Setup Function - END")
        print("********************************************************************************")

    # @file_data(file_data_path + data_files[0] + r'.json')
    def test_data(self):
        with open(file_data_path + data_files[0] + r'.json') as inputfile:
            Data = json.load(inputfile)

        homepage = HomePage(self.driver)
        homepage.user_info()
        self.driver.refresh()
        time.sleep(5)
        homepage.home_fwupdate('PIC 6')

        for key in list(Data.keys()):
            Iter = Data[key]["Data"]
            print("Test Data: ", key, Iter)
            Iter['Pass_wd']='ie68uxek'
            try:
                if homepage.pic6_login(Iter):
                    print ("Login Failed")
                    continue
                time.sleep(2)
                # homepage.pic6_status()
                # time.sleep(2)
                if homepage.pic6_file_download(Iter):
                    try:
                        homepage.pic6_logout()
                    except Exception as error:
                        print("Logout failed , error:", error)
            except Exception as Err:
                print("Download Failed, Error:",Err)
                self.driver.refresh()
                time.sleep(5)
                homepage.home_homeicon()
                time.sleep(5)
                homepage.home_fwupdate('PIC 6')
            time.sleep(3)

    def tearDown(self):
        print("********************************************************************************")
        print("Teardown Function - START")
        print("********************************************************************************")
        self.driver.refresh()
        time.sleep(10)
        homepage = HomePage(self.driver)

        # homepage_obj.home_homeicon()
        homepage.user_logout()
        web_drv = WebDriver()
        web_drv.close_session()
        print("********************************************************************************")
        print("Teardown Function - END")
        print("********************************************************************************")

    def pic6restore(self):
        print(" Executing PIC6 download")
        self.setUp()
        self.test_data()
        self.tearDown()

if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(FirmwareUpdateTest)
    #unittest.TextTestRunner(verbosity=1).run(suite)
    #unittest.main(testRunner=HT.HTMLTestRunner(output=dirnameutils))
    c=RestoreTest()
    c.pic6restore()
