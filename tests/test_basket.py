import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_shopping_basket(driver):
    open_main_page(driver)
    # driver.get("http://localhost/litecart/en/")
    # WebDriverWait(driver, 10).until(EC.title_is("Online Store | My Store"))
    add_item_in_basket(driver)
    # for quantity in range(1, 4):
    #     select_first_item(driver)
    #     # driver.find_elements_by_css_selector('li[class^=product]')[0].click()
    #     # WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src*="1-lonely-duck.jpg"]')))
    #     check_options_height(driver)
    #     # size = driver.find_elements_by_css_selector('select[name="options[Size]"]')
    #     # if len(size) > 0:
    #     #     size[0].click()
    #     #     driver.find_element_by_css_selector('option[value="Small"]').click()
    #     time.sleep(1)
    #     driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
    #     WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a.content span.quantity'), "%s" % quantity))
    #     driver.find_element_by_css_selector('div.middle a[href="/litecart/"]').click()
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src*="1-lonely-duck.jpg"]')))
    time.sleep(1)
    checkout(driver)
    # driver.find_element_by_css_selector('a[href*="checkout"].link').click()
    # WebDriverWait(driver, 10).until(EC.title_is("Checkout | My Store"))
    remove_all_items(driver)
    # items = driver.find_elements_by_css_selector('td.item')
    # for quantity in range(len(items)):
    #     if len(driver.find_elements_by_css_selector('td a[href*="litecart/en/"]')) != 1:
    #         element = driver.find_element_by_name('remove_cart_item')
    #         WebDriverWait(driver, 10).until((EC.visibility_of(element)))
    #         element.click()


def open_main_page(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is("Online Store | My Store"))


def check_options_height(driver):
    size = driver.find_elements_by_css_selector('select[name="options[Size]"]')
    if len(size) > 0:
        size[0].click()
        driver.find_element_by_css_selector('option[value="Small"]').click()


def checkout(driver):
    driver.find_element_by_css_selector('a[href*="checkout"].link').click()
    WebDriverWait(driver, 10).until(EC.title_is("Checkout | My Store"))


def remove_all_items(driver):
    items = driver.find_elements_by_css_selector('td.item')
    for quantity in range(len(items)):
        if len(driver.find_elements_by_css_selector('td a[href*="litecart/en/"]')) != 1:
            element = driver.find_element_by_name('remove_cart_item')
            WebDriverWait(driver, 10).until((EC.visibility_of(element)))
            element.click()


def select_first_item(driver):
    driver.find_elements_by_css_selector('li[class^=product]')[0].click()
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src*="1-lonely-duck.jpg"]')))


def add_item_in_basket(driver):
    for quantity in range(1, 4):
        select_first_item(driver)
        # driver.find_elements_by_css_selector('li[class^=product]')[0].click()
        # WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src*="1-lonely-duck.jpg"]')))
        check_options_height(driver)
        # size = driver.find_elements_by_css_selector('select[name="options[Size]"]')
        # if len(size) > 0:
        #     size[0].click()
        #     driver.find_element_by_css_selector('option[value="Small"]').click()
        time.sleep(1)
        driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a.content span.quantity'), "%s" % quantity))
        open_main_page(driver)
        # заменил на открытие главной страницы, т.к. загрузка наличие картинки и заголовка следствие открытия главной страницы
        # driver.find_element_by_css_selector('div.middle a[href="/litecart/"]').click()
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src*="1-lonely-duck.jpg"]')))
