import pyautogui
import time

class HMI_Interaction:
    
    def __init__(self):
        pyautogui.FAILSAFE = False

    # click Home Button
    def ResetHMIAlarm (self,ser_fac_user_pwd):
        #pyautogui.moveTo(350,170,2)
        #time.sleep(0.5)
        #pyautogui.click()
        #Click on address bar
        #pyautogui.moveTo(346,47,2)
        time.sleep(0.5)
        #pyautogui.click()
        #pyautogui.press('enter')
##        time.sleep(1)
##        #click on password
##        pyautogui.moveTo(476, 514, 2)
##        pyautogui.click()
##        time.sleep(0.5)
##        # enter on password
##        pyautogui.typewrite(ser_fac_user_pwd)
##        # Click on Login button
##        pyautogui.moveTo(719, 594, 2)
##        pyautogui.click()

        # Click on home button
        pyautogui.moveTo(238, 148, 2)
        time.sleep(0.5)
        pyautogui.click()

        # Click on power
        pyautogui.moveTo(1182, 346, 2)
        time.sleep(0.5)
        pyautogui.click()
        # Click on Reset Alarm
        pyautogui.moveTo(977, 297, 2)
        time.sleep(0.5)
        pyautogui.click()
        # Click on Reset ON
        pyautogui.moveTo(713, 504, 2)
        time.sleep(0.5)
        pyautogui.click()

        #Click Unlock Button
        #pyautogui.moveTo(950,170,2)
        #time.sleep(0.5)
        #pyautogui.click()

        #provide password
        #pyautogui.moveTo(650,490,2)
        #pyautogui.click()
        #pyautogui.typewrite(ser_fac_user_pwd)
        #pyautogui.press('enter')
        #time.sleep(2)

        #click Home Button
        #pyautogui.moveTo(350,170,2)
        #time.sleep(0.5)
        #pyautogui.click()
        #113
        #click Unlock button
        #pyautogui.moveTo(350,580,2)
        #time.sleep(5)
        #pyautogui.click()
        #time.sleep(5)

        #click Alarm(BELL) button
        #pyautogui.moveTo(1075,170,2)
        #time.sleep(0.5)
        #pyautogui.click()

        #click Reset Alarms button
        #pyautogui.moveTo(450,250,2)
        #time.sleep(0.2)
        #pyautogui.click()
        #time.sleep(0.5)

        #click Reset-yes/no
        #pyautogui.moveTo(800,220,2)
        #time.sleep(0.2)
        #pyautogui.click()
        #time.sleep(0.5)

        #selecting Reset-yes/no
        #pyautogui.moveTo(900,370,2)
        #time.sleep(0.1)
        #pyautogui.click()
        #time.sleep(0.5)

        #click Unlock button
        #pyautogui.moveTo(350,580,2)
        #time.sleep(0.5)
        #pyautogui.click()
        #time.sleep(1)

    def ResetHMI_warning(self):
        #pyautogui.moveTo(350,140,2)
        time.sleep(1)
        #pyautogui.click()
        #pyautogui.moveTo(550,550,5)
        #time.sleep(0.5)
        #pyautogui.click()

    # To select local mode On

    def HMILocalon(self,ser_fac_user_pwd):
        # Click on address bar
        pyautogui.moveTo(346, 47, 2)
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.press('enter')
        time.sleep(1)
        # click on password
        pyautogui.moveTo(476, 514, 2)
        pyautogui.click()
        time.sleep(0.5)
        # enter on password
        pyautogui.typewrite(ser_fac_user_pwd)
        # Click on Login button
        pyautogui.moveTo(719, 594, 2)
        pyautogui.click()

        # Click on home button
        pyautogui.moveTo(238, 148, 2)
        time.sleep(0.5)
        pyautogui.click()

        # Click on Power 2
        pyautogui.moveTo(257, 686, 2)
        time.sleep(0.5)
        pyautogui.click()


        # Click on Local ON
        pyautogui.moveTo(656, 251, 2)
        time.sleep(0.5)
        pyautogui.click()
        # click Home Button
        #pyautogui.moveTo(350, 170, 2)
        #time.sleep(0.5)
        #pyautogui.click()

        #Click Unlock Button
        #pyautogui.moveTo(950,170,2)
        #time.sleep(0.5)
        #pyautogui.click()

        #provide password
        #pyautogui.moveTo(650,490,2)
        #pyautogui.click()
        #pyautogui.typewrite(ser_fac_user_pwd)
        #pyautogui.press('enter')
        #time.sleep(2)
        # click Home Button
        #pyautogui.moveTo(350, 170, 2)
        #time.sleep(0.5)
        #pyautogui.click()

        # To select power button
        #pyautogui.moveTo(1024, 165, 2)
        #pyautogui.click()

        # To select Local on
        #pyautogui.moveTo(712, 221, 2)
        #pyautogui.click()

    # To select Network mode On
    def HMINeton(self,ser_fac_user_pwd):
        # click Home Button
        pyautogui.moveTo(350, 170, 2)
        time.sleep(0.5)
        pyautogui.click()

        # Click Unlock Button
        pyautogui.moveTo(950, 170, 2)
        time.sleep(0.5)
        pyautogui.click()

        # provide password
        pyautogui.moveTo(650, 490, 2)
        pyautogui.click()
        pyautogui.typewrite(ser_fac_user_pwd)
        pyautogui.press('enter')
        time.sleep(2)
        # click Home Button
        pyautogui.moveTo(350, 170, 2)
        time.sleep(0.5)
        pyautogui.click()

        # To select power button
        pyautogui.moveTo(1024, 165, 2)
        pyautogui.click()

        # To select Network mode
        pyautogui.moveTo(703, 368, 2)
        pyautogui.click()

    # To select Remote mode On
    def HMIRemoff(self,ser_fac_user_pwd):
        # click Home Button
        pyautogui.moveTo(350, 170, 2)
        time.sleep(0.5)
        pyautogui.click()

        # Click Unlock Button
        pyautogui.moveTo(950, 170, 2)
        time.sleep(0.5)
        pyautogui.click()

        # provide password
        pyautogui.moveTo(650, 490, 2)
        pyautogui.click()
        pyautogui.typewrite(ser_fac_user_pwd)
        pyautogui.press('enter')
        time.sleep(2)
        # click Home Button
        pyautogui.moveTo(350, 170, 2)
        time.sleep(0.5)
        pyautogui.click()
        # To select power button
        pyautogui.moveTo(1024, 165, 2)
        pyautogui.click()
        # To select Remote mode
        pyautogui.mov113
        eTo(693, 438, 2)
        pyautogui.click()

        # To select Confirm stop
    # To turn unit to local off
    def HMILocaloff(self,ser_fac_user_pwd):
        # Click on address bar
        pyautogui.moveTo(346, 47, 2)
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.press('enter')
        time.sleep(1)
        # click on password
        pyautogui.moveTo(476, 514, 2)
        pyautogui.click()
        time.sleep(0.5)
        # enter on password
        pyautogui.typewrite(ser_fac_user_pwd)
        # Click on Login button
        pyautogui.moveTo(719, 594, 2)
        pyautogui.click()

        # Click on home button
        pyautogui.moveTo(238, 148, 2)
        time.sleep(0.5)
        pyautogui.click()

        # Click on Power 2
        pyautogui.moveTo(257, 686, 2)

        time.sleep(0.5)
        pyautogui.click()

        # Click on Local off
        pyautogui.moveTo(673, 454, 2)
        time.sleep(0.5)
        pyautogui.click()

    def HMI_stop(self, ser_fac_user_pwd):
        # click Home Button
        pyautogui.moveTo(350, 170, 2)
        time.sleep(0.5)
        pyautogui.click()
        # Click Unlock Buttons
        pyautogui.moveTo(950, 170, 2)
        time.sleep(0.5)
        pyautogui.click()

        # provide password
        pyautogui.moveTo(650, 490, 2)
        pyautogui.click()
        pyautogui.typewrite(ser_fac_user_pwd)
        pyautogui.press('enter')
        time.sleep(2)

        # Click on Power 2
        pyautogui.moveTo(257, 686, 2)
        pyautogui.click()

        # To click on confirm stop
        pyautogui.moveTo(673, 454, 2)
        time.sleep(0.5)
        pyautogui.click()






