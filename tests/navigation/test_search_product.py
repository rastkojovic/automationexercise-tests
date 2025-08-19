from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.home_page import HomePage
from pages.product_page import ProductPage
import test_data
import pytest

@pytest.mark.xfail(reason="The search results return non-matching products; product bug", strict=True)
def test_search_product(driver):

    home_page = HomePage(driver)
    home_page.open()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.BASE_URL))

    current_url = driver.current_url
    homepage_title = home_page.get_title()

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert homepage_title == test_data.HOMEPAGE_TITLE, f"Expected H1 text: {test_data.HOMEPAGE_TITLE}, actual H1 text: {homepage_title}"

    home_page.click_products()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.PRODUCTS_PAGE_PATH))

    product_page = ProductPage(driver)
    product_name = "dress"
    product_page.search(product_name)

    search_title = product_page.get_search_title()
    assert test_data.SEARCH_TITLE in search_title, f"Expected search title: '{test_data.SEARCH_TITLE}', actual search title: '{search_title}'"

    product_names = product_page.get_product_names()

    assert product_page.check_search_results(product_name, product_names), f"The product list does not match the search term '{product_name}'"