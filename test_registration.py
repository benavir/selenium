import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import string
import random
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


# генерируем рандомный почтовый адрес
def random_postmail(maxlen, suffix):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + suffix


# генерируем рандомные имена и город
def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


# генерируем рандомный адрес
def random_address(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


# генерируем рандомные почтовый индекс и телефон
def random_phone_postcode(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(maxlen)])


def change_field_value(driver, field_name, text):
    if text is not None:
        driver.find_element_by_name(field_name).click()
        driver.find_element_by_name(field_name).clear()
        driver.find_element_by_name(field_name).send_keys(text)


def test_shopping_basket(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is("Online Store | My Store"))
    driver.find_element_by_css_selector('div.content tr td a').click()
    f_name = random_string("F_", 7)
    l_name = random_string("L_", 10)
    address = random_address("ADR_", 12)
    p_code = random_phone_postcode(5)
    city = random_string("CT_", 8)
    email = random_postmail(15, "@qaz.qa")
    phone = random_phone_postcode(11)
    country = driver.find_element_by_css_selector('select[name="country_code"]')
    driver.execute_script("arguments[0].selectedIndex = 224; arguments[0].dispatchEvent(new Event('change'))", country)

    time.sleep(1)
    change_field_value(driver, "firstname", f_name)
    change_field_value(driver, "lastname", l_name)
    change_field_value(driver, "address1", address)
    change_field_value(driver, "postcode", p_code)
    change_field_value(driver, "city", city)
    change_field_value(driver, "email", email)
    change_field_value(driver, "phone", phone)
    change_field_value(driver, "password", "!QAZ2wsx")
    change_field_value(driver, "confirmed_password", "!QAZ2wsx")

    driver.find_element_by_name("create_account").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#notices-wrapper')))

    time.sleep(1)
    driver.find_element_by_css_selector('div.content a[href*="logout"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#box-account-login")))

    change_field_value(driver, "email", email)
    change_field_value(driver, "password", "!QAZ2wsx")
