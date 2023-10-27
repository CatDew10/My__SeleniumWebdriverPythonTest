from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# URL collection
url_google = "https://www.google.com/"
url_yahoo = "https://www.yahoo.com/"
url_tesla = "https://www.tesla.com/"
driver.get(url_google)
driver.maximize_window()

# URL verification
assert driver.current_url == url_google
current_url = driver.current_url
if current_url == url_google:
    print("Current URL is OK: ", driver.current_url)
else:
    print("Current URL is different than Expected URL", driver.current_url)

# Titles collection
pageGoogle_ExpectedTitle = "Google"
pageYahoo_ExpectedTitle = "Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos"
pageTesla_ExpectedTitle = "Electric Cars, Solar & Clean Energy | Tesla"
current_title = driver.title

# Title verification
if current_title == pageGoogle_ExpectedTitle:
    print("Current Title is OK: ", driver.title)
else:
    print("Current Title is different than Expected Title. Current Title is: ", driver.title)

# LOGOs collection
# GoogleIcon = driver.find_element(By.XPATH, '//*[@alt="Google"]')
# GoogleIconNY = driver.find_element(By.XPATH, "//img[@id='hplogo']")
# GoogleIconLaborDay = driver.find_element(By.XPATH, "//img[@alt='Labor Day 2022']")
if current_url == url_google:
    GoogleIcon = driver.find_element(By.XPATH, '//img[@alt="Google"]')
    # GoogleIconLaborDay = driver.find_element(By.XPATH, "//img[@alt='Labor Day 2022']")
elif current_url == url_yahoo:
    YahooIcon = driver.find_element(By.XPATH, "//img[@src='https://s.yimg.com/rz/p/yahoo_homepage_en"
                                              "-US_s_f_p_bestfit_homepage.png']")
elif current_url == url_tesla:
    TeslaIcon = driver.find_element(By.XPATH, '//a[@aria-label="Tesla Logo"]')
else:
    print("Current URL is out of scope", driver.current_url)

# Page LOGO verification
# if GoogleIconNY:
if GoogleIcon:
    print("Google Logo is OK", driver.get_screenshot_as_file("current_page.png"))
else:
    print("NO Google Logo", driver.get_screenshot_as_file("wrong_current_page.png"))

driver.quit()