from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math


link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "span#num1")
    num2 = browser.find_element(By.CSS_SELECTOR, "span#num2")
    res = int(num1.text) + int(num2.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла