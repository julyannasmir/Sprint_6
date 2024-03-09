from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_BUTTON = [By.CLASS_NAME, "Button_Button__ra12g"]
    NAME = [By.CSS_SELECTOR, "[placeholder='\* Имя']"]
    LASTNAME = [By.CSS_SELECTOR, "[placeholder='\* Фамилия']"]
    ADDRESS = [By.CSS_SELECTOR, "[placeholder='\* Адрес: куда привезти заказ']"]
    UNDERGROUND = [By.XPATH, "//div[@class='select-search__value']"]
    PHONE = [By.CSS_SELECTOR, "[placeholder='\* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = (By.XPATH, "//a[contains(text(),'Далее')]")
    DATE_FIELD = [By.CSS_SELECTOR, "[placeholder='\* Когда привезти самокат']"]
    RENTAL_PERIOD = [By.CSS_SELECTOR, "[placeholder='\* Срок аренды']"]
    COLOR = [By.CSS_SELECTOR, "[placeholder='\* Цвет самоката']"]
    COMMENT = [By.CSS_SELECTOR, "[placeholder='\* Комментарий для курьера']"]
    CHECKBOX = [By.ID, "//input[@id='black']"]
    YES_BUTTON = [By.XPATH, "//button[contains(text(),'Да')]"]
    ORDER_TEXT = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]
    SCOOTER_BUTTON =[By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]
    YANDEX_BUTTON = [By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"]
    HOME_PAGE_LOCATOR = [By.XPATH, "//div[@class='Home_Header__iJKdX']"]
    DZEN_LOCATOR = [By.XPATH, "//a[@class=desktop-base-header__logoLink-aE']"]

