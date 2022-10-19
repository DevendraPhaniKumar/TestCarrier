import os
import sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
sys.path.append(dirnameutils+'\Selenium_Lib')
from selenium.webdriver.common.keys import Keys
from Selenium_Lib.BaseClass import Page
from Page_locators.ChecklistPage_locators import *
from Page_locators.MainPage_locators import *
from Page_locators.HomePage_locatars import *
from Page_locators.LoginPage_locatars import *
from Page_locators.ConnectPage_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes
driver = object
delay = 45

class LoginPage(Page):
    def getdriver(self, webdriver):
        global driver, delay
        driver = webdriver

    def wait(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.TITLE))
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print("Loading took too much time!")
            filename1 = "HomePage"
            self.screen_capture(filename1)

    def enter_email(self, user):
        self.wait()
        self.find_element(*LoginPageLocatars.EMAIL).clear()
        self.find_element(*LoginPageLocatars.EMAIL).send_keys(user)

    def enter_password(self, user):
        self.find_element(*LoginPageLocatars.PASSWORD).clear()
        self.find_element(*LoginPageLocatars.PASSWORD).send_keys(user)

    def click_login_button(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.SUBMIT))
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print("Loading took too much time!")
        time.sleep(0.5)
        self.find_element(*LoginPageLocatars.SUBMIT).click()
        print('Successfully logged in')

    def get_error_msg(self):
        try:
            element_present = EC.presence_of_element_located((LoginPageLocatars.SUBMIT))
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print("Loading took too much time!")
        time.sleep(3)
        return self.find_element(*LoginPageLocatars.invalid_user_error).text

    def logout(self):
        self.find_element(*LoginPageLocatars.user_options).click()
        self.find_element(*LoginPageLocatars.logout).click()

class HomePage(Page):
    global driver, delay

    def wait(self):
        try:
            element_present = EC.presence_of_element_located((HomePageLocatars.TITLE))
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print("Loading took too much time!")

    def user_verion_info(self):
        self.wait()
        title = self.find_element(*HomePageLocatars.TITLE).text
        user = self.find_element(*HomePageLocatars.USER).text
        print('Title & Version = ', title)
        print('User = ', user.split(',')[-1])


class ConnectPage(Page):
    global driver, delay
    def wait(self):
        try:
            element_present = EC.presence_of_element_located((ConnectPageLocators.TITLE))
            WebDriverWait(driver, delay).until(element_present)
            print("Home Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

    def enter_page(self):
        self.find_element(*ConnectPageLocators.connection).click()

    def select_protocol(self):
        try:
            element_present = EC.presence_of_element_located(ConnectPageLocators.connection_protocol_LOE)
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print("Loading page took too long!")
        time.sleep(2)
        ele = self.find_elements(*ConnectPageLocators.connection_protocol_LOE)
        ele[0].click()
        self.find_element(*ConnectPageLocators.bacnet_protocol).click()

    def select_bus(self, bus):
        self.find_element(*ConnectPageLocators.bus).clear()
        self.find_element(*ConnectPageLocators.bus).send_keys(bus)
        self.find_element(*ConnectPageLocators.bus).send_keys(Keys.ENTER)

    def select_baudrate(self, baud):
        element = self.find_elements(*ConnectPageLocators.baudrate_LOE)
        element[1].click()
        self.find_element(*ConnectPageLocators.default_baud).click()

    def connect_ccn(self):
        self.find_element(*ConnectPageLocators.connect).click()
        try:
            element_present = EC.presence_of_element_located((ConnectPageLocators.loading))
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print("Please check the connection")

    def toggle_refresh(self):
        try:
            element_present = EC.presence_of_element_located((ConnectPageLocators.overview_opt))
            WebDriverWait(driver, delay).until(element_present)
        except TimeoutException:
            print("Loading took too much time!")
        self.find_element(*ConnectPageLocators.refresh).click()

    def read_points(self, ccn_point):
        return self.find_element(*ConnectPageLocators.ccn_point).text

class ChecklistPage(Page):
    def checklist(self):
        try:
            element_present = EC.presence_of_element_located((ChecklistPageLocators.checklist))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Loading took too much time!")
        self.find_element(*ChecklistPageLocators.checklist).click()

    def new_form(self):
        try:
            element_present = EC.presence_of_element_located((ChecklistPageLocators.create_new_form_text))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Loading took too much time!")
        time.sleep(2)
        self.find_element(*ChecklistPageLocators.new_form).click()

    def find_form(self, customer_name, form_type):
        try:
            element_present = EC.presence_of_element_located((ChecklistPageLocators.search))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Loading took too much time!")
        i = 1
        while i:
            # try:
            path = ('xpath', ChecklistPageLocators.customer_name[-1]+'/div['+str(i)+']/div[1]')
            text = self.find_element(*path).text
            if text == customer_name:
                path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(i) + ']/div[4]')
                text = self.find_element(*path).text
                if text == form_type:
                    return i
            i = i+1
            # except:
            #     print 'Please check the input data'
            #     break

    def existing_form(self):
        self.find_element(*ChecklistPageLocators.existing_form).click()

    def edit_form(self, form_type, customer_name):
        index = self.find_form(form_type, customer_name)
        path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[1]/a/i')
        self.find_element(*path).click()

    def mail_form(self, form_type, customer_name):
        index = self.find_form(form_type, customer_name)
        path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[2]/a/i')
        self.find_element(*path).click()

    def export_form(self, form_type, customer_name):
        index = self.find_form(form_type, customer_name)
        path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[3]/a/i')
        self.find_element(*path).click()

    def delete_form(self, form_type, customer_name):
        index = self.find_form(form_type, customer_name)
        path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[4]/a/i')
        self.find_element(*path).click()


