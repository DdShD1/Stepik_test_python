from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import math

def math1(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome("C:\\Users\\Gorshok\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 13).until(
    EC.text_to_be_present_in_element((By.ID, "price"), str(100))
)
button = browser.find_element_by_id('book').click()
s = int(browser.find_element_by_id("input_value").text)
field = browser.find_element_by_id("answer")
field.send_keys(str(math1(s)))
browser.find_element_by_css_selector("[type='submit']").click()
time.sleep(10)
browser.quit()
