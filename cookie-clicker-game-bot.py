from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

current = time.time() + 5
final = time.time() + 60*5

while True:
    cookie.click()
    money = driver.find_element(By.ID, "money")
    money = money.text.strip().replace(",", "")
    items = driver.find_elements(By.CSS_SELECTOR, "#store div b")

    item_prices = []

    for item in items[:-1]:
        new = item.text.split(" - ")[1]
        new = new.strip().replace(",", "")
        item_prices.append(new)

    cookie.click()
    if time.time() >= current:
        for i in range(len(item_prices)-1, 0, -1):
            if int(item_prices[i]) < int(money):
                items[i].click()

        current = time.time() + 20
    if time.time() > final:
        break

# driver.quit()
