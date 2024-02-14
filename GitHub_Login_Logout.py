from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create a WebDriver instance
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

# Navigate to GitHub login site
driver.get("https://github.com/login")

# Here you have to enter your login and password: put them between quotation marks
your_login = ""
your_password = ""

# Log in to GitHub
driver.find_element(By.ID, "login_field").send_keys(your_login)
driver.find_element(By.ID, "password").send_keys(your_password)
driver.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()

# Log out of GitHub
driver.find_element(By.XPATH, "//*[@aria-label='Open user account menu']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()

# Close browser window
time.sleep(2)
driver.close()
