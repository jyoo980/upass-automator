from selenium.webdriver.common.by import By
from webium import BasePage, Find
from webium.controls.click import Clickable
from webium.controls.select import Select

from pages.UBCLoginPage import UBCLoginPage


class UPassSelectPage(BasePage):

    school_select = Find(Select, by=By.XPATH, value="//*[@class='hasCustomSelect']")
    confirm_button = Find(Clickable, by=By.XPATH, value="//*[@id='goButton']")

    def select_school(self, school_name):
        self.school_select.select_by_visible_text(school_name)
        self.confirm_button.click()
        return UBCLoginPage()

    






