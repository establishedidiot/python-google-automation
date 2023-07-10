from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('https://www.google.com')


search_input=browser.find_element(By.XPATH,"//textarea")
search_input.send_keys('hello world')
time.sleep(2)

search_btn=browser.find_element(By.XPATH,"//input[@value='Google Search']")
search_btn.click()
time.sleep(2)
