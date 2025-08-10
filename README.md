# AUTOMATION-INSTAGRAM-BOT-FOLLOWER
AUTOMATION INSTAGRAM BOT — Follower

Automated Instagram follower bot using Selenium (educational purposes only).

🔎 Project Overview

This script automates the process of logging into Instagram, visiting a target account's followers list, and following users automatically. It's implemented in Python using Selenium and is intended for learning browser automation and scripting. Use at your own risk. Read Instagram's Terms of Service before running any automation.

⚠️ Important Warning

Automating actions on Instagram can violate their Terms of Service and may lead to account restriction or permanent ban. Use a throwaway/test account and conservative action rates. The author is not responsible for any account consequences.

Features

Log in to Instagram with provided credentials

Open a target account's followers list

Scroll and iterate through followers

Follow users with basic safety delays and randomization (to reduce rate detection)

Configurable limits and delays

Prerequisites

Python 3.8+ installed

Google Chrome browser (compatible with chosen ChromeDriver)

ChromeDriver executable matching your Chrome version

Python packages:

pip install selenium
pip install webdriver-manager        # optional but convenient

Setup

Clone or download this repository to your local machine.

Install required Python packages:

pip install -r requirements.txt

If you don't have a requirements.txt, run: pip install selenium webdriver-manager

Download ChromeDriver that matches your Chrome version and put it in a known path.

Edit the main script and set configuration variables (example names shown below):

SIMILAR_ACCOUNT = "target_account_here"   # account whose followers you want to follow
EMAIL = "your_instagram_username_or_email"
PASSWORD = "your_instagram_password"
CHROME_DRIVER_PATH = r"C:\path\to\chromedriver.exe"  # or use webdriver-manager
MAX_FOLLOWS_PER_RUN = 50
DELAY_MIN = 3   # seconds
DELAY_MAX = 8   # seconds
SCROLL_PAUSE = 2

Usage

Run the script from the command line:

python instagram_follower_bot.py

Typical flow:

Script opens Chrome and navigates to instagram.com.

Logs in using provided credentials.

Navigates to the specified SIMILAR_ACCOUNT followers list.

Scrolls the modal to load followers, then iterates through visible profiles and clicks follow.

Stops after reaching MAX_FOLLOWS_PER_RUN or end of the list.

Example (core logic outline)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random

# config variables here

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get('https://www.instagram.com/accounts/login/')
# login flow: find username/password inputs, sign in
# navigate to target profile
# open followers modal
# while follows_done < MAX_FOLLOWS_PER_RUN:
#   find follow buttons in modal
#   for button in buttons:
#       if button.text.lower() == 'follow':
#           button.click()
#           follows_done += 1
#           time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
#   scroll modal to load more

This README intentionally keeps the code high-level. See the repository file instagram_follower_bot.py for the full implementation.

Configuration suggestions (safety-first)

Use small MAX_FOLLOWS_PER_RUN (e.g., 10–30) for new accounts.

Use randomized delays between actions (3–10 seconds) and occasional longer pauses.

Avoid running the bot continuously — run it manually and monitor results.

Consider adding proxy or multiple accounts only if you understand the risks.

Troubleshooting

selenium.common.exceptions.NoSuchElementException: Page structure changed — Instagram updates frequently; update selector paths.

SessionNotCreatedException: ChromeDriver version mismatch — download the correct ChromeDriver for your Chrome version.

Login fails: Instagram often shows challenge pages (captcha, 2FA, suspicious login). You may need to handle 2FA or manual verification steps.

Ethical & Legal Notes

Do not use automation to harass, scrape private data, or violate privacy laws.

This project is meant for educational purposes and research on automation only.

Contribution

Contributions, bug reports, and pull requests are welcome. If you add features (e.g., unfollow, like/comment throttling, headless mode, proxies), please document configuration and safety considerations.

License

This project is released under the MIT License — see LICENSE for details.

Acknowledgements

Built using Selenium; inspired by multiple community projects that experiment with social media automation. Always credit original authors if you adapt code.

