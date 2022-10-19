""""Designed this framework to automate any kind of wpf and win32 desktop application """
import os,sys
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(dirnameutils)
sys.path.append(utils)
sys.path.append(dirnameutils+'\\Lib_space\\WPF_Lib')
print('Dirnameutils is'+dirnameutils)
print('Utils is'+utils)
import pywinauto
import time
from Lib_space.WPF_Lib import Windowsappdetsila
from Lib_space.WPF_Lib import PROVIEWHTMLREPORTGENERATOR
from pywinauto.keyboard import send_keys
import datetime

report = PROVIEWHTMLREPORTGENERATOR.GenerateReport("ProviewdesktopTestreportcustom.HTML")
report.writeTableHeader("Proview-Testreport custom methods")
# report.writeTableHeader("Proview - Test Report")
report.writeToTable(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# app = pywinauto.Application(backend="uia").start(Windowsappdetsila.app)
app = pywinauto.Application(backend="uia").connect(path=r'C:\Program Files (x86)\Carrier\ProView\ProviewDeviceManager\Proview.DeviceManager.exe')
# app.ProViewDeviceManager.set_focus()

def show_app(bestmatch):
    print(f" Bringing {bestmatch} active")
    dlg_app = app.window(best_match='ProView - test CCN')
    dlg_app.restore()

def Doubleclick(locator, controltype, typeoflocator, bestmatch):
    try:
        dlg_app = app.window(best_match=bestmatch)

        if typeoflocator.upper() == "AUTOMATIONID":
            dlg_app.child_window(auto_id=locator, control_type=controltype).double_click_input()
            report.writeToTable("Double click was success on " + locator)
        if typeoflocator.upper() == "TITLE":
            dlg_app.child_window(title=locator, control_type=controltype).double_click_input()
            report.writeToTable("Double click was success on " + locator)

    except Exception as error:
        report.writeToTable(str(error))


def click(locator, controltype, typeoflocator, bestmatch):
    try:
        dlg_app = app.window(best_match=bestmatch)
        time.sleep(3)
        if typeoflocator.upper() == "TITLE":
            dlg_app.child_window(title=locator, control_type=controltype).click()
            report.writeToTable("click was success on " + locator)
        if typeoflocator.upper() == "AUTOMATIONID":
            dlg_app.child_window(auto_id=locator, control_type=controltype).click()
            report.writeToTable("click was success on " + locator)
    except Exception as error:
        report.writeToTable(str(error))


def Screenshot(image):
    try:
        screenshot = app.top_window()
        screenshot.set_focus()
        img = screenshot.capture_as_image()
        img.save(image + ".png")
        report.writeToTable("Screenshot captured and saved")

    except Exception as error:
        report.writeToTable(str(error))


def wait(standardwait):
    try:
        time.sleep(int(standardwait))
        report.writeToTable("Waited for user defined time")

    except Exception as error:
        report.writeToTable(str(error))


def LocatorAccess():
    try:
        locdata = app.dialogs.print_control_identifiers()
        report.writeToTable("Locator data saved on locdatafile")

    except Exception as error:
        report.writeToTable(str(error))


def readingtable(locator, controltype, typeoflocator, bestmatch, input_cond=None):
    try:
        final_res = []
        if typeoflocator.upper() == "AUTOMATIONID":
            dlg = app.Dialog.child_window(auto_id=locator, control_type=controltype)
            # dlg2= app.Dialog.child_window(title="Cooling ECW Setpoint    ", control_type="Text")
            Children_list = dlg.children()
            num_childs = len(Children_list)
            for i in range(0, num_childs):
                templist = dlg.children()[i].descendants(control_type="Text")
                templist2 = []
                for j in templist:
                    templist2.append(((j.texts()[0])).rstrip())
                #report.writeToTable(str(templist2[1]))
                if input_cond != "None":
                    for each_cond in input_cond:
                        if templist2.__contains__(each_cond):
                            test = templist2
                            print(test[1])
                            report.writeToTable("The Value is :" + str(test[1])) ## This line for end to end test case
                            ## later we need to chnage to proview test automation
                        else:
                            pass
                else:
                    print(templist2)

        if typeoflocator.upper() == "TITLE":
            dlg = app.Dialog.child_window(title=locator, control_type=controltype)
            # dlg2= app.Dialog.child_window(title="Cooling ECW Setpoint    ", control_type="Text")
            Children_list = dlg.children()
            num_childs = len(Children_list)
            for i in range(0, num_childs):
                templist = dlg.children()[i].descendants(control_type="Text")
                templist2 = []
                for j in templist:
                    templist2.append(((j.texts()[0])).rstrip())
                #report.writeToTable(str(templist2[1]))
                if input_cond != "None":
                    for each_cond in input_cond:
                        if templist2.__contains__(each_cond):
                            test = templist2
                            print(test[1])
                            report.writeToTable("The Value is :" + str(test[1]))  ## This line for end to end test case
                            ## later we need to chnage to proview test automation
                        else:
                            pass
                else:
                    print(templist2)
    except Exception as error:
        report.writeToTable(str(error))


def closeapp():
    try:
        app.kill()
        report.writeToTable("Application Closed")

    except Exception as error:
        report.writeToTable("error: " + str(error))


def Readcaption(locator, controltype, typeoflocator, bestmatch):
    try:
        dlg_app = app.window(best_match=bestmatch)
        if typeoflocator.upper() == "TITLE":
            Msg = dlg_app.child_window(title=locator, control_type=controltype)
            Label = Msg.legacy_properties()['Name']
            report.writeToTable("Label for" + locator + ": is : " + Label)
        if typeoflocator.upper() == "AUTOMATIONID":
            label = dlg_app.child_window(auto_id=locator, control_type=controltype).wait('exists')
            print(label.get_value())
            report.writeToTable("Label for" + locator + ": is" + label)
    except Exception as error:
        report.writeToTable("error: " + str(error))


def Settext(locator, controltype, typeoflocator, bestmatch, usrinput):
    try:
        if typeoflocator.upper() == "TITLE":
            dlg_app = app.window(best_match=bestmatch)
            dlg_app.child_window(title=locator, control_type=controltype).set_text(usrinput)
            report.writeToTable("Set text was success " + locator)
        if typeoflocator.upper() == "AUTOMATIONID":
            dlg_app = app.window(best_match=bestmatch)
            dlg_app.child_window(auto_id=locator, control_type=controltype).set_text(usrinput)
            report.writeToTable("Set text was success " + locator)

    except Exception as error:
        report.writeToTable("error: " + str(error))


def Keyboardactions(Kebordkey):
    try:
        pywinauto.keyboard.send_keys(Kebordkey)
    except Exception as error:
        report.writeToTable("error: " + str(error))


def doubleclickondialougbox(locator, controltype, typeoflocator, bestmatch):
    try:
        if typeoflocator.upper() == "TITLE":
            app.Dialog.child_window(title=locator, control_type=controltype).double_click_input()
            report.writeToTable("Double click was success on " + locator)
        if typeoflocator.upper() == "AUTOMATIONID":
            app.Dialog.child_window(auto_id=locator, control_type=controltype).double_click_input()
            report.writeToTable("Double click was success on " + locator)
    except Exception as error:
        report.writeToTable("Error: " + str(error))


def Clickondialougebox(locator, controltype, typeoflocator, bestmatch):
    try:
        if typeoflocator.upper() == "TITLE":
            app.Dialog.child_window(title=locator, control_type=controltype).click()
            report.writeToTable("click was success on " + locator)
        if typeoflocator.upper() == "AUTOMATIONID":
            app.Dialog.child_window(auto_id=locator, control_type=controltype).click()
            report.writeToTable("click was success on " + locator)

    except Exception as error:
        report.writeToTable("error: " + str(error))

def Rightclick(locator, controltype, typeoflocator, bestmatch):
    try:
        dlg_app = app.window(best_match=bestmatch)
        time.sleep(3)
        if typeoflocator.upper() == "TITLE":
            dlg_app.child_window(title=locator, control_type=controltype).click_input(button='right')
            report.writeToTable("click was success on " + locator)
        if typeoflocator.upper() == "AUTOMATIONID":
            dlg_app.child_window(auto_id=locator, control_type=controltype).click_input(button='right')
            report.writeToTable("click was success on " + locator)
    except Exception as error:
        report.writeToTable(str(error))


if __name__ == "__main__":
    click()
    Doubleclick()
    Screenshot()
    wait()
    LocatorAccess()
    readingtable()
    closeapp()
    Readcaption()
    Settext()
    Keyboardactions()
    doubleclickondialougbox()
    Clickondialougebox()
