from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script('document.getElementsByTagName("input")[0].scrollIntoView(true);')
    inpt = browser.find_element(By.CSS_SELECTOR, "input#answer")
    inpt.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    checkbox.click()
    radiobtn = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    radiobtn.click()
    btn = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    btn.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла