import os
import sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(dirnameutils)
sys.path.append(utils)
sys.path.append(dirnameutils+'\Selenium_Lib')
from Selenium_Lib.BaseClass import Page
from Page_locators.HomePage_locatars import HomePageLocatars
from Page_locators.ConnectPage_locators import ConnectPageLocators
from Page_locators.ChecklistPage_locators import ChecklistPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
import configparser
import time
import datetime
driver = object
delay = 45


class HomePage(Page):
    global driver, delay

    def wait(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, element[-1])))
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),": ","Page ready!")
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),": ","Loading took too much time!")
        # try:
        #     self.find_element(*HomePageLocatars.HOME).click()
        # except:
        #     pass

    def user_verion_info(self, webdriver):
        global driver
        driver = webdriver
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ", "Application version Information")
        self.wait(HomePageLocatars.TITLE)
        title = self.find_element(*HomePageLocatars.TITLE).text
        user = self.find_element(*HomePageLocatars.USER).text
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",'Title & Version = ', title)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",'User = ', user.split(',')[-1])

    def user_profile(self, profile_info):
        print("**** User Profile Test **********")
        self.find_element(*HomePageLocatars.profile_btn).click()
        profile_title = self.find_element(*HomePageLocatars.Profile_title).text
        try:
			assert str(profile_info), profile_title
        except:
		    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:", profile_title)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",profile_title)

    def profile_name(self, first,last,First_Name_text,Last_name_text,error_msg):
        print("**** User Profile: Profile Name Test **********")
        first_name = self.find_element(*HomePageLocatars.Profile_FirstName_lbl).text
        try:
            assert First_Name_text, first_name
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",first_name)
        self.find_element(*HomePageLocatars.Profile_FirstName_val).clear()
        if first != "":
            self.find_element(*HomePageLocatars.Profile_FirstName_val).send_keys(first)
        last_name = self.find_element(*HomePageLocatars.Profile_LastName_lbl).text
        try:
            assert Last_name_text, last_name
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:", last_name)
        self.find_element(*HomePageLocatars.Profile_LastName_val).clear()
        if last != '':
            self.find_element(*HomePageLocatars.Profile_LastName_val).send_keys(last)
        self.find_element(*HomePageLocatars.Save_btn).click()
        try:
            self.wait(str(self.find_element(*HomePageLocatars.First_error_msg).text))
            err_1  = self.find_element(*HomePageLocatars.First_error_msg).text
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Error:", err_1)
            try:
                assert err_1,error_msg
            except:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",error_msg)
        except:
            pass
        try:
            self.wait(str(find_element(*HomePageLocatars.LastName_err_msg).text))
            err_2 =  self.find_element(*HomePageLocatars.LastName_err_msg).text
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Error:",err_2)
            try:
                assert err_2,error_msg
            except:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",error_msg)
        except:
            pass
        try:
            self.wait(str(self.find_element(*HomePageLocatars.Update_error_msg).text))
            pass_msg = self.find_element(*HomePageLocatars.Update_error_msg).text
            try:
                assert pass_msg, error_msg
            except:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:", error_msg)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ", "Update Message:", error_msg)
        except:
            pass
        first_name_val = self.find_element(*HomePageLocatars.Profile_FirstName_val).text
        try:
            assert first, first_name_val
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:", first_name_val)
        last_name_val = self.find_element(*HomePageLocatars.Profile_LastName_val).text
        try:
            assert last, last_name_val
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:", last_name_val)

    def profile_mail_id(self,userid_label,userid ):
        print("**** User Profile: Profile ID Test **********")
        text =  self.find_element(*HomePageLocatars.Profile_UsrName_lbl).text
        try:
            assert text, userid_label
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",userid_label)
        uid = self.find_element(*HomePageLocatars.Profile_UsrName_val).get_attribute('value')
        try:
            assert uid, userid
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",userid)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","UserName:", str(uid))

    def profile_update_password(self, pwd,repwd):
        print("**** User Profile: Profile Password Test **********")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Password Change - Expect:","Change Password","Actual:",self.find_element(*HomePageLocatars.Profile_change_passwd_lbl).text)
        pass_lbl = self.find_element(*HomePageLocatars.Profile_change_passwd_lbl).text
        try:
            assert "Change Password", pass_lbl
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",pass_lbl)
        if pwd != '':
            self.find_element(*HomePageLocatars.Profile_change_passwd_val).send_keys(pwd)
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Blank password")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Password Change - Expect:", "Re-Type New Password", "Actual:", self.find_element(*HomePageLocatars.Profile_change_passwd_Confirm_lbl).text)
        repass_lbl = self.find_element(*HomePageLocatars.Profile_change_passwd_Confirm_lbl).text
        try:
            assert "Re-type New Password", repass_lbl
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",repass_lbl)
        if repwd != '':
            self.find_element(*HomePageLocatars.Profile_change_passwd_Confirm_val).send_keys(pwd)
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Blank password")
        self.find_element(*HomePageLocatars.Save_btn).click()
        #self.wait(str(self.find_element(*HomePageLocatars.Update_error_msg).text))
        update_msg = self.find_element(*HomePageLocatars.Update_error_msg).text
        if update_msg == "Profile updated successfully":
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Update message:", update_msg)
            return
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",update_msg)
            try:
                self.wait(str(self.find_element(HomePageLocatars.Passwd_error_msg).text))
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.Passwd_error_msg).text)
            except:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","No password error")

    def app_font_size(self,size_input):
        print("**** User Profile: Profile font size Test **********")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.Fontsize_lbl).text)
        self.find_element(*HomePageLocatars.Fontsize_sel).click()
        self.find_element(*HomePageLocatars.Fontsize_LOE)
        link = driver.find_element_by_link_text(size_input)
        link.click()
        self.find_element(*HomePageLocatars.Save_btn).click()


    def app_language_select(self,lang):
        print("**** User Profile: Profile language Test **********")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.Language_lbl).text)
        self.find_element(*HomePageLocatars.Language_sel).click()
        self.find_element(*HomePageLocatars.Language_LOE)
        link = driver.find_element_by_link_text(lang)
        link.click()
        self.find_element(*HomePageLocatars.Save_btn).click()

    def unit_change(self,unit_type):
        print("**** User Profile: Profile Unit type Test **********")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.Unit_type_lbl).text)
        self.find_element(*HomePageLocatars.Unit_type_sel).click()
        self.find_element(*HomePageLocatars.Unit_type_LOE)
        link = driver.find_element_by_link_text(unit_type)
        link.click()
        self.find_element(*HomePageLocatars.Save_btn).click()

    def license_validation(self,usr_lvl,usrid,validity):
        print("**** User Profile: License screen Test **********")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",usr_lvl, self.find_element(*HomePageLocatars.License_level).text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.License_Validity).text)
        self.find_element(*HomePageLocatars.License_Update_btn).click()
        lic_pop_title =self.find_element(*HomePageLocatars.License_Update_title).text
        try:
            assert "Update License", lic_pop_title
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",lic_pop_title)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.License_Update_title).text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.License_type_lbl).text)
        lic_type_lbl =self.find_element(*HomePageLocatars.License_type_txt).text
        try:
            assert usr_lvl, lic_type_lbl
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:", lic_type_lbl)
        lic_usr_lbl = self.find_element(*HomePageLocatars.License_Usr_txt).text
        try:
            assert usrid, lic_usr_lbl
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",lic_usr_lbl)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.License_Usr_lbl).text)
        lic_usr_val = self.find_element(*HomePageLocatars.License_Usr_txt).text
        try:
            assert usrid, lic_usr_val
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",lic_usr_val)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Expect:", usrid,"Actual:", self.find_element(*HomePageLocatars.License_Usr_txt).text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.License_Expiry_lbl).text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",validity, self.find_element(*HomePageLocatars.License_Expiry_txt).text)
        self.find_element(*HomePageLocatars.License_Update_close).click()
        self.find_element(*HomePageLocatars.Save_btn).click()

    def license_activation(self,userid,passwd):
        print("**** User Profile: License activation Test **********")
        self.find_element(*HomePageLocatars.License_Update_btn).click()
        lic_update_title = self.find_element(*HomePageLocatars.License_Update_title).text
        try:
            assert "Update License", lic_update_title
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",lic_update_title)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.License_type_lbl).text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",usr_lvl, self.find_element(*HomePageLocatars.License_type_txt).text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.License_Expiry_lbl).text)
        env_key =str(self.find_element(*HomePageLocatars.License_Expiry_lbl).text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Env_key", env_key)
        admin_portal = OtherPage()
        other_driver.otherpage_login('udayabhaskar.challa@fs.utc.com', 'Uday@1234')
        #env_key = 'Ym1ZQThLbTN0SzZjZG1BeTN4a2Q4bGtxdDgyTXk1Nm8rSmxMVC9VZk43L3RUOSsrb1ZmY3Vobi8zNDc5eVRpRWxiand4M2U4dGlyWDRjaWJYR09neER0UFp2azF6bTVHTEx2RFBUd2VTT0k9'
        lic_key = other_driver.get_activationkey(env_key,userid)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","License_key", lic_key)
        self.find_element(*HomePageLocatars.License_key_val).send_keys(lic_key)
        self.find_element(*HomePageLocatars.License_apply_btn).click()
        try:
            self.wait(str(self.find_element(*HomePageLocatars.License_error_msg).text))
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Error msg: ", self.find_element(*HomePageLocatars.License_error_msg).text)
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","No error")
        self.find_element(*HomePageLocatars.License_Update_close).click()
        updated_usr_lvl = self.find_element(*HomePageLocatars.License_label).text
        if  updated_usr_lvl == "Advanced":
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","License updated and User is updated to Advanced")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","License update failed",updated_usr_lvl)
        self.find_element(*HomePageLocatars.Save_btn).click()

    def profile_save(self):
        try:
            self.find_element(*HomePageLocatars.Save_btn).click()
        except:
            pass
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.Update_error_msg).text)
        #self.find_element(*HomePageLocatars.profile_btn).click()

    def home_screen_test(self):
        #list of elements
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","************ Home Screen functions Content*********")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.HOME).text)
        #validate each feature screen present
        elements = driver.find_elements(*HomePageLocatars.home_screen_content)
        for i in elements:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Radio button text:", i.text)# elements.get(i).getAttribute("value")

    def home_connect(self):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","\n************ Connectivity Content*********")
        connectivity_lbl = self.find_element(*HomePageLocatars.home_connectivity).text
        try:
            assert 'Connectivity', connectivity_lbl
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",connectivity_lbl)
        self.find_element(*HomePageLocatars.home_connectivity).click()
        time.sleep(1.0)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*ConnectPageLocators.connectivity_TITLE).text)
        element = self.find_element(*ConnectPageLocators.connectivity_icon)
        if element.is_displayed:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Connectivity function present")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def disconnect_ccn(self):

        self.find_element(*HomePageLocatars.home_connectivity).click()
        self.wait(ConnectPageLocators.connectivity_TITLE)
        if self.driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div[1]/div/div/div/div[1]/div/ul/li/button[2]").text == "Disconnect":
            self.driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div[1]/div/div/div/div[1]/div/ul/li/button[2]").click()
       # self.wait(*ConnectPageLocators.connect_message)
      #  msg = self.find_element(*ConnectPageLocators.connect_message).text
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "Device disconnected")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def home_checklist(self):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","\n************ Checklist Content*********")
        time.sleep(1.0)
        checklist_lbl =self.find_element(*HomePageLocatars.home_checklist).text
        try:
            assert 'Checklist',checklist_lbl
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",checklist_lbl)
        self.find_element(*ChecklistPageLocators.checklist).click()
        time.sleep(1.0)
        if self.find_element(*HomePageLocatars.checklist_btn).is_displayed:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Checklist icon is present")
            self.find_element(*ConnectPageLocators.connectivity_icon).click() # Checklist button validation
            self.find_element(*HomePageLocatars.checklist_btn).click() # Checklist button validation
            if self.find_element(*ChecklistPageLocators.existing_form).is_displayed:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Existing form page is present",self.find_element(*ChecklistPageLocators.All_forms).text)
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Existing form page is not loaded")
            if self.find_element(*ChecklistPageLocators.new_form).is_displayed:
                self.find_element(*ChecklistPageLocators.new_form).click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," New form page is present", self.find_element(*ChecklistPageLocators.create_new_form_text).text)
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," New form page is not loaded")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Checklist Page is not loaded")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def home_Reports(self):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","************ Reports Content*********")
        try:
            assert 'Reports',self.find_element(*HomePageLocatars.home_reports).text
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",self.find_element(*HomePageLocatars.home_reports).text)
        self.find_element(*HomePageLocatars.home_reports).click()
        time.sleep(1.0)
        self.find_element(*ConnectPageLocators.connectivity_icon).click()
        if self.find_element(*HomePageLocatars.reports_btn).is_displayed:
            self.find_element(*HomePageLocatars.reports_btn).click()
            if self.find_element(*HomePageLocatars.reports_chart).is_displayed:
                self.find_element(*HomePageLocatars.reports_chart).click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Report menu is present")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Reports page is not loaded")
            if self.find_element(*HomePageLocatars.reports_trend_cfg).is_displayed:
                self.find_element(*HomePageLocatars.reports_trend_cfg).click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Trend page is present")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Trend page is not loaded")
            if self.find_element(*HomePageLocatars.reports_trace_history).is_displayed:
                self.find_element(*HomePageLocatars.reports_trace_history)
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Trace History page is present")
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Trace History is not loaded")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": "," Report Page is not loaded")
        self.find_element(*HomePageLocatars.Home_btn).click()
    def home_fwupdate(self):
        print("************ Firwmare update/File Transfer Content*********")
        self.find_element(*HomePageLocatars.home_reports).click()
        if self.find_element(*HomePageLocatars.firmware_update_btn).is_displayed:
            self.find_element(*HomePageLocatars.firmware_update_btn).click()
            assert 'Firmware Update/File Transfer', self.find_element(*HomePageLocatars.firmware_update_text).text
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ", "Firmware Update button is present")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ", "Firmware Update page is not present")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def home_settings(self):
        print("************ Setting Content*********")
        try:
            assert 'Settings',self.find_element(*HomePageLocatars.home_settings).text
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",self.find_element(*HomePageLocatars.home_settings).text)
        self.find_element(*HomePageLocatars.home_settings).click()
        if self.find_element(*HomePageLocatars.Settings_btn).is_displayed:
            self.find_element(*HomePageLocatars.Features_btn).click()
            self.find_element(*HomePageLocatars.Settings_btn).click()
            if self.find_element(*HomePageLocatars.chillercfg_text).is_displayed:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ", "Setting page is present",self.find_element(*HomePageLocatars.chillercfg_text).text)
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ", "Setting page is not present")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Settings button is not present")
        print("******Functions(Wrench) Button*****")
        if self.find_element(*HomePageLocatars.Features_btn).is_displayed:
                self.find_element(*HomePageLocatars.Features_btn).click()
                if self.find_element(*ConnectPageLocators.connectivity_TITLE).is_displayed:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ", "Functions page is present")
                else:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ", "Functions page is not present")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def home_help(self):
        print("************ Help Content*********")
        try:
            assert 'Help', self.find_element(*HomePageLocatars.home_help).text
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Assertion Failed:",self.find_element(*HomePageLocatars.home_help).text)
        self.find_element(*HomePageLocatars.home_help).click()
        time.sleep(1.0)
        if self.find_element(*HomePageLocatars.help_btn).is_displayed:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",self.find_element(*HomePageLocatars.help_title).text)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Help is  present")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Help page is not present")
        self.find_element(*HomePageLocatars.Home_btn).click()
    def home_homeicon(self):
        self.find_element(*HomePageLocatars.Home_btn).click()


    def home_alarms(self):
        print("************ Alarms Content*********")
        try:
            self.wait(HomePageLocatars.Home_btn)
            self.find_element(*HomePageLocatars.Home_btn).click()
            print("loaded functions screen")
        except:
            self.wait(HomePageLocatars.home_alarms)
            print("loaded home screen")
            self.find_element(*HomePageLocatars.home_alarms).click()

        try:
            assert 'Alarms/Alerts',self.find_element(*HomePageLocatars.home_alarms).text
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:",self.find_element(*HomePageLocatars.home_alarms).text)
        self.find_element(*HomePageLocatars.home_alarms).click()
        #self.wait(HomePageLocatars.alarms_btn)
       # self.find_element(*HomePageLocatars.home_alarms).click()
        if self.find_element(*HomePageLocatars.alarms_btn).is_displayed:
            try:
                self.wait(*HomePageLocatars.alarm_msg)
                err_msg = self.find_element(*HomePageLocatars.alarm_msg).text
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ", err_msg)
                return
            except:
                print("No Message ")
            if self.find_element(*HomePageLocatars.current_alarm).is_displayed:
                self.find_element(*HomePageLocatars.current_alarm).click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Current Alarms: ",self.find_element(*HomePageLocatars.current_alarm).text)
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Current alarm page is not loaded")
            if self.find_element(*HomePageLocatars.hist_alarm).is_displayed:
                self.find_element(*HomePageLocatars.hist_alarm).click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Hist Alarms: ",self.find_element(*HomePageLocatars.hist_alarm).text)
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Hist alarm page is not loaded")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Alarm button is not available")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def home_alarms_validation(self):
        print("************ Alarms Content*********")
        try:
            self.wait(HomePageLocatars.Home_btn)
            self.find_element(*HomePageLocatars.Home_btn).click()
            print("loaded functions screen")
        except:
            self.wait(HomePageLocatars.home_alarms)
            print("loaded home screen")
            self.find_element(*HomePageLocatars.home_alarms).click()

        try:
            assert 'Alarms/Alerts', self.find_element(*HomePageLocatars.home_alarms).text
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Assertion Failed:", self.find_element(
                *HomePageLocatars.home_alarms).text)
        self.find_element(*HomePageLocatars.home_alarms).click()
        if self.find_element(*HomePageLocatars.alarms_btn).is_displayed:
            if self.find_element(*HomePageLocatars.current_alarm).is_displayed:
                try:
                    self.wait(*HomePageLocatars.alarm_msg)
                    err_msg = self.find_element(*HomePageLocatars.alarm_msg).text
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", err_msg)
                    return
                except:
                    print("No Message ")
                self.find_element(*HomePageLocatars.current_alarm).click()
                ###Alarm table validation to be updated
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Current alarm page is not loaded")
            if self.find_element(*HomePageLocatars.hist_alarm).is_displayed:
                self.find_element(*HomePageLocatars.hist_alarm).click()
                ###Alarm table validation to be updated
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Hist alarm page is not loaded")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Alarm button is not available")
        self.find_element(*HomePageLocatars.Home_btn).click()

    def user_logout(self):
        try:
            self.find_element(*HomePageLocatars.profile_btn).click()
            self.find_element(*HomePageLocatars.Logout_btn).click()
        except:
            pass
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ","Logout successfully")

