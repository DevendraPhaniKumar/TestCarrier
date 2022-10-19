from Automation_Suite.LibSpace.SELENIUM.BaseClass import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException
import time
import unittest
import pyodbc
import re
import sys
import datetime
import configparser
import os

from Automation_Suite.LibSpace.SELENIUM.Page_locators.CarrierSmart.Connectivity.Connectivity_PageLocators import Connectivity_PageLocators
from Automation_Suite.LibSpace.SELENIUM.BaseClass import Page, WebDriver
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
defaultwaittime = 20  # 20 seconds is given as default for any click operation...
TestParameters = configparser.ConfigParser()
TestParameters.read(dirnameutils + "\\Utilities\\parameters.ini")
loginSleepTime = 10


class CommonOperations(Page):
    global delay

    def __init__(self, driver):
          # super(Alarms, self).__init__(webdriver)
        self.driver = driver

    def search_chiller(self,mac_address_of_device):
        serial_number_of_device = self.get_serial_number(mac_address_of_device).lower() # converting to lower case letters
        time.sleep(loginSleepTime)
        self.click_element(*Connectivity_PageLocators.search_field_id)
        time.sleep(loginSleepTime)
        self.send_keys(*Connectivity_PageLocators.search_field_id, value=mac_address_of_device, clear_first=True,
                       click_first=True)
        self.click_element(*Connectivity_PageLocators.search_button)

        return serial_number_of_device

    def click_and_open_chiller(self, serial_number_of_device):
        time.sleep(loginSleepTime)
        #chiller_serial_number_xpath = self.driver.find_element_by_xpath( "//*[@id='deviceList_scroll']/div[1]/table/tbody/tr[2]/td[3]/span")
        #time.sleep(loginSleepTime)
        #chiller_serial_number_xpath.click()
        self.click_element(*Connectivity_PageLocators.chiller_serial_number_xpath)

        # chiller_serial_number_xpath = "//span[contains(text(),'"+serial_number_of_device+"')]"
        # self.wait_until_text_to_be_present_in_element_byXpath(self.driver,chiller_serial_number_xpath,
        #                                                                   serial_number_of_device)
        # chiller_serial_number = driver.find_element_by_xpath("//span[contains(text(),'"+serial_number_of_device+"')]")
        # if chiller_serial_number.is_displayed():
        #     chiller_serial_number_text = chiller_serial_number.text
        #     print("get_serial_number", chiller_serial_number_text)
        #     if serial_number_of_device in chiller_serial_number_text:
        #         #chiller_serial_number.click()
        #         CommonOperations.click_element_byXpath(self, driver, chiller_serial_number_xpath)
        #         print("Chiller Serial number found and is clicked")
        #         print("Waiting for Chiller Page to open")
        #         time.sleep(5)
        #         print("Chiller Page is Opened")
        #     else:
        #         print("chiller serial number not matching in search with - ", chiller_serial_number_text)
        # else:
        #     print("*********Chiller not found*********")

    def click_and_open_section_details(self):
        # Clicking Chiller Section tab
        chiller_section_page_button = self.driver.find_element_by_id("btn_SectionDetails")
        if chiller_section_page_button.is_displayed():
            chiller_section_page_button.click()
            print("Chiller Section found and is clicked, time is ", datetime.datetime.now())
            time.sleep(10)
        else:
            print("chiller Section not matching in search with - ")

    def open_configuration_section(self):
        time.sleep(5)
        print(datetime.datetime.now())
        right_arrow_xpath = "//i[contains(text(),'chevron_right')]"
        right_arrow = self.driver.find_element_by_xpath("//i[contains(text(),'chevron_right')]")
        #right_arrow.click()
        CommonOperations.click_element_byXpath(self, right_arrow_xpath)
        time.sleep(10)
        chiller_configuration_page_button = self.driver.find_element_by_xpath("//span[contains(text(),'Configuration')]")
        if chiller_configuration_page_button.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(chiller_configuration_page_button).perform()
            chiller_configuration_page_button.click()
            print("Session configuration found and is clicked")
            time.sleep(5)
        else:
            print("Session configuration not found")

    def establish_database_connection(self):
        server = TestParameters.get("TEST_PARAMETERS", "server")
        database = TestParameters.get("TEST_PARAMETERS", "database")
        username = TestParameters.get("TEST_PARAMETERS", "username")
        password = TestParameters.get("TEST_PARAMETERS", "password")
        driver = '{SQL Server}'  # Driver you need to connect to the database
        port = '1433'
        cnn = pyodbc.connect(
            'DRIVER=' + driver + ';PORT=port;SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID='
            + username + ';PWD=' + password)
        return cnn

    def database_connecton(self, mac_address_of_device):
        cnn = CommonOperations.establish_database_connection(self)
        dbcursor = cnn.cursor()

        my_query = "SELECT MODELID FROM DEVICE WHERE RAWMAC = ?"
        dbcursor.execute(my_query, mac_address_of_device)
        existing_selected_model_id = 0
        for model_id in dbcursor.fetchall():
            existing_selected_model_id = (model_id[0])
            print("DataType of model id = ", type(model_id[0]))
        print("Model id = ", existing_selected_model_id)

        my_query = "SELECT MODELNAME FROM MODEL WHERE MODELID = %s"
        dbcursor.execute(my_query % existing_selected_model_id)
        existing_selected_model = ' '
        for model_name in dbcursor.fetchall():
            existing_selected_model = model_name[0]
            print(type(model_name[0]))
            existing_selected_model_version = 0
        print(existing_selected_model)

        my_query = "SELECT Max(Version) FROM MODELCONFIGVERSION WHERE MODELID = %s"
        dbcursor.execute(my_query % existing_selected_model_id)
        for version in dbcursor.fetchall():
            existing_selected_model_version = version[0]
            print("existing_selected_model_version", type(version[0]))
        print("Model version = ", existing_selected_model_version)
        print("DataType of Model version = ", type(existing_selected_model_version))
        dbcursor.close()
        del dbcursor
        cnn.close()
        return existing_selected_model, existing_selected_model_version

    def get_serial_number(self, mac_address_of_device):
        cnn = CommonOperations.establish_database_connection(self)
        dbcursor = cnn.cursor()

        my_query = "SELECT businesskey FROM DEVICE WHERE RAWMAC = ?"
        dbcursor.execute(my_query, mac_address_of_device)
        existing_serial_number = ''
        for model_id in dbcursor.fetchall():
            existing_serial_number = (model_id[0])
            print(type(model_id[0]))
        print(existing_serial_number)
        dbcursor.close()
        del dbcursor
        cnn.close()
        return existing_serial_number

    def update_metric(self, metric_key, hours_value, mins_value, cov_threshold):
        search_metric_key = self.driver.find_element_by_xpath("//*[@class='search-group pad-lft10']/input")
        # search metric key
        search_metric_key.clear()
        search_metric_key.send_keys(metric_key)
        # open metric information
        edit_metric_pencil = self.driver.find_element_by_xpath("//*[@id='btn_EditMetric']")
        edit_metric_pencil.click()
        print("Edit metric information is open")
        # update telemetry
        if hours_value > 0 or mins_value > 0:
            frequency_radio_button = self.driver.find_element_by_xpath("(//*[@class ='col-md-5'])[2]/label/input")
            frequency_radio_button.click()
            frequency_hours = self.driver.find_element_by_xpath("(//*[@class ='col-md-7'])/div/input[1]")
            frequency_minutes = self.driver.find_element_by_xpath("(//*[@class ='col-md-7'])/div/input[2]")
            frequency_hours.clear()
            frequency_hours.send_keys(hours_value)
            frequency_minutes.clear()
            frequency_minutes.send_keys(mins_value)

        if cov_threshold > 0:
            change_of_value_radio_button = self.driver.find_element_by_xpath("(//*[@class ='col-md-5'])[3]/label/input")
            change_of_value_radio_button.click()
            change_of_value = self.driver.find_element_by_xpath("(//*[@class ='col-md-6'])[12]/div/input")
            change_of_value.clear()
            change_of_value.send_keys(str(cov_threshold))

        if (hours_value > 0 or mins_value > 0) and cov_threshold > 0:
            both_radio_button = self.driver.find_element_by_xpath("(//*[@class ='col-md-11'])[4]/label/input")
            both_radio_button.click()

        save_edit_metric_button = self.driver.find_element_by_xpath("//*[@id='btn_NewModel']")
        save_edit_metric_button.click()
        return

    def locate_element(self, xpath):
        scroll_to_element = self.driver.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        print("locate element start wait time = ", datetime.datetime.now())
        WebDriverWait(self.driver, defaultwaittime).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        print("locate element end wait time = ", datetime.datetime.now())
        actions.move_to_element(scroll_to_element).perform()
        print("element is located")
        #time.sleep(5)

    def click_and_open_evaporator_section(self):
        # clicking evaporator section page
        CommonOperations.wait_until_text_to_be_present_in_element_byXpath(self,
                                                             "//span[contains(text(),'Evaporator')]",'Evaporator')
        evaporator_section_button = self.driver.find_element_by_xpath("//span[contains(text(),'Evaporator')]")
        if evaporator_section_button.is_displayed():
            evaporator_section_button.click()
            print("Evaporator Section is open")
            time.sleep(5)
        else:
            print("Evaporator Section not open")

    def click_open_condenser_section(self):
        # clicking condenser section page
        CommonOperations.wait_until_text_to_be_present_in_element_byXpath(self,
                                                                          "//span[contains(text(),'Condenser')]",
                                                                          'Condenser')
        evaporator_section_button = self.driver.find_element_by_xpath("//span[contains(text(),'Condenser')]")
        if evaporator_section_button.is_displayed():
            evaporator_section_button.click()
            print("condenser Section is open")
            time.sleep(5)
        else:
            print("Condenser Section not open")

    def get_binary_metric_name_value(self, xpath):
        #not completed
        metric_xpath = self.driver.find_element_by_xpath(xpath)
        metric_list = re.split('(\d+)', metric_xpath.text)
        metric_name = metric_list[0].strip('\n')
        metric_value = float(metric_list[1])
        return metric_name, metric_value

    def get_analog_metric_name_value(self, metric_name):
        i = 1
        element_value = 0
        element_name = "element_initialization"
        while not element_name == metric_name :                             # changed on 14-11-2019 from in to ==
            zpath = '(//*[@class ="metricStick"])[{0}]/div'.format(str(i))
            traversing_metric = self.driver.find_element_by_xpath(zpath)
            metric_list = re.split('(\d+)', traversing_metric.text)
            if len(metric_list) >= 2:
                element_name = metric_list[0].strip('\n')
                element_value = float(metric_list[1])
            if i < 115:
                i = i + 1
            else:
                break
        return element_name, element_value

    def set_analog_metric_value(self, metric_name, point_value):
        i = 1
        element_value = 0
        element_name = "element_initialization"
        zpath = '(//*[@class ="metricStick"])[{0}]'.format(str(i))
        while not element_name in metric_name:
            zpath = '(//*[@class ="metricStick"])[{0}]'.format(str(i))
            ypath = zpath + "/div"
            traversing_metric = self.driver.find_element_by_xpath(ypath)
            metric_list = re.split('(\d+)', traversing_metric.text)
            if len(metric_list) >= 2:
                element_name = metric_list[0].strip('\n')
                element_value = float(metric_list[1])
            if i < 68:
                i = i + 1
            else:
                break

        # edit pencil
        update_pencil_string = zpath + "/span/i"
        #CommonOperations.locate_element(self,driver,update_pencil_string)
        update_pencil_xpath = self.driver.find_element_by_xpath(update_pencil_string)
        actions = ActionChains(self.driver)
        actions.move_to_element(update_pencil_xpath).perform()
        update_pencil_xpath.click()
        time.sleep(5)

        # edit value
        update_value_string = zpath + "/span/popover-content/div/div[3]/div/input"
        #update_value_xpath = driver.find_element_by_xpath("//div[@class='popover right in']//input[@id='new_value']")
        update_value_xpath = self.driver.find_element_by_xpath(update_value_string)
        actions = ActionChains(self.driver)
        actions.move_to_element(update_value_xpath).perform()

        update_value_xpath.click()
        update_value_xpath.clear()
        update_value_xpath.send_keys(str(point_value))

        # Click Update button
        update_button_xpath = self.driver.find_element_by_xpath("//div[@class='popover right in']//button[@id='btn_Update']")
        actions = ActionChains(self.driver)
        actions.move_to_element(update_button_xpath).perform()
        update_button_xpath.click()
        time.sleep(5)

    def get_alarm_details(self,total_no_of_alarms, alarm_description):
        i = 1
        element_name = "alarm description text"
        #zpath = '//div[@id="chiller"]/div[{0}]'.format(str(i))
        zpath = '//*[@id="chiller"]/cdk-virtual-scroll-viewport/div[1]/div/table/tbody/tr[{0}]'.format(str(i))
        while element_name not in alarm_description:
            if i <= total_no_of_alarms:
                # zpath = '//div[@id="chiller"]/div[{0}]'.format(str(i))
                zpath = '//*[@id="chiller"]/cdk-virtual-scroll-viewport/div[1]/div/table/tbody/tr[{0}]'.format(str(i))
                # ypath = zpath + "/span[2]/span"
                ypath = zpath + "/td[2]/span"
                traversing_metric = self.driver.find_element_by_xpath(ypath)
                element_name = traversing_metric.text
                print("Alarm text - ", alarm_description, " searching next element in alarm list", i)
                i = i + 1
            else:
                print("Alarm text not found", alarm_description, " last element in alarm list", i)
                break
        #alarm_date_xpath = zpath + "/span[3]/span"
        alarm_date_xpath = zpath + "/td[3]/span"
        cs_alarm_date = self.driver.find_element_by_xpath(alarm_date_xpath).text
        print("cs_alarm_date:", cs_alarm_date)
        #alarm_time_xpath = zpath + "/span[4]/span"
        alarm_time_xpath = zpath + "/td[4]/span"
        cs_alarm_time = self.driver.find_element_by_xpath(alarm_time_xpath).text
        print("cs_alarm_time:", cs_alarm_time)
        return cs_alarm_date, cs_alarm_time

    def get_date_time_split(self, alarm_generation_time,cs_alarm_time):
        #alarm_generation_time = '08:44p'
        #cs_alarm_time = '6:42p IST'
        expected = re.split('(\d+)', alarm_generation_time)
        print(expected)
        temp = cs_alarm_time[:-4]
        print("temp", temp)
        actual = re.split('(\d+)', temp)
        print(actual)
        return expected, actual

    def click_element_byXpath(self, xpath):
        WebDriverWait(self.driver, defaultwaittime).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        #WebDriverWait(driver, defaultwaittime).until(EC.element_to_be_clickable((By.XPATH, xpath))).submit()
        print("Clicked element @ ", xpath)

    def click_element_byID(self, id):
        WebDriverWait(self.driver, defaultwaittime).until(EC.element_to_be_clickable((By.ID, id))).click()
        print("Clicked element @ ", id)

    def wait_until_element_visible_byXpath(self, xpath):
        WebDriverWait(self.driver, defaultwaittime).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        print("Visible element @ ", xpath)

    def wait_until_text_to_be_present_in_element_byXpath(self, xpath, text):
        WebDriverWait(self.driver, defaultwaittime).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))
        print("Text is present in element @ ", xpath, "Text = ", text)

    def wait_until_text_to_be_present_in_element_value_byXpath(self, xpath, text):
        WebDriverWait(self.driver, defaultwaittime).until(EC.text_to_be_present_in_element_value((By.XPATH, xpath), text))
        print("Text is present in element value @ ", xpath, "Text = ", text)
