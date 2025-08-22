from selenium.webdriver.common.by import By
import test_data

def test_view_category_products(driver, home_page):
    '''
    Test Case 18: View Category Products
    '''

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