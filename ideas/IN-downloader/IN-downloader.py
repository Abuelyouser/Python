import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



password=""
login_link = ""

course_link = input('Enter the course link: ')
course_name = course_link.split('/')[-1]

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
time.sleep(10)
search_btn.click()
time.sleep(40)
print("Logged in!")
driver.get(course_link)
time.sleep(10)
print(course_name)
time.sleep(5)

def extract_modules_and_submodules():
    sections = driver.find_elements(By.CSS_SELECTOR, 'section.group__topic-wrapper')
    result = []

    for section in sections:
        # Extract module name
        module_name_element = section.find_element(By.CSS_SELECTOR, '.topic__title')
        module_name = module_name_element.text.strip() if module_name_element else 'Unknown Module'

        # Extract sub-modules
        sub_modules = []
        sub_module_wrapper_elements = section.find_elements(By.CSS_SELECTOR, '.level__title-wrapper')

        for wrapper in sub_module_wrapper_elements:
            p_element = wrapper.find_element(By.CSS_SELECTOR, '.level__title > span')
            if p_element:
                sub_module_text = p_element.text.strip()
                sub_modules.append(sub_module_text)

        # Store the module name and its sub-modules
        result.append({
            'moduleName': module_name,
            'subModules': sub_modules
        })

    return result

# Extract modules and sub-modules
modules_and_submodules = extract_modules_and_submodules()

# Save the result to a JSON file
with open('modules_and_submodules.json', 'w') as file:
    json.dump(modules_and_submodules, file, indent=2)

print("JSON data has been saved to 'modules_and_submodules.json'.")

# Close the WebDriver
driver.quit()
