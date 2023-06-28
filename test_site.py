# libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# constants
URL='https://www.saucedemo.com/'
NAME='standard_user'
PASSWORD='secret_sauce'

# functions
def get_element_by_id(driver,locator):
    return driver.find_element(By.ID, locator)

def element_click(driver,locator):
    element=get_element_by_id(driver,locator)
    element.click()

def element_send_keys(driver,locator,text):
    element = get_element_by_id(driver,locator)
    element.send_keys(text)



def open_login_page():
    element_click(driver,'user-name')

def login(driver,name,password):
        element_send_keys(driver,'user-name',name)
        element_send_keys(driver,'password',password)
        element_click(driver,'login-button')


# code
driver.get(URL)
element_click(driver,'user-name')

open_login_page()
login(driver,NAME,PASSWORD)

# end
driver.quit()