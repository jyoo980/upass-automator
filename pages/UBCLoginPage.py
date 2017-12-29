from selenium.webdriver.common.by import By
from webium import BasePage, Find


class UBCLoginPage(BasePage):

    username_box = Find(by=By.ID, value='j_username')
    password_box = Find(by=By.ID, value='password')
    login_button = Find(by=By.XPATH, value="//*[@value='Continue']")

    def fill_username(self, name):
        self.username_box.fill_text_box(name)

    def fill_password(self, pword):
        self.password_box.fill_text_box(pword)

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.login_button.click()