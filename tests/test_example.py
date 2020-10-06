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

#     driver.find_element_by_css_selector('a[href*="template"]').click()
#     # driver.get("http://localhost/litecart/admin/?app=appearance&doc=template")
#     # driver.find_element_by_xpath('//span[text()[normalize-space(.) = "Appearence"]]').click()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1")))
#     # WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//h1'), "Template"))
#     # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[contains(.," Template")]')))
#     driver.find_element_by_css_selector('a[href*="logotype"]').click()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content h1")))


def test_side_menu(driver):
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


def test_stickers(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is("Online Store | My Store"))
    products = driver.find_elements_by_css_selector('li[class^=product]')
    for duck in range(len(products)):
        positions = []
        all_prod = driver.find_elements_by_css_selector('li[class^=product]')[duck]
        sticker = all_prod.find_elements_by_css_selector('div[class^=sticker]')
        for labels in sticker:
            text = labels.text
            positions.append(text)
        #     assert len(positions) == 1
        # print(positions)
        try:
            if len(positions) == 1:
                print(positions)
            else:
                print(positions, 'Too many labels')
        except:
            pass


def test_price(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is("Online Store | My Store"))
    products = driver.find_elements_by_css_selector('li[class^=product]')
    for duck in range(len(products)):
        positions = []
        all_prod = driver.find_elements_by_css_selector('li[class^=product]')[duck]
        sticker = all_prod.find_elements_by_css_selector('div>*[class*=price]')
        for dollars in sticker:
            text = dollars.text
            positions.append(text)
        try:
            if len(positions) == 1:
                print(positions)
            else:
                print(positions, 'Too many prices')
        except:
            pass


def check_county_zones(driver, zones):
    exec(f"""driver.find_element_by_xpath("//a[text() = '{zones}']").click()""")
    driver.find_elements_by_css_selector('tbody>tr:not([class=header])>td>input[name*="][name]"]')
