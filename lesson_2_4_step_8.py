from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '//*[@id="book"]')
    price = browser.find_element(By.ID, "price")
    # работа с ожиданием нужного значения
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    # вариант с циклом, без явно прописанного ожидания
    # while price.text != "$100":
    #     price = browser.find_element(By.ID, "price")

    button.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
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
