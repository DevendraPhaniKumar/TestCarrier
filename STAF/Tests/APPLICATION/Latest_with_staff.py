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
# print(dirnameutils)

from Lib_space import CCN
from Lib_space import VirSim_Module
from Lib_space import HMI_Interaction
from Utility import GeneralFunctions
from Lib_space.APPLICATION import P_Link
import configparser


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

        print(Colour + "Setup Function - Completed")
        print("********************************************************************************")

    # def test_1_application(self):
    #     print(Colour + " Reading Software Version")
    #     print("********************************************************************************")
    #     self.APP.SW_Version()
    #     print(Colour + "Unlocking Using Factory Password")
    #     print("********************************************************************************")
    #     self.APP.lock()
    #     print(Colour + "Clearing Alarms")
    #     print("********************************************************************************")
    #     self.APP.Clear_Alarm()
    #
    # def test_2_application(self):
    #     # print(Colour + "Changing the IP Address of ETH0")
    #     # print("********************************************************************************")
    #     # self.APP.Eath0_IP()
    #     # print(Colour + "Changing the IP Address of ETH1")
    #     # print("********************************************************************************")
    #     # self.APP.Eath1_IP()
    #     # print(Colour + "Changing the DNS Servers")
    #     # print("********************************************************************************")
    #     # self.APP.DNS_Server()
    #     print(Colour + "Changing the Network Configurations")
    #     print("********************************************************************************")
    #     self.APP.Network_Config()
    #
    # def test_3_application(self):
    #     print(Colour + "Doing CCN Configuration ")
    #     print("********************************************************************************")
    #     self.APP.CCN_Config()
    #     print(Colour + "Factory and Service Parameters writing")
    #     print("********************************************************************************")
    #     self.APP.ccn_par_write()
    #     self.APP.Reboot_Pic6()
    #
    def test_4_application(self):
        print(Colour + "NTP Server Settings")
        print("********************************************************************************")
        self.APP.NTP_Time_Syn()
    #
    def test_5_application(self):
        print(Colour + " Verifing Time Zone settings")
        print("********************************************************************************")
        self.APP.Time_Zone()

    # def test_6_Quick_PreCheck(self):
    #     print(Colour + "Performing the Pre Check of Quick Test")
    #     print("********************************************************************************")
    #     self.APP.quick_test()
    #     print(Colour + "Pre Check of Quick Test Completed Successfully")

    # def test_7_Quick_Enable(self):
    #     print(Colour + "Enabling the Quick Test")
    #     print("********************************************************************************")
    #     self.APP.Quick_Enable()
    #     print(Colour + "Enabling Quick Test Completed Successfully")
    #
    # def test_8_Quick_EXV(self):
    #     print(Colour + "Performing EXV Test (Quick Test)")
    #     print("********************************************************************************")
    #     self.APP.Quick_EXV()
    #     print(Colour + "EXV Test Completed Successfully")





    # def test_7_application(self):
    #     print(Colour + "Performing the negative scenario of Quick Test")
    #     print("********************************************************************************")
    #     self.APP.Neg_test()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\" + "e@e"))
