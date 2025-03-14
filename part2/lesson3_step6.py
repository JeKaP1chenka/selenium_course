from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    btn = browser.find_element(By.XPATH, '//button[@class="trollface btn btn-primary"]')
    btn.click()
    browser.switch_to.window(browser.window_handles[1])
    
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    inpt = browser.find_element(By.CSS_SELECTOR, "input#answer")
    inpt.send_keys(y)
    btn = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    btn.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла