from data import Order
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrder:

    def test_order_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.ORDER_BUTTON)
        order_page.fill_in_the_field(OrderPageLocators.NAME, Order.name)
        order_page.fill_in_the_field(OrderPageLocators.LASTNAME, Order.last_name)
        order_page.fill_in_the_field(OrderPageLocators.ADDRESS, Order.address)
        order_page.choose_dropdown(OrderPageLocators.UNDERGROUND, 'Бульвар Рокоссовского')
        order_page.fill_in_the_field(OrderPageLocators.PHONE, Order.phone)
        order_page.click_on_element(OrderPageLocators.NEXT_BUTTON)
        order_page.fill_in_the_field(OrderPageLocators.DATE_FIELD, Order.date)
        order_page.choose_dropdown(OrderPageLocators.UNDERGROUND, 'сутки')
        order_page.fill_in_the_field(OrderPageLocators.DATE_FIELD, Order.date)
        order_page.click_on_element(OrderPageLocators.CHECKBOX)
        order_page.fill_in_the_field(OrderPageLocators.COMMENT, Order.comment)
        order_page.click_on_element(OrderPageLocators.YES_BUTTON)

    def test_click_on_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.SCOOTER_BUTTON)
        order_page.check_home_page()

    def test_click_on_yandex(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.YANDEX_BUTTON)
        order_page.check_yandex_page()






