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
PIC6 = PIC6_Rest_Utility.Rest_Utility()


class Application_Test():

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
        elif failStr !="":
            raise Exception(failStr)
        self.Quick_Disable()






