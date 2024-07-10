from selenium import webdriver
from selenium.webdriver.common.by import By

ZILLOW_CLONE = "https://appbrewery.github.io/Zillow-Clone/"
FORMS = "YOUR FORMS LINK"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(ZILLOW_CLONE)

ADDRESS = [item.text.replace(" | ", " ") for item in driver.find_elements(By.CSS_SELECTOR, "#grid-search-results ul li a address")]
LINK = [item.get_attribute("href") for item in driver.find_elements(By.CSS_SELECTOR, "#grid-search-results ul li a")]
COST = [item.text.replace("/mo", "").split("+")[0] for item in driver.find_elements(By.CLASS_NAME, "PropertyCardWrapper__StyledPriceLine")]

driver.get(FORMS)

# the X-PATH would change acc to the google forms arrangement

for i in range(len(ADDRESS)):
    address = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    cost = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(ADDRESS[i])
    link.send_keys(LINK[i])
    cost.send_keys(COST[i])
    submit.click()
    
    another = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another.click()
    
driver.quit()
