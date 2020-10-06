import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # wd = webdriver.Chrome(chrome_options=options)
    # wd = webdriver.Chrome(service_log_path="chrome_driver.log", service_args=["--verbose", "--log-path=D:\\qc1.log"])
    # caps = DesiredCapabilities.CHROME
    caps = webdriver.DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    wd = webdriver.Chrome(desired_capabilities=caps, chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_find_logs(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    WebDriverWait(driver, 10).until(EC.title_is("Catalog | My Store"))
    ducks = driver.find_elements_by_css_selector('tr.row a[href*="product"]:not([title])')
    for duck in range(len(ducks)):
        driver.find_elements_by_css_selector('tr.row a[href*="product"]:not([title])')[duck].click()
        logs_browser(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p img")))
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")


def logs_browser(driver):
    for l in driver.get_log("performance"):
        print(l)

