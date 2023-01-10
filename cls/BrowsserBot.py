import os
import pickle
import time
from selenium import webdriver


from config import CHROMEDRIVER_PATH, CHROME_OPTIONS


class Browser:
    def __init__(self):
        self.bot = webdriver.Chrome(CHROMEDRIVER_PATH, options=CHROME_OPTIONS)

    def close(self):
        """
        Close browser after finishing ANY interaction with browser.
        """
        self.bot.close()


class Bot(Browser):
    def __init__(self):
        super().__init__()

    def google_test(self):
        # Check if "no-gpu" browser is OK
        self.bot.get("https://www.google.com")
        print(f'"{self.bot.title}" test passed.\n')

    def save_cookies(self):
        cookie = self.bot.get_cookies()
        pickle.dump(cookie, open(f"cookies", "wb"))
        print('\n[INFO] Cookies saved!\n')

    def check_cookies(self):

        self.bot.get("https://bets4.org/")
        time.sleep(0.5)
        self.bot.delete_all_cookies()

        self._load_cookies()
        # Here you can paste any checking cookies condition.
        # It may be:
        #           - UserName
        #           - Balance
        #           - Any other condition

    def _load_cookies(self):
        try:
            for cookie in pickle.load(open(f"cookies", "rb")):
                self.bot.add_cookie(cookie)

        except FileNotFoundError:
            print("There is no any cookies in main directory")
        except Exception as ex:
            print(ex)
        finally:
            time.sleep(0.5)
            self.bot.refresh()
