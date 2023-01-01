''' Страница "Статус заказа" '''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderStatusPage:
    scooter_logo = [By.CSS_SELECTOR, '[alt = "Scooter"]']
    yandex_logo = [By.CSS_SELECTOR, '[href*="yand"]']
    scooter_model = [By.XPATH, './/div[contains(text(), "одел")]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переходим на главную страницу Самоката кликом на логотип сервиса')
    def go_to_base_page(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step('Переходим на главную страницу Яндекса кликом на логотип сервиса и переключаемся на неё')
    def go_to_yandex_page(self, tab):
        self.driver.find_element(*self.yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[tab])

    @allure.step('Проверяем отображение модели самоката на главной странице')
    def check_scooter_model_on_page(self):
        self.driver.find_element(*self.scooter_logo).is_displayed()

    @allure.step('Получаем url текущей страницы и возвращаем его для сравнения')
    def url_on_page(self):
        WebDriverWait(self.driver, timeout=5).until(EC.any_of(*[EC.url_contains('yandex'),
                                                                EC.url_contains('praktikum')]))
        return self.driver.current_url
