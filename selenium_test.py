from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

input = driver.find_element(by=By.CSS_SELECTOR, value='#kw')
input.send_keys("苍老师照片")

time.sleep(3)

button = driver.find_element(by=By.CSS_SELECTOR, value='#su')
button.click()

time.sleep(30)