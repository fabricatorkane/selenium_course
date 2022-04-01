# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу,
# как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке",
# точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

# Ваша программа должна:
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(i):
    x = str(math.log(abs(12 * math.sin(int(i)))))
    return x


link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element(By.ID, 'treasure')
    num_treasure = treasure.get_attribute('valuex')
    print(num_treasure)

    x = calc(num_treasure)
    find_input = browser.find_element(By.ID, 'answer')
    find_input.send_keys(x)    # вставляем в инпут циферку

    find_check = browser.find_element(By.ID, 'robotCheckbox')    # ищем чекбокс
    find_check.click()

    find_radio = browser.find_element(By.ID, 'robotsRule')    # находим нужный радиобатон
    find_radio.click()

    find_submit = browser.find_element(By.CLASS_NAME, 'btn')    # ищем кнопку подтверждения
    find_submit.click()


finally:
    time.sleep(100)
    browser.quit()
