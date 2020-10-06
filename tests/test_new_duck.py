import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import string
import random
import datetime
import os.path


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


# генерируем рандомные имена и код
def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


# генерируем рандомное число
def random_digit(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(maxlen)])


# заполнение форм ввода
def change_field_value(driver, field_name, text):
    if text is not None:
        driver.find_element_by_name(field_name).click()
        driver.find_element_by_name(field_name).clear()
        driver.find_element_by_name(field_name).send_keys(text)


def test_add_duck(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))

    # catalog page
    time.sleep(1)
    driver.find_element_by_css_selector('div>ul>li>a[href*="catalog"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1")))
    driver.find_element_by_css_selector('div>a[href*="edit_product"]').click()
    # name = driver.find_element_by_css_selector("#content h1").get_attribute("textContent")
    # nm = name.replace("\n ",'')
    # n = nm.replace(" ",'')
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content h1"), "Add New Product"))

    time.sleep(1)
    driver.find_element_by_css_selector('label input[value="1"]').click()
    name = random_string("N_", 7)
    code = random_string("C_", 5)
    change_field_value(driver, "name[en]", name)
    change_field_value(driver, "code", code)
    gender = driver.find_elements_by_css_selector('input[type="checkbox"][name="product_groups[]"]')[2].click()
    quantity = random_digit(1)
    if quantity == '0':
        quantity = 1
    change_field_value(driver, "quantity", quantity)

    date_from = datetime.date.today()
    d_f = date_from.strftime("%d%m%Y")
    date_to = '31122020'
    change_field_value(driver, "date_valid_from", d_f)
    change_field_value(driver, "date_valid_to", date_to)

    f = "pictures\Rubber_duck.jpg"
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f)
    driver.find_element_by_css_selector('input[type="file"]').send_keys(file)

    # informatoin page
    driver.find_element_by_css_selector('a[href*="information"]').click()
    driver.find_element_by_name('manufacturer_id').click()
    Select(driver.find_element_by_name("manufacturer_id")).select_by_visible_text("ACME Corp.")
    driver.find_element_by_name('supplier_id').click()
    Select(driver.find_element_by_name("supplier_id")).select_by_visible_text("-- Select --")

    keywords = random_string("KW_", 10)
    change_field_value(driver, "keywords", keywords)
    short_description = random_string("SD_", 10)
    change_field_value(driver, "short_description[en]", short_description)
    description = random_string("DESCRIPTION_", 10)
    driver.find_element_by_css_selector('div.trumbowyg-editor').click()
    driver.find_element_by_css_selector('div.trumbowyg-editor').clear()
    driver.find_element_by_css_selector('div.trumbowyg-editor').send_keys(description)
    # change_field_value(driver, "description[en]", description)
    head_title = random_string("HEAD_", 10)
    change_field_value(driver, "head_title[en]", head_title)
    meta_description = random_string("META_", 10)
    change_field_value(driver, "meta_description[en]", meta_description)

    # prices page
    driver.find_element_by_css_selector('a[href*="prices"]').click()
    price = random_digit(1)
    if price == '0':
        price = 1
    change_field_value(driver, "purchase_price", price)
    driver.find_element_by_name('purchase_price_currency_code').click()
    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_visible_text("US Dollars")
    usd_eur = random_digit(2)
    if usd_eur in ['0','1','2','3','4','5','6','7','8','9']:
        usd_eur = 11
    change_field_value(driver, "prices[USD]", usd_eur)
    change_field_value(driver, "prices[EUR]", usd_eur)

    driver.find_element_by_name('save').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="notice success"]')))
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'table.dataTable a[href*="edit_product"]'), "%s" % name))
