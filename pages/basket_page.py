from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasketHelper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        self.driver.find_element_by_css_selector('a[href*="checkout"].link').click()
        WebDriverWait(self.driver, 10).until(EC.title_is("Checkout | My Store"))

    def remove_all_items(self):
        items = self.driver.find_elements_by_css_selector('td.item')
        for quantity in range(len(items)):
            if len(self.driver.find_elements_by_css_selector('td a[href*="litecart/en/"]')) != 1:
                element = self.driver.find_element_by_name('remove_cart_item')
                WebDriverWait(self.driver, 10).until((EC.visibility_of(element)))
                element.click()