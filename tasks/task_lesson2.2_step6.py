from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    y = math.log(abs(12*math.sin(x)))
    print(y)
    return y


link = 'http://suninjuly.github.io/execute_script.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_num = browser.find_element(By.ID, 'input_value')
    num = int(find_num.text)

    fx = calc(num)

    input_num = browser.find_element(By.ID, 'answer')
    input_num.send_keys(fx)

    # browser.execute_script("window.scrollBy(0, 99);")    #с этим работает, нужно разобраться с остальными

    find_check = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', find_check)
    find_check.click()

    find_radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', find_radio)
    find_radio.click()

    find_button = browser.find_element(By.CLASS_NAME, 'btn')
    # browser.execute_script('return arguments[0],scrollIntoView(true);', find_button)    # с этим почему-то не работает
    find_button.click()

finally:
    time.sleep(20)
    browser.quit()

