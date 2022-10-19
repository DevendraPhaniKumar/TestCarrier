from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configparser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class HMI_Interaction:
    def __init__(self, HMI_CONTROLLER = 'PIC6', HMIPOINTS = None, target_url = "https://169.254.1.1"):
        TestParameters = configparser.ConfigParser()
        TestParameters.read(dirnameutils + "\\Utilities\TestParamaters.ini")
        chromedriver = TestParameters.get("TEST_PARAMETERS", "chromedriver")
        self.target_url = target_url
        capabilities = {'chromeOptions': {'useAutomationExtension': False}}
        try:
            session_id = TestParameters.get("TEST_PARAMETERS", "session_id")
            executor_url = TestParameters.get("TEST_PARAMETERS", "executor_url")
            web_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
            web_driver.close()
            web_driver.session_id = session_id
        except:
            web_driver = webdriver.Chrome(chromedriver, desired_capabilities=capabilities)
            session_id = web_driver.session_id
            executor_url = web_driver.command_executor._url
            TestParameters['TEST_PARAMETERS']['session_id'] = session_id
            TestParameters['TEST_PARAMETERS']['executor_url'] = executor_url
            with open(dirnameutils + "\\Utilities\TestParamaters.ini", 'w') as configfile:
                TestParameters.write(configfile)
                web_driver.get(target_url)
        self.driver = web_driver
        self.hmi_conf_handle = configparser.ConfigParser()
        self.Hwtype = HMI_CONTROLLER
        self.home_elements = ['//*[@id="spnHome"]', '//*[@id="screen_0_home"]', '//*[@id="screen_27_home"]', '//*[@id="screen_20_home"]',
                         '//*[@id="screen_18_home"]','//*[@id="screen_24_home"]', '//*[@id="screen_23_home"]', '//*[@id="screen_22_home"]']

    def get_driver(self):
        return self.driver

    def ResetHMIAlarm(self, fac_password):
        self.ResetHMI_warning()

        self.wait(self.home_elements[0])


        if self.Hwtype == "PIC5":
            pass

        elif self.Hwtype == "PIC6":
            for i in range(len(self.home_elements)):
                try:
                    elem_home = self.driver.find_element_by_xpath(self.home_elements[i])
                    elem_home.click()
                except:
                    pass

            web_login = '//*[@id="s0_159"]'
            self.wait(web_login)
            # open Lock button
            elem_login = self.driver.find_element_by_xpath(web_login)
            elem_login.click()

            # write password
            pass_click = '//*[@id="s_19w_791"]/div/img'
            self.wait(pass_click)
            elem_password = self.driver.find_element_by_xpath(pass_click)
            elem_password.click()

            pass_ctrl = '//*[@id="pwd"]'
            self.wait(pass_ctrl)
            elem_password1 = self.driver.find_element_by_xpath(pass_ctrl)
            elem_password1.clear()
            elem_password1.send_keys(fac_password)
            elem_password1.send_keys(Keys.ENTER)

            # select Bell button
            bell_btn = ['//*[@id="screen_19_custom1"]/div[2]/img', '//*[@id="screen_0_custom1"]/div[2]/img']
            time.sleep(2)
            for i in bell_btn:
                try:
                    elem_bellbtn = self.driver.find_element_by_xpath(i)
                    elem_bellbtn.click()
                except:
                    pass

            reset_alrm = '//*[@id="td33Reset_Alarms"]/table/tbody/tr[1]/td/div/img'
            self.wait(reset_alrm)
            # Set Reset Alarms Button
            elem_Rst_ALM = self.driver.find_element_by_xpath(reset_alrm)
            elem_Rst_ALM.click()
            WebDriverWait(self.driver, 120).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'tabularCheckbox')))

            # select Reset button
            elem_Alm_Rstbtn = self.driver.find_element_by_class_name('tabularCheckbox')
            elem_Alm_Rstbtn.click()

            # click yes
            yes_radio_btn = '//*[@id="screen_20"]/div[7]/div/div[1]/span[4]/label'
            self.wait(yes_radio_btn)
            elem_yes = self.driver.find_element_by_xpath(yes_radio_btn)
            elem_yes.click()

            # click set button
            set_btn = '//*[@id="screen_20"]/div[7]/div/div[5]/div[1]/input'
            self.wait(set_btn)
            elem_set = self.driver.find_element_by_xpath(set_btn)
            elem_set.click()

    def RebootTheUnit(self):
        self.ResetHMIAlarm('113')
        for i in range(len(self.home_elements)):
            try:
                self.driver.find_element_by_xpath(self.home_elements[i]).click()
            except:
                pass

        menu_btn_xpath = '//*[@id="screen_0_custom5"]/div[2]/img'
        self.wait(menu_btn_xpath)

        menu_btn = self.driver.find_element_by_xpath(menu_btn_xpath)
        menu_btn.click()

        main_menu_page2 = '//*[@id="s_32w_902"]/div/img'
        self.wait(main_menu_page2)

        page2 = self.driver.find_element_by_xpath(main_menu_page2)
        page2.click()

        config_menu = '//*[@id="td32Configuration_Menu"]/table/tbody/tr[1]/td/div/img'
        self.wait(config_menu)

        config_menu_bn = self.driver.find_element_by_xpath(config_menu)
        config_menu_bn.click()

        fac_params = '//*[@id="td34Factory_Parameters"]/table/tbody/tr[1]/td/div/img'
        self.wait(fac_params)

        fac_param_btn = self.driver.find_element_by_xpath(fac_params)
        fac_param_btn.click()
        try:
            reboot = '//*[@id="s69_3468"]'
            time.sleep(12)

            reboot_btn = self.driver.find_element_by_xpath(reboot)
            reboot_btn.click()
        except:
            print("The reboot button is not active.(check for the configuration similarity)")

    def wait(self, element):
        WebDriverWait(self.driver, 600).until(
            EC.visibility_of_element_located((By.XPATH, element)))

    def ResetHMI_warning(self):
        self.driver.get(self.target_url)

    def close(self):
        pass
