from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service("D:\chromedriver_win32\chromedriver.exe")
chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")

driver.find_elements()
CSS_SELECTOR = "css selector"
event_time = driver.find_elements(CSS_SELECTOR, ".event-widget time")
event_name = driver.find_elements(CSS_SELECTOR, ".event-widget li a")
#Because you are getting a list in event time

events = {}
for n in range(len(event_time)):
    events[n] = {
        "date": event_time[n].text,
        "name": event_name[n].text
    }

print(events)
driver.close() # close only one tab
driver.quit() # close the browser `


"""
Don't forget to check find by elements and find by path and those stuff on lesson 387 
"""