from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

class User:
    def __init__(self, is_authenticated):
        self.is_authenticated = is_authenticated

@pytest.fixture()
def test_browser():
    global driver
    # Create a WebDriver instance
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    # Navigate to GitHub login site
    driver.get("https://github.com/login")

# Log in to GitHub
def test_login(test_browser):
    # Here you have to enter your login and password: put them between quotation marks
    global user
    user = ""
    password = ""
    driver.find_element(By.ID, "login_field").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()
    user = User(is_authenticated=True)
    assert user.is_authenticated == True, 'You are not looged in'

# Log out of GitHub and close browser window
def test_logout():
    driver.find_element(By.XPATH, "//*[@aria-label='Open user account menu']").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
    user = User(is_authenticated=False)
    assert user.is_authenticated == False, "You are still logged in"
    time.sleep(2)
    driver.close()
