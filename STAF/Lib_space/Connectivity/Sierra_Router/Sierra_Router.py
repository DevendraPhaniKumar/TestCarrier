import time
import unittest
import os, sys
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(dirname)
print("It is........"+dirname)
from Lib_space.Connectivity.Sierra_Router.BaseClass import WebDriver


class Fx30:

    global driver

    def __init__(self):
        dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        print("It is........"+dirnameutils)
        self.TestParameters = configparser.ConfigParser()
        self.TestParameters.read(dirnameutils + "\\Utility\\parameter_connectedservice.ini")
        self.User = self.TestParameters.get("SIERRA_ROUTER_PARAMETERS", "fx30_user")
        self.passW = self.TestParameters.get("SIERRA_ROUTER_PARAMETERS", "fx30_pass")
        self.target_url = self.TestParameters.get("SIERRA_ROUTER_PARAMETERS", "fx30_target_url")
        self.driver = WebDriver.same_driver
        self.driver.maximize_window()
        self.driver.get(self.target_url)
        time.sleep(5)

    def login(self):
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys(self.User)
        x = self.driver.find_element_by_xpath("//*[@id='username']")
        x.send_keys(Keys.TAB + self.passW)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        print("Successfully logged in to the Sierra router")

    def network_status(self):
        # click and open the network status section
        network_status_section_xpath = "//a[contains(text(),'Network Status')]"
        network_status = self.driver.find_element_by_xpath(network_status_section_xpath)
        network_status.click()
        time.sleep(10)
        my_dict = {}
        for x in range(12):
            try:
                keypath = '(*//li)[{0}]/div[1]'.format(str(x))
                valuepath = '(*//li)[{0}]/div[3]'.format(str(x))
                key = self.driver.find_element_by_xpath(keypath).text
                value = self.driver.find_element_by_xpath(valuepath).text
                my_dict.update({key: value})
                print(key, " : ",value )
            except:
                pass
        return my_dict

    def network_settings(self):
        # click and open the network settings section
        network_setting_section_xpath = "//a[contains(text(),'Network Settings')]"
        network_setting = self.driver.find_element_by_xpath(network_setting_section_xpath)
        network_setting.click()
        time.sleep(5)

        # return below variables to PIC6 APP
        dns1 = dns2 = gateway_ip = "192.168.1.2"
        gateway_mask = "0.0.0.0/0"
        pic6_eth1_ipaddress = "192.168.1.10"
        pic6_eth1_subnetmask = "255.255.0.0"

        # Ip address
        ipaddress_xpath = "*//form/div[3]/div/input"
        ipaddress = self.driver.find_element_by_xpath(ipaddress_xpath)

        # setIpaddress
        ipaddress.clear()
        ipaddress.send_keys("192.168.1.2")
        time.sleep(2)

        # gateway not required for pic6
        gateway_xpath = "*//form/div[5]/div/input"
        gateway = self.driver.find_element_by_xpath(gateway_xpath)

        # set gateway
        gateway.clear()
        gateway.send_keys("0.0.0.0")
        time.sleep(2)

        # subnet mask
        subnetmask_xpath = "*//form/div[4]/div/input"
        subnetmask = self.driver.find_element_by_xpath(subnetmask_xpath)

        # set gateway
        subnetmask.clear()
        subnetmask.send_keys("255.255.0.0")
        time.sleep(2)

        # save configuration
        saveconfig_xpath = "(*//button)[13]"
        saveconfig = self.driver.find_element_by_xpath(saveconfig_xpath)
        saveconfig.click()
        time.sleep(5)

        # close popup
        closepopup_xpath = '//*[@id="showMessageModal"]/div/div/div[3]/button'
        closepopup = self.driver.find_element_by_xpath(closepopup_xpath)
        closepopup.click()
        time.sleep(5)

        dns1 = dns2 = gateway_ip = ipaddress.get_attribute('value')
        pic6_eth1_subnetmask = subnetmask.get_attribute('value')
        print("type", type(dns1), type(dns2), type(gateway_ip))
        gateway_mask = "0.0.0.0/0" # has to be manual
        pic6_eth1_ipaddress = "192.168.1.10" # has to be manual
        print(pic6_eth1_ipaddress, pic6_eth1_subnetmask, gateway_ip, gateway_mask, dns1, dns2)

        return pic6_eth1_ipaddress, pic6_eth1_subnetmask, gateway_ip, gateway_mask, dns1, dns2

    def close_browser(self):
        self.driver.quit()
        print("Sierra Router(FX30) web session is closed")


if __name__ == '__main__':
    test = Fx30()
    Fx30.login(self=test)
    Fx30.network_status(self=test)
    Fx30.network_settings(self=test)
    Fx30.close_browser(self=test)


'''

class SierraRouterTests(unittest.TestCase):

    def setup(self):
        print("***SIERRA CONFIGURATION TEST***")
        pass

    def test_sierra_smart_configuration(self):
        # Checking the internet connection
        sierra_configuration()
        self.assertEqual('Yes', my_dict['Connected to Internet'], "Sierra **NOT** connected to Internet")
        network_settings()

    def tearDown(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SierraRouterTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

'''