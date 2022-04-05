# Попробуйте оформить тесты из первого модуля в стиле unittest.
# Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# Создайте новый файл
# Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# Запустите получившиеся тесты из файла
# Просмотрите отчёт о запуске и найдите последнюю строчку
# Отправьте эту строчку в качестве ответа на это задание
# Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте.
# Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо
# (во всяком случае, здесь)!

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
link1 = "http://suninjuly.github.io/registration1.html"    # форма без бага
link2 = "http://suninjuly.github.io/registration2.html"    # форма с багом


class TestTask(unittest.TestCase):

    def test_open_link1(self):

        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block  .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block  .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block  .third')
        input3.send_keys("moi@moi.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, '.second_block  .first')
        input4.send_keys("34234234234")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Something went wrong')

    def test_open_link2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block  .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block  .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block  .third')
        input3.send_keys("moi@moi.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, '.second_block  .first')
        input4.send_keys("34234234234")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Something went wrong')


if __name__ == '__main__':
    unittest.main()
