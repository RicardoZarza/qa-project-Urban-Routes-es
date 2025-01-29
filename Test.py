import data
import locators
from locators import UrbanRoutesComfortFormLocators
from main import UrbanRoutesPage, UrbanRoutesComfortForm, UrbanRoutesAddPhone, UrbanRoutesPaymentMethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        actual_address_from =  routes_page.get_from()
        actual_address_to = routes_page.get_to()
        assert data.address_from == actual_address_from
        assert data.address_to == actual_address_to

    def test_add_blanket_and_tissue(self):
        comfort_form = UrbanRoutesComfortForm(self.driver)
        comfort_form.look_for_comfort_taxi()
        comfort_form.add_blanket_option_checked()
        actual_option_for_blanket_status = comfort_form.get_blanket_and_handkerchiefs_option_checked()
        assert  actual_option_for_blanket_status == data.blanket_and_tissue

    def test_add_comment_to_driver(self):
        comfort_form = UrbanRoutesComfortForm(self.driver)
        comfort_form.add_comment_for_driver(data.message_for_driver)
        actual_message_for_driver = comfort_form.get_comment()
        assert actual_message_for_driver == data.message_for_driver

    def test_ask_for_two_icecream(self):
        comfort_form = UrbanRoutesComfortForm(self.driver)
        comfort_form.ask_for_ice_cream()
        actual_number_of_iceream = comfort_form.get_ice_cream_number()
        assert actual_number_of_iceream == data.ice_cream_number


    def test_add_card(self):
        add_card_page = UrbanRoutesPaymentMethod(self.driver)
        add_card_page.add_a_new_payment_card(data.card_number, data.card_code)
        actual_card_number = add_card_page.get_card_number()
        actual_card_code = add_card_page.get_card_code()
        actual_payment_method = add_card_page.confirm_payment_method()
        assert actual_card_number == data.card_number
        assert actual_card_code == data.card_code
        assert actual_payment_method == data.payment_method

    def test_add_phone(self):
        add_phone_page = UrbanRoutesAddPhone(self.driver)
        add_phone_page.add_new_phone_number(data.phone_number)
        actual_phone_number = add_phone_page.get_phone_number()
        ask_for_taxi = add_phone_page.ask_for_taxi_enabled()
        assert actual_phone_number == data.phone_number
        assert ask_for_taxi == data.ask_for_taxi_button_enabled_text
        print("El modal para buscar taxi ha aparecido, la prueba concluyó")


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
