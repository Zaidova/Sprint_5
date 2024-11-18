from selenium.webdriver.common.by import By

class PageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") # Кнопка "Войти в аккаунт" на главной
    ACCOUNT_BUTTON = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка "Личный кабинет" на главной
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка "Войти" в форме авторизации
    REG_BUTTON = (By.XPATH, ".//a[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться" в форме авторизации
    INPUT_NAME = (By.XPATH, "(.//input[@name = 'name'])[1]") # Поле ввода имени в форме регистрации
    INPUT_EMAIL = (By.XPATH, "(.//input[@name = 'name'])[2]") # Поле ввода e-mail в форме регистрации
    INPUT_PASS = (By.XPATH, ".//input[@name = 'Пароль']") # Поле ввода пароля в форме регистрации
    REG_BUTTON_FORM = (By.XPATH, ".//button[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться" в форме регистрации
    ACCOUNT_NAME = (By.XPATH, ".//input[@name = 'Name']")
    INPUT_EMAIL_ENT = (By.XPATH, ".//input[@name = 'name']")
    INVALID_PASSWORD_MESSAGE = (By.XPATH, ".//p[text() = 'Некорректный пароль']")
    SET_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    LOGIN_REG_FORM_BUTTON = (By.XPATH, ".//a[text() = 'Войти']")
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")
    COLLECT_BURGER = (By.XPATH, ".//h1[text() = 'Соберите бургер']")
    EXIT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
    LOGO = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")
    BREAD_SECTION = (By.XPATH, ".//span[text() = 'Булки']")
    SAUCE_SECTION = (By.XPATH, ".//span[text() = 'Соусы']")
    FILLINGS_SECTION = (By.XPATH, ".//span[text() = 'Начинки']")
    FLUO_BREAD = (By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']")
    SPICY_X_SAUCE = (By.XPATH, ".//p[text() = 'Соус Spicy-X']")
    MEAT = (By.XPATH, ".//p[text() = 'Мясо бессмертных моллюсков Protostomia']")