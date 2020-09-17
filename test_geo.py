import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_geo_countries(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    WebDriverWait(driver, 10).until(EC.title_is("Countries | My Store"))
    names = []
    country_zones = []
    for countries in driver.find_elements_by_css_selector('tbody tr.row'):
        cells = countries.find_elements_by_tag_name("td")
        name = cells[4].text
        zone = cells[5].text
        names.append(name)
        if zone != '0':
            country_zones.append(name)
    zns = []
    for zones in country_zones:
        driver.find_element_by_xpath('//a[text()[normalize-space(.) = "%s"]]' % zones).click()
        for zones in driver.find_elements_by_css_selector('tbody>tr:not([class=header])>td>input[name*="][name]"]'):
            zn = zones.get_attribute("value")
            zns.append(zn)
        ordered_zns = sorted(zns)
        assert zns == ordered_zns
        zns = []
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    ordered_names = sorted(names)
    assert names == ordered_names


def test_geo_zones(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    WebDriverWait(driver, 10).until(EC.title_is("Geo Zones | My Store"))
    countries_list = []
    for country in driver.find_elements_by_css_selector('tr>td>a:not([title=Edit])'):
        cntry = country.text
        countries_list.append(cntry)
    for cnt in countries_list:
        driver.find_element_by_xpath('//a[text()[normalize-space(.) = "%s"]]' % cnt).click()
        zns = []
        # for zones in driver.find_elements_by_css_selector('tbody>tr:not([class=header])>td>select[name*="][zone_code]"]'):
        for zones in driver.find_elements_by_css_selector('option[selected]:not([data-tax-id-format])'):
            zone = zones.text
            zns.append(zone)
        ordered_zns = sorted(zns)
        assert zns == ordered_zns
        zns = []
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")