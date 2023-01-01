''' Страница "Про аренду" '''

from selenium.webdriver.common.by import By
from pages.order_approve_page import OrderApprovePage
import allure


class OrderAboutPage:
    when = [By.CSS_SELECTOR, '[placeholder*="сам"]']
    how_long = [By.CSS_SELECTOR, '[class="Dropdown-placeholder"]']
    one_day = [By.XPATH, "(.//div[contains(text(), 'сут')])[1]"]
    black_color = [By.CSS_SELECTOR, '[for="black"]']
    comment = [By.CSS_SELECTOR, '[placeholder*="ммен"]']
    order_button_in_footer = [By.XPATH, "(.//button[contains(text(), 'казат')])[2]"]
    one_day_calendar = [By.XPATH, '(.//*[@class="react-datepicker__week"])[2]//*[@tabindex="0"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'Заполняем поле - когда и выбираем его из календаря')
    def set_when(self, when):
        self.driver.find_element(*self.when).send_keys(when)
        self.driver.find_element(*self.one_day_calendar).click()

    @allure.step(f'Заполняем поле - срок и выбираем его из саджеста')
    def set_how_long(self):
        self.driver.find_element(*self.how_long).click()
        self.driver.find_element(*self.one_day).click()

    @allure.step('Выбираем цвет - "чёрный жемчуг"')
    def set_black_color(self):
        self.driver.find_element(*self.black_color).click()

    @allure.step(f'Заполняем поле комментарий')
    def set_comment(self, comment):
        self.driver.find_element(*self.comment).send_keys(comment)

    @allure.step('Кликаем на кнопку "Заказать" и возвращаем экземляр следующего PageObject-a - Подтверждение заказа')
    def end_with_filling_info(self):
        self.driver.find_element(*self.order_button_in_footer).click()
        return OrderApprovePage(self.driver)

    @allure.step('Заполняем все поля в форме')
    def fill_order_form_second(self, when, comment):
        self.set_when(when)
        self.set_how_long()
        self.set_black_color()
        self.set_comment(comment)
