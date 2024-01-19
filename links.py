import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



chrome_service = ChromeService(executable_path="C:\\Drivers\\Chrome-Driver\\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)
driver.get("https://demoqa.com/links")
time.sleep(2)

first_URL = driver.find_element(By.ID, "simpleLink")
first_URL.send_keys(Keys.CONTROL + Keys.RETURN)
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)

driver.switch_to.window(driver.window_handles[0])
second_URL = driver.find_element(By.ID, "dynamicLink")
second_URL.send_keys(Keys.CONTROL + Keys.RETURN)
time.sleep(2)

driver.switch_to.window(driver.window_handles[2])
time.sleep(2)
driver.close()

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.close()
driver.quit()


