''' Страница "Вопросы и ответы" '''

from selenium.webdriver.common.by import By
from config import BASE_URL
import allure


class QuestionsAndAnswersPage:
    questions = {1: [By.ID, "accordion__heading-0"],
                 2: [By.ID, "accordion__heading-1"],
                 3: [By.ID, "accordion__heading-2"],
                 4: [By.ID, "accordion__heading-3"],
                 5: [By.ID, "accordion__heading-4"],
                 6: [By.ID, "accordion__heading-5"],
                 7: [By.ID, "accordion__heading-6"],
                 8: [By.ID, "accordion__heading-7"]}

    answers = {1: [By.ID, "accordion__panel-0"],
               2: [By.ID, "accordion__panel-1"],
               3: [By.ID, "accordion__panel-2"],
               4: [By.ID, "accordion__panel-3"],
               5: [By.ID, "accordion__panel-4"],
               6: [By.ID, "accordion__panel-5"],
               7: [By.ID, "accordion__panel-6"],
               8: [By.ID, "accordion__panel-7"]}

    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'Открываем страницу {BASE_URL}')
    def get_base_page(self):
        return self.driver.get(BASE_URL)

    @allure.step('Скроллим страницу к вопросу')
    def scroll_to_question(self, question):
        self.question = self.questions[question]
        element = self.driver.find_element(*self.question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текст вопроса и возвращаем его для сравнения')
    def get_question(self, question):
        self.question = self.questions[question]
        return self.driver.find_element(*self.question).text

    @allure.step('Кликаем по тексту вопроса для раскрытия')
    def get_any_answer(self, question):
        self.question = self.questions[question]
        self.driver.find_element(*self.question).click()

    @allure.step('Получаем текст ответа и возвращаем его для сравнения')
    def get_any_answer_text(self, answer):
        self.answer = self.answers[answer]
        return self.driver.find_element(*self.answer).text
