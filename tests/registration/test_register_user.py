from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_data
from pages.signup_page import SignupPage
from pages.delete_page import DeletePage

def test_register_user(driver, home_page):
    '''
    Test Case 1: Register User
    '''

    home_page.nav.click_signup_login()

    signup_form_title = home_page.get_signup_form_title()
    assert signup_form_title == test_data.SIGNUP_FORM_TITLE, f"Expected signup form title: '{test_data.SIGNUP_FORM_TITLE}', actual signup form title: '{signup_form_title}'"

    signup_page = SignupPage(driver)
    signup_page.enter_name(test_data.NAME)
    signup_page.enter_email(test_data.EMAIL)
    signup_page.click_signup_button()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains(test_data.SIGNUP_PAGE_PATH))

    signup_page_title = signup_page.get_signup_page_title()
    assert signup_page_title == test_data.SIGNUP_PAGE_TITLE, f"Expected title: '{test_data.SIGNUP_PAGE_TITLE}', actual title: {signup_page_title}"

    signup_page.select_title(test_data.TITLE)
    signup_page.enter_password(test_data.PASSWORD)
    signup_page.select_dob(day=test_data.DOB["day"], month=test_data.DOB["month"], year=test_data.DOB["year"])
    signup_page.check_newsletter()
    signup_page.check_special()
    signup_page.enter_first_name(test_data.NAME)
    signup_page.enter_last_name(test_data.LAST_NAME)
    signup_page.enter_company_name(test_data.COMPANY)
    signup_page.enter_address1(test_data.ADDRESS1)
    signup_page.enter_address2(test_data.ADDRESS2)
    signup_page.select_country(test_data.COUNTRY)
    signup_page.enter_state(test_data.STATE)
    signup_page.enter_city(test_data.CITY)
    signup_page.enter_zipcode(test_data.ZIP)
    signup_page.enter_mobile(test_data.PHONE_NUM)
    signup_page.create_account()

    account_created_title = signup_page.get_account_created_title()
    assert account_created_title == test_data.ACCOUNT_CREATED_TITLE, f"Expected H2 title: '{test_data.ACCOUNT_CREATED_TITLE}', actual H2 title: '{account_created_title}'"
    
    signup_page.click_continue_btn()

    logged_in_text = signup_page.nav.get_loggedin_msg()
    assert logged_in_text == f"Logged in as {test_data.NAME}", f"Expected text: 'Logged in as {test_data.NAME}', actual text: '{logged_in_text}'"

    signup_page.nav.click_delete_account()

    delete_page = DeletePage(driver)
    account_deleted_title = delete_page.get_account_deleted_title()
    assert account_deleted_title == test_data.ACCOUNT_DELETED_TITLE, f"Expected title: '{test_data.ACCOUNT_DELETED_TITLE}', actual title: '{account_deleted_title}'"

    delete_page.click_continue_btn()