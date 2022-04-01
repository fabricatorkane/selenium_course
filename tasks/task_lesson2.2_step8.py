import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')    # получаем абсолютный путь для загружаемого файла
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_fname = browser.find_element(By.NAME, 'firstname')
    find_fname.send_keys('Ivan')

    find_lname = browser.find_element(By.NAME, 'lastname')
    find_lname.send_keys('Petrov')

    find_email = browser.find_element(By.NAME, 'email')
    find_email.send_keys('test@te.ru')

    find_upload = browser.find_element(By.CSS_SELECTOR, '[type="file"]')    # находим кнопку, по которой грузий файл
    find_upload.send_keys(file_path)    # загружаем сам файл

    find_submit = browser.find_element(By.CLASS_NAME, 'btn')
    find_submit.click()

finally:
    time.sleep(10)
    browser.quit()
