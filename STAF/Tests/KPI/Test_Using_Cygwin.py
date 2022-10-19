# Date 12-Aug-2022 
# Developed By: DevendraPhaniKumar 
# Email:Devendra.Manepalli@Carrier.com

import time,os,sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui
import subprocess
import unittest

class FwTestCygwin(unittest.TestCase):

    def test_FWwithCygwin(self):
        tic=time.perf_counter()
        subprocess.call(r'C:\End to End\pic6_upgrade_utility\upgrade.bat')
        desired_capabilities = DesiredCapabilities.CHROME.copy()
        desired_capabilities['acceptInsecureCerts'] = True
        driver = webdriver.Chrome(executable_path=r'C:\E2E_HVAC_Testing\STAF\Utility\WEB_Drivers\chromedriver.exe',desired_capabilities=desired_capabilities)
        driver.get('https://169.254.1.1/PIC6/#/loading')

        timeout = 15
        try:
            element_present = EC.presence_of_element_located((By.XPATH,"//*[@id='s_0w_112']"))
            #Alternate ID To check it -DPK
            #element_present = EC.presence_of_element_located((By.XPATH,'//*[@ng-app="pic-app"]'))
            WebDriverWait(driver, timeout).until(element_present)
            print("founded")
            toc=time.perf_counter()
        except TimeoutException:
            print ("Timed out waiting for page to load")

        driver.close()

        # Print the Difference Minutes and Seconds
        # print(f"Build finished in {(toc - tic)/60:0.0f} minutes {(toc - tic)%60:0.0f} seconds")
        # For additional Precision
        print(f"Build finished in {toc - tic:0.4f} seconds")
        FWTime=toc - tic
        self.assertLess(int(FWTime),240,"Build Took more than 240seconds")

if __name__ == '__main__':
    # Need Info in Debug Console
    unittest.main()
    # HTML Report
    # unittest.main(testRunner=HT.HTMLTestRunner(output=r'C:\E2E_HVAC_Testing\STAF\TestReports'))
