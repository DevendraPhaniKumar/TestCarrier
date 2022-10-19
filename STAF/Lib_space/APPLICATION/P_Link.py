import os
import sys
import struct
from datetime import date
from pytz import timezone
import time
import xlrd
import configparser
import unittest
import colorama
from colorama import Fore, Style
Colour1 = Fore.GREEN
Colour2 = Fore.RED
from Lib_space.APPLICATION.Local_UI import PIC6_UI_Touch
A = PIC6_UI_Touch.UI_Touch()

from Lib_space.APPLICATION.PIC6_API import PIC6_Rest_Utility
from Tests.CONNECTIVITY.Sierra_Router import Fx30
PIC6 = PIC6_Rest_Utility.Rest_Utility()



sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
# dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(dirnameutils)

assertions = unittest.TestCase('__init__')
TestParameters = configparser.ConfigParser()

""" below lines calls fx30 sierra router and gets newly set IP address details"""
test = Fx30()
Fx30.login(self=test)
pic6_eth1_ipaddress, pic6_eth1_subnetmask, gateway_ip, gateway_mask, dns1, dns2 = Fx30.network_settings(self=test)
Fx30.network_status(self=test)
print(pic6_eth1_ipaddress, pic6_eth1_subnetmask, gateway_ip, gateway_mask, dns1, dns2)
Fx30.close_browser(self=test)
time.sleep(10)


