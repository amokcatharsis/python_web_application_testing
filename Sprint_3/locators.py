''' Локаторы для страниц приложения Stellar Burgers '''


class MainPage:
    '''Основная страница'''
    LOGIN_BUTTON = '//*[@id="root"]/div/main/section[2]/div/button'  # Войти в аккаунт
    PERSONAL_CABINET = '#root > div > header > nav > a > p'  # Личный кабинет
    COSTRUCTOR_TAB = './/p[contains(text(), "Констру")]'  # Конструктор
    WELCOME_TITLE = './/h1[contains(text(), "Собери")]'  # Текст "Соберите бургер"
    LOGO = 'div > a > svg'  # Логотип


class ConstructorPage:
    '''Конструктор'''
    BUNS_SECTION_TAB = './/span[contains(text(), "Булки")]'  # Таб "Булки"
    BUNS_SECTION = './/h2[contains(text(), "улки")]'  # Секция "Булки"
    BUNS_ELEMENTS = './/p[contains(text(), "булка")]'  # Элементы в секции "Булки"
    SAUCES_SECTION_TAB = './/span[contains(text(), "Соусы")]'  # Таб "Соусы"
    SAUCES_SECTION = './/h2[contains(text(), "оус")]'  # Секция "Соусы"
    SAUCES_ELEMENTS = './/p[contains(text(), "оус")]'  # Элементы в секции "Соусы"
    FILLING_SECTION_TAB = './/span[contains(text(), "Начинки")]'  # Таб "Начинки"
    FILLING_SECTION = './/h2[contains(text(), "ачинк")]'  # Секция "Начинки"
    FILLING_ELEMENTS_ONE_OF_FIRST = '[alt~=метеорит]'  # Один из первых элементов секции "Начинки"
    FILLING_ELEMENTS_ONE_OF_LAST = '[alt~=Сыр]'  # Один из последних элементов секции "Начинки"


class AuthPage:
    '''Авторизация'''
    EMAIL_FIELD = 'form > fieldset:nth-child(1) > div > div > input'  # Поле "Email"
    PASS_FIELD = 'form > fieldset:nth-child(2) > div > div > input'  # Поле "Пароль"
    LOGIN_BUTTON = '#root > div > main > div > form > button'  # Кнопка "Войти"
    REG_NEW_USER_BUTTON = 'a[href*="register"]'  # Кнопка "Зарегистрироваться"
    ENTER_LABLE = '#root > div > main > div > h2'  # Название формы "Вход"
    PERSONAL_CABINET = '#root > div > header > nav > a > p'  # Кнопка "Личный кабинет" для страницы "Авторизация"
    PASS_RECOVERY_BUTTON = './/a[contains(text(), "пароль")]'  # Кнопка "Восстановить пароль"
    LOGIN_BUTTON_ON_PASS_RECOVERY_PAGE = './/a[contains(text(), "Войти")]'  # Кнопка "Войти" страницы "Восстановление"


class RegistrationPage:
    '''Регистрация'''
    NAME_FIELD = 'form > fieldset:nth-child(1) > div > div > input'  # Поле "Имя"
    EMAIL_FIELD = 'form > fieldset:nth-child(2) > div > div > input'  # Поле "Email"
    PASS_FIELD = '[type="password"]'  # Поле "Пароль"
    REG_SUBMIT_BUTTON = './/button[contains(text(), "ться")]'  # Кнопка "Зарегистрироваться"
    REG_ERROR_POPUP = '[class="input__error text_type_main-default"]'  # Поп-ап ошибки


class PersonalCabinet:
    '''Личный кабинет'''
    NAME_FIELD = 'input[value*=еловая]'  # Поле "Имя"
    LOGIN_FIELD = 'input[value*=sad_tester]'  # Поле "Логин"
    PROFILE_BUTTON = 'a[href*="profile"]'  # Кнопка "Профиль"
    ORDER_HISTORY_BUTTON = 'a[href*="order-history"]'  # Кнопка "История заказов"
    LOGOUT_BUTTON = './/button[contains(text(), "Выход")]'  # Кнопка "Выход"
