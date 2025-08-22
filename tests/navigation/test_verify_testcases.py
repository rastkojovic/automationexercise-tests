import test_data

def test_verify_testcases(driver, home_page):
    '''
    Test Case 7: Verify Test Cases Page
    '''

    home_page.nav.click_testcases()

    assert test_data.TEST_CASES_PAGE_PATH in driver.current_url, f"Expected URL: '{test_data.TEST_CASES_PAGE_PATH}', actual URL: '{driver.current_url}'"