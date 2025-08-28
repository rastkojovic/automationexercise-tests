from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

def _in_viewport(driver, element):
    "Check if element is in browser's current viewport"
    
    script = """
var rect = arguments[0].getBoundingClientRect();
const vw = window.innerWidth || document.documentElement.clientWidth;
const vh = window.innerHeight || document.documentElement.clientHeight;
const partiallyInView =
  rect.right > 0 && rect.bottom > 0 && rect.left < vw && rect.top < vh &&
  rect.width > 0 && rect.height > 0;

return partiallyInView
"""
    return driver.execute_script(script, element)

def test_verify_scroll_without_arrow(driver, home_page):
    '''
    Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality
    '''
    wait = WebDriverWait(driver, 10)
    subscription_title = driver.find_element(By.CSS_SELECTOR, "#footer h2")
    ActionChains(driver).scroll_to_element(subscription_title).perform()

    wait.until(lambda d: _in_viewport(d, subscription_title))
    assert _in_viewport(driver, subscription_title), f"Subscription title not in viewport!"
    
    home_page.click_up()
    subheading = driver.find_element(By.CSS_SELECTOR, ".carousel-inner .active h2")
    
    wait.until(lambda d: _in_viewport(d, subheading))
    assert _in_viewport(driver, subheading), f"Subheading not in viewport!"