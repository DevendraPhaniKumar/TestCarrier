# Date 19-Aug-2022 
# Developed By: DevendraPhaniKumar 
# Email:Devendra.Manepalli@Carrier.com

from curses.ascii import *
from doctest import OutputChecker
import wmi
import pyautogui as pa
import subprocess as sp
import paramiko
import time,sys
import unittest
import pytesseract
import HtmlTestRunner as HT
# Provide pytesseract for the exection software location
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
from PIL import ImageGrab
from win32 import win32gui
sys.path.append(r'C:\E2E_HVAC_Testing\STAF')
from Tests.KPI.ScreenTransistion_Methods import ScreenTransTime as STM
Timesess=2
Screendelay=5

class ScreenTransTime7(unittest.TestCase):

    def test_K07_HomeToLogin(self):
        print('*'*25)
        print('K7_HomeToLogin Screen Transistion \n')
        STM.click(self,34,37)  # Click Operation on PIC6
        print("Clicked Home Button \n")
        time.sleep(Screendelay)
        STM.click(self,632,33)  # Click Operation on PIC6
        print("Clicked Loginscreen Button \n")
        time.sleep(Screendelay)
        STM.copy(self)
        STM.pscp_copy(self)
        res=STM.read_from_file(self)
        if res!=0:
            self.assertLess(res,2000,"Exceed than Expected predefined Time")
        if res==0:
            res=10#To simulate the error
            print("Reset your PIC6")
            self.assertLess(res,1,"PIC6 Recodring the '0' values Rest your PIC6 and try again")
        
        STM.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)
        STM.delete(self)
        f = wmi.WMI()
        name='putty.exe'
        for process in f.Win32_Process():
            if process.name == name:
                process.Terminate()
    
   
# if __name__ == '__main__':

#     suite = unittest.TestLoader().loadTestsFromTestCase(ScreenTransTime7)
#     unittest.TextTestRunner(verbosity=1).run(suite)
    
    #outputresults=r'C:\E2E_HVAC_Testing\STAF\TestReports'
    #c=ScreenTransTime1()
    #c.start()
    # Launching into Home Screen
    # c.click(34,37) 
    # c.test_K01_HomeToAny()
    # Need Info in Debug Console
    # unittest.main()
    # HTML Report
    #unittest.main(testRunner=HT.HTMLTestRunner(output=outputresults))
    