import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import AllureReports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test" keyword

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
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='qqq']")))
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
        time.sleep(1)

        search = driver.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "WOW!" in driver.title
        print("Page title in Chrome is:", driver.title)

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
    unittest.main(AllureReports)
