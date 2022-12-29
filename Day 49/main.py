from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

ser_obj = Service("C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3376998095&f_LF=f_AL&geoId=102257491&keywords=junior%20python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")
driver.maximize_window()

signin = driver.find_element(By.LINK_TEXT, "Sign in")
signin.click()

email = driver.find_element(By.ID, "username")
email.send_keys("abc@gmail.com")

pswrd = driver.find_element(By.ID, "password")
pswrd.send_keys("abc@")
pswrd.send_keys(Keys.ENTER)
time.sleep(5)
apply = driver.find_element(By.XPATH, "//button[@id='ember327']//span[@class='artdeco-button__text'][normalize-space()='Easy Apply']")
apply.click()

cou_code = Select(driver.find_element(By.XPATH, "//select[@id='text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3376998095-75943669-phoneNumber-country']"))
cou_code.select_by_visible_text("India (+91)")

num = driver.find_element(By.XPATH, "//input[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3376998095-75943669-phoneNumber-nationalNumber']")
num.send_keys("33")

next = driver.find_element(By.XPATH, "//button[@id='ember343']//span[@class='artdeco-button__text'][normalize-space()='Next']").click()

choose = driver.find_element(By.XPATH, "//span[normalize-space()='Choose']").click()
driver.find_element(By.XPATH, "//button[@id='ember343']//span[@class='artdeco-button__text'][normalize-space()='Next']").click()
