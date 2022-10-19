from selenium.webdriver.common.by import By


class LoginPageLocatars(object):
    TITLE = (By.XPATH, "//*[@id='content']/div/div[1]/div")
    EMAIL = (By.XPATH, "//*[@id='input-email']")
    '//*[@id="input-email"]'
    PASSWORD = (By.XPATH, "//*[@id='input-pwd']")
    offline_btn = (By.XPATH,'//*[@id="content"]/div/div[2]/form[1]/div[1]/label/div')
    SUBMIT = (By.XPATH, "//*[@id='content']/div/div[2]/form[1]/button/div/img")
    Email_msg = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/form[1]/section[1]/span[1]/span[1]')
    ERROR_MESSAGE = (By.XPATH, "//*[@id='content']/div/div[2]/span[2]")
    invalid_user_error = (By.XPATH, "//*[@id='content']/div/div[2]/span[2]")
    user_options = (By.XPATH, '//*[@id="top"]/div/div[1]/div/div[4]/ul/li[2]/div[1]/span[2]/button/span')
    user_title = (By.XPATH, '//*[@id="top"]/div[1]/div[1]/div[1]/div[2]/span[3]')
    logout = (By.XPATH, '//*[@id="mydiv"]/div[2]/div[11]/div[2]/button')
    app_version = (By.XPATH, '//*[@id="content"]/div/div[2]/div[1]/div[2]')
    tool_update_close = (By.XPATH,'//*[@id="versionsList"]/div[1]/div[1]/div[3]/ul/li/a')
    tool_update_title = (By.XPATH,'//*[@id="versionsList"]/div[1]/div[1]/div[1]/div[1]')
    tool_updated_ver=(By.XPATH,'//*[@id="versionsList"]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]')
    tool_update_btn = (By.XPATH,'//*[@id="top"]/div/div[1]/div/div[3]/ul/li[3]')
    license_notify = (By.XPATH,'//*[@id="notificationModals"]/div[1]/div[1]/div[1]/div[2]/div[1]')