import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.yatra.com/")
driver.find_element(By.LINK_TEXT,'My Account').click()
driver.find_element(By.LINK_TEXT,"Login").click()
time.sleep(3)
contdemo=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
contdemo.screenshot(".\\test.png")
contdemo.click()
time.sleep(3)
driver.get_screenshot_as_file("c:\\my vscode\\error.jpg")
driver.save_screenshot("\\test1.png")
driver.quit()

wrong