from selenium.webdriver.common.by import By

class Locators:
    #Для регистрации
    ENTRANCE_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    REG_BUTTON = (By.XPATH, "//a[@href='/register']")
    REG_NAME = (By.XPATH, "//input[@name='name']")
    REG_EMAIL = (By.XPATH, "(//input[@name='name'])[2]")
    REG_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    REG_BUTTON_DATA = (By.XPATH, "//button[contains(.,'Зарегистрироваться')]")

    #Для входа по кнопке «Войти в аккаунт» на главной
    LOGIN_EMAIL = (By.XPATH, "//input[@name='name']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")

    #Для входа по кнопке "Личный кабинет" на главной 
    LOGIN_PERSONAL_ACC= (By.XPATH, "//p[contains(., 'Личный Кабинет')]")

    #Для входа через регистрацию 
    LOGIN = (By.XPATH, "//a[@href='/login']")

    #Для входа через восстановить пароль 
    FORGOT_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")

    #Кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(.,'Конструктор')]")

    #Кнопка "Лого"
    BUTTON_LOGO = (By.XPATH, "//a[@href='/']")

    #Кнопка Выйти ил ЛК
    EXITE_BUTTON = (By.XPATH, "//button[contains(.,'Выход')]")

    #Текст бургера 
    BURGER_TEXT = (By.XPATH, "//h1[contains(.,'Соберите бургер')]")
    
    #Текст некорректный пароль 
    WRONG_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
  
    #Сделать заказ
    MAKE_ORDER = (By.XPATH, "//button[contains(.,'Оформить заказ')]")

    #Cоусы 
    BUTTON_SAUCE = (By.XPATH, "//span[contains(.,'Соусы')]")
    FIRST_SPICY_SAUCE = (By.XPATH, "(//img[contains(@alt,'Соус')])[1]")

    #Начинки 
    BUTTON_TOPPING = (By.XPATH, "//span[contains(.,'Начинки')]")
    FIRST_TOPPING = (By.XPATH, "(//img[contains(@alt,'Мясо')])[1]")


    #Булки 
    BUTTON_BREAD = BUTTON_BREAD = (By.XPATH, "//span[contains(., 'Булки')]")
    FIRST_BREAD = (By.XPATH, "(//img[contains(@alt,'булка')])[1]")
    
    