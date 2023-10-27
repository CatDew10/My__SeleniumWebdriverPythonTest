# Google Chrome Video script with Action Chains

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://htmltestpage.w3spaces.com/testpage.html")
driver.maximize_window()

# Verify you on correct page
try:
    assert "HTML5 Test Page" in driver.title
except WDE:
    print("Title is different", driver.title)

driver.find_element(By.XPATH, "//h1[contains(text(),'HTML5 Test Page')]")

# Find 'Text' inner link and click on it
driver.find_element(By.XPATH, '//a[@href="#text"]').click()
time.sleep(1)

# Find 'Top' inner link before 'Paragraphs' and click on it
driver.find_element(By.XPATH, '//*[@id="text__headings"]//*[@href="#top"]').click()
time.sleep(1)

# Find 'Video' link and click on it
driver.find_element(By.XPATH, "//a[contains(text(),'Video')]").click()
time.sleep(1)

# identifying the source element
naMarsVideo = driver.find_element(By.XPATH, '//*[@src="https://www.youtube.com/embed/4bncs8ReBzU"]')
naMarsVideo.click()
# action chain object creation
action = ActionChains(driver)

# double click operation and perform
action.double_click(naMarsVideo).perform()

time.sleep(50)

action.double_click(naMarsVideo).perform()
time.sleep(2)

print("End of test")

driver.quit()