from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num1= int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    num2 = int(num2.text)
    sumab = num1+num2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sumab))  # ищем элемент с текстом "Python"


    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций 
    browser.quit()

# не забываем оставить пустую строку в конце файла