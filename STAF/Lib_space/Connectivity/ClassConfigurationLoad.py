from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import datetime
import unittest
import pyodbc
import re
import os
import sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils + "\LibSpace")
sys.path.append(dirnameutils + "\LibSpace\Connectivity")
from lib_common_operations import CommonOperations


class ConfigurationLoad(unittest.TestCase):

    def setup(self):
        pass

    def version_check(self, driver, mac_address_of_device, existing_selected_model_version):
        # get version information from carrier smart landing page
            # navigate to landing page
        print(" Time Now = ", datetime.datetime.now())
        print("Waiting for 15 mins - Version verification delay due to CarrierSmart Search Engine")
        time.sleep(900)  # required for carrier smart search engine to populate data in UI
        print(" Time Now = ", datetime.datetime.now())

        driver.refresh()
        logo_xpath = "//div[@class='appLogo']"
        CommonOperations.click_element_byXpath(self, driver, logo_xpath)  # added on 9/aug/2019
        # search chiller to find version information
        CommonOperations.search_chiller(self, driver, mac_address_of_device)

        model_version_landing_page_xpath = "//*[@id='deviceListItems']/cdk-virtual-scroll-viewport/div[1]/div/table/tbody/tr/td[7]/span"
        #CommonOperations.wait_until_element_visible_byXpath(self, driver, chiller_model_version_landing_page_xpath)
        model_version_landing_page = driver.find_element_by_xpath(model_version_landing_page_xpath)
        time.sleep(1)
        chiller_model_version_landing_page_text = model_version_landing_page.text

        print("chiller_model_version_landing_page_text = ", chiller_model_version_landing_page_text)
        time.sleep(10)
        if chiller_model_version_landing_page_text != ' ':
            version_number = re.split('(\d+)', chiller_model_version_landing_page_text)
            print("version_number", version_number, version_number[1])
            self.assertEqual('Success', chiller_model_version_landing_page_text[0:7], "Comparison of Version Text")
            self.assertEqual(int(version_number[1]),existing_selected_model_version, "Comparison of Version Number")
            #  if chiller_model_version_landing_page_text[0:7] == 'Success' \
            #        and int(version_number[1]) == existing_selected_model_version:
            #       print("****CONFIG LOAD/UPDATE SUCCESSFUL****")
            #  else:
            #       print("****CONFIG LOAD/FAILURE FAILURE****")
        else:
            "In Version Check - After driver refresh - Carrier smart landing page not open"

    def config_load(self, mac_address_of_device, modelname):

        driver = CommonOperations.open_carrier_smart(self)

        # Searching for chiller based on MAC address
        serial_number_of_device = CommonOperations.search_chiller(self, driver, mac_address_of_device)
        print("Serial number of Device = ", serial_number_of_device)
        # Finding the serial number
        chiller_serial_number_xpath = "//span[contains(text(),'"+serial_number_of_device+"')]"
        #chiller_serial_number = driver.find_element_by_xpath("//span[contains(text(),'"+serial_number_of_device+"')]")
        CommonOperations.click_element_byXpath(self, driver, chiller_serial_number_xpath)
        #chiller_serial_number.click()
        #time.sleep(10)

        #if chiller_serial_number_xpath.is_displayed():
        #    chiller_serial_number_text = chiller_serial_number_xpath.text
        #    print("get_serial_number", chiller_serial_number_text)
        #    if serial_number_of_device in chiller_serial_number_text:
        #        chiller_serial_number_xpath.click()
        #        print("Chiller Serial number found and is clicked")
        #        print("Waiting for Chiller Page to open")
        #        time.sleep(10)
        #        print("Chiller Page is Opened")
        #    else:
        #        print("chiller serial number not matching in search with - ", chiller_serial_number_text )

        # Opening Chiller Setting Page
        chiller_settings_page_button_xpath = "(//*[@class='button'])[2]"
        #chiller_settings_page_button = driver.find_element_by_xpath("(//*[@class='button'])[2]")
        #chiller_settings_page_button.click()
        CommonOperations.click_element_byXpath(self, driver, chiller_settings_page_button_xpath)
        #time.sleep(10)
        print("Chiller setting page button is clicked")

        # Chiller data screen in Chiller Setting Page
        #chiller_tab_xpath = "//*[@class='settings']/div[1]/div[5]"
        chiller_tab_xpath = "//*[@id='navbarCollapse']/ul/li[2]/a"
        #chiller_tab = driver.find_element_by_xpath("//*[@class='settings']/div[1]/div[5]")
        #chiller_tab.click()
        CommonOperations.click_element_byXpath(self, driver, chiller_tab_xpath)
        #time.sleep(10)
        print("Chiller Design tab is Opened")

        # Scroll down to chiller model version
        CommonOperations.locate_element(self, driver, xpath="//*[contains(text(), 'Chiller Model Version')]")
        print("Scrolled down to chiller model version")

        # Change chiller model
        #option_text1 = modelname   # tbd remove additional assignment of var...
        #option_text2 = '19DV_1471_16SDK'

        chiller_model_selection_xpath = "(//*[@id='drp_Device'])[3]/option[text()='"+modelname+"']"
        #chiller_model_selection.click()
        CommonOperations.click_element_byXpath(self, driver, chiller_model_selection_xpath)
        chiller_model_selection = driver.find_element_by_xpath(
            "(//*[@id='drp_Device'])[3]/option[text()='" + modelname + "']")
        print("modified_chiller_model_selected - ", chiller_model_selection.text)
        #time.sleep(10)

        # Save Chiller configuration
        save_details_xpath = "//*[@id='btn_SaveDetails']"
        CommonOperations.click_element_byXpath(self, driver, save_details_xpath)
        #save_details = driver.find_element_by_xpath("(//*[@id='btn_SaveDetails'])[4]")
        #save_details.click()
        #time.sleep(10)

        success_save_message_xpath = "(//*[@class ='messages'])/ul/li"
        close_button_xpath = "(//*[@id='btn_Close'])[2]"
        #close_button = driver.find_element_by_xpath(close_button_xpath)
        CommonOperations.wait_until_element_visible_byXpath(self, driver, success_save_message_xpath)
        success_save_message = driver.find_element_by_xpath(success_save_message_xpath)
        if success_save_message.is_displayed():
            success_save_message_text = success_save_message.text
            print("Message - ", success_save_message_text)
            if 'Chiller successfully updated' in success_save_message_text:
                CommonOperations.click_element_byXpath(self, driver, close_button_xpath)
                print("Chiller Model configuration is saved successfully")
            else:
                print("Chiller Model configuration failed with error - ", success_save_message_text )

        #Getting model version from database and verify at UI for version after verfication of success..
        existing_selected_model, existing_selected_model_version = CommonOperations.database_connecton(self, mac_address_of_device)
        ConfigurationLoad.version_check(self, driver, mac_address_of_device, existing_selected_model_version)

        return driver

    def tearDown(self):
        pass

