from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def math1(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome("C:\\Users\\Gorshok\\Downloads\\chromedriver_win32\\chromedriver.exe")
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
button = browser.find_element_by_class_name('trollface.btn.btn-primary').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
s = int(browser.find_element_by_id("input_value").text)
field = browser.find_element_by_id("answer")
field.send_keys(str(math1(s)))
browser.find_element_by_css_selector("[type='submit']").click()
time.sleep(10)
browser.quit()
