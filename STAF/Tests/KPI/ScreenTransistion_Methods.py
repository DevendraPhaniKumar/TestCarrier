# Date 19-Aug-2022 
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

class ScreenTransTime:

    def init(self):
        #Launching the Putty Application
        path = "C://Program Files//PuTTY//putty.exe"
        sp.Popen(path)
        time.sleep(Timesess)
        #Entering the Connection ID
        pa.typewrite('169.254.1.1')
        time.sleep(Timesess)
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the User Name to login to the session
        pa.typewrite('app')
        pa.press('enter')
        time.sleep(Timesess)
        #Providing the Password to login to the session
        pa.write('7uR!\!2dxp*t$')
        pa.press('enter')
        time.sleep(Timesess)
        #Passing the Telnet command
        pa.typewrite('telnet 223.254.254.252')
        time.sleep(Timesess)
        pa.press('enter')
        pa.typewrite('cd mnt')
        time.sleep(Timesess)
        pa.press('enter')
        #Tailing the log file as required
        pa.typewrite('tail -f ui.log')
        pa.press('enter')
        time.sleep(Timesess)

    def snip_n_grab(self):
        #Putty Window Application
        snip = win32gui.FindWindow(None, r'169.254.1.1 - PuTTY')
        time.sleep(Timesess)
        #Capturing the dimension of window for screenshot
        dim=win32gui.GetWindowRect(snip)
        #Based on dimesnion it captures the image
        time.sleep(Timesess)
        img=ImageGrab.grab(dim)
        #img.show()
        time.sleep(Timesess+3)
        #Converts the captured image to text
        text=pytesseract.image_to_string(img)
        #print(text)
        time.sleep(Timesess+3)
        #print("The Screen transistion Time is: ")
        p=text.find('It took')
        #print(p)
        NewText=text[p:p+18].replace(" ",'')
        #print(NewText)
        RevNewText=NewText[::-1]
        #print(RevNewText)
        time.sleep(Timesess)
        store=''
        for i in RevNewText:
            if i.isdigit():
                store=i+store
        print("The Screen transistion Time is: "+store+" ms")
        #print(NewText[p:p+15])
        #print(store)
        print('*'*25)
        val=int(store)
        #win32gui.DestroyWindow(snip)
        return val

    def copy(self):
        global ssh
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('169.254.1.1', port=22, username='sdk', password='7uR!\!2dxp*t$')
        
        stdin, stdout, stderr = ssh.exec_command("/home/sdk/CONFIG/Test_Read.sh",timeout=500)
        
        
        time.sleep(5)
        ssh.close()

    def delete(self):
        global ssh
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('169.254.1.1', port=22, username='sdk', password='7uR!\!2dxp*t$')
        
        stdin, stdout, stderr = ssh.exec_command("rm /home/sdk/LOG/copyui.txt")
        
        
        time.sleep(5)
        ssh.close()

    def read_from_file(self):
        time.sleep(5)
        path=r"C:\E2E_HVAC_Testing\STAF\Utility\ScreenTransistion_Logs\copyui.txt"
        with open(path, 'r') as fp:
            # read all lines using readline()
            lines = fp.readlines()
            l=[]
            for row in lines:
                # check if string present on a current line
                word = 'Screen transition complete'
                #print(row.find(word))
                # find() method returns -1 if the value is not found,
                # if found it return 0
                if row.find(word) > 0:
                    #print('string exists in file')
                    #print("line number:"+ str(lines.index(row)))
                    l.append(lines.index(row))
            #print(l)
            #print(l[-1])
            s=l[-1]
            str=lines[s]
            print(str)
            split=str.split()
            val=int(split[6])
            #print(val)
        return val

    def pscp_copy(self):
        path = r"C:\E2E_HVAC_Testing\STAF\Utility\ScreenTransistion_Logs\Test_Read.bat"
        k=sp.Popen(path,stdout=sp.PIPE, shell=True)
        time.sleep(Timesess)

    def start(self):
        #self.init()
        self.pscp_copy()
            
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
# if __name__ == '__main__':
    
#     outputresults=r'C:\E2E_HVAC_Testing\STAF\TestReports'
    #c=ScreenTransTime1()
    #c.start()
    # Launching into Home Screen
    # c.click(34,37) 
    # c.test_K01_HomeToAny()
    # Need Info in Debug Console
    # unittest.main()
    # HTML Report
    #unittest.main(testRunner=HT.HTMLTestRunner(output=outputresults))
    