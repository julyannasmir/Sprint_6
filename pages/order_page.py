from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Order
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def fill_in_the_field(self, field_name, text):
        self.click_on_element(field_name)
        self.set_text_to_element(field_name, text)

    def check_successful_ordering(self, locator):
        order_text = self.get_text_from_element(locator).text
        assert order_text == "Заказ оформлен"

    def check_home_page(self, driver):
        current_page = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.HOME_PAGE_LOCATOR)).text
        assert current_page == 'Самокат'

    def check_yandex_page(self, driver):
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 5).until(EC.url_contains(Order.yandex_page_url))
        assert self.driver.curren_url == Order.yandex_page_url
