from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import message_for_driver
from locators import UrbanRoutesLocators, UrbanRoutesComfortFormLocators, UrbanRoutesAddPhoneLocators, UrbanRoutesPaymentMethodLocators


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = UrbanRoutesLocators.FROM_FIELD
    to_field = UrbanRoutesLocators.TO_FIELD

    def __init__(self, driver):
        self.driver = driver

    def wait_for_from_input(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.from_field))

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.wait_for_from_input()
        self.set_from(from_address)
        self.set_to(to_address)
        self.get_from()
        self.get_to()

class UrbanRoutesComfortForm:
    flash_option_button = UrbanRoutesComfortFormLocators.FLASH_OPTION_BUTTON
    taxi_option_button = UrbanRoutesComfortFormLocators.TAXI_OPTION_BUTTON
    look_for_taxi_button = UrbanRoutesComfortFormLocators.LOOK_FOR_TAXI_BUTTON
    comfort_taxi_option = UrbanRoutesComfortFormLocators.COMFORT_TAXI_OPTION
    message_for_driver_box = UrbanRoutesComfortFormLocators.MESSAGE_FOR_DRIVER_BOX
    blanket_and_tissue_slider = UrbanRoutesComfortFormLocators.BLANKET_AND_TISSUE_SLIDER
    ice_cream_slider = UrbanRoutesComfortFormLocators.ICE_CREAM_SLIDER

    def __init__(self, driver):
        self.driver = driver

    def wait_for_look_for_taxi_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.look_for_taxi_button))

    def click_flash_option(self):
        self.driver.find_element(*self.flash_option_button).click()

    def click_taxi_option(self):
        self.driver.find_element(*self.taxi_option_button).click()

    def click_look_for_taxi_button(self):
        self.driver.find_element(*self.look_for_taxi_button).click()

    def wait_for_taxi_types_list(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.comfort_taxi_option))

    def click_comfort_option(self):
        self.driver.find_element(*self.comfort_taxi_option).click()

    def wait_for_comfort_form(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.message_for_driver_box))

    def write_a_comment_to_driver(self, comment):
        self.driver.find_element(*self.message_for_driver_box).send_keys(comment)

    def wait_for_comment(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(message_for_driver))

    def click_to_ask_for_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_and_tissue_slider).click()

    def double_click_to_ask_for_two_icecream(self):
        self.driver.find_element(*self.ice_cream_slider).click()
        self.driver.find_element(*self.ice_cream_slider).click()

    def get_comment(self):
        return self.driver.find_element(*self.message_for_driver_box).get_property('value')

    def get_ice_cream_number(self):
        return self.driver.find_element(*self.ice_cream_slider).get_property('value')

    def get_blanket_tissues_confirmation(self):
        return self.driver.find_element(*self.message_for_driver_box).get_property()

    def look_for_comfort_taxi(self, comment):
        self.wait_for_look_for_taxi_button()
        self.click_flash_option()
        self.click_taxi_option()
        self.click_look_for_taxi_button()
        self.wait_for_taxi_types_list()
        self.click_comfort_option()
        self.wait_for_comfort_form()
        self.write_a_comment_to_driver(comment)
        self.click_to_ask_for_blanket_and_tissues()
        self.double_click_to_ask_for_two_icecream()
        self.get_comment()
        self.get_ice_cream_number()


class UrbanRoutesAddPhone:
    set_phone = UrbanRoutesAddPhoneLocators.SET_PHONE
    add_phone_number = UrbanRoutesAddPhoneLocators.ADD_PHONE_NUMBER
    button_next = UrbanRoutesAddPhoneLocators.BUTTON_NEXT
    set_confirmation_code = UrbanRoutesAddPhoneLocators.SET_CONFIRMATION_CODE
    confirmation_button = UrbanRoutesAddPhoneLocators.CONFIRMATION_BUTTON

    def __init__(self, driver):
        self.driver = driver

    def wait_for_set_phone_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.set_phone))

    def click_set_phone(self):
        self.driver.find_element(*self.set_phone).click()

    def wait_for_set_phone_window(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.add_phone_number))

    def set_phone_number(self, number_phone):
        self.driver.find_element(*self.add_phone_number).send_keys(number_phone)

    def get_phone_number(self):
        return self.driver.find_element(*self.add_phone_number).get_property('value')

    def click_next_button(self):
        self.driver.find_element(*self.button_next).click()

    def wait_for_verification_window(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.set_confirmation_code))

    def set_verification_code(self):
        confirmation_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.set_confirmation_code).send_keys(confirmation_code)

    def click_confirmation_button(self):
        self.driver.find_element(*self.confirmation_button).click()

    def add_new_phone_number(self, number_phone):
        self.wait_for_set_phone_button()
        self.click_set_phone()
        self.wait_for_set_phone_window()
        self.set_phone_number(number_phone)
        self.get_phone_number()
        self.click_next_button()
        self.wait_for_verification_window()
        self.set_verification_code()
        self.click_confirmation_button()


class UrbanRoutesPaymentMethod:

    select_payment_method_button = UrbanRoutesPaymentMethodLocators.SELECT_PAYMENT_METHOD_BUTTON
    selected_pay_method = UrbanRoutesPaymentMethodLocators.SELECTED_PAY_METHOD
    add_card_info_button = UrbanRoutesPaymentMethodLocators.ADD_CARD_INFO_BUTTON
    set_card_number =  UrbanRoutesPaymentMethodLocators.SET_CARD_NUMBER
    set_card_code = UrbanRoutesPaymentMethodLocators.SET_CARD_CODE
    card_second_row = UrbanRoutesPaymentMethodLocators.CARD_SECOND_ROW #se usa para hacer click y habilitar el botón de agregar
    add_card_button = UrbanRoutesPaymentMethodLocators.ADD_CARD_BUTTON
    close_payment_methods_window_button = UrbanRoutesPaymentMethodLocators.CLOSE_PAYMENT_METHODS_WINDOW_BUTTON


    def __init__(self, driver):
        self.driver = driver

    def wait_for_payment_method_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(self.select_payment_method_button))

    def click_payment_method_button(self):
        self.driver.find_element(*self.select_payment_method_button).click()

    def wait_for_payment_options_window(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.add_card_info_button))

    def click_add_card_info(self):
        self.driver.find_element(*self.add_card_info_button).click()

    def wait_card_info_window(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.set_card_number))

    def write_card_number(self, number_card):
        self.driver.find_element(*self.set_card_number).send_keys(number_card)

    def write_card_code(self, code_card):
        self.driver.find_element(*self.set_card_code).send_keys(code_card)

    def click_second_row_to_activate_add_button(self):
        self.driver.find_element(*self.card_second_row).click()

    def get_card_number(self):
        return self.driver.find_element(*self.set_card_number).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.set_card_code).get_property('value')

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def wait_for_card_info_window_closing(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.close_payment_methods_window_button))

    def click_close_window_button(self):
        self.driver.find_element(*self.close_payment_methods_window_button).click()

    def add_a_new_payment_card(self, number_card, code_card):
        self.wait_for_payment_method_button()
        self.click_payment_method_button()
        self.wait_for_payment_options_window()
        self.click_add_card_info()
        self.wait_card_info_window()
        self.write_card_number(number_card)
        self.write_card_code(code_card)
        self.click_second_row_to_activate_add_button()
        self.click_add_card_button()
        self.wait_for_card_info_window_closing()
        self.click_close_window_button()

