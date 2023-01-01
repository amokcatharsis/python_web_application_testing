''' Тесты для страниц приложения Stellar Burgers '''

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

link = 'https://stellarburgers.nomoreparties.site/'

# Словарь с тестовыми данными, перед запуском тестов нужно изменить число после beta_
entities = {'name': 'Деловая КОЛБАСКА',
            'email': 'sad_tester_beta_20112@mail.ru',
            'valid_password': 'test_your@_SOUL',
            'invalid_password': 12345
            }
# в среднем на 20 прогонов 1 раз падает тест 14 - но это не повод завешивать всё ожиданиями
# в конце концов, мы и не ожидаем стопроцентной стабильности от самых хрупких - UI тестов


class TestStellarBurgersRegistration:
    ''' Тесты регистрации '''
    def test_reg_passed_with_correct_fields(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.REG_NEW_USER_BUTTON).click()

        name_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.NAME_FIELD)
        name_field.send_keys(entities['name'])

        email_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.EMAIL_FIELD)
        email_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.XPATH, RegistrationPage.REG_SUBMIT_BUTTON).click()

        driver.implicitly_wait(1)
        reg_new_button_text = driver.find_element(By.CSS_SELECTOR, AuthPage.REG_NEW_USER_BUTTON).text
        assert reg_new_button_text == 'Зарегистрироваться'

        driver.quit()

    def test_reg_user_with_non_unique_mail_cant_be_registered(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.REG_NEW_USER_BUTTON).click()

        name_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.NAME_FIELD)
        name_field.send_keys(entities['name'])

        email_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.EMAIL_FIELD)
        email_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.XPATH, RegistrationPage.REG_SUBMIT_BUTTON).click()

        driver.implicitly_wait(1)
        text = driver.find_element(By.CSS_SELECTOR, RegistrationPage.REG_ERROR_POPUP).text
        assert text == 'Такой пользователь уже существует'

        driver.quit()

    def test_reg_user_invalid_password_popup_displayed(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.REG_NEW_USER_BUTTON).click()

        pass_field = driver.find_element(By.CSS_SELECTOR, RegistrationPage.PASS_FIELD)
        pass_field.send_keys(entities['invalid_password'])

        driver.find_element(By.CSS_SELECTOR, RegistrationPage.EMAIL_FIELD).click()

        driver.implicitly_wait(1)
        text = driver.find_element(By.CSS_SELECTOR, RegistrationPage.REG_ERROR_POPUP).text
        assert text == 'Некорректный пароль'

        driver.quit()


class TestStellarBurgersAllWaysToLogin:
    ''' Тесты логина-логаута '''
    def test_login_with_button_in_main_page_success(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        driver.implicitly_wait(1)
        actual_name = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.NAME_FIELD)
        actual_email = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.LOGIN_FIELD)

        assert actual_name
        assert actual_email

        driver.quit()

    def test_login_with_personal_cabinet_button_success(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, MainPage.PERSONAL_CABINET).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        driver.implicitly_wait(1)
        actual_name = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.NAME_FIELD)
        actual_email = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.LOGIN_FIELD)

        assert actual_name
        assert actual_email

        driver.quit()

    def test_login_with_reg_frame_success(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        driver.implicitly_wait(1)
        actual_name = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.NAME_FIELD)
        actual_email = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.LOGIN_FIELD)

        assert actual_name
        assert actual_email

        driver.quit()

    def test_login_with_password_recovery_frame_success(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, AuthPage.PASS_RECOVERY_BUTTON).click()
        driver.find_element(By.XPATH, AuthPage.LOGIN_BUTTON_ON_PASS_RECOVERY_PAGE).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        driver.implicitly_wait(1)
        actual_name = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.NAME_FIELD)
        actual_email = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.LOGIN_FIELD)

        assert actual_name
        assert actual_email

        driver.quit()

    def test_logout(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.implicitly_wait(1)
        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()
        driver.find_element(By.XPATH, PersonalCabinet.LOGOUT_BUTTON).click()

        reg_page = driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON)

        assert reg_page.is_displayed()

        driver.quit()


