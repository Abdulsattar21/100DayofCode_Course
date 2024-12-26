from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service("D:\chromedriver_win32\chromedriver.exe")
chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(service=service)

driver.get("https://secure-retreat-92358.herokuapp.com/")

CSS_SELECTOR = "css selector"
CLASS_NAME = "class name"

first_name = driver.find_element("name", "fName")
last_name = driver.find_element("name", "lName")
email = driver.find_element("name", "email")
btn = driver.find_element(By.XPATH, "/html/body/form/button")

first_name.send_keys("Mahmoud")
last_name.send_keys("Ali")
email.send_keys("email@email.com")
btn.click()







print("DONE")


# driver.close() # close only one tab
# driver.quit() # close the browser `

