#@author: Pramodh kalidindi
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configparser
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Lib_space import VirSim_Module
import os
# import Utilities

dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class HMI_Interaction:

    def __init__(self, HMI_CONTROLLER = 'PIC6', HMIPOINTS = None, target_url = "https://169.254.1.1"):
        self.TestParameters = configparser.ConfigParser()

        # self.TestParameters.read(dirnameutils + r'\Utilities\Test_Parameters.ini')
        # chromedriver = self.TestParameters.get("TEST_PARAMETERS", "chromedriver")
        # self.target_url = target_url
        # capabilities = {'chromeOptions': {'useAutomationExtension': False}}
        #
        # try:
        #     session_id = self.TestParameters.get("TEST_PARAMETERS", "session_id")
        #     executor_url = self.TestParameters.get("TEST_PARAMETERS", "executor_url")
        #     web_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
        #     web_driver.close()
        #     web_driver.session_id = session_id
        # except:
        #     web_driver = webdriver.Chrome(chromedriver, desired_capabilities=capabilities)
        #     session_id = web_driver.session_id
        #     executor_url = web_driver.command_executor._url
        #     self.TestParameters['TEST_PARAMETERS']['session_id'] = session_id
        #     self.TestParameters['TEST_PARAMETERS']['executor_url'] = executor_url
        #     with open(dirnameutils + r'\Utilities\Test_Parameters.ini', 'w') as configfile:
        #         self.TestParameters.write(configfile)
        #         web_driver.get(target_url)
        # self.driver = web_driver
        # self.hmi_conf_handle = configparser.ConfigParser()
        # self.Hwtype = HMI_CONTROLLER
        # self.home_elements = ['//*[@id="spnHome"]', '//*[@id="screen_0_home"]','//*[@id="screen_1_home"]', '//*[@id="screen_27_home"]', '//*[@id="screen_20_home"]',
        #                  '//*[@id="screen_18_home"]','//*[@id="screen_24_home"]', '//*[@id="screen_23_home"]', '//*[@id="screen_22_home"]',
        #                       '//*[@id="screen_63_home"]', '//*[@id="screen_19_home"]','//*[@id="screen_64_home"]']

    def get_driver(self):
        return True

    # def ResetHMIAlarm(self, fac_password):
    #     self.ResetHMI_warning()
    #
    #     self.goto_home()
    #
    #     if self.Hwtype == "PIC5":
    #         pass
    #
    #     elif self.Hwtype == "PIC6":
    #         self.goto_home()
    #
    #         self.unlock_fac_lev(fac_password)
    #
    #         self.goto_home()
    #
    #         # select Bell button
    #         bell_btn = ['//*[@id="screen_0_custom1"]/div[2]/img','//*[@id="screen_36_custom1"]/div[2]/img']
    #         time.sleep(2)
    #         for i in bell_btn:
    #             try:
    #                 elem_bellbtn = self.driver.find_element_by_xpath(i)
    #                 elem_bellbtn.click()
    #             except:
    #                 pass
    #
    #         reset_alrm = '//*[@id="td36Reset_Alarms"]/table/tbody/tr[1]/td/div/img'
    #         # reset_alrm = '//*[@id="screen_0_custom1"]/div[2]/img'
    #
    #         # '//*[@id="screen_0_custom1"]/div[2]/img' \
    #         # '//*[@id="screen_0_custom1"]/div[2]/img'
    #
    #         self.wait(reset_alrm)
    #         # Set Reset Alarms Button
    #         elem_Rst_ALM = self.driver.find_element_by_xpath(reset_alrm)
    #         # elem_Rst_ALM2= self.driver.find_element_by_xpath(reset_alrm2)
    #         # if elem_Rst_ALM.is_displayed():
    #         elem_Rst_ALM.click()
    #         # if elem_Rst_ALM2.is_displayed():
    #         #     elem_Rst_ALM2.click()
    #
    #         back_button = '//*[@id="screen_23_back"]'
    #         elem_back_button = self.driver.find_element_by_xpath(back_button)
    #         elem_back_button.click()
    #
    #         reset_alrm = '//*[@id="td36Reset_Alarms"]/table/tbody/tr[1]/td/div/img'
    #         self.wait(reset_alrm)
    #         elem_Rst_ALM = self.driver.find_element_by_xpath(reset_alrm)
    #         # elem_Rst_ALM2= self.driver.find_element_by_xpath(reset_alrm2)
    #         # if elem_Rst_ALM.is_displayed():
    #         elem_Rst_ALM.click()
    #
    #         WebDriverWait(self.driver, 160).until(
    #             EC.visibility_of_element_located((By.CLASS_NAME, 'tabularCheckbox')))
    #
    #         # select Reset button
    #         elem_Alm_Rstbtn = self.driver.find_element_by_class_name('tabularCheckbox')
    #         elem_Alm_Rstbtn.click()
    #
    #         # click yes
    #         yes_radio_btn = '//*[@id="screen_23"]/div[7]/div/div[1]/span[4]/label'
    #         self.wait(yes_radio_btn)
    #         elem_yes = self.driver.find_element_by_xpath(yes_radio_btn)
    #         elem_yes.click()
    #
    #         # click set button
    #         set_btn = '//*[@id="screen_23"]/div[7]/div/div[5]/div[1]/input'
    #         self.wait(set_btn)
    #         elem_set = self.driver.find_element_by_xpath(set_btn)
    #         elem_set.click()

    def RebootTheUnit(self):
        subprocess.call(r"D:\Python3_app\Lib_Space\UI\reboot_ui.bat")

    # def RebootTheUnit_old(self):
    #     self.ResetHMI_warning()
    #     self.goto_home()
    #     self.unlock_fac_lev('113')
    #     time.sleep(2)
    #     self.goto_home()
    #
    #     power_btn_xpath = '//*[@id="screen_0_custom2"]/div[2]/img'
    #     self.wait(power_btn_xpath)
    #     #
    #     power_btn = self.driver.find_element_by_xpath(power_btn_xpath)
    #     power_btn.click()
    #
    #     time.sleep(2)
    #
    #     reboot_ui_btn_xpath = '//*[@id="s64_3130"]'
    #     self.wait(reboot_ui_btn_xpath)
    #
    #     reboot_ui_btn = self.driver.find_element_by_xpath(reboot_ui_btn_xpath)
    #     reboot_ui_btn.click()
    #
    #     # menu_btn_xpath = '//*[@id="screen_0_custom5"]/div[2]/img'
    #     # self.wait(menu_btn_xpath)
    #     #
    #     # menu_btn = self.driver.find_element_by_xpath(menu_btn_xpath)
    #     # menu_btn.click()
    #     #
    #     # main_menu_page2 = '//*[@id="s_32w_898"]/div/img'
    #     # self.wait(main_menu_page2)
    #     #
    #     # page2 = self.driver.find_element_by_xpath(main_menu_page2)
    #     # page2.click()
    #     #
    #     # config_menu = '//*[@id="td32Configuration_Menu"]/table/tbody/tr[1]/td/div/img'
    #     # self.wait(config_menu)
    #     #
    #     # config_menu_bn = self.driver.find_element_by_xpath(config_menu)
    #     # config_menu_bn.click()
    #     #
    #     # fac_params = '//*[@id="td34Factory_Parameters"]/table/tbody/tr[1]/td/div/img'
    #     # self.wait(fac_params)
    #     #
    #     # fac_param_btn = self.driver.find_element_by_xpath(fac_params)
    #     # fac_param_btn.click()
    #     # try:
    #     #     reboot = '//*[@id="s69_3461"]'
    #     #     time.sleep(12)
    #     #
    #     #     reboot_btn = self.driver.find_element_by_xpath(reboot)
    #     #     reboot_btn.click()
    #     # except:
    #     #     print "The reboot button is not active.(check for the configuration similarity)"

    # def set_local_mode_off(self):
    #     # self.ResetHMI_warning()
    #     self.unlock_fac_lev('113')
    #     time.sleep(2)
    #     self.goto_home()
    #
    #     power_btn_xpath = '//*[@id="screen_0_custom2"]/div[2]/img'
    #     self.wait(power_btn_xpath)
    #
    #     power_btn = self.driver.find_element_by_xpath(power_btn_xpath)
    #     power_btn.click()
    #
    #     # reboot_ui_btn_xpath = '//*[@id="s70_3304"]'
    #     # self.unlock_fac_lev('113')
    #     #
    #     # self.goto_home()
    #     #
    #     # power_btn_xpath = '//*[@id="screen_0_custom2"]/div[2]/img'
    #     # self.wait(power_btn_xpath)
    #     #
    #     # power_btn = self.driver.find_element_by_xpath(power_btn_xpath)
    #     # power_btn.click()
    #
    #     try:
    #
    #         Local_on_Button = '//*[@id="s64_3111"]'
    #         if self.driver.find_element_by_xpath(Local_on_Button).is_displayed():
    #             print ("System already in Local OFF")
    #         else:
    #             confirm_stop_bt = '//*[@id="s64_3116"]'
    #             # local_off_xpath = '//*[@id="s64_3123"]]'
    #             self.wait(confirm_stop_bt)
    #
    #             local_off = self.driver.find_element_by_xpath(confirm_stop_bt)
    #             local_off.click()
    #     except:
    #         pass
    #     print("Netwrok: Set to Local OFF")
    #
    # def set_local_mode_on(self):
    #     # self.ResetHMI_warning()
    #     self.unlock_fac_lev('113')
    #     # time.sleep(2)
    #     self.goto_home()
    #
    #     power_btn_xpath = '//*[@id="screen_0_custom2"]/div[2]/img'
    #     self.wait(power_btn_xpath)
    #
    #     power_btn = self.driver.find_element_by_xpath(power_btn_xpath)
    #     power_btn.click()
    #
    #     time.sleep(10)
    #
    #     # reboot_ui_btn_xpath = '//*[@id="s70_3304"]'
    #     # self.unlock_fac_lev('113')
    #     #
    #     # self.goto_home()
    #     #
    #     # power_btn_xpath = '//*[@id="screen_0_custom2"]/div[2]/img'
    #     # self.wait(power_btn_xpath)
    #     #
    #     # power_btn = self.driver.find_element_by_xpath(power_btn_xpath)
    #     # power_btn.click()
    #
    #     try:
    #         confirm_stop_Button = '//*[@id="s64_3116"]'
    #         if self.driver.find_element_by_xpath(confirm_stop_Button).is_displayed():
    #             print ("System already in Local ON")
    #         else:
    #             Local_on_Button = '//*[@id="s64_3111"]'
    #             self.wait(Local_on_Button)
    #
    #             local_on= self.driver.find_element_by_xpath(Local_on_Button)
    #             local_on.click()
    #     except:
    #         # confirm_stop_Button = '//*[@id="s64_3116"]'
    #         # self.wait(confirm_stop_Button)
    #         # print("System already in LOCAL ON")
    #         pass
    #
    #     print("System in LOCAL ON")
    #
    # def set_network_mode(self):
    #     self.ResetHMI_warning()
    #     self.unlock_fac_lev('113')
    #
    #     self.goto_home()
    #
    #     power_btn_xpath = '//*[@id="screen_64_custom2"]/div[2]/img'
    #     self.wait(power_btn_xpath)
    #
    #     power_btn = self.driver.find_element_by_xpath(power_btn_xpath)
    #     power_btn.click()
    #
    #     network_btn_xpath = '//*[@id="s64_3120"]'
    #     self.wait(network_btn_xpath)
    #     network_btn = self.driver.find_element_by_xpath(network_btn_xpath)
    #     network_btn.click()
    #
    #     print("Netwrok: Set to Network")
    #
    # def unlock_fac_lev(self, fac_password):
    #     self.ResetHMI_warning()
    #     self.goto_home()
    #
    #     web_login = '//*[@id="s0_156"]'
    #     self.wait(web_login)
    #     # open Lock button
    #     elem_login = self.driver.find_element_by_xpath(web_login)
    #     elem_login.click()
    #
    #     # write password
    #     #pass_click = '//*[@id="s_19w_787"]/div/img'
    #     pass_click = '//*[@id="s_1w_215"]/div/img'
    #     self.wait(pass_click)
    #     elem_password = self.driver.find_element_by_xpath(pass_click)
    #     elem_password.click()
    #
    #     pass_ctrl = '//*[@id="pwd"]'
    #     self.wait(pass_ctrl)
    #     elem_password1 = self.driver.find_element_by_xpath(pass_ctrl)
    #     elem_password1.clear()
    #     elem_password1.send_keys(fac_password)
    #     time.sleep(5)
    #     elem_login = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
    #     elem_login.click()
    #     # elem_password1.submit()
    #
    #     # bell_btn = ['//*[@id="screen_0_custom1"]/div[2]/img', '//*[@id="screen_36_custom1"]/div[2]/img']
    #     # time.sleep(2)
    #     # for i in bell_btn:
    #     #     try:
    #     #         elem_bellbtn = self.driver.find_element_by_xpath(i)
    #     #         elem_bellbtn.click()
    #     #     except:
    #     #         pass
    #     # login_btn = '//*[@id="popupBasic"]/form/div/div[4]/div[2]/button'
    #     # self.wait(login_btn)
    #     # login_btn_op = self.driver.find_element_by_xpath(login_btn)
    #     # login_btn_op.click()
    #     # for i in range(0,3):
    #     #     elem_password1.send_keys(Keys.ENTER)
    #
    #
    #     print("Login Level: Factory")
    #
    # def goto_home(self):
    #     for i in range(len(self.home_elements)):
    #         try:
    #             self.driver.find_element_by_xpath(self.home_elements[i]).click()
    #         except:
    #             pass
    #
    # def wait(self, element):
    #     WebDriverWait(self.driver, 600).until(
    #         EC.visibility_of_element_located((By.XPATH, element)))
    #
    def ResetHMI_warning(self):
        return True
        # self.driver.get(self.target_url)
        # self.goto_home()
    #
    #
    #def read_ALMdes(self):
        #Alarm_desc = self.driver.find_element_by_xpath('//*[@id="s0_189"]').text
        #print(str(Alarm_desc))
        #return True
    def close(self):
        pass
