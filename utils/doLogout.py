import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def doLogout(driver):
    driver.get('https://ais.usvisa-info.com/en-ca/niv/users/sign_in')
    sleep(random.randrange(2, 5))
    if driver.title == "U.S. Visa Information - Login":
        print('Logged Out Successfully')
        return
    DropDown_Menus = driver.find_element(By.CSS_SELECTOR, '.vertical .medium-horizontal .menu .dropdown')
    Actions = DropDown_Menus.find_elements(By.TAG_NAME,'li')
    Actions[2].click()
    sleep(40)
    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Logout'))).click()
    # sleep(random.randrange(2, 5))
    # WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Yes'))).click()
    # sleep(random.randrange(2, 5))
    # driver.quit()
    # service.stop()