from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_data
from pages.contact_page import ContactPage

def test_contact_form(driver, home_page):
    '''
    Test Case 6: Contact Us Form
    '''

    home_page.nav.click_contact()
    
    contact_page = ContactPage(driver)
    contact_form_title = contact_page.get_form_title()

    assert contact_form_title == test_data.CONTACT_FORM_TITLE, f"Expected H2 text: '{test_data.CONTACT_FORM_TITLE}', actual H2 text: '{contact_form_title}'"

    contact_page.enter_name(test_data.NAME)
    contact_page.enter_email(test_data.EMAIL)
    contact_page.enter_subject(test_data.CONTACT_SUBJECT)
    contact_page.enter_message(test_data.CONTACT_MESSAGE)
    # Create dummy file for upload
    with open(file="dummy_file.txt", mode="w") as file:
        for _ in range(20):
            file.write(f"Test file.\n")
    contact_page.upload_file("dummy_file.txt")
    contact_page.submit()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    success_message = contact_page.get_success_msg()
    assert success_message == test_data.CONTACT_SUCCESS_MESSAGE, f"Expected message: '{test_data.CONTACT_SUCCESS_MESSAGE}', actual message: '{success_message}'"

    contact_page.click_home_button()

    wait.until(EC.url_contains(test_data.BASE_URL))

    assert test_data.BASE_URL in driver.current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{driver.current_url}'"