# На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера,
# но сложным для человека.
# Ваша программа должна выполнить следующие шаги:
# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(i):
    x = str(math.log(abs(12 * math.sin(int(i)))))
    return x


link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_num = browser.find_element(By.ID, 'input_value')
    num_text = find_num.text

    x = calc(num_text)
    print(x)
    input1 = browser.find_element(By.CLASS_NAME, 'form-control')
    input1.send_keys(x)

    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio.click()

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()


