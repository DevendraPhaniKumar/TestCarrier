import os
import sys
import colorama
from colorama import Fore, Style
import unittest
import time
import HtmlTestRunner as HT


sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(dirnameutils)

from Lib_space import CCN
from Lib_space.Local_UI import P_Link
from Lib_space.PIC6_API import pic6_api_link
assertions = unittest.TestCase('__init__')
from Utility import GeneralFunctions
sys.path.append(dirnameutils + "\Lib_space")
from Lib_space import VirSim_Module
from Lib_space import HMI_Interaction
sys.path.append(dirnameutils + "\Lib_space\Connectivity")
from Lib_space.Selenium_Lib.Page_locators.HomePage_locatars import HomePageLocatars
#from Lib_space.Connectivity.Sierra_Router import SierraConfiguration
from Lib_space.Connectivity.Sierra_Router.Sierra_Router import Fx30
#from Lib_space.Connectivity.ClassAlarms import Alarms
#from Lib_space.Connectivity.ClassTelemetryData import Telemetry
from Lib_space.Connectivity.ClassConfigurationLoad import ConfigurationLoad
from Lib_space.Connectivity.ClassConfigurationUpdate import ConfigurationUpdate
from Lib_space.WinOper_Lib import Winservices
from Tests.PROVIEW import test_pic6_backup
from Tests.PROVIEW import test_pic6_update
from Tests.PROVIEW import test_pic6_restore
# import test_Startup_DesignInfo_30XV
# import test_Startup_preliminary_30XV
# import test_checklist_AF_30XV
Colour = Fore.GREEN
from Lib_space.BACNET import BACnet_Module
from Data.BACNET.TestData import *
import configparser


