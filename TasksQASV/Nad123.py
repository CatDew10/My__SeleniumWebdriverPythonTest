import random
import time
from selenium import webdriver
from faker import Faker
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()

assert "Online Order Form" in driver.title
print(driver.title)

driver.find_element(By.XPATH, "//h1[contains(text(),'Order Form')]")

f = Faker()

# filling in the form
driver.find_element(By.XPATH, "//input[@placeholder='First']").click()
driver.find_element(By.XPATH, "//input[@placeholder='First']").send_keys(f.first_name())

driver.find_element(By.XPATH, "//input[@placeholder='Last']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Last']").send_keys(f.last_name())

driver.find_element(By.XPATH, "//input[@type='email']").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys(f.email())

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("1233654798")

driver.find_element(By.XPATH, "//span[contains(text(),'# Product 1')]").click()

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

time.sleep(2)

random_number = random.randint(1, 10)
driver.find_element(By.XPATH, "//input[@type='number']").click()
driver.find_element(By.XPATH, "//input[@type='number']").send_keys(random_number)

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
time.sleep(2)

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

time.sleep(3)

driver.find_element(By.XPATH, "//div[@role='application']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//div[@data-month='10'])[30]").click()
time.sleep(3)


driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
time.sleep(3)

driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys("Holly Lane")

driver.find_element(By.XPATH, "//input[@placeholder='City']").click()
driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys("Chicago")

driver.find_element(By.XPATH,  "//input[@placeholder='Region']").click()
driver.find_element(By.XPATH,  "//input[@placeholder='Region']").send_keys("IL")

driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys("60006")

driver.find_element(By.XPATH, "//div[@data-size='fill']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@placeholder='Country']").send_keys("uni")
driver.find_element(By.XPATH, "//div[@data-index='240'][contains(.,'United States')]").click()

time.sleep(1)
driver.find_element(By.ID, "form").click()
driver.find_element(By.ID, "form").click()
time.sleep(1)

driver.find_element(By.XPATH, "(//label[@role='checkbox'])[1]").click()
driver.find_element(By.XPATH, "(//label[@role='checkbox'])[2]").click()

time.sleep(1)

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)

driver.quit()