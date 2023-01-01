''' Страницы "Хотите оформить заказ?" и "Заказ оформлен" '''

from selenium.webdriver.common.by import By
from pages.order_status_page import OrderStatusPage
import allure


class OrderApprovePage:
    order_cancellation_button = [By.XPATH, ".//button[contains(text(), 'Нет')]"]
    order_confirmation_button = [By.XPATH, ".//button[contains(text(), 'Да')]"]
    status_button = [By.XPATH, ".//button[contains(text(), 'смотр')]"]
    order_successfully_created_title = [By.XPATH, ".// div[contains(text(), 'оформлен')]"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.driver.find_element(*self.order_confirmation_button).click()

    @allure.step('Кликаем на кнопку "Статус заказа" и возвращаем экземляр следующего PageObject-a - Статус Заказа')
    def go_to_order_status_page(self):
        self.driver.find_element(*self.status_button).click()
        return OrderStatusPage(self.driver)

    @allure.step('Проверяем наличие кнопок "Нет" и "Да"')
    def check_order_buttons_on_page(self):
        self.driver.find_element(*self.order_cancellation_button).is_displayed()
        self.driver.find_element(*self.order_confirmation_button).is_displayed()

    @allure.step('Проверяем наличие кнопки "Статус заказа"')
    def check_status_button_on_page(self):
        self.driver.find_element(*self.status_button).is_displayed()

    @allure.step('Забираем текст заголовка окна и возвращаем его для сравнения')
    def check_frame_title(self):
        return self.driver.find_element(*self.order_successfully_created_title).text
