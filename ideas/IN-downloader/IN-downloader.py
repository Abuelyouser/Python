import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


user="i.selem@absega.com"
password="Ericsoon_5"
login_link = "https://my.ine.com/login"

# initialize the Chrome driver
options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(
   "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
# navigate to the website
print("Opening INE ...")
driver.get(login_link)
wait = WebDriverWait(driver, 20)
search_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
search_input.send_keys(user)
search_input1 = driver.find_element('xpath', "//input[@placeholder='Password']")
search_input1.send_keys(password)
search_btn = driver.find_element('xpath', "//div[@class='ine-form__submit-btn-wrapper auth-form__actions-submit-wrapper auth-form__actions-submit-wrapper--login']")
time.sleep(50)
search_btn.click()
time.sleep(50)
print("Logged in!")




