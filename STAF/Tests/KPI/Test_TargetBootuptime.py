from email.errors import StartBoundaryNotFoundDefect
import re
from tracemalloc import start
import paramiko,time
from curses.ascii import *
import wmi
import pyautogui as pa
import subprocess as sp
import paramiko
import time
import unittest
import pytesseract
import HtmlTestRunner as HT
# Provide pytesseract for the exection software location
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
from PIL import ImageGrab
from win32 import win32gui
Timesess=2
Screendelay=5
waittime=5
from datetime import datetime


class TargetBootuptime(unittest.TestCase):

    def reboot(self):
        global ssh
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('169.254.1.1', port=22, username='sdk', password='7uR!\!2dxp*t$')
        
        stdin, stdout, stderr = ssh.exec_command("reboot -f")
        start=datetime.now()
        current_time=start.strftime("%H:%M:%S")
        #print("current is:"+str(current_time))
        time.sleep(10)
        ssh.close()
        return current_time

    def test_targetbootuptime(self):
        
        print("Please ensure your PIC6 is synced with the timezone as similar to computer which is running the script")
        starttime=self.reboot()
        print("Reboot start time is : "+starttime)
        self.pscp_copy()
        time.sleep(2)
        stoptime=self.read_from_file()
        print("Captured target time is : "+stoptime)
        timetakenS=int(starttime[6:8])-int((str(stoptime))[6:8])
        timetakenM=int(starttime[3:5])-int((str(stoptime))[3:5])
        timetakenH=int(starttime[0:2])-int((str(stoptime))[0:2])

        print("The time taken for the application Bootup is:"+str(timetakenH)+"Hour "+str(timetakenM)+"Min "+str(timetakenS)+"Sec")
    
    def pscp_copy(self):
        #Provide the script name that copies the file here"
        path = r"C:\E2E_HVAC_Testing\STAF\Utility\BootupTime\Boot_Test_Read.bat"
        k=sp.Popen(path,stdout=sp.PIPE, shell=True)
        time.sleep(Timesess)

    def read_from_file(self):
        time.sleep(5)
        "Provide the path name of the file from where we have to read the data"
        path=r"C:\E2E_HVAC_Testing\STAF\Utility\BootupTime\PIC6_app_stert_time_stamp"
        with open(path, 'r') as fp:
            # read all lines using readline()
            lines = fp.readlines()
            #print(lines)
            l=[]
            for row in lines:
                l.append(row[-9:-1])
                #print(l)
           
            #print(l[0])
    
        return l[0]


if __name__ == '__main__':
    
    c=TargetBootuptime()
    c.test_Targetbootuptime()
    # Launching into Home Screen
    # c.click(34,37) 
    # c.test_K01_HomeToAny()
    # Need Info in Debug Console
    # unittest.main()
    # HTML Report
    # unittest.main(testRunner=HT.HTMLTestRunner(output=r'C:\\End to End\\2.ScreenTransistion'))