class OtherPage:
    testParameters = configparser.ConfigParser()
    testParameters.read(utils + "\\Utilities\parameters.ini")
    Chromedriver = testParameters.get("TEST_PARAMETERS", "chromedriver")
    Capabilities = {'chromeOptions': {'useAutomationExtension': False}}

    def __init__(self, other_base_url='https://cstadminui-uat.azurewebsites.net/User/DisplayUsersList'):
        self.other_base_url = other_base_url
        self.other_driver = webdriver.Chrome(OtherPage.Chromedriver, desired_capabilities=OtherPage.Capabilities)
        self.other_driver.get(other_base_url)

    def otherpage_login(self,usr,passwrd):
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_login_usr_txt[-1]).send_keys(usr)
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_login_passwd_txt[-1]).send_keys(passwrd)
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_login_btn[-1]).click()
     #   self.wait(HomePageLocatars.admin_home)

    def get_activationkey(self,env_key,usrid):
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_search_usr[-1]).send_keys(usrid)
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_search_btn[-1]).click()
        result = self.other_driver.find_element_by_xpath(HomePageLocatars.admin_result_usr_name[-1]).text
        if str(result) == usrid :
            self.other_driver.find_element_by_xpath(HomePageLocatars.admin_view_license_btn[-1]).click()
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",str(result),' is available')
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",'Unable to find user: ',str(result))
            return NULL
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_new_btn[-1]).click()
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_envkey_txt[-1]).click()
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_envkey_txt[-1]).send_keys(env_key)
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_check_envkey_btn[-1]).click()
        time.sleep(1.0)
        self.other_driver.find_element_by_xpath(HomePageLocatars.dialog[-1]).click()
        try:
            WebDriverWait(other_driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            alert = self.driver.switch_to_alert()
            alert.accept()
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",'alert closed')
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),": ",'no alert')

        validity_date =  '12/31/2030'
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_validity[-1]).send_keys(validity_date)
        status = 'Active'#Expired,#Disabled
        self.other_driver.find_element_by_xpath("//*[@id='CurrentStatus']/option[text()='" +  status +  "']").click()
        lic_type = 'Advanced' #Basic
        self.other_driver.find_element_by_xpath("//*[@id='LicenseTypeId']/option[text() ='" + lic_type + "']").click()
        self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_generate_btn[-1]).click()
        key = self.other_driver.find_element_by_xpath(HomePageLocatars.admin_license_key_val[-1]).text
        return 'key'

    def get_validity(self,usr):
        pass

    def set_usr_validity(self,usr,status):
        pass
