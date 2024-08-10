import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie = driver.find_element(By.CSS_SELECTOR, '#cookieAnchor #bigCookie')

while True:
    try:
        driver.find_element(By.CSS_SELECTOR, '#cookieAnchor #bigCookie').click()
    except:
        print("Loading website..")
        time.sleep(3)

