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
import subprocess,time
import pyautogui as pg
import pywinauto as pw
Timesess=2
Screendelay=5
from datetime import datetime

start=datetime.now()

print("now is "+str(start))

current_time=start.strftime("%H:%M:%S")

print("current is:"+str(current_time))
# class ScreenTransTime1(unittest.TestCase):

#     def init(self):
        #Launching the Putty Application
#subprocess.call(r'C:\Users\ManepaDP\E2E%20HVAC%20Testing\STAF\Test_Read.bat')

# pg.typewrite('7uR!\!2dxp*t$')

# print("Finished ..its")

# time.sleep(Timesess)

# file_path = 'randomfile.txt'

# file_text = open(file_path, "r")

# a = True

# while a:
#     file_line = file_text.readline()
#     if not file_line:
#         print("End Of File")
#         a = False

# file_text.close()

# global ssh
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('169.254.1.1', port=22, username='sdk', password='7uR!\!2dxp*t$')
                
# stdin, stdout, stderr = ssh.exec_command("rm /home/sdk/LOG/copyui.txt")
# #stdin, stdout, stderr = ssh.exec_command("/home/sdk/CONFIG/Test_Read.sh",timeout=500)

# print("Finished") 
# print(stdout.read())        
                
# time.sleep(8)
# ssh.close()