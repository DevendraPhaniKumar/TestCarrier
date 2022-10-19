import os
import sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(dirnameutils)
sys.path.append(utils)
sys.path.append(dirnameutils+'\Selenium_Lib')
from Selenium_Lib.BaseClass import Page
from Page_locators.HomePage_locatars import HomePageLocatars
from Page_locators.ConnectPage_locators import ConnectPageLocators
from Page_locators.ChillerInfoPage_locators import ChillerinfoPageLocators
from Page_locators.SettingsPage_locators import SettingPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
import configparser
import time
import datetime
driver = object
delay = 30

class ChillersettingsPage(Page):
    global driver, delay
    def __init__(self, webdriver):
        global driver
        super(ChillersettingsPage, self).__init__(webdriver)
        driver = webdriver

    def wait(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element[-1])))
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Page is ready!!")
            return 0
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Loading took too much time!")
            filename1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.driver.save_screenshot('Timeout_' + filename1 + '.png')
            return 1

    def setting_page(self):
        try:
            self.find_element(*SettingPageLocators.home_setting_btn).click()
        except:
            self.find_element(*SettingPageLocators.setting_icon_btn).click()


    def chillerinfo_setting(self):
        print("****Chiller Settings****")
        time.sleep(2.0)
        self.find_element(*SettingPageLocators.chiller_info_setting_btn).click()
        self.wait(SettingPageLocators.chiller_settings_title)
        model = self.find_element(*SettingPageLocators.chiller_model).get_attribute('value')
        version = self.find_element(*SettingPageLocators.chiller_version).get_attribute('value')
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Model- ",model,"\tVersion- ",version)

    def chiller_table(self):
        print("*****Chiller Config List******")
        self.wait(SettingPageLocators.chiller_settings_title)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":",self.find_element(
            *SettingPageLocators.chiller_cfg_title).text)
        #print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", "Table Headers\n",self.find_element(*SettingPageLocators.chiller_cfg_table_labels).text
        table_content = self.find_elements('xpath', '//div[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/*')
        if len(table_content) == 0: print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", "No chiller is model onboarded ")
        else:  print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", "No.of chiler models onboarded: ", len(table_content))
        chiller_model = []
        chiller_ver = []
        for tcnt in range(1, len(table_content)+1):
            chiller_model.insert(tcnt-1, str(
                self.find_element('xpath', '//div[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[' + str(
                    tcnt) + ']/div[2]').text))
            chiller_ver.insert(tcnt- 1, str(
                self.find_element('xpath', '//div[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[' + str(
                    tcnt) + ']/div[4]').text))
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),": ", tcnt,"model:", chiller_model[tcnt-1],\
                "version", chiller_ver[tcnt-1])
        for id in range(len(table_content),0,-1):
            print(id, chiller_model[id-1])
            self.chiller_cfg_action(chiller_model[id-1],"Edit","No")
            self.chiller_cfg_action(chiller_model[id-1],"Delete","No")
            self.chiller_cfg_action(chiller_model[id-1],"Delete","Yes")


    def chiller_cfg_action(self,model,action,delete):
        print("******Data point action test******")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", model,action, delete)
        self.search_key(model)
        time.sleep(2.0)
        search_result = self.find_elements('xpath', '//div[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/*')
        if len(search_result) == 0:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", " No result found with model ", model)
            return
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","No.of items",len(search_result))
        for tcnt in range(1, len(search_result)+1):
            ver = str(self.find_element('xpath', '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[' + str(
                tcnt) + ']/div[2]').text)
            if ver != model:
                print("Read model:", ver)
                break
            if action == "Edit":
                try:
                    self.find_element('xpath', '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[' + str(
                    tcnt) + ']/div[5]/ul/li[1]/a/i').click()
                    self.wait(SettingPageLocators.chiller_version)
                    chiller_model = str(self.find_element(*SettingPageLocators.chiller_version).get_attribute("value"))
                    print(tcnt, ":", model, "/ ",chiller_model)
                    assert model, chiller_model
                    self.find_element(*SettingPageLocators.setting_save_btn).click()
                except:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","exception occured")
                time.sleep(2.0)
                if len(search_result) >> 1:
                    self.find_element(*SettingPageLocators.point_search).send_keys(model)
                    time.sleep(2.0)
            elif action =="Delete":
                if delete == "Yes":
                    print(tcnt, ":", model, "/ ", ver)
                    self.find_element('xpath','//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div['+str(tcnt)+']/div[5]/ul[1]/li[2]/a[1]/i[1]').click()
                    try:
                        time.sleep(3.0)
                        print(self.find_element(*SettingPageLocators.chiller_cfg_delete_yes).text)
                        self.wait(SettingPageLocators.chiller_cfg_delete_yes)
                        self.find_element(*SettingPageLocators.chiller_cfg_delete_yes).click()
                        self.wait(SettingPageLocators.chiller_cfg_title)
                        search_result = self.find_elements('xpath','//div[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/*')
                        if search_result !=0: print("Search result after delete :",str(len(search_result)))
                        #assert len(search_result)== 0,"Assert failed:" + str(len(search_result))
                    except:
                        time.sleep(2.0)
                        print(self.find_element(*SettingPageLocators.chiller_cfg_delete_connected).text)
                        self.wait(SettingPageLocators.chiller_cfg_delete_connected)
                        self.find_element(*SettingPageLocators.chiller_cfg_delete_warn_accept).click()
                        self.wait(SettingPageLocators.chiller_cfg_title)
                else:#Delete but say no
                    print(tcnt, ":", model, "/ read model", ver)
                    try:
                        self.find_element('xpath', '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[' + str(
                        tcnt) + ']/div[5]/ul[1]/li[2]/a[1]/i[1]').click()
                        time.sleep(2.0)
                        print(self.find_element(*SettingPageLocators.chiller_cfg_delete_no).text)
                        self.wait(SettingPageLocators.chiller_cfg_delete_yes)
                        self.find_element(*SettingPageLocators.chiller_cfg_delete_no).click()
                        #assert model, str(self.find_element('xpath', '//*[@id="content"]/div[1]/div[2]/div[2]/div[
                        # 1]/div[2]/div[' + str(tcnt) + ']/div[2]').text)
                    except:
                        time.sleep(2.0)
                        print(self.find_element(*SettingPageLocators.chiller_cfg_delete_connected).text)
                        self.wait(SettingPageLocators.chiller_cfg_delete_connected)
                        self.find_element(*SettingPageLocators.chiller_cfg_delete_warn_accept).click()
                        self.wait(SettingPageLocators.chiller_cfg_title)
                time.sleep(2.0)
        model =""
        self.find_element(*SettingPageLocators.point_search).clear()
    def chiller_table_pagination(self):
        print("*****Chiller Config Pagination******")
        self.wait(SettingPageLocators.chiller_settings_title)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":",self.find_element(
            *SettingPageLocators.chiller_cfg_title).text)
        try:
            self.wait(SettingPageLocators.chiller_cfg_page_loe)
            page_size = self.find_elements(*SettingPageLocators.chiller_cfg_page_loe)

            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":","No.of pages:", len(page_size)-4)
            for page_no in range(1,len(page_size)+1):
                page_index = self.find_element('xpath',
                                  '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/dir-pagination-controls[1]/ul/li['+
                                  str(page_no)+']/a')
                print(page_no, page_index.text)
                page_index.click()
                table_content = self.find_elements('xpath', '//div[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/*')
                if len(table_content) != 0:  print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "No.of chiler models onboarded: ", len(table_content))
                else:   print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "No chiller is model onboarded ")
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "No pages found view chiller " \
                                                                             "configuration")

    def chiller_datapoint_actions(self,data_point,action, dp_edit='No',dp_trend='No'):
        print("********Chiller Data point Actions**********")
        self.wait(SettingPageLocators.chiller_cfg_edit_title)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", self.find_element(
            *SettingPageLocators.chiller_cfg_edit_title).text)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", data_point,action,dp_edit,dp_trend)
        self.search_key(data_point)
        table_ele = self.find_elements('xpath', '//div[@id="datapoint"]/*')
        if len(table_ele) > 2:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "There may be duplicate points, " \
                                                                                  "data may not be saved")
            return
        self.find_element(*SettingPageLocators.dp_edit).click()
        self.wait(SettingPageLocators.dp_edit_title)
        for id in range(1,8):
            details_text = self.find_element('xpath','//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div['
                                                     '1]/ul[1]/li['+str(id)+']/label').text
            details_val = self.find_element('xpath', '//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div['
                                                      '1]/ul[1]/li[' + str(id) + ']/div[1]/input').get_attribute(
                'value')
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"\t",details_text,":",details_val)

        if (action.lower())=="write":
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(self.find_element(
                *SettingPageLocators.dp_edit_write_txt).text))
            if (dp_edit.lower()) =="yes":
                state = self.find_element(*SettingPageLocators.dp_edit_write_btn).is_selected()
                if state:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", "Write already selected")
                else:
                    self.find_element(*SettingPageLocators.dp_edit_write_btn).click()
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":","Write option Selected")
            else:
                state = self.find_element(*SettingPageLocators.dp_edit_write_btn).is_selected()
                if not(state):
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "Write already unselected")
                else:
                    self.find_element(*SettingPageLocators.dp_edit_write_btn).click()
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":","Write option unselected")
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(self.find_element(
                *SettingPageLocators.dp_edit_trend_txt).text))
            if (dp_trend.lower()) =="yes":
                state = self.find_element(*SettingPageLocators.dp_edit_trend_btn).is_selected()
                if state:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", "Trend already selected")
                else:
                    self.find_element(*SettingPageLocators.dp_edit_trend_btn).click()
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":","Trend Option selected")
            else:
                state = self.find_element(*SettingPageLocators.dp_edit_trend_btn).is_selected()
                if not(state):
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", "Trend already unselected")
                else:
                    self.find_element(*SettingPageLocators.dp_edit_trend_btn).click()
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":","Trend Option unselected")
        self.find_element(*SettingPageLocators.dp_edit_save).click()
        time.sleep(2.0)
        try:
            self.wait(SettingPageLocators.dp_edit_ccn_err_msg)
            self.wait(SettingPageLocators.dp_edit_ccn_field_mand_msg)
            err_msg = self.find_element(*SettingPageLocators.dp_edit_ccn_err_msg).text
            mand_msg = self.find_element(*SettingPageLocators.dp_edit_ccn_field_mand_msg).text
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","Error occured- ", err_msg, mand_msg,\
                "\nClosing edit point dialog instead of saving")
            self.find_element(*SettingPageLocators.dp_edit_close).click()
            time.sleep(2.0)
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","No Error Messages")
        self.find_element(*SettingPageLocators.point_search).clear()
        time.sleep(1.0)

    def search_key(self,data_point,dp='dp'):
        print("*****Search******** ",data_point)
        self.wait(SettingPageLocators.point_search)
        self.find_element(*SettingPageLocators.point_search).send_keys(data_point)
        time.sleep(1.0)
        search_key = str(self.find_element(*SettingPageLocators.point_search).get_attribute("value"))
        if search_key != data_point:
            self.find_element(*SettingPageLocators.point_search).clear()
            print(datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"), ":", "DATA POINT is not entered in search field", search_key)
            self.find_element(*SettingPageLocators.point_search).send_keys(data_point)
        if point == 'dp':
            dp_text = str(self.find_element(*SettingPageLocators.dp_display_textname).get_attribute(\
                'value'))
            assert (dp_text == data_point),"Data point doesn't match"
        else:
            dp_text = str(self.find_element(*SettingPageLocators.table_chiller_vername).get_attribute( \
                'value'))
            assert (dp_text == data_point), "Data point doesn't match"

    def datapoint_prognostics_rule(self,  data_point, min_val, max_val, unit_type, color, message):
        print("****Data Point Progronstic Rule*******")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","DP- ",data_point,"MIN- ", min_val,\
            "MAX- ", max_val, "Unit- ",  unit_type, "Color code- ",color,"n\Message - ", message)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", self.find_element(
            *SettingPageLocators.chiller_cfg_edit_title).text)
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        self.search_key(data_point)
        self.find_element(*SettingPageLocators.prog_btn).click()
        self.wait(SettingPageLocators.prog_rule_dialog_title)
        rule_ele =self.find_elements('xpath','//div[@id="content"]/div/div[2]/div[2]/div/div[1]/*')
        self.set_datapoint_prognostics_rule(data_point, min_val, max_val, unit_type, color, message)
        if len(rule_ele)>2:
            print("No.of Rules created: ",len(rule_ele))
            for id in range(2, len(rule_ele)):
                details = self.get_datapoint_prognostics_rule(data_point, id)
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","Rule No.",id, "\n",\
                    '\tMin Val- ',details[0],"\tMax Val- ",details[1],"\tUnit- ",details[2],"\tColor- ", details[3], \
                    "\tMessage- ",details[4])
                details = ""
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "No rule created")
        self.find_element(*SettingPageLocators.prog_exit).click()
        time.sleep(2.0)
        self.wait(SettingPageLocators.chiller)

    def set_datapoint_prognostics_rule(self,  data_point, min_val, max_val, unit_type, color, message):
        print("****Data Point Progronstic Rule- Set*******")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","DP- ",data_point,"MIN- ", min_val,\
            "MAX- ", max_val, "Unit- ",  unit_type, "Color code- ",color,"n\Message - ", message)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", self.find_element(
            *SettingPageLocators.chiller_cfg_edit_title).text)
        self.find_element(*SettingPageLocators.prog_new_rule).click()
        self.wait(SettingPageLocators.prog_rule_dialog_title)
        rule_ele = self.find_elements(*SettingPageLocators.prog_rule_loe)
        for elements in range(1,len(rule_ele)+1):
            label = str(self.find_element('xpath',
                                          '//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div/ul/li[' + str(
                                              elements) + ']/label').text)
            assert (SettingPageLocators.rule_labels[elements-1]== label),"Label Doesnot match"
            if (elements == 1):
                self.find_element('xpath', '//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li['
                                           '1]/div[1]/input').send_keys(max_val)
            elif (elements == 2):
                self.find_element('xpath', '//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li['
                                           '2]/div[1]/input').send_keys(min_val)
            elif(elements==3):
                self.find_element(*SettingPageLocators.prog_unit_btn).click()
                self.find_elements(*SettingPageLocators.prog_unit_loe)
                items = self.driver.find_element_by_link_text(unit_type)
                items.click()
            elif(elements==4):
                self.find_element(*SettingPageLocators.dp_color_loe).click()
                self.find_element('xpath','//*[@id="myModal"]/div/div/form/div/div[2]/div/ul/li['
                                          '4]/div/div/div/div/div/div/div/div['+str(color)+']').click()
            else:
                self.find_element(*SettingPageLocators.prog_rule_message).send_keys(message)
        self.find_element(*SettingPageLocators.prog_rule_save).click()
        try:
            if(self.wait(SettingPageLocators.prog_rule_max_err_msg)):
                msg = self.find_element(*SettingPageLocators.prog_rule_max_err_msg).text
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","max val",msg)
            elif(self.wait(SettingPageLocators.prog_rule_min_err_msg)):
                msg = self.find_element(*SettingPageLocators.prog_rule_min_err_msg).text
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","min val",msg)
            elif(self.wait(SettingPageLocators.prog_rule_msg_err_msg)):
                msg = self.find_element(*SettingPageLocators.prog_rule_msg_err_msg).text
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "msg input", msg)
            self.find_element(*SettingPageLocators.prog_rule_close).click()
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","Set rule successfully")

    def get_datapoint_prognostics_rule(self,  data_point, id):
        print("****Data Point Progronstic Rule- Read*******")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":","DP- ",data_point)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", self.find_element(
            *SettingPageLocators.chiller_cfg_edit_title).text)
        rule_details =[]
        for cnt in range(0,5):
            if cnt == 3:
                rule_details.insert(cnt,(Color.from_string(str(self.find_element('xpath','//*[@id="content"]/div/div[2]/div['
                      '2]/div/div/div['+str(id)+']/div['+str(cnt+1)+']/span').value_of_css_property('background-color'))).hex))
            else:
                rule_details.insert(cnt, str(self.find_element('xpath','//*[@id="content"]/div/div[2]/div['
                                          '2]/div/div/div['+str(id)+']/div['+str(cnt+1)+']').text))
        return rule_details

    def set_datapoint_prognostics_reference(self, data_point, val, condition, unit_type,color, message):
        print("****Data Point Progronstic Rule- Set*******")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "DP- ", data_point, "Val- ", val, \
            "Condition- ", condition, "Unit- ", unit_type, "Color code- ", color, "n\Message - ", message)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", self.find_element(
            *SettingPageLocators.chiller_cfg_edit_title).text)
        self.find_element(*SettingPageLocators.prog_new_ref_rule).click()
        self.wait(SettingPageLocators.prog_rule_dialog_title)
        rule_ele = self.find_elements(*SettingPageLocators.prog_rule_loe)
        for elements in range(1, len(rule_ele) + 1):
            label = str(self.find_element('xpath',
                                          '//*[@id="myModalRR"]/div[1]/div[1]/form[1]/div[1]/div[2]/div/ul/li[' + str(
                                              elements) + ']/label').text)
            assert (SettingPageLocators.rule_labels[elements - 1] == label), "Label Doesnot match"
            if (elements == 1):
                self.find_element('xpath', '//*[@id="myModalRR"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li['
                                           '1]/div[1]/input').send_keys(max_val)
            elif (elements == 2):
                self.find_element(*SettingPageLocators.prog_unit_btn).click()
                self.find_elements(*SettingPageLocators.prog_unitrr_loe)
                items = self.driver.find_element_by_link_text(unit_type)
                items.click()
                self.find_element('xpath', '//*[@id="myModalRR"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li['
                                           '2]/div[1]/input').send_keys(val)
            elif (elements == 3):
                self.find_element(*SettingPageLocators.prog_cond_btn_btn).click()
                self.find_elements(*SettingPageLocators.prog_cond_loe)
                items = self.driver.find_element_by_link_text(cond)
                items.click()
            elif (elements == 4):
                self.find_element(*SettingPageLocators.dp_color_loe).click()
                self.find_element('xpath', '//*[@id="myModalRR"]/div/div/form/div/div[2]/div/ul/li['
                                           '4]/div/div/div/div/div/div/div/div[' + str(color) + ']').click()
            else:
                self.find_element(*SettingPageLocators.prog_rule_message).send_keys(message)
        self.find_element(*SettingPageLocators.prog_rule_save).click()
        try:
            if (self.wait(SettingPageLocators.prog_rule_val_err_msg)):
                msg = self.find_element(*SettingPageLocators.prog_rule_val_err_msg).text
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "max val", msg)
            elif (self.wait(SettingPageLocators.prog_rule_cond_err_msg)):
                msg = self.find_element(*SettingPageLocators.prog_rule_cond_err_msg).text
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "min val", msg)
            elif (self.wait(SettingPageLocators.prog_rule_msg_err_msg)):
                msg = self.find_element(*SettingPageLocators.prog_rule_msg_err_msg).text
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "msg input", msg)

            self.find_element(*SettingPageLocators.prog_rule_close).click()
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "No Error Message")

    def get_datapoint_prognostics_reference(self, data_point,id):
        print("****Data Point Progronstic Rule Reference- Read*******")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", "DP- ", data_point)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ":", self.find_element(
            *SettingPageLocators.chiller_cfg_edit_title).text)
        rule_details = []
        for cnt in range(0, 5):
            if cnt == 3:
                rule_details.insert(cnt, (
                    Color.from_string(str(self.find_element('xpath', '//*[@id="content"]/div/div[2]/div['
                                                                     '2]/div/div[6]/div[' + str(id) + ']/div[' + str(
                        cnt + 1) + ']/span').value_of_css_property('background-color'))).hex))
            else:
                rule_details.insert(cnt, str(self.find_element('xpath', '//*[@id="content"]/div/div[2]/div['
                                                                        '2]/div/div[6]/div[' + str(id) + ']/div[' + str(
                    cnt + 1) + ']').text))
        return rule_details
    def datapoint_list(self,chiller_version,conn_type="CCN"):
        self.wait(SettingPageLocators.chiller_cfg_title)
        self.search_key((chiller_version.split(" "))[1],'ver')
        self.find_element(*SettingPageLocators.chiller_cfg_action_edit).click()
        self.wait(SettingPageLocators.chiller_cfg_edit_title)
        print("Chiller version: ",self.find_element(*SettingPageLocators.chiller_version).get_attribute('value'))
        if conn_type=="CCN":
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.find_element( *SettingPageLocators.display_text_title).text, ":", self.find_element(*SettingPageLocators.ccn_point_title).text)
            self.find_elements(*SettingPageLocators.datapoint_table_loe)
            ele = self.find_elements('xpath', '//div[@id="datapoint"]/*')
            dp_list = {}
            for tcnt in range(2, len(ele)-1):
                try:
                    dp_text = str(self.find_element('xpath', '//*[@id="datapoint"]/div[' + str(tcnt) + ']/div[3]').text)
                    dp_point = str(self.find_element('xpath', '//*[@id="datapoint"]/div[' + str(tcnt) + ']/div[6]').text)
                    print(tcnt, dp_text, ":", dp_point)
                except:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"No Element found")
                dp_list[dp_text] = dp_point
                print(dp_list[dp_text])
            return dp_list
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.find_element(*SettingPageLocators.display_text_title).text,",",self.find_element(*SettingPageLocators.bacnet_point_title).text)
            self.find_elements(*SettingPageLocators.datapoint_table_loe)
            ele = self.find_elements('xpath', '//div[@id="datapoint"]/*')
            dp_list = {}
            for tcnt in range(2, len(ele)-1):
                try:
                    dp_text = str(self.find_element('xpath', '//*[@id="datapoint"]/div[' + str(tcnt) + ']/div[3]').text)
                    dp_point = str(self.find_element('xpath', '//*[@id="datapoint"]/div[' + str(tcnt) + ']/div[5]').text)
                    print(tcnt, dp_text, ":", dp_point)
                except:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "No Element found")
                dp_list[dp_text] = dp_point
            return dp_list
    def save_setting(self):
        self.wait(SettingPageLocators.chiller_cfg_edit_title)
        self.find_element(*SettingPageLocators.setting_save_btn).click()
        self.wait(SettingPageLocators.chiller_cfg_title)