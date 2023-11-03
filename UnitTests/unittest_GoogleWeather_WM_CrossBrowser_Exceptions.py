# Cross-Browser test with Chrome, FireFox and Edge. 3 same tests for each Browser
# With delay() function, try-except, and WebDriver Manager

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import random
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service


# import HtmlTestRunner
# for Tutorial "How to use Webdriver Manager" go to: https://github.com/SergioUS/webdriver_manager

# driver sleep from 2 to 3 seconds
def delay():
    time.sleep(random.randint(1, 5))


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_chrome(self):
        driver = self.driver
        driver.get('http://www.google.com')

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        delay()  # simulate long running test

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        delay()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Check Weather frame functionality with "try-except"
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
            print("Weather widget is visible")
        except TimeoutException:
            print("Weather widget loading took more than 2 sec")

        # Check Weather frame functionality with NO "try-except"
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
        delay()

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        delay()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Check Weather frame functionality with "try-except" and TimeoutException
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
            driver.find_element(By.ID, "wob_rain").click()
            delay()
            driver.find_element(By.ID, "wob_wind").click()
            delay()
            driver.find_element(By.ID, "wob_temp").click()
        except TimeoutException:
            print("Weather widget loading took more than 5 sec")

    def test_search_weather_chrome_1120x950(self):
        driver = self.driver
        driver.set_window_size(1120, 950)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        delay()

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        delay()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Check Weather frame functionality with "try-except" and NoSuchElementException
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        except NoSuchElementException:
            print("Weather widget in invisible")
            driver.find_element(By.ID, "wob_rain").click()
            delay()
            driver.find_element(By.ID, "wob_wind").click()
            delay()
            driver.find_element(By.ID, "wob_temp").click()

    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_firefox(self):
        driver = self.driver
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        delay()

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        delay()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome 1120x850 is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        delay()
        driver.find_element(By.ID, "wob_wind").click()
        delay()
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_firefox_1120x850(self):
        driver = self.driver
        driver.set_window_size(1120, 850)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        delay()

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        delay()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome 1120x850 is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        delay()
        driver.find_element(By.ID, "wob_wind").click()
        delay()
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_firefox_1120x950(self):
        driver = self.driver
        driver.set_window_size(1120, 950)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        delay()

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        delay()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome 1120x850 is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        delay()
        driver.find_element(By.ID, "wob_wind").click()
        delay()
        driver.find_element(By.ID, "wob_temp").click()

    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_chrome(self):
        driver = self.driver
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        delay()  # simulate long running test

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        delay()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        delay()
        driver.find_element(By.ID, "wob_wind").click()
        delay()
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_chrome_1120x850(self):
        driver = self.driver
        driver.set_window_size(1120, 850)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        delay()

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        delay()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        delay()
        driver.find_element(By.ID, "wob_wind").click()
        delay()
        driver.find_element(By.ID, "wob_temp").click()

    def test_search_weather_chrome_1120x950(self):
        driver = self.driver
        driver.set_window_size(1120, 950)
        driver.get('http://www.google.com')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        delay()

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        delay()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element(By.ID, "wob_rain").click()
        delay()
        driver.find_element(By.ID, "wob_wind").click()
        delay()
        driver.find_element(By.ID, "wob_temp").click()

    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()