from selenium import webdriver
from selenium.webdriver.common.by import By
# keep Chrome brownser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# driver.close() close tab
# driver.quit() close all tabs that are open

a = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li")

dict_events = {i.text.split()[0]:" ".join(i.text.split()[1:]) for i in a}

for key, value in dict_events.items():
    print(f"Chave: {key}, Valor: {value}")

driver.close()