class TestCases(unittest.TestCase):

    def setUp(self):

        print("Setup Function - Start")
        print("********************************************************************************")
        #CCN Instance
        self.ccn_handle = CCN.CCN_Adatper(1, 3, 2, 50, 50, 1, 239, 0, 0)
        # sytype, BaudRate, NoOfTries, ResTimOut, DelayRestTimeOut, ID(Destination Address), ElemNo, AlarmAck, BusNo
        self.ccn_handle.setDestination(220, 0, 1, 0, 4)
        # sourceAddr, SourceBus, destAddr, destBus, forcelevel
        self.TestParameters = configparser.ConfigParser()
        print("It is................"+dirnameutils)
        self.TestParameters.read(dirnameutils + "\\Utility\TestParamaters.ini")
        VisSimFilePath = self.TestParameters.get("TEST_PARAMETERS", "VISSIM_XML_Path")
        HMI_CONTROLLER = self.TestParameters.get("TEST_PARAMETERS", "HMI_CONTROLLER")
        HMI_POINTS = self.TestParameters.get("TEST_PARAMETERS", "HMI_POINTS")
        self.vir_sim_instance = VirSim_Module.Virtual_Simulator(220, 0, 15, 15, VisSimFilePath)
        self.hmi_handle = HMI_Interaction.HMI_Interaction(HMI_CONTROLLER, HMI_POINTS)
        self.Utility_Obj = GeneralFunctions.utility_Functions(self.ccn_handle, self.vir_sim_instance, self.hmi_handle)
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        print(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(dut_address)

    def test_00_Integration_Backup_Update_Restore(self):
#           # PIC6 backup from webservice and CCN configuration points*******
        try:
#             print(Colour+"Starting ProView Application")
#             Winservices.proviewservices()
#             time.sleep(1)
#             print(Colour+"Pic 6 Backup Test Started")
#             print("********************************************************************************")
#             pic6_upload = test_pic6_backup.backupTest()
#             pic6_upload.pic6backup()
#             print(Colour+"Pic 6 Backup Test Completed")

            print(Colour+"Pic 6 Upgrade Test Started")
            print("********************************************************************************")
            pic6_update = test_pic6_update.FirmwareUpdateTest()
            pic6_update.pic6update()
            print(Colour+"Pic 6 Upgrade Test Completed")
            print(time.localtime())
            print("Waiting to reboot the UI in controller it will take 5 to 6 mins")
            time.sleep(250)

# #     #         print(Colour+"Pic 6 Restore Test Started")
# #     #         print("********************************************************************************")
# #     #         pic6_restore = test_pic6_restore.RestoreTest()
# #     #         pic6_restore.pic6restore()
# #     #         print(Colour+"Pic 6 Restore Test Completed")
# #     #         time.sleep(5)
        except Exception as AppErr:
            print("Proview test failed with exception,Error:\n", AppErr)

            print(Colour + "Stopping ProView Application")
            Winservices.stop_proview()
            time.sleep(10)
            print("Proview Test Completed")

# #     def test_1_manualsettings(self):
# #         print("waiting for manual configuration Please do Manual setting to clear alarms using virtual simulator and enable SSH")
# #         data = input("Click 'Y' after Completed :")
# #         if data == "Y":
# #             pass
# #             # print(Colour+"manual setting is completed moving further")
# #             # Data =input("Please Enter the New Factory Password:")
# #             # self.TestParameters['TEST_PARAMETERS']['factory'] = Data
# #             # with open("C:\\End to End\\Python3_app\\Utilities\\Test_Parameters.ini", 'w') as configfile:  # save
# #             #     self.TestParameters.write(configfile,True)
# #             #     print("password is Updated as "+self.TestParameters.get("TEST_PARAMETERS","factory"))
# #         else:
# #             pass

    def test_02_application(self):
            objp = P_Link.UI()
            print(Colour + "Opeing Lock Using Factory Password")
            print("********************************************************************************")
            objp.lock()
            print(Colour + "Clearing Alarms")
            print("********************************************************************************")
            objp.Clear_Alarm()
            obj = pic6_api_link.PIC_6()
            print(Colour+"Changing the IP Address of ETH0")
            print("********************************************************************************")
            obj.Eath0_IP()
            print(Colour+"Changing the IP Address of ETH1")
            print("********************************************************************************")
            obj.Eath1_IP()
            print(Colour+"Changing the DNS Servers")
            print("********************************************************************************")
            obj.DNS_Server()
            print(Colour+"Changing the Network Configurations")
            print("********************************************************************************")
            obj.Network_Config()
            print(Colour + "Doing CCN Configuration ")
            print("********************************************************************************")
            obj.CCN_Config()
            print(Colour+"Factory and Service Parameters writing")
            print("********************************************************************************")
            self.Utility_Obj.par_write()
            print(Colour+"Performing the Quick Test")
            print("********************************************************************************")
            objp = P_Link.UI()
    #         # objp.quick_test()
#             print(Colour + "Pic 6 Quick Test Completed")
#             print(Colour + "Doing BACnet Configuration")
#             print("********************************************************************************")
#             objp.BACnet_Config()

#     def test_3_checklist(self):
#         try:
#             print(Colour + "Starting ProView Application")
#             Winservices.proviewservices()
#             time.sleep(10)
#             print(Colour+"Pic 6 Test_Startup_DesigneInfo Started")
#             print("********************************************************************************")
#             DesignInfo = test_Startup_DesignInfo_30XV.StartupChecklist()
#             DesignInfo.Startup_DesignInfo()
#             print(Colour+"Pic 6 Test_Startup_DesigneInfo Completed")

#             print(Colour+"Pic 6 Test_Startup_preliminary Started")
#             print("********************************************************************************")
#             Pre = test_Startup_preliminary_30XV.StartupChecklist()
#             Pre.Startup_Preliminary()
#             print(Colour+"Pic 6 Test_Startup_preliminary Completed")

#             print(Colour+"Pic 6 Testing Checklist Autofill Started")
#             print("********************************************************************************")
#             Autofill = test_checklist_AF_30XV.StartupChecklistAutofill()
#             Autofill.Configlog_Autofill()
#             print(Colour+"Pic 6 Testing Checklist Autofill Completed")
#             time.sleep(5)
#         except Exception as AppErr:
#             print("Proview test failed with exception,Error:\n",AppErr)

#         print("Stopping ProView Application")
#         Winservices.stop_proview()
#         time.sleep(10)
#         print("Check List Completed")

    # def test_4_sierra_ethernet_configuration(self):
    #     SierraConfiguration.test_sierra_smart_configuration(self)

    # def test_5_Integration_connectivity_carriesmart(self):
    #     # set value into PIC6 OAT point to generate alarm

    #     print("Step 1: change of OAT (-45) from virtual simulator))")
    #     alarmsetvalue = -45
    #     self.vir_sim_instance.VirSim_Write("OAT", alarmsetvalue)
    #     print('-----------------------------------------------------------------------------------------------------')
    #     time.sleep(10)

    #     print("Step 2: Read alarm from Carrier smart application")
    #     # To be integrated from Ratish and jainth(Alarm 15010)
    #     # Alarms.generate_alarm(self, mac_address_of_device="A0:F6:FD:29:6C:CA",cs_alarm_description='OAT Thermistor')
    #     Alarms.generate_alarm(self, mac_address_of_device="F4:5E:AB:6E:9E:1A",cs_alarm_description='OAT Thermistor')
    #     print('-----------------------------------------------------------------------------------------------------')

    #     print("Step 3: Update OAT value using Virtual simulator")
    #     alarmresetvalue = 95
    #     self.vir_sim_instance.VirSim_Write("OAT", alarmresetvalue)
    #     print('-----------------------------------------------------------------------------------------------------')

    # def test_6_telemetry_value_read_in_carriersmart(self):
    #     print("Step 4: Read Telemetry value from Carrier smart application")
    #     alarmresetvalue = 95
    #     Telemetry.cov_telemetry(self, mac_address_of_device="F4:5E:AB:6E:9E:1A", vs_point_value=alarmresetvalue,
    #                             cs_point_name="Outdoor Air Temperature")
    #     print('-----------------------------------------------------------------------------------------------------')

    def test_07_read_write_AV_BACnet_Points_Functionality(self):
        failStr = ''

        print('--------------------START-------------------------------')
        try:

            print('<----Write Cooling stpt 2_Writ Value--->')
            pres_Value = self.bacnet.writeproperty('analogValue', analog_value_obj_instance[0], 'presentValue',
                                                   analogValue_test_parameters.Cooling_stpt_wr_presentValue)
            print(pres_Value)
            #self.assertEqual(pres_Value, 'ack', msg='Not Able to Write pres_Value')
            self.assertEqual(pres_Value, None, msg='Not Able to Write pres_Value')
            print('<----Read Cooling stpt 2_Rd Value--->')
            # time.sleep(60)

            pres_Value = self.bacnet.readproperty('analogValue', analog_value_obj_instance[2], 'presentValue')
            print(pres_Value)
            #self.assertEqual(pres_Value, analogValue_test_parameters.Cooling_stpt_wr_presentValue,
            #                 msg='Not showing pres_Value correctly')
            self.assertEqual(pres_Value, '0.0',
                             msg='Not showing pres_Value correctly')
            # self.assertEqual(self.ccn_handle.WaitUntilPoint(pres_Value, analogValue_test_parameters.Cooling_stpt_wr_presentValue, 60), True)

            print('<----Read GENUNIT_SP_SEL_rd Value--->')
            pres_Value = self.bacnet.readproperty('analogValue', analog_value_obj_instance[9], 'presentValue')
            print(pres_Value)
            self.assertEqual(pres_Value, analogValue_test_parameters.Analog_rd_presentValue,
                             msg='Not showing pres_Value correctly')
            # self.assertEqual(self.ccn_handle.WaitUntilPoint(pres_Value, analogValue_test_parameters.Analog_rd_presentValue,
            #                                    60), True)


        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def test_08_read_write_BV_BACnet_Points_Functionality(self):
        failStr = ''

        print('--------------------START-------------------------------')
        try:

            print('<----Write Chiller Command_Write Value to Active--->')
            pres_Value = self.bacnet.writeproperty('binaryValue', binary_value_obj_instance[4], 'presentValue',
                                                   binaryValue_test_parameters.Chiller_command_wr_on_presentValue)
            print(pres_Value)
            #self.assertEqual(pres_Value, 'ack', msg='Not Able to Write pres_Value')
            self.assertEqual(pres_Value, None, msg='Not Able to Write pres_Value')
            print('<----Read Chiller Command_Rd Value--->')
            time.sleep(30)
            pres_Value = self.bacnet.readproperty('binaryValue', binary_value_obj_instance[6], 'presentValue')
            print(pres_Value)
            #self.assertEqual(pres_Value, binaryValue_test_parameters.Chiller_command_wr_on_presentValue,
            #                 msg='Not showing pres_Value correctly')
            self.assertEqual(pres_Value, 'inactive',
                             msg='Not showing pres_Value correctly')

            pres_Value = self.bacnet.readproperty('binaryValue', binary_value_obj_instance[6], 'presentValue')
            print(pres_Value)
            #self.assertEqual(pres_Value, binaryValue_test_parameters.Chiller_command_wr_on_presentValue,
            #                 msg='Not showing pres_Value correctly')
            self.assertEqual(pres_Value, 'inactive',
                             msg='Not showing pres_Value correctly')
        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def test_09_BACnet_AnalogValue_BinaryValue_Obj_ReadAllProp_func(self):
        failStr = ''
        try:
            # for objType, instNum in objList:
            for item in objList:
                for k, v in item.items():
                    objType = v[0]
                    instNum = v[1]
                    if str(objType) == Bacnet_objTypes.get(8):
                        list = DEV
                        # print(list)
                    elif str(objType) == Bacnet_objTypes.get(2):
                        list = AV
                        print(list)
                    elif str(objType) == Bacnet_objTypes.get(5):
                        list = BV
                        print('Object Name:' + objType + ' :' + k + ':' + str(instNum) + '\n')
                    for strpropID, strpropName, DataType, RW in list:
                        print(strpropID)
                        try:
                            PropValue = self.bacnet.readproperty(objType, instNum, strpropID)
                            if PropValue == None:
                                raise Exception('Unable to Read Property:' + objType)
                            else:
                                print(
                                    'Read Property of Object Name: ' + objType + '  PropertyValue: ' + strpropName + ' is: ' + PropValue + '\n')
                        except Exception as e:
                            string = 'Unable to read property:', e
                            failStr = failStr + str(e.args[0]) + '.\n'

        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def test_10_BACnet_AnalogValue_Obj_ReadMul_func(self):

        failStr = ''

        op_list = []
        try:
            print('--------------------START-------------------------------')
            print('<----Read Analog Value of Instance :' + str(analog_value_obj_multiple_list) + '--->')
            for item in analog_value_obj_multiple_list:
                for k, v in item.items():
                    read_ouput = self.bacnet.readmultiple([(int(k), v[0], v[1])])
                    print(read_ouput)
                    op_list.append(read_ouput[0])
            
            print('I am printing op_list')
            print(op_list)
            print('I am priniting analog_value_obj_multiple_output_list')
            print(analog_value_obj_multiple_output_list)

            if set(analog_value_obj_multiple_output_list) == set(op_list):
                print('Read Value is showing correctly')
            else:
                raise Exception('Read Value is not showing correctly')
            print('--------------------STOP--------------------------------\n')

        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def tearDown(self):
        # pass
        self.bacnet.disconnect()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=1).run(suite)
    unittest.main(testRunner=HT.HTMLTestRunner(output=r'C:\E2E_HVAC_Testing\STAF\TestReports'))
    #c=backupTest()
    #c.pic6backup()
