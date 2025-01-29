from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    ASK_FOR_TAXI = (By.CLASS_NAME, "smart-button-main")

class UrbanRoutesComfortFormLocators:
    FLASH_OPTION_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[2]')
    TAXI_OPTION_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[2]/div[3]')
    LOOK_FOR_TAXI_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    COMFORT_TAXI_OPTION = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    MESSAGE_FOR_DRIVER_BOX = (By.XPATH, '//*[@id="comment"]')
    option_switches = (By.CLASS_NAME, 'switch')
    option_switches_inputs = (By.CLASS_NAME, 'switch-input')
    ICE_CREAM_SLIDER = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    ICE_CREAM_COUNTER = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')

class UrbanRoutesAddPhoneLocators:
    SET_PHONE = (By.CLASS_NAME, 'np-text')
    ADD_PHONE_NUMBER = (By.ID, 'phone')
    BUTTON_NEXT = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    SET_CONFIRMATION_CODE = (By.ID, 'code')
    CONFIRMATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')

class UrbanRoutesPaymentMethodLocators:
    SELECT_PAYMENT_METHOD_BUTTON = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]")
    SELECTED_PAY_METHOD = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]")
    ADD_CARD_INFO_BUTTON = (By.CLASS_NAME, 'pp-plus-container')
    SET_CARD_NUMBER = (By.ID, 'number')
    SET_CARD_CODE = (By.XPATH, "//input[@id='code'][@class='card-input']")
    CARD_SECOND_ROW = (By.CLASS_NAME, 'card-second-row')
    ADD_CARD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    CLOSE_PAYMENT_METHODS_WINDOW_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    ASK_FOR_TAXI_BUTTON_ENABLE = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button/span[1]')