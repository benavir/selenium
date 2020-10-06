from selenium import webdriver
from pages.item_page import ItemHelper
from pages.basket_page import BasketHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.item_page = ItemHelper(self.driver)
        self.basket_page = BasketHelper(self.driver)

    def quit(self):
        self.driver.quit()

    def add_item_in_basket(self):
        self.item_page.open_main_page()
        self.item_page.add_item_in_basket()

    def remove_all_from_basket(self):
        self.basket_page.checkout()
        self.basket_page.remove_all_items()
