import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(dirnameutils + "\Lib_Space")
# sys.path.append(dirnameutils + "\Lib_Space\Selenium_Lib")
'''
import unittest
from Lib_Space.Selenium_Lib.CSTWebPages.LoginPageAPI import LoginPage
from Lib_Space.Selenium_Lib.CSTWebPages.HomePageAPI import HomePage
from Lib_Space.Selenium_Lib.CSTWebPages.ChecklistPage import Checklist
from Lib_Space.Selenium_Lib.CSTWebPages.ChecklistPage import PreliminaryEquipCheck
from ddt import ddt,data,unpack,file_data
from Lib_Space.Excel2Json import csv2json
from Lib_Space.Selenium_Lib.BaseClass import WebDriver
import time
# file_data_path = os.path.dirname(os.path.abspath(__file__)) + "\\TestData\\"
#
# data_files = ['startup_preliminaryequipchecklist_30XV']
# for data_file in data_files:
#     csv2json.convert(file_data_path + data_file +r'.csv')
#     print(file_data_path + data_file)
#
# @ddt
class StartupChecklist(unittest.TestCase):

    def setUp(self):
        print("\n********************************************************************************")
        print("Setup Function - START")
        print("********************************************************************************")
        self.driver = WebDriver()
        self.driver = self.driver.launch_application()

        self.loginpage_obj = LoginPage(self.driver)
        self.loginpage_obj.enter_email('udayabhaskar.challa@fs.utc.com')
        self.loginpage_obj.enter_password('Uday@1234')
        self.loginpage_obj.login()

        homepage_obj = HomePage(self.driver)
        user_name = homepage_obj.user_info()
        # print "Logged in by user: ", user_name
        # app_name, version_info = homepage_obj.app_info()
        # print "Testing: ", app_name, "\nVersion: ", version_info
        self.driver.refresh()
        print("********************************************************************************")
        print("Setup Function - END")
        print("********************************************************************************")

    # @file_data(file_data_path + data_files[0] + r'.json')
    def test_design_info(self):#, Data):
        Data = {'JobName': 'Startup Checklist', 'JobNumber': '30XV', 'CustomerName': 'test30XV', 'Address': 'HRDC',
                'Model': "30XV", 'SerialNo': '12687s5777', "FormType": 'Startup Checklist', 'testdata': '1A2B@3456*xyz78gh910X','Checklist index':'4'}
        print('\nTesting :: Checklist :: Startup Form :: '+ Data['Model'] +' :: PreStart')
        checklist_obj = Checklist.ChecklistPage(self.driver)
        time.sleep(5)
        checklist_obj.goto_checklist()
        checklist_obj.goto_new_form()
        checklist_obj.job_name(Data['JobName'])
        checklist_obj.job_no(Data['JobNumber'])
        checklist_obj.cust_name(Data['CustomerName'])
        checklist_obj.address(Data['Address'])
        checklist_obj.model_no(Data['Model'])
        checklist_obj.serial_no(Data['SerialNo'])
        checklist_obj.create_form(Data["FormType"])
        preliminaryequipcheck_obj = PreliminaryEquipCheck.PreliminaryEquipCheck(self.driver)
        checklist_obj.goto_menu(Data, "PreliminaryEquipCheckPageLocators", "preliminaryequipcheck")
        preliminaryequipcheck_obj.write_prelim_info_data(Data)
        preliminaryequipcheck_obj.preliminaryequipcheck_save()
        checklist_obj.save_form()
        checklist_obj.search_form(Data)
        # checklist_obj.email_existing_form(Data)
        # checklist_obj.export_from()
        checklist_obj.edit_existing_form(Data)
        checklist_obj.goto_menu(Data, "PreliminaryEquipCheckPageLocators", "preliminaryequipcheck")
        preliminaryequipcheck_obj.read_data(Data)
        checklist_obj.reset()
        preliminaryequipcheck_obj.read_reset_data(Data)
        checklist_obj.save_section()
        # checklist_obj.delete_form(Data)



    def tearDown(self):
        print("********************************************************************************")
        print("Teardown Function - START")
        print("********************************************************************************")
        self.driver.refresh()
        time.sleep(10)
        homepage_obj = HomePage(self.driver)
        # homepage_obj.home_homeicon()
        homepage_obj.user_logout()
        web_drv = WebDriver()
        web_drv.close_session()

        print("********************************************************************************")
        print("Teardown Function - END")
        print("********************************************************************************")

    def Startup_Preliminary(self):
        print(" Executing PIC6 Primilinary Checklist form")
        self.setUp()
        self.test_design_info()
        self.tearDown()
