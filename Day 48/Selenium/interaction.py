from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
artiles = driver.find_element(By.XPATH, "//a[@title='Special:Statistics']")
print(artiles.text)

driver.quit()
