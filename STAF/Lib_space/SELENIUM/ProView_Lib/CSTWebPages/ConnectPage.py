import os
import sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)

# from webcolors
from Lib_Space.Selenium_Lib.BaseClass import Page
from Lib_Space.Selenium_Lib.Page_locators.ConnectPage_locators import ConnectPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
import datetime
driver = object
delay = 40


class ConnectPage(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(ConnectPage, self).__init__(webdriver)
        driver = webdriver

    def wait_until_element(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element[-1])))
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"page is ready!!")
            return 0
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Loading took too much time!")
            filename1 = "Connectpage"
            self.screen_capture(filename1)
            return 1

    def wait_until_visible(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, element[-1])))
        except TimeoutException:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Loading took too much time!")

    def enter_page(self, webdriver, Connection='CCN'):
        global driver
        driver = webdriver
        self.driver.refresh()
        time.sleep(5.0)
        self.wait_until_visible(ConnectPageLocators.connection_ccn)
        if Connection == 'CCN':
            self.find_element(*ConnectPageLocators.connection_ccn).click()
            self.wait_until_visible(ConnectPageLocators.connect_ccn_title)
        elif Connection == 'BACnet':
            self.find_element(*ConnectPageLocators.connection_bacnet).click()
            try:
                self.wait_until_visible(ConnectPageLocators.connect_bacnet_title)
                print("Connectivity page loaded")
            except:
                if (self.wait_until_element(ConnectPageLocators.bacnet_nodevice_dialog_title) == 0):
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Error",\
                          self.find_element(*ConnectPageLocators.bacnet_nodevice_dialog_title).text)
                    self.find_element(*ConnectPageLocators.bacnet_nodevice_dialog_ok_btn).click()
        return 0

    # Click on Add-> edit name,bus, element,buad, ipadr, type and check in ccn list
    # ccn_name, conn_type, bus = '0', ele = '240', baud = '38400', ip_addr = '192.168.168.100';;CCN_Name, Type, Bus, Element, Baud, IP_Addr
    def add_CCNID(self, Data):
        self.find_element(*ConnectPageLocators.add_ccnid_btn).click()
        self.wait_until_element(ConnectPageLocators.ccnid_name_lbl)
        self.find_element(*ConnectPageLocators.ccnid_name_input).send_keys(Data['CCN_Name'])
        # Check for unique name error
        try:
            if self.find_element('xpath','//*[@id="content"]/div/div[10]/div[1]/div/div/div[6]/form/fieldset[1]/div[2]/div').is_displayed():
                print (self.find_element('xpath','//*[@id="content"]/div/div[10]/div[1]/div/div/div[6]/form/fieldset[1]/div[2]/div').text)
                return -1
        except:
            print ("No error found")
        self.select_ccntype(Data)
        if Data['conn_Type'] == 'USB':
            self.find_element(*ConnectPageLocators.ccnid_bus_input).clear()
            self.find_element(*ConnectPageLocators.ccnid_elem_usb_input).clear()
            self.find_element(*ConnectPageLocators.ccnid_bus_input).send_keys(Data['Bus'])
            self.find_element(*ConnectPageLocators.ccnid_elem_usb_input).send_keys(Data['Element'])
            self.select_baudrate(Data)
        if Data['conn_Type'] == 'LAN':
            self.find_element(*ConnectPageLocators.ccnid_elem_lan_input).clear()
            self.find_element(*ConnectPageLocators.ccnid_elem_lan_input).send_keys(Data['Element'])
            self.set_CCN_IP(Data)
        else:
            pass
        self.find_element(*ConnectPageLocators.ccnid_save_btn).click()
        self.ccnid_search_list(Data)
        return 0

    def configure_CCNID(self, Data):
        if self.find_element(*ConnectPageLocators.configure_ccnid_btn).is_displayed():
            self.find_element(*ConnectPageLocators.configure_ccnid_btn).click()
        self.wait_until_element(ConnectPageLocators.ccnid_name_lbl)
        if Data['CCN_Name'] !="":
            self.find_element(*ConnectPageLocators.ccnid_name_input).send_keys(Data['CCN_Name'])
        if Data['conn_Type'] !="":
            self.select_ccntype(Data)
        if Data['conn_Type'] == 'USB':
            if Data['Bus'] !="":
                self.find_element(*ConnectPageLocators.ccnid_bus_input).clear()
                self.find_element(*ConnectPageLocators.ccnid_bus_input).send_keys(Data['Bus'])
            if Data['Element'] != "":
                self.find_element(*ConnectPageLocators.ccnid_elem_usb_input).clear()
                self.find_element(*ConnectPageLocators.ccnid_elem_usb_input).send_keys(Data['Element'])
            if Data['Baud'] != "":
                self.select_baudrate(Data)
        if Data['conn_Type'] == 'LAN':
            if Data['Element'] != "":
                self.find_element(*ConnectPageLocators.ccnid_elem_lan_input).clear()
                self.find_element(*ConnectPageLocators.ccnid_elem_lan_input).send_keys(Data['Element'])
            if Data['IP_Addr'] != "":
                self.set_CCN_IP(Data)
        else:
            pass
        self.find_element(*ConnectPageLocators.ccnid_save_btn).click()

    def delete_ccnid(self,Data):
        print("*"*5,"CCN Delete","*"*5)
    # search ccnid ->select CCN id -> click delete
        self.select_ccnid(Data)
        self.find_element(*ConnectPageLocators.ccnid_delete_btn).click()
        self.wait_until_element(ConnectPageLocators.ccnid_delete_msg)

        if self.find_element(*ConnectPageLocators.ccnid_delete_err).is_displayed:
            print(self.find_element(*ConnectPageLocators.ccnid_delete_err).text)
            self.find_element(*ConnectPageLocators.ccnid_delete_err_close).click()
            return 1
        self.find_element(*ConnectPageLocators.ccnid_delete_yes).click()
        time.sleep(2)
        self.ccnid_search_cnt(Data)


    def launch_device_manager(self, Data):
        print('*' * 5, 'Launch Device Manager', '*' * 5)
        self.select_ccnid(Data)
        try:
            if Data['DM_load_type'] == "DM_button":
                self.find_element (*ConnectPageLocators.device_manager_btn).click()
                self.wait_until_element(ConnectPageLocators.connect_message)
            elif Data['DM_load_type']=='Double-click':
                ccn_table_name = self.find_element('xpath', ConnectPageLocators.ccn_tbl[-1] + '[1]/td[1]')
                ActionChains(self.driver).double_click(ccn_table_name).perform()
                # ccn_list = self.find_elements(*ConnectPageLocators.ccn_tbl)

        except Exception as e:
             print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Launch DM failed.Exception occured.",e)

    def launch_trace(self, Data):
        print('*' * 5, 'Launch Device Manager', '*' * 5)
        try:
            self.find_element (*ConnectPageLocators.device_manager_btn).click()
            self.wait_until_element(*ConnectPageLocators.connect_message)
        except:
         print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Launch Trace failed.Exception occured.")

    def launch_network_monitor(self):
        print('*' * 5, 'Launch Device Manager', '*' * 5)
        self.find_element(*ConnectPageLocators.network_monitor_btn).click()

    def connect_ccn(self,Data,disconnect_ccn ='yes'):
        print('*' * 5, "Connect CCN", '*' * 5)
        print ('Connecting to CCN ',Data['CCN_Name'])
        # self.find_element(*ConnectPageLocators.ccnid_search_input).send_keys(Data['CCN_Name'])
        ccn_list  = self.find_elements(*ConnectPageLocators.ccn_tbl)
        for ccn_cnt in range(len(ccn_list)):
            ccn_table_name = self.find_elements('xpath',
                                               ConnectPageLocators.ccn_tbl[-1] + '[' + str(ccn_cnt + 1) + ']/td')
            if self.find_element('xpath',ConnectPageLocators.ccn_tbl[-1] + '[' + str(ccn_cnt+1) +']/td[1]').text == Data['CCN_Name']:
                ccn_table_name[ccn_cnt].click()
            else:
                print(" CCN is not selected")
                return -1
        if self.find_element(*ConnectPageLocators.ccn_connect_btn).is_enabled():
            self.find_element(*ConnectPageLocators.ccn_connect_btn).click()
            try:
                if self.wait_until_visible(ConnectPageLocators.ccn_connect_override_dialog):
                    print(self.find_element(*ConnectPageLocators.ccn_connect_override_dialog).text)
                    self.find_element(*ConnectPageLocators.ccn_connect_override_yes_btn).click()
                    if self.find_element(*ConnectPageLocators.ccn_msg_txt):
                        print("override connect Status: ", self.find_element(*ConnectPageLocators.connect_message).text)
                else:
                    self.find_element(*ConnectPageLocators.ccn_connect_btn).click()

            except Exception as e:
                print(e)
            else:
                if self.find_element(*ConnectPageLocators.ccn_disconnect_btn).is_enabled():
                    print("Succesfully connected")

        else:
            print("Already connected to CCN")
        for ccn_cnt in range(0, len(ccn_list)):
            if self.find_element('xpath',ConnectPageLocators.ccn_tbl[-1] + '[' + str(ccn_cnt+1) + ']/td[1]').text == Data['CCN_Name']:
                ele_color = self.find_element('xpath', ConnectPageLocators.ccn_tbl[-1] + '[' + str(ccn_cnt + 1) + ']/td').value_of_css_property('background-color')
                print (ele_color)

        print("\nConnection Status", self.find_element('xpath',ConnectPageLocators.ccn_conn_status_btn[-1][:-6]).get_attribute('title'))
        self.find_element(*ConnectPageLocators.ccn_conn_status_btn).click()
        time.sleep(2)
        print("\nconnection details:",self.find_element(*ConnectPageLocators.ccn_conn_status_txt).text)
        self.find_element(*ConnectPageLocators.ccn_conn_status_btn).click()

    def disconnect_ccn(self):
        print ('*'*5,"Disconnect CCN",'*'*5)
        self.find_element(*ConnectPageLocators.ccn_disconnect_btn).click()
        self.wait_until_element(*ConnectPageLocators.loader_txt)
        if self.find_element(*ConnectPageLocators.ccn_connect_btn).is_displayed():
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'CCN disconnect success')
        else:
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'CCN disconnect failed')
        print ("\nConnection Status", self.find_element(*ConnectPageLocators.ccn_conn_status_btn).text)

    def select_ccntype(self, Data):
        print('*' * 5, 'CCN Type', '*' * 5)
        conn_type=Data['conn_Type']
        self.find_element(*ConnectPageLocators.ccnid_type_btn).click()
        element = self.find_elements(*ConnectPageLocators.ccnid_type_loe)
        # element[1].click()
        if 'USB' == conn_type:
            self.find_element(*ConnectPageLocators.ccnid_type_usb).click()
        if 'LAN' == conn_type:
            self.find_element(*ConnectPageLocators.ccnid_type_lan).click()
        if 'db' == conn_type:
            self.find_element(*ConnectPageLocators.ccnid_type_db).click()

    def set_CCN_IP(self,Data):
        print('Setting CCN IP address')
        Ip_addr= Data['IP_Addr'].split('.')
        self.find_element(*ConnectPageLocators.ccnid_ip_addr1).send_keys(Ip_addr[0])
        self.find_element(*ConnectPageLocators.ccnid_ip_addr2).send_keys(Ip_addr[1])
        self.find_element(*ConnectPageLocators.ccnid_ip_addr3).send_keys(Ip_addr[2])
        self.find_element(*ConnectPageLocators.ccnid_ip_addr4).send_keys(Ip_addr[3])

    def ccnid_search_cnt(self,Data):
        print('*' * 5, 'CCNID Search', '*' * 5)
        self.find_element(*ConnectPageLocators.ccnid_search_input).clear()
        search_data = str(Data['CCN_Name'])
        print(search_data)
        self.find_element(*ConnectPageLocators.ccnid_search_input).send_keys(search_data)

        ccn_list = self.find_elements(*ConnectPageLocators.ccn_tbl)
        for ccn_cnt in range(1, len(ccn_list)):
            ccn_name= self.find_element('xpath',ConnectPageLocators.ccn_tbl[-1] + '[' + str(ccn_cnt) + ']/td[1]').text
            if ccn_name == Data['CCN_Name']:
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":"," CCN Name:", ccn_name)
                return ccn_cnt
            else:
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),":", " CCN Name", Data['CCN_Name'],
                      "is not found in list")
                return 0

    def ccnid_list(self):
        print ('*'*5,'CCNID LIST','*'*5,'\n')
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.find_element(*ConnectPageLocators.ccn_tbl_header).text)
        ccn_name = []
        ccn_list = self.find_elements(*ConnectPageLocators.ccn_tbl)
        for ccn_cnt in range(len(ccn_list)):
            print(ccn_cnt, self.find_element('xpath',ConnectPageLocators.ccn_tbl[-1] + '[' + str(ccn_cnt+1) + ']/td[1]').text)

            ccn_name.insert(ccn_cnt, self.find_element('xpath',ConnectPageLocators.ccn_tbl[-1] + '[' + str(ccn_cnt+1) + ']/td[1]').text)

        return ccn_name
    def select_ccnid(self, Data):
        print("*"*5,"Select CCN ID ","*"*5)
        ccn_no= self.ccnid_search_list(Data)
        ccn_list = self.find_elements(*ConnectPageLocators.ccn_tbl)
        try:
            for ccn_cnt in range(len(ccn_list)):
                ccn_table_name = self.find_element('xpath',ConnectPageLocators.ccn_tbl[-1] + '[' + str(ccn_cnt+1) + ']/td[1]')
                if ccn_table_name.text == Data['CCN_Name']:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ccn_cnt, ccn_table_name.text)
                    ccn_table_name.click()
                    return
                    # if Data['DM_load_type']=='Double-click':
                    #     ActionChains(self.driver).double_click(ccn_table_name).perform()
                    #     self.wait_until_element(ConnectPageLocators.ccn_conn_prmpt_dialog)
                    #     if Data['DM_launch_mode'] == 'online':
                    #         self.find_element(*ConnectPageLocators.ccn_conn_yes_btn).click()
                    #     elif Data['DM_launch_mode'] == 'offline':
                    #         self.find_element(*ConnectPageLocators.ccn_conn_no_btn).click()
                    #     else:
                    #         self.find_element(*ConnectPageLocators.ccn_conn_cancel_btn).click()
                    # else:
                    #     ccn_table_name.click()
                else:
                    self.add_CCNID(Data)
        except Exception as error:
            print("Error: ",error)
    def app_launch_mode(self,launch_mode):
        print("*"*5,"App launch mode","*"*5)
        try:
            self.wait_until_visible(ConnectPageLocators.ccn_conn_prmpt_dialog)
            if launch_mode == 'online':
                self.find_element(*ConnectPageLocators.ccn_conn_yes_btn).click()
                print("CCN connection prompt dialog selected 'yes' button")
                try:
                    print("Checking whether other CCN is connected")
                    if self.wait_until_visible(ConnectPageLocators.ccn_connect_override_dialog):
                        print("Override CCN connection dialog visible")
                        print(self.find_element(*ConnectPageLocators.ccn_connect_override_dialog).text)
                        self.find_element(*ConnectPageLocators.ccn_connect_override_yes_btn).click()
                except Exception as e:
                    print("Override message not found ", e)

            elif launch_mode == 'offline':
                self.find_element(*ConnectPageLocators.ccn_conn_no_btn).click()
            else:
                self.find_element(*ConnectPageLocators.ccn_conn_cancel_btn).click()
        except Exception as e:
            print(f'App launch mode failed: {e}')
        time.sleep(5)
    def ccnid_search_list(self, Data):
        node_list=[]
        self.find_element(*ConnectPageLocators.ccnid_search_input).clear()
        self.find_element(*ConnectPageLocators.ccnid_search_input).send_keys(Data['CCN_Name'])
        ccn_list = self.find_elements(*ConnectPageLocators.ccn_tbl)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.find_element(*ConnectPageLocators.ccn_tbl_header).text)
        for ccn_cnt in range(len(ccn_list)):
            node_list.insert (ccn_cnt,self.find_element('xpath', ConnectPageLocators.ccn_tbl[-1] + '[' + str(ccn_cnt+1) + ']/td[1]').text)
            print(ccn_cnt,node_list[ccn_cnt] )
        return node_list
    def ccn_importexport(self,Data,type):
        print ('*'*5,'CCN export','*'*5)
        try:
            if type =='export':
                self.select_ccnid(Data)
                fp = Data['folder_path']
                self.find_element(*ConnectPageLocators.ccn_export_btn).click()
            else:
                self.find_element(*ConnectPageLocators.ccn_import_btn).click()
                fp = Data['folder_path']+'\\'+Data['CCN_Name']

            self.wait_until_visible(ConnectPageLocators.ccn_export_path)
            self.find_element(*ConnectPageLocators.ccn_export_path).clear()
            self.find_element(*ConnectPageLocators.ccn_export_path).send_keys(fp)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," Folder path selected as : ",self.find_element(*ConnectPageLocators.ccn_export_path).get_attribute('value'))
            if Data['oper']=='yes':
                self.find_element(*ConnectPageLocators.ccn_export_path_yes_btn).click()
                if self.wait_until_element(ConnectPageLocators.ccn_msg_txt)==0:
                    print("path error:",self.find_element(*ConnectPageLocators.ccn_msg_txt).text)
            else:
                self.find_element(*ConnectPageLocators.ccn_export_path_no_btn).click()

            if type == 'import':
                try:
                    if self.wait_until_element(ConnectPageLocators.ccnid_name_error)==0:
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Imported CCN Name :",self.find_element(*ConnectPageLocators.ccnid_name_input).get_attribute('value'))
                        self.find_element(*ConnectPageLocators.ccnid_name_input).send_keys(' 1')
                        new_ccn= self.find_element(*ConnectPageLocators.ccnid_name_input).get_attribute('value')
                    else:
                        new_ccn=self.find_element(*ConnectPageLocators.ccnid_name_input).get_attribute('value')
                except Exception as error:
                    print("import error",error)
                self.find_element(*ConnectPageLocators.ccnid_save_btn).click()
            self.wait_until_visible(ConnectPageLocators.loader_txt)
            if self.wait_until_element(ConnectPageLocators.ccn_msg_txt)==0:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Import/Export status: ", self.find_element(*ConnectPageLocators.ccn_msg_txt).text)
            return new_ccn
        except Exception as error:
            print("CCN Import/Export error :", error)


    def bacnet_device_scan(self):
        print('*' * 5, 'BACnet Device scan', '*' * 5)
        time.sleep(10.0)
        device_list=[]
        self.wait_until_element(ConnectPageLocators.bacnet_device_scan_btn)
        self.find_element(*ConnectPageLocators.bacnet_device_scan_btn).click()
        self.wait_until_element(ConnectPageLocators.bacnet_device_tbl)
        try:
            ele =self.find_elements(*ConnectPageLocators.bacnet_device_tbl)
            if len(ele) != 0:
                for lst in range (0, len(ele)):
                    path = ConnectPageLocators.bacnet_device_tbl[-1]
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),lst,self.find_element('xpath',path +'['+str(lst+1)+']').text)
                    device_list.insert(lst-1,str(self.find_element('xpath',path +'['+str(lst+1)+']/td[2]').text))
        except:
            if (self.wait_until_element(ConnectPageLocators.bacnet_nodevice_dialog_title) ==0):
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Error",self.find_element(*ConnectPageLocators.bacnet_nodevice_dialog_title).text)
                self.find_element(*ConnectPageLocators.bacnet_nodevice_dialog_ok_btn).click()
        time.sleep(5.0)
        print ("Scan success",device_list)
        return device_list

    def bacnet_connect(self,Data,conn_type =1):
        print('*' * 5, 'BACnet Device Connect', '*' * 5)
        print('BACnet Device IP', Data['BACnet_IP'],'\t Device Id ',Data['Device_Id'])
        self.wait_until_element(ConnectPageLocators.bacnet_connect_btn)
        if conn_type:
            list = self.bacnet_device_scan()
            ele = self.find_elements(*ConnectPageLocators.bacnet_device_tbl)

            for item in range(len(ele)):
                path = ConnectPageLocators.bacnet_device_tbl[-1]
                device = self.find_element('xpath', path + '[' + str(item + 1) + ']/td[3]')
                if device.text == Data['Device_Id']:
                    device.click()
                    time.sleep(2.0)
                    break
                else:
                    continue
        else:
            self.find_element(*ConnectPageLocators.bacnet_ip_txt).clear()
            self.find_element(*ConnectPageLocators.bacnet_ip_txt).send_keys(Data['BACnet_IP'])
            self.find_element(*ConnectPageLocators.bacnet_id_txt).clear()
            self.find_element(*ConnectPageLocators.bacnet_id_txt).send_keys(Data['Device_Id'])
        print ('Connecting with :', 'IP Addr: ', self.find_element(*ConnectPageLocators.bacnet_ip_txt).get_attribute('value'),'\t Device Id:',self.find_element(*ConnectPageLocators.bacnet_id_txt).get_attribute('value'))
        self.find_element(*ConnectPageLocators.bacnet_connect_btn).click()
        try:
            if self.wait_until_element(ConnectPageLocators.bacnet_object_view_lbl)==0:

                self.find_element(*ConnectPageLocators.bacnet_conn_status).click()
                time.sleep(0.5)
                print(self.find_element(*ConnectPageLocators.bacnet_conn_status_text).text)
                self.find_element(*ConnectPageLocators.bacnet_conn_status).click()
                print("Connected to device")
            elif self.wait_until_element(ConnectPageLocators.loader_txt)==0:
                while (self.find_element(*ConnectPageLocators.loader_txt).text).is_displayed():
                    print (self.find_element(*ConnectPageLocators.loader_txt).text)
                    time.sleep(2.0)
        except:
            if (self.wait_until_element(ConnectPageLocators.bacnet_nodevice_dialog_title) ==0):
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Error",self.find_element(*ConnectPageLocators.bacnet_nodevice_dialog_title).text)

    def bacnet_disconnect(self):
        print('*' * 5, 'BACnet Device Disconnect', '*' * 5)

        self.find_element(*ConnectPageLocators.bacnet_connect_side_btn).click()
        time.sleep(2)
        try:
            self.wait_until_element(ConnectPageLocators.bacnet_disconnect_btn)
            self.find_element(*ConnectPageLocators.bacnet_disconnect_btn).click()
            if self.find_element(*ConnectPageLocators.bacnet_connect_btn).is_displayed() :
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "device Disconnect success")
            else:
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "device Disconnect failed")
        except:
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "device disconnect button not found")

    def select_baudrate(self, Data):
        baud =Data['Baud']
        self.find_element(*ConnectPageLocators.baudrate_btn).click()
        element = self.find_elements(*ConnectPageLocators.baudrate_LOE)
        # element[1].click()
        if '9600' == baud:
            self.find_element(*ConnectPageLocators.baud_9600).click()
        if '19200' == baud:
            self.find_element(*ConnectPageLocators.baud_19200).click()
        if '38400' == baud:
            self.find_element(*ConnectPageLocators.baud_38400).click()
