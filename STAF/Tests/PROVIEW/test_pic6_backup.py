import os
import sys
#sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
#dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dirnameutils = (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
#sys.path.append(dirnameutils + "\Selenium_POM")
#dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils)
print(dirnameutils)
# '''
# dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(dirnameutils + "\Lib_space")
# sys.path.append(dirnameutils + "\Lib_space\Selenium_Lib")
# '''
import unittest
from Lib_space.Selenium_Lib.CSTWebPages.LoginPageAPI import *
from Lib_space.Selenium_Lib.CSTWebPages.HomePageAPI import *
from Lib_space.Selenium_Lib.Page_locators.HomePage_locatars import HomePageLocatars
from Lib_space.Selenium_Lib.CSTWebPages.ConnectPage import *
from Lib_space.Selenium_Lib.BaseClass import WebDriver
import time
import selenium
# import datetime
import json
from ddt import ddt
from Lib_space.Excel2Json import csv2json
from Lib_space.WinOper_Lib import Winservices
from Lib_space.WinOper_Lib.Windowsapp_oper import WindowApp
file_data_path = os.path.dirname(os.path.abspath(__file__)) + "\\TestData\\"

data_files = ['pic6_backup']


for data_file in data_files:
    csv2json.convert(file_data_path + data_file + r'.csv')


@ddt
class backupTest(unittest.TestCase):
    def setUp(self):
        print("\n********************************************************************************")
        print("Setup Function - START")
        print("********************************************************************************")
        # Winservices.proviewservices()

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
        # conn_type = "CCN"
        CCN_name = '30XV'
        controller_name = "PIC6:30XV-0,1"
        ccn_Data = {"CCN_Name": CCN_name, "DM_load_type": "Double-click", "DM_launch_mode": "online"}
        connection_page = ConnectPage(self.driver)
        connection_page.enter_page(self.driver, 'CCN')
        try:
            connection_page.select_ccnid(ccn_Data)
            connection_page.launch_device_manager(ccn_Data)
            time.sleep(3)
            connection_page.app_launch_mode(ccn_Data['DM_launch_mode'])

        except Exception as e:
            print(" DM launch failure error: ", e)

        homepage_obj = HomePage(self.driver)
        time.sleep(5)
        homepage_obj.home_homeicon()
        #

        try:
            from Lib_space.WPF_Lib import DeviceManager
            dm_obj = DeviceManager.DeviceManager_fun(CCN_name, controller_name)

            dm_obj.ConnectCCN()
            time.sleep(3)
            dm_obj.upload_controller_cont(controller_name)
            time.sleep(3)
            dm_obj.controller_config_export(controller_name)
            time.sleep(3)
            dm_obj.DisConnectCCN()
            time.sleep(2)
            dm_obj.close_app()
        except Exception as error:
            print(error)
            dm_obj.close_app()

        homepage.home_fwupdate('PIC 6')
        time.sleep(2)
        fw_p=Data['TestCases1']["Data"]['upload_path']
        nvm_file = fw_p + '\\BACKUP.nvmcfg'
        if os.path.exists(nvm_file):
            print(f"{nvm_file} already exist. Deleting the file...")
            os.remove(nvm_file)
        app = WindowApp()
        app.app_close('Downloads')
        for key in list(Data.keys()):
            Iter = Data[key]["Data"]
            print("\n\nTest Data: ", key, Iter)
            Iter['Pass_wd'] = '113'
            # print("Test Data: ",key, Iter)

            try:
                if homepage.pic6_login(Iter):
                    print("Login Failed")
                    continue
                time.sleep(2)
                # homepage.pic6_status()
                # time.sleep(2)
                homepage.pic6_logfile_upload(Iter)
            except Exception as error:
                print("PIC6 backup failed, Error:", error)
            try:
                homepage.pic6_logout()
            except Exception as error:
                print("Logout failed , error:", error)
                self.driver.refresh()
                time.sleep(5)
                homepage.home_homeicon()
                time.sleep(5)
                homepage.home_fwupdate('PIC 6')
            #
            time.sleep(5)


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

    def pic6backup(self):
        print(" Executing PIC6 upload")
        self.setUp()
        self.test_data()
        self.tearDown()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(backupTest)
    unittest.TextTestRunner(verbosity=1).run(suite)
    #unittest.main(testRunner=HT.HTMLTestRunner(output=dirnameutils))
    #c=backupTest()
    #c.pic6backup()