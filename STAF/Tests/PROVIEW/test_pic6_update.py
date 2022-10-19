#from asyncore import file_dispatcher
import os, sys
import HtmlTestRunner as HT
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
dirnameutils = (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
#sys.path.append(dirnameutils + "\Selenium_POM")
#dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils)
#sys.path.append(dirnameutils + "\Lib_space")
#sys.path.append(dirnameutils + "\Lib_space\Selenium_Lib")
print(dirnameutils)

import unittest
from Lib_space.Selenium_Lib.CSTWebPages.LoginPageAPI import *
from Lib_space.Selenium_Lib.CSTWebPages.HomePageAPI import *
from Lib_space.Selenium_Lib.CSTWebPages.ConnectPage import ConnectPage
from Lib_space.Selenium_Lib.CSTWebPages.ChillerSettingsPage import *
from Lib_space.Selenium_Lib.BaseClass import WebDriver
import time
import datetime
from ddt import ddt,data,unpack,file_data
import json
from Lib_space.Excel2Json import csv2json
from Lib_space.WinOper_Lib import Winservices
from Lib_space.WinOper_Lib.Windowsapp_oper import WindowApp
file_data_path = os.path.dirname(os.path.abspath(__file__)) + "\\TestData\\"
print("My file to be in this location "+file_data_path)
data_files = ['pic6_update']
for data_file in data_files:
    csv2json.convert(file_data_path + data_file +r'.csv')

#@ddt
class FirmwareUpdateTest(unittest.TestCase):
    
    def setUp(self):
        print("\n********************************************************************************")
        print("Setup Function - START")
        print("********************************************************************************")

        # launch Proview services -->        client service & comm services
        Winservices.proviewservices()
        self.driver = WebDriver()
        self.driver = self.driver.launch_application()
        self.driver.maximize_window()
        loginPage = LoginPage(self.driver)
        loginPage.enter_email('devendra.manepalli@carrier.com')
        loginPage.enter_password('Carrier@123')
        loginPage.login(0)

        print("********************************************************************************")
        print("Setup Function - END")
        print("********************************************************************************")

 #  @file_data(file_data_path + data_files[0] + r'.json')
    def test_data(self):
        print(file_data_path)
        with open(file_data_path + data_files[0] + r'.json') as inputfile:
            Data = json.load(inputfile)
          
        homepage = HomePage(self.driver)
        homepage.user_info()
        self.driver.refresh()
        time.sleep(5)
        homepage.home_fwupdate('PIC 6')

        for key in list(Data.keys()):
            Iter = Data[key]["Data"]
            print("\n\nTest Data: ", key, Iter)
            Iter['Pass_wd'] = '113'
            try:
                if homepage.pic6_login(Iter):
                    print("Login Failed")
                    continue
                time.sleep(2)
                homepage.pic6_status()
                time.sleep(2)
                status= homepage.update_pic6(Iter)
                print("The Status is:",+(status))
                if  status ==0:
                    continue
                if status == 1:
                    print("PIC6 update failed")
                if status == 2: 
                    print ("Date/mismatch found , syncing date/time from Device manager")
                    CCN_name = 'test CCN'
                    controller_name = "30XV_PIC: 30XV - 0, 1"
                    ccn_Data = {"CCN_Name": CCN_name, "DM_load_type": "Double-click", "DM_launch_mode": "online"}

                    homepage_obj.home_homeicon()
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
                    time.sleep(3)
                    app = WindowApp()
                    app.app_maximize(CCN_name)
                    try:
                        from Lib_space.WPF_Lib import DeviceManager
                        dm_obj = DeviceManager.DeviceManager_fun(CCN_name, controller_name)
                        dm_obj.ConnectCCN()
                        time.sleep(3)
                        dm_obj.date_time_broadcast(controller_name)
                        time.sleep(3)
                        dm_obj.close_app()
                    except Exception as error:
                        print(error)
                        dm_obj.close_app()

                    homepage.home_fwupdate('PIC 6')

            except Exception as Error:
                print("Update Failed, Error: ",Error)
            time.sleep(2)
            try:
                homepage.pic6_logout()
            except Exception as error:
                print("Logout failed , error:",error)
                self.driver.refresh()
                time.sleep(5)
                homepage.home_homeicon()
                time.sleep(5)
                homepage.home_fwupdate('PIC 6')
            time.sleep(3)
        
    def tearDown(self):
        #homepage = HomePage(self.driver)
        #stopping the timer count
        #tock=homepage.stoptime()
        #print(tock)
        #Time Counting Operation
        #if self.tock-self.tick>0:
            # Print the Difference Minutes and Seconds
        #print(f"Build finished in {(self.tock - self.tick)/60:0.0f} minutes {(self.tock - self.tick)%60:0.0f} seconds")
            # For additional Precision
        #print(f"Build finished in {self.tock - self.tick:0.4f} seconds")
        print("********************************************************************************")
        print("Teardown Function - START")
        print("********************************************************************************")
        self.driver.refresh()
        time.sleep(10)
        homepage = HomePage(self.driver)
        
        homepage.user_logout()
        web_drv = WebDriver()
        web_drv.close_session()
        print("********************************************************************************")
        print("Teardown Function - END")
        print("********************************************************************************")


    def pic6update(self):
        print('*'*10,"\n Executing PIC6 update\n",'*'*10)
        self.setUp()
        self.test_data()
        self.tearDown()
        
if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(FirmwareUpdateTest)
    #unittest.TextTestRunner(verbosity=1).run(suite)
    unittest.main(testRunner=HT.HTMLTestRunner(output=r'C:\E2E_HVAC_Testing\STAF\TestReports'))
    #c=FirmwareUpdateTest
    #c.pic6update()
