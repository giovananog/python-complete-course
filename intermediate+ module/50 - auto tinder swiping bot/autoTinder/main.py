from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/app/recs")

time.sleep(2)

enter = driver.find_element(By.LINK_TEXT, "Entrar")
enter.click()

time.sleep(3)
exit = driver.find_elements(By.CSS_SELECTOR, "button")
# exit.click()

j = 0
for i in exit:
    j += 1
    if j == 6:
        i.click()



time.sleep(3)


password = driver.find_element(By.CSS_SELECTOR, ".i52ujdq input")
password.send_keys("00")
time.sleep(2)
password.send_keys(Keys.ENTER)


# not finished

driver.close()