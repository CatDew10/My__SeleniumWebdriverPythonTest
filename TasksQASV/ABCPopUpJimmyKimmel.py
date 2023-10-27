from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE


driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()

# wait 2 sec, then proceed with script
time.sleep(2)

# find "Google Search" field and type "abc" there
driver.find_element(By.NAME, "q").send_keys("abc")
time.sleep(1)
# click on "Google Search" button
driver.find_element(By.NAME, "btnK").click()

# Find and click on the ABC link
driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Network - ABC.com").click()
time.sleep(2)
assert "ABC Network - ABC.com" in driver.title
print("ABC Page Title is: ", driver.title)

# this is is NOT common practice, but you could use it
if "ABC Network - ABC.com" not in driver.title:
    raise Exception("Title for ABC page is wrong!")

# wait max 5 sec for page loading, then show "Load Error"
# set_page_load_timeout() is using for Chrome and FireFox mostly
driver.set_page_load_timeout(5)
# close Pop Up message
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.ESCAPE)
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Browse").click()
time.sleep(2)

# Check Minimize and Maximize window functionality
driver.minimize_window()
time.sleep(1)
driver.maximize_window()
time.sleep(2)

# Check is Menu element ("Comedy" button) is visible and click on it
driver.find_element(By.XPATH, "//button[contains(text(),'Comedy')]").is_displayed()
driver.find_element(By.XPATH, "//button[contains(text(),'Comedy')]").click()

try:
    driver.find_element(By.XPATH, "//span[contains(text(),'Jimmy Kimmel Live!')]").click()
    print("'Jimmy Kimmel Live!' text is visible")
except WDE:
    driver.find_element(By.XPATH, '//img[@alt="Jimmy Kimmel Live!"]').click()
    print("'Jimmy Kimmel Live!' text is Hidden")
finally:
    print("Exception worked OK")

time.sleep(1)

# Check webpage current Title and compare it with string below
assert "Watch Jimmy Kimmel Live! TV Show - ABC.com" in driver.title

# Verify (find) Main Logo on the Jimmy page
driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]')

# Print attributes "title" and "src" for the Main Logo on the Jimmy page
print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))
print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("src"))

# Find element value, then store this value to variable "JimmyPageLogo"
jimmyPageLogo = driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]').get_attribute("title")

# Assert (compare) stored element value with required value
assert jimmyPageLogo == "Jimmy Kimmel Live!"
assert jimmyPageLogo in driver.page_source

# Create variable for Jimmy webpage URL
jimmyShowURL = "https://abc.com/shows/jimmy-kimmel-live"

# Check if URL for Jimmy webpage URL is the same in the browser during a Test
assert jimmyShowURL == driver.current_url
if jimmyShowURL != driver.current_url:
    print("Current Jimmy Kimmel Show URL is different and it is: ", driver.current_url)
else:
    print("Current Jimmy Show URL is OK: ", driver.current_url)

# Same element verification for "Jimmy Page Logo"
if jimmyPageLogo:
    print("Jimmy Kimmel Show Page Logo is OK")
else:
    print("NO Jimmy Kimmel Show Page Logo")

# view Show Schedule
driver.find_element(By.XPATH, "//span[contains(text(),'VIEW SCHEDULE')]").click()
time.sleep(1)

# Create variable for Jimmy webpage current Title
jimmyShowScheduleTitle = "Jimmy Kimmel Live Schedule for the Week"

# Check if Title for Jimmy webpage URL is the same in the browser during a Test
assert jimmyShowScheduleTitle in driver.title
if jimmyShowScheduleTitle:
    print("Jimmy Kimmel Show Schedule is available")
else:
    print("Jimmy Kimmel Show Schedule is unavailable")
time.sleep(0.5)

# Go back to the previous Page
driver.back()

# quit from browser
driver.quit()