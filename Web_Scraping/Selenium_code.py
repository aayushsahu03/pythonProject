import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# ChromeOptions need to be set to stop that from happening
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.in/Instant-Pot-Duo-Multi-Functional-Pressure/dp/B01NBKTPTS")

# price_rupees =  driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_paise =  driver.find_element(By.CLASS_NAME, value='a-price-fraction')
driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, value='submit')
# print(search_bar.get_attribute('name'))

events_list_time = driver.find_elements(By.CSS_SELECTOR,'.medium-widget.event-widget time')
events_list_name = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')
# events_dict= {event.find_element(By.CSS_SELECTOR,'').text:event.find_element(By.CSS_SELECTOR,'ul li a').text for event in events_list}
events_dict = {events_list_time[i].text:events_list_name[i].text for i in range(len(events_list_name))}
print(events_dict)

driver.close()

## CODE BELOW IS OF ANOTHER COOKIE PROGRAM

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break


