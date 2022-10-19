from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest
import pyodbc
import re
import sys
import datetime
import configparser
import os
#import pyautogui
dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils + "\Lib_Space")
sys.path.append(dirnameutils + "\Lib_Space\Connectivity")
#from BaseClass import WebDriver_test


dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
defaultwaittime = 60  # 20 seconds is given as default for any click operation...
TestParameters = configparser.ConfigParser()
TestParameters.read(dirnameutils + "\\Utilities\\parameters.ini")
loginSleepTime = 2


class CommonOperations:

    def setup(self):
        pass

    def login(self, driver):
        # Added by pramodh on date 11 June 2020
        carrier_logo_xpath ="//*[@id= 'i0281']/div/div/div[1]/div[2]/div[1]/img"
        email_address_id = 'i0116'
        logo_xpath = "//div[@class='appLogo']"
        next_button_id= 'idSIButton9'
        password_id = 'i0118'
        sign_in_id = 'idSIButton9'
        email = TestParameters.get("TEST_PARAMETERS", "email")

        user = TestParameters.get("TEST_PARAMETERS", "user")
        passW = TestParameters.get("TEST_PARAMETERS", "passW")
        sign_in_organization_id = "UTCAD"
        choose_user_to_login = 'otherTileText'
        enter_username = 'i0116'
        next_button = "idSIButton9"

        try:
            CommonOperations.wait_until_element_visible_byXpath(self, driver, carrier_logo_xpath)
            if driver.find_element_by_id(carrier_logo_xpath).is_displayed():
                id_enter_useremailaddress = driver.find_element_by_id(email_address_id)
                id_enter_useremailaddress.clear()
                id_enter_useremailaddress.send_keys(email)
                time.sleep(2)
                CommonOperations.click_element_byID(self, driver, next_button_id)
                time.sleep(2)
                id_enter_userpassword = driver.find_element_by_id(password_id)
                id_enter_userpassword.clear()
                id_enter_userpassword.send_keys(passW)
                time.sleep(2)
                CommonOperations.click_element_byID(self, driver, next_button_id)
        except (NoSuchElementException, StaleElementReferenceException):
            pass

        for x in range(3):
            print("Login Iteration Count", x + 1, " Time Now = ", datetime.datetime.now())
            try:
                logo = driver.find_element_by_xpath(logo_xpath)
            except (NoSuchElementException, StaleElementReferenceException):
                try:
                    time.sleep(10)
                    if driver.find_element_by_id(sign_in_organization_id).is_displayed():
                        CommonOperations.click_element_byID(self, driver, sign_in_organization_id)
                        id_enter_username = driver.find_element_by_id(enter_username)
                        id_enter_username.clear()
                        id_enter_username.send_keys(user)
                        CommonOperations.click_element_byID(self, driver, next_button)
                    #if driver.find_element_by_id("i0116").is_displayed():
                    #    username = driver.find_element_by_id("i0116")
                        #next_button = driver.find_element_by_id("idSIButton9")
                        #next_button_id = "idSIButton9"
                        #username.clear()
                        #username.send_keys(user)
                        #CommonOperations.click_element_byID(self, driver, next_button_id)

                except (NoSuchElementException, StaleElementReferenceException):
                    print(x, " attempt of LOGIN Failed")
                time.sleep(loginSleepTime)

                try:
                    if driver.find_element_by_id("userNameInput").is_displayed():
                        username = driver.find_element_by_id("userNameInput")
                        password = driver.find_element_by_id("passwordInput")
                        #signin_button = driver.find_element_by_id("submitButton")
                        signin_button_id = "submitButton"
                        username.clear()
                        username.send_keys(user)
                        password.clear()
                        password.send_keys(passW)
                        CommonOperations.click_element_byID(self, driver, signin_button_id)
                        #signin_button.click()
                except (NoSuchElementException, StaleElementReferenceException):
                    print("LOGIN - Failed 1st attempt of UTC N/W")
                time.sleep(loginSleepTime)
                print(x, " loop is login over :(")

    def open_carrier_smart(self):

        TestParameters = configparser.ConfigParser()
        TestParameters.read(dirnameutils + "\\Utilities\\parameters.ini")
        chrome_driver_path = TestParameters.get("TEST_PARAMETERS", "chromedriver")
        target_url = TestParameters.get("TEST_PARAMETERS", "target_url")

        #chrome_driver_path = r"D:\!D-Drive\python\ConnectedChillers\Automation\Automation_Suite\Utilities\WEB_Drivers\chromedriver.exe"
        #driver = WebDriver_test.same_driver
        capabilities = {'chromeOptions': {'useAutomationExtension': False}}
        driver = webdriver.Chrome(chrome_driver_path, desired_capabilities=capabilities)

        driver.maximize_window()
        driver.get(target_url)
        #driver.get("https://smartchillerwebdev-test.azurewebsites.net/")
        #time.sleep(10)

        CommonOperations.login(self, driver)

        #print("Waiting 10 seconds for google pages to load")
        #time.sleep(10)
        print("Carrier Smart Landing Page Loaded")

        # Click accept for Cookies Accept button at bottom of Carrier Smart Page
        try:

            cookies_accept_button_xpath = "//*[@class='termsOfUse']/button"
            cookies_accept_button = driver.find_element_by_xpath(cookies_accept_button_xpath)
            CommonOperations.click_element_byXpath(self, driver, cookies_accept_button_xpath)
            #cookies_accept_button.click()
            print("Cookies accept button is clicked - hence banner disabled")
        except (NoSuchElementException, StaleElementReferenceException):
            print("Accept button not there hence proceeding")
        return driver

    def search_chiller(self, driver, mac_address_of_device):
        chillers_loaded_InView_xpath = "//div[contains(text(),'In View')]"
        CommonOperations.wait_until_element_visible_byXpath(self, driver, chillers_loaded_InView_xpath)

        serial_number_of_device = CommonOperations.get_serial_number(self, mac_address_of_device).lower() # converting to lower case letters
        mac_address_search_field = driver.find_element_by_xpath(".//*[@class='searchPattern']/input")
        mac_address_search_field.send_keys(mac_address_of_device)
        # time.sleep(5)
        # search_chiller_button = driver.find_element_by_xpath(".//*[@class='search']/i")
        # search_chiller_button.click()
        search_chiller_button_xpath = ".//*[@class='search']/i"
        CommonOperations.click_element_byXpath(self, driver, search_chiller_button_xpath)
        one_chiller_inView_xpath = "//div[contains(text(),'1 In View')]"
        CommonOperations.wait_until_element_visible_byXpath(self, driver, one_chiller_inView_xpath)
        # Scrolling to Chiller displayed in Carrier smart
        CommonOperations.locate_element(self, driver, xpath="//*[@id='deviceListItems']") #changed on 9/aug/2019
        return serial_number_of_device

    def click_and_open_chiller(self, driver, serial_number_of_device):
        time.sleep(10)
        chiller_serial_number_xpath = "//span[contains(text(),'"+serial_number_of_device+"')]"
        chiller_serial_number = driver.find_element_by_xpath("//span[contains(text(),'"+serial_number_of_device+"')]")
        if chiller_serial_number.is_displayed():
            chiller_serial_number_text = chiller_serial_number.text
            print("get_serial_number", chiller_serial_number_text)
            if serial_number_of_device in chiller_serial_number_text:
                #chiller_serial_number.click()
                CommonOperations.click_element_byXpath(self, driver, chiller_serial_number_xpath)
                print("Chiller Serial number found and is clicked")
                print("Waiting for Chiller Page to open")
                time.sleep(5)
                print("Chiller Page is Opened")
            else:
                print("chiller serial number not matching in search with - ", chiller_serial_number_text)
        else:
            print("*********Chiller not found*********")

    def click_and_open_section_details(self, driver):
        # Clicking Chiller Section tab
        chiller_section_page_button = driver.find_element_by_id("btn_SectionDetails")
        if chiller_section_page_button.is_displayed():
            chiller_section_page_button.click()
            print("Chiller Section found and is clicked, time is ", datetime.datetime.now())
            time.sleep(10)
        else:
            print("chiller Section not matching in search with - ")

    def open_configuration_section(self, driver):
        time.sleep(5)
        print(datetime.datetime.now())
        right_arrow_xpath = "//i[contains(text(),'chevron_right')]"
        right_arrow = driver.find_element_by_xpath("//i[contains(text(),'chevron_right')]")
        #right_arrow.click()
        CommonOperations.click_element_byXpath(self, driver, right_arrow_xpath)
        time.sleep(10)
        chiller_configuration_page_button = driver.find_element_by_xpath("//span[contains(text(),'Configuration')]")
        if chiller_configuration_page_button.is_displayed():
            actions = ActionChains(driver)
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
        print(existing_selected_model)

        my_query = "SELECT Max(Version) FROM MODELCONFIGVERSION WHERE MODELID = %s"
        dbcursor.execute(my_query % existing_selected_model_id)
        existing_selected_model_version = 0
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

    def update_metric(self, driver, metric_key, hours_value, mins_value, cov_threshold):
        search_metric_key = driver.find_element_by_xpath("//*[@class='search-group pad-lft10']/input")
        # search metric key
        search_metric_key.clear()
        search_metric_key.send_keys(metric_key)
        # open metric information
        edit_metric_pencil = driver.find_element_by_xpath("//*[@id='btn_EditMetric']")
        edit_metric_pencil.click()
        print("Edit metric information is open")
        # update telemetry
        if hours_value > 0 or mins_value > 0:
            frequency_radio_button = driver.find_element_by_xpath("(//*[@class ='col-md-5'])[2]/label/input")
            frequency_radio_button.click()
            frequency_hours = driver.find_element_by_xpath("(//*[@class ='col-md-7'])/div/input[1]")
            frequency_minutes = driver.find_element_by_xpath("(//*[@class ='col-md-7'])/div/input[2]")
            frequency_hours.clear()
            frequency_hours.send_keys(hours_value)
            frequency_minutes.clear()
            frequency_minutes.send_keys(mins_value)

        if cov_threshold > 0:
            change_of_value_radio_button = driver.find_element_by_xpath("(//*[@class ='col-md-5'])[3]/label/input")
            change_of_value_radio_button.click()
            change_of_value = driver.find_element_by_xpath("(//*[@class ='col-md-6'])[12]/div/input")
            change_of_value.clear()
            change_of_value.send_keys(str(cov_threshold))

        if (hours_value > 0 or mins_value > 0) and cov_threshold > 0:
            both_radio_button = driver.find_element_by_xpath("(//*[@class ='col-md-11'])[4]/label/input")
            both_radio_button.click()

        save_edit_metric_button = driver.find_element_by_xpath("//*[@id='btn_NewModel']")
        save_edit_metric_button.click()
        return

    def locate_element(self, driver, xpath):
        scroll_to_element = driver.find_element_by_xpath(xpath)
        actions = ActionChains(driver)
        print("locate element start wait time = ", datetime.datetime.now())
        WebDriverWait(driver, defaultwaittime).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        print("locate element end wait time = ", datetime.datetime.now())
        actions.move_to_element(scroll_to_element).perform()
        print("element is located")
        #time.sleep(5)

    def click_and_open_evaporator_section(self,driver):
        # clicking evaporator section page
        evaporator_section_button = driver.find_element_by_xpath("//span[contains(text(),'Evaporator')]")
        if evaporator_section_button.is_displayed():
            evaporator_section_button.click()
            print("Evaporator Section is open")
            time.sleep(5)
        else:
            print("Evaporator Section not open")

    def click_open_condenser_section(self, driver):
        # clicking condenser section page
        evaporator_section_button = driver.find_element_by_xpath("//span[contains(text(),'Condenser')]")
        if evaporator_section_button.is_displayed():
            evaporator_section_button.click()
            print("condenser Section is open")
            time.sleep(5)
        else:
            print("Condenser Section not open")

    def get_binary_metric_name_value(self, driver, xpath):
        #not completed
        metric_xpath = driver.find_element_by_xpath(xpath)
        metric_list = re.split('(\d+)', metric_xpath.text)
        metric_name = metric_list[0].strip('\n')
        metric_value = float(metric_list[1])
        return metric_name, metric_value

    def get_analog_metric_name_value(self, driver, metric_name):
        i = 1
        element_value = 0
        element_name = "element_initialization"
        while not element_name == metric_name :                             # changed on 14-11-2019 from in to ==
            zpath = '(//*[@class ="metricStick"])[{0}]/div'.format(str(i))
            traversing_metric = driver.find_element_by_xpath(zpath)
            metric_list = re.split('(\d+)', traversing_metric.text)
            if len(metric_list) >= 2:
                element_name = metric_list[0].strip('\n')
                element_value = float(metric_list[1])
            if i < 115:
                i = i + 1
            else:
                break
        return element_name, element_value

    def set_analog_metric_value(self, driver, metric_name, point_value):
        i = 1
        element_value = 0
        element_name = "element_initialization"
        zpath = '(//*[@class ="metricStick"])[{0}]'.format(str(i))
        while not element_name in metric_name:
            zpath = '(//*[@class ="metricStick"])[{0}]'.format(str(i))
            ypath = zpath + "/div"
            traversing_metric = driver.find_element_by_xpath(ypath)
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
        update_pencil_xpath = driver.find_element_by_xpath(update_pencil_string)
        actions = ActionChains(driver)
        actions.move_to_element(update_pencil_xpath).perform()
        update_pencil_xpath.click()
        time.sleep(5)

        # edit value
        update_value_string = zpath + "/span/popover-content/div/div[3]/div/input"
        #update_value_xpath = driver.find_element_by_xpath("//div[@class='popover right in']//input[@id='new_value']")
        update_value_xpath = driver.find_element_by_xpath(update_value_string)
        actions = ActionChains(driver)
        actions.move_to_element(update_value_xpath).perform()

        update_value_xpath.click()
        update_value_xpath.clear()
        update_value_xpath.send_keys(str(point_value))

        # Click Update button
        update_button_xpath = driver.find_element_by_xpath("//div[@class='popover right in']//button[@id='btn_Update']")
        actions = ActionChains(driver)
        actions.move_to_element(update_button_xpath).perform()
        update_button_xpath.click()
        time.sleep(5)

    def get_alarm_details(self, driver, total_no_of_alarms, alarm_description):
        i = 1
        element_name = "alarm description text"
        zpath = '//div[@id="chiller"]/div[{0}]'.format(str(i))
        while element_name not in alarm_description:
            zpath = '//div[@id="chiller"]/div[{0}]'.format(str(i))
            ypath = zpath + "/span[2]/span"
            traversing_metric = driver.find_element_by_xpath(ypath)
            element_name = traversing_metric.text
            if i < total_no_of_alarms:
                print("Alarm text not found - ", alarm_description, " searching next element in alarm list", i)
                i = i + 1
            else:
                print("Alarm text not found", alarm_description, " last element in alarm list", i)
                break
        alarm_date_xpath = zpath + "/span[3]/span"
        cs_alarm_date = driver.find_element_by_xpath(alarm_date_xpath).text
        alarm_time_xpath = zpath + "/span[4]/span"
        cs_alarm_time = driver.find_element_by_xpath(alarm_time_xpath).text
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

    def click_element_byXpath(self, driver, xpath):
        WebDriverWait(driver, defaultwaittime).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        print("Clicked element @ ", xpath)

    def click_element_byID(self, driver, id):
        WebDriverWait(driver, defaultwaittime).until(EC.element_to_be_clickable((By.ID, id))).click()
        print("Clicked element @ ", id)

    def wait_until_element_visible_byXpath(self, driver, xpath):
        WebDriverWait(driver, defaultwaittime).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        print("Visible element @ ", xpath)

    def wait_until_text_to_be_present_in_element_byXpath(self, driver, xpath, text):
        WebDriverWait(driver, defaultwaittime).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))
        print("Text is present in element @ ", xpath, "Text = ", text)

    def wait_until_text_to_be_present_in_element_value_byXpath(self, driver, xpath, text):
        WebDriverWait(driver, defaultwaittime).until(EC.text_to_be_present_in_element_value((By.XPATH, xpath), text))
        print("Text is present in element value @ ", xpath, "Text = ", text)

    def tearDown(self):
        pass
