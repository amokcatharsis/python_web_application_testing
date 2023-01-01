''' Тесты для вопросов и ответов '''

from selenium import webdriver
from pages.questions_and_answers_page import QuestionsAndAnswersPage
import allure
from data_for_tests import questions_texts, question_answers_texts


class TestQuestionsAndAnswers:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Вопрос № 1')
    @allure.description('Получаем текст вопроса, текст ответа и сравниваем их с эталонными')
    def test_first_question(self):

        question = QuestionsAndAnswersPage(self.driver)

        question.get_base_page()
        question.scroll_to_question(1)

        question_text = question.get_question(1)
        assert question_text == questions_texts[1], 'Текст вопроса не совпадает!'

        question.get_any_answer(1)

        question_answer = question.get_any_answer_text(1)
        assert question_answer == question_answers_texts[1], 'Текст ответа не совпадает!'

    @allure.title('Вопрос № 2')
    @allure.description('Получаем текст вопроса, текст ответа и сравниваем их с эталонными')
    def test_second_question(self):

        question = QuestionsAndAnswersPage(self.driver)

        question.get_base_page()
        question.scroll_to_question(2)

        question_text = question.get_question(2)
        assert question_text == questions_texts[2], 'Текст вопроса не совпадает!'

        question.get_any_answer(2)

        question_answer = question.get_any_answer_text(2)
        assert question_answer == question_answers_texts[2], 'Текст ответа не совпадает!'

    @allure.title('Вопрос № 3')
    @allure.description('Получаем текст вопроса, текст ответа и сравниваем их с эталонными')
    def test_third_question(self):

        question = QuestionsAndAnswersPage(self.driver)

        question.get_base_page()
        question.scroll_to_question(3)

        question_text = question.get_question(3)
        assert question_text == questions_texts[3], 'Текст вопроса не совпадает!'

        question.get_any_answer(3)

        question_answer = question.get_any_answer_text(3)
        assert question_answer == question_answers_texts[3], 'Текст ответа не совпадает!'

    @allure.title('Вопрос № 4')
    @allure.description('Получаем текст вопроса, текст ответа и сравниваем их с эталонными')
    def test_fourth_question(self):

        question = QuestionsAndAnswersPage(self.driver)

        question.get_base_page()
        question.scroll_to_question(4)

        question_text = question.get_question(4)
        assert question_text == questions_texts[4], 'Текст вопроса не совпадает!'

        question.get_any_answer(4)

        question_answer = question.get_any_answer_text(4)
        assert question_answer == question_answers_texts[4], 'Текст ответа не совпадает!'

    @allure.title('Вопрос № 5')
    @allure.description('Получаем текст вопроса, текст ответа и сравниваем их с эталонными')
    def test_fifth_question(self):

        question = QuestionsAndAnswersPage(self.driver)

        question.get_base_page()
        question.scroll_to_question(5)

        question_text = question.get_question(5)
        assert question_text == questions_texts[5], 'Текст вопроса не совпадает!'

        question.get_any_answer(5)

        question_answer = question.get_any_answer_text(5)
        assert question_answer == question_answers_texts[5], 'Текст ответа не совпадает!'

    @allure.title('Вопрос № 6')
    @allure.description('Получаем текст вопроса, текст ответа и сравниваем их с эталонными')
    def test_sixth_question(self):

        question = QuestionsAndAnswersPage(self.driver)

        question.get_base_page()
        question.scroll_to_question(6)

        question_text = question.get_question(6)
        assert question_text == questions_texts[6], 'Текст вопроса не совпадает!'

        question.get_any_answer(6)

        question_answer = question.get_any_answer_text(6)
        assert question_answer == question_answers_texts[6], 'Текст ответа не совпадает!'

    @allure.title('Вопрос № 7')
    @allure.description('Получаем текст вопроса, текст ответа и сравниваем их с эталонными')
    def test_seventh_question(self):

        question = QuestionsAndAnswersPage(self.driver)

        question.get_base_page()
        question.scroll_to_question(7)

        question_text = question.get_question(7)
        assert question_text == questions_texts[7], 'Текст вопроса не совпадает!'

        question.get_any_answer(7)

        question_answer = question.get_any_answer_text(7)
        assert question_answer == question_answers_texts[7], 'Текст ответа не совпадает!'

    @allure.title('Вопрос № 8')
    @allure.description('Получаем текст вопроса, текст ответа и сравниваем их с эталонными')
    def test_eighth_question(self):

        question = QuestionsAndAnswersPage(self.driver)

        question.get_base_page()
        question.scroll_to_question(8)

        question_text = question.get_question(8)
        assert question_text == questions_texts[8], 'Текст вопроса не совпадает!'

        question.get_any_answer(8)

        question_answer = question.get_any_answer_text(8)
        assert question_answer == question_answers_texts[8], 'Текст ответа не совпадает!'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
