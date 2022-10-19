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
from Page_locators.ChecklistPage_locators import ChecklistPageLocators
from selenium.webdriver.common.by import By

driver = object
delay = 45


class ChecklistPage(Page):
    def checklist(self, webdriver):
        global driver, delay
        driver = webdriver
        self.wait_until_element((ChecklistPageLocators.checklist))
        self.find_element(*ChecklistPageLocators.checklist).click()

    def new_form(self):
        self.wait_until_element((ChecklistPageLocators.create_new_form_text))
        self.wait_until_element(ChecklistPageLocators.new_form)
        self.find_element(*ChecklistPageLocators.new_form).click()

    def find_form(self, customer_name, form_type):
        self.wait_until_element((ChecklistPageLocators.search))
        i = 1
        while i:
            # try:
            time.sleep(8)
            try:
                path1 = ('xpath', ChecklistPageLocators.customer_name[-1]+'/div['+str(i)+']/div[1]')
                self.wait_until_element(path1)
                text = self.find_element(*path1).text
            except:
                path1 = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div/div[1]')
                self.wait_until_element(path1)
                text = self.find_element(*path1).text
            if text == customer_name:
                try:
                    path2 = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(i) + ']/div[4]')
                    self.wait_until_element(path2)
                    text = self.find_element(*path2).text
                except:
                    path2 = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div/div[4]')
                    self.wait_until_element(path2)
                    text = self.find_element(*path2).text
                if text == form_type:
                    return i
            i = i+1

    def existing_form(self):
        self.find_element(*ChecklistPageLocators.existing_form).click()

    def edit_form(self, form_type, customer_name):
        index = self.find_form(form_type, customer_name)
        path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[1]/a/i')
        self.wait_until_element(path)
        self.find_element(*path).click()

    def mail_form(self, form_type, customer_name):
        index = self.find_form(form_type, customer_name)
        path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[2]/a/i')
        self.find_element(path).click()

    def export_form(self, form_type, customer_name):
        index = self.find_form(form_type, customer_name)
        path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[3]/a/i')
        self.find_element(path).click()

    def delete_form(self, Data):
        self.save_form()
        form_type = Data['Model'] + ' ' + Data['FormType']
        index = self.find_form(Data['CustomerName'], form_type)
        if index == 1:
            delete_path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div/div[7]/ul/li[4]/a/i')
        else:
            delete_path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[4]/a/i')
        self.wait_until_element(delete_path)
        self.find_element(*delete_path).click()
        time.sleep(1.5)
        self.find_element(*ChecklistPageLocators.delete_form_yes).click()

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
        self.wait_until_element(ChecklistPageLocators.proceed)
        self.find_element(*ChecklistPageLocators.proceed).click()
        time.sleep(2)

    def design_data(self):
        try:
            self.wait_until_element(ChecklistPageLocators.design_data)
            element = driver.find_element_by_xpath(ChecklistPageLocators.design_data[-1])
            driver.execute_script("$(arguments[0]).click();", element)
        except:
            self.wait_until_element(ChecklistPageLocators.design_data_three)
            element = driver.find_element_by_xpath(ChecklistPageLocators.design_data_three[-1])
            driver.execute_script("$(arguments[0]).click();", element)

    def click(self, xpath):
        self.find_element('xpath', eval("ChecklistPageLocators." + xpath)[-1]).click()

    def write(self, xpath, Data):
        self.find_element('xpath', eval("ChecklistPageLocators." + xpath)[-1]).send_keys(Data['testdata'])
        self.find_element('xpath', eval("ChecklistPageLocators." + xpath)[-1]).send_keys(Keys.ENTER)
        print ('Written Design Information('+xpath+')'+' =', Data['testdata'])

    def write_design_info_data(self, Data):
        if Data['Model'] == u'30XA' or Data['Model'] == u'30XV':
            self.prefix = 'M30XA_30XV'
        elif Data['Model'] == u'32XR':
            self.prefix = 'M32XR'
        elif Data['Model'] == u'30XW' or Data['Model'] == u'30XWV':
            self.prefix = 'M30XW_30XWV'
        elif Data['Model'][:2] == '30':
            self.prefix = 'M' + Data['Model']
        else:
            self.prefix = 'M' + Data['Model'][:2]
        if Data['Model'][:2] == '17' or Data['Model'][:2] == '23'or Data['Model'][:2] == '19' or self.prefix == 'M32XR':
            self.prefix = 'M19'
            M19 = ['_cooler_ref_tons', '_cooler_ref_flowrate', '_cooler_ref_presdrop', '_cooler_ref_pass', '_cooler_ref_tempin', '_cooler_ref_tempout']
            for ele in M19:
                self.write(self.prefix + ele, Data)

        if self.prefix == 'M16':
            list_of_sets = ['evaporator', 'absorber', 'cooler']
            M16 = ['_supply_steam_preasure', '_supply_preasure_generator', '_electrical_data', '_inhibitor']
            for ele in M16:
                self.write(self.prefix + ele, Data)

            for ele1 in list_of_sets:
                M16 = ['_ref_tons', '_ref_flowrate', '_ref_presdrop', '_ref_pass', '_ref_tempin', '_ref_tempout']
                for ele in M16:
                    self.write(self.prefix +"_"+ ele1 + ele, Data)

        if self.prefix == 'M19' or self.prefix == 'M17'  or self.prefix == 'M23' or self.prefix == 'M32XR':
            M = ['_cooler_ref_suctemp', '_cooler_ref_brine', '_condenser_ref_tons', '_condenser_ref_brine', '_condenser_ref_flowrate', '_condenser_ref_presdrop',
                 '_condenser_ref_pass', '_condenser_ref_suctemp', '_condenser_ref_tempin', '_condenser_ref_tempout']
            for ele in M:
                self.write(self.prefix + ele, Data)

        if self.prefix == 'M30HX':
            M30HX = ['_equip_model_no', '_equip_serial_no']
            for ele in M30HX:
                self.write(self.prefix + ele, Data)

        if self.prefix == 'M30MP':
            M30MP = ['_chiller_model_no', '_chiller_serial_no', '_comp_model_no', '_comp_serial_no']
            for ele in M30MP:
                self.write(self.prefix + ele, Data)

        if self.prefix == 'M30RAP':
            M30RAP = ['_capcity', '_ceat', '_ewt', '_lwt', '_fluid_type', '_flowrate', '_PD', '_model_no', '_serial_no']
            for ele in M30RAP:
                self.write(self.prefix + ele, Data)
        if self.prefix == 'M30RB':
            M30RB_write = ['_unit_model_no', '_unit_serial_no', '_cooler_model_no', '_cooler_serial_no']
            M30RB_click_comp = ['_Comp_type_A1', '_Comp_type_A2', '_Comp_type_A3', '_Comp_type_A4', '_Comp_type_B1',
                                '_Comp_type_B2', '_Comp_type_B3', '_Comp_type_B4', '_Comp_type_C1', '_Comp_type_C2',
                                '_Comp_type_C3', '_Comp_type_C4', '_comp_type_P1', '_comp_type_P2']

            M30RB_write_comp = [['_A1_ModelNo', '_A1_SerialNo', '_A1_SMP_Address'],
                                ['_A2_ModelNo', '_A2_SerialNo', '_A2_SMP_Address'],
                                ['_A3_ModelNo', '_A3_SerialNo', '_A3_SMP_Address'],
                                ['_A4_ModelNo', '_A4_SerialNo', '_A4_SMP_Address'],
                                ['_B1_ModelNo', '_B1_SerialNo', '_B1_SMP_Address'],
                                ['_B2_ModelNo', '_B2_SerialNo', '_B2_SMP_Address'],
                                ['_B3_ModelNo', '_B3_SerialNo', '_B3_SMP_Address'],
                                ['_B4_ModelNo', '_B4_SerialNo', '_B4_SMP_Address'],
                                ['_C1_ModelNo', '_C1_SerialNo', '_C1_SMP_Address'],
                                ['_C2_ModelNo', '_C2_SerialNo', '_C2_SMP_Address'],
                                ['_C3_ModelNo', '_C3_SerialNo', '_C3_SMP_Address'],
                                ['_C4_ModelNo', '_C4_SerialNo', '_C4_SMP_Address'],
                                ['_P1_ModelNo', '_P1_SerialNo'],
                                ['_P2_ModelNo', '_P2_SerialNo']]

            for ele in range(len(M30RB_click_comp)):
                self.click(self.prefix + M30RB_click_comp[ele])
                for e in M30RB_write_comp[ele]:
                    self.write(self.prefix + e, Data)
            for ele in M30RB_write:
                self.write(self.prefix + ele, Data)
        if self.prefix == 'M30XA_30XV':
            M30XA_30XV = ['_cooler_cap', '_cooler_ewt', '_cooler_lwt', '_cooler_fluid_type', '_cooler_flow_rate', '_cooler_PD', '_cooler_ambient',
                        '_unit_ModelNo', '_unit_SerialNo', '_cooler_ModelNo', '_cooler_SerialNo', '_comp_A_ModelNo', '_comp_A_SerialNo',
                     '_comp_B_ModelNo', '_comp_B_SerialNo']
            for ele in M30XA_30XV:
                self.write(self.prefix + ele, Data)

        if self.prefix == 'M30XW_30XWV':
            M30XW_30XWV = ["_evaporator_cap", "_evaporator_ewt", "_evaporator_lwt", "_evaporator_fluid_type", "_evaporator_flow_rate", "_evaporator_PD",
                     "_condenser_cap", "_condenser_ewt", "_condenser_lwt", "_condenser_fluid_type", "_condenser_flow_rate", "_condenser_PD", "_unit_ModelNo",
                     "_unit_SerialNo", "_comp_A_ModelNo", "_comp_A_SerialNo", "_comp_B_ModelNo", "_comp_B_SerialNo", "_evaporator_ModelNo", "_evaporator_SerialNo",
                     "_condenser_ModelNo", "_condenser_SerialNo"]
            for ele in M30XW_30XWV:
                self.write(self.prefix + ele, Data)

    def read(self, xpath, Data, command, index_assert=None):
        value = self.find_element('xpath', eval("ChecklistPageLocators." + xpath)[-1]).get_attribute('value')
        if command == 'read':
            if Data['Model'] == '30RAP'or Data['Model'] == '30XA' or Data['Model'] == '30XV' or Data['Model'] == '30XW'or Data['Model'] == '32XR':
                if index_assert == None:
                    assert value == Data['testdata']
                    print ('Read Design Information('+xpath+')'+' =', value)
                else:
                    assert float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:index_assert])
                    print ('Read Design Information('+xpath+')'+' =', value)
            elif Data['Model'] == '30HX' or Data['Model'] == '30MP' or Data['Model'] == '30RB':
                assert value == Data['testdata']
                print ('Read Design Information('+xpath+')'+' =', value)
            else:
                assert float(value) == float(''.join(filter(str.isdigit, str(Data['testdata']))))
                print ('Read Design Information('+xpath+')'+' =', value)
        else:
            assert value == ''
            print ('Read Design Information =', 'Null')

    def read_design_info_data(self, Data):
        if Data['Model'][:2] == '17' or Data['Model'][:2] == '23'or Data['Model'][:2] == '19' or self.prefix == 'M32XR':
            self.prefix = 'M19'
            M19 = ['_cooler_ref_tons', '_cooler_ref_flowrate', '_cooler_ref_presdrop', '_cooler_ref_pass', '_cooler_ref_tempin', '_cooler_ref_tempout']
            index_list = [5 for i in range(len(M19))]
            for ele in range(len(M19)):
                self.read(self.prefix + M19[ele], Data, 'read', index_list[ele])

        if self.prefix == 'M16':
            list_of_sets = ['evaporator', 'absorber', 'cooler']
            M16 = ['_supply_steam_preasure', '_supply_preasure_generator', '_electrical_data', '_inhibitor']
            for ele in M16:
                self.read(self.prefix + ele, Data, 'read')

            for ele1 in list_of_sets:
                M16 = ['_ref_tons', '_ref_flowrate', '_ref_presdrop', '_ref_pass', '_ref_tempin', '_ref_tempout']
                for ele in M16:
                    self.read(self.prefix +"_"+ ele1 + ele, Data, 'read')

        if self.prefix == 'M19' or self.prefix == 'M17'  or self.prefix == 'M23' or self.prefix == 'M32XR':
            M = ['_cooler_ref_suctemp', '_cooler_ref_brine', '_condenser_ref_tons', '_condenser_ref_brine', '_condenser_ref_flowrate', '_condenser_ref_presdrop',
                 '_condenser_ref_pass', '_condenser_ref_suctemp', '_condenser_ref_tempin', '_condenser_ref_tempout']
            index_list = [5 for i in range(len(M))]
            for ele in range(len(M)):
                self.read(self.prefix + M[ele], Data, 'read', index_list[ele])

        if self.prefix == 'M30HX':
            M30HX = ['_equip_model_no', '_equip_serial_no']
            for ele in M30HX:
                self.read(self.prefix + ele, Data, 'read')

        if self.prefix == 'M30MP':
            M30MP = ['_chiller_model_no', '_chiller_serial_no', '_comp_model_no', '_comp_serial_no']
            for ele in M30MP:
                self.read(self.prefix + ele, Data, 'read')

        if self.prefix == 'M30RAP':
            M30RAP = ['_capcity', '_ceat', '_ewt', '_lwt', '_fluid_type', '_flowrate', '_PD', '_model_no', '_serial_no']
            index_assert = [2, 5, 5, 5, 5, 5, 5, None, None]
            for i in range(len(M30RAP)):
                self.read(self.prefix + M30RAP[i], Data, 'read', index_assert[i])

        if self.prefix == 'M30RB':
            M30RB_write = ['_unit_model_no', '_unit_serial_no', '_cooler_model_no', '_cooler_serial_no']
            M30RB_click_comp = ['_Comp_type_A1', '_Comp_type_A2', '_Comp_type_A3', '_Comp_type_A4', '_Comp_type_B1',
                                '_Comp_type_B2', '_Comp_type_B3', '_Comp_type_B4', '_Comp_type_C1', '_Comp_type_C2',
                                '_Comp_type_C3', '_Comp_type_C4', '_comp_type_P1', '_comp_type_P2']

            M30RB_write_comp = [['_A1_ModelNo', '_A1_SerialNo', '_A1_SMP_Address'],
                                ['_A2_ModelNo', '_A2_SerialNo', '_A2_SMP_Address'],
                                ['_A3_ModelNo', '_A3_SerialNo', '_A3_SMP_Address'],
                                ['_A4_ModelNo', '_A4_SerialNo', '_A4_SMP_Address'],
                                ['_B1_ModelNo', '_B1_SerialNo', '_B1_SMP_Address'],
                                ['_B2_ModelNo', '_B2_SerialNo', '_B2_SMP_Address'],
                                ['_B3_ModelNo', '_B3_SerialNo', '_B3_SMP_Address'],
                                ['_B4_ModelNo', '_B4_SerialNo', '_B4_SMP_Address'],
                                ['_C1_ModelNo', '_C1_SerialNo', '_C1_SMP_Address'],
                                ['_C2_ModelNo', '_C2_SerialNo', '_C2_SMP_Address'],
                                ['_C3_ModelNo', '_C3_SerialNo', '_C3_SMP_Address'],
                                ['_C4_ModelNo', '_C4_SerialNo', '_C4_SMP_Address'],
                                ['_P1_ModelNo', '_P1_SerialNo'],
                                ['_P2_ModelNo', '_P2_SerialNo']]

            for ele in range(len(M30RB_click_comp)):
                self.click(self.prefix + M30RB_click_comp[ele])
                for e in M30RB_write_comp[ele]:
                    self.read(self.prefix + e, Data, 'read')
            for ele in M30RB_write:
                self.read(self.prefix + ele, Data, 'read')

        if self.prefix == 'M30XA_30XV':
            index_assert = [2, 5, 5, 5, 5, 5, 5, None, None, None, None, None, None, None, None]
            M30XA_30XV = ['_cooler_cap', '_cooler_ewt', '_cooler_lwt', '_cooler_fluid_type', '_cooler_flow_rate', '_cooler_PD', '_cooler_ambient',
                        '_unit_ModelNo', '_unit_SerialNo', '_cooler_ModelNo', '_cooler_SerialNo', '_comp_A_ModelNo', '_comp_A_SerialNo',
                     '_comp_B_ModelNo', '_comp_B_SerialNo']
            for ele in range(len(M30XA_30XV)):
                self.read(self.prefix + M30XA_30XV[ele], Data, 'read', index_assert[ele])

        if self.prefix == 'M30XW_30XWV':
            index_assert = [2, 5, 5, 5, 5, 5, 2, 5, 5, 5, 5, 5, None, None, None, None, None, None, None, None, None, None]
            M30XW_30XWV = ["_evaporator_cap", "_evaporator_ewt", "_evaporator_lwt", "_evaporator_fluid_type", "_evaporator_flow_rate", "_evaporator_PD",
                     "_condenser_cap", "_condenser_ewt", "_condenser_lwt", "_condenser_fluid_type", "_condenser_flow_rate", "_condenser_PD", "_unit_ModelNo",
                     "_unit_SerialNo", "_comp_A_ModelNo", "_comp_A_SerialNo", "_comp_B_ModelNo", "_comp_B_SerialNo", "_evaporator_ModelNo", "_evaporator_SerialNo",
                     "_condenser_ModelNo", "_condenser_SerialNo"]
            for ele in range(len(M30XW_30XWV)):
                self.read(self.prefix + M30XW_30XWV[ele], Data, 'read', index_assert[ele])

    def goto_design_info(self, Data):
        form_type = Data['Model'] + ' ' + Data['FormType']
        self.edit_form(Data['CustomerName'], form_type)
        try:
            self.wait_until_element(ChecklistPageLocators.design_data)
            element = driver.find_element_by_xpath(ChecklistPageLocators.design_data[-1])
            driver.execute_script("$(arguments[0]).click();", element)
        except:
            try:
                self.wait_until_element(ChecklistPageLocators.design_data_three)
                element = driver.find_element_by_xpath(ChecklistPageLocators.design_data_three[-1])
                driver.execute_script("$(arguments[0]).click();", element)
            except:
                self.wait_until_element(ChecklistPageLocators.design_data_two)
                element = driver.find_element_by_xpath(ChecklistPageLocators.design_data_two[-1])
                driver.execute_script("$(arguments[0]).click();", element)

    def design_info_reset_check(self, Data):
        if Data['Model'][:2] == '17' or Data['Model'][:2] == '23'or Data['Model'][:2] == '19' or self.prefix == 'M32XR':
            self.prefix = 'M19'
            M19 = ['_cooler_ref_tons', '_cooler_ref_flowrate', '_cooler_ref_presdrop', '_cooler_ref_pass', '_cooler_ref_tempin', '_cooler_ref_tempout']
            for ele in M19:
                self.read(self.prefix + ele, Data, 'reset_read')

        if self.prefix == 'M16':
            list_of_sets = ['evaporator', 'absorber', 'cooler']
            M16 = ['_supply_steam_preasure', '_supply_preasure_generator', '_electrical_data', '_inhibitor']
            for ele in M16:
                self.read(self.prefix + ele, Data, 'reset_read')

            for ele1 in list_of_sets:
                M16 = ['_ref_tons', '_ref_flowrate', '_ref_presdrop', '_ref_pass', '_ref_tempin', '_ref_tempout']
                for ele in M16:
                    self.read(self.prefix +"_"+ ele1 + ele, Data, 'reset_read')

        if self.prefix == 'M19' or self.prefix == 'M17'  or self.prefix == 'M23':
            M = ['_cooler_ref_suctemp', '_cooler_ref_brine', '_condenser_ref_tons', '_condenser_ref_brine', '_condenser_ref_flowrate', '_condenser_ref_presdrop',
                 '_condenser_ref_pass', '_condenser_ref_suctemp', '_condenser_ref_tempin', '_condenser_ref_tempout']
            for ele in M:
                self.read(self.prefix + ele, Data, 'reset_read')

        if self.prefix == 'M30HX':
            M30HX = ['_equip_model_no', '_equip_serial_no']
            for ele in M30HX:
                self.read(self.prefix + ele, Data, 'reset_read')

        if self.prefix == 'M30MP':
            M30MP = ['_chiller_model_no', '_chiller_serial_no', '_comp_model_no', '_comp_serial_no']
            for ele in M30MP:
                self.read(self.prefix + ele, Data, 'reset_read')

        if self.prefix == 'M30RAP':
            M30RAP = ['_capcity', '_ceat', '_ewt', '_lwt', '_fluid_type', '_flowrate', '_PD', '_model_no', '_serial_no']
            for ele in M30RAP:
                self.read(self.prefix + ele, Data, 'reset_read')

        if self.prefix == 'M30RB':
            M30RB_write = ['_unit_model_no', '_unit_serial_no', '_cooler_model_no', '_cooler_serial_no']
            M30RB_click_comp = ['_Comp_type_A1', '_Comp_type_A2', '_Comp_type_A3', '_Comp_type_A4', '_Comp_type_B1',
                                '_Comp_type_B2', '_Comp_type_B3', '_Comp_type_B4', '_Comp_type_C1', '_Comp_type_C2',
                                '_Comp_type_C3', '_Comp_type_C4', '_comp_type_P1', '_comp_type_P2']

            M30RB_write_comp = [['_A1_ModelNo', '_A1_SerialNo', '_A1_SMP_Address'],
                                ['_A2_ModelNo', '_A2_SerialNo', '_A2_SMP_Address'],
                                ['_A3_ModelNo', '_A3_SerialNo', '_A3_SMP_Address'],
                                ['_A4_ModelNo', '_A4_SerialNo', '_A4_SMP_Address'],
                                ['_B1_ModelNo', '_B1_SerialNo', '_B1_SMP_Address'],
                                ['_B2_ModelNo', '_B2_SerialNo', '_B2_SMP_Address'],
                                ['_B3_ModelNo', '_B3_SerialNo', '_B3_SMP_Address'],
                                ['_B4_ModelNo', '_B4_SerialNo', '_B4_SMP_Address'],
                                ['_C1_ModelNo', '_C1_SerialNo', '_C1_SMP_Address'],
                                ['_C2_ModelNo', '_C2_SerialNo', '_C2_SMP_Address'],
                                ['_C3_ModelNo', '_C3_SerialNo', '_C3_SMP_Address'],
                                ['_C4_ModelNo', '_C4_SerialNo', '_C4_SMP_Address'],
                                ['_P1_ModelNo', '_P1_SerialNo'],
                                ['_P2_ModelNo', '_P2_SerialNo']]

            for ele in range(len(M30RB_click_comp)):
                self.click(self.prefix + M30RB_click_comp[ele])
                for e in M30RB_write_comp[ele]:
                    self.read(self.prefix + e, Data, 'reset_read')
            for ele in M30RB_write:
                self.read(self.prefix + ele, Data, 'reset_read')
        if self.prefix == 'M30XA_30XV':
            M30XA_30XV = ['_cooler_cap', '_cooler_ewt', '_cooler_lwt', '_cooler_fluid_type', '_cooler_flow_rate', '_cooler_PD', '_cooler_ambient',
                        '_unit_ModelNo', '_unit_SerialNo', '_cooler_ModelNo', '_cooler_SerialNo', '_comp_A_ModelNo', '_comp_A_SerialNo',
                     '_comp_B_ModelNo', '_comp_B_SerialNo']
            for ele in range(len(M30XA_30XV)):
                self.read(self.prefix + M30XA_30XV[ele], Data, 'reset_read')

        if self.prefix == 'M30XW_30XWV':
            M30XW_30XWV = ["_evaporator_cap", "_evaporator_ewt", "_evaporator_lwt", "_evaporator_fluid_type", "_evaporator_flow_rate", "_evaporator_PD",
                     "_condenser_cap", "_condenser_ewt", "_condenser_lwt", "_condenser_fluid_type", "_condenser_flow_rate", "_condenser_PD", "_unit_ModelNo",
                     "_unit_SerialNo", "_comp_A_ModelNo", "_comp_A_SerialNo", "_comp_B_ModelNo", "_comp_B_SerialNo", "_evaporator_ModelNo", "_evaporator_SerialNo",
                     "_condenser_ModelNo", "_condenser_SerialNo"]
            for ele in M30XW_30XWV:
                self.read(self.prefix + ele, Data, 'reset_read')

        try:
            self.wait_until_element(ChecklistPageLocators.save_form)
            element = driver.find_element_by_xpath(ChecklistPageLocators.save_form[-1])
            driver.execute_script("$(arguments[0]).click();", element)
        except:
            self.wait_until_element(ChecklistPageLocators.save_form_2)
            element = driver.find_element_by_xpath(ChecklistPageLocators.save_form_2[-1])
            driver.execute_script("$(arguments[0]).click();", element)

    def design_data_reset(self):
        print ('Reseting all the values of Design Information(Startup Checklist)')
        self.wait_until_element(ChecklistPageLocators.design_data_reset)
        element = driver.find_element_by_xpath(ChecklistPageLocators.design_data_reset[-1])
        driver.execute_script("$(arguments[0]).click();", element)
        # self.find_element(*ChecklistPageLocators.design_data_reset).click()

    def design_data_exit(self):
        self.find_element(*ChecklistPageLocators.design_data_exit).click()

    def design_data_save(self):
        try:
            self.find_element(*ChecklistPageLocators.design_data_save).click()
        except:
            self.find_element(*ChecklistPageLocators.design_data_save_one).click()

    def design_data_cancel(self):
        self.find_element(*ChecklistPageLocators.design_data_cancel).click()

    def save_form(self):
        try:
            element = driver.find_element_by_xpath(ChecklistPageLocators.save_form[-1])
            driver.execute_script("$(arguments[0]).click();", element)
            # self.find_element('xpath', eval("ChecklistPageLocators.save_form")[-1]).click()
        except Exception:
            element = driver.find_element_by_xpath(ChecklistPageLocators.save_form_2[-1])
            driver.execute_script("$(arguments[0]).click();", element)
            # self.find_element('xpath', eval("ChecklistPageLocators.save_form_2")[-1]).click()
        time.sleep(2)
        self.find_element('xpath', eval("ChecklistPageLocators.save_form_popup_19")[-1]).click()
        time.sleep(2)
        self.find_element('xpath', eval("ChecklistPageLocators.exit_success_popup_msg_19")[-1]).click()
        time.sleep(2)

    def startup_form_cancle(self):
        self.find_element(*ChecklistPageLocators.startup_page_cancel).click()

    def startup_form_reset(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()

    def startup_form_exit(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()

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