class TestStellarBurgersMainRouting:
    ''' Тесты переходов между окнами системы '''
    def test_routing_in_personal_cabinet_from_main_page(self):
        # переход в личный кабинет
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        driver.implicitly_wait(1)
        profile_button = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.PROFILE_BUTTON)
        order_history_button = driver.find_element(By.CSS_SELECTOR, PersonalCabinet.ORDER_HISTORY_BUTTON)
        logout_button = driver.find_element(By.XPATH, PersonalCabinet.LOGOUT_BUTTON)

        assert profile_button
        assert order_history_button
        assert logout_button

        driver.quit()

    def test_routing_in_constructor_from_personal_cabinet_click_on_string(self):
        # переход в конструктор нажатием на строку "Конструктор"
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()
        driver.find_element(By.XPATH, MainPage.COSTRUCTOR_TAB).click()

        welcome_title = driver.find_element(By.XPATH, MainPage.WELCOME_TITLE)

        assert welcome_title.is_displayed()

        driver.quit()

    def test_routing_in_constructor_from_personal_cabinet_click_on_logo(self):
        # переход в конструктор нажатием на логотип
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()

        name_field = driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD)
        name_field.send_keys(entities['email'])

        pass_field = driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD)
        pass_field.send_keys(entities['valid_password'])

        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()
        driver.find_element(By.CSS_SELECTOR, MainPage.LOGO).click()

        welcome_title = driver.find_element(By.XPATH, MainPage.WELCOME_TITLE)

        assert welcome_title.is_displayed()

        driver.quit()


class TestStellarBurgersConstructorRouting:
    ''' Тесты переходов в окне "Конструктор" '''
    def test_navigate_to_filling_section_first_item_check(self):
        # переход к разделу "Начинки" с проверкой названия секции и одного из первых элементов
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, ConstructorPage.FILLING_SECTION_TAB).click()

        filling_section = driver.find_element(By.XPATH, ConstructorPage.FILLING_SECTION)
        one_of_first = driver.find_element(By.CSS_SELECTOR, ConstructorPage.FILLING_ELEMENTS_ONE_OF_FIRST)

        assert filling_section.is_displayed()
        assert one_of_first.is_displayed()

        driver.quit()

    def test_navigate_to_filling_section_last_item_check(self):
        # переход к разделу "Начинки" с проверкой одного из последних элементов в секции
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, ConstructorPage.FILLING_SECTION_TAB).click()

        one_of_last = driver.find_element(By.CSS_SELECTOR, ConstructorPage.FILLING_ELEMENTS_ONE_OF_LAST)
        driver.execute_script("arguments[0].scrollIntoView();", one_of_last)
        assert one_of_last.is_displayed()

        driver.quit()

    def test_navigate_to_sauces_section(self):
        # переход к разделу "Соусы"
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, ConstructorPage.SAUCES_SECTION_TAB).click()

        sauces_section = driver.find_element(By.XPATH, ConstructorPage.SAUCES_SECTION)
        assert sauces_section.is_displayed()

        sauce_elements = driver.find_elements(By.XPATH, ConstructorPage.SAUCES_ELEMENTS)
        for sauce_element in sauce_elements:
            assert sauce_element.is_displayed()

        driver.quit()

    def test_navigate_to_buns_section(self):
        # переход к разделу "Булки"
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, ConstructorPage.FILLING_SECTION_TAB).click()

        driver.find_element(By.XPATH, ConstructorPage.BUNS_SECTION_TAB).click()

        buns_section = driver.find_element(By.XPATH, ConstructorPage.BUNS_SECTION)
        assert buns_section.is_displayed()

        buns_element = driver.find_elements(By.XPATH, ConstructorPage.BUNS_ELEMENTS)
        for bun_element in buns_element:
            assert bun_element.is_displayed()

        driver.quit()