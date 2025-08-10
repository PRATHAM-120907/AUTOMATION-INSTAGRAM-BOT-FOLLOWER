from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT = "to go"
USER_NAME = "username of your's"
PASSWORD = "your password"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        # Accept cookies if prompted
        try:
            cookies = self.driver.find_element(By.XPATH, "//button[text()='Only allow essential cookies']")
            cookies.click()
        except:
            pass

        # Login input
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(USER_NAME)
        password.send_keys(PASSWORD)

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(5)

        # Handle Save Login Info popup
        try:
            not_now = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not now')]")
            not_now.click()
            time.sleep(3)
        except:
            pass

        # Handle Notification popup
        try:
            not_now = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
            not_now.click()
            time.sleep(3)
        except:
            pass

    def find_followers(self):
        # Go to target account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)

        # Click on 'followers'
        followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        followers_link.click()
        time.sleep(5)

        # Scroll followers modal
        modal = self.driver.find_element(By.XPATH, "//div[@role='dialog']//div[@class='_aano']")
        for _ in range(10):  # Scroll 10 times
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, "//button/div[text()='Follow']/..")

        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                try:
                    cancel_btn = self.driver.find_element(By.XPATH, "//button[text()='Cancel']")
                    cancel_btn.click()
                except:
                    pass
                time.sleep(1)

# ---- Running the bot ----
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
