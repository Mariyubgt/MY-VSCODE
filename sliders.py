import time
from selenium import webdriver
from selenium.webdriver import ActionChains 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.snapdeal.com/products/mobiles-accessories?sort=plrty")
driver.maximize_window()
ele1=driver.find_element(By.XPATH,'//a[contains(@class,"left-handle")]')
ele2=driver.find_element(By.XPATH,'//a[contains(@class,"right-handle")]')
ActionChains(driver).drag_and_drop_by_offset(ele1, 60, 0).perform()
time.sleep(2)
ActionChains(driver).drag_and_drop_by_offset(ele2, -80, 0).perform()
time.sleep(2)