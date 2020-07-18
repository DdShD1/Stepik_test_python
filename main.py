from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


def math1(x):
    return str(math.log(abs((12 * math.sin(x)))))


driver = webdriver.Chrome("C:\\Users\\Gorshok\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("http://suninjuly.github.io/execute_script.html")
s = float(driver.find_element_by_id("input_value").text)
select = driver.find_element_by_id("answer")
select.send_keys(math1(s))
driver.find_element_by_css_selector('[for="robotCheckbox"]').click()
robot = driver.find_element_by_css_selector('[for="robotsRule"]')
driver.execute_script("return arguments[0].scrollIntoView(true);", robot)
robot.click()
button = driver.find_element_by_css_selector("[type='submit']")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)
driver.quit()
