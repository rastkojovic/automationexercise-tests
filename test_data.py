# URLs
BASE_URL = "https://www.automationexercise.com"
LOGIN_PAGE_PATH = "/login"
SIGNUP_PAGE_PATH = "/signup"
CONTACT_PAGE_PATH = "/contact_us"
TEST_CASES_PAGE_PATH = "/test_cases"
PRODUCTS_PAGE_PATH = "/products"
PRODUCT_DETAILS_PAGE_PATH = "/product_details"
DELETE_ACCOUNT_PAGE_PATH = "/delete_account"
CART_PAGE_PATH = "/view_cart"
CHECKOUT_PAGE_PATH = "/checkout"
PAYMENT_PAGE_PATH = "/payment"

# USER DATA
NAME = "Jane"
LAST_NAME = "Doe"
COMPANY = "Fake Inc."
ADDRESS1 = "Fake address 1"
ADDRESS2 = "Fake address 2"
COUNTRY = "Canada"
STATE = "Ontario"
CITY = "Toronto"
ZIP = "111111111"
PHONE_NUM = "416000000000"
EMAIL = "test_8825py@email.com"
DOB = {
    "day": "1",
    "month": "January",
    "year": "1991"
}
PASSWORD = "password"
TITLE = "mrs"
CARD_NUMBER = "0000000000000000"
CVC = "111"
EXPIRY_MONTH = "05"
EXPIRY_YEAR = "2029"

# INVALID DATA
INVALID_EMAIL = "invalid.email@email.xyz"
INVALID_PASSWORD = "Qwerty1234"

# CONTACT DATA
CONTACT_SUBJECT = "Test message"
CONTACT_MESSAGE = "This is a test message. \nAdding another sentence. \nBye."

# PRODUCT 1 DETAILS
PRODUCT1_NAME = "Blue Top"
PRODUCT1_CATEGORY = "Women > Tops"
PRODUCT1_PRICE = "Rs. 500"
PRODUCT1_AVAILABILITY = "In Stock"
PRODUCT1_CONDITION = "New"
PRODUCT1_BRAND = "Polo"

# PRODUCT 2 DETAILS
PRODUCT2_NAME = "Men Tshirt"
PRODUCT2_CATEGORY = "Men > Tshirts"
PRODUCT2_PRICE = "Rs. 400"
PRODUCT2_AVAILABILITY = "In Stock"
PRODUCT2_CONDITION = "New"
PRODUCT2_BRAND = "H&M"

# TITLES AND MESSAGES
HOMEPAGE_TITLE = "AutomationExercise"
LOGGED_IN_MSG = "Logged in as Jane"
SIGNUP_FORM_TITLE = "New User Signup!"
LOGIN_FORM_TITLE = "Login to your account"
SIGNUP_PAGE_TITLE = "ENTER ACCOUNT INFORMATION"
ACCOUNT_CREATED_TITLE = "ACCOUNT CREATED!"
ACCOUNT_DELETED_TITLE = "ACCOUNT DELETED!"
INVALID_CRED_MSG = "Your email or password is incorrect!"
EXISTING_EMAIL_MSG = "Email Address already exist!"
CONTACT_FORM_TITLE = "GET IN TOUCH"
CONTACT_SUCCESS_MESSAGE = "Success! Your details have been submitted successfully."
SEARCH_TITLE = "SEARCHED PRODUCTS"
SUBSCRIPTION_SUCCESS_MESSAGE = "You have been successfully subscribed!"
ORDER_SUCCESS_MESSAGE = "Your order has been placed successfully!"
CATEGORY_TITLES = {
    "Women": {
        "Dress": "WOMEN - DRESS PRODUCTS",
    }, 
    "Men" : { # Normalize title
        "Jeans": "MEN - JEANS PRODUCTS"
    }
}
BRAND_NAMES = ['POLO', 'H&M', 'MADAME', 'MAST & HARBOUR', 'BABYHUG', 'ALLEN SOLLY JUNIOR', 'KOOKIE KIDS', 'BIBA']
BRAND_TITLES = {
    "Kookie Kids": "BRAND - KOOKIE KIDS PRODUCTS"
}