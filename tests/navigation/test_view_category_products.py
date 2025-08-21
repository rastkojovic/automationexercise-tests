from pages.home_page import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import test_data

def test_view_category_products(driver):
    '''
    Test Case 18: View Category Products
    '''

    home_page = HomePage(driver)
    home_page.open()

    homepage_title = driver.find_element(By.TAG_NAME, "h1").text
    assert test_data.BASE_URL in driver.current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{driver.current_url}'"
    assert test_data.HOMEPAGE_TITLE in homepage_title, f"Expected title: '{test_data.HOMEPAGE_TITLE}', actual title: '{homepage_title}'"

    expected_categories = ["MEN", "WOMEN", "KIDS"]
    category_names = home_page.get_category_names()

    for category in expected_categories:
        assert category in category_names, f"Category '{category}' not found!"    

    home_page.select_category(category_name="Women",subcategory_name="Dress")
    selected_category = driver.find_element(By.CSS_SELECTOR, "h2.title").text
    # Remove NBSP and normalize
    selected_category = " ".join(selected_category.replace("\xa0", " ").split())
    dress_title = test_data.CATEGORY_TITLES["Women"]["Dress"]
    assert dress_title in selected_category, f"Expected category: '{dress_title}', actual category: '{selected_category}'"

    home_page.select_category(category_name="Men", subcategory_name="Jeans")
    selected_category = driver.find_element(By.CSS_SELECTOR, "h2.title").text
    # Remove NBSP and normalize
    selected_category = " ".join(selected_category.replace("\xa0", " ").split())
    jeans_title = test_data.CATEGORY_TITLES["Men"]["Jeans"]
    assert jeans_title in selected_category, f"Expected category: '{jeans_title}', actual category: '{selected_category}'"