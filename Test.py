import data
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

    def test_comfort_taxi_form(self):
        comfort_form = UrbanRoutesComfortForm(self.driver)
        comfort_form.look_for_comfort_taxi(data.message_for_driver)

    def test_add_phone(self):
        add_phone_page = UrbanRoutesAddPhone(self.driver)
        add_phone_page.add_new_phone_number(data.phone_number)

    def test_add_card(self):
        self.driver.get(data.urban_routes_url)
        add_card_page = UrbanRoutesPaymentMethod(self.driver)
        add_card_page.add_a_new_payment_card(data.card_number, data.card_code)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
