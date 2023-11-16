# Parallel Cross-Browser test
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
from selenium.webdriver.support.wait import WebDriverWait
from BrowserStack import my_key

caps = [{
    'os_version': '11',
    'os': 'Windows',
    'browser': 'chrome',
    'browser_version': 'latest',
    'name': 'Parallel Test1_Win11_Chrome',  # test name
    'build': 'Parallel Cross-Browser test'  # Your tests will be organized within this build
},
    {
        'os_version': '10',
        'os': 'Windows',
        'browser': 'chrome',
        'browser_version': 'latest',
        'name': 'Parallel Test2_Win10_Chrome',  # test name
        'build': 'Parallel Cross-Browser test'
    },
    {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'chrome',
        'browser_version': 'latest',
        'name': 'Parallel Test3_OSX_Chrome',  # test name
        'build': 'Parallel Cross-Browser test'
    },
    {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'Firefox',
        'browser_version': 'latest',
        'name': 'Parallel Test4_OSX_Firefox',  # test name
        'build': 'Parallel Cross-Browser test'
    }]


def run_session(desired_cap):
    driver = webdriver.Remote(
        command_executor=my_key.key,  # you need to use your own key here
        desired_capabilities=desired_cap)

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
    try:
        assert "No results found." not in driver.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)
    except AssertionError:
        print("Check Title")

    # Check Weather frame functionality
    try:
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
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All actions is OK!"}}')
    except TimeoutException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Not all actions is OK!"}}')

    driver.quit()


# The Thread function takes run_session function and each set of capability from the caps array as an argument to run
# each session in parallel
for cap in caps:
    Thread(target=run_session, args=(cap,)).start()