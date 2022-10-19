from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import os
import time
import datetime
import unittest
import pyodbc
import re
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils + "\LibSpace")
sys.path.append(dirnameutils + "\LibSpace\Connectivity")
from lib_common_operations import CommonOperations


class ConfigurationUpdate(unittest.TestCase):

    def setup(self):
        pass

    def version_check(self, driver, mac_address_of_device, existing_selected_model_version):
        # get version information from carrier smart landing page

        print(" Time Now = ", datetime.datetime.now())
        print("Waiting for 15 mins - Version verification delay due to CarrierSmart Search Engine")
        time.sleep(900)  # required for carrier smart search engine to populate data in UI
        print(" Time Now = ", datetime.datetime.now())

        driver.refresh()
        logo_xpath = "//div[@class='appLogo']"
        CommonOperations.click_element_byXpath(self, driver, logo_xpath) # added on 9/aug/2019
        #time.sleep(60) #  removed as search operation waits until chillers are displayed...

        # search chiller to find version information
        CommonOperations.search_chiller(self, driver, mac_address_of_device)

        model_version_landing_page_xpath = "//*[@id='deviceListItems']/cdk-virtual-scroll-viewport/div[1]/div/table/tbody/tr/td[7]/span"
        CommonOperations.wait_until_element_visible_byXpath(self, driver, model_version_landing_page_xpath)
        time.sleep(10)  # had to use static delay as i could not find a proper wait until function for this... changed from 5 to 30 on 19-02-2019
        chiller_model_version_landing_page = driver.find_element_by_xpath(model_version_landing_page_xpath).text
        print("Model version text = ", "1"+chiller_model_version_landing_page+"1")
        print("Len chiller_model_version_landing_page_text", len(chiller_model_version_landing_page))

        if chiller_model_version_landing_page != ' ':
            version_number = re.split('(\d+)', chiller_model_version_landing_page)
            print("version_number", version_number, version_number[1])
            self.assertEqual('Success', chiller_model_version_landing_page[0:7], "Comparison of Version Text")
            self.assertEqual(int(version_number[1]),existing_selected_model_version, "Comparison of Version Number")
        else:
            "Carrier smart landing page not open"

    def config_update(self,mac_address_of_device, metricname, hours, minutes, cov):
        driver = CommonOperations.open_carrier_smart(self)

        # Opening Chiller Setting Page
        carrier_smart_settings_page_button_xpath = "//*[@class='sprite csmartico_gear']" # changed on 12 Aug 2019
        CommonOperations.click_element_byXpath(self, driver, carrier_smart_settings_page_button_xpath)

        print("Carrier Smart setting Page is Open")

        # Open model tab in settings page
        model_tab_xpath = "//*[@id='navbarCollapse']/ul/li[4]/a"
        CommonOperations.click_element_byXpath(self, driver, model_tab_xpath)


        # get existing model assigned to device from data base
        existing_selected_model, existing_selected_model_version = CommonOperations.database_connecton(self, mac_address_of_device)

        # search for model
        model_search = driver.find_element_by_xpath("//*[@class='search-group']/input")
        model_search.send_keys(existing_selected_model)
        time.sleep(5)

        # Open correct model to display metrics
        open_model_pencil_xpath = "//*[@id='btn_Edit']"
        get_displayed_model_name = driver.find_element_by_xpath("(//*[@class = 'zui-table table'])[1]/tbody/tr[1]/td[1]").text
        if get_displayed_model_name != existing_selected_model:
            open_model_pencil_xpath = "(//*[@id='btn_Edit'])[2]"
        CommonOperations.click_element_byXpath(self, driver, open_model_pencil_xpath)

        CommonOperations.update_metric(self, driver, metricname, hours, minutes, cov)  # do not give floating point value

        save_model_button_xpath = "//*[@id='btn_Save']"
        CommonOperations.click_element_byXpath(self, driver, save_model_button_xpath)

        success_save_message_xpath = "(//*[@class ='messages'])/ul/li"
        close_button_xpath = "//div[@class='buttonContainer']//div//button[@id='btn_Close']"
        CommonOperations.wait_until_element_visible_byXpath(self, driver, success_save_message_xpath)
        success_save_message = driver.find_element_by_xpath(success_save_message_xpath).text
        print("Message - ", success_save_message)

        if 'Model Details Are Saved Successfully' in success_save_message:
            CommonOperations.click_element_byXpath(self, driver, close_button_xpath)
            print("Model Details Are Saved Successfully")
        else:
            print("Model Details  failed with error - ", success_save_message)

        existing_selected_model_version = existing_selected_model_version + 1

        ConfigurationUpdate.version_check(self, driver, mac_address_of_device, existing_selected_model_version)

    def tearDown(self):
        #driver.close()
        pass


