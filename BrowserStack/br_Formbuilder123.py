# coding=utf8
from dotenv import load_dotenv
import os
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from threading import Thread
from selenium.common.exceptions import WebDriverException
from faker import Faker
from selenium.webdriver import Keys
import random
import time
from BrowserStack import my_key

fake = Faker()

# load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or my_key.BROWSERSTACK_USERNAME
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or my_key.BROWSERSTACK_ACCESS_KEY
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
    try:
        # test1 Chrome

        driver.get("https://form.123formbuilder.com/5012215")
        driver.maximize_window()

        # wait max 5 sec for page loading, then show "Load Error"
        # implicitly_wait() is using for all other browsers
        driver.implicitly_wait(5)

        # this method is depreciated in Selenium4

        assert "Online Order Form" in driver.title
        print("Page Title is: ", driver.title)

        # Not common use
        if "Online Order Form" not in driver.title:
            raise Exception("Title is wrong!")

        # wait max 5 sec for page loading, then show "Load Error"
        # set_page_load_timeout() is using for Chrome and FireFox mostly
        driver.find_element(By.XPATH, "//input[@placeholder='First']").send_keys(fake.first_name())
        driver.find_element(By.XPATH, "//input[@placeholder='Last']").send_keys(fake.last_name())
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(fake.email())
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").click()
        driver.find_element(By.XPATH, "(//input[contains(@type,'text')])[3]").send_keys(fake.phone_number())
        driver.find_element(By.XPATH, "(//label[@role='radio'])[4]").click()

        random_number = random.randint(1, 40)
        driver.find_element(By.XPATH, "//input[@type='number']").send_keys(random_number)
        driver.implicitly_wait(5)

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

        time.sleep(3)

        driver.find_element(By.XPATH, "//div[@data-role='expander']").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//div[contains(@data-day,'27')]").click()
        driver.implicitly_wait(5)

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

        driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys(fake.street_address())
        driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys(fake.city())
        driver.find_element(By.XPATH, "//input[@placeholder='Region']").send_keys(fake.country_code())
        driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys(fake.postcode())

        driver.find_element(By.XPATH, "//div[@data-size='fill']").click()
        time.sleep(1)

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

        driver.find_element(By.XPATH, "//*[@placeholder='Country']").send_keys("Uni")
        driver.find_element(By.XPATH, "//div[@data-index='240'][contains(.,'United States')]").click()
        time.sleep(1)

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

        driver.find_element(By.ID, "form").click()
        driver.find_element(By.ID, "form").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "(//label[@role='checkbox'])[1]").click()

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        time.sleep(1)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()


    except WebDriverException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')
    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')
    # Stop the driver
    driver.quit()


for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()
