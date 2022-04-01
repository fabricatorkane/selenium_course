from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(a, b):
    return int(a) + int(b)


link = 'http://suninjuly.github.io/selects2.html' # 'http://suninjuly.github.io/selects1.html'    #

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_num1 = browser.find_element(By.ID, 'num1')
    num1 = find_num1.text    # достаем значение числа

    find_num2 = browser.find_element(By.ID, 'num2')
    num2 = find_num2.text

    sum = str(calc(num1, num2))

    select = Select(browser.find_element(By.TAG_NAME, 'select'))    # инитим класс, находим элемент селекс,кликаем на него
    select.select_by_visible_text(sum)     # ищем в вариантах нужное нам значение

    find_submit = browser.find_element(By.CLASS_NAME, 'btn')     # ищем кнопку
    find_submit.click()    # кликаем на кнопку

finally:
    time.sleep(30)
    browser.quit()
