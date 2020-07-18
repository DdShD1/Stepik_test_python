from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def math1(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome("C:\\Users\\Gorshok\\Downloads\\chromedriver_win32\\chromedriver.exe")
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button1 = browser.find_element_by_css_selector("[type='Submit']").click()
promt = browser.switch_to.alert
promt.accept()
s = int(browser.find_element_by_id("input_value").text)
field = browser.find_element_by_id("answer")
field.send_keys(str(math1(s)))
browser.find_element_by_css_selector("[type='submit']").click()
time.sleep(10)
browser.quit()
