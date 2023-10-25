from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3719639765&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

enter = driver.find_element(By.LINK_TEXT, "Entrar")
time.sleep(3)
enter.click()

time.sleep(2)
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("ex@gmail.com")

time.sleep(3)
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("ex")

time.sleep(2)
password.send_keys(Keys.ENTER)

jobs = driver.find_elements(By.CSS_SELECTOR, ".artdeco-entity-lockup__title a")


for i in jobs:
    time.sleep(5)
    i.click()
    time.sleep(3)
    save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    save_button.click()
    # jobs = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list")


driver.close()