import pyautogui
import time
import configparser


class HMI_Interaction:
    def __init__(self, HMI_CONTROLLER, HMI_POINTS):
        pyautogui.FAILSAFE = False
        self.hmi_conf_handle = configparser.ConfigParser()
        self.Hwtype = HMI_CONTROLLER
        self.hmi_conf_handle.read(HMI_POINTS)
            
    def __moveTo(self, Button_name):
        data = self.hmi_conf_handle.get("HMI_"+ self.Hwtype,Button_name)
        data = data.split(',')
        return pyautogui.moveTo(int(data[0]), int(data[1]), 2)

    def __Reset(self):
        if self.Hwtype == "PIC5":            
            #click Alarm(BELL) button
            data = self.__moveTo("BELL_BUTTON")                
            time.sleep(0.5)
            pyautogui.click()

            #click Reset Alarms button
            data = self.__moveTo("ALMRESET_BUTTON")        
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(0.5)

            #click Reset-yes/no
            data = self.__moveTo("RESET_YES_BUTTON")        
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(0.5)

            #selecting Reset-yes/no
            data = self.__moveTo("RESET_YES_SEL_BUTTON")
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(0.5)
            
        elif self.Hwtype == "PIC6":
            pass

    def ResetHMIAlarm (self,ser_fac_user_pwd):
        # click Home Button
        data = self.__moveTo("HOME_BUTTON")        
        time.sleep(0.5)
        pyautogui.click()

        #Click Unlock Button
        data = self.__moveTo("UNLOCK_BUTTON")        
        time.sleep(0.5)
        pyautogui.click()

        #provide password
        data = self.__moveTo("PASSWORD")               
        pyautogui.click()
        pyautogui.typewrite(ser_fac_user_pwd)
        pyautogui.press('enter')
        time.sleep(2)

        #click Home Button
        data = self.__moveTo("HOME_BUTTON")        
        time.sleep(0.5)
        pyautogui.click()

        self.__Reset()

        
        #click Thunder button
        data = self.__moveTo("THUNDER_BUTTON")
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)

    def ResetHMI_warning(self):
        data = self.__moveTo("WARNING_BUTTON")        
        time.sleep(1)
        pyautogui.click()
        data = self.__moveTo("WARNING_OK")        
        time.sleep(0.5)
        pyautogui.click()

##    # To select local mode On
##    def HMILocalon(self,ser_fac_user_pwd):
##        # click Home Button
##        pyautogui.moveTo(350, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##
##        #Click Unlock Button
##        pyautogui.moveTo(950,170,2)
##        time.sleep(0.5)
##        pyautogui.click()
##
##        #provide password
##        pyautogui.moveTo(650,490,2)
##        pyautogui.click()
##        pyautogui.typewrite(ser_fac_user_pwd)
##        pyautogui.press('enter')
##        time.sleep(2)
##        # click Home Button
##        pyautogui.moveTo(350, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##
##        # To select power button
##        pyautogui.moveTo(1024, 165, 2)
##        pyautogui.click()
##
##        # To select Local on
##        pyautogui.moveTo(712, 221, 2)
##        pyautogui.click()
##
##    # To select Network mode On
##    def HMINeton(self,ser_fac_user_pwd):
##        # click Home Button
##        pyautogui.moveTo(350, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##
##        # Click Unlock Button
##        pyautogui.moveTo(950, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##
##        # provide password
##        pyautogui.moveTo(650, 490, 2)
##        pyautogui.click()
##        pyautogui.typewrite(ser_fac_user_pwd)
##        pyautogui.press('enter')
##        time.sleep(2)
##        # click Home Button
##        pyautogui.moveTo(350, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##
##        # To select power button
##        pyautogui.moveTo(1024, 165, 2)
##        pyautogui.click()
##
##        # To select Network mode
##        pyautogui.moveTo(703, 368, 2)
##        pyautogui.click()
##
##    # To select Remote mode On
##    def HMIRemoff(self,ser_fac_user_pwd):
##        # click Home Button
##        pyautogui.moveTo(350, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##
##        # Click Unlock Button
##        pyautogui.moveTo(950, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##
##        # provide password
##        pyautogui.moveTo(650, 490, 2)
##        pyautogui.click()
##        pyautogui.typewrite(ser_fac_user_pwd)
##        pyautogui.press('enter')
##        time.sleep(2)
##        # click Home Button
##        pyautogui.moveTo(350, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##        # To select power button
##        pyautogui.moveTo(1024, 165, 2)
##        pyautogui.click()
##        # To select Remote mode
##        pyautogui.moveTo(693, 438, 2)
##        pyautogui.click()
##
##        # To select Confirm stop
##    def HMI_stop(self, ser_fac_user_pwd):
##        # click Home Button
##        pyautogui.moveTo(350, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##        # Click Unlock Buttons
##        pyautogui.moveTo(950, 170, 2)
##        time.sleep(0.5)
##        pyautogui.click()
##
##        # provide password
##        pyautogui.moveTo(650, 490, 2)
##        pyautogui.click()
##        pyautogui.typewrite(ser_fac_user_pwd)
##        pyautogui.press('enter')
##        time.sleep(2)
##
##        # To select power button
##        pyautogui.moveTo(1024, 165, 2)
##        pyautogui.click()
##
##        # To click on confirm stop
##        pyautogui.moveTo(727, 302, 2)
##        pyautogui.click()






