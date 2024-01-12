from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless") 

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D")

address = [i.text for i in driver.find_elements(By.CSS_SELECTOR, "address")]
price = [i.text.split("$")[1].split("/")[0] for i in driver.find_elements(By.CSS_SELECTOR, ".PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")]
link = [i.text.split()[2] for i in driver.find_element(By.CSS_SELECTOR, ".property-card-data a")]

print(price)
print(address)
print(link)

driver.close()

driver.get("https://docs.google.com/forms/d/e/1FAIpQLScjSY9HD9IascFzby-P21FZ_YrJEnV4DlbW-ZgADZIAVHarsg/viewform?usp=sf_link")

address_input = driver.find_element(By.XPATH, "//*[@id='SchemaEditor']/div/div[2]/div/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/input")
price_input = driver.find_element(By.XPATH, "//*[@id='SchemaEditor']/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/input")
link_input = driver.find_element(By.XPATH, "//*[@id='SchemaEditor']/div/div[2]/div/div[2]/div[3]/div[3]/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/input")
send_form  = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/div[2]")

for i in range(len(link)):
    address_input = address[i]
    link_input = link[i]
    price_input = price[i]
    send_form.click()

