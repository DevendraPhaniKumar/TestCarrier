import os
import sys
import time
import paramiko
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import pyautogui
import xlrd
import unittest

assertions = unittest.TestCase('__init__')
global ssh
global Key
global quick_Table

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# print(dirnameutils+"\Data\APPLICATION\Pic6_7inch_Keypad.xlsx")
print(dirnameutils)

Path = dirnameutils + "\Data\APPLICATION\Pic6_7inch_Keypad.xlsx"
print(Path)
WB = xlrd.open_workbook(Path)

Key = []
quick_Table = []

for i in range(WB.nsheets):
    WS = WB.sheet_by_index(i)
    if i == 0:
        for j in range(WS.nrows):
            Key.append(WS.row_values(j))
    else:
        for l in range(WS.nrows):
            quick_Table.append(WS.row_values(l))


class UI_Touch():

    def init_ssh(self):
        global ssh
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('169.254.1.1', port=22, username='app', password='7uR!\!2dxp*t$')
        # ssh.connect('169.254.1.1', port=22, username='root', password='X*rD8u!6nk')

    def close_ssh(self):
        global ssh
        ssh.close()

    def cmd_ssh(self, A):
        global ssh
        stdin, stdout, stderr = ssh.exec_command(A)
        lines = stdout.readlines()
        return lines

    def dismiss_modal_window(self):
        global ssh
        stdin, stdout, stderr = ssh.exec_command(
            "echo 'D' | nc.traditional -v -v -n -w 1 -t 223.254.254.252 12349")
        lines = stdout.readlines()
        return lines

    def info(self):
        global ssh
        stdin, stdout, stderr = ssh.exec_command(
            "echo 'i' | nc.traditional -v -v -n -w 1 -t 223.254.254.252 12349")
        lines = stdout.readlines()
        return lines

    def reboot_device(self):
        global ssh
        stdin, stdout, stderr = ssh.exec_command(
            "reboot")
        lines = stdout.readlines()
        return lines

    def click(self, x, y):
        global ssh
        stdin, stdout, stderr = ssh.exec_command(
            "echo 't,{},{}' | nc.traditional -v -v -n -w 1 -t 223.254.254.252 12349".format(x, y))
        time.sleep(8)
        lines = stdout.readlines()
        A = lines
        # return lines
        Z = ['pen_tap(' + str(x) + ',' + str(y) + ')' + '\n']
        assertions.assertEqual(Z, A)

    def Field_Clear(self, N):
        for i in range(N):
            self.click(225, 339)  # Click on Back Space

    def Write_Field(self, Data):
        global Key
        A = list(Data)
        for i in range(len(A)):
            for j in range(len(Key)):
                B = (Key[j])
                Z = str(B[0])
                if A[i] == "/":
                    if Z[0] == str(A[i]):
                        self.click(529, 337)
                        self.click(int(B[1]), int(B[2]))
                        print(A[i], int(B[1]), int(B[2]))
                        break
                else:
                    if Z[0] == str(A[i]):
                        self.click(int(B[1]), int(B[2]))
                        print(A[i], int(B[1]), int(B[2]))
        self.click(593, 339)

    def quick_Test_write(self, Data):
        global quick_Table
        Q = list(Data)
        self.click(408, 303)  # Clear operation on clear button
        for i in range(len(Q)):
            for j in range(len(quick_Table)):
                C = quick_Table[j]
                D = str(C[0])
                if D[0] == str(Q[i]):
                    self.click(int(C[1]), int(C[2]))
        self.click(410, 341)  # Click operation on Set button
        global read_data

    def enable_set(self, a, b):
        self.click(a, b)
        self.click(420, 187)
        self.click(317, 293)

    def disable_set(self, c, d):
        self.click(c, d)
        self.click(256, 187)
        self.click(317, 293)

    def grab_image(self, name):
        global ssh
        stdin, stdout, stderr = ssh.exec_command("nohup ./rea_screenshot.sh > /dev/null &")
        lines = stdout.readlines()
        caps = DesiredCapabilities.INTERNETEXPLORER
        caps['ignoreProtectedModeSettings'] = True
        ddr = webdriver.Ie("IEDriverServer.exe", capabilities=caps)
        ddr.get("http://169.254.1.1:10080/")
        time.sleep(3)
        pyautogui.screenshot("{}.png".format(name), region=(0, 0, 900, 600))
        pyautogui.leftClick('close.png')
        return lines
