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


Path = "C:\E2E_HVAC_Testing\STAF\Lib_space\Local_UI\Pic6_7inch_Keypad.xlsx"
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

def init_ssh():
    global ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('169.254.1.1', port=22, username='app', password='7uR!\!2dxp*t$')
    # ssh.connect('169.254.1.1', port=22, username='root', password='X*rD8u!6nk')


def close_ssh():
    global ssh
    ssh.close()


def cmd_ssh(A):
    global ssh
    stdin, stdout, stderr = ssh.exec_command(A)
    lines = stdout.readlines()
    return lines


def dismiss_modal_window():
    global ssh
    stdin, stdout, stderr = ssh.exec_command(
        "echo 'D' | nc.traditional -v -v -n -w 1 -t 223.254.254.252 12349")
    lines = stdout.readlines()
    return lines


def info():
    global ssh
    stdin, stdout, stderr = ssh.exec_command(
        "echo 'i' | nc.traditional -v -v -n -w 1 -t 223.254.254.252 12349")
    lines = stdout.readlines()
    return lines


def reboot_device():
    global ssh
    stdin, stdout, stderr = ssh.exec_command(
        "reboot")
    lines = stdout.readlines()
    return lines

def click(x, y):
    global ssh
    stdin, stdout, stderr = ssh.exec_command(
        "echo 't,{},{}' | nc.traditional -v -v -n -w 1 -t 223.254.254.252 12349".format(x, y))
    time.sleep(8)
    lines = stdout.readlines()
    A =lines
    # return lines
    Z = ['pen_tap('+str(x)+','+str(y)+')'+'\n']
    assertions.assertEqual(Z,A)


def Field_Clear(N):
    for i in range(N):
        click(225, 339)  # Click on Back Space


def Write_Field(Data):
    global Key
    A = list(Data)
    for i in range(len(A)):
        for j in range(len(Key)):
            B = (Key[j])
            Z = str(B[0])
            if A[i] == "/":
                if Z[0] == str(A[i]):
                    click(529, 337)
                    click(int(B[1]), int(B[2]))
                    print(A[i], int(B[1]), int(B[2]))
                    break
            else:
                if Z[0] == str(A[i]):
                    click(int(B[1]), int(B[2]))
                    print(A[i], int(B[1]), int(B[2]))
    click(593, 339)


def quick_Test_write(Data):
    global quick_Table
    Q = list(Data)
    click(408, 303)  # Clear operation on clear button
    for i in range(len(Q)):
        for j in range(len(quick_Table)):
            C = quick_Table[j]
            D = str(C[0])
            if D[0] == str(Q[i]):
                click(int(C[1]), int(C[2]))
    click(410, 341)  # Click operation on Set button
    global read_data


def enable_set(a, b):
    click(a, b)
    click(420, 187)
    click(317, 293)


def disable_set(c, d):
    click(c, d)
    click(256, 187)
    click(317, 293)


def grab_image(name):
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


