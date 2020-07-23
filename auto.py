from selenium import webdriver
import selenium.webdriver.common.keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time

link = "https://move.ru/"

browser = webdriver.Chrome()
browser.get(link)

imp_first_page = browser.find_element_by_link_text("Разместить объявление").click()
time.sleep(2)

browser.find_element_by_partial_link_text("Войти").click()
time.sleep(1)

input1 = browser.find_element_by_css_selector("input[placeholder='Email или телефон']")
input1.send_keys("pashokmem@yandex.ru")

input2 = browser.find_element_by_css_selector("input[placeholder='Пароль']")
input2.send_keys("wMY-Vwy-vte-Us8")

browser.find_element_by_css_selector("button[type='submit'].btn").click()
time.sleep(7)

browser.find_element_by_css_selector("[class='radio-tab__label']:first-of-type").click()

browser.find_element_by_css_selector("[for='forcategory0'").click()

browser.find_element_by_css_selector("[for='forsubcategory0'").click()

input1 = browser.find_element_by_css_selector("input[type='search']:nth-child(2)")
input1.send_keys("Кристалл \n")

input1 = browser.find_element_by_css_selector("input[placeholder='Укажите улицу...']")
input1.send_keys("Тверская \n")

input1 = browser.find_element_by_css_selector("input[name='rooms']")
input1.send_keys("3 \n")

input1 = browser.find_element_by_css_selector("input[name='floor']")
input1.send_keys("3 \n")

input1 = browser.find_element_by_css_selector("input[name='squareTotal']")
input1.send_keys("100 \n")

input1 = browser.find_element_by_css_selector("input[name='squareLive']")
input1.send_keys("10 \n")

input1 = browser.find_element_by_css_selector("input[name='squareKitchen']")
input1.send_keys("10 \n")

input1 = browser.find_element_by_css_selector("input[name='floors'][class='input-text__input form-control']")
input1.send_keys("3 \n")

input1 = browser.find_element_by_css_selector("input[name='files[]'][type='file]")
input1.send_keys("104.jpg \n")

input1 = browser.find_element_by_css_selector("input[placeholder='Введите описание объекта...']")
input1.send_keys("Самый обычный дом \n")

input1 = browser.find_element_by_css_selector("input[placeholder='Номер телефона']")
input1.send_keys("9373061890 \n")

input1 = browser.find_element_by_css_selector("[title='Укажите фамилию и имя']")
input1.send_keys("Некто Мекто \n")

input1 = browser.find_element_by_name("price")
input1.send_keys("1000000 \n")

browser.find_element_by_link_text("Бесплатное размещение").click()
browser.find_element_by_class_name("adding-object__btn-finish").click()
time.sleep(10)
