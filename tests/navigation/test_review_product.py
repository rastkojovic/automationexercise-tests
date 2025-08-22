from pages.product_page import ProductPage
from pages.product_details_page import ProductDetailsPage
import test_data

def test_review_product(driver, home_page):
    '''
    Test Case 21: Add review on product
    '''

    home_page.nav.click_products()
    assert test_data.PRODUCTS_PAGE_PATH in driver.current_url, f"Expected URL: '{test_data.PRODUCTS_PAGE_PATH}', actual URL: '{driver.current_url}'"

    product_page = ProductPage(driver)
    product_page.view_product(3)

    product_details_page = ProductDetailsPage(driver)
    review_title = product_details_page.get_review_title()
    expected_review_title = "Write Your Review"
    assert expected_review_title.lower() == review_title.lower(), f"Expected title: {expected_review_title}, actual title: '{review_title}'"
    
    product_details_page.enter_name(test_data.NAME)
    product_details_page.enter_email(test_data.EMAIL)
    product_details_page.enter_review("This is a great product!")
    product_details_page.submit_review()
    review_message = product_details_page.get_review_message()
    expected_review_message = "Thank you for your review."
    assert expected_review_message.lower() == review_message.lower(), f"Expected message: '{expected_review_message}', actual message: '{review_message}'"