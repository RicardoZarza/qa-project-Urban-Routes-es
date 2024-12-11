from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    FROM_FIELD = (By.XPATH, '//*[@id="from"]')
    TO_FIELD = (By.XPATH, '//*[@id="to"]')

class UrbanRoutesComfortFormLocators:
    FLASH_OPTION_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[2]')
    TAXI_OPTION_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[2]/div[3]')
    LOOK_FOR_TAXI_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    COMFORT_TAXI_OPTION = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    MESSAGE_FOR_DRIVER_BOX = (By.XPATH, '//*[@id="comment"]')
    BLANKET_AND_TISSUE_SLIDER = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ICE_CREAM_SLIDER = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

class UrbanRoutesAddPhoneLocators:
    SET_PHONE = (By.CLASS_NAME, 'np-text')
    ADD_PHONE_NUMBER = (By.ID, 'phone')
    BUTTON_NEXT = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    SET_CONFIRMATION_CODE = (By.ID, 'code')
    CONFIRMATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')

class UrbanRoutesPaymentMethodLocators:
    SELECT_PAYMENT_METHOD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    ADD_CARD_INFO_BUTTON = (By.CLASS_NAME, 'pp-checkbox')
    SET_CARD_NUMBER = (By.CLASS_NAME, 'card-number-input')
    SET_CARD_CODE = (By.CLASS_NAME, 'card-code-input')
    CARD_SECOND_ROW = (By.CLASS_NAME, 'card-second-row')
    ADD_CARD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    CLOSE_PAYMENT_METHODS_WINDOW_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
