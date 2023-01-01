''' Страница "Для кого самокат" '''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_about_page import OrderAboutPage
from config import BASE_URL
import allure


class OrderForWhoPage:

    order_buttons = [By.XPATH, ".//button[contains(text(), 'казат')]"]
    order_button_in_header = [By.XPATH, "(.//button[contains(text(), 'казат')])[1]"]
    order_button_in_footer = [By.XPATH, "(.//button[contains(text(), 'казат')])[2]"]
    name = [By.CSS_SELECTOR, "[placeholder*='мя']"]
    sub_name = [By.CSS_SELECTOR, '[placeholder*="лия"]']
    order_state = [By.CSS_SELECTOR, '[placeholder*="дрес"]']
    metro = [By.CSS_SELECTOR, '[class="select-search__input"]']
    metro_selected = [By.CSS_SELECTOR, '[class="select-search__select"]']
    phone = [By.CSS_SELECTOR, '[placeholder*="кур"]']
    next_but = [By.XPATH, ".//button[contains(text(), 'але')]"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'Открываем страницу {BASE_URL}')
    def get_base_page(self):
        return self.driver.get(BASE_URL)

    @allure.step('Получаем количество кнопок "Заказать" на странице и возвращаем его для сравнения')
    def get_all_order_buttons_count(self):
        return len(self.driver.find_elements(*self.order_buttons))

    @allure.step('Кликаем на кнопку "Заказать" в header')
    def go_to_order_in_header(self):
        self.driver.find_element(*self.order_button_in_header).click()

    @allure.step('Кликаем на кнопку "Заказать" в footer')
    def go_to_order_in_footer(self):
        element = self.driver.find_element(*self.order_button_in_footer)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable(self.order_button_in_footer))
        self.driver.find_element(*self.order_button_in_footer).click()

    @allure.step('Кликаем на кнопку "Далее" и возвращаем экземляр следующего PageObject-a - Про аренду')
    def go_to_order_about_page(self):
        self.driver.find_element(*self.next_but).click()
        return OrderAboutPage(self.driver)

    @allure.step(f'Заполняем поле - имя')
    def set_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    @allure.step(f'Заполняем поле - фамилия')
    def set_sub_name(self, sub_name):
        self.driver.find_element(*self.sub_name).send_keys(sub_name)

    @allure.step(f'Заполняем поле - адрес')
    def set_order_state(self, order_state):
        self.driver.find_element(*self.order_state).send_keys(order_state)

    @allure.step(f'Заполняем поле - метро и выбираем его из саджеста')
    def set_metro(self, metro):
        self.driver.find_element(*self.metro).send_keys(metro)
        self.driver.find_element(*self.metro_selected).click()

    @allure.step(f'Заполняем поле - телефон')
    def set_phone(self, phone):
        self.driver.find_element(*self.phone).send_keys(phone)

    @allure.step('Заполняем все поля в форме')
    def fill_order_form_first(self, name, sub_name, order_state, metro, phone):
        self.set_name(name)
        self.set_sub_name(sub_name)
        self.set_order_state(order_state)
        self.set_metro(metro)
        self.set_phone(phone)
