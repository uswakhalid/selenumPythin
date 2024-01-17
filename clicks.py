import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_service = ChromeService(executable_path="C:\\Drivers\\Chrome-Driver\\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)
driver.get("https://demoqa.com/buttons")
time.sleep(2)

dynamic_click = driver.find_element(By.CSS_SELECTOR, ".mt-4:nth-child(3)>button")
time.sleep(2)
actions = ActionChains(driver)
actions.click(dynamic_click).perform()

# to verify that the click action is performed
message = driver.find_element(By.ID, "dynamicClickMessage")
expected_message = "You have done a dynamic click"
if message.text == expected_message:
    print(message.text)
else:
    print("Test case failed")

time.sleep(1)
context_button = driver.find_element(By.ID, "rightClickBtn")
time.sleep(2)
actions = ActionChains(driver)
actions.context_click(context_button).perform()

# to verify that the click action is performed
message = driver.find_element(By.ID, "rightClickMessage")
expected_message = "You have done a right click"
if message.text == expected_message:
    print(message.text)
else:
    print("Test case failed")

time.sleep(1)
context_button = driver.find_element(By.ID, "doubleClickBtn")
time.sleep(2)
actions = ActionChains(driver)
actions.double_click(context_button).perform()
# to verify that the click action is performed
message = driver.find_element(By.ID, "doubleClickMessage")
expected_message = "You have done a double click"
if message.text == expected_message:
    print(message.text)
else:
    print("Test case failed")
