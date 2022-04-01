# В этом задании после нажатия кнопки страница откроется в новой вкладке,
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.
# Сценарий для реализации выглядит так:
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    y = math.log(abs(12 * math.sin(x)))
    return y


try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_button = browser.find_element(By.CLASS_NAME, 'trollface')
    find_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    find_number = browser.find_element(By.ID, 'input_value')
    number = int(find_number.text)

    input_num = calc(number)

    find_input = browser.find_element(By.ID, 'answer')
    find_input.send_keys(input_num)

    find_submit = browser.find_element(By.CLASS_NAME, 'btn')
    find_submit.click()

finally:
    time.sleep(10)
    browser.quit()
