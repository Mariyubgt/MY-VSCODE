import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.ID,"login-button").click()
time.sleep(5)
driver.find_element(By.XPATH,'//button[@class="btn btn_primary btn_small btn_inventory "]').click()
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
time.sleep(5)
driver.find_element(By.XPATH,'//button[@class="btn btn_action btn_medium checkout_button "]').click()
driver.find_element(By.XPATH,'//input[@id="first-name"]').send_keys("marita")
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="last-name"]').send_keys("dsouza")
time.sleep(3)
driver.find_element(By.XPATH,'//input[@id="postal-code"]').send_keys("567123")
time.sleep(5)
driver.find_element(By.XPATH,'//input[@type="submit"]').click()
time.sleep(3)
driver.quit()