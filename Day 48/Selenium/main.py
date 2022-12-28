from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\DRIVERS\chromedriver_win32\chromedriver.exe"
service_obj = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service_obj)
URL = "https://www.python.org/"
driver.get(URL)

# ----------------------*******************************-----------------------------------

# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)
# price1 = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
# print(price1.text)
events_dict = {}

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget time ")
names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a ")
for n in range(len(events)):
    events_dict[n] = {
        "time": events[n].text,
        "name": names[n].text,
    }

print(events_dict)

# driver.close()  # closes active tab
driver.quit()  # closes entire browser


