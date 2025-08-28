from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

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

def scroll_by_arrow_key_until_visible(driver, element, poll_interval=0.01, max_iterations=500):
    # Keep scrolling until element in viewport
    iterations = 0
    while not _in_viewport(driver, element) and iterations <= max_iterations:
        ActionChains(driver).send_keys(Keys.DOWN).perform()
        iterations += 1
        time.sleep(poll_interval)
    if iterations >= max_iterations:    
        raise AssertionError("Timed out while scrolling to element")

def test_verify_scroll_arrow(driver, home_page):
    '''
    Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
    '''
    subscription_title = driver.find_element(By.CSS_SELECTOR, "#footer h2")
    driver.find_element(By.TAG_NAME, "body").click()
    scroll_by_arrow_key_until_visible(driver, subscription_title)

    assert _in_viewport(driver, subscription_title), f"Subscription title not in viewport!"

    home_page.click_up()
    subheading = driver.find_element(By.CSS_SELECTOR, ".carousel-inner .active h2")
    WebDriverWait(driver, 10).until(lambda d: _in_viewport(d, subheading))
    
    assert _in_viewport(driver, subheading), f"Subheading not in viewport!"