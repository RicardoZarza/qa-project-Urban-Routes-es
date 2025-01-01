import data
import main
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

    def test_comfort_taxi_form(self):
        comfort_form = UrbanRoutesComfortForm(self.driver)
        comfort_form.look_for_comfort_taxi(data.message_for_driver)
        actual_message_for_driver = comfort_form.get_comment()
        assert actual_message_for_driver == data.message_for_driver

    def test_add_phone(self):
        add_phone_page = UrbanRoutesAddPhone(self.driver)
        add_phone_page.add_new_phone_number(data.phone_number)
        main.retrieve_phone_code(self.driver)
        actual_phone_number = add_phone_page.get_phone_number()
        assert actual_phone_number == data.phone_number

    def test_add_card(self):
        add_card_page = UrbanRoutesPaymentMethod(self.driver)
        add_card_page.add_a_new_payment_card(data.card_number, data.card_code)
        actual_card_number = add_card_page.get_card_number()
        actual_card_code = add_card_page.get_card_code()
        assert actual_card_number == data.card_number
        assert actual_card_code == data.card_code

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
