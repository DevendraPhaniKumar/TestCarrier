import os
import sys

from Lib_Space.WinOper_Lib.Windowsapp_oper import WindowApp
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(dirnameutils)
sys.path.append(utils)
# sys.path.append(dirnameutils+'\Selenium_Lib')
from Lib_Space.Selenium_Lib.BaseClass import Page
from Lib_Space.Selenium_Lib.Page_locators.HomePage_locatars import HomePageLocatars
from Lib_Space.Selenium_Lib.Page_locators.ConnectPage_locators import ConnectPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPage_locators import ChecklistPageLocators
from Lib_Space.Selenium_Lib.Page_locators.LoginPage_locatars import LoginPageLocatars
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
# import pandas as pd
# from pandas.testing import assert_frame_equal
import configparser
import time
import datetime
driver = object
delay = 60


class HomePage(Page):
    global driver, delay
    def __init__(self, webdriver):
        global driver
        super(HomePage, self).__init__(webdriver)
        driver = webdriver

    def wait(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, element[-1])))
            # filename1 = "HomePage"
            # self.screen_capture(filename1)
            return 0
        except TimeoutException:
            print("Loading took too much time!")
            # filename1 = "HomePage_error"
            # self.screen_capture(filename1)
            return 1

    def wait_until_visible(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element[-1])))
            filename1 = "HomePage"
            self.screen_capture(filename1)
            return 0
        except TimeoutException:
            print("Loading took too much time!")
            # filename1 = "HomePage_error"
            # self.screen_capture(filename1)
            return 1

    def user_info(self):
        try:
            self.wait(HomePageLocatars.TITLE)
            self.user_license_notify()
            user = self.find_element(*HomePageLocatars.USER).text
            title , release_yr, release_version = self.app_info()
            print('User: ', user.split(',')[-1], "\nApp details: ", "Title:", title ,"Release Yrs:", release_yr, "Version: ",  release_version)
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(2.0)
            self.user_profile("Profile Information")
            print("Role : ", self.find_element(*HomePageLocatars.Role_txt).text)
            self.profile_save()
            time.sleep(2.0)
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        except:
            print("User info button not available.Failed")
        info_app = user.split(',')[-1]
        return info_app
    def user_license_notify(self):
        try:
            self.wait_until_visible(LoginPageLocatars.license_notify)
            print(" License warning: ", self.find_element(*LoginPageLocatars.license_notify).text)
        except:
            print("No license warning found")

    def app_info(self):
        self.find_element(*HomePageLocatars.info_btn).click()
        self.wait(HomePageLocatars.info_title)
        title = self.find_element(*HomePageLocatars.info_title).text
        tool_version = self.find_element(*HomePageLocatars.app_version).text
        return title, tool_version.split('|')[0],tool_version.split('|')[1]

    def user_profile(self, profile_info):
        print("**** User Profile Test **********")
        self.wait(HomePageLocatars.profile_btn)
        self.find_element(*HomePageLocatars.profile_btn).click()
        profile_title = self.find_element(*HomePageLocatars.Profile_title).text
        try:
            assert str(profile_info), profile_title
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", profile_title)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", profile_title)

    def profile_name(self, first, last, First_Name_text, Last_name_text, error_msg):
        print("**** User Profile: Profile Name Test **********")
        first_name = self.find_element(*HomePageLocatars.Profile_FirstName_lbl).text
        try:
            assert (First_Name_text== first_name),"First Name Assertion Failed"
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "First Name Assertion Failed:", first_name)
        self.find_element(*HomePageLocatars.Profile_FirstName_val).clear()
        if first != "":
            self.find_element(*HomePageLocatars.Profile_FirstName_val).send_keys(first)
        last_name = self.find_element(*HomePageLocatars.Profile_LastName_lbl).text
        try:
            assert Last_name_text, last_name
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "LastName Assertion Failed:", last_name)
        self.find_element(*HomePageLocatars.Profile_LastName_val).clear()
        if last != '':
            self.find_element(*HomePageLocatars.Profile_LastName_val).send_keys(last)
        self.find_element(*HomePageLocatars.Save_btn).click()
        try:
            self.wait(str(self.find_element(*HomePageLocatars.First_error_msg).text))
            err_1 = self.find_element(*HomePageLocatars.First_error_msg).text
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Error:", err_1)
            try:
                assert err_1, error_msg
            except:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", error_msg)
        except:
            pass
        try:
            self.wait(HomePageLocatars.LastName_err_msg)
            err_2 = self.find_element(*HomePageLocatars.LastName_err_msg).text
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Error:", err_2)
            try:
                assert err_2, error_msg
            except:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", error_msg)
        except:
            pass
        try:
            self.wait(str(self.find_element(*HomePageLocatars.Update_error_msg).text))
            pass_msg = self.find_element(*HomePageLocatars.Update_error_msg).text
            try:
                assert pass_msg, error_msg
            except:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", error_msg)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Update Message:", error_msg)
        except:
            pass
        first_name_val = self.find_element(*HomePageLocatars.Profile_FirstName_val).text
        try:
            assert first, first_name_val
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", first_name_val)
        last_name_val = self.find_element(*HomePageLocatars.Profile_LastName_val).text
        try:
            assert last, last_name_val
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", last_name_val)

    def profile_mail_id(self, userid_label, userid):
        print("**** User Profile: Profile ID Test **********")
        text = self.find_element(*HomePageLocatars.Profile_UsrName_lbl).text
        try:
            assert text, userid_label
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", userid_label)
        uid = self.find_element(*HomePageLocatars.Profile_UsrName_val).get_attribute('value')
        try:
            assert uid, userid
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", userid)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "UserName:", str(uid))


    def app_language_select(self, lang):
        print("**** User Profile: Profile language Test **********")

        self.find_element(*HomePageLocatars.Language_sel).click()
        self.find_element(*HomePageLocatars.Language_LOE)
        link = driver.find_element_by_link_text(lang)
        link.click()
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
            *HomePageLocatars.Language_lbl).text,self.find_element(*HomePageLocatars.Language_sel).text)
        self.find_element(*HomePageLocatars.Save_btn).click()

    def unit_change(self, unit_type):
        print("**** User Profile: Profile Unit type Test **********")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
            *HomePageLocatars.Unit_type_lbl).text)
        print("Units selected:",unit_type)
        self.find_element(*HomePageLocatars.Unit_type_sel).click()
        self.find_element(*HomePageLocatars.Unit_type_LOE)

        link = driver.find_element_by_link_text(unit_type)
        link.click()
        self.find_element(*HomePageLocatars.Save_btn).click()
        time.sleep(2.0)

    # def license_validation(self, usr_lvl, usrid, validity):
    #     print("**** User Profile: License screen Test **********")
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", usr_lvl, self.find_element(
    #         *HomePageLocatars.License_level).text)
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
    #         *HomePageLocatars.License_Validity).text)
    #     self.find_element(*HomePageLocatars.License_Update_btn).click()
    #     lic_pop_title = self.find_element(*HomePageLocatars.License_Update_title).text
    #     try:
    #         assert "Update License", lic_pop_title
    #     except:
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", lic_pop_title)
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
    #         *HomePageLocatars.License_Update_title).text)
    #     lic_type_lbl = self.find_element(
    #         *HomePageLocatars.License_type_lbl).text
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
    #         *HomePageLocatars.License_type_lbl).text, self.find_element(*HomePageLocatars.License_type_txt).text)
    #     try:
    #         assert usr_lvl, lic_type_lbl
    #     except:
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "License Type Assertion Failed:", \
    #             lic_type_lbl)
    #     lic_usr_lbl = self.find_element(*HomePageLocatars.License_Usr_txt).text
    #     try:
    #         assert usrid, lic_usr_lbl
    #     except:
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", lic_usr_lbl)
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
    #         *HomePageLocatars.License_Usr_lbl).text,self.find_element(*HomePageLocatars.License_Usr_txt).text)
    #     try:
    #         assert (usrid == lic_usr_val), "email Assertion failed"
    #     except:
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed: ", lic_usr_val)
    #         print(datetime.datetime.now().strftime(
    #         "%Y-%m-%d %H:%M"), ": ", "Expect:", usrid, "Actual:", self.find_element(
    #         *HomePageLocatars.License_Usr_txt).text)
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
    #         *HomePageLocatars.License_Expiry_lbl).text , validity, self.find_element(
    #         *HomePageLocatars.License_Expiry_txt).text)
    #     self.find_element(*HomePageLocatars.License_Update_close).click()
    #     self.find_element(*HomePageLocatars.Save_btn).click()

    # def license_activation(self, userid, passwd):
    #     print("**** User Profile: License activation Test **********")
    #     self.find_element(*HomePageLocatars.License_Update_btn).click()
    #     lic_update_title = self.find_element(*HomePageLocatars.License_Update_title).text
    #     try:
    #         assert "Update License", lic_update_title
    #     except:
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", lic_update_title)
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
    #         *HomePageLocatars.License_type_lbl).text)
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "User level:", self.find_element(\
    #         *HomePageLocatars.License_type_txt).text)
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(\
    #         *HomePageLocatars.License_Expiry_lbl).text)
    #     env_key = str(self.find_element(*HomePageLocatars.License_Expiry_lbl).text)
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Env_key", env_key)
    #     admin_portal = OtherPage()
    #     other_driver.otherpage_login('udayabhaskar.challa@fs.utc.com', 'Uday@1234')
    #     # env_key = 'Ym1ZQThLbTN0SzZjZG1BeTN4a2Q4bGtxdDgyTXk1Nm8rSmxMVC9VZk43L3RUOSsrb1ZmY3Vobi8zNDc5eVRpRWxiand4M2U4dGlyWDRjaWJYR09neER0UFp2azF6bTVHTEx2RFBUd2VTT0k9'
    #     lic_key = other_driver.get_activationkey(env_key, userid)
    #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "License_key", lic_key)
    #     self.find_element(*HomePageLocatars.License_key_val).send_keys(lic_key)
    #     self.find_element(*HomePageLocatars.License_apply_btn).click()
    #     try:
    #         self.wait(str(self.find_element(*HomePageLocatars.License_error_msg).text))
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Error msg: ", self.find_element(
    #             *HomePageLocatars.License_error_msg).text)
    #     except:
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "No error")
    #     self.find_element(*HomePageLocatars.License_Update_close).click()
    #     updated_usr_lvl = self.find_element(*HomePageLocatars.License_label).text
    #     if updated_usr_lvl == "Advanced":
    #         print(datetime.datetime.now().strftime(
    #             "%Y-%m-%d %H:%M"), ": ", "License updated and User is updated to Advanced")
    #     else:
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "License update failed", updated_usr_lvl)
    #     self.find_element(*HomePageLocatars.Save_btn).click()

    def profile_save(self):
        try:
            self.find_element(*HomePageLocatars.Save_btn).click()
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
            *HomePageLocatars.Update_error_msg).text)

    def home_screen_test(self):
        # list of elements
        print(datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M"), ": ", "************ Home Screen functions Content*********")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(*HomePageLocatars.HOME).text)
        # validate each feature screen present
        elements = driver.find_elements(*HomePageLocatars.home_screen_content)
        for i in elements:
            print(datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M"), ": ", "Radio button text:", i.text)  # elements.get(i).getAttribute("value")

    def home_chillerinfo(self):
        time.sleep(2.0)
        self.find_element(*HomePageLocatars.home_chillerinfo).click()
        self.wait(HomePageLocatars.Chiller_info_btn)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ": ", "Chiller dashboard")

    def home_connect(self):
        print(datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M"), ": ", "\n************ Connectivity Content*********")
        connectivity_lbl = self.find_element(*HomePageLocatars.home_connectivity).text
        try:
            assert 'Connectivity', connectivity_lbl
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", connectivity_lbl)
        self.find_element(*HomePageLocatars.home_connectivity).click()
        time.sleep(1.0)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
            *ConnectPageLocators.connectivity_TITLE).text)
        element = self.find_element(*ConnectPageLocators.connectivity_icon)
        if element.is_displayed:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Connectivity function present")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def disconnect_ccn(self):

        self.find_element(*HomePageLocatars.home_connectivity).click()
        self.wait(ConnectPageLocators.connectivity_TITLE)
        if self.driver.find_element_by_xpath(
                "//*[@id='content']/div/div[2]/div[1]/div/div/div/div[1]/div/ul/li/button[2]").text == "Disconnect":
            self.driver.find_element_by_xpath(
                "//*[@id='content']/div/div[2]/div[1]/div/div/div/div[1]/div/ul/li/button[2]").click()
        # self.wait(*ConnectPageLocators.connect_message)
        #  msg = self.find_element(*ConnectPageLocators.connect_message).text
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "Device disconnected")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def home_checklist(self):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "\n************ Checklist Content*********")
        time.sleep(1.0)
        checklist_lbl = self.find_element(*HomePageLocatars.home_checklist).text
        try:
            assert 'Checklist', checklist_lbl
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", checklist_lbl)
        self.find_element(*ChecklistPageLocators.checklist).click()
        time.sleep(1.0)
        if self.find_element(*HomePageLocatars.checklist_btn).is_displayed:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Checklist icon is present")
            self.find_element(*ConnectPageLocators.connectivity_icon).click()  # Checklist button validation
            self.find_element(*HomePageLocatars.checklist_btn).click()  # Checklist button validation
            if self.find_element(*ChecklistPageLocators.existing_form).is_displayed:
                print(datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M"), ": ", " Existing form page is present", self.find_element(
                    *ChecklistPageLocators.All_forms).text)
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Existing form page is not loaded")
            if self.find_element(*ChecklistPageLocators.new_form).is_displayed:
                self.find_element(*ChecklistPageLocators.new_form).click()
                print(datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M"), ": ", " New form page is present", self.find_element(
                    *ChecklistPageLocators.create_new_form_text).text)
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " New form page is not loaded")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Checklist Page is not loaded")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def home_Reports(self):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "************ Reports Content*********")
        try:
            assert 'Reports', self.find_element(*HomePageLocatars.home_reports).text
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", self.find_element(
                *HomePageLocatars.home_reports).text)
        self.find_element(*HomePageLocatars.home_reports).click()
        time.sleep(1.0)
        self.find_element(*ConnectPageLocators.connectivity_icon).click()
        if self.find_element(*HomePageLocatars.reports_btn).is_displayed:
            self.find_element(*HomePageLocatars.reports_btn).click()
            if self.find_element(*HomePageLocatars.reports_chart).is_displayed:
                self.find_element(*HomePageLocatars.reports_chart).click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Report menu is present")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Reports page is not loaded")
            if self.find_element(*HomePageLocatars.reports_trend_cfg).is_displayed:
                self.find_element(*HomePageLocatars.reports_trend_cfg).click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Trend page is present")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Trend page is not loaded")
            if self.find_element(*HomePageLocatars.reports_trace_history).is_displayed:
                self.find_element(*HomePageLocatars.reports_trace_history)
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Trace History page is present")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Trace History is not loaded")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", " Report Page is not loaded")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def home_fwupdate(self,control):
        print("************ Firwmare update/File Transfer Content*********")
        self.find_element(*HomePageLocatars.home_fwupdate).click()
        time.sleep(2.0)
        if self.find_element(*HomePageLocatars.firmware_update_btn).is_displayed:
            self.find_element(*HomePageLocatars.firmware_update_btn).click()
            assert 'Firmware Update/File Transfer', self.find_element(*HomePageLocatars.firmware_update_text).text
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Firmware Update button is present")
            # self.find_element(*HomePageLocatars.home_fwupdate).click()
            time.sleep(2.0)
            self.wait(HomePageLocatars.firmware_update_text)
            self.find_element(*HomePageLocatars.update_control_sel_btn).click()
            self.find_elements(*HomePageLocatars.update_control_sel_loe)
            element = self.driver.find_element_by_link_text(control)
            element.click()
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Firmware Update page is not present")
        # self.find_element(*HomePageLocatars.Home_btn).click()

    def pic5_file_xfer(self,ip_addr,usr_name='root',pass_wd='rootpasswd'):
        print('**** PIC5 File transfer*****')
        self.wait(HomePageLocatars.file_pic5_title)
        usr_lbl = self.find_element(*HomePageLocatars.file_pic5_usr_lbl).text
        assert (usr_lbl == 'User Name:*'), 'User Name label doesnot match'
        pass_lbl = self.find_element(*HomePageLocatars.file_pic5_passwd_lbl).text
        assert (pass_lbl == 'Password:*'), 'Password label doesnot match'
        ip_lbl = self.find_element(*HomePageLocatars.file_pic5_ip_addr_lbl).text
        assert (ip_lbl == 'Host Address:'), 'Device ip label doesnot match'
        print("Username:", self.find_element(*HomePageLocatars.file_pic5_usr_in).get_attribute('value'))
        self.find_element(*HomePageLocatars.file_pic5_usr_in).clear()
        time.sleep(1.0)
        self.find_element(*HomePageLocatars.file_pic5_usr_in).send_keys(usr_name)
        print("Password:",self.find_element(*HomePageLocatars.file_pic5_passwd_in).get_attribute('value'))
        self.find_element(*HomePageLocatars.file_pic5_passwd_in).clear()
        time.sleep(1.0)
        self.find_element(*HomePageLocatars.file_pic5_passwd_in).send_keys(pass_wd)
        print("Host Address:",self.find_element(*HomePageLocatars.file_pic5_ip_addr_in).get_attribute('value'))
        self.find_element(*HomePageLocatars.file_pic5_ip_addr_in).send_keys(ip_addr)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ","Download black box")
        self.find_element(*HomePageLocatars.file_pic5_blackbox_download_btn).click()
        try:
            self.wait(HomePageLocatars.file_pic5_view_files)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
                *HomePageLocatars.file_pic5_view_files).text)
            self.find_element(*HomePageLocatars.file_pic5_view_files).click()
        except:
            if (self.wait(HomePageLocatars.file_pic5_download_msg)=='0'):
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ",self.find_element(
                *HomePageLocatars.file_pic5_download_msg).text)
        print("Download Config file")
        self.find_element(*HomePageLocatars.file_pic5_cfg_download_btn).click()
        try:
            self.wait(HomePageLocatars.file_pic5_view_files)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
                *HomePageLocatars.file_pic5_view_files).text)
            self.find_element(*HomePageLocatars.file_pic5_view_files).click()
        except:
            if self.wait(HomePageLocatars.file_pic5_download_msg)=='0':
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", self.find_element(
                *HomePageLocatars.file_pic5_download_msg).text)

    def pic6_login(self,Data):
        print('**** PIC6 login*****\n',)
        ip_addr =Data['ip_addr']
        usr_name = Data['usr_name']
        pass_wd =Data['Pass_wd']
        self.wait(HomePageLocatars.update_pic6_deviceip_lbl)
        ip_lbl = self.find_element(*HomePageLocatars.update_pic6_deviceip_lbl).text
        assert (ip_lbl == 'Device IP:*'), 'Device ip label doesnot match'
        usr_lbl = self.find_element(*HomePageLocatars.update_pic6_usr_lbl).text
        assert (usr_lbl == 'User Name:*'), 'User Name label doesnot match'
        pass_lbl = self.find_element(*HomePageLocatars.update_pic6_passwd_lbl).text
        assert (pass_lbl == 'Password:*'), 'Password label doesnot match'
        try:
            self.find_element(*HomePageLocatars.update_pic6_deviceip_in).clear()
            self.find_element(*HomePageLocatars.update_pic6_usr_in).clear()
            self.find_element(*HomePageLocatars.update_pic6_passwd_in).clear()
            time.sleep(2)
            self.find_element(*HomePageLocatars.update_pic6_deviceip_in).send_keys(ip_addr)
            self.find_element(*HomePageLocatars.update_pic6_usr_in).send_keys(usr_name)
            self.find_element(*HomePageLocatars.update_pic6_passwd_in).send_keys(pass_wd)
            login_btn = self.find_element(*HomePageLocatars.update_pic6_login_btn)
            if (login_btn.is_enabled()):
                login_btn.click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), " Login clicked ")
                # time.sleep(5)
                try:
                    print("Waiting for PIC6 home screen")
                    if self.wait(HomePageLocatars.update_file_path_lbl):
                        print (self.find_element(*HomePageLocatars.update_file_path_lbl).text)
                    elif self.wait(HomePageLocatars.update_login_err):
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), " ", "Login error:", self.find_element(
                            *HomePageLocatars.update_login_err).text)
                        return 1
                except Exception as error:
                    print(f"Login exception error:\n {error}")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),"\tDevice ip/ username/ Password Field are blank; Enter valid input")
                return 1
        except Exception as loginErr:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),"Login exception :\n",loginErr)
        # check for error message
        try:
            self.find_element(*HomePageLocatars.update_pic6_logout_btn).text
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Login Successful with PIC6")
            return 0
        except:
            print ("Checking for login error")
            if self.wait(HomePageLocatars.update_login_err) ==1 :
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), " ", "Login failed")
                return 1


    def pic6_logout(self):
        print('*'*5,'PIC6 logout','*'*5,)
        # if self.find_element(*HomePageLocatars.update_pic6_login_btn).is_displayed():
        #     print(" PIC 6 logged out already")
        #     return
        # else:
        try:
            if self.wait_until_visible(HomePageLocatars.update_pic6_logout_btn)==0:
                self.find_element(*HomePageLocatars.update_pic6_logout_btn).click()
                time.sleep(10)
            if self.wait_until_visible(HomePageLocatars.update_pic6_login_btn)==0:
                print (datetime.datetime.now().strftime("\n%Y-%m-%d %H:%M:%S"),"logout successful")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")," Logout failed")
        except Exception as error:
            print (datetime.datetime.now().strftime("\n%Y-%m-%d %H:%M:%S"),f"logout exception occured {error} \nRefreshing PIC6 page")

            self.find_element(*HomePageLocatars.update_pic6_logout_btn).click()
            time.sleep(3)
            self.driver.refresh()
            time.sleep(5)
            self.home_homeicon()
            time.sleep(5)
            self.home_fwupdate('PIC 6')

    def update_pic5(self,fw_path,fw_file):
        self.wait(HomePageLocatars.update_title)
        current_ver_title = self.find_element(*HomePageLocatars.update_current_ver_lbl).text
        current_ver = self.find_element(*HomePageLocatars.update_current_ver).text
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", current_ver_title, "- ", current_ver)
        self.find_element(*HomePageLocatars.update_btn).click()
        os.chdir(fw_path)
        os.system(HomePageLocatars.autoit_exec_path_sserivce + "" + str(fw_file))

    def update_pic6(self,Data):
        print('**** PIC6 update*****')
        # self.wait(HomePageLocatars.update_pic6_update_tab_title)
        self.find_element(*HomePageLocatars.update_pic6_update_tab_btn).click()
        time.sleep(2)
        fw_p =Data["file_path"]
        file_n=Data["xfer_file"]
        kp_cfg=Data["keep_cfg"]
        oper=Data["operation"]
        update_erase =Data['update_erasecfg']
        print("FilePath: ",fw_p,file_n)
        self.find_element(*HomePageLocatars.update_pic6_fw_file).click()
        time.sleep(2)
        self.file_sel(fw_p, file_n)
        if self.find_element(*HomePageLocatars.update_pic6_fw_file).text != '':
            print("Selected file: ",self.find_element(*HomePageLocatars.update_pic6_fw_file).text)
        else:
            print("File is not selected")
            return 1
        # self.wait(HomePageLocatars.update_login_loader)
        time.sleep(3)
        try:
            self.wait(HomePageLocatars.update_pic6_fw_menifest_content)
            menifest = self.find_element(*HomePageLocatars.update_pic6_fw_menifest_content).text
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ","File contents:\n",menifest)

            # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ","Keep Configuration option\n",self.find_element(*HomePageLocatars.update_pic6_fw_kp_cfg_lbl).text)
            if(kp_cfg=='yes'):
                if self.find_element(*HomePageLocatars.update_pic6_fw_kp_cfg_chk).is_enabled():
                    print (" Configuration will be intact")
            else:
                self.find_element(*HomePageLocatars.update_pic6_fw_kp_cfg_chk).send_keys(Keys.SPACE)
                print(" Configuration will be erased")

            if (oper == "continue"):

                if self.find_element(*HomePageLocatars.update_pic6_fw_menifest_update).is_displayed():
                    self.find_element(*HomePageLocatars.update_pic6_fw_menifest_update).click()
                time.sleep(2)# check for error msgs :date/time mistmactch or connection abort
                if self.find_element(*HomePageLocatars.update_pic6_fw_erase_cfg_pop_msg).is_displayed():
                    time.sleep(2)

                    print("Erase configuration Warning:\n",
                          self.find_element(*HomePageLocatars.update_pic6_fw_erase_cfg_pop_msg).text)
                    if update_erase == 'yes':
                        self.find_element(*HomePageLocatars.update_pic6_fw_erase_cfg_pop_update).click()
                    else:
                        self.find_element(*HomePageLocatars.update_pic6_fw_erase_cfg_pop_cancel).click()
                        time.sleep(1)
                        self.find_element(*HomePageLocatars.update_pic6_fw_menifest_cancel).click()
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ",
                              "Update Operation cancelled")
                        return

                try:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ": ", self.find_element(
                        *HomePageLocatars.update_pic6_download_progress_lbl).text)

                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "\t Download duration ", self.find_element(*HomePageLocatars.update_pic6_fw_duration_msg).text)

                    while 1:
                        try:
                            stat_val = self.find_element(*HomePageLocatars.update_pic6_download_progress_val).text
                            sts_per = stat_val.strip('%')
                            if not(sts_per == ''):
                                print(datetime.datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S"), ": ", "file download progress", sts_per)
                            elif (self.find_element(*HomePageLocatars.update_pic6_fw_error).text):
                                print("Update error: \n",self.find_element(*HomePageLocatars.update_pic6_fw_error).text)
                                self.find_element(*HomePageLocatars.update_pic6_fw_hw_err_accept).click()
                                return 1
                            else:
                                break
                            time.sleep(2.0)
                        except Exception as download_eerr:
                            print(" FIle download exception: ",download_eerr)
                            break
                    while 1:
                        try:
                            stat_val = self.find_element(*HomePageLocatars.update_pic6_update_progress_val).text
                            sts_per = stat_val.strip('%')
                            if (self.find_element(*HomePageLocatars.update_pic6_fw_error).text):
                                print("UPdate error:\n",self.find_element(*HomePageLocatars.update_pic6_fw_error).text)
                                self.find_element(*HomePageLocatars.update_pic6_fw_hw_err_accept).click()
                                return 1
                            elif not (sts_per == "100"):
                                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ": ", "update progress", \
                          sts_per)
                            else:
                                break
                            time.sleep(2.0)
                        except Exception as update_err:
                            print("FIle update exception :\n",update_err)
                            break
                    if(self.wait(HomePageLocatars.update_pic6_fw_success_msg)==0):
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": Update success",\
                            self.find_element(*HomePageLocatars.update_pic6_fw_success_msg).text)
                        self.find_element(*HomePageLocatars.update_pic6_fw_success_msg_accept).click()
                        self.wait(HomePageLocatars.update_login_loader)
                        time.sleep(120)
                        return 0
                    elif self.find_element(*HomePageLocatars.update_pic6_fw_file_error):
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ",self.find_element(*HomePageLocatars.update_pic6_fw_file_error).text)
                        self.find_element(*HomePageLocatars.update_pic6_fw_success_msg_accept).click()
                    else:
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ","message not found")
                except:
                    try:
                        if self.find_element(*HomePageLocatars.update_pic6_fw_connection_abort_msg).text:
                            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Err Msg: ",self.find_element(*HomePageLocatars.update_pic6_fw_connection_abort_msg).text)
                            self.find_element(*HomePageLocatars.update_pic6_fw_connection_abort_msg_accept).click()
                    except Exception as e:
                        print(f"UPdate error message exception {e}")
                    try:
                        if self.find_element(*HomePageLocatars.update_pic6_fw_dt_error).text:
                            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Err Msg: ",\
                                  self.find_element(*HomePageLocatars.update_pic6_fw_dt_error).text)
                            self.find_element(*HomePageLocatars.update_pic6_fw_dt_accept).click()
                            return 2
                    except Exception as e:
                        print(f"UPdate error message exception {e}")
                    try:
                        if self.find_element(*HomePageLocatars.update_pic6_fw_hw_error).text:
                            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Err Msg: ",
                              self.find_element(*HomePageLocatars.update_pic6_fw_hw_error).text)
                            self.find_element(*HomePageLocatars.update_pic6_fw_hw_err_accept).click()
                    except Exception as e:
                        print(f"UPdate error message exception {e}")
                    else:
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "message not found")
                    return 1
            else:
                self.find_element(*HomePageLocatars.update_pic6_fw_menifest_cancel).click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Update Operation cancelled")
        except Exception as Error:
            try:
                if self.find_element(*HomePageLocatars.update_pic6_fw_menifest_content).is_displayed():
                    menifest = self.find_element(*HomePageLocatars.update_pic6_fw_menifest_content).text
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Err Msg: ", menifest)
                    self.find_element(*HomePageLocatars.update_pic6_fw_menifest_err_accept).click()
            except Exception as e:
                print(f"UPdate error message exception {e}")
            try:
                if self.find_element(*HomePageLocatars.update_pic6_fw_connection_abort_msg).text:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Err Msg: ",
                          self.find_element(*HomePageLocatars.update_pic6_fw_connection_abort_msg).text)
                    self.find_element(*HomePageLocatars.update_pic6_fw_connection_abort_msg_accept).click()
            except Exception as e:
                print(f"UPdate error message exception {e}")
            # try:
            #     if self.find_element(*HomePageLocatars.update_pic6_fw_dt_error).text:
            #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Err Msg: ", \
            #               self.find_element(*HomePageLocatars.update_pic6_fw_dt_error).text)
            #         self.find_element(*HomePageLocatars.update_pic6_fw_dt_accept).click()
            # except Exception as e:
            #     print(f"UPdate error message exception {e}")
            # try:
            #     if self.find_element(*HomePageLocatars.update_pic6_fw_hw_error).text:
            #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Err Msg: ",
            #               self.find_element(*HomePageLocatars.update_pic6_fw_hw_error).text)
            #         self.find_element(*HomePageLocatars.update_pic6_fw_hw_err_accept).click()
            # except Exception as e:
            #     print(f"UPdate error message exception {e}")
            # else:
            #     print("Updated failed with Error:",Error)
            return 1


    def pic6_status(self):
        print('*'*5,"PIC6 current status",'*'*5)
        self.find_element(*HomePageLocatars.update_pic6_status_tab_btn).click()
        time.sleep(2)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), " PIC6 status:\n ", self.find_element(*HomePageLocatars.update_pic6_status_txt).text)
        time.sleep(5)
        self.find_element(*HomePageLocatars.update_pic6_iot_refresh).click()
        time.sleep(2)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), " PIC6 status after refresh:\n ",
              self.find_element(*HomePageLocatars.update_pic6_status_txt).text)

    def pic6_logfile_upload(self,Data):
        print('**** PIC6 file transfer*****')
        # fw_p, file_n, oper, kp_cfg, ip_addr, usr_name, pass_wd, xfer_update,file_sel

        # Filepath
        fw_p = Data['upload_path']
        file_sel =Data['file_type']
        oper= Data["operation"]
        print(f"File upload type: {file_sel} \t FilePath: {fw_p}\t Operation:{oper} " )
        if self.find_element(*HomePageLocatars.update_pic6_filepath_cancel_btn).is_displayed():
            print("Warning: File path operation is not properly terminated")
            self.find_element(*HomePageLocatars.update_pic6_filepath_cancel_btn).click()
            time.sleep(1)
            self.find_element(*HomePageLocatars.update_pic6_filepath_edit_btn).click()
        else:
            self.find_element(*HomePageLocatars.update_pic6_filepath_edit_btn).click()
        self.find_element('xpath', '//*[@id="txt_Default_PIC6_Upload"]').clear()
        time.sleep(1)
        self.find_element('xpath','//*[@id="txt_Default_PIC6_Upload"]').send_keys(fw_p)
        time.sleep(1)
        self.find_element(*HomePageLocatars.update_pic6_filepath_save_btn).click()
        try:
            self.wait(HomePageLocatars.update_pic6_save_pop_ok_btn)
            warn= self.find_element('xpath','//*[@id="commonMsgModal"]/div/div/div/div[2]').text
            if warn == "Saved successfully":
                print("File path selected: ",
                      self.find_element('xpath', '//*[@id="txt_Default_PIC6_Upload"]').get_attribute('value'))
            else:
                print("Error: ", self.find_element('xpath', '//*[@id="commonMsgModal"]/div/div/div/div[2]').text)
                self.find_element('xpath','//*[@id="commonMsgModal"]/div/div/div/div[3]/ul/li/a').click()
                time.sleep(2)
                self.find_element(*HomePageLocatars.update_pic6_filepath_cancel_btn).click()
                return 1
            self.find_element(*HomePageLocatars.update_pic6_save_pop_ok_btn).click()

        except:
            print (" Save dialog not found")
        time.sleep(2)

        self.wait(HomePageLocatars.update_pic6_file_upload_tab_btn)
        self.find_element(*HomePageLocatars.update_pic6_file_upload_tab_btn).click()
        if self.wait_until_visible(HomePageLocatars.update_pic6_upload_lang_loe)==1:
            self.find_element(*HomePageLocatars.update_pic6_file_upload_tab_btn).click()
        ActionChains(self.driver).send_keys(Keys.CONTROL,Keys.SUBTRACT).perform()
        time.sleep(2)
        #set upload file type
        try:
            if file_sel =="Retrieve Language file":
                list_option =Select(self.find_element(*HomePageLocatars.update_pic6_upload_lang_loe))
                list_option.select_by_visible_text(str(Data["Lang"]))
                self.pic6_upload_button(1)
            if (file_sel =='all files upload'):
                # assert self.find_element('xpath','//*[@id="collapseOne"]/div[1]/div[2]/div[1]/span[1]/strong[1]').text=='All logs (for engineering purposes)'
                check_box = self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div[1]/div[2]/div[1]/input[1]')
                if check_box.is_selected():
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Option is already checked:", \
                        file_sel)
                else:
                    check_box.send_keys(Keys.SPACE)

                self.pic6_upload_button(nopop=file_sel)
                check_box.send_keys(Keys.SPACE)
                #status msg
            elif (file_sel=='Retrieve Equipment Data Recorder'):
                # assert (str(self.find_element('xpath', '//*[@id="collapseOne"]/div[1]/div[1]/div[1]/div[2]').text) == "Retrieve Equipment Data Recorder (blackbox) (.csv)\ndelete"),\
                #     "Selected file doesn't match"
                check_box= self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div[1]/div[1]/div[1]/div[2]/input[1]')
                if check_box.is_selected():
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Option is already checked:",\
                        file_sel)
                else:
                    check_box.send_keys(Keys.SPACE)
                if oper=="delete":
                    if self.find_element(*HomePageLocatars.update_pic6_delete_btn).is_enabled():
                        self.find_element(*HomePageLocatars.update_pic6_delete_btn).click()
                    else:
                        print ("Warning: Delete button is not enabled")
                    self.wait('//*[@id="deletecon"]')
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ",self.find_element('xpath','//*[@id="deletecon"]').text)
                    self.find_element('xpath', '//*[@id="deletemodal"]/div/div/div/div[3]/ul/li/a').click()
                else:
                    self.pic6_upload_button()
                    check_box.send_keys(Keys.SPACE)
            elif (file_sel=='Retrieve Configuration Data Backup'):
                # assert (self.find_element('xpath',
                #                          '//*[@id="collapseOne"]/div[1]/div[1]/div[1]/div[1]').text == 'Retrieve Configuration Data (Backup) (.nvmcfg)'),\
                #     "Selected file doesn't match"
                check_box = self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div[1]/div[1]/div[1]/div[1]/input[1]')

                if check_box.is_selected():
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Option is already checked:", \
                        file_sel)
                else:
                    check_box.send_keys(Keys.SPACE)
                time.sleep(1)
                self.pic6_upload_button(nopop=file_sel)
                time.sleep(1)
                check_box = self.driver.find_element_by_xpath(
                    '//*[@id="collapseOne"]/div[1]/div[1]/div[1]/div[1]/input[1]')

                check_box.send_keys(Keys.SPACE)

            elif (file_sel=='Retrieve Trends'):
                # assert str(self.find_element('xpath',
                #                           '//*[@id="collapseOne"]/div[1]/div[1]/div[1]/div[3]').text) == 'Retrieve Trends (.csv)', \
                #     "Selected file doesn't match"
                check_box = self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div[1]/div[1]/div[1]/div[3]/input[1]')
                if check_box.is_selected():
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Option is already checked:", \
                        file_sel)
                else:
                    check_box.send_keys(Keys.SPACE)
                # self.find_element('xpath', '//*[@id="collapseOne"]/div[1]/div[5]/div[3]/button[2]').click()
                self.pic6_upload_button()
                check_box = self.driver.find_element_by_xpath(
                    '//*[@id="collapseOne"]/div[1]/div[1]/div[1]/div[3]/input[1]')
                check_box.send_keys(Keys.SPACE)
            elif (file_sel=='Retrieve Application Logs'):
                # assert str(self.find_element('xpath',
                #                           '//*[@id="collapseOne"]/div/div[3]/div/div[1]').text) == 'Retrieve Application Logs', \
                #     "Selected file doesn't match"
                check_box = self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[3]/div/div[1]/input')
                if check_box.is_selected():
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Option is already checked:", \
                        file_sel)
                else:
                    check_box.send_keys(Keys.SPACE)
                self.pic6_upload_button()
                check_box.send_keys(Keys.SPACE)

            elif (file_sel=='Retrieve License Information'):
                # assert str(self.find_element('xpath',
                #                           '//*[@id="collapseOne"]/div/div[4]/div/div[2]').text) == 'Retrieve License Information', \
                #     "Selected file doesn't match"
                check_box = self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/div/div[2]/input')
                if check_box.is_selected():
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Option is already checked:", \
                        file_sel)
                else:
                    check_box.send_keys(Keys.SPACE)
                self.pic6_upload_button()
                check_box.send_keys(Keys.SPACE)
            elif(file_sel=='Retrieve Platform Configuration'):
                # assert str(self.find_element('xpath',\
                #                           '//*[@id="collapseOne"]/div/div[4]/div/div[1]').text )== 'Retrieve Platform Configuration', \
                #     "Selected file doesn't match"
                check_box = self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/div/div[1]/input')
                if check_box.is_selected():
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Option is already checked:", \
                        file_sel)
                else:
                    check_box.send_keys(Keys.SPACE)
                self.pic6_upload_button()
                check_box.send_keys(Keys.SPACE)

            elif (file_sel=='Retrieve Platform Log Files'):
                # assert (self.find_element('xpath',
                #                           '//*[@id="collapseOne"]/div/div[3]/div/div[2]').text == 'Retrieve Platform Log Files'), \
                #     "Selected file doesn't match"
                check_box = self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[3]/div/div[2]/input')
                if check_box.is_selected():
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Option is already checked:", \
                        file_sel)
                else:
                    check_box.send_keys(Keys.SPACE)
                self.pic6_upload_button(nopop=file_sel)
                check_box.send_keys(Keys.SPACE)
            elif (file_sel=='Retrieve IOT Log Files'):
                # assert (self.find_element('xpath',
                #                           '//*[@id="collapseOne"]/div/div[4]/div/div[2]').text == 'Retrieve '
                #                                                                                'IOT Log Files'), \
                #     "Selected file doesn't match"
                check_box = self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[3]/div/div[3]/input')
                if check_box.is_selected():
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Option is already checked:", \
                        file_sel)
                else:
                    check_box.send_keys(Keys.SPACE)
                self.pic6_upload_button()
                check_box.send_keys(Keys.SPACE)
        except Exception as Error:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), " PIC6 upload failed , Error:",Error)
        time.sleep(2)
        self.find_element(*HomePageLocatars.update_pic6_file_upload_tab_btn).click()

    def pic6_upload_button(self, lang=0,nopop=None):
        if not(lang):
            btn_en = self.find_element('xpath', '//*[@id="collapseOne"]/div[1]/div[5]/div[3]/button[2]')
            if btn_en.text =='Upload':
                btn_en.click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "Log file Upload button clicked")
            else:
                print("Please select valid option")
            # uncheck file selection box
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), " Upload language button clicked")

            self.find_element(*HomePageLocatars.update_pic6_upload_lang_btn).click()
        # loader for status

        self.wait(HomePageLocatars.update_login_loader)

        if nopop =='Retrieve Configuration Data Backup':
            time.sleep(20)
            app = WindowApp()
            app.app_close('PIC6_data')
            return
        elif nopop == 'all files upload' or nopop == 'Retrieve Platform Log Files':
            time.sleep(30)
        else:
            time.sleep(5)
        app = WindowApp()
        app.app_close('PIC6_data')

        try:
            self.wait('//*[@id="uploadfailmodal"]/div/div/div')
            txt=self.find_element('xpath', '//*[@id="uploadcon"]/ul').text

            if "success" not in txt.lower():
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "Download failed: ", txt)
                self.find_element('xpath', '//*[@id="uploadfailmodal"]/div/div/div/div[3]/ul/li/a').click()
                self.find_element(*HomePageLocatars.update_pic6_file_upload_tab_btn).click()
                self.pic6_logout()
                return 1
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "Uploaded files Successful, Uploaded file content: ",
                      self.find_element('xpath', '//*[@id="uploadcon"]/ul').text)
            self.find_element('xpath', '//*[@id="uploadfailmodal"]/div/div/div/div[3]/ul/li/a').click()

            time.sleep(2)
            # ActionChains(self.driver).send_keys(Keys.ALT, Keys.TAB).perform()
            if self.wait_until_visible(HomePageLocatars.update_pic6_file_upload_tab_btn)==1:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),  "Not able come back to PIC6 screen")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), 'popup closed')

            # Add text validation
        except:
            self.wait('//*[@id="uploadcon"]/h5')
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Upload failed: ", \
                  self.find_element('xpath', '//*[@id="uploadcon"]/h5').text)
            self.find_element('xpath', '//*[@id="uploadfailmodal"]/div/div/div/div[3]/ul/li/a').click()
        time.sleep(2)


    def pic6_file_download (self,Data ):
        print("PIC 6 File Download")
        fw_p =Data["file_path"]
        file_n = Data["xfer_file"]
        file_sel=Data["file_type"]
        print(f"File download type: {file_sel}, {file_n}\t ")

        self.wait(HomePageLocatars.update_pic6_file_download_tab_btn)
        self.find_element(*HomePageLocatars.update_pic6_file_download_tab_btn).click()
        time.sleep(3)
        if self.wait_until_visible(HomePageLocatars.update_pic6_download_btn)==1:
            self.find_element(*HomePageLocatars.update_pic6_file_download_tab_btn).click()
        try:
            if (file_sel == 'nvm_restore'):
                assert str(self.find_element('xpath',
                                          '//*[@id="collapseTwo"]/div/div[1]/div/div[1]/label').text) == 'Restore Configuration Data(*.nvmcfg)', \
                    "Selected option doesn't match"
                self.find_element('xpath','//*[@id="collapseTwo"]/div/div[1]/div/div[1]/input').click()
                element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(HomePageLocatars.update_pic6_download_file_sel))
                # don't click on the element, just send the path directly
                element.send_keys(fw_p  + file_n)
                self.find_element(*HomePageLocatars.update_pic6_download_btn).click()
                time.sleep(2)

                # self.driver.switch_to_alert()
                try:
                    if self.find_element('xpath', '//*[@id="nvmFileConfirm"]/div/div/div/div[2]/div/p').text:
                        if Data['reboot'] == 'yes':
                            print("Reboot after download selected as Yes")
                            self.find_element('xpath', '//*[@id="nvmFileConfirm"]/div/div/div/div[3]/ul/li[1]/a').click()

                        else:
                            self.find_element('xpath', '//*[@id="nvmFileConfirm"]/div/div/div/div[3]/ul/li[2]/a').click()
                            print("Reboot after download selected as No")
                            return 1
                except Exception as error:
                    if self.find_element('xpath','//*[@id="downloadfailmodal"]/div/div/div/div').is_displayed():
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "File error: ",self.find_element('xpath','//*[@id="downloadfailmodal"]/div/div/div/div[2]').text)
                        self.find_element('xpath','//*[@id="downloadfailmodal"]/div/div/div/div[3]/ul/li/a').click()

                    return 1
            elif (file_sel == 'language_download'):
                print("Language file download")
                assert str(self.find_element('xpath',
                                          '//*[@id="collapseTwo"]/div/div[1]/div/div[2]/label').text) == 'Language(*.csv)', \
                    "Selected option doesn't match"
                self.find_element('xpath', '//*[@id="collapseTwo"]/div/div[1]/div/div[2]/input').click()
                element = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(HomePageLocatars.update_pic6_download_file_sel))
                # don't click on the element, just send the path directly
                element.send_keys(fw_p  + file_n)
                time.sleep(2)
                self.find_element(*HomePageLocatars.update_pic6_download_btn).click()
                time.sleep(4)
                try:
                    if self.find_element('xpath','//*[@id="langUploadConfirm"]/div/div/div/div[2]/div/p').text:
                        print(self.find_element('xpath','//*[@id="langUploadConfirm"]/div/div/div/div[2]/div/p').text)
                        if Data['reboot'] == 'yes':
                            print("Selected reboot as yes")
                            self.find_element('xpath', '//*[@id="langUploadConfirm"]/div/div/div/div[3]/ul/li[1]/a').click()
                        else:
                            self.find_element('xpath', '//*[@id="langUploadConfirm"]/div/div/div/div[3]/ul/li[2]/a').click()
                            print("Selected reboot as no")
                            return 1
                except Exception as Err:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Reboot dialog error",Err)
                    self.find_element(*HomePageLocatars.update_pic6_file_download_tab_btn).click()
                    return 1
            elif (file_sel == 'soft_key download'):
                assert (self.find_element('xpath',
                                          '//*[@id="collapseTwo"]/div/div[1]/div/div[3]/label').text == 'Software Protection Key(*.txt)'), \
                    "Selected option doesn't match"
                self.find_element('xpath', '//*[@id="collapseTwo"]/div/div[1]/div/div[3]/input').click()
                # self.find_element(*HomePageLocatars.update_pic6_download_file_sel).click()
                element = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(HomePageLocatars.update_pic6_download_soft_file_sel))
                # don't click on the element, just send the path directly
                element.send_keys(fw_p + file_n)
                self.find_element(*HomePageLocatars.update_pic6_download_btn).click()
            elif (file_sel == 'ssl_download'):
                assert (self.find_element('xpath',
                                          '//*[@id="collapseTwo"]/div/div[1]/div/div[4]/label').text == 'SSL Certification (*.pem)'), \
                    "Selected option doesn't match"
                self.find_element('xpath', '//*[@id="collapseTwo"]/div/div[1]/div/div[4]/input').click()
                # self.find_element(*HomePageLocatars.update_pic6_download_file_sel).click()
                element = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(HomePageLocatars.update_pic6_download_ssl_file_sel))
                # don't click on the element, just send the path directly
                element.send_keys(fw_p + file_n)
                self.find_element(*HomePageLocatars.update_pic6_download_btn).click()
            try:
                # self.driver.switch_to_alert()
                self.wait('//*[@id="downloadcon"]')
                txt= self.find_element('xpath', '//*[@id="downloadcon"]').text
                if "success" not in txt.lower():
                    print ("Download failed: ",txt)
                    self.find_element(*HomePageLocatars.update_pic6_file_download_tab_btn).click()
                    self.pic6_logout()
                    return 1
                print("Downloaded files: ", self.find_element('xpath', '//*[@id="downloadcon"]').text)
                self.find_element('xpath', '//*[@id="downloadfailmodal"]/div/div/div/div[3]/ul/li/a').click()
                time.sleep(10)
                if (file_sel== 'ssl_download') or(file_sel== 'soft_key download'):
                    self.find_element(*HomePageLocatars.update_pic6_file_download_tab_btn).click()
                    self.pic6_logout()
            except:
                self.wait('//*[@id="downloadcon"]')
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Download failed: ", \
                      self.find_element('xpath', '//*[@id="downloadcon"]').text)
                self.find_element('xpath', '//*[@id="downloadfailmodal"]/div/div/div/div[3]/ul/li/a').click()
                self.find_element(*HomePageLocatars.update_pic6_file_download_tab_btn).click()
                return 1
        except Exception as Erro:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), " PIC6 Restore failed, Error:\n ",Erro)
            if self.find_element('xpath', '//*[@id="downloadfailmodal"]/div/div/div').is_displayed():
                print ("PIC6 Error message: ",self.find_element('xpath', '//*[@id="downloadfailmodal"]/div/div/div').text)
            self.find_element('xpath', '//*[@id="downloadfailmodal"]/div/div/div/div[3]/ul/li/a').click()
            self.find_element(*HomePageLocatars.update_pic6_file_download_tab_btn).click()
            return 1
        time.sleep(3)

    def file_sel(self,f_path,f_name):
        print('******File selection********')
        # os.chdir(f_path)
        os.system(HomePageLocatars.file_upload_exec_path +" "+f_path+f_name)
        time.sleep(1.0)
        print("File Selected..")

    def set_filepath(self,f_path):
        print('******File path selection********')
        print(" Current path: ", self.find_element(*HomePageLocatars.pic6_file_path_input).attribute('value'))
        self.find_element(*HomePageLocatars.pic6_file_path_edit).click()
        self.find_element(*HomePageLocatars.pic6_file_path_input).send_keys(f_path)
        self.find_element(*HomePageLocatars.pic6_file_path_save).click()
        try:
            self.wait(HomePageLocatars.pic6_file_path_dialog)
            self.find_element(*HomePageLocatars.pic6_file_path_dialog_ok_btn).click()
            print(" PIC6 New path: ", self.find_element(*HomePageLocatars.pic6_file_path_input).attribute('value'))
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Save dialog not occured")


    def home_settings(self):
        print("************ Setting Content*********")
        try:
            assert 'Settings', self.find_element(*HomePageLocatars.home_settings).text
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", self.find_element(
                *HomePageLocatars.home_settings).text)
        self.find_element(*HomePageLocatars.home_settings).click()
        if self.find_element(*HomePageLocatars.Settings_btn).is_displayed:
            self.find_element(*HomePageLocatars.Features_btn).click()
            self.find_element(*HomePageLocatars.Settings_btn).click()
            if self.find_element(*HomePageLocatars.chillercfg_text).is_displayed:
                print(datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M"), ": ", "Setting page is present", self.find_element(
                    *HomePageLocatars.chillercfg_text).text)
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Setting page is not present")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Settings button is not present")
        print("******Functions(Wrench) Button*****")
        if self.find_element(*HomePageLocatars.Features_btn).is_displayed:
            self.find_element(*HomePageLocatars.Features_btn).click()
            if self.find_element(*ConnectPageLocators.connectivity_TITLE).is_displayed:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Functions page is present")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Functions page is not present")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def home_homeicon(self):
        try:
            self.find_element(*HomePageLocatars.Home_btn).click()
            time.sleep(2.0)
            self.wait(HomePageLocatars.home_screen_content)
        except:
            print("Home Button not found")
            self.driver.save_screenshot("Home_Button_error.png")

    def user_logout(self):
        if self.wait(HomePageLocatars.profile_btn) ==0:
            try:
                self.find_element(*HomePageLocatars.profile_btn).click()
                self.find_element(*HomePageLocatars.Logout_btn).click()
                # accept logout notifications
                time.sleep(2)
                obj1 = self.driver.switch_to.alert
                print ("Logout blocker: ",obj1.text)
                obj1.accept()
                time.sleep(2)
                obj2 = self.driver.switch_to.alert
                print("Logout blocker: ", obj2.text)
                obj2.accept()
                time.sleep(2)
                if self.wait(LoginPageLocatars.TITLE) == 0:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Logout successfully")
            except Exception as logouterr:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ","Logout exception\n",logouterr)
        else:
            print(" Re-Attempting logout")
            driver.maximize_window()
            time.sleep(2)
            self.driver.refresh()
            time.sleep(5)
            self.find_element(*HomePageLocatars.profile_btn).click()
            self.find_element(*HomePageLocatars.Logout_btn).click()


class OtherPage:
    testParameters = configparser.ConfigParser()
    testParameters.read(utils + "\\Utilities\parameters.ini")
    Chromedriver = testParameters.get("TEST_PARAMETERS", "chromedriver")
    Capabilities = {'chromeOptions': {'useAutomationExtension': False}}

    def __init__(self, other_base_url='https://cstadminui-uat.azurewebsites.net/User/DisplayUsersList'):
        self.other_base_url = other_base_url
        self.other_driver = webdriver.Chrome(OtherPage.Chromedriver, desired_capabilities=OtherPage.Capabilities)
        self.other_driver.get(other_base_url)

    def otherpage_login(self, usr, passwrd):
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_login_usr_txt[-1]).send_keys(usr)
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_login_passwd_txt[-1]).send_keys(passwrd)
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_login_btn[-1]).click()

    #   self.wait(HomePageLocatars.admin_home)

    # def get_activationkey(self, env_key, usrid):
    #     self.other_driver.find_element_by_xpath(HomePageLocatars.admin_search_usr[-1]).send_keys(usrid)
    #     self.other_driver.find_element_by_xpath(HomePageLocatars.admin_search_btn[-1]).click()
    #     result = self.other_driver.find_element_by_xpath(HomePageLocatars.admin_result_usr_name[-1]).text
    #     if str(result) == usrid:
    #         self.other_driver.find_element_by_xpath(HomePageLocatars.admin_view_license_btn[-1]).click()
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", str(result), ' is available')
    #     else:
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", 'Unable to find user: ', str(result))
    #         return "0"
    #     self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_new_btn[-1]).click()
    #     self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_envkey_txt[-1]).click()
    #     self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_envkey_txt[-1]).send_keys(env_key)
    #     self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_check_envkey_btn[-1]).click()
    #     time.sleep(1.0)
    #     self.other_driver.find_element_by_xpath(HomePageLocatars.dialog[-1]).click()
    #     try:
    #         WebDriverWait(other_driver, 3).until(EC.alert_is_present(),
    #                                              'Timed out waiting for PA creation ' +
    #                                              'confirmation popup to appear.')
    #
    #         alert = self.driver.switch_to_alert()
    #         alert.accept()
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", 'alert closed')
    #     except:
    #         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", 'no alert')
    #
    #     validity_date = '12/31/2030'
    #     self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_validity[-1]).send_keys(
    #         validity_date)
    #     status = 'Active'  # Expired,#Disabled
    #     self.other_driver.find_element_by_xpath("//*[@id='CurrentStatus']/option[text()='" + status + "']").click()
    #     lic_type = 'Advanced'  # Basic
    #     self.other_driver.find_element_by_xpath(
    #         "//*[@id='LicenseTypeId']/option[text() ='" + lic_type + "']").click()
    #     self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_generate_btn[-1]).click()
    #     key = self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_key_val[-1]).text
    #     return 'key'

    def get_validity(self, usr):
        pass

    def set_usr_validity(self, usr, status):
        pass