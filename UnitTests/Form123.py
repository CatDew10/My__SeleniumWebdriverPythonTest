# Cross-browser UnitTest framework script for Google and Wikipedia Gold page
# with Waiting and API functional and Webdriver-Manager functionality
# for Chrome, FireFox and Edge browsers
import time
from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import random
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from faker import Faker
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# import HtmlTestRunner
# for Tutorial "How to use Webdriver Manager" go to: https://github.com/SergioUS/webdriver_manager
fake = Faker()


class ChromeInput(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_form(self):
        driver = self.driver
        driver.get("https://form.123formbuilder.com/5012215")

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

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
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            delay()

            driver.find_element(By.XPATH, "//div[@data-role='expander']").click()
            delay()
            driver.find_element(By.XPATH, "//div[contains(@data-day,'30')]").click()
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys(fake.street_address())
            driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys(fake.city())
            driver.find_element(By.XPATH, "//input[@placeholder='Region']").send_keys(fake.country_code())
            driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys(fake.postcode())

            driver.find_element(By.XPATH, "//div[@data-size='fill']").click()
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.XPATH, "//*[@placeholder='Country']").send_keys("Uni")
            driver.find_element(By.XPATH, "//div[@data-index='240'][contains(.,'United States')]").click()
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.ID, "form").click()
            driver.find_element(By.ID, "form").click()
            delay()

            driver.find_element(By.XPATH, "(//label[@role='checkbox'])[1]").click()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            delay()
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def tearDown(self):
        self.driver.quit()


class FirefoxInput(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_form(self):
        driver = self.driver
        driver.get("https://form.123formbuilder.com/5012215")

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

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
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            delay()

            driver.find_element(By.XPATH, "//div[@data-role='expander']").click()
            delay()
            driver.find_element(By.XPATH, "//div[contains(@data-day,'30')]").click()
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys(fake.street_address())
            driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys(fake.city())
            driver.find_element(By.XPATH, "//input[@placeholder='Region']").send_keys(fake.country_code())
            driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys(fake.postcode())

            driver.find_element(By.XPATH, "//div[@data-size='fill']").click()
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.XPATH, "//*[@placeholder='Country']").send_keys("Uni")
            driver.find_element(By.XPATH, "//div[@data-index='240'][contains(.,'United States')]").click()
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.ID, "form").click()
            driver.find_element(By.ID, "form").click()
            delay()

            driver.find_element(By.XPATH, "(//label[@role='checkbox'])[1]").click()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            delay()
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def tearDown(self):
        self.driver.quit()


class EdgeInput(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_form(self):
        driver = self.driver
        driver.get("https://form.123formbuilder.com/5012215")

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

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
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            delay()

            driver.find_element(By.XPATH, "//div[@data-role='expander']").click()
            delay()
            driver.find_element(By.XPATH, "//div[contains(@data-day,'30')]").click()
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys(fake.street_address())
            driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys(fake.city())
            driver.find_element(By.XPATH, "//input[@placeholder='Region']").send_keys(fake.country_code())
            driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys(fake.postcode())

            driver.find_element(By.XPATH, "//div[@data-size='fill']").click()
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.XPATH, "//*[@placeholder='Country']").send_keys("Uni")
            driver.find_element(By.XPATH, "//div[@data-index='240'][contains(.,'United States')]").click()
            delay()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.ID, "form").click()
            driver.find_element(By.ID, "form").click()
            delay()

            driver.find_element(By.XPATH, "(//label[@role='checkbox'])[1]").click()

            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            delay()
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
            driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

            driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     unittest.main()
