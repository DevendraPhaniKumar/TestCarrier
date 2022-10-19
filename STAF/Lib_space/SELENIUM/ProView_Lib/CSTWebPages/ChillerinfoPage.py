import os
import sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(dirnameutils)
sys.path.append(utils)
# from openpyxl import Workbook
sys.path.append(dirnameutils+'\Selenium_Lib')
from Selenium_Lib.BaseClass import Page
from Page_locators.HomePage_locatars import HomePageLocatars
from CSTWebPages.ChillerSettingsPage import *
from Page_locators.ChillerInfoPage_locators import ChillerinfoPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
import configparser
bacnet_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(bacnet_path + "\Lib_Space")
from Lib_Space.BACNET_Lib import BACnet_Module
# import CCN_Lib

import time
import datetime
driver = object
delay = 45

class ChillerinformationPage(Page):
    global driver, delay,start_date, end_date, start_point, end_point, start_cond, end_cond, start_val, end_val, sample_interval
    def __init__(self, webdriver):#,ccn_handle):
        global driver,bacnet
        super(ChillerinformationPage, self).__init__(webdriver)
        driver = webdriver
        # self.ccn_handle = ccn_handle
        bacnet = BACnet_Module.Adapter(bacnet_path+r'\Lib_Space\BACNET_Lib\Adpater_setting.ini')
    def wait(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element[-1])))
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "page is ready!!")
            return 0
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Loading took too much time!")
            filename1 = "Chillerinfopage"
            self.screen_capture(filename1)
            return 1

    def enter_page(self, webdriver):
        global driver
        driver = webdriver
        self.find_element(*ChillerinfoPageLocators.chillerinfo_btn).click()

    def chiller_details(self,model):
        print("********Chiller Details Validation**********")
        self.wait(ChillerinfoPageLocators.chiller_status)
        model_val = self.find_element(*ChillerinfoPageLocators.chiller_model).text
        chiller_version = self.find_element(*ChillerinfoPageLocators.chiller_version).text
        try:
            assert model,model_val
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"\tExpect: ",chiller_version, "\tActual: ",\
                model_val)

        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":","chiller model & version \n",model_val, chiller_version)
        return model_val +" "+ chiller_version

    def read_tables(self,Data):
        print("*********Bacnet object validation********")
        try:
            table_list = self.find_elements(*ChillerinfoPageLocators.dtable_LOE)
            print("No.of Objects :", len(table_list))
            for i in range(1, len(table_list)):
                try:
                    object_item = ChillerinfoPageLocators.dtable_LOE[-1]
                    table_text = str(self.find_element('xpath', object_item+'[' + str(
                        i) + ']').text)
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i, "ObjectId:", table_text)
                    self.find_element('xpath', object_item + '[' + str(i) + ']').click()
                    time.sleep(1.0)
                    self.wait(ChillerinfoPageLocators.table_header)
                    self.data_point_validation(table_text,Data)
                except:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i, "table text not found")
                ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
                print ("\n")
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Tables not loaded")

    def data_point_validation(self, table_text,Data ):
        print("**** Data point validation***")
        disp_text_list =[]
        try:
            assert table_text, str(self.find_element(*ChillerinfoPageLocators.table_text).text)
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", str(self.find_element(*ChillerinfoPageLocators.table_text).text))
        prop_lst = self.find_elements(*ChillerinfoPageLocators.table_loe)
        print ("Object: ", table_text,"Properties Count:",len(prop_lst))
        prop_value = table_text.split (" - ")[0]
        try:
            self.bacnet.set_destination(Data["BACnet_Ip"])

            object_type = ((prop_value.split(',')[0]).strip('(')).split('-')[0] + \
                      ((prop_value.split(',')[0]).strip('(')).split('-')[1].capitalize()
            object_id = (prop_value.split(',')[1]).strip(')')
            print(object_type, " - ", object_id)
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":",'\t')
            for count in range (1,len(prop_lst)):
                prop_id_path = ChillerinfoPageLocators.table_loe[-1]
                prop_id = self.find_element('xpath',prop_id_path+'['+str(count)+']/td[1]').text
                prop_value = self.find_element('xpath',prop_id_path + '['+str(count)+']/td[2]/input').get_attribute('value')

                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":",table_text, count,"\t", prop_id,"\t",prop_value)
                print ("\t\t backend value :",self.bacnet.read_property(object_type,object_id,prop_id))
        except:
            print ("exception occured at point read and compare")
            self.bacnet.disconnect()


    def toggle_refresh(self):
        print ("Upload data from Bacnet device")
        self.find_element(*ChillerinfoPageLocators.refresh).click()
        self.wait(ChillerinfoPageLocators.refresh)
    def search_object(self,object_name):
        self.find_element(*ChillerinfoPageLocators.search_object_input).click()
        self.find_element(*ChillerinfoPageLocators.search_object_input).send_keys(object_name)

        try:
            table_list = self.find_elements(*ChillerinfoPageLocators.dtable_LOE)
            print("No.of Objects :", len(table_list))
            for i in range(1, len(table_list)):
                try:
                    object_item = ChillerinfoPageLocators.dtable_LOE[-1]
                    table_text = str(self.find_element('xpath', object_item + '[' + str(i) + ']').text)
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i, "ObjectId:", table_text)
                    self.find_element('xpath', object_item + '[' + str(i) + ']').click()
                    self.wait(ChillerinfoPageLocators.table_header)
                except:
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i," object not found")
        except:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i, " search result not found")

    def record_data_config(self,table_l,action,sel_type='all',clear_point='none'):
        print('*' * 5, 'Data configuration', '*' * 5)
        if(action =='add'):
            if(self.find_element(*ChillerinfoPageLocators.record_data_summary_empty_msg).text==
                ChillerinfoPageLocators.record_data_summary_empty_msg_txt):
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":",self.find_element(*ChillerinfoPageLocators.record_data_summary_empty_msg).text)
                time.sleep(2.0)
            else: print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":","Previously data points are " \
                                                                                  "selected and will be appended with current selection")
            print(self.find_element(*ChillerinfoPageLocators.record_data_table_lbl).text," Select")
            for t_items  in range(1, len(table_l)):
                if self.record_data_table_sel(table_l[t_items-1]):
                    print(table_l[t_items-1]," Table present")
                    try:
                        if self.wait(ChillerinfoPageLocators.record_data_pts_lst)==0:
                            pnt_list = self.find_elements(*ChillerinfoPageLocators.record_data_pts_lst)
                            if(sel_type =='all'):
                                if(self.find_element(*ChillerinfoPageLocators.record_data_selectall_chk).is_selected()):
                                    print("All table points selected")
                                else:
                                    self.find_element(*ChillerinfoPageLocators.record_data_selectall_chk).click()
                                    time.sleep(0.5)
                            else: #random pick
                                for pnt_item in range(2,len(pnt_list),3):
                                    pnt_path = ChillerinfoPageLocators.record_data_pts_lst[-1]+'['+str(
                                        pnt_item)+']/div/div/label/input'
                                    pnt_txt= self.find_element('xpath',pnt_path[:-5]).text
                                    self.find_element('xpath',pnt_path).click()
                                    time.sleep(0.5)
                                    if(self.find_element('xpath',pnt_path).is_selected()): print(pnt_txt,"point selected")
                                    else:
                                        print(pnt_txt,"Not selected")
                            print("Points for table selected", table_l[t_items - 1], " are: ")
                            for pts in range(2, len(pnt_list)):
                                pnt_path = ChillerinfoPageLocators.record_data_pts_lst[-1] + '[' + str(
                                    pts) + ']/div/div/label/span'
                                pnt_name = self.find_element('xpath', pnt_path).text
                                print(pts - 1, pnt_name)
                        elif self.wait(ChillerinfoPageLocators.record_data_summary_empty_msg) == 0:
                            print("table not present, continuing for next table")
                    except:
                        if(self.wait(ChillerinfoPageLocators.record_data_summary_empty_msg)==0):
                            print("Exception: table not present")
                else:
                    print(table_l[t_items-1],"Table not present")
                    continue
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Data points selected and clearing:",clear_point)
            if(clear_point =='all'):
                self.find_element(*ChillerinfoPageLocators.record_data_summary_clrall).click()
                if(self.find_element(*ChillerinfoPageLocators.record_data_summary_empty_msg)==ChillerinfoPageLocators
                        .record_data_summary_empty_msg_txt): print("Cleared all points")
            elif(clear_point =='none'):
                selected_pts = self.find_elements(*ChillerinfoPageLocators.record_data_summary_pts_lst)
                for pts in range(1, len(selected_pts) + 1):
                    disp_path = ChillerinfoPageLocators.record_data_summary_pts_lst[-1] + '[' + str(pts) + ']/div'
                    disp_point_txt = self.find_element('xpath', disp_path).text
                    print(disp_point_txt)

    def record_data_table_sel(self,table_item):
        print('*' * 5, 'Table item selection', '*' * 5)
        print("Table ",table_item,"to be selected")
        table_len = self.find_elements(*ChillerinfoPageLocators.record_data_table_lst)
        for t_items in range(1, len(table_len)):
            table_path = ChillerinfoPageLocators.record_data_table_lst[-1] + '[' + str(t_items) + ']/div/label'
            table_data = self.find_element('xpath', table_path)
            if str(table_item) == str(table_data.text):
                print("Selected table: ",table_data.text)
                table_data.click()
                table_present=1
                break
            else:
                table_present=0
        return table_present

    def record_type_instant(self,record_type,interval='2'):
        print('*'*5,record_type,'*'*5)
        if(self.wait(ChillerinfoPageLocators.record_type_lbl)=='0'):
            print(self.find_element(*ChillerinfoPageLocators.record_type_lbl).text)

        self.find_element(*ChillerinfoPageLocators.record_type_btn).click()
        self.find_elements(*ChillerinfoPageLocators.record_type_loe)
        link = driver.find_element_by_link_text(record_type)
        link.click()
        print("Selected type:", self.find_element(*ChillerinfoPageLocators.record_type_btn).text)
        print(str(self.find_element(*ChillerinfoPageLocators.record_interval_lbl).text))

        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Interval: ",str(self.find_element(
            *ChillerinfoPageLocators.record_interval_input).get_attribute('value')))
        self.find_element(*ChillerinfoPageLocators.record_interval_input).clear()
        self.find_element(*ChillerinfoPageLocators.record_interval_input).send_keys(interval)
        self.find_element(*ChillerinfoPageLocators.record_save_btn).click()
        try:
            if (self.wait(ChillerinfoPageLocators.trace_btn_lbl) == 0):
                print("Config success")
        except:
            if (self.wait(ChillerinfoPageLocators.record_err_msg) == 0):
                err_msg = self.find_element(*ChillerinfoPageLocators.record_err_msg).text
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), err_msg)

    def record_type_time(self,start_date,end_date,action='save_record',interval='2'):
        record_type = 'Time Based'
        print('*'*5, record_type, '*'*5)
        if (self.wait(ChillerinfoPageLocators.record_type_lbl) == '0'):
            print(self.find_element(*ChillerinfoPageLocators.record_type_lbl).text)
        strt_date_d = start_date.split(" ")[0]
        strt_date_l = start_date.split(" ")[1]
        strt_time_hr = strt_date_l.split(":")[0]
        strt_time_min = strt_date_l.split(":")[1]
        strt_time_ampm = strt_date_l.split(":")[2]
        end_date_d = end_date.split(" ")[0]
        end_date_l = end_date.split(" ")[1]
        end_time_hr = end_date_l.split(":")[0]
        end_time_min = end_date_l.split(":")[1]
        end_time_ampm = end_date_l.split(":")[2]
        self.find_element(*ChillerinfoPageLocators.record_type_btn).click()
        self.find_elements(*ChillerinfoPageLocators.record_type_loe)
        link = driver.find_element_by_link_text(record_type)
        link.click()
        print("Selected type:", self.find_element(*ChillerinfoPageLocators.record_type_btn).text)
        print(str(self.find_element(*ChillerinfoPageLocators.record_interval_lbl).text))
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Interval: ", str(self.find_element(
            *ChillerinfoPageLocators.record_interval_input).get_attribute('value')))
        self.find_element(*ChillerinfoPageLocators.record_time_interval_input).clear()
        self.find_element(*ChillerinfoPageLocators.record_time_interval_input).send_keys(interval)
        time.sleep(1.0)
        self.find_element(*ChillerinfoPageLocators.record_strt_date_btn).click()
        #self.find_element(*ChillerinfoPageLocators.record_strt_date_cal_today).click()
        self.date_set(ChillerinfoPageLocators.record_strt_date_cal,strt_date_d)
        time.sleep(1.0)
        print(self.find_element(*ChillerinfoPageLocators.record_strt_date_lbl).text, ": ", self.find_element(
            *ChillerinfoPageLocators.record_strt_date_val).get_attribute('value'))
        self.find_element(*ChillerinfoPageLocators.record_strt_time_hr).clear()
        self.find_element(*ChillerinfoPageLocators.record_strt_time_hr).send_keys(strt_time_hr)
        self.find_element(*ChillerinfoPageLocators.record_strt_time_min).clear()
        self.find_element(*ChillerinfoPageLocators.record_strt_time_min).send_keys(strt_time_min)
        if(strt_time_ampm != str(self.find_element(*ChillerinfoPageLocators.record_strt_time_ampm).text)):
            self.find_element(*ChillerinfoPageLocators.record_strt_time_ampm).click()
        time.sleep(1.0)
        self.find_element(*ChillerinfoPageLocators.record_end_date_btn).click()
        # self.find_element(*ChillerinfoPageLocators.record_end_date_cal_today).click()
        self.date_set(ChillerinfoPageLocators.record_end_date_cal,end_date_d)
        time.sleep(1.0)
        print(self.find_element(*ChillerinfoPageLocators.record_end_date_lbl).text, ": ", self.find_element(
            *ChillerinfoPageLocators.record_end_date_val).get_attribute('value'))
        self.find_element(*ChillerinfoPageLocators.record_end_time_hr).clear()
        self.find_element(*ChillerinfoPageLocators.record_end_time_hr).send_keys(end_time_hr)
        self.find_element(*ChillerinfoPageLocators.record_end_time_min).clear()
        self.find_element(*ChillerinfoPageLocators.record_end_time_min).send_keys(end_time_min)
        if(end_time_ampm != str(self.find_element(*ChillerinfoPageLocators.record_end_time_ampm).text)):
            self.find_element(*ChillerinfoPageLocators.record_end_time_ampm).click()
        if(action =='save_record'):
            self.find_element(*ChillerinfoPageLocators.record_time_save_btn).click()
            try:
                if (self.wait(ChillerinfoPageLocators.trace_btn_lbl) == 0):
                    print("Config success and record in progress")
            except:
                if (self.wait(ChillerinfoPageLocators.record_time_err_msg) == 0):
                    err_msg = self.find_element(*ChillerinfoPageLocators.record_err_msg).text
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), err_msg)
        else:
            self.find_element(*ChillerinfoPageLocators.record_time_exit_btn).click()

    def record_type_trigger(self,strt_trg_point,strt_trg_cond,strt_trg_val,end_trg_point,end_trg_cond,end_trg_val,
                          interval ='2'):
        print('*'*5,'Trigger Based Record','*'*5)
        record_type = "Trigger Based"
        self.find_element(*ChillerinfoPageLocators.record_type_btn).click()
        self.find_elements(*ChillerinfoPageLocators.record_type_loe)
        link = driver.find_element_by_link_text(record_type)
        link.click()
        print("Selected type:", self.find_element(*ChillerinfoPageLocators.record_type_btn).text)
        print(self.find_element(*ChillerinfoPageLocators.trg_strt_lbl).text)
        self.find_element(*ChillerinfoPageLocators.trg_strt_dp_val_btn).click()
        self.find_element(*ChillerinfoPageLocators.trg_strt_dp_val_search).send_keys(strt_trg_point)
        time.sleep(0.5)
        strt_dp = self.find_elements(*ChillerinfoPageLocators.trg_strt_dp_val_lst)
        strt_dp[0].click()
        print(self.find_element(*ChillerinfoPageLocators.trg_strt_dp_lbl).text,  self.find_element(
            *ChillerinfoPageLocators.trg_strt_dp_val_btn).text)
        self.find_element(*ChillerinfoPageLocators.trg_strt_cond_btn).click()
        self.find_elements(*ChillerinfoPageLocators.trg_strt_cond_lst)
        strt_cond = self.driver.find_element_by_link_text(strt_trg_cond)
        strt_cond.click()
        self.find_element(*ChillerinfoPageLocators.trg_strt_val_input).send_keys(strt_trg_val)
        print(self.find_element(*ChillerinfoPageLocators.trg_strt_cond_btn).text, self.find_element(
            *ChillerinfoPageLocators.trg_strt_val_input).get_attribute('value'))
        print('\n',self.find_element(*ChillerinfoPageLocators.trg_end_lbl).text)
        self.find_element(*ChillerinfoPageLocators.trg_end_dp_btn).click()
        if self.find_element(*ChillerinfoPageLocators.trg_end_dp_search).text == "":
            self.find_element(*ChillerinfoPageLocators.trg_end_dp_search).clear()
        self.find_element(*ChillerinfoPageLocators.trg_end_dp_search).send_keys(end_trg_point)
        end_dp=self.find_elements(*ChillerinfoPageLocators.trg_end_dp_val_lst)
        end_dp[0].click()
        print(self.find_element(*ChillerinfoPageLocators.trg_end_dp_lbl).text, self.find_element(
            *ChillerinfoPageLocators.trg_end_dp_btn).text)
        self.find_element(*ChillerinfoPageLocators.trg_end_cond_btn).click()
        self.find_elements(*ChillerinfoPageLocators.trg_end_cond_lst)
        end_cond = self.driver.find_element_by_link_text(end_trg_cond)
        end_cond.click()
        self.find_element(*ChillerinfoPageLocators.trg_end_val_input).send_keys(end_trg_val)
        print(self.find_element(*ChillerinfoPageLocators.trg_end_cond_btn).text,",", self.find_element(
            *ChillerinfoPageLocators.trg_end_val_input).text)
        self.find_element(*ChillerinfoPageLocators.trg_interval_in).send_keys(interval)
        print(self.find_element(*ChillerinfoPageLocators.trg_interval_lbl).text, self.find_element(
            *ChillerinfoPageLocators.trg_interval_in).get_attribute('value'))
        self.find_element(*ChillerinfoPageLocators.trg_save_btn).click()
        try:
            if (self.wait(ChillerinfoPageLocators.trace_btn_lbl) == 0):
                print("Config success")
        except:
            if (self.wait(ChillerinfoPageLocators.record_err_msg) == 0):
                err_msg = self.find_element(*ChillerinfoPageLocators.record_err_msg).text
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), err_msg)

    def record_start(self,action):
        print("***********Trace start/stop********")
        self.wait(ChillerinfoPageLocators.trace_btn)
        if ((self.trace_status() != "Stop Recording") and (action=='start')):
            print(self.find_element(*ChillerinfoPageLocators.trace_btn_lbl).text)
            self.find_element(*ChillerinfoPageLocators.trace_btn).click()
        elif(action=='stop'):
            self.find_element(*ChillerinfoPageLocators.trace_btn).click()
            time.sleep(1.0)
            self.find_element(*ChillerinfoPageLocators.record_stop_prompt_yes).click()
            print('record state:', self.find_element(*ChillerinfoPageLocators.trace_btn_lbl).text)
        elif(self.trace_status() == "Stop Recording") and (action=='start'):
            print("Previous trace job in progress")
            self.find_element(*ChillerinfoPageLocators.trace_btn).click()
            time.sleep(1.0)
            self.find_element(*ChillerinfoPageLocators.record_stop_prompt_yes).click()
            time.sleep(1.0)
            self.find_element(*ChillerinfoPageLocators.trace_btn).click()

    def trace_status(self):
        self.hover(*ChillerinfoPageLocators.record_sts_icon)
        print(self.find_element(*ChillerinfoPageLocators.record_sts_popover_msg).get_attribute('uib-popover'))
        return str(self.find_element(*ChillerinfoPageLocators.trace_btn_lbl).text)

    def trace_history(self,search_item,model_ver,trace_type,job_start='',job_end='',action='Export'):

        self.wait(ChillerinfoPageLocators.trace_history_btn)
        self.find_element(*ChillerinfoPageLocators.trace_history_btn).click()
        if (self.wait(ChillerinfoPageLocators.trace_hist_lbl)==0):
            print('*'*5,self.find_element(*ChillerinfoPageLocators.trace_hist_lbl).text,'*'*5)
            print(self.find_element(*ChillerinfoPageLocators.trace_hist_lbl).text,'\n',\
            "Trace records table header",self.find_element(*ChillerinfoPageLocators.trace_hist_table_header).text)
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Trace History is not present")
            return
        if search_item == 'model-version':
            self.search_key(ChillerinfoPageLocators.trace_hist_search_input, search_item)
            print(search_item, self.find_element(*ChillerinfoPageLocators.trace_reports_search_input).get_attribute(
                'value'))
        elif search_item =='trace_type':
            self.search_key(ChillerinfoPageLocators.trace_hist_search_input, search_item)
            print(search_item, self.find_element(*ChillerinfoPageLocators.trace_reports_search_input).get_attribute(
                'value'))
        search_items = self.find_elements('xpath','//div[@id="content"]/div[1]/div[2]/ng-include/div[1]/div[2]/div['
                                                 '1]/div[2]/*')
        print('list of records:',len(search_items))
        for li in range(1,len(search_items)+1):
            table_list_path = '//*[@id="content"]/div[1]/div[2]/ng-include/div[1]/div[2]/div/div[2]/div['
            print("-"*25,"\n",self.find_element('xpath',table_list_path+str(li)+']').text)
            device_model = self.find_element('xpath',table_list_path+str(li)+']/div[2]').text
            assert (model_ver in device_model),"model-version Assertion failed"
            record_type = self.find_element('xpath',table_list_path+str(li)+']/div[3]').text
            assert (trace_type in record_type),"Trace type assertion failed"
            if action =="stop":
                status = self.find_element('xpath',table_list_path+str(1)+']/div[6]').text
                if(status==ChillerinfoPageLocators.trace_hist_status_recording):
                    self.find_element('xpath',table_list_path+str(li)+']/div[7]/a').click()
                    if self.wait(ChillerinfoPageLocators.trace_hist_stop_record)==0:
                        print(self.find_element(*ChillerinfoPageLocators.trace_hist_stop_record_txt).text)
                        self.find_element(*ChillerinfoPageLocators.trace_hist_stop_record_yes).click()
                else:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status)
            elif action=='Export':
                status = self.find_element('xpath', table_list_path + str(li) + ']/div[6]').text
                if status ==(ChillerinfoPageLocators.trace_hist_status_complete or
                             ChillerinfoPageLocators.trace_hist_status_stop or
                             ChillerinfoPageLocators.trace_hist_status_error):
                    self.find_element('xpath', table_list_path + str(li) + ']/div[7]/a[1]/i').click()
                    if (self.wait(ChillerinfoPageLocators.loader) == 0):
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," Exporting")
                    self.wait(ChillerinfoPageLocators.trace_hist_lbl)
                else:
                    print("Trace record is in progress")
            elif action == 'Delete':
                status = self.find_element('xpath', table_list_path + str(li) + ']/div[6]').text
                if status == ChillerinfoPageLocators.trace_hist_status_complete:
                    self.find_element('xpath', table_list_path + str(li) + ']/div[7]/a[2]/i').click()
                    if(self.wait(ChillerinfoPageLocators.trace_hist_item_delete_title)==0):
                        print(self.find_element(
                        *ChillerinfoPageLocators.trace_hist_item_delete_txt).text)
                        self.find_element(*ChillerinfoPageLocators.trace_hist_item_delete_yes).click()
                        if(self.wait(ChillerinfoPageLocators.loader)==0):
                            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Deleting")
                    self.wait(ChillerinfoPageLocators.trace_hist_lbl)
                else:
                    print("Trace record is in progress")
            time.sleep(65.0)
        self.find_element(*ChillerinfoPageLocators.trace_hist_exit).click()
        self.wait(ChillerinfoPageLocators.trace_btn)

    def trace_report(self,search_item,model_ver,trace_type,job_start='',job_end='',action='Export'):
        self.wait(HomePageLocatars.reports_btn)
        self.find_element(*HomePageLocatars.reports_btn).click()
        time.sleep(1.0)
        self.find_element(*HomePageLocatars.reports_trace_history).click()
        if (self.wait(ChillerinfoPageLocators.trace_reports_lbl) == 0):
            print('*'*10, "Reports",self.find_element(*ChillerinfoPageLocators.trace_reports_lbl).text, '*'*10)
            print(self.find_element(*ChillerinfoPageLocators.trace_reports_lbl).text, '\n', \
                "Trace records table header :\n", self.find_element(
                *ChillerinfoPageLocators.trace_reports_table_header).text)
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Trace History is not present")
            return
        if search_item == 'model-version':
            self.search_key(ChillerinfoPageLocators.trace_reports_search_input, model_ver)
            print(search_item, self.find_element(*ChillerinfoPageLocators.trace_reports_search_input).get_attribute(
                'value'))
        elif search_item =='trace_type':
            self.search_key(ChillerinfoPageLocators.trace_reports_search_input, trace_type)
            print(search_item, self.find_element(*ChillerinfoPageLocators.trace_reports_search_input).get_attribute(
                'value'))
        search_items = self.find_elements('xpath', '//div[@id="trendReport"]/div[9]/ng-include[1]/div[1]/div[2]/div['
                                                   '1]/div[2]/*')
        print('list of records:', len(search_items))
        for li in range(1, len(search_items) + 1):
            table_list_path = '//*[@id="trendReport"]/div[9]/ng-include[1]/div[1]/div[2]/div[1]/div[2]/div['
            print("-" * 25, "\n", self.find_element('xpath', table_list_path + str(li) + ']').text)
            device_model = self.find_element('xpath', table_list_path + str(li) + ']/div[2]').text
            assert (model_ver in device_model), "model-version Assertion failed"
            record_type = self.find_element('xpath', table_list_path + str(li) + ']/div[3]').text
            assert (trace_type in record_type), "Trace type assertion failed"
            if action == "stop":
                status = self.find_element('xpath', table_list_path + str(1) + ']/div[6]').text
                if (status == ChillerinfoPageLocators.trace_reports_status_recording):
                    self.find_element('xpath', table_list_path + str(li) + ']/div[7]/a').click()
                    if self.wait(ChillerinfoPageLocators.trace_reports_stop_record) == 0:
                        print(self.find_element(*ChillerinfoPageLocators.trace_reports_stop_record_txt).text)
                        self.find_element(*ChillerinfoPageLocators.trace_reports_stop_record_yes).click()
                else:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status)
            elif action == 'Export':
                status = self.find_element('xpath', table_list_path + str(li) + ']/div[6]').text
                if status == (ChillerinfoPageLocators.trace_reports_status_complete or
                              ChillerinfoPageLocators.trace_reports_status_stop or
                              ChillerinfoPageLocators.trace_reports_status_error):
                    self.find_element('xpath', table_list_path + str(li) + ']/div[7]/a[1]/i').click()
                    if (self.wait(ChillerinfoPageLocators.loader) == 0):
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), " Exporting")
                    self.wait(ChillerinfoPageLocators.trace_reports_lbl)
                else:
                    print("Trace record is in progress")
            elif action == 'Delete':
                status = self.find_element('xpath', table_list_path + str(li) + ']/div[6]').text
                if status == ChillerinfoPageLocators.trace_reports_status_complete:
                    self.find_element('xpath', table_list_path + str(li) + ']/div[7]/a[2]/i').click()
                    if (self.wait(ChillerinfoPageLocators.trace_reports_item_delete_title) == 0):
                        print(self.find_element(
                            *ChillerinfoPageLocators.trace_reports_item_delete_txt).text)
                        self.find_element(*ChillerinfoPageLocators.trace_reports_item_delete_yes).click()
                        if (self.wait(ChillerinfoPageLocators.loader) == 0):
                            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Deleting")
                    self.wait(ChillerinfoPageLocators.trace_reports_lbl)
                else:
                    print("Trace record is in progress")
            time.sleep(65.0)


    def date_set(self,element,date_sel):
        print('*'*5,'Date Setting','*'*5)
        date_m = ChillerinfoPageLocators.month_name[(int(date_sel.split("/")[0]))-1]
        date_d = date_sel.split("/")[1]
        date_y = date_sel.split("/")[2]
        print('Month/year:',date_m,'Day:',date_d,'Year:',date_y)
        # year pick
        month_path = element[-1]+'/li[1]/div/table/thead/tr/th[2]/button'
        self.find_element('xpath',month_path).click()
        time.sleep(1.0)
        year_path =element[-1]+'/li[1]/div/table/thead/tr/th[2]/button'
        self.find_element('xpath',year_path).click()
        for y in range(1, 5):
            for z in range(1, 6):
                path = element[-1] + '/li[1]/div/table/tbody/tr[' + str(y) + ']/td[' + str(z) + ']'
                yr_pick = self.find_elements('xpath', path)
                if (str(date_y[2:]) == str(yr_pick[0].text)):
                    yr_pick[0].click()

                    break
            else:      continue
            break
        # month pick
        time.sleep(1.0)
        for m in range(1,5):
            for n in range(1,4):
                path = element[-1] + '/li[1]/div/table/tbody/tr['+str(m)+']/td['+str(n)+']'
                mon_pick = self.find_elements('xpath',path)
                if(str(date_m) == str(mon_pick[0].text)):
                    mon_pick[0].click()
                    break
            else:
                continue
            break

        time.sleep(2.0)
        #date pick
        for i in range(1,7):
            for d in range (2,9):
                path = element[-1] + '/li[1]/div/table/tbody/tr['+str(i)+']/td['+str(d)+']'
                date_pick = self.find_elements('xpath',path)
                if str(date_d) ==str(date_pick[0].text):
                    date_pick[0].click()
                    break
            else:
                continue
            break
    def search_key(self,element,data_point):
        print("*****Search******** ",data_point)
        self.wait(element)
        self.find_element(*element).send_keys(data_point)
        time.sleep(1.0)
        search_key = str(self.find_element(*element).get_attribute("value"))
        if search_key != data_point:
            self.find_element(*element).clear()
            print(datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"), ":", "DATA POINT is not entered in search field", search_key)
            self.find_element(*element).send_keys(data_point)
