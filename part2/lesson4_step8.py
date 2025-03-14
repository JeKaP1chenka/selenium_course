from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # browser.implicitly_wait(5)
    # browser.back()  
    
    text = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), "$100")
    )
    print(text)
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    button.click()
    
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    inpt = browser.find_element(By.CSS_SELECTOR, "input#answer")
    inpt.send_keys(y)
    btn = browser.find_element(By.XPATH, '//button[@id="solve"]')
    btn.click()
    
    # нада
    alert = browser.switch_to.alert
    print(alert.text)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла