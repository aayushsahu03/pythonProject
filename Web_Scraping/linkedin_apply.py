from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL_ID = "aayush.sahu.03@gmail.com"
PASSWD = "Dummy"
MAX_TIME_OUT = 20


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
try:
    reject_button.click()
except NoSuchElementException:
    pass

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

username = driver.find_element(by=By.ID, value='username')
username.send_keys(EMAIL_ID)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWD)
password_field.send_keys(Keys.ENTER)

print("Complete Captcha to proceed")