from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import re


def getToAppointments(driver):
    continue_button = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Continue')))
    current_appointment = driver.find_element(By.CLASS_NAME, 'consular-appt').text
    current_appointment = re.search(r'\b\d{1,2} [A-Za-z]+, \d{4}\b', current_appointment).group(0)
    continue_button.click()
    sleep(random.randrange(2, 5))
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Reschedule'))).click()
    sleep(random.randrange(2, 5))
    small_only_expanded = driver.find_elements(By.CLASS_NAME, 'small-only-expanded')
    small_only_expanded[3].click()
    sleep(random.randrange(2, 5))
