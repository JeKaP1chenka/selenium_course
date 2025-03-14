from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_block ='//div[@class="first_block"]'
    second_block ='//div[@class="second_block"]'
    input_lmb = lambda x : f'//input[@class="form-control {x}"]'
    
    input1 = browser.find_element(By.XPATH, f'{first_block}{input_lmb("first")}')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, f'{first_block}{input_lmb("second")}')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, f'{first_block}{input_lmb("third")}')
    input3.send_keys("test@mail.temp")
    input4 = browser.find_element(By.XPATH, f'{second_block}{input_lmb("first")}')
    input4.send_keys("89998887766")
    input5 = browser.find_element(By.XPATH, f'{second_block}{input_lmb("second")}')
    input5.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()