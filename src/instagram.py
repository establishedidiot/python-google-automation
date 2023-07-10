from selenium import webdriver
from config import USERNAME,PASSWORD
from selenium.webdriver.common.by import By
import time

users=['mainpuneet']

browser = webdriver.Chrome()
browser.get("https://www.instagram.com")

time.sleep(2)
username_field=browser.find_element(By.XPATH,"//input[@name='username']")
username_field.send_keys(USERNAME)

password_field=browser.find_element(By.XPATH,"//input[@name='password']")
password_field.send_keys(PASSWORD)
time.sleep(2)

login_button=browser.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()
time.sleep(2)

for user in users :
    browser.get(f"https://www.instagram.com/{user}/")
    time.sleep(2)
    posts,followers,following=browser.find_elements(By.XPATH,"//span[contains(@class,'_ac2a')]")
    print(posts.text,followers.text,following.text)

    with open(f"{user}.txt",'w') as file:
        file.write(f"Number of Posts:{posts.text}\n")
