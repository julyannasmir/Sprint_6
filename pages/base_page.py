from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def confirm_cookies(self):
        self.click_on_element(MainPageLocators.CONFIRM_COOKIES_BUTTON)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text()

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def scroll_to_the_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def choose_dropdown(self, dropdown, text):
        select = Select(self.driver.find_element(dropdown))
        select.select_by_visible_text(text)
