from pages.product_page import ProductPage
import test_data


def test_search_product(driver, home_page):
    '''
    Test Case 9: Search Product
    '''

    home_page.nav.click_products()

    product_page = ProductPage(driver)
    search_term = "tshirt"
    product_page.search(search_term)

    search_title = product_page.get_search_title()
    assert test_data.SEARCH_TITLE in search_title, f"Expected search title: '{test_data.SEARCH_TITLE}', actual search title: '{search_title}'"

    product_names = product_page.get_product_names()
    check = product_page.check_search_results(search_term, product_names)
    assert check is True, f"The following product(s): {check} do not match the search term '{search_term}'"