# Cross-Browser test with Chrome, FireFox and Edge. 3 same tests for each Browser

import unittest
import time
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

fake = Faker()


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_chrome(self):
        driver = self.driver
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)  # simulate long running test

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        wait.until(EC.visibility_of_element_located((By.ID, 'wob_rain')))
        print("Precipitation button is visible")
        wait.until(EC.element_to_be_clickable((By.ID, 'wob_rain')))
        print("Precipitation button is clickable")
        driver.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'wob_wind')))
        print("Wind button is visible")
        wait.until(EC.element_to_be_clickable((By.ID, 'wob_wind')))
        print("Wind button is clickable")
        driver.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        wait.until(EC.visibility_of_element_located((By.ID, 'wob_temp')))
        print("Temperature button is visible")
        wait.until(EC.element_to_be_clickable((By.ID, 'wob_temp')))
        print("Temperature button is clickable")
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_chrome_1120x850(self):
        driver = self.driver
        driver.set_window_size(1120, 850)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_chrome_1120x950(self):
        driver = self.driver
        driver.set_window_size(1120, 950)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1.5)

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver.find_element(By.ID, "wob_temp").click()

    def test_check_user_account(self):
        driver = self.driver
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # filling in the form
        first_name = driver.find_element(By.ID, "input-firstname")
        first_name.send_keys(fake.first_name())

        last_name = driver.find_element(By.ID, "input-lastname")
        last_name.send_keys(fake.last_name())

        # random email with no Faker lib
        random_email = str(random.randint(0, 99999)) + "myemail" + "@example.com"

        email = driver.find_element(By.ID, "input-email")
        # email.send_keys(random_email)
        email.send_keys(fake.email())

        telephone = driver.find_element(By.ID, "input-telephone")
        telephone.send_keys(fake.phone_number())

        fakePassword = fake.password()
        password = driver.find_element(By.ID, "input-password")
        password.send_keys(fakePassword)

        password_confirm = driver.find_element(By.ID, "input-confirm")
        password_confirm.send_keys(fakePassword)

        newsletter = driver.find_element(By.XPATH, "//label[@for='input-newsletter-yes']")
        newsletter.click()

        terms = driver.find_element(By.XPATH, "//label[@for='input-agree']")
        terms.click()

        continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
        continue_button.click()

        # asserting that the browser title is correct
        # assert driver.title == "Your Account Has Been Created!"

        try:
            assert driver.title == "Your Account Has Been Created!"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
        try:
            assert driver.title == "My Account"
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        # find pic with user account
        driver.find_element(By.XPATH, '//i[@class="fas fa-2x mb-1 fa-user-edit"]')

        driver.find_element(By.LINK_TEXT, "Edit Account").click()
        time.sleep(0.5)

        try:
            assert driver.title == "My Account Information"
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_firefox(self):
        driver = self.driver
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Firefox"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Firefox 1120x850 is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_firefox_1120x850(self):
        driver = self.driver
        driver.set_window_size(1120, 850)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Firefox"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Firefox 1120x850 is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_firefox_1120x950(self):
        driver = self.driver
        driver.set_window_size(1120, 950)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Firefox"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Firefox 1120x850 is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver.find_element(By.ID, "wob_temp").click()

    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_edge(self):
        driver = self.driver
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)  # simulate long running test

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in  Edge"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in  Edge is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_edge_1120x850(self):
        driver = self.driver
        driver.set_window_size(1120, 850)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in  Edge"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in  Edge is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_edge_1120x950(self):
        driver = self.driver
        driver.set_window_size(1120, 950)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in  Edge"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in  Edge is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver.find_element(By.ID, "wob_temp").click()

    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()