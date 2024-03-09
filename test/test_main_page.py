import pytest

from data import Answers
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        "q_num, expected_result",
        [
            (0, Answers.ANSWER_Q_0),
            (1, Answers.ANSWER_Q_1),
            (2, Answers.ANSWER_Q_2),
            (3, Answers.ANSWER_Q_3),
            (4, Answers.ANSWER_Q_4),
            (5, Answers.ANSWER_Q_5),
            (6, Answers.ANSWER_Q_6),
            (7, Answers.ANSWER_Q_7)
        ]
    )
    def test_questions(self, driver, q_num, expected_result):
        main_page = MainPage(driver)
        result = main_page.click_on_question_and_get_answer_text(
            MainPageLocators.QUESTION_LOCATOR,
            MainPageLocators.ANSWER_LOCATOR,
            q_num
        )
        assert main_page.check_answer(result, expected_result)
