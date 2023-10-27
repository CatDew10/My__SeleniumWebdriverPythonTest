from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

fake = Faker()
website_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"
driver = webdriver.Chrome()
driver.get(website_url)
driver.maximize_window()

# generated brand new Browser session
driver.delete_all_cookies()

# Check "Account registration" page Title
acct_reg_expected_title = "Register Account"
acct_reg_actual_title = driver.title
if acct_reg_expected_title == acct_reg_actual_title:
    print('"Account registration" page Title is correct:', driver.title)
else:
    print('"Account registration" page Title is wrong:', driver.title)


# Check "Account registration" page URL
acct_reg_expected_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"
acct_reg_actual_url = driver.current_url
if acct_reg_expected_url == acct_reg_actual_url:
    print('"Account registration" page URL is correct:', driver.current_url)
else:
    print('"Account registration" page URL is wrong:', driver.current_url)


mainPageTitle = "Register Account"
assert driver.title == mainPageTitle

WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Register Account')]")))

# filling in the form
# first_name
driver.find_element(By.ID, "input-firstname").send_keys(fake.first_name())

# last_name
driver.find_element(By.ID, "input-lastname").send_keys(fake.last_name())

# random email with no Faker lib
# random_email = str(random.randint(0, 99999)) + "myemail" + "@example.com"
# email.send_keys(random_email)

# random email with Faker lib
driver.find_element(By.ID, "input-email").send_keys(fake.email())

# telephone
driver.find_element(By.ID, "input-telephone").send_keys(fake.phone_number())

# password
fakePassword = fake.password()
driver.find_element(By.ID, "input-password").send_keys(fakePassword)

# password_confirm
driver.find_element(By.ID, "input-confirm").send_keys(fakePassword)

# newsletter
driver.find_element(By.XPATH, "//label[@for='input-newsletter-yes']").click()

# terms
driver.find_element(By.XPATH, "//label[@for='input-agree']").click()

# continue_button
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# asserting that the browser title is correct with No Exception
# assert driver.title == "Your Account Has Been Created!"

# asserting that the browser title is correct with Exception
try:
    assert driver.title == "Your Account Has Been Created!"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

# get Text from Paragraph and store it in variable
text_congrats_website = driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations! Your new')]").text
text_congrats_expected = "Congratulations! Your new account has been successfully created!"

# Compare expected and actual Paragraph text
try:
    assert text_congrats_website == text_congrats_expected
    print("Paragraph text is correct. Current text is:", text_congrats_website)
except AssertionError:
    print("Paragraph text is different. Current text is:", text_congrats_website)

# click button "Continue" with Exception
driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
try:
    assert driver.title == "My Account"
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

# click "Edit Account" button
driver.find_element(By.LINK_TEXT, "Edit Account").click()
time.sleep(0.5)

try:
    assert driver.title == "My Account Information"
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

# closing the browser
driver.quit()