import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
driver.find_element(By.LINK_TEXT,"Mobiles").click()
time.sleep(3)
driver.find_element(By.XPATH,'//button[@class="_2KpZ6l_2doB4z"]').click()
driver.find_element(By.LINK_TEXT,"Flights").click()
driver.quit()