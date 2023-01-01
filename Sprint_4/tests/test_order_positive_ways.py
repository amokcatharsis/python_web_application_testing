''' Тесты для позитивных сценариев '''

from selenium import webdriver
import allure
from pages.order_for_who_page import OrderForWhoPage
from config import BASE_URL, YANDEX_URL
from data_for_tests import test_suite_one, test_suite_two

# в сформированном заказе станция метро выбирается на одну позицию ниже,
# чем указана в тесте - но проверка этого не указана в условиях позитивного сценария

class TestOrderPositiveWays:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Позитивный сценарий через кнопку в header с первым набором тестовых данных')
    @allure.description('Проверяем весь флоу позитивного сценария')
    def test_positive_way_entry_in_header_with_suite_one(self):

        order_for_who_page = OrderForWhoPage(self.driver)
        order_for_who_page.get_base_page()

        count_of_order_buttons = order_for_who_page.get_all_order_buttons_count()
        assert count_of_order_buttons == 2, 'Количество кнопок "Заказать" != 2!'

        order_for_who_page.go_to_order_in_header()

        order_for_who_page.fill_order_form_first(test_suite_one['name_text'],
                                                 test_suite_one['sub_name_text'],
                                                 test_suite_one['order_state_text'],
                                                 test_suite_one['metro_text'],
                                                 test_suite_one['phone_text'])

        order_about_page = order_for_who_page.go_to_order_about_page()
        order_about_page.fill_order_form_second(test_suite_one['when'],
                                                test_suite_one['comment'])

        order_approve_page = order_about_page.end_with_filling_info()
        order_approve_page.check_order_buttons_on_page()

        order_approve_page.confirm_order()

        order_approve_page.check_status_button_on_page()

        order_successfully_created_title = order_approve_page.check_frame_title()
        assert 'Заказ оформлен' in order_successfully_created_title, 'Заказ не был оформлен!'

        order_status_page = order_approve_page.go_to_order_status_page()
        order_status_page.go_to_base_page()
        order_status_page.check_scooter_model_on_page()

        url_on_base_page = order_status_page.url_on_page()
        assert url_on_base_page == BASE_URL, 'Клик на логотип Самоката не ведёт на главную страницу сервиса!'

        order_status_page.go_to_yandex_page(1)

        url_on_yandex_page = order_status_page.url_on_page()
        assert url_on_yandex_page == YANDEX_URL, 'Клик на логотип Яндекса не ведёт на главную страницу сервиса!'

    @allure.title('Позитивный сценарий через кнопку в header со вторым набором тестовых данных')
    @allure.description('Проверяем весь флоу позитивного сценария')
    def test_positive_way_entry_in_header_with_suite_two(self):

        order_for_who_page = OrderForWhoPage(self.driver)
        order_for_who_page.get_base_page()

        count_of_order_buttons = order_for_who_page.get_all_order_buttons_count()
        assert count_of_order_buttons == 2, 'Количество кнопок "Заказать" != 2!'

        order_for_who_page.go_to_order_in_header()

        order_for_who_page.fill_order_form_first(test_suite_two['name_text'],
                                                 test_suite_two['sub_name_text'],
                                                 test_suite_two['order_state_text'],
                                                 test_suite_two['metro_text'],
                                                 test_suite_two['phone_text'])

        order_about_page = order_for_who_page.go_to_order_about_page()
        order_about_page.fill_order_form_second(test_suite_two['when'],
                                                test_suite_two['comment'])

        order_approve_page = order_about_page.end_with_filling_info()
        order_approve_page.check_order_buttons_on_page()

        order_approve_page.confirm_order()

        order_approve_page.check_status_button_on_page()

        order_successfully_created_title = order_approve_page.check_frame_title()
        assert 'Заказ оформлен' in order_successfully_created_title, 'Заказ не был оформлен!'

        order_status_page = order_approve_page.go_to_order_status_page()
        order_status_page.go_to_base_page()
        order_status_page.check_scooter_model_on_page()

        url_on_base_page = order_status_page.url_on_page()
        assert url_on_base_page == BASE_URL, 'Клик на логотип Самоката не ведёт на главную страницу сервиса!'

        order_status_page.go_to_yandex_page(2)

        url_on_yandex_page = order_status_page.url_on_page()
        assert url_on_yandex_page == YANDEX_URL, 'Клик на логотип Яндекса не ведёт на главную страницу сервиса!'

    @allure.title('Позитивный сценарий через кнопку в footer с первым набором тестовых данных')
    @allure.description('Проверяем весь флоу позитивного сценария')
    def test_positive_way_entry_in_footer_with_suite_one(self):
        order_for_who_page = OrderForWhoPage(self.driver)
        order_for_who_page.get_base_page()

        count_of_order_buttons = order_for_who_page.get_all_order_buttons_count()
        assert count_of_order_buttons == 2, 'Количество кнопок "Заказать" != 2!'

        order_for_who_page.go_to_order_in_footer()

        order_for_who_page.fill_order_form_first(test_suite_one['name_text'],
                                                 test_suite_one['sub_name_text'],
                                                 test_suite_one['order_state_text'],
                                                 test_suite_one['metro_text'],
                                                 test_suite_one['phone_text'])

        order_about_page = order_for_who_page.go_to_order_about_page()
        order_about_page.fill_order_form_second(test_suite_one['when'],
                                                test_suite_one['comment'])

        order_approve_page = order_about_page.end_with_filling_info()

        order_approve_page.check_order_buttons_on_page()

        order_approve_page.confirm_order()

        order_approve_page.check_status_button_on_page()

        order_successfully_created_title = order_approve_page.check_frame_title()
        assert 'Заказ оформлен' in order_successfully_created_title, 'Заказ не был оформлен!'

        order_status_page = order_approve_page.go_to_order_status_page()

        order_status_page.go_to_base_page()
        order_status_page.check_scooter_model_on_page()

        url_on_base_page = order_status_page.url_on_page()
        assert url_on_base_page == BASE_URL, 'Клик на логотип Самоката не ведёт на главную страницу сервиса!'

        order_status_page.go_to_yandex_page(3)

        url_on_yandex_page = order_status_page.url_on_page()
        assert url_on_yandex_page == YANDEX_URL, 'Клик на логотип Яндекса не ведёт на главную страницу сервиса!'

    @allure.title('Позитивный сценарий через кнопку в footer со вторым набором тестовых данных')
    @allure.description('Проверяем весь флоу позитивного сценария')
    def test_positive_way_entry_in_footer_with_suite_two(self):
        order_for_who_page = OrderForWhoPage(self.driver)
        order_for_who_page.get_base_page()

        count_of_order_buttons = order_for_who_page.get_all_order_buttons_count()
        assert count_of_order_buttons == 2, 'Количество кнопок "Заказать" != 2!'

        order_for_who_page.go_to_order_in_footer()

        order_for_who_page.fill_order_form_first(test_suite_two['name_text'],
                                                 test_suite_two['sub_name_text'],
                                                 test_suite_two['order_state_text'],
                                                 test_suite_two['metro_text'],
                                                 test_suite_two['phone_text'])

        order_about_page = order_for_who_page.go_to_order_about_page()
        order_about_page.fill_order_form_second(test_suite_two['when'],
                                                test_suite_two['comment'])

        order_approve_page = order_about_page.end_with_filling_info()

        order_approve_page.check_order_buttons_on_page()

        order_approve_page.confirm_order()

        order_approve_page.check_status_button_on_page()

        order_successfully_created_title = order_approve_page.check_frame_title()
        assert 'Заказ оформлен' in order_successfully_created_title, 'Заказ не был оформлен!'

        order_status_page = order_approve_page.go_to_order_status_page()

        order_status_page.go_to_base_page()
        order_status_page.check_scooter_model_on_page()

        url_on_base_page = order_status_page.url_on_page()
        assert url_on_base_page == BASE_URL, 'Клик на логотип Самоката не ведёт на главную страницу сервиса!'

        order_status_page.go_to_yandex_page(4)

        url_on_yandex_page = order_status_page.url_on_page()
        assert url_on_yandex_page == YANDEX_URL, 'Клик на логотип Яндекса не ведёт на главную страницу сервиса!'

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
