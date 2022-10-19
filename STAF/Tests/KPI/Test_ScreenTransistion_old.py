# Date 19-Aug-2022 
# Developed By: DevendraPhaniKumar 
# Email:Devendra.Manepalli@Carrier.com

from curses.ascii import *
import pyautogui as pa
import subprocess as sp
import paramiko
import time,wmi
import unittest
import pytesseract
import HtmlTestRunner as HT
# Provide pytesseract for the exection software location
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
from PIL import ImageGrab
from win32 import win32gui
Timesess=2
Screendelay=5

class ScreenTransTime(unittest.TestCase):

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

    def test_K01_HomeToAny(self):
        print('*'*25)
        print('K1_HomeToAny Screen Transistion \n')
        self.click(34,37)  # Click Operation on PIC6
        print("Clicked Home Button \n")
        time.sleep(Screendelay)
        self.click(158,39)  # Click Operation on PIC6
        print("Clicked Menu Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,2000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)
    
    def test_K03_AutoTablebackbuttonToMain(self):
        print('*'*25)
        print('K3_AutoTable backbutton To Main Screen Transistion \n')
        self.click(158,39)  # Click Operation on PIC6
        print("Clicked Alarm Screen \n")
        time.sleep(Screendelay)
        self.click(101,32)  # Click Operation on PIC6
        print("Clicked Back Button from Alarm Table Screen \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,2000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)

    def test_K04_HomeToAlarm(self):
        print('*'*25)
        print('K4_HomeToAlarm Screen Transistion \n')
        self.click(34,37)  # Click Operation on PIC6
        print("Clicked Home Button \n")
        time.sleep(Screendelay)
        self.click(763,28)  # Click Operation on PIC6
        print("Clicked Alarm Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,2000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)

    def test_K05_AlarmToHome(self):
        print('*'*25)
        print('K5_AlarmToHome Screen Transistion \n')
        self.click(763,28)  # Click Operation on PIC6
        print("Clicked Alarm Button \n")
        time.sleep(Screendelay)
        self.click(34,37)  # Click Operation on PIC6
        print("Clicked Home Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,2000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)

    def test_K06_HomeToStartStop(self):
        print('*'*25)
        print('K6_HomeToStartStop Screen Transistion \n')
        self.click(34,37)  # Click Operation on PIC6
        print("Clicked Home Button \n")
        time.sleep(Screendelay)
        self.click(710,27)  # Click Operation on PIC6
        print("Clicked StartStop Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()             
        self.assertLess(res,2000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)

    def test_K07_HomeToLogin(self):
        print('*'*25)
        print('K7_HomeToLogin Screen Transistion \n')
        self.click(34,37)  # Click Operation on PIC6
        print("Clicked Home Button \n")
        time.sleep(Screendelay)
        self.click(632,33)  # Click Operation on PIC6
        print("Clicked Loginscreen Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,2000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)

    def test_K08_LoginToPasswordOK(self):
        print('*'*25)
        print('K8_Login To PasswordOK Screen Transistion \n')
        self.click(632,33)  # Click Operation on PIC6
        print("Clicked Loginscreen Button \n")
        time.sleep(Screendelay)
        self.click(145,282) #Pressed Factory Login
        time.sleep(Screendelay)
        self.click(491,164) #Touched to enter the login password
        time.sleep(Screendelay)
        self.click(198,165) #Touched 1
        time.sleep(Screendelay)
        self.click(198,165) #Touched 1
        time.sleep(Screendelay)
        self.click(288,178) #Touched 3
        time.sleep(Screendelay)
        self.click(589,352)  # Click Operation on PIC6
        print("Clicked Done Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,2000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)
    
    def test_K09_AlarmToResetAlarm(self):
        print('*'*25)
        print('K9_Alarm To Reset Alarm Screen Transistion \n')
        self.click(763,28)  # Click Operation on PIC6
        print("Clicked Alarm Button \n")
        time.sleep(Screendelay)
        self.click(121,130)  # Click Operation on PIC6
        print("Clicked ResetAlarm Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,2000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)

    def test_K10_HomeToCircuitA(self):
        print('*'*25)
        print('K10_HomeToCircuitA Screen Transistion \n')
        self.click(34,37)  # Click Operation on PIC6
        print("Clicked Home Button \n")
        time.sleep(Screendelay)
        self.click(336,260)  # Click Operation on PIC6
        print("Clicked CircuitA Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,4000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)

    def test_K11_CircuitAToHome(self):
        print('*'*25)
        print('K11_CircuitAToHome Screen Transistion \n')
        self.click(336,260)  # Click Operation on PIC6
        print("Clicked CircuitA Button \n")
        time.sleep(Screendelay)
        self.click(34,37)  # Click Operation on PIC6
        print("Clicked Home Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,4000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)
    
    def test_K12_ConfigmenuToFactoryConfig(self):
        print('*'*25)
        print('K12_Configuration Menu To Factory Configuration Screen Transistion \n')
        self.click(162,35)  # Click Operation on Menu
        time.sleep(Screendelay)
        self.click(780,468)  # Click on downarrow to go to 2nd screen of menu
        time.sleep(Screendelay)
        self.click(139,132)  # Click Operation on Menu
        print("Clicked Configuration Menu Button \n")
        time.sleep(Screendelay)
        self.click(406,355)  # Click Operation on PIC6
        print("Clicked Factory Configuration Button \n")
        time.sleep(Screendelay)
        res=self.snip_n_grab()
        self.assertLess(res,4000,"Exceed than Expected predefined Time")
        self.click(34,37)  # Click to be at Home Screen
        time.sleep(Screendelay)
    
    # def test_K13_FactoryConfigToReboot(self):
    #     self.click(34,37)  # Click to be at Home Screen
    #     time.sleep(Screendelay)
    #     print('*'*25)
    #     print('K12_Configuration Menu To Factory Configuration Screen Transistion \n')
    #     self.click(162,35)  # Click Operation on Menu
    #     time.sleep(Screendelay)
    #     self.click(780,468)  # Click on downarrow to go to 2nd screen of menu
    #     time.sleep(Screendelay)
    #     self.click(139,132)  # Click Operation on Menu
    #     print("Clicked Configuration Menu Button \n")
    #     time.sleep(Screendelay)
    #     self.click(406,355)  # Click Operation on PIC6
    #     print("Clicked Factory Configuration Button \n")
    #     time.sleep(Screendelay)
    #     res=self.snip_n_grab()
    #     self.assertLess(res,4000,"Exceed than Expected predefined Time")
    #     self.click(34,37)  # Click to be at Home Screen
    #     time.sleep(Screendelay)


    def snip_n_grab(self):
        #Putty Window Application
        snip = win32gui.FindWindow(None, r'169.254.1.1 - PuTTY')
        time.sleep(Timesess)
        #Capturing the dimension of window for screenshot
        dim=win32gui.GetWindowRect(snip)
        #Based on dimesnion it captures the image
        time.sleep(Timesess)
        img=ImageGrab.grab(dim)
        img.show()
        time.sleep(Timesess+3)
        #Converts the captured image to text
        text=pytesseract.image_to_string(img)
        #print(text)
        time.sleep(Timesess+3)
        #print("The Screen transistion Time is: ")
        p=text.find('It took')
        print(p)
        NewText=text[p:p+18].replace(" ",'')
        print(NewText)
        RevNewText=NewText[::-1]
        print(RevNewText)
        time.sleep(Timesess)
        store=''
        for i in RevNewText:
            if i.isdigit():
                store=i+store
        print("The Screen transistion Time is: "+store+" ms")
        print(NewText[p:p+15])
        print(store)
        print('*'*25)
        val=int(store)
        return val
        f = wmi.WMI()
        name='putty.exe'
        for process in f.Win32_Process():
            if process.name == name:
                process.Terminate()

    def start(self):
        self.init()
        # For Code Testing
        # self.click(34,37)
        # self.test_K10_HomeToCircuitA()


if __name__ == '__main__':
    
    c=ScreenTransTime()
    c.start()
    # Launching into Home Screen
    c.click(34,37) 
    # Need Info in Debug Console
    # unittest.main()
    # HTML Report
    unittest.main(testRunner=HT.HTMLTestRunner(output=r'C:\\End to End\\2.ScreenTransistion'))
   
