import os
import sys
import HtmlTestRunner
import colorama
from colorama import Fore, Style
import unittest
import time
Colour = Fore.CYAN

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(dirnameutils)


from Lib_space import CCN
from Lib_space import VirSim_Module
from Lib_space import HMI_Interaction
from Utility import GeneralFunctions
from Lib_space.APPLICATION import P_Link
import configparser,ast

from Lib_space.BACNET import BACnet_Module

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)
# print(foldername)

DataParameter = configparser.ConfigParser()
DataParameter.read(dirnameutils + '\\Data\\BACNET\\TestData.ini')
bacnet_analog_value_obj_instance = ast.literal_eval(DataParameter.get("Inputs", "av_forcelevel_instance"))
bacnet_analog_value_obj_propname = ast.literal_eval(DataParameter.get("Inputs", "analog_value_obj_propname"))
bacnet_analog_value_obj_propname_1 = ast.literal_eval(DataParameter.get("Inputs", "av_obj_unsupported_propname")) #  in Name _1 is added  for Unsupported_Propname


class TestCases(unittest.TestCase):

    def setUp(self):

        print(Colour + "Setup Function - Start")
        print("********************************************************************************")
        self.ccn_handle = CCN.CCN_Adatper(1, 3, 2, 50, 50, 1, 239, 0, 0)
        # sytype, BaudRate, NoOfTries, ResTimOut, DelayRestTimeOut, ID(Destination Address), ElemNo, AlarmAck, BusNo
        self.ccn_handle.setDestination(220, 0, 1, 0, 4)
        # sourceAddr, SourceBus, destAddr, destBus, forcelevel
        self.TestParameters = configparser.ConfigParser()
        self.TestParameters.read(dirnameutils + "\\Data\\APPLICATION\\Test_Parameters.ini")
        VisSimFilePath = self.TestParameters.get("TEST_PARAMETERS", "VISSIM_XML_Path")
        HMI_CONTROLLER = self.TestParameters.get("TEST_PARAMETERS", "HMI_CONTROLLER")
        HMI_POINTS = self.TestParameters.get("TEST_PARAMETERS", "HMI_POINTS")
        self.vir_sim_instance = VirSim_Module.Virtual_Simulator(220, 0, 15, 15, VisSimFilePath)
        self.hmi_handle = HMI_Interaction.HMI_Interaction(HMI_CONTROLLER, HMI_POINTS)
        self.APP = P_Link.Application_Test(self.ccn_handle, self.vir_sim_instance, self.hmi_handle)
        self.Utility_Obj = GeneralFunctions.utility_Functions(self.ccn_handle, self.vir_sim_instance, self.hmi_handle)
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(DataParameter.get("Config", "dut_address"))


        print(Colour + "Setup Function - Completed")
        print("********************************************************************************")

    def test_01_Application_Reading_Software_Version(self):
        print(Colour + " Reading Software Version")
        print("********************************************************************************")
        self.APP.SW_Version()
        print(Colour + "Unlocking Using Factory Password")
        print("********************************************************************************")
        self.APP.lock()
        print(Colour + "Clearing Alarms")
        print("********************************************************************************")
        self.APP.Clear_Alarm()

    def test_02_Application_Setting_IP_Address(self):
        print(Colour + "Changing the IP Address of ETH0")
        print("********************************************************************************")
        self.APP.Eath0_IP()
        print(Colour + "Changing the IP Address of ETH1")
        print("********************************************************************************")
        self.APP.Eath1_IP()
        print(Colour + "Changing the DNS Servers")
        print("********************************************************************************")
        self.APP.DNS_Server()
        print(Colour + "Changing the Network Configurations")
        print("********************************************************************************")
        time.sleep(120)
        self.APP.Network_Config()

    def test_03_Application_Writing_Factroy_parameters(self):
        print(Colour + "Doing CCN Configuration ")
        print("********************************************************************************")
        self.APP.CCN_Config()
        print(Colour + "Factory and Service Parameters writing")
        print("********************************************************************************")
        self.APP.ccn_par_write()
        self.APP.Reboot_Pic6()

    def test_04_Application_NTP_Server_Setting(self):
        print(Colour + "NTP Server Settings")
        print("********************************************************************************")
        self.APP.NTP_Time_Syn()

    def test_05_Application_Verifing_TimeZone_Settings(self):
        print(Colour + " Verifing Time Zone settings")
        print("********************************************************************************")
        self.APP.Time_Zone()

    def test_06_Application_Quick_Test(self):
        print(Colour + "Performing the Pre Check of Quick Test")
        print("********************************************************************************")
        self.APP.lock()
        self.APP.quick_test()
        print(Colour + "Pre Check of Quick Test Completed Successfully")

    def test_07_Application_Quick_Negitive_Cases(self):
        print(Colour + "Performing the negative scenario of Quick Test")
        print("********************************************************************************")
        self.APP.lock()
        self.APP.Neg_test()

    def test_08_BACnet_AV_Obj_ForceLevelTest_func(self):

        failStr = ''
        try:
            print('--------------------START-------------------------------')

            print('<----Read Analog Value of Instance :' + bacnet_analog_value_obj_instance + '--->')
            read_ouput = self.bacnet.readproperty('analogValue', bacnet_analog_value_obj_instance,
                                                  bacnet_analog_value_obj_propname[0])
            print(read_ouput)
            self.assertEqual(read_ouput, '100.0', msg='Read Analog Value is not showing correctly')

            print(
                '<----Write Force level negative test :AV ,Instance 553->write present value with Force 2=value 7--->')
            pres_Value = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance, 'presentValue', '7',
                                                   priority=2)
            print(pres_Value)

            print('<----Verify present value with Force 2=value 7 for AV ,Instance 553---->')
            read_ouput = self.bacnet.readproperty('analogValue', bacnet_analog_value_obj_instance,
                                                  bacnet_analog_value_obj_propname[0])
            print(read_ouput)
            self.assertEqual(read_ouput, '7.0', msg='Read Analog Value is not showing correctly')

            print(
                '<----Write Force level negative test :AV ,Instance 553->write present value with Force 4=value 14--->')
            pres_Value = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance, 'presentValue',
                                                   '14', priority=4)
            print(pres_Value)

            print('<----Verify present value with Force 4=value 14 for AV ,Instance 553---->')
            read_ouput = self.bacnet.readproperty('analogValue', bacnet_analog_value_obj_instance,
                                                  bacnet_analog_value_obj_propname[0])
            print(read_ouput)
            self.assertEqual(read_ouput, '7.0', msg='Read Analog Value is not showing correctly')
            self.assertNotEqual(read_ouput, '14.0', msg='Read Analog Value is showing correctly')

            print('<----Verify present value as Null with Force 2 and do relinquish for AV ,Instance 553---->')
            prop_val = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance, 'presentValue',
                                                 'null', priority=2)
            print(prop_val)
            self.assertEqual(prop_val, 'ack', msg='Not able to write Analog Value')

            print('<----Verify present value with Force 4=value 14 for AV ,Instance 553---->')
            read_ouput = self.bacnet.readproperty('analogValue', bacnet_analog_value_obj_instance,
                                                  bacnet_analog_value_obj_propname[0])
            print(read_ouput)
            self.assertEqual(read_ouput, '14.0', msg='Read Analog Value is not showing correctly')

            print(
                '<----Write Force level negative test :AV ,Instance 553->write present value with Force 14=value 22--->')
            pres_Value = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance, 'presentValue',
                                                   '22', priority=14)
            print(pres_Value)

            print('<----Verify present value with Force 14=value 22 for AV ,Instance 553---->')
            read_ouput = self.bacnet.readproperty('analogValue', bacnet_analog_value_obj_instance,
                                                  bacnet_analog_value_obj_propname[0])
            print(read_ouput)
            self.assertEqual(read_ouput, '14.0', msg='Read Analog Value is not showing correctly')
            self.assertNotEqual(read_ouput, '22.0', msg='Read Analog Value is showing correctly')
            print('--------------------STOP--------------------------------\n')

            print('<----Verify present value as Null with Force 4 and do relinquish for AV ,Instance 553---->')
            prop_val = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance, 'presentValue',
                                                 'null', priority=4)
            print(prop_val)
            self.assertEqual(prop_val, 'ack', msg='Not able to write Analog Value')

            print('<----Verify present value as Null with Force 14 and do relinquish for AV ,Instance 553---->')
            prop_val = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance, 'presentValue',
                                                 'null', priority=14)
            print(prop_val)
            self.assertEqual(prop_val, 'ack', msg='Not able to write Analog Value')

            print('<----Read Analog Value of Instance :' + bacnet_analog_value_obj_instance + '--->')
            read_ouput = self.bacnet.readproperty('analogValue', bacnet_analog_value_obj_instance,
                                                  bacnet_analog_value_obj_propname[0])
            print(read_ouput)
            self.assertEqual(read_ouput, '100.0', msg='Read Analog Value is not showing correctly')

        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def test_09_BACnet_AnalogValue_Obj_Read_Negative_func(self):
        failStr = ''
        AV = [
            #['85', 'presentValue', 'Real', 'O']
            ['22', 'covIncrement', 'Real', 'O'],
            ['87', 'priorityArray', 'PriorityArray', 'R'],
            ['104', 'relinquishDefault', 'Real', 'O']
            ]
        objList1 = [('analogValue', 545)]
        print('***************************************')
        for objType, instNum in objList1:
            print(objType)
            print(instNum)

            list = AV
            for strpropID, strpropName, DataType, RW in list:
                try:
                    PropValue = self.bacnet.readproperty(objType, instNum, strpropID)
                    print(PropValue)
                    self.assertEqual(PropValue, None,msg='Property Value is: ' + strpropName + ' is not working')
                    print('Read Property of Object Name: ' + objType + '  PropertyValue: ' + strpropID + '  is: ' + str(PropValue))
                except Exception as e:
                    failStr = failStr + str(e.args[0]) + '.\n'
        if failStr != "":
            raise Exception(failStr)

    def test_10_BACnet_AV_Obj_OutofRangeTest_func(self):

        failStr = ''
        try:
            print('--------------------START-------------------------------')

            print('<----Read Analog Value of Instance :' + bacnet_analog_value_obj_instance + '--->')
            pres_Value = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance,
                                                   bacnet_analog_value_obj_propname[0], '-1')
            print(pres_Value)
            self.assertEqual(pres_Value, None, msg='Read Analog Value is not showing correctly')

        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def test_11_BACnet_AnalogValue_Obj_Write_Negative_func(self):

        failStr = ''
        inst_list = [545, 546]
        prop_list = {'description': 'test', 'objectName': 'test', 'outOfService': 'True', 'units': 'degreesCelsius',
                     'eventState': 'normal', 'statusFlags': '[0, 0, 0, 0]',
                     'objectIdentifier': """('analogValue', 545)""", 'objectType': 'analogValue'}
        try:
            print('--------------------START-------------------------------')
            print('<----Write AnalogValue Propertys --->')
            for i in range(0, len(inst_list)):
                for k, v in prop_list.items():
                    Op_Value = self.bacnet.writeproperty('analogValue', int(inst_list[i]), str(k), v)
                    print(Op_Value)
                    self.assertEqual(Op_Value, None, msg='Able to Write Value')
            print('--------------------STOP--------------------------------\n')

        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def test_12_BACnet_AV_Obj_UnsupportedPropTest_func(self):

        failStr = ''
        try:
            print('--------------------START-------------------------------')
            for propName in bacnet_analog_value_obj_propname_1:
                print(propName)
                print('<----Read Analog Value of Instance :' + bacnet_analog_value_obj_instance + '--->')
                read_ouput = self.bacnet.readproperty('analogValue', bacnet_analog_value_obj_instance, propName)
                print(read_ouput)
                self.assertEqual(read_ouput, None, msg='Read Analog Value is not showing correctly')

        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def test_13_BACnet_BinaryValue_Obj_Read_Negative_func(self):
        failStr = ''
        BV = [
            #['85', 'presentValue', 'Real', 'O']
            #['22', 'covIncrement', 'Real', 'O'],
            ['87', 'priorityArray', 'PriorityArray', 'R'],
            ['104', 'relinquishDefault', 'Real', 'O']
            ]
        objList1 = [('binaryValue', 1),('binaryValue', 2)]
        print('***************************************')
        for objType, instNum in objList1:
            print(objType)
            print(instNum)

            list = BV
            for strpropID, strpropName, DataType, RW in list:
                try:
                    PropValue = self.bacnet.readproperty(objType, instNum, strpropID)
                    print(PropValue)
                    self.assertEqual(PropValue, None,msg='Property Value is: ' + strpropName + ' is not working')
                    print('Read Property of Object Name: ' + objType + '  PropertyValue: ' + strpropID + '  is: ' + str(PropValue))
                except Exception as e:
                    failStr = failStr + str(e.args[0]) + '.\n'
        if failStr != "":
            raise Exception(failStr)

    def test_14_BACnet_BinaryValue_Obj_Write_Negative_func(self):

        failStr = ''
        inst_list = [1, 2]
        prop_list = {'description': 'test', 'objectName': 'test', 'outOfService': 'True', 'inactiveText': 'True',
                     'eventState': 'normal', 'statusFlags': '[0, 0, 0, 0]',
                     'objectIdentifier': """('binaryValue', 1)""", 'objectType': 'binaryValue'}
        try:
            print('--------------------START-------------------------------')
            print('<----Write BinaryValue Propertys --->')
            for i in range(0, len(inst_list)):
                for k, v in prop_list.items():
                    Op_Value = self.bacnet.writeproperty('binaryValue', int(inst_list[i]), str(k), v)
                    print(Op_Value)
                    self.assertEqual(Op_Value, None, msg='Able to Write Value')
            print('--------------------STOP--------------------------------\n')

        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def test_15_BACnet_MSV_Obj_Read_Negative_func(self):
        failStr = ''
        MV = [
            ['113', 'timeDelay', 'Real', 'O'],
            ['87', 'priorityArray', 'PriorityArray', 'R'],
            ['104', 'relinquishDefault', 'Real', 'O']
            ]
        objList1 = [('multiStateValue', 21),('multiStateValue', 109)]
        print('***************************************')
        for objType, instNum in objList1:
            print(objType)
            print(instNum)

            list = MV
            for strpropID, strpropName, DataType, RW in list:
                try:
                    PropValue = self.bacnet.readproperty(objType, instNum, strpropID)
                    print(PropValue)
                    self.assertEqual(PropValue, None,msg='Property Value is: ' + strpropName + ' is not working')
                    print('Read Property of Object Name: ' + objType + '  PropertyValue: ' + strpropID + '  is: ' + str(PropValue))
                except Exception as e:
                    failStr = failStr + str(e.args[0]) + '.\n'
        if failStr != "":
            raise Exception(failStr)

    def test_16_BACnet_MSV_Obj_Write_Negative_func(self):

        failStr = ''
        inst_list = [21, 109]
        prop_list = {'description': 'test', 'objectName': 'test', 'outOfService': 'True', 'units': 'degreesCelsius',
                     'eventState': 'normal', 'statusFlags': '[0, 0, 0, 0]', 'presentValue':1, 'relinquishDefault':1,
                     'objectIdentifier': """('multiStateValue', 21)""", 'objectType': 'multiStateValue'}
        try:
            print('--------------------START-------------------------------')
            print('<----Write Multi State Value Propertys --->')
            for i in range(0, len(inst_list)):
                for k, v in prop_list.items():
                    Op_Value = self.bacnet.writeproperty('multiStateValue', int(inst_list[i]), str(k), v)
                    print(Op_Value)
                    self.assertEqual(Op_Value, None, msg='Able to Write Value')
            print('--------------------STOP--------------------------------\n')

        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

    def test_17_download_sierra_router_firmware_package(self):
        os.system("python C:\\End_To_End_Automation\\STAF\\Tests\\CONNECTIVITY\\Sierra_fw_upgrade.py")



    def tearDown(self):
        self.bacnet.disconnect()
        pass

if __name__ == '__main__':
    # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\" + foldername))
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\" + "E2E"))
