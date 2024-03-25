from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def opendriver(x):
    liste = []
    for i in range(x):
        liste.append(webdriver.Firefox())
    return liste

def opensite(x,driverliste):
    driverliste[x].get('https://addons.mozilla.org/de/firefox/addon/adblock-plus/')

def einloggen2(driver):
    server = driver.find_element_by_xpath('//*[@id="joinGame"]/button')
    time.sleep(1)
    server.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])

def lasttab(driver):
    driver.switch_to.window(driver.window_handles[-1])

