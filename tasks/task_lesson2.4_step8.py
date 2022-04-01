# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element
# из библиотеки expected_conditions.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math


def calc(x):
    y = math.log(abs(12 * math.sin(x)))
    return y


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    find_number = browser.find_element(By.ID, 'input_value')
    number = int(find_number.text)

    input_num = calc(number)

    find_input = browser.find_element(By.ID, 'answer')
    find_input.send_keys(input_num)

    find_submit = browser.find_element(By.ID, 'solve')
    find_submit.click()

finally:
    time.sleep(10)
    browser.quit()
