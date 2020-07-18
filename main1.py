from selenium import webdriver
import time
browser = webdriver.Chrome("C:\\Users\\Gorshok\\Downloads\\chromedriver_win32\\chromedriver.exe")
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)
browser.quit()
