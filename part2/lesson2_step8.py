from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    last_name.send_keys("Petrov")
    email = browser.find_element(By.XPATH, '//input[@name="email"]')
    email.send_keys("test@mail.temp")
    file_upload = browser.find_element(By.XPATH, '//input[@name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file_upload.send_keys(file_path)
    btn = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла