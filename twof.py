from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome("C:\\Users\\Gorshok\\Downloads\\chromedriver_win32\\chromedriver.exe")
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
input1 = browser.find_element_by_css_selector("[name='firstname']")
input1.send_keys('Pavel')
input2 = browser.find_element_by_css_selector("[name='lastname']")
input2.send_keys('Kirillov')
input2 = browser.find_element_by_css_selector("[name='email']")
input2.send_keys('petlenov@yandex.ru')
input3 = browser.find_element_by_css_selector("[type='file']")
input3.send_keys(file_path)
button = browser.find_element_by_css_selector("button.btn").click()
time.sleep(10)
browser.quit()
