from Lib_space import Local_UI as A
from Lib_space.PIC6_API import rest_frame as PIC6
import time
import configparser
import unittest
assertions = unittest.TestCase('__init__')
TestParameters = configparser.ConfigParser()

class UI:

    def ethernet(self):
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
        A.click(687,205)  # Click on Save Button
        print("Clicking Gateway Block")
        A.click(608,292)  # Click on Gateway block
        print("Clearing previous Gateway...")
        A.Field_Clear(16)  # Clear Previous Data
        print("Entering gateway address")
        A.Write_Field("192.168.100.1")  # Enter Gate Way Address
        print("Clicking Dest/Mask Block")
        A.click(608,329)  # Click on GW1 Dest/Mask block
        print("Clearing Previous Dest/Mask Way Address ")
        A.Field_Clear(16)  # Clear Previous Data
        print("Entering Dest/Mask Way Address")
        A.Write_Field("192.168.0.0/16")  # Enter GW1 Dest/Mask Way Address
        print("Clicking on Not apply Button")
        A.click(419,382)  # Click on Not Apply Button
        print("Clicking on Apply option")
        A.click(398,247)  # Click on  Apply Option
        print("Clicking Down Navigation Arrow")
        A.click(779,449)  # Click on Down Navigation Arrow
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
        A.click(662,334)  # Click on GW1 Dest/Mask block
        print("Clearing Prevoius Desk/Mask Data")
        A.Field_Clear(16)  # Clear Previous Data
        print("Entering Dest/Mask Address")
        A.Write_Field("192.168.0.0/16")  # Enter GW1 Dest/Mask Way Address
        print("Clicking Not Apply Box")
        A.click(388,381)  # Click on Not Apply Button
        print("Selecting Apply Button ")
        A.click(424,252)  # Click on  Apply Option
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
        print("Clicking Back Button to navigate Network Diagnostics Icon") # ************************(Working)
        A.click(99, 26)  # Click on Back Button
        A.click(99, 26)  # Click on Back Button
        A.click(99, 26)  # Click on Back Button
        A.click(99, 26)  # Click on Back Button
        A.click(776, 461)  # Click on Down Arrow
        print("Clicking Network Diagnostics icon ")
        A.click(136, 255)  # Click on Network Diagnostics icon
        print("Clicking Server Address Block")
        A.click(593,198)  # Click on Server Address block
        print("Clearing previous Server Address ")
        A.Field_Clear(16)  # Clear previous Server Address
        print("Entering Server Address")
        A.Write_Field("google.com")  # Enter Server Address
        print("Clicking Interface Block")
        A.click(505,246)  # Click on Interface block
        print("Selecting WLAN 0")
        A.click(405,211)  # Click on Wlan0
        print("Clicking Run Cloud Test")
        A.click(410, 448)  # Click on Run Cloud Test
        print("Clicking Run Ping Test")
        A.click(435,295)  # Click on Run Ping Test
        print("Clicking home Button")
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()

    # Quick Test Table Operations ***************************************************

    def quick_test(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
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
        # TestParameters.read("C:\\End to End\\Python3_app\\Utilities\\TestParamaters.ini")
        # password = TestParameters.get("TEST_PARAMETERS", "factory")
        # A.Write_Field(password)  # Entering Password
        print("Clicking  Home Button")
        A.click(37, 37)  # Click Operation on home Button
        print("Clicking Main Menu Button")
        A.click(156, 33)  # Click Operation on Main Menu
        print("Clicking Down Navigation Arrow")
        A.click(776, 455)  # Click Operation on Down Navigation Arrow
        print("Clicking Quick Test Table Icon")
        A.click(402, 114)  # Click On Quick Test Table Icon
        # print("Quick test 1 st page operations Starting")
        # A.disable_set(504, 124)
        # time.sleep(5)
        PIC6.ss_rest_read_check("GENUNIT_CTRL_TYP", "0")
        # V = PIC6.ss_rest_read("GENUNIT_STATUS")
        # print(V)
        PIC6.ss_rest_read_check("GENUNIT_STATUS","Off     ")
        print("PIC6 in Local Off Mode")
        print("Enabling Quick Test")
        A.enable_set(504, 124)  # Click on EnableQuick Test
        PIC6.ss_rest_read_check("QCK_TEST_QCK_TEST", "1")
        PIC6.ss_rest_read_check("GENUNIT_CTRL_TYP", "0")
        # V = PIC6.ss_rest_read("GENUNIT_STATUS")
        # print(V)
        PIC6.ss_rest_read_check("GENUNIT_STATUS","Test    ")
        print("Quick Test is Enabled Successfully")
        print(" Now PIC6 in Local Test Mode")
        # print("Clicking Down Navigation Arrow")
        A.click(780, 452)  # Click on Down Arrow
        # Page 2 *************************************************************************
        # print("Quick test 2nd page operations starting")
        # print("Clicking Down Navigation Arrow")
        A.click(780, 452)  # Click on Down Arrow
        # Page 3 *************************************************************************
        # print("Quick test 3rd page operations starting")
        print("Enabling Evaporator Heater ")
        A.enable_set(508, 160)  # Evaporator Heater enable
        PIC6.ss_rest_read_check("OUTPUTS_EVAP_HEATER", "1")
        print("Evaporator Heater Enabled Successfully")
        print("Clicking Evaorator Pump1 Box")
        A.click(412, 201)  # click on Evaporator Pump1 box
        print("Entering value to Evaporator Pump 1")
        A.quick_Test_write("1")  # Write value to Evaporator Pump1
        time.sleep(1)
        PIC6.ss_rest_read_check("PUMPSTAT_CPUMP_1", "1")
        print("Evaorator Pump1 is On")
        time.sleep(10)
        PIC6.ss_rest_read_check("PUMPSTAT_CPUMP_1", "0")
        print("Evaorator Pump1 is Off")
        print("Clicking Evaporator Pump2 Box")
        A.click(400, 238)  # click on Evaporator Pump2 box
        print("Writing Value to Evaporator Pump 2")
        A.quick_Test_write("1")  # Write value to Evaporator
        time.sleep(1)
        PIC6.ss_rest_read_check("PUMPSTAT_CPUMP_2", "1")
        print("Evaorator Pump2 is On")
        time.sleep(10)
        PIC6.ss_rest_read_check("PUMPSTAT_CPUMP_2", "0")
        print("Evaorator Pump2 is Off")
        # print("Clicking Down Navigation Arrow Button")
        A.click(780, 452)  # Click on Down Arrow

        # Page 4 *************************************************************************
        # print("Quick test 4th page operations Started")

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
        print("Fan Contactor 1A to 8A are in On Mode")
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
        print("Fan Contactor 1B to 8B are in On Mode")
        A.click(99, 26)  # Click on Back Button
        A.click(402, 114)  # Click On Quick Test Table Icon
        A.disable_set(504, 124)
        print("Quick test is finished")
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()

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
        A.click(148,237) # Click on Bacnet ICon
        print("Clicking on Bacnet Data Link Layer")
        A.click(634,234)
        print("Clicking On Bacnet IP Option")
        A.click(425,257)
        print("Click on Save Button")
        A.click(38 ,460)
        print("BACnet Configuration Completed")
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()
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

    def sample (self):
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
        TestParameters.read(r"C:\E2E_HVAC_Testing\STAF\Utility\TestParamaters.ini")
        password = TestParameters.get("TEST_PARAMETERS", "factory")
        A.Write_Field('113')  # Entering Password
        print("Clicking  Home Button")
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()

    def Clear_Alarm(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()
        # Ethernet 0 Configuration Change *************************************************(Working)
        A.click(37, 37)  # Click Operation on home Button
        print("Clcking on Alaram Icon")
        A.click(761,37)
        print("Clcking on reset Alarm")
        A.click(132,106)
        print("Enabling Alaram Reset ")
        A.enable_set(491,77)
        print("Clicking on Home Button")
        A.click(37, 37)  # Click Operation on home Button
        A.close_ssh()

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
        A.click(696,22)  # Click Operation on Power Icon
        print("Clicking on Local On")
        A.click(439,89)  # Click Operation on Local On Button
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
        A.click(423,253) # Stoping Chiller
        print("Clicking on Home Button")
        A.click(37, 37)  # Click Operation on home Button


