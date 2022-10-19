import re
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
sys.path.append(dirnameutils+'\Selenium_Lib')
from Lib_Space.Selenium_Lib.BaseClass import Page
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.ConfigLog_locators import ConfigLogPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.PrestartPage_locators import PreStartPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.PostStartPage_locators import PostStartPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.ChillerNamePlateData_locators import ChillerNamePlateDataPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.PreliminaryEquipCheck_locators import PreliminaryEquipCheckPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.ObliJobData_locators import ObliJobDataPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.SystemStartUp_locators import SystemStartupLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.HumidimizerStartUp_locators import HumidimizerStartUpLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.StartUp_locators import StartUpPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.UnitStartUp_locators import UnitStartUp_locators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.RefrigerationLog_locators import ReflogPageLocators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from selenium.webdriver.common.by import By
import datetime

driver = object
delay = 45


class ChecklistPage(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(ChecklistPage, self).__init__(webdriver)
        driver = webdriver

    def goto_checklist(self):
        self.wait_until_element((ChecklistPageLocators.checklist))
        time.sleep(2.0)
        self.find_element(*ChecklistPageLocators.checklist).click()
        time.sleep(5.0)

    def goto_autofill_cfg(self, conn_type,CCN_name,controller_name):
        print ("*"*5,"Auto_fill Configuration","*"*5)
        #protocol select
        self.wait_unit_visible(ChecklistPageLocators.autofill_tab)
        self.find_element(*ChecklistPageLocators.autofill_tab).click()
        time.sleep(2)


        try:
            # protocol
            self.find_element(*ChecklistPageLocators.autofill_protocol_btn).click()
            time.sleep(1)
            if conn_type=='CCN':
                self.driver.find_element_by_xpath(ChecklistPageLocators.autofill_protocol_lst[-1]+'[2]').click()
            else:
                self.driver.find_element_by_xpath(ChecklistPageLocators.autofill_protocol_lst[-1]+'[1]').click()
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ","Protocol selected as - ",self.find_element(*ChecklistPageLocators.autofill_protocol_btn).text)
            time.sleep(5)
            #CCN name select
            if conn_type=='CCN':
                self.find_element(*ChecklistPageLocators.autofill_ccn_name_btn).click()
                time.sleep(5)
                ele = self.find_elements(*ChecklistPageLocators.autofill_ccn_name_lst)
                for item in range(len(ele)):
                    val=self.driver.find_element_by_xpath(
                            ChecklistPageLocators.autofill_ccn_name_lst[-1] + '[' + str(item+1) + ']')
                    if val.text == CCN_name:
                        val.click()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "CCN Name selected as - ",
                      self.find_element(*ChecklistPageLocators.autofill_ccn_name_btn).text)
                #controller select
                time.sleep(5)
                self.find_element(*ChecklistPageLocators.autofill_ccn_ctrl_btn).click()
                time.sleep(1)
                ele = self.find_elements(*ChecklistPageLocators.autofill_ccn_ctrl_lst)
                for item in range(len(ele)):
                    val= self.driver.find_element_by_xpath(
                        ChecklistPageLocators.autofill_ccn_ctrl_lst[-1] + '[' + str(item+1) + ']')
                    if val.text== controller_name:
                        val.click()
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Controller selected as - ",\
                      self.find_element(*ChecklistPageLocators.autofill_ccn_ctrl_btn).text)
            else:
                # controller select
                self.find_element(*ChecklistPageLocators.autofill_bacnet_ctrl_btn).click()
                time.sleep(1)
                ele = self.find_elements(*ChecklistPageLocators.autofill_bacnet_ctrl_lst)
                for item in range(len(ele)):
                    val= self.driver.find_element_by_xpath(
                        ChecklistPageLocators.autofill_bacnet_lst[-1] + '[' + str(item+1) + ']')
                    if val.text == controller_name:
                        val.click()
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ", "Controller selected as - ",\
                      self.find_element(*ChecklistPageLocators.autofill_bacnet_ctrl_btn).text)
        except Exception as e:
            print(" Autofill config")
        time.sleep(5)
        try:
            self.find_element(*ChecklistPageLocators.autofill_save_btn).click()
            time.sleep(2)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ": ",   self.find_element(*ChecklistPageLocators.autofill_save_msg).text)
        except Exception as e:
            print(f" Auto fill config save error : {e}")
    def goto_new_form(self):

        self.wait_until_element(ChecklistPageLocators.new_form)
        self.wait_until_element((ChecklistPageLocators.create_new_form_text))
        self.find_element(*ChecklistPageLocators.new_form).click()
        self.wait_until_element(ChecklistPageLocators.create_form)

    def create_form(self, form_name):
        if form_name == 'Startup Checklist':
            self.select_startup_form()
            self.create()
        elif form_name == 'Refrigeration LogSheet':
            self.wait_until_element(ChecklistPageLocators.create_ref_form)
            self.find_element(*ChecklistPageLocators.create_ref_form).click()

    def find_form(self, form_type, customer_name):
        self.wait_until_element((ChecklistPageLocators.search))
        i = 1
        while i:
            # try:
            # time.sleep(8)
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
            # except:
            #     print 'Please check the input data'
            #     break

    def existing_form(self):
        self.find_element(*ChecklistPageLocators.existing_form).click()

    def edit_form(self, customer_name, form_type):
        # index = self.find_form(form_type, customer_name)
        time.sleep(3.5)
        path = ('xpath', ChecklistPageLocators.search_customer_name[-1])
        self.wait_until_element(path)
        self.wait_unit_visible(path)
        try:
            self.find_element(*path).click()
        except Exception as e:
            time.sleep(35)
            print(("Took too long to load the page" \
                  "Selenium error:", e))
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
        self.save_form_del()
        form_type = Data['Model'] + ' ' + Data['FormType']
        # index = self.find_form(form_type, Data['CustomerName'])
        # if index == 1:
        # delete_path = ('xpath', ChecklistPageLocators.delete_form[-1])
        # else:
        #     delete_path = ('xpath', ChecklistPageLocators.customer_name[-1] + '/div[' + str(index) + ']/div[7]/ul/li[4]/a/i')
        self.wait_until_element(ChecklistPageLocators.delete_form)
        time.sleep(5)
        try:
            self.wait_until_element(ChecklistPageLocators.delete_form)
            self.find_element(*ChecklistPageLocators.delete_form).click()
            self.driver.find_element_by_xpath(
                ChecklistPageLocators.delete_form[-1] + 'div[1]/div[7]/ul/li[4]/a/i').click()
        except Exception as e:
            print ("Exception occurred while deleting the form")
            print((e))
            time.sleep(5)
            self.wait_until_element(ChecklistPageLocators.delete_form)
            self.driver.find_element_by_xpath(ChecklistPageLocators.delete_form[-1]+'/div[1]/div[7]/ul/li[4]/a/i').click()

        time.sleep(5)
        self.wait_until_element(ChecklistPageLocators.delete_form_yes)
        self.find_element(*ChecklistPageLocators.delete_form_yes).click()
        # self.wait_until_element(ChecklistPageLocators.delete_success_msg)
        print((form_type,' is successfully deleted.'))

    def select_startup_form(self):
        self.find_element(*ChecklistPageLocators.startup_form).click()

    def select_reflog_form(self):
        self.find_element(*ChecklistPageLocators.refrigeration_form).click()

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
        time.sleep(5)
        for option in dropdown.find_elements_by_tag_name('li'):
            if option.text == model_no:
                option.click()
                break

    def serial_no(self, serial_no):
        self.find_element(*ChecklistPageLocators.serial_no).send_keys(serial_no)
        self.find_element(*ChecklistPageLocators.serial_no).send_keys(Keys.ENTER)

    def plant_type(self,plant):
        self.find_element(*ChecklistPageLocators.plant_type).send_keys(plant)
        self.find_element(*ChecklistPageLocators.plant_type).send_keys(Keys.ENTER)

    def refrigerant_type(self, refrigerant):
        self.find_element(*ChecklistPageLocators.refrigerant_type).send_keys(refrigerant)
        self.find_element(*ChecklistPageLocators.refrigerant_type).send_keys(Keys.ENTER)

    def create(self):
        self.wait_until_element(ChecklistPageLocators.create_form)
        self.find_element(*ChecklistPageLocators.create_form).click()
        time.sleep(2)
        self.wait_until_element(ChecklistPageLocators.proceed)
        self.find_element(*ChecklistPageLocators.proceed).click()
        time.sleep(2)
        self.wait_until_element(ChecklistPageLocators.custinfo_title)
        self.customer_details('HRDC','ProView','+917897897987','cst_prv.hrdc@gmail.com')
        time.sleep(2)
    def save_form_del(self):
        try:
            # element = driver.find_element_by_xpath(ChecklistPageLocators.save_form[-1])
            # driver.execute_script("$(arguments[0]).click();", element)
            self.wait_until_element(ChecklistPageLocators.save_form)
            element = driver.find_element_by_xpath(ChecklistPageLocators.save_form[-1])
            driver.execute_script("$(arguments[0]).click();", element)
            #self.find_element('xpath', eval("ChecklistPageLocators.save_form")[-1]).click()
        except Exception as e:
            # element = driver.find_element_by_xpath(ChecklistPageLocators.save_form_2[-1])
            # driver.execute_script("$(arguments[0]).click();", element)
            self.wait_until_element(ChecklistPageLocators.save_form)
            # element = driver.find_element_by_xpath(ChecklistPageLocators.save_form_2[-1])
            # driver.execute_script("$(arguments[0]).click();", element)
            self.find_element('xpath', eval("ChecklistPageLocators.save_form_2")[-1]).click()
            print((e))
        time.sleep(3)
        self.find_element('xpath', eval("ChecklistPageLocators.save_form_popup_19")[-1]).click()
        time.sleep(2)
        self.find_element('xpath', eval("ChecklistPageLocators.exit_success_popup_msg_19")[-1]).click()
        time.sleep(5)

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

    def search_form(self, Data):
        self.form_type = Data['Model'] + ' ' + Data['FormType']
        print(('Searching for the form', Data['CustomerName']))
        self.wait_until_element(ChecklistPageLocators.search_form)
        self.find_element('xpath', ChecklistPageLocators.search_form_input[-1]).send_keys(Data['CustomerName'])
        self.find_element('xpath', ChecklistPageLocators.search_form_input[-1]).send_keys(Keys.ENTER)
        print(('Found form', Data['CustomerName']))

    def email_existing_form(self, Data):
        self.wait_until_element(ChecklistPageLocators.mail_form)
        element = driver.find_element_by_xpath(ChecklistPageLocators.mail_form[-1])
        driver.execute_script("$(arguments[0]).click();", element)
        self.wait_until_element(ChecklistPageLocators.recipients_mails)
        element = driver.find_element_by_xpath(ChecklistPageLocators.recipients_mails[-1])
        driver.execute_script("$(arguments[0]).click();", element)
        time.sleep(2)
        self.find_element('xpath', ChecklistPageLocators.recipients_mails[-1]).send_keys(Data['UserID'])
        self.find_element('xpath', ChecklistPageLocators.search_form[-1]).send_keys(Keys.ENTER)
        element = driver.find_element_by_xpath(ChecklistPageLocators.send_email[-1])
        driver.execute_script("$(arguments[0]).click();", element)
        while 1:
            try:
                self.wait_until_element(ChecklistPageLocators.loading_email_status)
            except:
                break
        print((self.form_type + ' has been emailed to ', Data['UserID']))

    def edit_existing_form(self, Data):
        form_type = Data['Model'] + ' ' + Data['FormType']
        self.edit_form(Data['CustomerName'], form_type)
        time.sleep(1.0)


    def save_form(self):
        element = driver.find_element_by_xpath(ChecklistPageLocators.save_form[-1])
        driver.execute_script("$(arguments[0]).click();", element)
        time.sleep(2)
        self.find_element(*ChecklistPageLocators.save_form_pop_name).clear()
        self.find_element(*ChecklistPageLocators.save_form_pop_name).send_keys("Tech")
        job_date=(datetime.datetime.now().strftime("%m/%d/%Y"))

        self.find_element(*ChecklistPageLocators.save_form_pop_date).send_keys(job_date)

        self.find_element('xpath', eval("ChecklistPageLocators.save_form_popup_19")[-1]).click()
        time.sleep(2)
        self.find_element('xpath', eval("ChecklistPageLocators.exit_success_popup_msg_19")[-1]).click()
        time.sleep(2)

    def save_section(self):
        try:
            self.wait_until_element(ChecklistPageLocators.save_form)
            element = driver.find_element_by_xpath(ChecklistPageLocators.save_form[-1])
            driver.execute_script("$(arguments[0]).click();", element)

        except Exception as e:
            self.wait_until_element(ChecklistPageLocators.save_form)
            self.find_element('xpath', eval("ChecklistPageLocators.save_form_2")[-1]).click()
            print((e))
        time.sleep(3.0)

    def export_from(self):
        self.wait_until_element(ChecklistPageLocators.export_form)
        element = driver.find_element_by_xpath(ChecklistPageLocators.export_form[-1])
        driver.execute_script("$(arguments[0]).click();", element)
        time.sleep(30)
        print('Checklist has been downloaded. Please check the download folder.')

    def goto_menu(self, Data, page_locators, menu):
        self.wait_until_element(eval(page_locators+"."+menu))
        time.sleep(2)
        element = self.find_elements(*(eval(page_locators+"."+menu)))
        try:
            element[int(Data['Checklist index'])].click()
        except:
            element = self.find_elements(*(eval(page_locators+"."+menu+"_filled")))
            element[int(Data['Checklist index'])].click()

    def goto_submenu(self, Data, page_locators, submenu):
        self.wait_until_element(eval(page_locators+"."+ submenu))
        time.sleep(2)
        element = self.find_elements(*(eval(page_locators+"."+ submenu)))
        try:
            element[int(Data['SubMenu Index'])].click()
        except:
            element = self.find_elements(*(eval(page_locators+"."+ submenu +"_filled")))
            element[int(Data['SubMenu Index'])].click()

    def click(self, xpath, page_locators):
        self.find_element('xpath', eval(page_locators+"." + xpath)[-1]).click()

    def write(self, xpath, Data):
        self.find_element('xpath', xpath[-1]).send_keys(str(Data['testdata']))
        time.sleep(0.5)
        self.find_element('xpath', xpath[-1]).send_keys(Keys.ENTER)
        time.sleep(0.5)

    def write_similar_element(self, xpath, index, Data):
        xpath[index].send_keys(Data['testdata'])
        xpath[index].send_keys(Keys.ENTER)

    def read(self, xpath, common_xpath, Data, command, page_locators, index_assert=None):
        if command == 'read_normal':
            try:
                value = self.find_element('xpath', eval(page_locators+"." + xpath)[-1]).get_attribute('value')
                return value
            except Exception as e:
                print(e)
            # if index_assert == None:
            #     return value
            # else:
            #     pass
                # assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:index_assert]), True)

        if command == 'read':
            list_index = eval(page_locators+"." +xpath)
            value = common_xpath[list_index].get_attribute('value')
            return value

        elif command == 'yes|no':
            value = self.find_element('xpath', eval(page_locators+"." + xpath)[-1]+'/..')
            for option in value.find_elements_by_tag_name('input'):
                value = option.get_attribute('checked')
            return value

        elif command == 'reset_read':
            # self.wait_until_element(page_locators+".poststart_reset")
            list_index = eval(page_locators+"." + xpath)
            value = common_xpath[list_index].get_attribute('value')
            return value

        elif command == 'reset_read_normal':
            # self.wait_until_element(page_locators+".poststart_reset")
            value = eval(page_locators+"." + xpath).get_attribute('value')
            return value

        elif command == 'reset_yes|no':
            value = self.find_element('xpath', eval(page_locators+"." + xpath)[-1] + '/..')
            for option in value.find_elements_by_tag_name('input'):
                value = option.get_attribute('checked')
                return value

    def read_reset_data(self, Data, page_locators):
        for ele in eval("self."+self.prefix[Data['Model']]+"_same_writables"):
            if ele != self.prefix[Data['Model']]+"_Default":
                self.read(ele, Data, 'reset_read', page_locators=page_locators, index_assert=5)
        for ele in eval("self."+self.prefix[Data['Model']]+"_clickables"):
            self.read(ele, Data, 'reset_yes|no', page_locators=page_locators)

        self.wait_until_element(ChecklistPageLocators.save_form)
        element = driver.find_element_by_xpath(ChecklistPageLocators.save_form[-1])
        driver.execute_script("$(arguments[0]).click();", element)

    def set_dropdown(self, xpath, index):
        pass

    def reset(self):
        print ('Reseting all the values of Design Information(Startup Checklist)')
        self.wait_until_element(ChecklistPageLocators.reset)
        element = driver.find_element_by_xpath(ChecklistPageLocators.reset[-1])
        driver.execute_script("$(arguments[0]).click();", element)

    def customer_details(self,compname,poc,phno,emailaddr):
        print('*'*10,"Customer details","*"*10)
        self.find_element(*ChecklistPageLocators.custinfo_compname).clear()
        self.find_element(*ChecklistPageLocators.custinfo_compname).send_keys(compname)
        self.find_element(*ChecklistPageLocators.custinfo_poc).clear()
        self.find_element(*ChecklistPageLocators.custinfo_poc).send_keys(poc)
        self.find_element(*ChecklistPageLocators.custinfo_phno).clear()
        self.find_element(*ChecklistPageLocators.custinfo_phno).send_keys(phno)
        self.find_element(*ChecklistPageLocators.custinfo_email).clear()
        self.find_element(*ChecklistPageLocators.custinfo_email).send_keys(emailaddr)

        self.find_element(*ChecklistPageLocators.custinfo_save).click()

