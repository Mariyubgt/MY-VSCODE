import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://demo.seleniumeasy.com/basic-radiobutton-demo.html")
driver.find_element(By.XPATH,"//input[@type='radio']").click()
print(driver.find_element(By.XPATH,"//input[@type='radio']").is_selected())
driver.find_element(By.NAME,"gender").click()
print(driver.find_element(By.NAME,"gender").is_selected())
time.sleep(4)
driver.quit()