class Startup_Form(Page):
    def startup_form(self):
        self.find_element(*ChecklistPageLocators.startup_form).click()

    def job_name(self, job_name):
        self.find_element(*ChecklistPageLocators.job_name).send_keys(job_name)
        self.find_element(*ChecklistPageLocators.job_name).send_keys(Keys.ENTER)

    def job_no(self, job_no):
        self.find_element(*ChecklistPageLocators.job_no).send_keys(job_no)
        self.find_element(*ChecklistPageLocators.job_no).send_keys(Keys.ENTER)

    def cust_name(self, custname):
        self.find_element(*ChecklistPageLocators.cust_name).send_keys(custname)
        self.find_element(*ChecklistPageLocators.cust_name).send_keys(Keys.ENTER)

    def address(self, address):
        self.find_element(*ChecklistPageLocators.address).send_keys(address)
        self.find_element(*ChecklistPageLocators.address).send_keys(Keys.ENTER)

    def model_no(self, model_no):
        # Click on the select drop down button
        self.find_element(*ChecklistPageLocators.model_no).click()
        # get the dropdown handle
        dropdown = self.find_element(*ChecklistPageLocators.model_no_dropdown)
        # loopby each option in the drop down and check for a match and then select
        for option in dropdown.find_elements_by_tag_name('li'):
            if option.text == model_no:
                option.click()
                break

    def serial_no(self, serial_no):
        self.find_element(*ChecklistPageLocators.serial_no).send_keys(serial_no)
        self.find_element(*ChecklistPageLocators.serial_no).send_keys(Keys.ENTER)

    def create_form(self):
        self.find_element(*ChecklistPageLocators.create_form).click()
        time.sleep(2)
        try:
            element_present = EC.presence_of_element_located(ChecklistPageLocators.caution)
            WebDriverWait(driver, 45).until(element_present)
        except TimeoutException:
            print("Loading took too much time!")
        self.find_element(*ChecklistPageLocators.proceed).click()
        time.sleep(2)

    def design_data(self):
        self.find_element(*ChecklistPageLocators.design_data).click()

    def write_design_info_data(self, Data):
        self.find_element(*ChecklistPageLocators.dd_cooler_ref_tons).send_keys(Data['cooler_ref_tons'])
        self.find_element(*ChecklistPageLocators.dd_cooler_ref_tons).send_keys(Keys.ENTER)
        print('Written Design Information :: Cooler :: Tons =', Data['cooler_ref_tons'])

        self.find_element(*ChecklistPageLocators.dd_cooler_ref_brine).send_keys(Data['cooler_ref_brine'])
        self.find_element(*ChecklistPageLocators.dd_cooler_ref_brine).send_keys(Keys.ENTER)
        print('Written Design Information :: Cooler :: Brine =', Data['cooler_ref_brine'])

        self.find_element(*ChecklistPageLocators.dd_cooler_ref_flowrate).send_keys(Data['cooler_ref_flowrate'])
        self.find_element(*ChecklistPageLocators.dd_cooler_ref_flowrate).send_keys(Keys.ENTER)
        print('Written Design Information :: Cooler :: Flow Rate =', Data['cooler_ref_flowrate'])

        self.find_element(*ChecklistPageLocators.dd_cooler_ref_presdrop).send_keys(Data['cooler_ref_presdrop'])
        self.find_element(*ChecklistPageLocators.dd_cooler_ref_presdrop).send_keys(Keys.ENTER)
        print('Written Design Information :: Cooler :: Pressure Drop =', Data['cooler_ref_presdrop'])

        self.find_element(*ChecklistPageLocators.dd_cooler_ref_pass).send_keys(Data['cooler_ref_pass'])
        self.find_element(*ChecklistPageLocators.dd_cooler_ref_pass).send_keys(Keys.ENTER)
        print('Written Design Information :: Cooler :: Pass =', Data['cooler_ref_pass'])

        self.find_element(*ChecklistPageLocators.dd_cooler_ref_suctemp).send_keys(Data['cooler_ref_suctemp'])
        self.find_element(*ChecklistPageLocators.dd_cooler_ref_suctemp).send_keys(Keys.ENTER)
        print('Written Design Information :: Cooler :: Suction Temp =', Data['cooler_ref_suctemp'])

        self.find_element(*ChecklistPageLocators.dd_cooler_ref_tempin).send_keys(Data['cooler_ref_tempin'])
        self.find_element(*ChecklistPageLocators.dd_cooler_ref_tempin).send_keys(Keys.ENTER)
        print('Written Design Information :: Cooler :: Temp IN =', Data['cooler_ref_tempin'])

        self.find_element(*ChecklistPageLocators.dd_cooler_ref_tempout).send_keys(Data['cooler_ref_tempout'])
        self.find_element(*ChecklistPageLocators.dd_cooler_ref_tempout).send_keys(Keys.ENTER)
        print('Written Design Information :: Cooler :: Temp OUT =', Data['cooler_ref_tempout'])

        self.find_element(*ChecklistPageLocators.dd_condenser_ref_tons).send_keys(Data['condenser_ref_tons'])
        self.find_element(*ChecklistPageLocators.dd_condenser_ref_tons).send_keys(Keys.ENTER)
        print('Written Design Information :: Condenser :: Tons =', Data['condenser_ref_tons'])

        self.find_element(*ChecklistPageLocators.dd_condenser_ref_brine).send_keys(Data['condenser_ref_brine'])
        self.find_element(*ChecklistPageLocators.dd_condenser_ref_brine).send_keys(Keys.ENTER)
        print('Written Design Information :: Condenser :: Brine =', Data['condenser_ref_brine'])

        self.find_element(*ChecklistPageLocators.dd_condenser_ref_flowrate).send_keys(Data['condenser_ref_flowrate'])
        self.find_element(*ChecklistPageLocators.dd_condenser_ref_flowrate).send_keys(Keys.ENTER)
        print('Written Design Information :: Condenser :: Flow Rate =', Data['condenser_ref_flowrate'])

        self.find_element(*ChecklistPageLocators.dd_condenser_ref_presdrop).send_keys(Data['condenser_ref_presdrop'])
        self.find_element(*ChecklistPageLocators.dd_condenser_ref_presdrop).send_keys(Keys.ENTER)
        print('Written Design Information :: Condenser :: Pressure Drop =', Data['condenser_ref_presdrop'])

        self.find_element(*ChecklistPageLocators.dd_condenser_ref_pass).send_keys(Data['condenser_ref_pass'])
        self.find_element(*ChecklistPageLocators.dd_condenser_ref_pass).send_keys(Keys.ENTER)
        print('Written Design Information :: Condenser :: Pass =', Data['condenser_ref_pass'])

        self.find_element(*ChecklistPageLocators.dd_condenser_ref_suctemp).send_keys(Data['condenser_ref_suctemp'])
        self.find_element(*ChecklistPageLocators.dd_condenser_ref_suctemp).send_keys(Keys.ENTER)
        print('Written Design Information :: Condenser :: Suction Temp =', Data['condenser_ref_suctemp'])

        self.find_element(*ChecklistPageLocators.dd_condenser_ref_tempin).send_keys(Data['condenser_ref_tempin'])
        self.find_element(*ChecklistPageLocators.dd_condenser_ref_tempin).send_keys(Keys.ENTER)
        print('Written Design Information :: Condenser :: Temp IN =', Data['condenser_ref_tempin'])

        self.find_element(*ChecklistPageLocators.dd_condenser_ref_tempout).send_keys(Data['condenser_ref_tempout'])
        self.find_element(*ChecklistPageLocators.dd_condenser_ref_tempout).send_keys(Keys.ENTER)
        print('Written Design Information :: Condenser :: Temp OUT =', Data['condenser_ref_tempout'])

    def read_design_info_data(self, Data):
        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_tons).get_attribute('value')
        assert value == Data['cooler_ref_tons']
        print('Read Design Information :: Cooler :: Tons =', Data['cooler_ref_tons'])

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_brine).get_attribute('value')
        assert value == Data['cooler_ref_brine']
        print('Read Design Information :: Cooler :: Brine =', Data['cooler_ref_brine'])

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_flowrate).get_attribute('value')
        assert value == Data['cooler_ref_flowrate']
        print('Read Design Information :: Cooler :: Flow Rate =', Data['cooler_ref_flowrate'])

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_presdrop).get_attribute('value')
        assert value == Data['cooler_ref_presdrop']
        print('Read Design Information :: Cooler :: Pressure Drop =', Data['cooler_ref_presdrop'])

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_pass).get_attribute('value')
        assert value == Data['cooler_ref_pass']
        print('Read Design Information :: Cooler :: Pass =', Data['cooler_ref_pass'])

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_suctemp).get_attribute('value')
        assert value == Data['cooler_ref_suctemp']
        print('Read Design Information :: Cooler :: Suction Temp =', Data['cooler_ref_suctemp'])

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_tempin).get_attribute('value')
        assert value == Data['cooler_ref_tempin']
        print('Read Design Information :: Cooler :: Temp IN =', Data['cooler_ref_tempin'])

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_tempout).get_attribute('value')
        assert value == Data['cooler_ref_tempout']
        print('Read Design Information :: Cooler :: Temp OUT =', Data['cooler_ref_tempout'])

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_tons).get_attribute('value')
        assert value == Data['condenser_ref_tons']
        print('Read Design Information :: Condenser :: Tons =', Data['condenser_ref_tons'])

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_brine).get_attribute('value')
        assert value == Data['condenser_ref_brine']
        print('Read Design Information :: Condenser :: Brine =', Data['condenser_ref_brine'])

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_flowrate).get_attribute('value')
        assert value == Data['condenser_ref_flowrate']
        print('Read Design Information :: Condenser :: Flow Rate =', Data['condenser_ref_flowrate'])

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_presdrop).get_attribute('value')
        assert value == Data['condenser_ref_presdrop']
        print('Read Design Information :: Condenser :: Pressure Drop =', Data['condenser_ref_presdrop'])

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_pass).get_attribute('value')
        assert value == Data['condenser_ref_pass']
        print('Read Design Information :: Condenser :: Pass =', Data['condenser_ref_pass'])

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_suctemp).get_attribute('value')
        assert value == Data['condenser_ref_suctemp']
        print('Read Design Information :: Condenser :: Suction Temp =', Data['condenser_ref_suctemp'])

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_tempin).get_attribute('value')
        assert value == Data['condenser_ref_tempin']
        print('Read Design Information :: Condenser :: Temp IN =', Data['condenser_ref_tempin'])

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_tempout).get_attribute('value')
        assert value == Data['condenser_ref_tempout']
        print('Read Design Information :: Condenser :: Temp OUT =', Data['condenser_ref_tempout'])

    def goto_design_info(self, Data):
        checklistpage = ChecklistPage(driver)
        form_type = Data['Model'] + ' ' + Data['FormType']
        checklistpage.edit_form(Data['CustomerName'], form_type)
        try:
            self.find_element(*ChecklistPageLocators.design_data).click()
        except:
            self.find_element(*ChecklistPageLocators.design_data_2).click()

    def design_info_reset_check(self):
        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_tons).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Cooler :: Tons =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_brine).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Cooler :: Brine =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_flowrate).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Cooler :: Flow Rate =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_presdrop).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Cooler :: Pressure Drop =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_pass).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Cooler :: Pass =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_suctemp).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Cooler :: Suction Temp =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_tempin).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Cooler :: Temp IN =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_cooler_ref_tempout).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Cooler :: Temp OUT =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_tons).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Condenser :: Tons =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_brine).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Condenser :: Brine =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_flowrate).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Condenser :: Flow Rate =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_presdrop).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Condenser :: Pressure Drop =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_pass).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Condenser :: Pass =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_suctemp).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Condenser :: Suction Temp =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_tempin).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Condenser :: Temp IN =', 'Null')

        value = self.find_element(*ChecklistPageLocators.dd_condenser_ref_tempout).get_attribute('value')
        assert value == ''
        print('Read Design Information :: Condenser :: Temp OUT =', 'Null')

    def design_data_reset(self):
        print('Reseting all the values of Design Information(Startup Checklist)')
        self.find_element(*ChecklistPageLocators.design_data_reset).click()

    def design_data_exit(self):
        self.find_element(*ChecklistPageLocators.design_data_exit).click()

    def design_data_save(self):
        self.find_element(*ChecklistPageLocators.design_data_save).click()

    def design_data_cancel(self):
        self.find_element(*ChecklistPageLocators.design_data_cancel).click()

    def save_form(self):
        try:
            self.find_element(*ChecklistPageLocators.save_form).click()
        except Exception:
            self.find_element(*ChecklistPageLocators.save_form_2).click()
        time.sleep(2)
        self.find_element(*ChecklistPageLocators.save_form_popup).click()
        time.sleep(4)
        self.find_element(*ChecklistPageLocators.exit_success_popup_msg).click()

    def startup_form_cancle(self):
        self.find_element(*ChecklistPageLocators.startup_page_cancel).click()

    def startup_form_reset(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()

    def startup_form_exit(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()
