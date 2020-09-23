import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_shopping_basket(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is("Online Store | My Store"))
    products = driver.find_elements_by_css_selector('li[class^=product]')
    first_product = driver.find_elements_by_css_selector('li[class^=product]')[0]
    
