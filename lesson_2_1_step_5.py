from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # поиск значения на странице
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text

    # функция возвращающая вычисленное значение
    def calc(num):
        return str(math.log(abs(12 * math.sin(int(num)))))

    y = calc(x)
    # ввод вычисленного значения в поле
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    # отмечаем чекбокс
    option1 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/label")
    option1.click()
    #  отмечаем радиокнопку
    option2 = browser.find_element(By.XPATH, "/html/body/div/form/div[4]/label")
    option2.click()
    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
