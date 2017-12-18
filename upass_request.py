from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import getpass
import sys

target_url = "https://upassbc.translink.ca/"

ubc_username = input("Please enter your ubc id: ")
ubc_password = getpass.getpass("Please enter your ubc password: ")

xpaths_upass = { 'schoolSelect' : "//*[@class='hasCustomSelect']", 
				 'ubcSelect' : "//*[contains(@value, 'ubc')]",
				 'ok' : "//*[@id='goButton']",
				 'chkBox' : "//*[@id='chk_1']",
				 'requestBtn' : "//*[@id='requestButton']"
}

xpaths_ubc = { 'username_box' : "//*[@id='j_username']",
			   'password_box' : "//*[@id='password']",
			   'login' : "//*[@value='Continue']"
}

driver = webdriver.Chrome()
driver.get(target_url)
driver.maximize_window()

# Select UBC from the selection dropdown, click 'ok'
driver.find_element_by_xpath(xpaths_upass['schoolSelect']).click()
driver.find_element_by_xpath(xpaths_upass['ubcSelect']).click()
driver.find_element_by_xpath(xpaths_upass['ok']).click()

# Fill in UBC credentials
driver.find_element_by_xpath(xpaths_ubc['username_box']).clear()
driver.find_element_by_xpath(xpaths_ubc['username_box']).send_keys(ubc_username)
driver.find_element_by_xpath(xpaths_ubc['password_box']).clear()
driver.find_element_by_xpath(xpaths_ubc['password_box']).send_keys(ubc_password)
driver.find_element_by_xpath(xpaths_ubc['login']).click()

# Request UPASS Page
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpaths_upass['chkBox'])))

checkbox = driver.find_element_by_xpath(xpaths_upass['chkBox'])
actions = ActionChains(driver)
actions.move_to_element(checkbox).perform()

checkbox.click()
driver.find_element_by_xpath(xpaths_upass['requestBtn']).click()
sys.exit()
