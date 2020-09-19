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


def test_price(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is("Online Store | My Store"))
    regular_price = driver.find_elements_by_css_selector('div#box-campaigns li a div s.regular-price')[0]
    campaign_price = driver.find_elements_by_css_selector('div#box-campaigns li a div strong.campaign-price')[0]
    name = driver.find_elements_by_css_selector('div#box-campaigns li a div.name')[0].text
    reg_price = regular_price.text
    camp_price = campaign_price.text
    reg_size = regular_price.size
    camp_size = campaign_price.size
    check_size(reg_size, camp_size)

    color_reg_price = regular_price.value_of_css_property('color')
    color_camp_price = campaign_price.value_of_css_property('color')
    c_r_p = color_reg_price.replace('rgba(','')
    c_c_p = color_camp_price.replace('rgba(', '')
    check_color(c_r_p, c_c_p)

    driver.find_element_by_css_selector('div#box-campaigns li').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.manufacturer a")))
    regular_price_prod = driver.find_element_by_css_selector('s.regular-price')
    campaign_price_prod = driver.find_element_by_css_selector('strong.campaign-price')
    name_prod = driver.find_element_by_css_selector('div h1').text
    reg_price_prod = regular_price_prod.text
    camp_price_prod = campaign_price_prod.text
    reg_size = regular_price_prod.size
    camp_size = campaign_price_prod.size
    check_size(reg_size, camp_size)

    color_reg_price_prod = regular_price_prod.value_of_css_property('color')
    color_camp_price_prod = campaign_price_prod.value_of_css_property('color')
    c_r_p = color_reg_price_prod.replace('rgba(','')
    c_c_p = color_camp_price_prod.replace('rgba(', '')
    check_color(c_r_p, c_c_p)

    if name == name_prod:
        print("Names are same")
    else:
        print("Names are different")
    if reg_price == reg_price_prod:
        print("Regular prices are same")
    else:
        print("Regular prices are different")
    if camp_price == camp_price_prod:
        print("Campaign prices are same")
    else:
        print("Campaign prices are different")


def check_color(c_r_p, c_c_p):
    new_c_r_p = c_r_p.split(',')
    new_c_c_p = c_c_p.split(',')
    if int(new_c_r_p[0]) == int(new_c_r_p[1]) == int(new_c_r_p[2]):
        print("Color is green")
    else:
        print("Color is not green")
    if int(new_c_c_p[1]) == int(new_c_c_p[2]):
        print("Color is red")
    else:
        print("Color is not red")


def check_size(reg_size, camp_size):
    reg_size_height = reg_size['height']
    reg_size_width = reg_size['width']
    camp_size_height = camp_size['height']
    camp_size_width = camp_size['width']
    if (reg_size_height < camp_size_height) and (reg_size_width < camp_size_width):
        print("Campaign price bigger than regular price")
    else:
        print("Regular price bigger than campaign price")