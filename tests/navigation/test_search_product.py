from pages.product_page import ProductPage
import test_data
import pytest

@pytest.mark.xfail(reason="The search results return non-matching products; product bug", strict=True)
def test_search_product(driver, home_page):
    '''
    Test Case 9: Search Product
    '''

    home_page.nav.click_products()

    product_page = ProductPage(driver)
    product_name = "dress"
    product_page.search(product_name)

    search_title = product_page.get_search_title()
    assert test_data.SEARCH_TITLE in search_title, f"Expected search title: '{test_data.SEARCH_TITLE}', actual search title: '{search_title}'"

    product_names = product_page.get_product_names()

    assert product_page.check_search_results(product_name, product_names), f"The product list does not match the search term '{product_name}'"