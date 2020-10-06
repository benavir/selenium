from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class ItemHelper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_main_page(self):
        self.driver.get("http://localhost/litecart/en/")
        WebDriverWait(self.driver, 10).until(EC.title_is("Online Store | My Store"))
        return self

    def check_options_height(self):
        size = self.driver.find_elements_by_css_selector('select[name="options[Size]"]')
        if len(size) > 0:
            size[0].click()
            self.driver.find_element_by_css_selector('option[value="Small"]').click()

    def select_first_item(self):
        self.driver.find_elements_by_css_selector('li[class^=product]')[0].click()
        WebDriverWait(self.driver, 10).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src*="1-lonely-duck.jpg"]')))

    def add_item_in_basket(self):
        for quantity in range(1, 4):
            self.select_first_item()
            self.check_options_height()
            time.sleep(1)
            self.driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a.content span.quantity'), "%s" % quantity))
            self.open_main_page()