from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/cats.html"

# try:
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)
browser.find_element(By.ID, "button")



# finally:
# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла