from selenium.webdriver.chrome.options import Options

# './chromedriver' for development(Chromedriver needs to be in main directory)
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless")
CHROME_OPTIONS.add_argument('disable-gpu')
CHROME_OPTIONS.add_argument("no-sandbox")
CHROME_OPTIONS.add_argument(
    'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
