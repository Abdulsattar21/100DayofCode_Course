from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service("D:\chromedriver_win32\chromedriver.exe") 
chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

CSS_SELECTOR = "css selector"
CLASS_NAME = "class name"
number = driver.find_element("id", "articlecount")
link = driver.find_element("link text", "English")

search = driver.find_element("name", "search")
print("1")
search.send_keys("Python")
search.send_keys(Keys.ENTER)






print("DONE")


# driver.close() # close only one tab
# driver.quit() # close the browser `

