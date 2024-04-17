from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'num1')
    y_element = browser.find_element(By.ID, 'num2')
    x = x_element.text
    y = y_element.text
    sum_xy = int(x) + int(y)
    sum_text = str(sum_xy)
    # выбираем в селекторе ответ по вычисленному значению
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_text)
    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
