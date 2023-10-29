import random
import time
from selenium import webdriver
from faker import Faker
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

fake = Faker()


driver = webdriver.Chrome()
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
driver.find_element(By.XPATH,"//input[@type='email']").send_keys(fake.email())
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
driver.find_element(By.XPATH, "//div[contains(@data-day,'30')]").click()
driver.implicitly_wait(5)

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)


driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys(fake.street_address())
driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys(fake.city())
driver.find_element(By.XPATH,  "//input[@placeholder='Region']").send_keys(fake.country_code())
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

driver.quit()




