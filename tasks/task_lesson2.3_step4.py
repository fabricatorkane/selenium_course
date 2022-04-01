# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    y = math.log(abs(12 * math.sin(x)))
    return y


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_button = browser.find_element(By.CLASS_NAME, 'btn')
    find_button.click()

    confirm = browser.switch_to.alert     # шмякаем в алерте, что мы с ним согласны
    confirm.accept()

    find_x = browser.find_element(By.ID, 'input_value')
    x = int(find_x.text)

    num = calc(x)

    find_answer = browser.find_element(By.ID, 'answer')
    find_answer.send_keys(num)

    find_comfirm = browser.find_element(By.CLASS_NAME, 'btn')
    find_comfirm.click()

finally:
    time.sleep(10)
    browser.quit()

