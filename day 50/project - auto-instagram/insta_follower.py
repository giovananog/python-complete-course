from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get('https://www.instagram.com/')

        time.sleep(5)
        user_input = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        user_input.send_keys("ex")
        
        time.sleep(5)
        password_input = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        password_input.send_keys("ex")

        time.sleep(5)
        password_input.send_keys(Keys.ENTER)

        time.sleep(10)
        profile = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        profile.send_keys(Keys.ENTER)
        # time.sleep(5)
        # profile = self.driver.find_element(By.XPATH, "//*[@id='mount_0_0_VP']/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[6]/div/span/div/a")
        # profile.send_keys(Keys.ENTER)

        self.driver.get("https://www.instagram.com/chefsteps/followers/")
        time.sleep(10)
        # profile = self.driver.find_element(By.XPATH, "//*[@id='mount_0_0_qB']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
        # profile.send_keys(Keys.ENTER)



    def find_followers(self):
        time.sleep(5)
        # followers = self.driver.find_element(By.XPATH, "//*[@id='mount_0_0_j9']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a")
        # followers.click()

        time.sleep(5)
        followers = self.driver.find_elements(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div")


        for i in followers:
            i.click()
            follow = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button")
            follow.click()


    def follow(self):
        self.driver.close()
