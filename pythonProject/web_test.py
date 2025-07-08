from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()  # Or any other browser driver
website_url = 'https://practicetestautomation.com/practice-test-login/'
driver.get(website_url)

user_ip = driver.find_element(By.ID, "username")
pass_ip = driver.find_element(By.ID, 'password')
# Enter text into the field
user_ip.send_keys("student")
pass_ip.send_keys("Password123")
# You can also simulate pressing keyboard keys
# user_ip.send_keys(Keys.ENTER)
# pass_ip.send_keys(Keys.ENTER)

# Example using ID
button = driver.find_element(By.ID, "submit")
button.click()
time.sleep(5)
# print(driver.window_handlesen)
# driver.switch_to.window(driver.window_handles[1])


print(driver.current_url)

# Wait for the response element to appear
# response_element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "submit"))
# )
# # Extract the response data
# response_text = response_element.text
#
# # Print the response
# print("Response:", response_text)