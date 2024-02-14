from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Create a WebDriver instance
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

# Navigate to Google site
driver.get("https://google.pl")

# Find button to deny cookies and click it
driver.find_element(By.ID,"W0wltc").click()

# Locate search field and enter a search query - "Kraków"
search_field = driver.find_element(By.CSS_SELECTOR, "textarea")
search_field.send_keys("Kraków")
search_field.send_keys(Keys.ENTER)

# Wait for the search results page to load
wait = WebDriverWait(driver, 10, 0.5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Kraków – Wikipedia, wolna encyklopedia')]")))

# Locate the link with the text "Kraków – Wikipedia, wolna encyklopedia" in the search results
driver.find_element(By.XPATH, "//h3[contains(text(),'Kraków – Wikipedia, wolna encyklopedia')]").click()

# Print some information about Kraków
print("\nThere is some information about Kraków:\n")
print(driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[1]").text)

# Close browser window
driver.close()
