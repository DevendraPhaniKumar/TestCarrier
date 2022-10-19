from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    username = (By.XPATH, "//*[@id='username']")
    password = (By.XPATH, '//*[@id="password"]')
    submit = (By.XPATH, "//button[@type='submit']")
    network_status_section = (By.XPATH, "//a[contains(text(),'Network Status')]")
    valuepath = (By.XPATH, '(*//li)[{0}]/div[3]') # valuepath = '(*//li)[{0}]/div[3]'.format(str(x)) -- need to create a customer function in page action
    keypath = (By.XPATH, "(*//li)[{0}]/div[1]") # keypath = '(*//li)[{0}]/div[1]'.format(str(x)) --- Need to create a customer function in page action
    network_setting_section = (By.XPATH, "//a[contains(text(),'Network Settings')]")
    ipaddress =(By.XPATH, "*//form/div[3]/div/input")
    gateway = (By.XPATH, "*//form/div[5]/div/input")
    subnetmask = (By.XPATH, "*//form/div[4]/div/input")
    saveconfig = (By.XPATH, "(*//button)[13]")
    closepopup = (By.XPATH, '//*[@id="showMessageModal"]/div/div/div[3]/button')
