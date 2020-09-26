import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(desired_capabilities={"pageLoadStrategy": "eager"})
    request.addfinalizer(wd.quit)
    return wd


def test_edit_countries(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    WebDriverWait(driver, 10).until(EC.title_is("Countries | My Store"))
    # выбираем рандомное число из идентификатора стран и кликаем на кнопку редактирования страны
    index = random.randint(1, 239)
    driver.find_elements_by_css_selector('i.fa-pencil')[index].click()
    main_window = driver.current_window_handle
    old_windows = driver.window_handles
    old_string = ','.join(old_windows)
    links = driver.find_elements_by_css_selector('i.fa-external-link')
    for link in range(len(links)):
        links[link].click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        new_windows = driver.window_handles
        new_string = ','.join(new_windows)
        string = new_string.replace(old_string, '')
        another_string = string.replace(",", '')
        # это список идентификаторов новых окон
        # another_string = list([string.replace(",", '')])
        driver.switch_to_window(another_string)
        # WebDriverWait(driver, 10).until_not(EC.title_is("Edit Country | My Store"))
        driver.close()
        driver.switch_to_window(main_window)