class Application_Test():

    def __init__(self, ccnhandle, virsim_handle, hmihandle):
        self.Util_ccn_handle = ccnhandle
        self.Util_VirSim_handle = virsim_handle
        self.Util_hmi_handle = hmihandle
        # self.ccn_handle = CCN.CCN_Adatper(1, 3, 2, 50, 50, 1, 239, 0,0)  # sytype, BaudRate, NoOfTries, ResTimOut, DelayRestTimeOut, ID(Destination Address), ElemNo, AlarmAck, BusNo
        # self.ccn_handle.setDestination(220, 0, 1, 0, 4)  # sourceAddr, SourceBus, destAddr, destBus, forcelevel

    def Eath0_IP(self):
        PIC6.ss_rest_write("PLTSP_set_eth0_ip", "169.254.1.1")  # writing Eth0 IP Address
        PIC6.ss_rest_write("PLTSP_set_eth0_nmask", "255.255.0.0")  # Writing Eth0 Subnet Mask Address
        PIC6.ss_rest_write("PLT_set_eth0_aply_dn", "1")  # Click on Save Button
        Status = PIC6.ss_rest_read("PLTSP_set_eth0_stat")  # Read the IP Status of IP and Subnet Mask Saving
        if Status == "0":
            print("ETH0 IP & Subnet Mask Address Updated Successfully(IP Address: 169.254.1.1  SubnetMask:255.255.0.0)")
        else:
            print("ETH0 IP & Subnet Mask Address Updating is Failed")
        # Gateway
        PIC6.ss_rest_write("PLTSP_set_gw1_aply_dn", "2")  # Click on Delete
        time.sleep(3)
        PIC6.ss_rest_write("PLTSP_set_gw1", "192.168.1.2")  # Writing Gateway 1 IP 169.254.1.3
        PIC6.ss_rest_write("PLTSP_set_gw1_mask", "0.0.0.0/0")  # Writing GW 1 Dest/Mask Address
        PIC6.ss_rest_write("PLTSP_set_gw1_aply_dn", "1")  # Click on Apply
        Status = PIC6.ss_rest_read("PLTSP_set_gw1_stat")  # Read the Status of Gateway
        if Status == "0":  # O for Applied Successful 9 For Already Gateway Exists
            print("Eath0 Gateway Address Updated Successfully(Gateway: 192.168.1.2  Dest/Mask:0.0.0.0/0)")
        elif Status == "5":
            print("Invalid Gateway Mask")
            print("Eath0 Gateway Address Updating is Failed")
        elif Status == "9":
            print("Gateway Exists")
            print("Eath0 Gateway Address Updated Successfully")
        elif Status == "7":
            print("Invalid Argument To Route Command")
            print("Eath0 Gateway Address Updating is Failed")
        else:
            print("Gateway is not update correctly")

    def Eath1_IP(self):
        time.sleep(10)
        PIC6.ss_rest_write("PLTSP_set_eth1_ip", pic6_eth1_ipaddress)  # Writing Eth 1 IP Address
        print(pic6_eth1_ipaddress)
        PIC6.ss_rest_write("PLTSP_set_eth1_nmask", pic6_eth1_subnetmask)  # Writing Eth 1 IP Address
        print(pic6_eth1_subnetmask)
        PIC6.ss_rest_write("PLT_set_eth1_aply_dn", "1")  # Click on Save Button
        Status = PIC6.ss_rest_read("PLTSP_set_eth1_stat")  # Read the Status of IP Status
        if Status == "0":
            print(
                "ETH1 IP & Subnet Mask Address Updated Successfully(IP Address: 192.168.1.10  Subnet Mask:255.255.0.0)")
        else:
            print("ETH1 IP & Subnet Mask Address Updating is Failed")
        # Gateway
        PIC6.ss_rest_write("PLTSP_set_gw2_aply_dn", "2")  # Click on Delete
        time.sleep(5)
        PIC6.ss_rest_write("PLTSP_set_gw2_aply_dn", "2")
        time.sleep(5)
        PIC6.ss_rest_write("PLTSP_set_gw2", gateway_ip)  # Writing Gateway 2 IP
        print(gateway_ip)
        PIC6.ss_rest_write("PLTSP_set_gw2_mask", gateway_mask)  # Writing GW2 Dest/Mask Address
        print(gateway_mask)
        PIC6.ss_rest_write("PLTSP_set_gw2_aply_dn", "1")  # Click on Apply
        time.sleep(10)
        Status = PIC6.ss_rest_read("PLTSP_set_gw2_stat")  # Read The Status of Gateway
        print(Status)
        if Status == "0":  # O for Applyed Successsfull 9 For Already Gateway Exists
            print("Eath1 Gateway Address Updated Successfully(Gateway: 192.168.1.2  Dest/Mask:0.0.0.0/0)")
        elif Status == "5":
            print("Invalid Gateway Mask")
            print("Eath1 Gateway Address Updating is Failed")
        elif Status == "9":
            print("Gateway Exists")
            print("Eath0 Gateway Address Updated Successfully")
        elif Status == "7":
            print("Invalid Argument To Route Command")
            print("Eath1 Gateway Address Updating is Failed")
        else:
            print("Gateway is not setting correctly ")

    def DNS_Server(self):
        time.sleep(10)
        # DSN Server
        print(dns1,"        ", dns2, ":DNS IPs")
        PIC6.ss_rest_write("PLTSP_set_dnsip1", dns1)
        PIC6.ss_rest_write("PLTSP_set_dnsip2",dns2)
        PIC6.ss_rest_write("PLTSP_dns_aply_dn", "1")
        Status = PIC6.ss_rest_read("PLTSP_dns_stat")
        if Status == "0":
            print("DNS Server Address Updated Successfully(DNS1 :192.168.1.2   DNS2: 192.168.1.2)")
        else:
            print("DNS Server Address Updating is Failed")

    def Network_Config(self):
        # Cloud Test
        print("Performing Cloud Test ********:")
        PIC6.ss_rest_write("PLTSP_nw_cloud_tst_tout", "5")  # Writing Time out Time
        PIC6.ss_rest_write("PLTSP_nw_cloud_tst", "1")  # Click on Cloud Test
        time.sleep(30)
        Status = PIC6.ss_rest_read("PLTSP_nw_cloud_tst_sts")  # Read the Status of Cloud Test
        # print(Status)
        if Status == "1":
            print(Colour1 + "Cloud Test is Passed")
        else:
            print(Colour2 + "Cloud Test is Failed")

        # Ping Test
        print("Performing Ping Test ********: ")
        PIC6.ss_rest_write("PLTSP_nw_png_tst_ip", "google.com")  # Write Server Address
        PIC6.ss_rest_write("PLTSP_nw_png_tst_if", "2")  # Select the Inter face  2 For Eath:1
        PIC6.ss_rest_write("PLTSP_nw_png_tst", "1")  # Click on Ping Test
        time.sleep(30)
        Status = PIC6.ss_rest_read("PLTSP_nw_png_tst_sts")  # Read the Status of Ping Test
        if Status == "1":
            print(Colour1 + "Ping Test is Passed")
        else:
            print(Colour2 + "Ping Test Is Failed")

        # IOT Certificate Checking
        Status = PIC6.ss_rest_read("PLTSP_nw_iot_cert_exist")
        # print(Status)
        if Status != "0":
            print(Colour1 + "IOT Certificate is Present")
        else:
            print(Colour2 + "IOT Certificate is Not Present")

    def CCN_Config(self):
        PIC6.ss_rest_write("CTRLID_CCN_ADDRESS", "1")
        print("CCN Address is set as :" + PIC6.ss_rest_read("CTRLID_CCN_ADDRESS"))
        PIC6.ss_rest_write("CTRLID_CCN_BUS", "0")
        print("CCN BUS is set as :" + PIC6.ss_rest_read("CTRLID_CCN_BUS"))
        PIC6.ss_rest_write("CTRLID_CCN_BAUD_PRI", "38400")
        print("CCN Baudrate is set as :" + PIC6.ss_rest_read("CTRLID_CCN_BAUD_PRI"))
        print(" CCN Configuration Completed")

    def ethernet(self): # Planing to remove (Coordinate base)
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
        # Ethernet 0 Configuration Change *************************************************(Working)
        print("Clicking on Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking on Lock Button")
        A.click(640, 24)  # Click on lock
        print("Clicking on Factory Login button")
        A.click(213, 279)  # Click on Factory Login
        print("clicking on Scanner logo")
        A.click(35, 444)  # Click on Scaner button
        print("Clicking on Login button ")
        A.click(619, 353)  # Click on Login
        print("Entering Password")
        A.Write_Field("gh9vxku7")  # Entering Password
        print("Clicking Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking Main Menu ")
        A.click(156, 33)  # Click Operation on Main Menu
        print("Clicking Down Arrow")
        A.click(776, 455)  # Click Operation on Down Navigation Arrow
        print("Clicking Cofiguration menu icon")
        A.click(137, 112)  # Click Operation on Configuration Menu
        print("Clicking HMI Configuration Icon")
        A.click(144, 100)  # Click Operation on HMI Configuration
        print("Clicking ETH-0 Icon")
        A.click(136, 108)  # Click Operation on Ethernet-0 icon
        print("Clicking interface box")
        A.click(510, 90)  # Click interface eth0
        print("selecting  Static on selection")
        A.click(426, 232)  # For Static Selection
        print("Clicking Configuration Button")
        A.click(419, 456)  # Click Operation on Configure button
        print("Clicking on IP Address Block")
        A.click(527, 78)  # Click Operation on IP Address Block
        print("Clearing IP Address Field")
        A.Field_Clear(16)  # Clear previous IP Address
        print("Entering IP Address")
        A.Write_Field("169.254.1.1")  # Enter IP Address
        # A.click(583,350)  # Click Done in keypad
        print("Clicking on Subnet Mask Block")
        A.click(527, 113)  # Click on Subnet Mask
        print("Clearing Subnet Mask address")
        A.Field_Clear(16)  # Clear previous subnet mask
        print("Entering Subnet Mask Address")
        A.Write_Field("255.255.0.0")  # Enter Subnet Mask Address
        # A.click(583,350) # Click Done in keypad
        print("Clicking on Save Button")
        A.click(687, 205)  # Click on Save Button
        print("Clicking Gateway Block")
        A.click(608, 292)  # Click on Gateway block
        print("Clearing previous Gateway...")
        A.Field_Clear(16)  # Clear Previous Data
        print("Entering gateway address")
        A.Write_Field("192.168.100.1")  # Enter Gate Way Address
        print("Clicking Dest/Mask Block")
        A.click(608, 329)  # Click on GW1 Dest/Mask block
        print("Clearing Previous Dest/Mask Way Address ")
        A.Field_Clear(16)  # Clear Previous Data
        print("Entering Dest/Mask Way Address")
        A.Write_Field("192.168.0.0/16")  # Enter GW1 Dest/Mask Way Address
        print("Clicking on Not apply Button")
        A.click(419, 382)  # Click on Not Apply Button
        print("Clicking on Apply option")
        A.click(398, 247)  # Click on  Apply Option
        print("Clicking Down Navigation Arrow")
        A.click(779, 449)  # Click on Down Navigation Arrow
        print("Clicking DNS IP Config Button")
        A.click(409, 221)  # Click on DNS IP Config Button
        print("Clicking DSN1 server Block")
        A.click(595, 123)  # Click in DSN 1 Server Block
        print("Clearing previous DSN1 address")
        A.Field_Clear(16)  # Clear previous DSN 1 Address
        print("Entering DSN 1 Server Address")
        A.Write_Field("0.0.0.0")  # Enter DSN 1 Server Address
        print("Clicking DSN2 server Block")
        A.click(609, 164)  # Click in DSN 2 Server Block
        print("Clearing previous DSN2 address")
        A.Field_Clear(16)  # Clear previous DSN 2 Address
        print("Entering DSN 1 Server Address")
        A.Write_Field("0.0.0.0")  # Enter DSN 2 Server Address
        print("Clicking Save Button")
        A.click(646, 216)  # Click on Save Button
        print("Clicking back button to navigate to HMI Configuration Page")
        A.click(99, 26)  # Click on Back Button
        A.click(99, 26)  # Click on Back Button
        A.click(99, 26)  # Click on Back Button
        A.click(99, 26)  # Click on Back Button
        # # Ethernet 1 Configuration Change *************************************************(working)
        print("CLicking Eth1:Icon")
        A.click(396, 122)  # Click Operation on Ethernet-1 icon
        print("Clicking interface Block")
        A.click(510, 90)  # Click interface eth1
        print("Clicking on Satatic option")
        A.click(426, 232)  # For Static Selection
        print("Clicking Configuration Button")
        A.click(419, 456)  # Click Operation on Configure button
        print("Clicking Ip Address Block")
        A.click(527, 78)  # Click Operation on IP Address Block
        print("Clearing Previous IP Address")
        A.Field_Clear(16)  # Clear previous IP Address
        print("Entering IP Address")
        A.Write_Field("192.160.15.100")  # Enter IP Address
        # A.click(583,350) # Click Done in keypad
        print("Clicking Subnet Mask Block")
        A.click(527, 113)  # Click on Subnet Mask
        print("Clearing previous Subnet mask")
        A.Field_Clear(16)  # Clear previous Subnet mask
        print("Entering Subnet Mask Address")
        A.Write_Field("255.255.255.0")  # Enter Subnet Mask Address
        # A.click(583,350) # Click Done in keypad
        print("Clicking Save Button")
        A.click(695, 210)  # Click on Save Button
        print("Clicking Gateway Block")
        A.click(645, 289)  # Click on Gateway block
        print("Clearing Previous Gateway Address")
        A.Field_Clear(16)  # Clear Previous Data
        print("Entering Gateway Address")
        A.Write_Field("192.168.100.1")  # Enter Gate Way Address
        print("Clicking GW1 Desk/Mask Block")
        A.click(662, 334)  # Click on GW1 Dest/Mask block
        print("Clearing Prevoius Desk/Mask Data")
        A.Field_Clear(16)  # Clear Previous Data
        print("Entering Dest/Mask Address")
        A.Write_Field("192.168.0.0/16")  # Enter GW1 Dest/Mask Way Address
        print("Clicking Not Apply Box")
        A.click(388, 381)  # Click on Not Apply Button
        print("Selecting Apply Button ")
        A.click(424, 252)  # Click on  Apply Option
        print("Clicking Down Arrow Button")
        A.click(778, 460)  # Click on Down Navigation Arrow
        print("Clicking DSN configuration Icon")
        A.click(409, 221)  # Click on DNS IP Config Button
        print("Clicking DSN 1 Server Block")
        A.click(595, 123)  # Click in DSN 1 Server Block
        print("Clearing previous DSN 1 Server data")
        A.Field_Clear(16)  # Clear previous DSN 1 Address
        print("Entering DSN 1 Server Address")
        A.Write_Field("0.0.0.0")  # Enter DSN 1 Server Address
        print("Clicking DSN 2 Server Block")
        A.click(609, 164)  # Click in DSN 2 Server Block
        print("Clearing previous DSN 2 Server data")
        A.Field_Clear(16)  # Clear previous DSN 2 Address
        print("Clicking DSN 2 Server Block")
        A.Write_Field("0.0.0.0")  # Enter DSN 2 Server Address
        print("Clicking Save Button")
        A.click(656, 228)  # Click on Save Button
        # Network Diagnostics
        print("Clicking Back Button to navigate Network Diagnostics Icon")  # ************************(Working)
        A.click(99, 26)  # Click on Back Button
        A.click(99, 26)  # Click on Back Button
        A.click(99, 26)  # Click on Back Button
        A.click(99, 26)  # Click on Back Button
        A.click(776, 461)  # Click on Down Arrow
        print("Clicking Network Diagnostics icon ")
        A.click(136, 255)  # Click on Network Diagnostics icon
        print("Clicking Server Address Block")
        A.click(593, 198)  # Click on Server Address block
        print("Clearing previous Server Address ")
        A.Field_Clear(16)  # Clear previous Server Address
        print("Entering Server Address")
        A.Write_Field("google.com")  # Enter Server Address
        print("Clicking Interface Block")
        A.click(505, 246)  # Click on Interface block
        print("Selecting WLAN 0")
        A.click(405, 211)  # Click on Wlan0
        print("Clicking Run Cloud Test")
        A.click(410, 448)  # Click on Run Cloud Test
        print("Clicking Run Ping Test")
        A.click(435, 295)  # Click on Run Ping Test
        print("Clicking home Button")
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()

    # Quick Test Table Operations ***************************************************    #

    def quick_test(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
        '''
        # print("Clicking Home Button")
        # A.click(37, 37)  # Click Operation on home Button
        # print("Clicking Lock Button")
        # A.click(640, 24)  # Click on lock
        # print("Clicking Factory Login Button")
        # A.click(213,279)  # Click on Factory Login
        # print("Clicking Scanner Button ")
        # A.click(35,444)   # Click on Scaner button
        # print("Clicking Login Box")
        # A.click(619,353)  # Click on Login
        # print("Entering Password")
        # TestParameters.read("C:\\End to End\\Python3_app\\Utilities\\Test_Parameters.ini")
        # password = TestParameters.get("TEST_PARAMETERS", "factory")
        # A.Write_Field(password)  # Entering Password
        '''

        print("Clicking  Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking Main Menu Button")
        A.click(156, 33)  # Click Operation on Main Menu
        print("Clicking Down Navigation Arrow")
        A.click(776, 455)  # Click Operation on Down Navigation Arrow
        print("Clicking Quick Test Table Icon")
        A.click(402, 114)  # Click On Quick Test Table Icon
        # print("Quick test 1 st page operations Starting")
        A.disable_set(504, 124)
        time.sleep(5)
        PIC6.ss_rest_write("LOCAL_OPERTYP", "0")
        time.sleep(60)

        failStr = ''
        try:
            print("Test 1 : Checking PIC 6 is in Local Off Mode or Not")
            PIC6.ss_rest_read_check("GENUNIT_CTRL_TYP", "0")
            PIC6.ss_rest_read("")
            PIC6.ss_rest_read_check("GENUNIT_STATUS", "Off     ")
            print("PIC6  in Local Off Mode")
        except Exception as e:
            a = PIC6.ss_rest_read("GENUNIT_CTRL_TYP")
            b = PIC6.ss_rest_read("GENUNIT_STATUS")
            if a==0:
                print("PIC6 is in Local"+ b+ "Mode")
            if a == 1:
                print("PIC6 is in Local Schedule" + b + "Mode")
            elif a == 2:
                print("PIC6 is in Network" + b + "Mode")
            elif a == 3:
                print("PIC6 is in Remote" + b + "Mode")
            elif a == 4:
                print("PIC6 is in Master" + b + "Mode")
            else:
                print("PIC6 is in Unknown mode")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 2 : Enabling Quick Test")
            A.enable_set(504, 124)  # Click on EnableQuick Test
            PIC6.ss_rest_read_check("QCK_TEST_QCK_TEST", "1")
            print("Quick Test is Enabled")
        except Exception as e:
            print("Quick Test is not Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        # V = PIC6.ss_rest_read("GENUNIT_STATUS")
        # print(V)
        try:
            print("Test 3 : Checking PIC 6 is in Local Test Mode or Not")
            PIC6.ss_rest_read_check("GENUNIT_CTRL_TYP", "0")
            time.sleep(10)
        except Exception as e:
            print("Pic 6 is not in Local Mode")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            PIC6.ss_rest_read_check("GENUNIT_STATUS", "Test    ")
            print(" Now PIC6 in Local Test Mode")
        except Exception as e:
            print("Pic 6 is not in Test Mode")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 4 : EXV Position verification")
            A.click(429, 163)  # Click on Circuit A EXV Position box
            # print("Entering EXV Position Value")
            A.quick_Test_write("100")  # Write data in to EXV Position
            time.sleep(30)
            PIC6.ss_rest_read_check("EXV_CTRL_EXV_A", "100")
        except Exception as e:
            print("EXV_A value verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            PIC6.ss_rest_read_check("EXV_CTRL_EXV_STPA", "3810")
            print("EXV Position status verified")
        except Exception as e:
            print("EXV_A Step value verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 5 : Enabling Oil Solenoid ")
            A.enable_set(500, 207)  # Circuit A Oil Solenoid enable
            PIC6.ss_rest_read_check("TBLSHT_OIL_SL_A", "1")
            print("Oil Solenoid is Enabled")
        except Exception as e:
            print("Oil Solenoid verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 6: EXV Eco Position Cri A ")
            A.click(408, 245)  # EXV Eco Position Cri A:
            print("Entering EXV Eco Position Cri A value ")
            A.quick_Test_write("100")  # Write data in to EXV Eco Position Cri A
            time.sleep(30)
            PIC6.ss_rest_read_check("ECO_CTRL_eco_a", "100.000008")
            PIC6.ss_rest_read_check("ECO_CTRL_eco_stpa", "2625")
            print("EXV Eco Position Cri A test is passed")
        except Exception as e:
            print("EXV Eco Position Cri A verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 7: Enabling Oil Heater Circuit A")
            A.enable_set(503, 283)  # Oil Heater Circuit A:
            PIC6.ss_rest_read_check("OUTPUTS_OIL_HT_A", "1")
            print("Oil Heater Circuit A is Enabled")
        except Exception as e:
            print("Oil Heater Circuit A Test is failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 8:Capacity Cri A Output")
            A.click(431, 318)  # Capacity Cri A Output:
            print("Entering value in to Capacity Cri A Output")
            A.quick_Test_write("100")  # Write data in to Capacity Cri A Output
            time.sleep(30)
            PIC6.ss_rest_read_check("TBLSHT_CAPT010A", "10")
            print("Capacity Cri A Output test is passed")
        except Exception as e:
            print("Capacity Cri A Output test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 9: Enabling Comp A Running Output")
            A.enable_set(504, 362)  # Comp A Running Output enable
            PIC6.ss_rest_read_check("OUTPUTS_CP_A", "1")
            print("Comp A Running Output Enabled")
        except Exception as e:
            print("Comp A Running Output verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 10: Enabling Isolation Valve State A open ")
            A.enable_set(503, 407)  # Isolation Valve State A open
            PIC6.ss_rest_read_check("OUTPUTS_ISO_OP_A", "1")
            print("Isolation Valve State A open Enabled")
        except Exception as e:
            print("Isolation Valve State A open Test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        A.click(780, 452)  # Click on Down Arrow
        # Page 2 *************************************************************************
        try:
            print("Test 11: Enabling Circuit A VI ")
            A.enable_set(498, 83)  # Circuit A VI enable
            PIC6.ss_rest_read_check("OUTPUTS_VI_A", "1")
            print("Circuit A VI Enabled")
        except Exception as e:
            print("Circuit A VI verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        #  FANS ***********************************************************************
        ECM = PIC6.ss_rest_read("FACTORY_ECM_fans")
        if ECM == "0":
            try:
                print("Test:12 VariFan Speed A ")
                A.click(404, 124)  # click on VariFan Speed A box
                print("Entering Value to VariFan Speed A ")
                A.quick_Test_write("100")  # Writing value to VariFan Speed A
                time.sleep(30)
                PIC6.ss_rest_read_check("OUTPUTS_VFAN_A", "0")
                print("VariFan Speed At test is passed")
            except Exception as e:
                print("VariFan Speed A test verification failed")
                failStr = failStr + str(e.args[0]) + '.\n'
        else:
            print("ECM Fan is Enabled so VariFan Speed test is not Performed")

        try:
            print(" Test 13: Circuit B EXV Position")
            A.click(398, 162)  # click on Circuit B EXV Position box
            print("Entering values to Circuit B EXV Position")
            A.quick_Test_write("100")  # Write the value to Circuit B EXV Position
            time.sleep(30)
            PIC6.ss_rest_read_check("EXV_CTRL_EXV_B", "100")
            PIC6.ss_rest_read_check("EXV_CTRL_EXV_STPB", "3810")
            print("Circuit B EXV Position test is passed")
        except Exception as e:
            print("Circuit B EXV Position test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 14: Enabling Circuit B Oil Solenoid ")
            A.enable_set(501, 200)  # Circuit B Oil Solenoid enable
            PIC6.ss_rest_read_check("TBLSHT_OIL_SL_B", "1")
            print("Circuit B Oil Solenoid is Enabled")
        except Exception as e:
            print("Circuit B Oil Solenoid verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 15: EXV Eco Position Cri B Test")
            A.click(414, 236)  # Click on EXV Eco Position Cri B box
            print("writing values to EXV Eco Position Cri B")
            A.quick_Test_write("100")  # Write value to EXV Eco Position Cri B
            time.sleep(30)
            PIC6.ss_rest_read_check("ECO_CTRL_eco_b", "100.000008")
            PIC6.ss_rest_read_check("ECO_CTRL_eco_stpb", "2625")
            print("EXV Eco Position Cri B test is passed")
        except Exception as e:
            print("EXV Eco Position Cri A test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:16 Enabling Oil Heater Circuit B ")
            A.enable_set(501, 285)  # Oil Heater Circuit B enable
            PIC6.ss_rest_read_check("OUTPUTS_OIL_HT_B", "1")
            print("Oil Heater Circuit B is Enabled")
        except Exception as e:
            print("Oil Heater Circuit B verification  failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:17  Capacity Cir B Output ")
            A.click(416, 323)  # click on Capacity CirB Output box
            print("writing vale to Capacity Cir B Output")
            A.quick_Test_write("100")  # Write value to Capacity CirB Output box
            time.sleep(30)
            PIC6.ss_rest_read_check("TBLSHT_CAPT010B", "10")
            print("Capacity Cri B Output test is passed")
        except Exception as e:
            print("Capacity Cri B Output test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:18 Enabling Comp B Running Output")
            A.enable_set(499, 363)  # Comp B Running Output enable
            PIC6.ss_rest_read_check("OUTPUTS_CP_B", "1")
            print("Comp B Running Output Enabled")
        except Exception as e:
            print("Comp B Running Output verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:19 Enabling Isolation Valve State B")
            A.enable_set(505, 399)  # Isolation Valve State B enable
            PIC6.ss_rest_read_check("OUTPUTS_ISO_OP_B", "1")
            print("Isolation Valve State B open Enabled")
        except Exception as e:
            print("Isolation Valve State B open verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        A.click(780, 452)  # Click on Down Arrow
        # Page 3 *************************************************************************
        try:
            print("Test:20 Enabling Circuit B VI")
            A.enable_set(501, 81)  # Circuit B VI enable
            PIC6.ss_rest_read_check("OUTPUTS_VI_B", "1")
            print("Circuit B VI Enabled")
        except Exception as e:
            print("Circuit B VI verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        ECM = PIC6.ss_rest_read("FACTORY_ECM_fans")
        if ECM == "0":
            try:
                print("Test: 21 Vari Fan Speed B")
                A.click(411, 121)  # click on VariFan Speed B box
                print("writing value to Vari Fan Speed B")
                A.quick_Test_write("100")  # Write value to VariFan Speed B
                time.sleep(30)
                PIC6.ss_rest_read_check("OUTPUTS_VFAN_B", "0")
                print("VariFan Speed B test is passed")
            except Exception as e:
                print("VariFan Speed B test verification failed")
                failStr = failStr + str(e.args[0]) + '.\n'
        else:
            print(" ECM Fan is Enabled so Vari Fan Speed test is not performed")

        try:
            print("Test:22 Enabling Evaporator Heater ")
            A.enable_set(508, 160)  # Evaporator Heater enable
            PIC6.ss_rest_read_check("OUTPUTS_EVAP_HEATER", "1")
            print("Evaporator Heater Enabled Successfully")
        except Exception as e:
            print("Evaporator Heater verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test :23 Evaporator Pump1 ")
            A.click(412, 201)  # click on Evaporator Pump1 box
            print("Entering value to Evaporator Pump 1")
            A.quick_Test_write("1")  # Write value to Evaporator Pump1
            time.sleep(1)
            PIC6.ss_rest_read_check("PUMPSTAT_CPUMP_1", "1")
            # print("Evaorator Pump1 is On")
            time.sleep(10)
            PIC6.ss_rest_read_check("PUMPSTAT_CPUMP_1", "0")
            # print("Evaorator Pump1 is Off")
            print("Evaporator Pump 1 test is passed")
        except Exception as e:
            print("Evaporator pump 1 test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:24 Evaporator Pump2 ")
            A.click(400, 238)  # click on Evaporator Pump2 box
            print("Writing Value to Evaporator Pump 2")
            A.quick_Test_write("1")  # Write value to Evaporator
            time.sleep(1)
            PIC6.ss_rest_read_check("PUMPSTAT_CPUMP_2", "1")
            # print("Evaorator Pump2 is On")
            time.sleep(10)
            PIC6.ss_rest_read_check("PUMPSTAT_CPUMP_2", "0")
            # print("Evaorator Pump2 is Off")
            print("Evaporator Pump 2 test is passed")
        except Exception as e:
            print("Evaporator pump 2 test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:25 Enabling Alarm Relay Status")
            A.enable_set(501, 283)  # Alarm Relay Status enable
            PIC6.ss_rest_read_check("OUTPUTS_ALARM", "1")
            print("Alarm Relay Status Enabled Successfully")
        except Exception as e:
            print("Alarm Relay Status verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:26 Enabling Shutdown Status")
            A.enable_set(505, 320)  # Shutdown Relay Status enable
            PIC6.ss_rest_read_check("OUTPUTS_SHUTDOWN", "1")
            print("Shutdown Status Enabled Successfully")
        except Exception as e:
            print("Shutdown Status Test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:27 Enabling Running Relay Status")
            A.enable_set(507, 365)  # Running Relay Status enable
            PIC6.ss_rest_read_check("OUTPUTS_RUNNING", "1")
            print("Running Relay Status Enabled Successfully")
        except Exception as e:
            print("Running Relay Status Test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:28 Enabling Alert Relay Switch")
            A.enable_set(506, 401)  # Alert Relay Switch
            PIC6.ss_rest_read_check("OUTPUTS_ALERT", "1")
            print("Alert Relay Switch Enabled Successfully")
        except Exception as e:
            print("Alert Relay Switch Test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        A.click(780, 452)  # Click on Down Arrow
        # Page 4 *************************************************************************
        try:
            print("Test:29 Capacity Total Output ")
            A.click(392, 84)  # Click on Capacity Total Output box
            print("Entering value to Capacity Total Output")
            A.quick_Test_write("100")  # Write value to Capacity Total Output
            PIC6.ss_rest_read_check("OUTPUTS_CAPT_010", "10")
            print("Capacity Total Output test is passed")
        except Exception as e:
            print("Capacity Total Output test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:30 Enabling drive heater A ")
            A.enable_set(501, 123)  # Com drive heater A enable
            PIC6.ss_rest_read_check("VLT_DRV_drv_HTRa", "1")
            print("drive heater A Enabled Successfully")
        except Exception as e:
            print("drive heater A Test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:31 Enabling drive heater B ")
            A.enable_set(502, 163)  # Com drive heater B enable
            PIC6.ss_rest_read_check("VLT_DRV_drv_HTRb", "1")
            print("drive heater B Enabled Successfully")
        except Exception as e:
            print("drive heater B Test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        ECM = PIC6.ss_rest_read("FACTORY_ECM_fans")
        if ECM == "0":
            try:
                print("Test:32 Fan Contactors Related A ")
                print("Enabling Fan Contactor 1A ")
                A.enable_set(501, 206)  # Fan Contactor 1A enable
                print("Enabling Fan Contactor 2A ")
                A.enable_set(499, 249)  # Fan Contactor 2A enable
                print("Enabling Fan Contactor 3A ")
                A.enable_set(503, 291)  # Fan Contactor 3A enable
                print("Enabling Fan Contactor 4A ")
                A.enable_set(505, 323)  # Fan Contactor 4A enable
                print("Enabling Fan Contactor 5A ")
                A.enable_set(500, 363)  # Fan Contactor 5A enable
                print("Enabling Fan Contactor 6A ")
                A.enable_set(500, 407)  # Fan Contactor 6A enable
                # print("Clicking Down Navigation Arrow")
                A.click(780, 452)  # Click on Down Arrow
                # Page 5 *************************************************************************
                # print("Quick test 5th page operations starting")
                print("Enabling Fan Contactor 7A ")
                A.enable_set(497, 80)  # Fan Contactor 7A enable
                print("Enabling Fan Contactor 8A ")
                A.enable_set(501, 120)  # Fan Contactor 8A enable
                PIC6.ss_rest_read_check("OUTPUTS_FCA1", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCA2", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCA3", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCA4", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCA5", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCA6", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCA7", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCA8", "1")
                # print("Fan Contactor 1A to 8A are in On Mode")
                print("Fan Contactors Related A Test is Passed")
            except Exception as e:
                print("Fan Contactors Related A Test verification failed")
                failStr = failStr + str(e.args[0]) + '.\n'

            try:
                print("Test:33 Fan Contactors Related B ")
                print("Enabling Fan Contactor 1B ")
                A.enable_set(506, 161)  # Fan Contactor 1B enable
                print("Enabling Fan Contactor 2B ")
                A.enable_set(505, 203)  # Fan Contactor 2B enable
                print("Enabling Fan Contactor 3B ")
                A.enable_set(507, 246)  # Fan Contactor 3B enable
                print("Enabling Fan Contactor 4B ")
                A.enable_set(504, 284)  # Fan Contactor 4B enable
                print("Enabling Fan Contactor 5B ")
                A.enable_set(504, 323)  # Fan Contactor 5B enable
                print("Enabling Fan Contactor 6B ")
                A.enable_set(505, 363)  # Fan Contactor 6B enable
                print("Enabling Fan Contactor 7B ")
                A.enable_set(506, 402)  # Fan Contactor 7B enable
                # print("Clicking Down Navigation Arrow")
                A.click(780, 452)  # Click on Down Arrow

                # Page 6 *************************************************************************
                # print("Quick test 6th page operations strting")
                print("Enabling Fan Contactor 8B ")
                A.enable_set(503, 80)  # Fan Connector 8B enable
                PIC6.ss_rest_read_check("OUTPUTS_FCB1", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCB2", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCB3", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCB4", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCB5", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCB6", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCB7", "1")
                PIC6.ss_rest_read_check("OUTPUTS_FCB8", "1")
                # print("Fan Contactor 1B to 8B are in On Mode")
                print("Fan Contactors Related B Test is Passed")
            except Exception as e:
                print("Fan Contactors Related B Test verification failed")
                failStr = failStr + str(e.args[0]) + '.\n'
        else:
            print("ECM Fan Is Enable  so Fan Contactors Operation Can Be Performed")

        try:
            print("Test:34 Enabling Comp.HW Enable A ")
            A.enable_set(504, 125)  # Comp.HW Enable A enable
            PIC6.ss_rest_read_check("OUTPUTS_VFD_EN_A", "1")
            print("Comp.HW Enable A is Enabled")
        except Exception as e:
            print("Comp.HW Enable A Test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:35 Enabling Comp.HW Enable B ")
            A.enable_set(502, 163)  # Comp.HW Enable B enable
            PIC6.ss_rest_read_check("OUTPUTS_VFD_EN_B", "1")
            print("Comp.HW Enable B is Enabled")
        except Exception as e:
            print("Comp.HW Enable B Test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:36 Enabling Control Box Heater ")
            A.enable_set(500, 201)  # Control Box Heater enable
            PIC6.ss_rest_read_check("OUTPUTS_BOX_HTR", "1")
            print("Control Box Heater is Enabled")
        except Exception as e:
            print("Control Box Heater Test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:37 All ECM Fan Spd CIRA ")
            A.click(401, 244)  # Click on All ECM Fan spd CIRA box
            print("writing value to All ECM Fan Spd CIRA ")
            A.quick_Test_write("100")  # Write value to All ECM Fan spd CIRA box
            PIC6.ss_rest_read_check("ECM_FAN1_SPEED_PERCENT", "100")
            print("All ECM Fan Spd CIRA test is passed")
        except Exception as e:
            print("All ECM Fan Spd CIRA test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:38 All ECM Fan Spd CIRB ")
            A.click(392, 282)  # Click on All ECM Fan spd CIRB box
            print("writing value to All ECM Fan Spd CIRB ")
            A.quick_Test_write("100")  # Write value to All ECM Fan spd CIRB box
            PIC6.ss_rest_read_check("ECM_FAN2_SPEED_PERCENT", "100")
            print("All ECM Fan Spd CIRB test is passed")
        except Exception as e:
            print("All ECM Fan Spd CIRB test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        A.click(99, 26)  # Click on Back Button
        A.click(402, 114)  # Click On Quick Test Table Icon
        A.disable_set(504, 124)
        print("Quick test is finished")
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()

        if failStr != "":
            raise Exception(failStr)

    def BACnet_Config(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
        print("Clicking Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking Main Menu ")
        A.click(156, 33)  # Click Operation on Main Menu
        print("Clicking Down Arrow")
        A.click(776, 455)  # Click Operation on Down Navigation Arrow
        print("Clicking Cofiguration menu icon")
        A.click(137, 112)  # Click Operation on Configuration Menu
        print("Clicking HMI Configuration Icon")
        A.click(144, 100)  # Click Operation on HMI Configuration
        print("Clicking BACnet ICON")
        A.click(148, 237)  # Click on Bacnet ICon
        print("Clicking on Bacnet Data Link Layer")
        A.click(634, 234)
        print("Clicking On Bacnet IP Option")
        A.click(425, 257)
        print("Click on Save Button")
        A.click(38, 460)
        print("BACnet Configuration Completed")
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()

        failStr = ''
        # Metric Units setting
        try:
            PIC6.ss_rest_write("SHDW_BACNET_bacunit", "1")
            PIC6.ss_rest_read_check("SHDW_BACNET_bacunit", "1")
            print("Metric Units is changed successfully")
        except Exception as e:
            print("Metric Units Verification Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        # Network settings
        try:
            PIC6.ss_rest_write("SHDW_BACNET_network", "1602")
            PIC6.ss_rest_read_check("SHDW_BACNET_network", "1602")
            print("Network setting is changed successfully")
        except Exception as e:
            print("Network setting Verification Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        # Identifier settings
        try:
            PIC6.ss_rest_write("SHDW_BACNET_ident", "1600002")
            PIC6.ss_rest_read_check("SHDW_BACNET_ident", "1600002")
            print("Identifier settings is changed successfully")
        except Exception as e:
            print("Identifier settings Verification Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        # BACnet Mgmt Device settings
        try:
            PIC6.ss_rest_write("SHDW_BACNET_bbmd", "0")
            PIC6.ss_rest_read_check("SHDW_BACNET_bbmd", "0")
            print("BACnet Mgmt Device settings is changed successfully")
        except Exception as e:
            print("BACnet Mgmt Device settings Verification Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        # BACnet Data Link Layer settings
        try:
            PIC6.ss_rest_write("SHDW_BACNET_bacdlink", "16")
            PIC6.ss_rest_read_check("SHDW_BACNET_bacdlink", "16")
            print("BACnet Data Link Layer settings is changed successfully")
        except Exception as e:
            print("BACnet Data Link Layer settings Verification Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        # MS/TP Mac Address Reading
        try:
            PIC6.ss_rest_read_check("SHDW_BACNET_mstpaddr", "1")
            print("MS/TP Mac Address Reading successfully")
        except Exception as e:
            print("MS/TP Mac Address Verification Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        # MS/TP Baud Rate
        try:
            PIC6.ss_rest_write("SHDW_BACNET_mstpbaud", "1")
            PIC6.ss_rest_read_check("SHDW_BACNET_mstpbaud", "1")
            print("MS/TP Baud Rate settings is changed successfully")
        except Exception as e:
            print("MS/TP Baud Rate settings Verification Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        # Max Masters Reading
        try:
            print("Max Masters :" + PIC6.ss_rest_read("SHDW_BACNET_maxmastr"))
        except Exception as e:
            print("Max Masters Verification Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        # MS/TP Max Info Frames
        try:
            print("MS/TP Max Info Frames:" + PIC6.ss_rest_read("SHDW_BACNET_maxmastr"))
        except Exception as e:
            print("MS/TP Max Info Frames Verification Failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)

        ''''
        # Page 1 *************************************************************************
        print("Enabling Quick Test ")
        # A.disable_set(504,124)
        A.enable_set(504, 124)  # Click on EnableQuick Test
        # A.disable_set(504,124)                                           Future need to change
        PIC6.ss_rest_read_check("QCK_TEST_QCK_TEST","1")
        print("Clicking EXV Position Box")
        A.click(429, 163)  # Click on Circuit A EXV Position box
        print("Entering EXV Position Value")
        A.quick_Test_write("20")  # Write data in to EXV Position
        print("Enabling Oil Solenoid ")
        A.enable_set(500, 207)  # Circuit A Oil Solenoid enable
        print("Clicking EXV Eco Position Cri A Box")
        A.click(408, 245)  # EXV Eco Position Cri A:
        print("Entering EXV Eco Position Cri A value ")
        A.quick_Test_write("1")  # Write data in to EXV Eco Position Cri A
        print("Enabling Oil Heater Circuit A")
        A.enable_set(503, 283)  # Oil Heater Circuit A:
        print("Clicking Capacity Cri A Output")
        A.click(431, 318)  # Capacity Cri A Output:
        print("Entering value in to Capacity Cri A Output")
        A.quick_Test_write("1")  # Write data in to Capacity Cri A Output
        print("Enabling Comp A Running Output")
        A.enable_set(504, 362)  # Comp A Running Output enable
        print("Enabling Isolation Valve State A open ")
        A.enable_set(503, 407)  # Isolation Valve State A open
        print("Clicking Down Navigation Arrow")
        A.click(780, 452)  # Click on Down Arrow

        # Page 2 *************************************************************************
        print("Quick test 2nd page operations starting")
        print("Enabling Circuit A VI ")
        A.enable_set(498, 83)  # Circuit A VI enable
        print("Clicking on VariFan Speed A Box")
        A.click(404, 124)  # click on VariFan Speed A box
        print("Entering Value to VariFan Speed A ")
        A.quick_Test_write("1")  # Writing value to VariFan Speed A
        print("Clicking Circuit B EXV Position box ")
        A.click(398, 162)  # click on Circuit B EXV Position box
        print("Entering values to Circuit B EXV Position")
        A.quick_Test_write("1")  # Write the value to Circuit B EXV Position
        print("Enabling Circuit B Oil Solenoid ")
        A.enable_set(501, 200)  # Circuit B Oil Solenoid enable
        print("Clicking EXV Eco Position Cri B box")
        A.click(414, 236)  # Click on EXV Eco Position Cri B box
        print("writing values to EXV Eco Position Cri B")
        A.quick_Test_write("1")  # Write value to EXV Eco Position Cri B
        print("Enabling Oil Heater Circuit B ")
        A.enable_set(501, 285)  # Oil Heater Circuit B enable
        print("Clicking Capacity Cir B ")
        A.click(416, 323)  # click on Capacity CirB Output box
        print("writing vale to Capacity Cir B Output")
        A.quick_Test_write("1")  # Write value to Capacity CirB Output box
        print("Enabling Comp B Running Output")
        A.enable_set(499, 363)  # Comp B Running Output enable
        print("Enabling Isolation Valve State B")
        A.enable_set(505, 399)  # Isolation Valve State B enable
        print("Clicking Down Navigation Arrow")
        A.click(780, 452)  # Click on Down Arrow

        # Page 3 *************************************************************************
        print("Quick test 3rd page operations starting")
        print("Enabling Circuit B VI")
        A.enable_set(501, 81)  # Circuit B VI enable
        print("Clicking Vari Fan Speed B Box")
        A.click(411, 121)  # click on VariFan Speed B box
        print("writing value to Vari Fan Speed B")
        A.quick_Test_write("1")  # Write value to VariFan Speed B
        print("Enabling Evaporator Heater ")
        A.enable_set(508, 160)  # Evaporator Heater enable
        print("Clicking Evaorator Pump1 Box")
        A.click(412, 201)  # click on Evaporator Pump1 box
        print("Entering value to Evaporator Pump 1")
        A.quick_Test_write("1")  # Write value to Evaporator Pump1
        print("Clicking Evaporator Pump2 Box")
        A.click(400, 238)  # click on Evaporator Pump2 box
        print("Writing Value to Evaporator Pump 2")
        A.quick_Test_write("1")  # Write value to Evaporator
        print("Enabling Alarm Relay Status")
        A.enable_set(501, 283)  # Alarm Relay Status enable
        print("Enabling Shutdown Status")
        A.enable_set(505, 320)  # Shutdown Relay Status enable
        print("Enabling Running Relay Status")
        A.enable_set(507, 365)  # Running Relay Status enable
        print("Enabling Aleart Relay Switch")
        A.enable_set(506, 401)  # Alert Relay Switch
        print("Clicking Down Navigation Arrow Button")
        A.click(780, 452)  # Click on Down Arrow

        # Page 4 *************************************************************************
        print("Quick test 4th page operations Started")
        print("Clicking Capacity Total Output Box")
        A.click(392, 84)  # Click on Capacity Total Output box
        print("Entering value to Capacity Total Output")
        A.quick_Test_write("1")  # Write value to Capacity Total Output
        print("Enabling drive heater A ")
        A.enable_set(501, 123)  # Com drive heater A enable
        print("Enabling drive heater B ")
        A.enable_set(502, 163)  # Com drive heater B enable
        print("Enabling Fan Contactor 1A ")
        A.enable_set(501, 206)  # Fan Contactor 1A enable
        print("Enabling Fan Contactor 2A ")
        A.enable_set(499, 249)  # Fan Contactor 2A enable
        print("Enabling Fan Contactor 3A ")
        A.enable_set(503, 291)  # Fan Contactor 3A enable
        print("Enabling Fan Contactor 4A ")
        A.enable_set(505, 323)  # Fan Contactor 4A enable
        print("Enabling Fan Contactor 5A ")
        A.enable_set(500, 363)  # Fan Contactor 5A enable
        print("Enabling Fan Contactor 6A ")
        A.enable_set(500, 407)  # Fan Contactor 6A enable
        print("Clicking Down Navigation Arrow")
        A.click(780, 452)  # Click on Down Arrow

        # Page 5 *************************************************************************
        print("Quick test 5th page operations starting")
        print("Enabling Fan Contactor 7A ")
        A.enable_set(497, 80)  # Fan Contactor 7A enable
        print("Enabling Fan Contactor 8A ")
        A.enable_set(501, 120)  # Fan Contactor 8A enable
        print("Enabling Fan Contactor 1B ")
        A.enable_set(506, 161)  # Fan Contactor 1B enable
        print("Enabling Fan Contactor 2B ")
        A.enable_set(505, 203)  # Fan Contactor 2B enable
        print("Enabling Fan Contactor 3B ")
        A.enable_set(507, 246)  # Fan Contactor 3B enable
        print("Enabling Fan Contactor 4B ")
        A.enable_set(504, 284)  # Fan Contactor 4B enable
        print("Enabling Fan Contactor 5B ")
        A.enable_set(504, 323)  # Fan Contactor 5B enable
        print("Enabling Fan Contactor 6B ")
        A.enable_set(505, 363)  # Fan Contactor 6B enable
        print("Enabling Fan Contactor 7B ")
        A.enable_set(506, 402)  # Fan Contactor 7B enable
        print("Clicking Down Navigation Arrow")
        A.click(780, 452)  # Click on Down Arrow

        # Page 6 *************************************************************************
        print("Quick test 6th page operations strting")
        print("Enabling Fan Contactor 8B ")
        A.enable_set(503, 80)  # Fan Connector 8B enable
        print("Enabling Comp.HW Enable A ")
        A.enable_set(504, 125)  # Comp.HW Enable A enable
        print("Enabling Comp.HW Enable B ")
        A.enable_set(502, 163)  # Comp.HW Enable B enable
        print("Enabling Control Box Heater ")
        A.enable_set(500, 201)  # Control Box Heater enable
        print("Clicking All ECM Fan Spd CIRA Box")
        A.click(401,244)  # Click on All ECM Fan spd CIRA box
        print("writing value to All ECM Fan Spd CIRA ")
        A.quick_Test_write("1")  # Write value to All ECM Fan spd CIRA box
        print("Clicking All ECM Fan Spd CIRB Box")
        A.click(392, 282)  # Click on All ECM Fan spd CIRB box
        print("writing value to All ECM Fan Spd CIRB ")
        A.quick_Test_write("1")  # Write value to All ECM Fan spd CIRB box
        print("Quick test is finished")
        # A.read_CCN_Data()
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()
        '''

    def sample(self):
        print("Hi Yogesh i am From Correct Test case")

    def lock(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
        print("Clicking Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking Lock Button")
        A.click(640, 24)  # Click on lock
        print("Clicking Factory Login Button")
        A.click(213, 279)  # Click on Factory Login
        print("Clicking Scanner Button ")
        A.click(35, 444)  # Click on Scaner button
        print("Clicking Login Box")
        A.click(619, 353)  # Click on Login
        print("Entering Password")
        TestParameters.read(dirnameutils + "\\Data\\APPLICATION\\Test_Parameters.ini")
        password = TestParameters.get("TEST_PARAMETERS", "factory")
        A.Write_Field(password)  # Entering Password
        print("Clicking  Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Unlocking Completed Successfully")
        A.close_ssh()

    def Clear_Alarm(self):
        PIC6.ss_rest_write("ALARMRST_RST_ALM","1")
        time.sleep(10)
        PIC6.ss_rest_write("ALARMRST_RST_ALM","0")
        print("Clearing Alarms Completed")
        # A.init_ssh()
        # A.cmd_ssh("login root")  # login as root
        # A.cmd_ssh("X*rD8u!6nk")  # root Password
        # A.dismiss_modal_window()
        # # Ethernet 0 Configuration Change *************************************************(Working)
        # A.click(37, 37)  # Click Operation on home Button
        # print("Clcking on Alaram Icon")
        # A.click(761, 37)
        # print("Clcking on reset Alarm")
        # A.click(132, 106)
        # print("Enabling Alaram Reset ")
        # A.enable_set(491, 77)
        # print("Clicking on Home Button")
        # A.click(37, 37)  # Click Operation on home Button
        # A.close_ssh()

    def Chiller_ON(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
        # Ethernet 0 Configuration Change *************************************************(Working)
        print("Clicking on Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking on Lock Button")
        A.click(640, 24)  # Click on lock
        print("Clicking on Factory Login button")
        A.click(213, 279)  # Click on Factory Login
        print("clicking on Scanner logo")
        A.click(35, 444)  # Click on Scaner button
        print("Clicking on Login button ")
        A.click(619, 353)  # Click on Login
        print("Entering Password")
        A.Write_Field("asqrbxex")  # Entering Password
        print("Clicking Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking on Power Icon")
        A.click(696, 22)  # Click Operation on Power Icon
        print("Clicking on Local On")
        A.click(439, 89)  # Click Operation on Local On Button
        print("Waiting for chill to reach 100 % capacity")

    def Chiller_Off(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
        # Ethernet 0 Configuration Change *************************************************(Working)
        print("Clicking on Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking on Lock Button")
        A.click(640, 24)  # Click on lock
        print("Clicking on Factory Login button")
        A.click(213, 279)  # Click on Factory Login
        print("clicking on Scanner logo")
        A.click(35, 444)  # Click on Scaner button
        print("Clicking on Login button ")
        A.click(619, 353)  # Click on Login
        print("Entering Password")
        A.Write_Field("asqrbxex")  # Entering Password
        print("Clicking Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking on Power Icon")
        A.click(696, 22)  # Click Operation on Power Icon
        print("Clicking on Chiller Stop Icon")
        A.click(423, 253)  # Stoping Chiller
        print("Clicking on Home Button")
        A.click(37, 37)  # Click Operation on home Button

    def ModbusConfig(self):
        # Modbus TCP Enable Setting(Disable)
        PIC6.ss_rest_write("MODBUS_mip_opt", "0")
        PIC6.ss_rest_read_check("MODBUS_mip_opt", "0")
        # Modbus TCP Port Number Settings(Default value 502)
        PIC6.ss_rest_write("MODBUS_port_nbr", "502")
        PIC6.ss_rest_read_check("MODBUS_port_nbr", "502")
        # Modbus IP 32 Bit reg support flag(0:NO, 1:Yes)
        PIC6.ss_rest_write("MODBUSIP_reg32bit_supt", "1")
        PIC6.ss_rest_read_check("MODBUSIP_reg32bit_supt", "1")
        # Modbus Master IP Config(0:NO, 1:Yes)
        PIC6.ss_rest_write("MODBUS_master_IP_con", "1")
        PIC6.ss_rest_read_check("MODBUS_master_IP_con", "1")
        # Modbus Swap Endian(setting Little Endian)
        PIC6.ss_rest_write("MODBUS_swap_b", "0")
        PIC6.ss_rest_read_check("MODBUS_swap_b", "0")
        # Modbus IP Communication Timeout(s)
        PIC6.ss_rest_write("MODBUS_comm_timeout", "60")
        PIC6.ss_rest_read_check("MODBUS_comm_timeout", "60")
        print("Modbus-TCP Configuration is Done Successfully ")

        # Modbus RTU Option Enabling
        PIC6.ss_rest_write("MODBUS_mrtu_opt", "1")
        PIC6.ss_rest_read_check("MODBUS_mrtu_opt", "1")
        # Modbus RTU Baudrate setting(0:9600,1:19200,2:38400)
        PIC6.ss_rest_write("MODBUS_baudrate", "1")
        PIC6.ss_rest_read_check("MODBUS_baudrate", "1")
        # Modbus RTU Parity Option (0:None, 1:Odd, 2:Even)
        PIC6.ss_rest_write("MODBUS_parity", "0")
        PIC6.ss_rest_read_check("MODBUS_parity", "0")
        # Modbus RTU Stop Bit Setting( 0:1 Bit,1: 2 Bit)
        PIC6.ss_rest_write("MODBUS_stop_bit", "0")
        PIC6.ss_rest_read_check("MODBUS_stop_bit", "0")
        # Modbus RTU 32 Bit reg support Flag (0:NO, 1:Yes)
        PIC6.ss_rest_write("MODBUSRS_reg32bit_supt", "0")
        PIC6.ss_rest_read_check("MODBUSRS_reg32bit_supt", "0")
        # Modbus Real Type(0:NO,1: Yes)
        PIC6.ss_rest_write("MODBUS_real_typ", "0")
        PIC6.ss_rest_read_check("MODBUS_real_typ", "0")
        print("Modbus-RTU Configuration is Done Successfully ")

    def SW_Version(self):
        print("Software Version: " + (PIC6.ss_rest_read('GENUNIT_VERS_ID')))

    def Pump_Configuration(self):
        # Evap Pumps Sequences Selection(0: NoPump,1: One Pump Only, 2:Two Pumps Auto,3:Pump#1 Manual,4:Pump#2 Manual)
        PIC6.ss_rest_write("PUMPCONF_cpumpseq", "0")
        PIC6.ss_rest_read_check("PUMPCONF_cpumpseq", "0")
        # Pump Auto Rotation Delay
        PIC6.ss_rest_write("PUMPCONF_pump_del", "48")
        PIC6.ss_rest_read_check("PUMPCONF_pump_del", "48")
        # Pump Sticking Protection(0: No, 1: Yes)
        PIC6.ss_rest_write("PUMPCONF_pump_per", "0")
        PIC6.ss_rest_read_check("PUMPCONF_pump_per", "0")
        # Pump Check if Pump Off (0: No, 1: Yes)
        PIC6.ss_rest_write("PUMPCONF_pump_loc", "0")
        PIC6.ss_rest_read_check("PUMPCONF_pump_loc", "0")
        print("Pump Configuration is Completed Successfully")

    def Today_Date(self):
        today = date.today()
        d1 = today.strftime("%Y/%m/%d/%w")
        return d1

    def Date_Decode_WW(self, A):
        # A = "33621624"  # Date Value which is read from PIC-6
        B = struct.pack('<Q', int(A))
        Data = list(map(int, struct.pack('<Q', int(A))))
        # print(Data)
        Year = 1900 + Data[0]  # base year 1900 we need to Add
        Month = f"{Data[1]:02}"  # for getting 2 Digits
        Date = f"{Data[2]:02}"
        DOW = Data[3]
        return str(Year) + '/' + str(Month) + '/' + str(Date) + '/' + str(DOW)

    def Date_Decode(self, A):
        # A = "33621624"  # Date Value which is read from PIC-6
        B = struct.pack('<Q', int(A))
        Data = list(map(int, struct.pack('<Q', int(A))))
        # print(Data)
        Year = 1900 + Data[0]  # base year 1900 we need to Add
        Month = f"{Data[1]:02}"  # for getting 2 Digits
        Date = f"{Data[2]:02}"
        DOW = Data[3]
        return str(Year) + '-' + str(Month) + '-' + str(Date)

    def Date_Encoder(self, V):  # (Year/Month/Date/WOD/0/0/0/0) eg:((2019, 5, 6, 1, 0, 0, 0, 0))
        Z = [V[0] - 1900, V[1], V[2], V[3], V[4], V[5], V[6], V[7]]
        K = ""
        for i in range(len(Z)):
            B = (bin(Z[i]).replace("0b", ""))  # Generating Binary Value
            C = (B.zfill(8))  # For maintain 8 Bits after converting(padding Zeros)
            K = C + K
        # print(K)
        return int(K, 2)

    def Time_Encoder(self, V):  # Hours/Minutes/Seconds/0/0/0/0/0
        Z = [V[0], V[1], V[2]]
        K = ""
        for i in range(len(Z)):
            B = (bin(Z[i]).replace("0b", ""))  # Generating Binary Value
            C = (B.zfill(8))  # For maintain 8 Bits after converting(padding Zeros)
            K = C + K
        # print(K)
        return int(K, 2)

    def Time_Decode(self, A):
        # A = "33621624"  # Date Value which is read from PIC-6
        B = struct.pack('<Q', int(A))
        Data = list(map(int, struct.pack('<Q', int(A))))
        # print(Data)
        Hours = f"{Data[0]:02}"  # for getting 2 Digits
        Min = f"{Data[1]:02}"  # for getting 2 Digits
        Sec = f"{Data[2]:02}"
        return str(Hours) + ':' + str(Min) + ':' + str(Sec)

    def NTP_Time_Syn(self):
        failStr = ''
        try:
            print("Started NTP Time Syc Test ")
            PIC6.ss_rest_write("NTP_svr_addr", "216.239.35.0") # time.nplindia.org
            PIC6.ss_rest_write("NTP_svr_sync_freq", "1")
            # Time Syn /User Choice (1: 1 Shot, 2: Recurring ,3:Stop)
            PIC6.ss_rest_write("NTP_sync_user_opt", "1")
            time.sleep(5)
            PIC6.ss_rest_read_check("NTP_status", "0")
            print(Colour1 + "NTP Time Syc status is passed")
        except Exception as e:
            print(Colour2 + "NTP Time Syc Test is failed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            PIC6.ss_rest_write("MANUAL_timezone_now", "11")  # Setting Indian Time Zone
            PIC6.ss_rest_read_check("MANUAL_timezone_stat", "0")
            print(Colour1 + "Setting Indian Time Zone Done")
        except Exception as e:
            print(Colour2 + "Setting Indian Time Zone Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            import datetime
            d = PIC6.monitor_req_time()  # date Read from PIC6
            pic_time = d + datetime.timedelta(hours=5.5)  # indian Time of PIC6
            print("Time Read from PIC6 :" + str(pic_time))
            from datetime import datetime
            format = "%Y-%m-%d %H:%M:%S.%f"  # "%I:%M:%S.%f %p"
            now_utc = datetime.now(timezone('UTC'))  # Reading UTC Time from Net or PC
            Z = datetime.strptime(now_utc.strftime(format), format)  # string to date Format changing
            import datetime
            new_time = Z + datetime.timedelta(hours=5.5)  # getting Indian Time from UTC reading from Net
            print("Time Read from Internet :" + str(new_time))
            difference = new_time - pic_time
            import datetime
            if datetime.timedelta(minutes=-5) <= difference <= datetime.timedelta(minutes=5):
                print(Colour1 + "NTP Time Syc Test is passed")
        except Exception as e:
            print(Colour2 + "Date Comparison Failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        if failStr != "":
            raise Exception(failStr)

    def Time_Zone(self):
        zone_data = {0: "UTC",
                     1: "EasternTime(US and Canada)(UTC - 05: 00)",
                     2: "Brussels, Copenhagen, Madrid, Paris(UTC + 01: 00)",
                     3: "Beijing, Chongqing, HongKong, Urumqi(UTC + 08: 00)",
                     4: "PacificTime(US and Canada)(UTC - 08: 00)",
                     5: "Arizona(UTC - 07: 00)",
                     6: "Dublin, Edinburgh, Lisbon, London(UTC)",
                     7: "Moscow, St.Petersburg, Volgograd, Arabian(UTC + 03: 00)",
                     8: "AbuDhabi, Muscat(UTC + 04: 00)",
                     9: "KualaLumpur, Singapore(UTC + 08: 00)",
                     10: "Canberra, Melbourne, Sydney(UTC + 10: 00)",
                     11: "India, NewDelhi, Calcutta(UTC + 5: 30)"}
        list_diff = [+0, -5, +1, +8, -8, -7, +0, +3, +4, +8, +10, +5.5]
        try:
            for i in range(12):
                PIC6.ss_rest_write("MANUAL_timezone_now", str(i))  # Changing Time Zones in PIC6
                PIC6.ss_rest_read_check("MANUAL_timezone_stat", "0")  # Reading Status
                time.sleep(5)
                from datetime import datetime
                format = "%Y-%m-%d %H:%M:%S.%f"  # "%I:%M:%S.%f %p"
                now_utc = datetime.now(timezone('UTC'))  # Reading UTC Time from Net or PC
                Z = datetime.strptime(now_utc.strftime(format), format)  # string to date Format changing
                d = PIC6.monitor_req_time()  # date Read from PIC6
                o = float(PIC6.offset_Time())
                if list_diff[i] > 0:
                    import datetime
                    net_time = Z + datetime.timedelta(hours=list_diff[i])
                    pic_time = d + datetime.timedelta(hours=abs(o))
                    # print(new_time)
                else:
                    import datetime
                    net_time = Z - datetime.timedelta(hours=abs(list_diff[i]))
                    pic_time = d - datetime.timedelta(hours=abs(0))
                    # print(new_time)
                if net_time >= pic_time:
                    Z = net_time - pic_time
                else:
                    Z = pic_time - net_time
                import datetime
                if datetime.timedelta(minutes=-5) <= Z <= datetime.timedelta(minutes=5):
                    print("Time Zone Actual Time is :" + str(net_time))
                    print("PIC6 Time is             :" + str(pic_time))
                    print("Time Difference is       :" + str(Z))
                    ind = zone_data[i]
                    print(Colour1 + ind + " Test is passed")
                    print("********************************************************")
                else:
                    print("Time Zone Actual Time is :" + str(net_time))
                    print("PIC6 Time is             :" + str(pic_time))
                    print("Time Difference is       :" + str(Z))
                    ind = zone_data[i]
                    print(Colour2 + ind + " Test is Fail")
                    print("********************************************************")
            print("Time Zone Test is Completed")
        except:
            print(" Test Verification Failed")

    def Reboot_Pic6(self):
        PIC6.ss_rest_write("Ui_BOOL_var3", "1")
        time.sleep(120)
        self.Clear_Alarm()

    def Neg_test(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
        '''
        # print("Clicking Home Button")
        # A.click(37, 37)  # Click Operation on home Button
        # print("Clicking Lock Button")
        # A.click(640, 24)  # Click on lock
        # print("Clicking Factory Login Button")
        # A.click(213,279)  # Click on Factory Login
        # print("Clicking Scanner Button ")
        # A.click(35,444)   # Click on Scaner button
        # print("Clicking Login Box")
        # A.click(619,353)  # Click on Login
        # print("Entering Password")
        # TestParameters.read("C:\\End to End\\Python3_app\\Utilities\\Test_Parameters.ini")
        # password = TestParameters.get("TEST_PARAMETERS", "factory")
        # A.Write_Field(password)  # Entering Password
        '''

        print("Clicking  Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking Main Menu Button")
        A.click(156, 33)  # Click Operation on Main Menu
        print("Clicking Down Navigation Arrow")
        A.click(776, 455)  # Click Operation on Down Navigation Arrow
        print("Clicking Quick Test Table Icon")
        A.click(402, 114)  # Click On Quick Test Table Icon
        # print("Quick test 1 st page operations Starting")
        A.enable_set(504, 124)
        time.sleep(5)

        failStr = ''
        try:
            print("Test 1 : Checking PIC 6 is in Local Off Mode or Not")
            PIC6.ss_rest_read_Neg_check("GENUNIT_CTRL_TYP", "1")
        except Exception as e:
            print("Pic 6 is in Local Mode")
            failStr = failStr + str(e.args[0]) + '.\n'
        # V = PIC6.ss_rest_read("GENUNIT_STATUS")
        # print(V)
        try:
            PIC6.ss_rest_read_Neg_check("GENUNIT_STATUS", "Off     ")
            print("Pic 6 is not in Off Mode")
        except Exception as e:
            print("PIC6 in Local Off Mode")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 2 : Enabling Quick Test")
            A.disable_set(504, 124)  # Click on EnableQuick Test
            PIC6.ss_rest_read_Neg_check("QCK_TEST_QCK_TEST", "1")
            print("Quick Test is not Enabled")
        except Exception as e:
            print("Quick Test is Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        # V = PIC6.ss_rest_read("GENUNIT_STATUS")
        # print(V)
        try:
            print("Test 3 : Checking PIC 6 is in Local Test Mode or Not")
            PIC6.ss_rest_read_Neg_check("GENUNIT_CTRL_TYP", "1")
            time.sleep(10)
        except Exception as e:
            print("Pic 6 is not in Local Mode")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            PIC6.ss_rest_read_Neg_check("GENUNIT_STATUS", "Test    ")
            print("Pic 6 is not in Test Mode ")
        except Exception as e:
            print("Now PIC6 in Local Test Mode")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 4 : EXV Position verification")
            A.click(429, 163)  # Click on Circuit A EXV Position box
            # print("Entering EXV Position Value")
            A.quick_Test_write("100")  # Write data in to EXV Position
            time.sleep(30)
            PIC6.ss_rest_read_Neg_check("EXV_CTRL_EXV_A", "100")
        except Exception as e:
            print("EXV_A value verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            PIC6.ss_rest_read_Neg_check("EXV_CTRL_EXV_STPA", "3810")
            print("EXV_A Step value verification failed")
        except Exception as e:
            print("EXV Position status verified")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 5 : Enabling Oil Solenoid ")
            A.enable_set(500, 207)  # Circuit A Oil Solenoid enable
            PIC6.ss_rest_read_Neg_check("TBLSHT_OIL_SL_A", "1")
            print("Oil Solenoid verification failed")
        except Exception as e:
            print("Oil Solenoid is Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 6: EXV Eco Position Cri A ")
            A.click(408, 245)  # EXV Eco Position Cri A:
            print("Entering EXV Eco Position Cri A value ")
            A.quick_Test_write("100")  # Write data in to EXV Eco Position Cri A
            time.sleep(30)
            PIC6.ss_rest_read_Neg_check("ECO_CTRL_eco_a", "100.000008")
            PIC6.ss_rest_read_Neg_check("ECO_CTRL_eco_stpa", "2625")
            print("EXV Eco Position Cri A verification failed")
        except Exception as e:
            print("EXV Eco Position Cri A test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 7: Enabling Oil Heater Circuit A")
            A.enable_set(503, 283)  # Oil Heater Circuit A:
            PIC6.ss_rest_read_Neg_check("OUTPUTS_OIL_HT_A", "1")
            print("Oil Heater Circuit A Test is failed")
        except Exception as e:
            print("Oil Heater Circuit A is Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 8:Capacity Cri A Output")
            A.click(431, 318)  # Capacity Cri A Output:
            print("Entering value in to Capacity Cri A Output")
            A.quick_Test_write("100")  # Write data in to Capacity Cri A Output
            time.sleep(30)
            PIC6.ss_rest_read_Neg_check("TBLSHT_CAPT010A", "10")
            print("Capacity Cri A Output test verification failed")
        except Exception as e:
            print("Capacity Cri A Output test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 9: Enabling Comp A Running Output")
            A.enable_set(504, 362)  # Comp A Running Output enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_CP_A", "1")
            print("Comp A Running Output verification failed")
        except Exception as e:
            print("Comp A Running Output Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 10: Enabling Isolation Valve State A open ")
            A.enable_set(503, 407)  # Isolation Valve State A open
            PIC6.ss_rest_read_Neg_check("OUTPUTS_ISO_OP_A", "1")
            print("Isolation Valve State A open Test verification failed")
        except Exception as e:
            print("Isolation Valve State A open Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        A.click(780, 452)  # Click on Down Arrow
        # Page 2 *************************************************************************
        try:
            print("Test 11: Enabling Circuit A VI ")
            A.enable_set(498, 83)  # Circuit A VI enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_VI_A", "1")
            print("Circuit A VI verification failed")
        except Exception as e:
            print("Circuit A VI Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        #  FANS ***********************************************************************
        ECM = PIC6.ss_rest_read("FACTORY_ECM_fans")
        if ECM == "0":
            try:
                print("Test:12 VariFan Speed A ")
                A.click(404, 124)  # click on VariFan Speed A box
                print("Entering Value to VariFan Speed A ")
                A.quick_Test_write("100")  # Writing value to VariFan Speed A
                time.sleep(30)
                PIC6.ss_rest_read_Neg_check("OUTPUTS_VFAN_A", "100")
                print("VariFan Speed A test verification failed")
            except Exception as e:
                print("VariFan Speed At test is passed")
                failStr = failStr + str(e.args[0]) + '.\n'
        else:
            print("ECM Fan is Enabled so VariFan Speed test is not Performed")

        try:
            print(" Test 13: Circuit B EXV Position")
            A.click(398, 162)  # click on Circuit B EXV Position box
            print("Entering values to Circuit B EXV Position")
            A.quick_Test_write("100")  # Write the value to Circuit B EXV Position
            time.sleep(30)
            PIC6.ss_rest_read_Neg_check("EXV_CTRL_EXV_B", "100")
            PIC6.ss_rest_read_Neg_check("EXV_CTRL_EXV_STPB", "3810")
            print("Circuit B EXV Position test verification failed")
        except Exception as e:
            print("Circuit B EXV Position test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 14: Enabling Circuit B Oil Solenoid ")
            A.enable_set(501, 200)  # Circuit B Oil Solenoid enable
            PIC6.ss_rest_read_Neg_check("TBLSHT_OIL_SL_B", "1")
            print("Circuit B Oil Solenoid verification failed")
        except Exception as e:
            print("Circuit B Oil Solenoid is Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test 15: EXV Eco Position Cri B Test")
            A.click(414, 236)  # Click on EXV Eco Position Cri B box
            print("writing values to EXV Eco Position Cri B")
            A.quick_Test_write("100")  # Write value to EXV Eco Position Cri B
            time.sleep(30)
            PIC6.ss_rest_read_Neg_check("ECO_CTRL_eco_b", "100.000008")
            PIC6.ss_rest_read_Neg_check("ECO_CTRL_eco_stpb", "2625")
            print("EXV Eco Position Cri A test verification failed")
        except Exception as e:
            print("EXV Eco Position Cri B test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:16 Enabling Oil Heater Circuit B ")
            A.enable_set(501, 285)  # Oil Heater Circuit B enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_OIL_HT_B", "1")
            print("Oil Heater Circuit B verification  failed")
        except Exception as e:
            print("Oil Heater Circuit B is Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:17  Capacity Cir B Output ")
            A.click(416, 323)  # click on Capacity CirB Output box
            print("writing vale to Capacity Cir B Output")
            A.quick_Test_write("100")  # Write value to Capacity CirB Output box
            time.sleep(30)
            PIC6.ss_rest_read_Neg_check("TBLSHT_CAPT010B", "10")
            print("Capacity Cri B Output test verification failed")
        except Exception as e:
            print("Capacity Cri B Output test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:18 Enabling Comp B Running Output")
            A.enable_set(499, 363)  # Comp B Running Output enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_CP_B", "1")
            print("Comp B Running Output verification failed")
        except Exception as e:
            print("Comp B Running Output Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:19 Enabling Isolation Valve State B")
            A.enable_set(505, 399)  # Isolation Valve State B enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_ISO_OP_B", "1")
            print("Isolation Valve State B open verification failed")
        except Exception as e:
            print("Isolation Valve State B open Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        A.click(780, 452)  # Click on Down Arrow
        # Page 3 *************************************************************************
        try:
            print("Test:20 Enabling Circuit B VI")
            A.enable_set(501, 81)  # Circuit B VI enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_VI_B", "1")
            print("Circuit B VI verification failed")
        except Exception as e:
            print("Circuit B VI Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        ECM = PIC6.ss_rest_read("FACTORY_ECM_fans")
        if ECM == "0":
            try:
                print("Test: 21 Vari Fan Speed B")
                A.click(411, 121)  # click on VariFan Speed B box
                print("writing value to Vari Fan Speed B")
                A.quick_Test_write("100")  # Write value to VariFan Speed B
                time.sleep(30)
                PIC6.ss_rest_read_Neg_check("OUTPUTS_VFAN_B", "100")
                print("VariFan Speed B test verification failed")
            except Exception as e:
                print("VariFan Speed B test is passed")
                failStr = failStr + str(e.args[0]) + '.\n'
        else:
            print(" ECM Fan is Enabled so Vari Fan Speed test is not performed")

        try:
            print("Test:22 Enabling Evaporator Heater ")
            A.enable_set(508, 160)  # Evaporator Heater enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_EVAP_HEATER", "1")
            print("Evaporator Heater verification failed")
        except Exception as e:
            print("Evaporator Heater Enabled ")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test :23 Evaporator Pump1 ")
            A.click(412, 201)  # click on Evaporator Pump1 box
            print("Entering value to Evaporator Pump 1")
            A.quick_Test_write("0")  # Write value to Evaporator Pump1
            time.sleep(1)
            PIC6.ss_rest_read_Neg_check("PUMPSTAT_CPUMP_1", "1")
            # print("Evaorator Pump1 is On")
            time.sleep(10)
            PIC6.ss_rest_read_Neg_check("PUMPSTAT_CPUMP_1", "1")
            # print("Evaorator Pump1 is Off")
            print("Evaporator pump 1 test verification failed")
        except Exception as e:
            print("Evaporator Pump 1 test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:24 Evaporator Pump2 ")
            A.click(400, 238)  # click on Evaporator Pump2 box
            print("Writing Value to Evaporator Pump 2")
            A.quick_Test_write("0")  # Write value to Evaporator
            time.sleep(1)
            PIC6.ss_rest_read_Neg_check("PUMPSTAT_CPUMP_2", "1")
            # print("Evaorator Pump2 is On")
            time.sleep(10)
            PIC6.ss_rest_read_Neg_check("PUMPSTAT_CPUMP_2", "1")
            # print("Evaorator Pump2 is Off")
            print("Evaporator pump 2 test verification failed")
        except Exception as e:
            print("Evaporator Pump 2 test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:25 Enabling Alarm Relay Status")
            A.enable_set(501, 283)  # Alarm Relay Status enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_ALARM", "1")
            print("Alarm Relay Status verification failed")
        except Exception as e:
            print("Alarm Relay Status Enabled ")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:26 Enabling Shutdown Status")
            A.enable_set(505, 320)  # Shutdown Relay Status enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_SHUTDOWN", "1")
            print("Shutdown Status Test verification failed")
        except Exception as e:
            print("Shutdown Status Enabled Successfully")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:27 Enabling Running Relay Status")
            A.enable_set(507, 365)  # Running Relay Status enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_RUNNING", "1")
            print("Running Relay Status Test verification failed")
        except Exception as e:
            print("Running Relay Status Enabled Successfully")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:28 Enabling Alert Relay Switch")
            A.enable_set(506, 401)  # Alert Relay Switch
            PIC6.ss_rest_read_Neg_check("OUTPUTS_ALERT", "1")
            print("Alert Relay Switch Test verification failed")
        except Exception as e:
            print("Alert Relay Switch Enabled Successfully")
            failStr = failStr + str(e.args[0]) + '.\n'

        A.click(780, 452)  # Click on Down Arrow
        # Page 4 *************************************************************************
        try:
            print("Test:29 Capacity Total Output ")
            A.click(392, 84)  # Click on Capacity Total Output box
            print("Entering value to Capacity Total Output")
            A.quick_Test_write("100")  # Write value to Capacity Total Output
            PIC6.ss_rest_read_Neg_check("OUTPUTS_CAPT_010", "10")
            print("Capacity Total Output test verification failed")
        except Exception as e:
            print("Capacity Total Output test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:30 Enabling drive heater A ")
            A.enable_set(501, 123)  # Com drive heater A enable
            PIC6.ss_rest_read_Neg_check("VLT_DRV_drv_HTRa", "0")
            print("drive heater A Test verification failed")
        except Exception as e:
            print("drive heater A Enabled Successfully")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:31 Enabling drive heater B ")
            A.enable_set(502, 163)  # Com drive heater B enable
            PIC6.ss_rest_read_Neg_check("VLT_DRV_drv_HTRb", "0")
            print("drive heater B Test verification failed")
        except Exception as e:
            print("drive heater B Enabled Successfully")
            failStr = failStr + str(e.args[0]) + '.\n'

        ECM = PIC6.ss_rest_read("FACTORY_ECM_fans")
        if ECM == "0":
            try:
                print("Test:32 Fan Contactors Related A ")
                print("Enabling Fan Contactor 1A ")
                A.enable_set(501, 206)  # Fan Contactor 1A enable
                print("Enabling Fan Contactor 2A ")
                A.enable_set(499, 249)  # Fan Contactor 2A enable
                print("Enabling Fan Contactor 3A ")
                A.enable_set(503, 291)  # Fan Contactor 3A enable
                print("Enabling Fan Contactor 4A ")
                A.enable_set(505, 323)  # Fan Contactor 4A enable
                print("Enabling Fan Contactor 5A ")
                A.enable_set(500, 363)  # Fan Contactor 5A enable
                print("Enabling Fan Contactor 6A ")
                A.enable_set(500, 407)  # Fan Contactor 6A enable
                # print("Clicking Down Navigation Arrow")
                A.click(780, 452)  # Click on Down Arrow
                # Page 5 *************************************************************************
                # print("Quick test 5th page operations starting")
                print("Enabling Fan Contactor 7A ")
                A.enable_set(497, 80)  # Fan Contactor 7A enable
                print("Enabling Fan Contactor 8A ")
                A.enable_set(501, 120)  # Fan Contactor 8A enable
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCA1", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCA2", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCA3", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCA4", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCA5", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCA6", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCA7", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCA8", "1")
                # print("Fan Contactor 1A to 8A are in On Mode")
                print("Fan Contactors Related A Test verification failed")
            except Exception as e:
                print("Fan Contactors Related A Test is Passed")
                failStr = failStr + str(e.args[0]) + '.\n'

            try:
                print("Test:33 Fan Contactors Related B ")
                print("Enabling Fan Contactor 1B ")
                A.enable_set(506, 161)  # Fan Contactor 1B enable
                print("Enabling Fan Contactor 2B ")
                A.enable_set(505, 203)  # Fan Contactor 2B enable
                print("Enabling Fan Contactor 3B ")
                A.enable_set(507, 246)  # Fan Contactor 3B enable
                print("Enabling Fan Contactor 4B ")
                A.enable_set(504, 284)  # Fan Contactor 4B enable
                print("Enabling Fan Contactor 5B ")
                A.enable_set(504, 323)  # Fan Contactor 5B enable
                print("Enabling Fan Contactor 6B ")
                A.enable_set(505, 363)  # Fan Contactor 6B enable
                print("Enabling Fan Contactor 7B ")
                A.enable_set(506, 402)  # Fan Contactor 7B enable
                # print("Clicking Down Navigation Arrow")
                A.click(780, 452)  # Click on Down Arrow

                # Page 6 *************************************************************************
                # print("Quick test 6th page operations strting")
                print("Enabling Fan Contactor 8B ")
                A.enable_set(503, 80)  # Fan Connector 8B enable
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCB1", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCB2", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCB3", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCB4", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCB5", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCB6", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCB7", "1")
                PIC6.ss_rest_read_Neg_check("OUTPUTS_FCB8", "1")
                # print("Fan Contactor 1B to 8B are in On Mode")
                print("Fan Contactors Related B Test verification failed")
            except Exception as e:
                print("Fan Contactors Related B Test is Passed")
                failStr = failStr + str(e.args[0]) + '.\n'
        else:
            print("ECM Fan Is Enable  so Fan Contactors Operation Can Be Performed")

        try:
            print("Test:34 Enabling Comp.HW Enable A ")
            A.enable_set(504, 125)  # Comp.HW Enable A enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_VFD_EN_A", "1")
            print("Comp.HW Enable A Test verification failed")
        except Exception as e:
            print("Comp.HW Enable A is Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:35 Enabling Comp.HW Enable B ")
            A.enable_set(502, 163)  # Comp.HW Enable B enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_VFD_EN_B", "1")
            print("Comp.HW Enable B Test verification failed")
        except Exception as e:
            print("Comp.HW Enable B is Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:36 Enabling Control Box Heater ")
            A.enable_set(500, 201)  # Control Box Heater enable
            PIC6.ss_rest_read_Neg_check("OUTPUTS_BOX_HTR", "1")
            print("Control Box Heater Test verification failed")
        except Exception as e:
            print("Control Box Heater is Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:37 All ECM Fan Spd CIRA ")
            A.click(401, 244)  # Click on All ECM Fan spd CIRA box
            print("writing value to All ECM Fan Spd CIRA ")
            A.quick_Test_write("100")  # Write value to All ECM Fan spd CIRA box
            PIC6.ss_rest_read_Neg_check("ECM_FAN1_SPEED_PERCENT", "100")
            print("All ECM Fan Spd CIRA test verification failed")
        except Exception as e:
            print("All ECM Fan Spd CIRA test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        try:
            print("Test:38 All ECM Fan Spd CIRB ")
            A.click(392, 282)  # Click on All ECM Fan spd CIRB box
            print("writing value to All ECM Fan Spd CIRB ")
            A.quick_Test_write("100")  # Write value to All ECM Fan spd CIRB box
            PIC6.ss_rest_read_Neg_check("ECM_FAN2_SPEED_PERCENT", "100")
            print("All ECM Fan Spd CIRB test verification failed")
        except Exception as e:
            print("All ECM Fan Spd CIRB test is passed")
            failStr = failStr + str(e.args[0]) + '.\n'

        A.click(99, 26)  # Click on Back Button
        A.click(402, 114)  # Click On Quick Test Table Icon
        A.disable_set(504, 124)
        print("Quick test is finished")
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()

        if failStr != "":
            raise Exception(failStr)

    def Timer(self, A):
        t = int(A)
        while t:
            mins = t // 60
            sec = t % 60
            timer = '{:02d}:{:02d}'.format(mins, sec)
            print(f'\r{timer}', end='')
            time.sleep(1)
            t -= 1
        print("Done!!!!!!")

    def WR_Date(self, Year, Month, Date):
        import datetime
        import calendar
        date = (str(Year) + " " + str(Month) + " " + str(Date))
        born = datetime.datetime.strptime(date, '%Y %m %d').weekday()
        day = calendar.day_name[born]
        List = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for i in range(len(List)):
            if List[i] == day:
                WD_index = i
        else:
            pass
        WD = WD_index
        V = [Year, Month, Date, WD, 0, 0, 0, 0]
        Z = [V[0] - 1900, V[1], V[2], V[3], V[4], V[5], V[6],
             V[7]]  # Z = [V[0] - 1900, V[1], V[2], V[3], V[4], V[5], V[6], V[7]]
        K = ""
        for i in range(len(Z)):
            B = (bin(Z[i]).replace("0b", ""))  # Generating Binary Value
            C = (B.zfill(8))  # For maintain 8 Bits after converting(padding Zeros)
            K = C + K
        Date_data = int(K, 2)
        PIC6.ss_rest_write("MANUAL_date", str(Date_data))
        return Date_data

    def loop_helper(self, wb, ws):
        self.wb = wb
        self.ws = ws
        a = []
        # print("total no.of parameters: " + str(len(a)))
        for i in range(ws.nrows):
            a.append(ws.row_values(i))
        print("Total no.of parameters: " + str(len(a)))
        for j in range(len(a)):
            l1 = a[j]
            S = str(l1[1])
            k = S.find(".0")
            # print(k)
            if j > 0:
                try:
                    print(l1[0], l1[1])
                    if k == -1:
                        self.Util_ccn_handle.CCN_WritePointinTable(str(l1[0]), float(l1[1]), BlockNum=5)
                    else:
                        self.Util_ccn_handle.CCN_WritePointinTable(str(l1[0]), int(l1[1]), BlockNum=5)
                except:
                    print("row getting error ***********************" + str(l1[0]) + str(j))

    def ccn_par_write(self):
        # Parameter file should be present in Utilities folder
        path = dirnameutils + "\\Data\\APPLICATION\\Parameter_W_File.xlsx"
        # print(path)
        wb = xlrd.open_workbook(path)  # WB Stand For Workbook
        for i in range(wb.nsheets):
            ws = wb.sheet_by_index(i)
            a = []  # Defining List
            if i == 0:
                print("writing Factory Values")
                print("********************************************************************************")
                self.loop_helper(wb, ws)
            else:
                print("writing Service Values")
                print("********************************************************************************")
                self.loop_helper(wb, ws)

    def ccn_pra_read(self):
        path = dirnameutils + "\\Data\\APPLICATION\\Parameter_R_File.xlsx"
        wb = xlrd.open_workbook(path)
        data = []

        for i in range(wb.nsheets):
            ws = wb.sheet_by_index(0)
            for j in range(ws.nrows):
                data.append(ws.row_values(j))

        for i in range(len(data)):
            cur = data[i]
            cur1 = cur[0]
            if i > 0:
                try:
                    cur2 = int(cur[1])
                    # print(cur1, cur2)
                    print("Checking  " + str(cur1), "value == " + str(cur2))
                    # assertions.assertEqual(self.ccn_handle.WaitUntilPoint("X", "Y", 20), True)
                    # self.ccn_handle.CCN_ReadTablePoint_with_TableName("Q_EXVA", "QCK_TEST", BlockNum=5)
                    assertions.assertEqual(self.Util_ccn_handle.WaitUntilPoint(cur1, cur2, 50), True)
                except:
                    print("row getting error ***********************" + str(i))

    def loadXML(self):
        self.Util_VirSim_handle.reloadXML()
        time.sleep(15)

    def Chiller_test_Local_On(self):
        # PIC6.ss_rest_read("CTRLID_MODEL_NB")
        print("Resetting Alarms")
        PIC6.ss_rest_write("ALARMRST_RST_ALM", '1')
        PIC6.ss_rest_write("LOCAL_OPERTYP", '0')
        time.sleep(60)
        self.Util_ccn_handle.CCN_WritePointinTable("unitsize", 200, BlockNum=5)
        self.Util_ccn_handle.CCN_WritePointinTable("voltage", 380, BlockNum=5)
        self.Util_ccn_handle.CCN_WritePointinTable("freq_60H", 1, BlockNum=5)
        self.Util_ccn_handle.CCN_WritePointinTable("mfg_tier", 2, BlockNum=5)
        self.Util_ccn_handle.CCN_WritePointinTable("emm_nrcp", 1, BlockNum=5)
        time.sleep(10)
        PIC6.ss_rest_write("Ui_BOOL_var3", "1")  # Reboot the PIC6
        time.sleep(60)
        PIC6.ss_rest_write("ALARMRST_RST_ALM", '1')
        time.sleep(5)
        PIC6.ss_rest_read_check("FACTORY_unitsize", "200")
        PIC6.ss_rest_read_check("FACTORY_voltage", "380")
        PIC6.ss_rest_read_check("FACTORY_freq_60H", "1")
        PIC6.ss_rest_read_check("FACTORY_mfg_tier", "2")
        PIC6.ss_rest_read_check("FACTORY_emm_nrcp", "1")
        PIC6.ss_rest_write("GENCONF_prio_cir", '1')
        PIC6.ss_rest_write("GENCONF_ramp_sel", '0')
        PIC6.ss_rest_read_check("GENCONF_prio_cir", "1")
        PIC6.ss_rest_read_check("GENCONF_ramp_sel", "0")
        PIC6.ss_rest_write("LOCAL_OPERTYP", '1')
        print("Waiting 460 sec to reach ciller capacity to 100%")
        time.sleep(700)
        PIC6.ss_rest_read_check("GENUNIT_CAP_T", "100")
        PIC6.ss_rest_read_check("ALARMRST_alarm_1c", "0")
        PIC6.ss_rest_read_check("ALARMRST_alarm_2c", "0")
        PIC6.ss_rest_read_check("ALARMRST_alarm_3c", "0")
        PIC6.ss_rest_read_check("GENUNIT_CTRL_TYP", "0")
        PIC6.ss_rest_read_check("GENCONF_prio_cir", "1")
        PIC6.ss_rest_read_check("GENCONF_ramp_sel", "0")
        PIC6.ss_rest_read_check("GENUNIT_STATUS", "Ready   ")
        PIC6.ss_rest_read_check("CAPACTRL_ctrl_wt", "50.000397")
        PIC6.ss_rest_read_check("CAPACTRL_cap_lim", "100")
        PIC6.ss_rest_read_check("CAPACTRL_drvcmda", "105")
        PIC6.ss_rest_read_check("CAPACTRL_capstata", "WATER_T")
        PIC6.ss_rest_read_check("CAPACTRL_captxta", "Water Temp. Ctrl")
        PIC6.ss_rest_read_check("CAPACTRL_ovrstata", "NO_OVR")
        PIC6.ss_rest_read_check("CAPACTRL_ovrtxta", "No Override Present")
        PIC6.ss_rest_read_check("CAPACTRL_cap_pc_a", "100")
        PIC6.ss_rest_read_check("CAPACTRL_drvcmdb", "105")
        PIC6.ss_rest_read_check("CAPACTRL_capstatb", "WATER_T")
        PIC6.ss_rest_read_check("CAPACTRL_captxtb", "Water Temp. Ctrl")
        PIC6.ss_rest_read_check("CAPACTRL_ovrstatb", "NO_OVR")
        PIC6.ss_rest_read_check("CAPACTRL_ovrtxtb", "No Override Present")
        PIC6.ss_rest_read_check("CAPACTRL_capmodb", "0")
        PIC6.ss_rest_read_check("CAPACTRL_cap_pc_b", "100")
        PIC6.ss_rest_write("LOCAL_OPERTYP", '0')
        time.sleep(60)
        PIC6.ss_rest_read_check("LOCAL_OPERTYP", '0')
        print("Local On Test Completed")

    def Chiller_test_Local_SC(self):
        # PIC6.ss_rest_read("CTRLID_MODEL_NB")
        print("Resetting Alarms")
        PIC6.ss_rest_write("ALARMRST_RST_ALM", '1')
        PIC6.ss_rest_write("LOCAL_OPERTYP", '0')
        time.sleep(60)
        self.Util_ccn_handle.CCN_WritePointinTable("unitsize", 200, BlockNum=5)
        self.Util_ccn_handle.CCN_WritePointinTable("voltage", 380, BlockNum=5)
        self.Util_ccn_handle.CCN_WritePointinTable("freq_60H", 1, BlockNum=5)
        self.Util_ccn_handle.CCN_WritePointinTable("mfg_tier", 2, BlockNum=5)
        self.Util_ccn_handle.CCN_WritePointinTable("emm_nrcp", 1, BlockNum=5)
        time.sleep(10)
        PIC6.ss_rest_write("Ui_BOOL_var3", "1")  # Reboot the PIC6
        time.sleep(60)
        PIC6.ss_rest_write("ALARMRST_RST_ALM", '1')
        time.sleep(5)
        PIC6.ss_rest_read_check("FACTORY_unitsize", "200")
        PIC6.ss_rest_read_check("FACTORY_voltage", "380")
        PIC6.ss_rest_read_check("FACTORY_freq_60H", "1")
        PIC6.ss_rest_read_check("FACTORY_mfg_tier", "2")
        PIC6.ss_rest_read_check("FACTORY_emm_nrcp", "1")
        PIC6.ss_rest_write("GENCONF_prio_cir", '1')
        PIC6.ss_rest_write("GENCONF_ramp_sel", '0')
        PIC6.ss_rest_read_check("GENCONF_prio_cir", "1")
        PIC6.ss_rest_read_check("GENCONF_ramp_sel", "0")
        PIC6.ss_rest_write("LOCAL_OPERTYP", '2')
        print("Waiting 700 sec to reach ciller capacity to 100%")
        time.sleep(700)
        PIC6.ss_rest_read_check("GENUNIT_CAP_T", "100")
        time.sleep(120)
        PIC6.ss_rest_read_check("ALARMRST_alarm_1c", "0")
        PIC6.ss_rest_read_check("ALARMRST_alarm_2c", "0")
        PIC6.ss_rest_read_check("ALARMRST_alarm_3c", "0")
        PIC6.ss_rest_read_check("ALARMRST_alarm_4c", "0")
        PIC6.ss_rest_read_check("ALARMRST_alarm_5c", "0")
        PIC6.ss_rest_read_check("GENUNIT_CTRL_TYP", "0")
        PIC6.ss_rest_read_check("GENCONF_prio_cir", "1")
        PIC6.ss_rest_read_check("GENCONF_ramp_sel", "0")
        PIC6.ss_rest_read_check("GENUNIT_STATUS", "Ready   ")
        PIC6.ss_rest_read_check("CAPACTRL_ctrl_wt", "50.000397")
        PIC6.ss_rest_read_check("CAPACTRL_cap_lim", "100")
        PIC6.ss_rest_read_check("CAPACTRL_drvcmda", "105")
        PIC6.ss_rest_read_check("CAPACTRL_capstata", "WATER_T")
        PIC6.ss_rest_read_check("CAPACTRL_captxta", "Water Temp. Ctrl")
        PIC6.ss_rest_read_check("CAPACTRL_ovrstata", "NO_OVR")
        PIC6.ss_rest_read_check("CAPACTRL_ovrtxta", "No Override Present")
        PIC6.ss_rest_read_check("CAPACTRL_cap_pc_a", "100")
        PIC6.ss_rest_read_check("CAPACTRL_drvcmdb", "105")
        PIC6.ss_rest_read_check("CAPACTRL_capstatb", "WATER_T")
        PIC6.ss_rest_read_check("CAPACTRL_captxtb", "Water Temp. Ctrl")
        PIC6.ss_rest_read_check("CAPACTRL_ovrstatb", "NO_OVR")
        PIC6.ss_rest_read_check("CAPACTRL_ovrtxtb", "No Override Present")
        PIC6.ss_rest_read_check("CAPACTRL_capmodb", "0")
        PIC6.ss_rest_read_check("CAPACTRL_cap_pc_b", "100")
        PIC6.ss_rest_write("LOCAL_OPERTYP", '0')
        time.sleep(5)
        PIC6.ss_rest_read_check("LOCAL_OPERTYP", '0')
        time.sleep(120)
        try:
            PIC6.ss_rest_read_check("CAPACTRL_lcapmodb", "9")
            PIC6.ss_rest_read_check("CAPACTRL_overridb", "0")
            PIC6.ss_rest_read_check("CAPACTRL_cap_pc_b", "0")
        except:
            A = PIC6.ss_rest_read("CAPACTRL_lcapmodb")
            print("A")
            B = PIC6.ss_rest_read("CAPACTRL_overridb")
            print(B)
            C = PIC6.ss_rest_read("CAPACTRL_cap_pc_b")
            print(C)
        PIC6.ss_rest_read_check("LOCAL_OPERTYP", '0')
        print("Local On SC Test Completed")

    def Quick_Pre_Check(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
        print("Clicking  Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking Main Menu Button")
        A.click(156, 33)  # Click Operation on Main Menu
        print("Clicking Down Navigation Arrow")
        A.click(776, 455)  # Click Operation on Down Navigation Arrow
        print("Clicking Quick Test Table Icon")
        A.click(402, 114)  # Click On Quick Test Table Icon
        A.disable_set(504, 124)
        time.sleep(5)
        try:
            print("Checking PIC 6 is in Local Off Mode or Not")
            PIC6.ss_rest_read_check("GENUNIT_CTRL_TYP", "0")
            PIC6.ss_rest_read_check("GENUNIT_STATUS", "Off     ")
            print("PIC6  in Local-OFF Mode")
        except:
            print("PIC6 is Not in Local-OFF mode")

    def Quick_Navigation(self):
        print("Clicking  Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking Main Menu Button")
        A.click(156, 33)  # Click Operation on Main Menu
        print("Clicking Down Navigation Arrow")
        A.click(776, 455)  # Click Operation on Down Navigation Arrow
        print("Clicking Quick Test Table Icon")
        A.click(402, 114)  # Click On Quick Test Table Icon

    def Quick_Enable(self):
        failStr = ''
        try:
            print("Enabling Quick Test")
            A.enable_set(504, 124)  # Click on EnableQuick Test
            PIC6.ss_rest_read_check("QCK_TEST_QCK_TEST", "1")
            print("Quick Test is button is Enabled")
        except Exception as e:
            print("Quick Test is not Enabled")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            print("Checking PIC 6 is in Local Test Mode or Not")
            PIC6.ss_rest_read_check("GENUNIT_CTRL_TYP", "0")
            time.sleep(10)
        except Exception as e:
            print("Pic 6 is not in Local Mode")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            PIC6.ss_rest_read_check("GENUNIT_STATUS", "Test    ")
            print(" Now PIC6 in Local Test Mode")
        except Exception as e:
            print("Pic 6 is not in Test Mode")
            failStr = failStr + str(e.args[0]) + '.\n'
        if failStr == "":
            print("Quick Test is Enabled Successfully")
        elif failStr !="":
            raise Exception(failStr)

    def Quick_Disable(self):
        print("Clicking  Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking Main Menu Button")
        A.click(156, 33)  # Click Operation on Main Menu
        print("Clicking Down Navigation Arrow")
        A.click(776, 455)  # Click Operation on Down Navigation Arrow
        print("Clicking Quick Test Table Icon")
        A.click(402, 114)  # Click On Quick Test Table Icon
        # print("Quick test 1 st page operations Starting")
        A.disable_set(504, 124)
        time.sleep(5)

    def Quick_EXV(self):
        self.Quick_Navigation()
        failStr = ''
        try:
            print("EXV Position and EXV Eco Position Circuit Verification")
            A.click(429, 163)  # Click on Circuit A EXV Position box
            # print("Entering EXV Position Value")
            A.quick_Test_write("100")  # Write data in to EXV Position
            time.sleep(30)
            PIC6.ss_rest_read_check("EXV_CTRL_EXV_A", "100")
        except Exception as e:
            print("EXV_A value verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            PIC6.ss_rest_read_check("EXV_CTRL_EXV_STPA", "3810")
            print("EXV Position status verified")
        except Exception as e:
            print("EXV_A Step value verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            print("Test 6: EXV Eco Position Cri A ")
            A.click(408, 245)  # EXV Eco Position Cri A:
            print("Entering EXV Eco Position Cri A value ")
            A.quick_Test_write("100")  # Write data in to EXV Eco Position Cri A
            time.sleep(30)
            PIC6.ss_rest_read_check("ECO_CTRL_eco_a", "100.000008")
            PIC6.ss_rest_read_check("ECO_CTRL_eco_stpa", "2625")
            print("EXV Eco Position Cri A test is passed")
        except Exception as e:
            print("EXV Eco Position Cri A verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        A.click(780, 452)  # Click on Down Arrow
        try:
            print(" Test 13: Circuit B EXV Position")
            A.click(398, 162)  # click on Circuit B EXV Position box
            print("Entering values to Circuit B EXV Position")
            A.quick_Test_write("100")  # Write the value to Circuit B EXV Position
            time.sleep(30)
            PIC6.ss_rest_read_check("EXV_CTRL_EXV_B", "100")
            PIC6.ss_rest_read_check("EXV_CTRL_EXV_STPB", "3810")
            print("Circuit B EXV Position test is passed")
        except Exception as e:
            print("Circuit B EXV Position test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        try:
            print("Test 15: EXV Eco Position Cri B Test")
            A.click(414, 236)  # Click on EXV Eco Position Cri B box
            print("writing values to EXV Eco Position Cri B")
            A.quick_Test_write("100")  # Write value to EXV Eco Position Cri B
            time.sleep(30)
            PIC6.ss_rest_read_check("ECO_CTRL_eco_b", "100.000008")
            PIC6.ss_rest_read_check("ECO_CTRL_eco_stpb", "2625")
            print("EXV Eco Position Cri B test is passed")
        except Exception as e:
            print("EXV Eco Position Cri A test verification failed")
            failStr = failStr + str(e.args[0]) + '.\n'
        if failStr == "":
            print("EXV Position and EXV Eco Position Circuit Verification Passed Successfully")
        elif failStr != "":
            raise Exception(failStr)
        self.Quick_Disable()

    # def EEM_IO_Table(self):
    #     PIC6.ss_rest_write("TEMP_SPACETMP","25")
    #     PIC6.ss_rest_read_check("TEMP_SPACETMP","25")
    #     PIC6.ss_rest_write("")
    #     PIC6.ss_rest_read_check("")
    #     PIC6.ss_rest_write("")
    #     PIC6.ss_rest_read_check("")
    #     PIC6.ss_rest_write("")
    #     PIC6.ss_rest_read_check("")
    #     PIC6.ss_rest_write("")
    #     PIC6.ss_rest_read_check("")
    #     PIC6.ss_rest_write("")
    #     PIC6.ss_rest_read_check("")
    #     PIC6.ss_rest_write("")
    #     PIC6.ss_rest_read_check("")
    #     PIC6.ss_rest_write("")
    #     PIC6.ss_rest_read_check("")
    #     PIC6.ss_rest_write("")
    #     PIC6.ss_rest_read_check("")
    #     PIC6.ss_rest_write("")
    #     PIC6.ss_rest_read_check("")



