import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

#     driver.find_element_by_css_selector('a[href*="template"]').click()
#     # driver.get("http://localhost/litecart/admin/?app=appearance&doc=template")
#     # driver.find_element_by_xpath('//span[text()[normalize-space(.) = "Appearence"]]').click()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1")))
#     # WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//h1'), "Template"))
#     # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[contains(.," Template")]')))
#     driver.find_element_by_css_selector('a[href*="logotype"]').click()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1")))


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
    rows = driver.find_elements_by_css_selector('div>ul>li>a')
    for number in range(len(rows)):
        maxi_element = driver.find_elements_by_css_selector('div>ul>li')[number]
        maxi_element.click()
        mini_elements = driver.find_elements_by_css_selector('div>ul>li')[number].find_elements_by_css_selector('li>ul>li')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1")))
        for number_mini in range(len(mini_elements)):
            driver.find_elements_by_css_selector('div>ul>li')[number].find_elements_by_css_selector('li>ul>li')[
                number_mini].click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1")))
