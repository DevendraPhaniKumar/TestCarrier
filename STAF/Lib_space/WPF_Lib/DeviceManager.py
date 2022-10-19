import os
import sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print('It is: '+dirnameutils)
sys.path.append(dirnameutils + "\\Lib_Space")
sys.path.append(dirnameutils + "\\Lib_Space\\WPF_Lib")
from Lib_space.Selenium_Lib.Page_locators.HomePage_locatars import HomePageLocatars
from Lib_space.WPF_Lib import Methods_framework
from Lib_space.WinOper_Lib.Windowsapp_oper import WindowApp
import time


class DeviceManager_fun():

    # global application_id

    def __init__(self, ccnid,controller_name=None):
        self.controller_name = controller_name
        self.ccnid = ccnid
        self.application_id= str("ProView - "+str(self.ccnid))
        print("application id: ", self.application_id)
        # app=WindowApp()
        # app.app_maximize(self.application_id)
        # Methods_framework.show_app(self.application_id)


    def Addcontroller(self, controllername, description, bus, element,add_mode, dm_title):
        Methods_framework.click("testCCN", "Text", "title", self.application_id)
        Methods_framework.click("btnAddControl", "Button", "AutomationID", self.application_id)
        Methods_framework.Settext("txtName", "Edit", "AutomationID", self.application_id, controllername)
        Methods_framework.Settext("txtDescription", "Edit", "AutomationID",
                                                self.application_id, description)

        Methods_framework.Keyboardactions("{TAB}")
        # Methods_framework.click("0", "edit", "title", self.application_id)
        Methods_framework.Settext("0", "edit", "title", self.application_id, bus)

        Methods_framework.Keyboardactions("{TAB}")
        # Methods_framework.click("1", "edit", "title", self.application_id)
        Methods_framework.Settext("1", "edit", "title", self.application_id, element)
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.click("btnOK", "Button", "AutomationID", self.application_id)
        Methods_framework.click("2", "Button", "AutomationID", self.application_id)
        Methods_framework.wait("3")

    def ConnectCCN(self):
        Methods_framework.click(self.ccnid, "Text", "Title",self.application_id)
        Methods_framework.click("btnConnect", "Button", "AutomationID", self.application_id)
        time.sleep(2)

    def DisConnectCCN(self):
        Methods_framework.click(self.ccnid, "Text", "Title",self.application_id)# self.application_id)
        Methods_framework.click("btnDisconnect", "Button", "AutomationID", self.application_id)#self.application_id)


    def readData(self,ccn_name,controllername, address, tablegroup, tablename, data, input_cond=None):
        Methods_framework.click(ccn_name, "Text", "Title", self.application_id)
        Methods_framework.click(controllername, "Text", "title", self.application_id)
        Methods_framework.Doubleclick(address, "Text", "TITLE",
                                                    self.application_id)
        Methods_framework.wait('3')
        Methods_framework.Doubleclick(tablegroup, "Text", "TITLE", self.application_id)
        Methods_framework.Doubleclick(tablename, "Text", "TITLE", self.application_id)
        Methods_framework.readingtable(data, "DataGrid", "AUTOMATIONID",self.application_id, input_cond=input_cond)
    
    def readData1(self):
        Methods_framework.Doubleclick("30XV_PIC: 30XV - 0, 1", "Text", "Title",
                                                    self.application_id)
        Methods_framework.wait('3')
        Methods_framework.Doubleclick("Status", "Text", "TITLE", self.application_id)
        Methods_framework.Doubleclick("TEMP", "Text", "TITLE",
                                                    self.application_id)
        Methods_framework.wait('3')
        Methods_framework.readingtable("PointsTable", "DataGrid", "AUTOMATIONID",self.application_id, input_cond=["OAT"])
    
    def Importcont(self,level, file_name,option_sel,single=0):
        if level=="CCN":Methods_framework.click("test CCN","Text","Title",self.application_id)
        else:Methods_framework.click("BUS 0","Text","Title",self.application_id)
        Methods_framework.click("btnImportConfiguration","Button","AUTOMATIONID",self.application_id)
        Methods_framework.wait(3)
        #Methods_framework.LocatorAccess()
        Methods_framework.send_keys(str(f'{file_name}'))
        Methods_framework.Keyboardactions("{TAB}")
       # Methods_framework.Doubleclicksubfolder("B000C001.cwx","Text","Title",'Open')
        Methods_framework.doubleclickondialougbox("7", "automationid", "button",
                                                                    self.application_id)
        Methods_framework.Keyboardactions("{TAB}")
        if single:
            Methods_framework.Keyboardactions("{ENTER}")
            Methods_framework.wait(3)
        else:
            if option_sel.upper() == "YES":
                Methods_framework.Doubleclick("Yes", "Button", "title",
                                                                self.application_id)
                Methods_framework.wait(5)
                Methods_framework.Doubleclick("Yes", "Button", "title",
                                                                self.application_id)
                Methods_framework.wait(5)
            if option_sel.upper() == "ALL":
                Methods_framework.Doubleclick("Yes to All", "Button", "title",
                                                                self.application_id)
                Methods_framework.wait(5)
            if option_sel.upper() == "NO":
                Methods_framework.Doubleclick("No", "Button", "title",
                                                                self.application_id)
            if option_sel.upper() == "CANCEL":
                Methods_framework.Doubleclick("Cancel", "Button", "title",
                                                                self.application_id)
    
        return
        #Methods_framework.closeapp()
    
    def Importbus(self):
        Methods_framework.click("BUS 0","Text","Title",self.application_id)
        #Methods_framework.wait(5)
        Methods_framework.click("btnImportConfiguration","Button","AUTOMATIONID",self.application_id)
        Methods_framework.wait(3)
        #Methods_framework.LocatorAccess()
        Methods_framework.send_keys("B000C001.cwx")
        time.sleep(1)
        Methods_framework.Keyboardactions("{TAB}")

        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{ENTER}")
        Methods_framework.wait(3)
        Methods_framework.Keyboardactions("{SPACE}")
        Methods_framework.wait(5)
        # Methods_framework.closeapp()
    
    
    def prop(self):
        Methods_framework.Doubleclick("test CCN", "Text", "Title", self.application_id)
        Methods_framework.wait(3)
        Methods_framework.click("btnProperties", "Button", "Automationid",
                                                  self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.send_keys("1")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.send_keys("241")
    
        Methods_framework.wait(3)
        Methods_framework.click("Cancel", "Button", "Title",
                                                  self.application_id)
    
    def unittypechange(self):
        Methods_framework.click("Options", "Text", "Title", self.application_id)
        Methods_framework.wait(3)
        Methods_framework.click("_Metric", "Text", "Title", self.application_id)

    def Export(self,controller_name):
        Methods_framework.Doubleclick("test CCN", "Text", "Title", self.application_id)

        Methods_framework.click(controller_name, "Text", "title", str(self.application_id))
        Methods_framework.Doubleclick(controller_name, "Text", "TITLE", str(self.application_id))
        Methods_framework.wait(3)
        Methods_framework.click("btnExportConfiguration", "Button", "Automationid",
                                                  self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Keyboardactions("{ENTER}")
        Methods_framework.wait(3)
        # Methods_framework.click("Yes to All", "Text", "Title", self.application_id)
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{ENTER}")

    def Forcewrite(self):
        Methods_framework.Screenshot('userdefined')
        Methods_framework.Readcaption("19PIC6: Carrier SmartView - 0, 2", "Text", "Title",
                                                        self.application_id)
        Methods_framework.wait('3')
    
        Methods_framework.Doubleclick("19PIC6: Carrier SmartView - 0, 2", "Text", "TITLE",
                                                        self.application_id)
        Methods_framework.wait("3")
        Methods_framework.Doubleclick("Status", "Text", "TITLE", self.application_id)
        Methods_framework.Doubleclick("GENUNIT", "Text", "TITLE", self.application_id)
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.send_keys("Network")
        Methods_framework.Keyboardactions("{ENTER}")
        Methods_framework.doubleclickondialougbox('Network:Cmd Start/Stop', "Text", "Title",
                                                                    self.application_id)
        Methods_framework.click("Enable", "Text", "TITLE", self.application_id)
        Methods_framework.click("Force", "Text", "TITLE", self.application_id)
    
    def Addresssearch(self, Data):
        Methods_framework.Doubleclick("19PIC6: Carrier SmartView - 0, 2", "Text", "TITLE",self.application_id)
        Methods_framework.click("btnAddressSearch", "Button", "Automationid",self.application_id)
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{ENTER}")
    
    def alarm_history_export(self,controller_name):
        Methods_framework.Doubleclick(controller_name, "Text", "Title", self.application_id)
        Methods_framework.wait("3")
        Methods_framework.Doubleclick("btnAlarmHistory", "Button", "AutomationID",self.application_id)
        Methods_framework.wait("30")
        Methods_framework.Doubleclick("btnExport", "Button", "AutomationID", self.application_id)
        Methods_framework.wait("3")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{ENTER}")
        Methods_framework.wait("5")
    
    def export_controller_ccn(self,option):
        Methods_framework.click("test CCN", "Text", "title", self.application_id)
        Methods_framework.click("btnExportConfiguration", "Button", "AutomationID", self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Keyboardactions("{ENTER}")
        if option.upper() == "YES":
            Methods_framework.Doubleclick("Yes", "Button", "title",self.application_id)
            Methods_framework.wait(5)
            Methods_framework.Doubleclick("Yes", "Button", "title",  self.application_id)
            Methods_framework.wait(5)
        if option.upper() == "ALL":
            Methods_framework.Doubleclick("Yes to All", "Button", "title", self.application_id)
            Methods_framework.wait(5)
        if option.upper() == "NO":
            Methods_framework.Doubleclick("No", "Button", "title", self.application_id)
        if option.upper() == "CANCEL":
            Methods_framework.Doubleclick("Cancel", "Button", "title", self.application_id)
    
    
    def export_controller_bus(self,option):
        Methods_framework.click("BUS 0", "Text", "title", self.application_id)
        Methods_framework.click("btnExportConfiguration", "Button", "AutomationID",self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Keyboardactions("{ENTER}")
        if option.upper() == "YES":
            Methods_framework.Doubleclick("Yes", "Button", "title",   self.application_id)
            Methods_framework.wait(5)
            Methods_framework.Doubleclick("Yes", "Button", "title",
                                                            self.application_id)
            Methods_framework.wait(5)
        if option.upper() == "ALL":
            Methods_framework.Doubleclick("Yes to All", "Button", "title",
                                                            self.application_id)
            Methods_framework.wait(5)
        if option.upper() == "NO":
            Methods_framework.Doubleclick("No", "Button", "title",
                                                            self.application_id)
        if option.upper() == "CANCEL":
            Methods_framework.Doubleclick("Cancel", "Button", "title",
                                                            self.application_id)
    
    
    def export_controller_cont(self,controller_name):
        Methods_framework.click(controller_name, "Text", "title", self.application_id)
        Methods_framework.click("btnExportConfiguration", "Button", "AutomationID",
                                                  self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Keyboardactions("{ENTER}")
        Methods_framework.wait(3)
    
    
    def delete_controller_ccn(self,ccn_name, option):
        Methods_framework.click(ccn_name, "Text", "title", self.application_id)
        Methods_framework.click("btnDeleteController", "Button", "AutomationID",
                                                  self.application_id)
        if option.upper() == "YES":
            Methods_framework.Doubleclick("Yes", "Button", "title",
                                                            self.application_id)
        if option.upper() == "ALL":
            Methods_framework.Doubleclick("Yes to All", "Button", "title",
                                                            self.application_id)
        if option.upper() == "NO":
            Methods_framework.Doubleclick("No", "Button", "title",
                                                            self.application_id)
        if option.upper() == "CANCEL":
            Methods_framework.Doubleclick("Cancel", "Button", "title",
                                                            self.application_id)
    
    
    def delete_controller_bus(self,bus_name, option):
        Methods_framework.click(bus_name, "Text", "title", self.application_id)
        Methods_framework.click("btnDeleteController", "Button", "AutomationID",
                                                  self.application_id)
        if option.upper() == "YES":
            Methods_framework.click("Yes", "Button", "title",
                                                      self.application_id)
        if option.upper() == "ALL":
            Methods_framework.click("Yes to All", "Button", "title",
                                                      self.application_id)
        if option.upper() == "NO":
            Methods_framework.Doubleclick("No", "Button", "title",
                                                            self.application_id)
        if option.upper() == "CANCEL":
            Methods_framework.Doubleclick("Cancel", "Button", "title",
                                                            self.application_id)
    
    
    def delete_controller_cont(self,controller_name, option):
        Methods_framework.click(controller_name, "Text", "title", self.application_id)
        Methods_framework.click("btnDeleteController", "Button", "AutomationID",
                                                  self.application_id)
        if option.upper() == "YES":
            Methods_framework.click("Yes", "Button", "title",
                                                      self.application_id)
        if option.upper() == "ALL":
            Methods_framework.click("Yes to All", "Button", "title",
                                                      self.application_id)
        if option.upper() == "NO":
            Methods_framework.Doubleclick("No", "Button", "title",
                                                            self.application_id)
        if option.upper() == "CANCEL":
            Methods_framework.Doubleclick("Cancel", "Button", "title",
                                                            self.application_id)
    
    
    def download_controller(self,controller_name, bus, chiller_name):
        Methods_framework.click(controller_name, "Text", "title", self.application_id)
        Methods_framework.click("btnDownloadController", "Button", "AutomationID",
                                                  self.application_id)
        Methods_framework.click(bus, "Text", "title", self.application_id)
        Methods_framework.click("btnDownloadController", "Button", "AutomationID",
                                                  self.application_id)
        Methods_framework.click(chiller_name, "Text", "title", self.application_id)
        Methods_framework.click("btnDownloadController", "Button", "AutomationID",
                                                  self.application_id)
    
    
    def download_controller_ccn(self,option):
        Methods_framework.click("test CCN", "Text", "title", self.application_id)
        Methods_framework.click("btnDownloadController", "Button", "AutomationID",
                                                  self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Keyboardactions("{ENTER}")
        if option.upper() == "YES":
            Methods_framework.Doubleclick("Yes", "Button", "title",
                                                            self.application_id)
            Methods_framework.wait(3)
            Methods_framework.Doubleclick("Yes", "Button", "title",
                                                            self.application_id)
            Methods_framework.doubleclickondialougbox("6", "Button", "AutomationID",
                                                                        self.application_id)
            Methods_framework.wait(3)
            Methods_framework.doubleclickondialougbox("2", "Button", "AutomationID",
                                                                        self.application_id)
            Methods_framework.wait(3)
            Methods_framework.Doubleclick("Yes", "Button", "title",
                                                            self.application_id)
            Methods_framework.wait(3)
        if option.upper() == "ALL":
            Methods_framework.Doubleclick("Yes to All", "Button", "title",
                                                            self.application_id)
            Methods_framework.wait(15)
        if option.upper() == "NO":
            Methods_framework.Doubleclick("No", "Button", "title",
                                                            self.application_id)
        if option.upper() == "CANCEL":
            Methods_framework.Doubleclick("Cancel", "Button", "title",
                                                            self.application_id)
    
    
    def download_controller_bus(self,option):
        Methods_framework.click("BUS 0", "Text", "title", self.application_id)
        Methods_framework.click("btnDownloadController", "Button", "AutomationID",
                                                  self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Keyboardactions("{ENTER}")
        if option.upper() == "YES":
            Methods_framework.Doubleclick("Yes", "Button", "title",
                                                            self.application_id)
            Methods_framework.wait(3)
            Methods_framework.Doubleclick("Yes", "Button", "title",
                                                            self.application_id)
            Methods_framework.doubleclickondialougbox("6", "Button", "AutomationID",
                                                                        self.application_id)
            Methods_framework.wait(3)
            Methods_framework.doubleclickondialougbox("2", "Button", "AutomationID",
                                                                        self.application_id)
            Methods_framework.wait(3)
            Methods_framework.Doubleclick("Yes", "Button", "title",
                                                            self.application_id)
            Methods_framework.wait(3)
        if option.upper() == "ALL":
            Methods_framework.Doubleclick("Yes to All", "Button", "title",
                                                            self.application_id)
            Methods_framework.wait(15)
        if option.upper() == "NO":
            Methods_framework.Doubleclick("No", "Button", "title",
                                                            self.application_id)
        if option.upper() == "CANCEL":
            Methods_framework.Doubleclick("Cancel", "Button", "title",
                                                            self.application_id)
    
    

    def download_controller_cont(self,controller_name):
        Methods_framework.click(controller_name, "Text", "title", self.application_id)
        Methods_framework.click("btnDownloadController", "Button", "AutomationID",
                                                  self.application_id)
        Methods_framework.wait(3)
        Methods_framework.doubleclickondialougbox("6", "Button", "AutomationID",
                                                                    self.application_id)
    
        Methods_framework.wait(5)


    def upload_controller_cont(self, controller_name):
        print (f" Upload controller {controller_name}")
        Methods_framework.click(str(self.ccnid), "Text", "title", str(self.application_id))
        Methods_framework.click(controller_name, "Text", "title", str(self.application_id))
        Methods_framework.Doubleclick(controller_name, "Text", "TITLE", str(self.application_id))

        Methods_framework.click("btnUploadController", "Button", "AutomationID",
                                self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Doubleclick("AlertDialogView", "Custom", "title",
                                      self.application_id)
        Methods_framework.Doubleclick("Yes", "Button", "title",
                                      self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Doubleclick("treControllers", "TreeView", "title", self.application_id)
        Methods_framework.Doubleclick(str(self.ccnid), "Text", "title", self.application_id)

    def windows_operation(self,option):
        Methods_framework.Doubleclick("Window", "MenuItem", "title", self.application_id)
        Methods_framework.wait(3)
        if option.upper() == "HORIZONTAL":
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.wait(3)
            Methods_framework.Keyboardactions("{ENTER}")
            Methods_framework.wait(3)
    
        if option.upper() == "VERTICAL":
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.wait(3)
            Methods_framework.Keyboardactions("{ENTER}")
            Methods_framework.wait(3)
    
        if option.upper() == "CASCADE":
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.wait(3)
            Methods_framework.Keyboardactions("{ENTER}")
            Methods_framework.wait(3)
    
        if option.upper() == "CLOSE":
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.Keyboardactions("{DOWN}")
            Methods_framework.wait(3)
            Methods_framework.Keyboardactions("{ENTER}")
            Methods_framework.wait(3)
    
    
    def alarm_history_export(self,controller_name):
        Methods_framework.click("test CCN", "Text", "title", self.application_id)
        Methods_framework.Doubleclick(controller_name, "Text", "Title",
                                                        self.application_id)
        Methods_framework.wait("3")
        Methods_framework.Doubleclick("btnAlarmHistory", "Button", "AutomationID",
                                                        self.application_id)
        Methods_framework.wait("30")
        Methods_framework.Doubleclick("btnExport", "Button", "AutomationID",
                                                        self.application_id)
        Methods_framework.wait("3")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{ENTER}")
        Methods_framework.wait("5")

    def date_time_broadcast(self, controller_name=None):
        Methods_framework.click("test CCN", "Text", "title", self.application_id)
        if controller_name != None:Methods_framework.click(controller_name, "Text", "title", self.application_id)
        Methods_framework.Doubleclick("btnDateTime", "Button", "AutomationID",
                                                        self.application_id)

        Methods_framework.wait("3")
        Methods_framework.Doubleclick("Use PC date/time", "Button", "title",
                                      self.application_id)
        time.sleep(5)
        Methods_framework.Doubleclick("OK", "Button", "title",
                                                        self.application_id)
        Methods_framework.wait("3")
        Methods_framework.Doubleclick("2", "Button", "AutomationID",self.application_id)
        Methods_framework.wait("5")

    def time_schedule_config(self,controller_name):
        Methods_framework.click(str(self.ccnid), "Text", "title", str(self.application_id))
        Methods_framework.click(controller_name, "Text", "title", str(self.application_id))
        Methods_framework.Doubleclick(controller_name, "Text", "TITLE", str(self.application_id))
        Methods_framework.wait("3")

        Methods_framework.click("Time Schedule", "Text", "TITLE",
                                      self.application_id)
        Methods_framework.Doubleclick("Time Schedule", "Text", "TITLE",
                                                        self.application_id)
        Methods_framework.Doubleclick("OCCPC01S", "Text", "TITLE",
                                                        self.application_id)
        Methods_framework.wait("3")
        Methods_framework.Doubleclick("From:", "Text", "TITLE",
                                                        self.application_id)
        Methods_framework.Keyboardactions("{DOWN}")
        Methods_framework.Keyboardactions("{DOWN}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{SPACE}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{SPACE}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{SPACE}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{SPACE}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.wait("3")
        Methods_framework.Settext("00", "Edit", "TITLE",
                                                    self.application_id, "09")
    
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.wait("3")
        Methods_framework.Settext("FirstSegment", "Edit", "AutomationID",
                                                    self.application_id, "12")
        Methods_framework.Doubleclick("btnSave", "Button", "AutomationID",
                                                        self.application_id)
    
    
    def controller_refresh_ccn(self):
        Methods_framework.Doubleclick("test CCN", "Text", "Title", self.application_id)
        Methods_framework.wait(3)
        Methods_framework.Doubleclick("btnRefresh", "Button", "AutomationID",
                                                        self.application_id)
        Methods_framework.wait("3")
        Methods_framework.Doubleclick("Yes to All", "Button", "title",
                                                        self.application_id)
        Methods_framework.wait("30")
    
    
    def BusScan(self):
        Methods_framework.Doubleclick("test CCN", "Text", "Title", self.application_id)
        Methods_framework.click("btnBusScan", "Button", "Automationid",
                                                  self.application_id)
        Methods_framework.wait("3")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{ENTER}")
        Methods_framework.wait("10")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{ENTER}")
        Methods_framework.wait("3")
        Methods_framework.Keyboardactions("{TAB}")
        Methods_framework.Keyboardactions("{ENTER}")
    
    
    def alarm_history(self,controller_name):
        Methods_framework.click("test CCN", "Text", "title", self.application_id)
        Methods_framework.click(controller_name, "Text", "title", self.application_id)
        Methods_framework.Doubleclick(controller_name, "Text", "TITLE",
                                                        self.application_id)
        Methods_framework.click("btnAlarmHistory", "Button", "AutomationID",
                                                  self.application_id)
    
    
    def autorefresh_controller(self,controllername):
    
        Methods_framework.click("test CCN", "Text", "title", self.application_id)
        Methods_framework.click(controllername, "Text", "title", self.application_id)
        Methods_framework.click("btnRefresh", "Button", "AutomationID",
                                                  self.application_id)
    
    def controller_config_export(self,controller_name):
        print (f"Export configuration {controller_name}")
        # Methods_framework.click("test CCN", "Text", "title", self.application_id)
        # Methods_framework.click(controller_name, "Text", "title", self.application_id)
        Methods_framework.click(str(self.ccnid), "Text", "title", str(self.application_id))
        Methods_framework.click(controller_name, "Text", "title", str(self.application_id))
        Methods_framework.Doubleclick(controller_name, "Text", "TITLE", str(self.application_id))
        Methods_framework.click("btnExportPoints", "Button", "AutomationID",str(self.application_id))
        Methods_framework.wait("20")
        # app = WindowApp()
        # app.app_close('Downloads')
        time.sleep(2)

    def close_app(self):
        Methods_framework.closeapp()
        print("DM App Closed")
        # os.system(HomePageLocatars.explorer_start)

if __name__ == "__main__":
    DM_obj=DeviceManager_fun("test CCN")
    controler_name="30XV_PIC: 30XV - 0, 1"
    DM_obj.ConnectCCN()
    DM_obj.date_time_broadcast(controler_name)
    time.sleep(5)
    DM_obj.DisConnectCCN()
    DM_obj.close_app()
  # DM_obj.windows_operation("CASCADE")
    # DM_obj.Addresssearch()
 # DM_obj.Export("30XV_PIC: 30XAXW PIC6 Ctrl - 0, 6")ccn
    # DM_obj.controller_config_export("30XV_PIC: 30XAXW PIC6 Ctrl - 0, 6")
    # DM_obj.BusScan()
    # DM_obj.upload_controller_cont("30XV_PIC: 30XAXW PIC6 Ctrl - 0, 6")
# Importcont("CCN",str('"B000C001.cwx" "B000C002.cwx"'),"ALL",1)
# controller_config_export("30XV_PIC: 30XV PIC6 - 0, 6")
# date_time_broadcast("30XV_PIC: 30XV PIC6 - 0, 6")
# alarm_history("30XV_PIC: 30XV PIC6 - 0, 6")
# alarm_history_export("30XV_PIC: 30XV PIC6 - 0, 6")

# Addcontroller("30XV_PIC","30XV PIC6 - 0, 6","0","6")
# autorefresh_controller("30XV_PIC: 30XV PIC6 - 0, 6")
#
# ConnectCCN()
# #
# time.sleep(4)

# #readData("testCCN", "30XV_PIC: 30XV - 0, 1", "Status", "TEMP", "PointsTable", input_cond=["OAT"])
# #readData("testCCN", "30XV_PIC: 30XV - 0, 1", "Maintenance", "ALARMRST", "PointsTable", input_cond=["Current Alarm 1"])
# #readData("testCCN", "30XV_PIC: 30XV - 0, 1", "Maintenance", "ALARMRST", "PointsTable", input_cond=["Alarm Reset"])

#

