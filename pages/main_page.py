from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_on_question_and_get_answer_text(self, locator_q, locator_a, num):
        self.confirm_cookies()
        method, locator = locator_q
        locator = locator.format(num)
        self.click_on_element((method, locator))
        self.scroll_to_the_element(locator_a)
        return self.get_text_from_element(locator_a)

    def check_answer(self, result, expected):
        return result == expected
