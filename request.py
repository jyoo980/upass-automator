from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import getpass
import sys
import page_elements

target_url = "https://upassbc.translink.ca/"
XPATH_UBC = page_elements.XPATHS_UBC
XPATH_UPASS = page_elements.XPATH_UPASS

def setup_webdriver():
    driver = webdriver.Chrome()
    driver.get(target_url)
    return driver

def ubc_login(driver, username, password):
    username_field = driver.find_element_by_xpath(XPATH_UBC["username_field"])
    username_field.clear()
    username.send_keys(username)
    password_field = driver.find_element_by_xpath(XPATH_UBC["password_field"])
    password_field.clear()
    password_field.send_keys(password)
    driver.find_element_by_xpath(XPATH_UBC["login"]).click()

def select_ubc_upass(driver):
    driver.find_element_by_xpath(XPATH_UPASS["school_select"]).click()
    driver.find_element_by_xpath(XPATH_UPASS["ubc"]).click()
    element = driver.find_element_by_id("//*[@id='goButton']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element_by_xpath(XPATH_UPASS["ok"]).click()

def request_ubc_upass(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH_UPASS["checkbox"])))
    checkbox = driver.find_element_by_xpath(XPATH_UPASS["checkbox"])
    actions = ActionChains(driver)
    actions.move_to_element(checkbox).perform()
    checkbox.click()
    driver.find_element_by_xpath(XPATH_UPASS["request_pass"]).click()

def request_script():
    ubc_username = input("Please enter your ubc id: ")
    ubc_password = getpass.getpass("Please enter your ubc password: ")
    driver = setup_webdriver()
    select_ubc_upass(driver)
    ubc_login(driver, ubc_username, ubc_password)
    request_ubc_upass(driver)

request_script()