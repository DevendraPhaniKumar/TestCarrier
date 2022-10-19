from selenium.webdriver.common.by import By


class MainPageLocatars(object):
    TITLE = (By.XPATH, "//*[@id='content']/div/div[1]/div")
    LOGO = (By.ID, 'nav-logo')
