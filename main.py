from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from interceptor import interceptor
import random
from utils.sleepRandom import send_keys_random_time
from utils.doLogout import doLogout
from utils.getToAppointments import getToAppointments
import os
from dotenv import load_dotenv
# loading variables from .env file
load_dotenv() 


# Start the ChromeDriver-controlled browser
service = Service('chromedriver.exe')
service.start()

# Connect to the ChromeDriver-controlled browser
driver = webdriver.Chrome(service=service)

# Perform actions
driver.get('https://ais.usvisa-info.com/en-ca/niv/users/sign_in')

driver.response_interceptor = interceptor

sleep(random.randrange(2, 5))

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('MY_PASSWORD')

# Enter credentials
email = driver.find_element('id', 'user_email')
email.clear()
send_keys_random_time(email, my_email)

sleep(random.randrange(2, 5))

password = driver.find_element('id', 'user_password')

password.clear()
send_keys_random_time(password, my_password)

sleep(random.randrange(2, 5))

# find element which contains class name 'btn-primary' and may have other class names as well and click on it
terms_conditions = driver.find_element(By.CSS_SELECTOR, '.icheck-label')
terms_conditions.click()
sleep(random.randrange(2, 5))

Sign_in = driver.find_element(By.CLASS_NAME, 'primary')
Sign_in.click()



current_appointment = getToAppointments(driver)


# 
# doLogout()




try:
    print("System Busy Check started")
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Close')))
    SystemBusy = driver.find_element(By.ID, 'consulate_date_time_not_available')
    if SystemBusy.text == "System is busy. Please try again later.":
        print("System Busy")
        driver.quit()
        service.stop()
except NoSuchElementException:
    print('No Such Element Found')
except:
    print('No System Busy')

# for request in driver.requests:
#     if request.response:
#         f = open("demofile2.txt", "a")
#         f.write("Request URL: " +request.url+ " " + str(request.response.status_code )+ "Request Headers: " + str(request.headers) +  "Response Headers: " + str(request.response.headers))
#         f.close()
#         print("Added to file")

sleep(50)
    

sleep(4000)


print(driver.title)

# Close the browser
# driver.quit()
# service.stop()


#  Group ID 42814961