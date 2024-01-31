#projekt: zdalna obsługa gry 2048 z poziomu Pythona
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def accept_cookies(browser):
    try:
        accept_button = browser.find_element(By.XPATH, '//button[contains(text(), "Zgadzam się")]')
        accept_button.click()
    except:
        pass


browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

accept_cookies(browser)

time.sleep(2)

for x in range(2):
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)
    time.sleep(1)
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_RIGHT)
    time.sleep(1)
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_LEFT)
    time.sleep(1)
    


