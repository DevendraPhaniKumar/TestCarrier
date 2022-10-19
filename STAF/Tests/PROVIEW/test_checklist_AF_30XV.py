import os, sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils)

import unittest
from Lib_Space.Selenium_Lib.CSTWebPages.LoginPageAPI import LoginPage
from Lib_Space.Selenium_Lib.CSTWebPages.HomePageAPI import HomePage
from Lib_Space.Selenium_Lib.CSTWebPages.ChecklistPage import Checklist
from Lib_Space.Selenium_Lib.CSTWebPages.ChecklistPage import UnitStartUp_30XV
from Lib_Space.Selenium_Lib.CSTWebPages.ConnectPage import ConnectPage

from Lib_Space.Excel2Json import csv2json
from Lib_Space.Selenium_Lib.BaseClass import WebDriver
# from Lib_Space.WinOper_Lib.Windowsapp_oper import WindowApp
from Lib_Space.WinOper_Lib import Winservices
import json
import time


import file_process
from ddt import ddt
file_data_path = os.path.dirname(os.path.abspath(__file__)) + "\\TestData\\"

data_files = ['AF_30XV']
for data_file in data_files:
    csv2json.convert(file_data_path + data_file +r'.csv')

@ddt
class StartupChecklistAutofill(unittest.TestCase):

    def setUp(self):
        print("\n********************************************************************************")
        print("Setup Function - START")
        print("********************************************************************************")
        Winservices.proviewservices()

        self.driver = WebDriver()
        self.driver = self.driver.launch_application()
        self.driver.maximize_window()
        self.loginpage_obj = LoginPage(self.driver)
        self.loginpage_obj.enter_email('udayabhaskar.challa@fs.utc.com')
        self.loginpage_obj.enter_password('Uday@1234')
        self.loginpage_obj.login()
        time.sleep(5)
        homepage_obj = HomePage(self.driver)
        homepage_obj.user_info()
        self.driver.refresh()

        time.sleep(5)
        print("********************************************************************************")
        print("Setup Function - END")
        print("********************************************************************************")

    # @file_data(file_data_path + data_files[0] + r'.json')
    def test_design_info(self):
        #DM launch
        conn_type = "CCN"
        CCN_name = 'test CCN'
        controller_name = "30XV_PIC: 30XV - 0, 1"

        ccn_Data={"CCN_Name": CCN_name, "DM_load_type": "Double-click", "DM_launch_mode": "offline"}
        connection_page = ConnectPage(self.driver)
        connection_page.enter_page(self.driver, 'CCN')
        connection_page.select_ccnid(ccn_Data)
        time.sleep(2)
        connection_page.launch_device_manager(ccn_Data)
        time.sleep(3)
        connection_page.app_launch_mode(ccn_Data['DM_launch_mode'])
        time.sleep(2)
        homepage_obj = HomePage(self.driver)
        homepage_obj.home_homeicon()

        try:
            from Lib_Space.WPF_Lib import DeviceManager
            dm_obj = DeviceManager.DeviceManager_fun(CCN_name, controller_name)
            time.sleep(5)
            dm_obj.ConnectCCN()
            time.sleep(5)
            dm_obj.upload_controller_cont(controller_name)
            time.sleep(10)
            dm_obj.controller_config_export(controller_name)
            time.sleep(10)
            dm_obj.close_app()
        except Exception as error:
            print (error)
            # dm_obj = DeviceManager.DeviceManager_fun(CCN_name, controller_name)
            time.sleep(5)
            dm_obj.close_app()
        # rename exported configuration file to 30XV_PIC_CCN.csv and place it test data folder

        dwn_path = r"C:\Users\thumati.yk\Downloads"
        file_obj = file_process.CCN_file()
        file_obj.get_ccn_file(controller_name,dwn_path)

        with open(file_data_path + data_files[0] + r'.json') as inputfile:
            Data = json.load(inputfile)
        print('\nTesting :: Checklist :: Startup Form :: 30XV :: Unit Start Up')
        checklist_obj = Checklist.ChecklistPage(self.driver)
        checklist_obj.goto_checklist()
        controller_name = "30XV_PIC : 30XV - 0, 1"
        # Autofill config
        checklist_obj.goto_autofill_cfg(conn_type, CCN_name, controller_name)
        time.sleep(3)

        print ("*"*5,"Creating New form","*"*5)
        checklist_obj.goto_new_form()
        checklist_obj.job_name('Startup30XV')
        checklist_obj.job_no('ABC1')
        checklist_obj.cust_name('test30XV')
        checklist_obj.address('HRDC')
        checklist_obj.model_no('30XV')
        checklist_obj.serial_no('123')
        checklist_obj.create_form('Startup Checklist')
        unitstartup_obj = UnitStartUp_30XV.UnitStartUp_30XV(self.driver)
        checklist_obj.goto_menu(Data["TestCases1"]["Data"], "UnitStartUp_locators", "unitstartup")

        for key in list(Data.keys()):
            checklist_obj.goto_submenu(Data[key]["Data"], "UnitStartUp_locators", Data[key]["Data"]["Model"])
            print("Performing Autofill")
            unitstartup_obj.autofill()
            print("Validating autofill points")
            try:
                unitstartup_obj.read_autofill_data(Data[key]["Data"])
            except Exception as e:
                print(e)
            unitstartup_obj.unitstartup_savesubmenu()
        unitstartup_obj.unitstartup_savemainmenu()
        checklist_obj.save_form()
        print("Performing Checklist PDF export")
        checklist_obj.export_from()
    def tearDown(self):
        print("********************************************************************************")
        print("Teardown Function - START")
        print("********************************************************************************")
        self.driver.refresh()
        time.sleep(10)
        try:
            homepage_obj = HomePage(self.driver)
            homepage_obj.user_logout()
        except Exception as error:
            print(error)
        web_drv = WebDriver()
        web_drv.close_session()
        print("********************************************************************************")
        print("Teardown Function - END")
        print("********************************************************************************")

    def Configlog_Autofill(self):
        print(" Executing 30XV checklist autofill")
        self.setUp()
        self.test_design_info()
        self.tearDown()