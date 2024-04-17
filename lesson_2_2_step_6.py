from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    result_x = math.log(abs(12 * math.sin(int(x))))

    # как вариант можно скрыть футер, вместо прокрутки
    # browser.execute_script("document.querySelector('footer').remove()")

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(result_x))
    option1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    # прокрутка для действия ниже видимой части страницы
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    # прокрутка для действия ниже видимой части страницы
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
