from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
PROMISED_DOWN = 150
PROMISED_UP = 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0 

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        button = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        self.driver.close()


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(5)
        input = self.driver.find_element(By.CSS_SELECTOR, "input")
        time.sleep(5)
        input.send_keys("ex@gmail.com")
        time.sleep(5)
        input.send_keys(Keys.ENTER)
        password = self.driver.find_element(By.NAME, "password")
        time.sleep(5)
        password.send_keys("ex@gmail.com")
        time.sleep(5)
        password.send_keys(Keys.ENTER)
        tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div")
        time.sleep(5)
        tweet.send_keys(f"WELL, my download internet speed is currently {self.down} when it should be {PROMISED_DOWN}, so as my upload speed, that right now is {self.up} but it was supposed to be {PROMISED_UP}")
        time.sleep(5)
        tweet.send_keys(Keys.ENTER)

        self.driver.close()

