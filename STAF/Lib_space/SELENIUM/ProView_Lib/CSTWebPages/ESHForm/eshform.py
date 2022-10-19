import re
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
sys.path.append(dirnameutils+'\Selenium_Lib')
from Selenium_Lib.BaseClass import Page
from Page_locators.EHSFormPagelocators.ESHPage_locators import ESHFormPageLocators
from selenium.webdriver.common.by import By
# from termcolor import colored
driver = object
delay = 45

class EHSPage(Page):
    def ESH(self, webdriver):
        global driver, delay
        driver = webdriver
        self.wait_until_element((ESHFormPageLocators.ESHchecklist))
        time.sleep(2)
        self.find_element(*ESHFormPageLocators.ESHchecklist).click()

    def new_form(self):
        self.wait_until_element((ESHFormPageLocators.create_new_form_text))
        self.wait_until_element(ESHFormPageLocators.new_form)
        self.find_element(*ESHFormPageLocators.new_form).click()

    def find_form(self, form_type, customer_name):
        self.wait_until_element((ESHFormPageLocators.search))
        i = 1
        while i:
            # try:
            #time.sleep(8)
            try:
                path1 = ('xpath', ESHFormPageLocators.customer_name[-1]+'/div['+str(i)+']/div[1]')
                self.wait_until_element(path1)
                text = self.find_element(*path1).text
            except:
                path1 = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div/div[1]')
                self.wait_until_element(path1)
                text = self.find_element(*path1).text
            if text == customer_name:
                try:
                    path2 = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div[' + str(i) + ']/div[4]')
                    self.wait_until_element(path2)
                    text = self.find_element(*path2).text
                except:
                    path2 = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div/div[4]')
                    self.wait_until_element(path2)
                    text = self.find_element(*path2).text

                if text == form_type:
                    return i
                else:
                    print ('selenium form Type text', text)
                    print ('form type data',form_type)
            else:
                    print ('selenium customer Name text', text)
                    print ('form type data',form_type)
            i = i+1
            # except:
            #     print 'Please check the input data'
            #     break

    def existing_form(self):
        self.find_element(*ESHFormPageLocators.existing_form).click()

    def edit_form(self, customer_name, form_type):
        index = self.find_form(form_type, customer_name)
        #print index
        path = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[1]/a/i')
        self.wait_until_element(path)
        self.find_element(*path).click()

    def mail_form(self, form_type, customer_name):
        index = self.find_form(form_type, customer_name)
        path = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[2]/a/i')
        self.find_element(path).click()

    def export_form(self, form_type, customer_name):
        index = self.find_form(form_type, customer_name)
        path = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[3]/a/i')
        self.find_element(path).click()

    def delete_form(self, Data):
        #self.save_form()
        form_type = Data['Model'] + ' ' + Data['FormType']
        print (form_type,'form_type')
        index = self.find_form(Data['CustomerName'], form_type)
        if index == 1:
            delete_path = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div/div[7]/ul/li[4]/a/i')
        else:
            delete_path = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[4]/a/i')
        self.wait_until_element(delete_path)
        self.find_element(*delete_path).click()
        time.sleep(1.5)
        self.find_element(*ESHFormPageLocators.delete_form_yes).click()

    def startup_form(self):
        self.find_element(*ESHFormPageLocators.startup_form).click()

    def job_name(self, job_name):
        self.find_element(*ESHFormPageLocators.job_name).send_keys(job_name)
        self.find_element(*ESHFormPageLocators.job_name).send_keys(Keys.ENTER)

    def job_no(self, job_no):
        self.find_element(*ESHFormPageLocators.job_no).send_keys(job_no)
        self.find_element(*ESHFormPageLocators.job_no).send_keys(Keys.ENTER)

    def cust_name(self, custname):
        self.find_element(*ESHFormPageLocators.cust_name).send_keys(custname)
        self.find_element(*ESHFormPageLocators.cust_name).send_keys(Keys.ENTER)

    def address(self, address):
        self.find_element(*ESHFormPageLocators.address).send_keys(address)
        self.find_element(*ESHFormPageLocators.address).send_keys(Keys.ENTER)

    def model_no(self, model_no):
        # Click on the select drop down button
        self.find_element(*ESHFormPageLocators.model_no).click()
        # get the dropdown handle
        dropdown = self.find_element(*ESHFormPageLocators.model_no_dropdown)
        # loopby each option in the drop down and check for a match and then select
        for option in dropdown.find_elements_by_tag_name('li'):
            if option.text == model_no:
                option.click()
                break

    def serial_no(self, serial_no):
        self.find_element(*ESHFormPageLocators.serial_no).send_keys(serial_no)
        self.find_element(*ESHFormPageLocators.serial_no).send_keys(Keys.ENTER)

    def create_form(self):
        self.find_element(*ESHFormPageLocators.create_form).click()
        time.sleep(1)
        ###self.find_element(*ESHFormPageLocators.Next).click()
        #self.wait_until_element(ESHFormPageLocators.proceed)
        #self.find_element(*ESHFormPageLocators.proceed).click()
        ###time.sleep(2)
        ###self.find_element(*ESHFormPageLocators.Next).click()
        ####time.sleep(2)
        # self.find_element(*ESHFormPageLocators.save_form).click()

    def esh_data_save(self):
        self.find_element(*ESHFormPageLocators.Next).click()
        time.sleep(1)
        self.find_element(*ESHFormPageLocators.Next).click()
        time.sleep(1)

    def save_form(self):
        try:
            element = driver.find_element_by_xpath(ESHFormPageLocators.save_form[-1])
            driver.execute_script("$(arguments[0]).click();", element)
            # self.find_element('xpath', eval("ESHFormPageLocators.save_form")[-1]).click()
        except Exception:
            element = driver.find_element_by_xpath(ESHFormPageLocators.save_form_2[-1])
            driver.execute_script("$(arguments[0]).click();", element)
            # self.find_element('xpath', eval("ESHFormPageLocators.save_form_2")[-1]).click()
        self.wait_until_element(ESHFormPageLocators.save_form_popup_19)
        time.sleep(5)
        self.find_element('xpath', eval("ESHFormPageLocators.save_form_popup_19")[-1]).click()
        time.sleep(5)
        self.find_element('xpath', eval("ESHFormPageLocators.exit_success_popup_msg_19")[-1]).click()
        time.sleep(1)

    def wait_until_element(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element[-1])))
        except TimeoutException:
            print ("Loading took too much time!")

    def wait_unit_visible(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, element[-1])))
        except TimeoutException:
            print ("Loading took too much time!")

    def esh_form(self):
        self.find_element(*ESHFormPageLocators.ehs_form).click()

    def click(self, xpath):
        self.find_element('xpath', eval("ESHFormPageLocators." + xpath)[-1]).click()

    def write(self, xpath, Data):
        self.wait_until_element('xpath', eval("ESHFormPageLocators." + xpath)[-1])
        self.find_element('xpath', eval("ESHFormPageLocators." + xpath)[-1]).send_keys(Data['testdata'])
        self.find_element('xpath', eval("ESHFormPageLocators." + xpath)[-1]).send_keys(Keys.ENTER)
        print ('Written Design Information('+xpath+')'+' =', Data['testdata'])

    def write_esh_info_data(self, Data):
        ######## 16JT and 16JB ##########
        #self.M16_clickables =   ["M16_IMP"]
        #self.M16_writables = ["M16_EQP"]
        #print Data['Model']
        #if Data['Model'] == u'16JB' or Data['Model'] == u'16JT':
        self.prefix = 'M16'
        #print self.prefix
        if self.prefix == 'M16':
            M16 = ['_SITESAFE_NO', '_EQUIPMENTSAFE_NO','_ELECTRICALDEV_NO','_ISOLATED_NO','_DUALPOWER_NO','_LOTO_NO','_LADDER_NO','_PLATFORM_NO','_INSPECTLADDER_NO','_MATERIALS_NO','_TRIPPING_NO','_HAZARDS_NO','_GUARDS_NO','_GFCI_NO',
                   '_COMPRESSED_NO', '_CALIBRATED_NO', '_WELDING_NO', '_BRAZING_NO', '_CONFINEDSPACE_NO','_ESCAPEROUTE_NO', '_WATERSOURCE_NO', '_PPE_NO', '_LIFTING_NO']
            #M16 = ['_MATERIALS_NO']
            for ele in M16:
                #print ele
                #time.sleep(1)
                self.click(self.prefix + ele)
                time.sleep(1)
                #xpath = (eval("ESHFormPageLocators." + self.prefix + self.M16_write[0]))
                xpath = (eval("ESHFormPageLocators.DATA" + ele))
                #print xpath
                ##element = self.find_elements(*xpath)
                #print element
                self.wait_until_element(xpath)
                #time.sleep(1)
                self.find_element(*xpath).send_keys(Data['testdata'])
                ##element = self.find_elements(*xpath)
                #print element
                #element.send_keys(Data['testdata'])
                time.sleep(1)
                xpath1 = (eval("ESHFormPageLocators.ADD" + ele))
                #print xpath1
                self.wait_until_element(xpath1)
                self.find_element(*xpath1).click()
                print ('Written EHS Information for Model ' + Data['Model']  + ' for '+self.prefix + ele)
                if ele == '_MATERIALS_NO' or ele == '_ESCAPEROUTE_NO':
                    self.find_element(*ESHFormPageLocators.Next).click()

    def goto_esh_info(self, Data):
        form_type = Data['Model'] + ' ' + Data['FormType']
        self.edit_form(Data['CustomerName'], form_type)

    def read(self, xpath, Data, command, index_assert=None,expected=None):
        #time.sleep(1)
        value = self.find_element('xpath', eval("ESHFormPageLocators." + xpath)[-1]).get_attribute('value')
        #print value
        if command == 'read':
            #if Data['Model'] == '16JB' or Data['Model'] == '16JT':
                if index_assert == None:
                    assert value == Data['testdata']
                    print ('Read Design Information('+xpath+')'+' =', value)
                else:
                    assert float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:index_assert])
                    print ('Read Design Information('+xpath+')'+' =', value)

        elif command == 'yes|no':
            value = self.find_element('xpath', eval("ESHFormPageLocators." + xpath)[-1] + '/..')
            if xpath[-3:] == 'YES':
                value = self.find_element('xpath', eval("ESHFormPageLocators." + xpath)[-1] + '/..')
                #print value
                for option in value.find_elements_by_tag_name('input'):
                    value = option.get_attribute('checked')
                assert value == None

            elif xpath[-2:] == 'NO':
                for option in value.find_elements_by_tag_name('input'):
                    value = option.get_attribute('checked')
                assert value == 'true'
            print ('Read ESH Information of ' + xpath + ' = ', value)

        elif command == 'NA':
            value = self.find_element('xpath', eval("ESHFormPageLocators." + xpath)[-1] + '/..')
            for option in value.find_elements_by_tag_name('input'):
                value = option.get_attribute('checked')
            assert value == None
            print ('Read ESH Information of ' + xpath + ' = ', value)

        elif command == 'reset_read':
            value = self.find_element('xpath', eval("ESHFormPageLocators." + xpath)[-1] + '/..')
            #print value
            for option in value.find_elements_by_tag_name('input'):
                value = option.get_attribute('checked')
            # value = value.get_attribute('checked')
            if xpath[-3:] == 'YES':
                assert value == 'true'
            elif xpath[-2:] == 'NO':
                assert value == None
            print ('Read ESH Information of ' + xpath + ' = ', value)
        else:
            assert value == ''
            print ('Read Design Information =', 'Null')

    def read_esh_info_data(self, Data,check):
        #if Data['Model'] == u'16JB' or Data['Model'] == u'16JT':
            self.prefix = 'M16'
            #M16 = ['_SITESAFE_NO','_SITESAFE_YES', '_EQUIPMENTSAFE_NO','_EQUIPMENTSAFE_YES']
            M16 = ['_SITESAFE_NO', '_SITESAFE_YES', '_EQUIPMENTSAFE_NO', '_EQUIPMENTSAFE_YES', '_ELECTRICALDEV_NO',
                   '_ELECTRICALDEV_YES', '_ISOLATED_NO', '_ISOLATED_YES','_DUALPOWER_NO', '_DUALPOWER_YES', '_LOTO_NO',
                   '_LOTO_YES', '_LADDER_NO', '_LADDER_YES','_PLATFORM_NO', '_PLATFORM_YES','_INSPECTLADDER_NO',
                   '_INSPECTLADDER_YES', '_MATERIALS_NO', '_MATERIALS_YES', '_TRIPPING_NO','_TRIPPING_YES',
                   '_HAZARDS_NO', '_HAZARDS_YES', '_GUARDS_NO', '_GUARDS_YES', '_GFCI_NO', '_GFCI_YES','_COMPRESSED_NO',
                   '_COMPRESSED_YES', '_CALIBRATED_NO', '_CALIBRATED_YES', '_WELDING_NO','_WELDING_YES','_BRAZING_NO',
                   '_BRAZING_YES', '_CONFINEDSPACE_NO', '_CONFINEDSPACE_YES','_ESCAPEROUTE_NO', '_ESCAPEROUTE_YES',
                   '_WATERSOURCE_NO', '_WATERSOURCE_YES', '_PPE_NO', '_PPE_YES','_LIFTING_NO', '_LIFTING_YES']

            #M16_NA = ['_SITESAFE_NA','_EQUIPMENTSAFE_NA']
            M16_NA = ['_SITESAFE_NA', '_EQUIPMENTSAFE_NA','_ELECTRICALDEV_NA','_ISOLATED_NA','_DUALPOWER_NA','_LOTO_NA','_LADDER_NA','_PLATFORM_NA','_INSPECTLADDER_NA','_MATERIALS_NA','_TRIPPING_NA','_HAZARDS_NA','_GUARDS_NA','_GFCI_NA',
                   '_COMPRESSED_NA', '_CALIBRATED_NA', '_WELDING_NA', '_BRAZING_NA', '_CONFINEDSPACE_NA','_ESCAPEROUTE_NA', '_WATERSOURCE_NA', '_PPE_NA', '_LIFTING_NA']

            if check == 'yes|no':
             index_list = [10 for i in range(len(M16))]
             for ele in range(len(M16)):
            #for ele in M16:
                #print ele,'1111111111111111111111111'
                self.read(self.prefix + M16[ele], Data, 'yes|no', index_list[ele])
                #self.read(self.prefix + M16[ele], Data, 'yes|no')
                #self.read(self.prefix + M16_NA[ele], Data, 'NA')
                if M16[ele] == '_MATERIALS_YES' or M16[ele] == '_ESCAPEROUTE_YES':
                 self.find_element(*ESHFormPageLocators.Next).click()

            elif check == 'NA':
             for ele in range(len(M16_NA)):
              self.read(self.prefix + M16_NA[ele], Data, 'NA')
              if M16_NA[ele] == '_MATERIALS_NA' or M16_NA[ele] == '_ESCAPEROUTE_NA':
                  self.find_element(*ESHFormPageLocators.Next).click()

    def esh_data_reset(self):
        print ('Reseting all the values of EHS Information')
        self.wait_until_element(ESHFormPageLocators.ehs_data_reset)
        #element = driver.find_element_by_xpath(ESHFormPageLocators.ehs_data_reset[-1])
        #driver.execute_script("$(arguments[0]).click();", element)
        self.find_element(*ESHFormPageLocators.ehs_data_reset).click()

    def esh_info_reset_check(self, Data):
        #if Data['Model'] == u'16JB' or Data['Model'] == u'16JT':
            self.prefix = 'M16'
            #M16 = ['_SITESAFE_NO','_SITESAFE_YES', '_EQUIPMENTSAFE_NO','_EQUIPMENTSAFE_YES']
            M16 = ['_SITESAFE_NO', '_SITESAFE_YES', '_EQUIPMENTSAFE_NO', '_EQUIPMENTSAFE_YES', '_ELECTRICALDEV_NO',
                   '_ELECTRICALDEV_YES', '_ISOLATED_NO', '_ISOLATED_YES','_DUALPOWER_NO', '_DUALPOWER_YES', '_LOTO_NO',
                   '_LOTO_YES', '_LADDER_NO', '_LADDER_YES','_PLATFORM_NO', '_PLATFORM_YES','_INSPECTLADDER_NO',
                   '_INSPECTLADDER_YES', '_MATERIALS_NO', '_MATERIALS_YES', '_TRIPPING_NO','_TRIPPING_YES',
                   '_HAZARDS_NO', '_HAZARDS_YES', '_GUARDS_NO', '_GUARDS_YES', '_GFCI_NO', '_GFCI_YES','_COMPRESSED_NO',
                   '_COMPRESSED_YES', '_CALIBRATED_NO', '_CALIBRATED_YES', '_WELDING_NO','_WELDING_YES','_BRAZING_NO',
                   '_BRAZING_YES', '_CONFINEDSPACE_NO', '_CONFINEDSPACE_YES','_ESCAPEROUTE_NO', '_ESCAPEROUTE_YES',
                   '_WATERSOURCE_NO', '_WATERSOURCE_YES', '_PPE_NO', '_PPE_YES','_LIFTING_NO', '_LIFTING_YES']
            for ele in M16:
                #print M16[ele]
                #print ele
                self.read(self.prefix + ele, Data, 'reset_read')
                if ele == '_MATERIALS_YES' or ele == '_ESCAPEROUTE_YES':
                 self.find_element(*ESHFormPageLocators.Next).click()


    def get_xpath_elements(self):
        self.prefix = 'M16'
        self.M16_write = ['_SITESAFE_NO']
        xpath = (eval("ESHFormPageLocators." + self.prefix + self.M16_write[0]))
        elements = self.find_elements(*xpath)
        print (elements)
        time.sleep(1)
        elements[1].click()

    def Verify_body_text_gui(self,text='',succ_str='',raise_str=''):
        #time.sleep(1)
        body_text = self.find_element('xpath', eval("ESHFormPageLocators.Bodytext")[-1]).text
        print (body_text)
        if body_text == text :
              print (succ_str)
        else:
              raise Exception(raise_str)

    def ehs_data_exit(self):
        self.find_element(*ESHFormPageLocators.ehs_data_exit).click()

    def delete_form(self, Data):
        self.save_form()
        time.sleep(2)
        form_type = Data['Model'] + ' ' + Data['FormType']
       # index = self.find_form(form_type, Data['CustomerName'])
        if index == 1:
            delete_path = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div/div[7]/ul/li[4]/a/i')
        else:
            delete_path = ('xpath', ESHFormPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[4]/a/i')
        self.wait_until_element(delete_path)
        self.find_element(*delete_path).click()
        time.sleep(1.5)
        self.find_element(*ESHFormPageLocators.delete_form_yes).click()
        print (form_type,' is successfully deleted.')

    def write_logs_info_data(self, Data):
        if Data['logsheet'] == u'quarterly':
         M16 = ['Cooler_Refridge_pressure', 'Cooler_Refridge_temp','Cooler_Water_pressure_in','Cooler_Water_pressure_out',
               'Cooler_Water_pressure_delta','Cooler_Water_temp_in','Cooler_Water_temp_out','Cooler_Water_temp_delta','Condenser_Water_approach',
               'Condenser_Refridge_pressure','Condenser_Refridge_temp','Condenser_Refridge_approach','Condenser_Water_pressure_in',
               'Condenser_Water_pressure_out','Condenser_Water_pressure_delta',
                   'Condenser_Water_temp_in', 'Condenser_Water_temp_out', 'Condenser_Water_temp_delta',
               'Compressor_Oil_pressure', 'Compressor_Oil_resevtmp','Compressor_Oil_resevlevel', 'Compressor_Oil_runhrs', 'Compressor_Oil_nostarts',
               'Compressor_Oil_capacity','Compressor_motor_tmp','Compressor_motor_bearingtmp']
        else:

         M16 = ['annual_Cooler_Refridge_pressure', 'annual_Cooler_Refridge_temp','annual_Cooler_Water_pressure_in','annual_Cooler_Water_pressure_out',
               'annual_Cooler_Water_pressure_delta','annual_Cooler_Water_temp_in','annual_Cooler_Water_temp_out','annual_Cooler_Water_temp_delta','annual_Condenser_Water_approach',
               'annual_Condenser_Refridge_pressure','annual_Condenser_Refridge_temp','annual_Condenser_Refridge_approach','annual_Condenser_Water_pressure_in',
               'annual_Condenser_Water_pressure_out','annual_Condenser_Water_pressure_delta',
                   'annual_Condenser_Water_temp_in', 'annual_Condenser_Water_temp_out', 'annual_Condenser_Water_temp_delta',
               'annual_Compressor_Oil_pressure', 'annual_Compressor_Oil_resevtmp','annual_Compressor_Oil_resevlevel', 'annual_Compressor_Oil_runhrs', 'annual_Compressor_Oil_nostarts',
               'annual_Compressor_Oil_capacity','annual_Compressor_motor_tmp','annual_Compressor_motor_bearingtmp']

        for ele in M16:
                #self.write(ele, Data)
                xpath = (eval("ESHFormPageLocators." + ele))
                self.wait_until_element(xpath)
                time.sleep(1)
                self.find_element(*xpath).send_keys(Data['testdata'])
                print ('Written logsheet Information for Model ' + Data['Model'] + ' for ' + ele + ' =', Data['testdata'])

    def logs_data_save(self,Data):
        if Data['logsheet'] == u'quarterly':
         time.sleep(1)
         self.find_element(*ESHFormPageLocators.Quaterly_logsheet_save).click()
         time.sleep(1)
        else:
         time.sleep(1)
         self.find_element(*ESHFormPageLocators.annual_logsheet_save).click()
         time.sleep(1)
    '''
    def annual_logs_data_save(self):
        time.sleep(1)
        self.find_element(*ESHFormPageLocators.annual_logsheet_save).click()
        time.sleep(1)
    '''
    def logs_save_form(self):
        self.wait_until_element(ESHFormPageLocators.logsheet_form_popup_19)
        time.sleep(5)
        self.find_element('xpath', eval("ESHFormPageLocators.logsheet_form_popup_19")[-1]).click()
        time.sleep(5)
        self.find_element('xpath', eval("ESHFormPageLocators.exit_success_popup_msg_19")[-1]).click()
        time.sleep(1)


    def readfunc(self, xpath, Data, command, index_assert=None):
        value = self.find_element('xpath', eval("ESHFormPageLocators." + xpath)[-1]).get_attribute('value')
        print (value,1)
        xpath = (eval("ESHFormPageLocators." +  self.M16_write[0]))
        self.wait_until_element(xpath)
        element = self.find_elements(*xpath)
        i = 0
        for textctrls in element:
            try:
                textctrls.get_attribute('value')
                print ('Read Design Information(' + self.M16_write[i] + ')' + ' =', value)
                i = i + 1
            except:
                pass
        print (Data['testdata'] ,'22222222')
        if command == 'read':
            #print index_assert,'111111'
            if index_assert == None:
                try:
                    assert value == Data['testdata']
                    print ('Read Design Information('+self.M16_write[i] +')'+' =', value)
                except:
                    print (" Assertion error:", self.M16_write[i], str(value))
            else:
                print (float(value),'333333333')
                #print float(''.join(filter(str.isdigit, int(Data['testdata'])))[:index_assert])
                try:
                    assert float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:index_assert])
                    print ('Read Design Information('+ self.M16_write[i] + ')'+' =', str(value))
                except:
                    print (" Assertion error:", self.M16_write[i], str(value))
        else:
            assert value == ''
            print ('Read Design Information =', 'Null')

    def read_logsheet_data(self, Data):
        self.prefix = 'M16'
        if Data['logsheet'] == u'quarterly':
        #self.M16_write = ['Cooler_Water_pressure_in']

         self.M16_write = ['Cooler_Water_pressure_in','Cooler_Water_pressure_out','Cooler_Water_pressure_delta',
               'Cooler_Water_temp_in', 'Cooler_Water_temp_out','Cooler_Water_temp_delta',
               'Condenser_Water_pressure_in','Condenser_Water_pressure_out', 'Condenser_Water_pressure_delta',
               'Condenser_Water_temp_in', 'Condenser_Water_temp_out', 'Condenser_Water_temp_delta',
               'Compressor_motor_tmp', 'Compressor_motor_bearingtmp']
        else:
         self.M16_write = ['annual_Cooler_Water_pressure_in','annual_Cooler_Water_pressure_out','annual_Cooler_Water_pressure_delta',
               'annual_Cooler_Water_temp_in', 'annual_Cooler_Water_temp_out','annual_Cooler_Water_temp_delta',
               'annual_Condenser_Water_pressure_in','annual_Condenser_Water_pressure_out', 'annual_Condenser_Water_pressure_delta',
               'annual_Condenser_Water_temp_in', 'annual_Condenser_Water_temp_out', 'annual_Condenser_Water_temp_delta',
               'annual_Compressor_motor_tmp', 'annual_Compressor_motor_bearingtmp']

        if self.prefix == 'M16':
            #index_list = [5 for i in range(len(self.M16_write))]
            #print index_list,'2222222222222'
            for ele in self.M16_write:
                 self.readfunc(ele, Data, 'read', 5)

    def logs_data_reset(self,Data):
        if Data['logsheet'] == u'quarterly':
            print ('Reseting all the values of EHS Information')
            self.wait_until_element(ESHFormPageLocators.ehs_data_reset)
            self.find_element(*ESHFormPageLocators.logs_data_reset).click()
        else:
            print ('Reseting all the values of EHS Information')
            self.wait_until_element(ESHFormPageLocators.ehs_data_reset)
            self.find_element(*ESHFormPageLocators.annual_logs_data_reset).click()

    def logs_info_reset_check(self, Data):

        if Data['logsheet'] == u'quarterly':

         M16 = ['Cooler_Water_pressure_in','Cooler_Water_pressure_out','Cooler_Water_pressure_delta',
               'Cooler_Water_temp_in', 'Cooler_Water_temp_out','Cooler_Water_temp_delta',
               'Condenser_Water_pressure_in','Condenser_Water_pressure_out', 'Condenser_Water_pressure_delta',
               'Condenser_Water_temp_in', 'Condenser_Water_temp_out', 'Condenser_Water_temp_delta',
               'Compressor_motor_tmp', 'Compressor_motor_bearingtmp']
        else:
         M16 = ['annual_Cooler_Water_pressure_in','annual_Cooler_Water_pressure_out','annual_Cooler_Water_pressure_delta',
               'annual_Cooler_Water_temp_in', 'annual_Cooler_Water_temp_out','annual_Cooler_Water_temp_delta',
               'annual_Condenser_Water_pressure_in','annual_Condenser_Water_pressure_out', 'annual_Condenser_Water_pressure_delta',
               'annual_Condenser_Water_temp_in', 'annual_Condenser_Water_temp_out', 'annual_Condenser_Water_temp_delta',
               'annual_Compressor_motor_tmp', 'annual_Compressor_motor_bearingtmp']

        #M16 = ['annual_Cooler_Water_pressure_in']
        for ele in M16:
            self.read(ele, Data, 'reset_read1')

    def annual_logs_data_reset(self):
        print ('Reseting all the values of EHS Information')
        self.wait_until_element(ESHFormPageLocators.ehs_data_reset)
        #element = driver.find_element_by_xpath(ESHFormPageLocators.ehs_data_reset[-1])
        #driver.execute_script("$(arguments[0]).click();", element)
        self.find_element(*ESHFormPageLocators.annual_logs_data_reset).click()

    def logsheet_form(self,Data):
        if Data['logsheet'] == u'quarterly':
            self.find_element(*ESHFormPageLocators.quaterly).click()
            self.find_element(*ESHFormPageLocators.logsheet).click()
        else:
            self.find_element(*ESHFormPageLocators.annual).click()
            self.find_element(*ESHFormPageLocators.annual_logsheet).click()
    def checklist_form(self,Data):
        if Data['logsheet'] == u'quarterly':
            self.find_element(*ESHFormPageLocators.checklist_new).click()
            self.find_element(*ESHFormPageLocators.checklist_quarterly).click()

        else:
            self.find_element(*ESHFormPageLocators.checklist_new).click()
            self.find_element(*ESHFormPageLocators.checklist_annual).click()
