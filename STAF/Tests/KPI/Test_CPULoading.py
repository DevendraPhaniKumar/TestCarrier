# Date 19-Sep-2022
# Developed By: DevendraPhaniKumar 
# Email:Devendra.Manepalli@Carrier.com

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
shiftnew=60

class CPULoading(unittest.TestCase):

    def init(self):
        #Launching the Putty Application
        path = "C://Program Files//PuTTY//putty.exe"
        k=sp.Popen(path,stdout=sp.PIPE, shell=True)
        time.sleep(Timesess)
        #Entering the Connection ID
        pa.typewrite('169.254.1.1')
        time.sleep(Timesess)
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the User Name to login to the session
        pa.typewrite('sdk')
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the Password to login to the session
        pa.typewrite('7uR!\!2dxp*t$')
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the User Name to login to the session su root
        pa.typewrite('su root')
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the Password to login to the session
        pa.typewrite('X*rD8u!6nk')
        pa.press('enter')
        time.sleep(Timesess)
        pa.typewrite('cd /home/data/global')
        time.sleep(Timesess)
        pa.press('enter')
        pa.typewrite('chmod 777 burn_cpu_cycle')
        time.sleep(Timesess)
        pa.press('enter')
        pa.typewrite('chown sdk:sdk burn_cpu_cycle')
        time.sleep(Timesess)
        pa.press('enter')
        pa.typewrite('ls -lrt')
        time.sleep(Timesess)
        pa.press('enter')
        pa.typewrite('./burn_cpu_cycle 50')
        pa.press('enter')
        time.sleep(Timesess)
        self.cpu60()
        self.newsession()
        #Time of 24Hrs for every CPU Loading
        #time.sleep(1*24*60*60) 
        time.sleep(1)
        self.Closesession()

    def Closesession(self):
        f = wmi.WMI()
        name='putty.exe'
        for process in f.Win32_Process():
            if process.name == name:
                process.Terminate()


    def newsession(self):
        #Launching the Additoinal Putty Application
        path = "C://Program Files//PuTTY//putty.exe"
        k=sp.Popen(path,stdout=sp.PIPE, shell=True)
        time.sleep(Timesess)
        #Entering the Connection ID
        pa.typewrite('169.254.1.1')
        time.sleep(Timesess)
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the User Name to login to the session
        pa.typewrite('sdk')
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the Password to login to the session
        pa.typewrite('7uR!\!2dxp*t$')
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the User Name to login to the session su root
        pa.typewrite('su root')
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the Password to login to the session
        pa.typewrite('X*rD8u!6nk')
        pa.press('enter')
        time.sleep(Timesess)
        pa.typewrite('htop')
        pa.press('enter')
        time.sleep(Timesess)

    def click(self, x, y):
        global ssh
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('169.254.1.1', port=22, username='app', password='7uR!\!2dxp*t$')
        
        stdin, stdout, stderr = ssh.exec_command(
                    "echo 't,{},{}' | nc.traditional -v -v -n -w 1 -t 223.254.254.252 12349".format(x, y))
        time.sleep(8)
        lines = stdout.readlines()
        A = lines
        # return lines
        Z = ['pen_tap(' + str(x) + ',' + str(y) + ')' + '\n']
        ssh.close()

    def puttytransitions(self):
        #print('*'*25)
        #print('K1_HomeToAny Screen Transistion \n')
        self.click(34,37)  # Click Operation on PIC6
        #print("Clicked Home Button \n")
        time.sleep(Screendelay)
        self.click(158,39)  # Click Operation on PIC6
        #print("Clicked Menu Button \n")
        time.sleep(Screendelay)
    
    # def webuitransitions(self):
    #     print("The webui script to be prepared")
    
    def loadbacnet(self):
        print("The Bacnet loading script to be prepared")
    
    # def loadccn(self):
    #     print("The CCN loading script to be prepared")

    # def loadmodbus(self):
    #     print("The Modbus loading script to be prepared")

    # def loadfromproview(self):
    #     print("The ProviewApp loading script to be prepared")

    def cpu60(self):
        #initial it is 60sec delay
        time.sleep(shiftnew)
        pa.keyDown('ctrl')
        pa.keyDown('c')
        pa.keyUp('c')
        pa.keyUp('ctrl')
        pa.press('enter')
        time.sleep(Timesess)
        pa.typewrite('./burn_cpu_cycle 60')
        pa.press('enter')
        time.sleep(Timesess)
    
    def cpu70(self):
        #initial it is 60sec delay
        time.sleep(shiftnew)
        pa.keyDown('ctrl')
        pa.keyDown('c')
        pa.keyUp('c')
        pa.keyUp('ctrl')
        pa.press('enter')
        time.sleep(Timesess)
        pa.typewrite('./burn_cpu_cycle 70')
        pa.press('enter')
        time.sleep(Timesess)
    
    def cpu80(self):
        #initial it is 60sec delay
        time.sleep(shiftnew)
        pa.keyDown('ctrl')
        pa.keyDown('c')
        pa.keyUp('c')
        pa.keyUp('ctrl')
        pa.press('enter')
        time.sleep(Timesess)
        pa.typewrite('./burn_cpu_cycle 80')
        pa.press('enter')
        time.sleep(Timesess)

    def cpu85(self):
        #initial it is 60sec delay
        time.sleep(shiftnew)
        pa.keyDown('ctrl')
        pa.keyDown('c')
        pa.keyUp('c')
        pa.keyUp('ctrl')
        pa.press('enter')
        time.sleep(Timesess)
        pa.typewrite('./burn_cpu_cycle 85')
        pa.press('enter')
        time.sleep(Timesess)
    
    def cpu90(self):
        #initial it is 60sec delay
        time.sleep(shiftnew)
        pa.keyDown('ctrl')
        pa.keyDown('c')
        pa.keyUp('c')
        pa.keyUp('ctrl')
        pa.press('enter')
        time.sleep(Timesess)
        pa.typewrite('./burn_cpu_cycle 90')
        pa.press('enter')
        time.sleep(Timesess)
    
    def cpu95(self):
        #initial it is 60sec delay
        time.sleep(shiftnew)
        pa.keyDown('ctrl')
        pa.keyDown('c')
        pa.keyUp('c')
        pa.keyUp('ctrl')
        pa.press('enter')
        time.sleep(Timesess)
        pa.typewrite('./burn_cpu_cycle 95')
        pa.press('enter')
        time.sleep(Timesess)

if __name__ == '__main__':
    
    c=CPULoading()
    c.Closesession()
    c.init()
    # c.newsession()
    # Launching into Home Screen
    # c.click(34,37) 
    # c.test_K01_HomeToAny()
    # Need Info in Debug Console
    # unittest.main()
    # HTML Report
    # unittest.main(testRunner=HT.HTMLTestRunner(output=r'C:\\End to End\\2.ScreenTransistion'))
    

        



