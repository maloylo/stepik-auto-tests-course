from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button.click()
    # работа с переключением на новое окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    result_x = math.log(abs(12 * math.sin(int(x))))

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(result_x))

    button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
