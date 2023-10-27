import random
import time
from selenium import webdriver
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

fake = Faker()

driver = webdriver.Chrome()
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
random_email = str(random.randint(0, 99999)) + "myemail@example.com"

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
try:
    driver.find_element(By.XPATH, '//i[@class="fas fa-2x mb-1 fa-user-edit"]')
    driver.find_element(By.XPATH, "//i[contains(@class,'fas fa-2x mb-1 fa-key')]")
except NoSuchElementException:
    print("Some icons is missing")


driver.find_element(By.LINK_TEXT, "Edit Account").click()
time.sleep(0.5)



try:
    assert driver.title == "My Account Information"
except AssertionError:
    print("Title is different. Current Title is:", driver.title)


# closing the browser
driver.quit()