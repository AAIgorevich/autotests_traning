from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects1.html"

#def calc(x):
   # return str(int(x1 + x2))

try: 

    browser = webdriver.Chrome()
    browser.get(link)
    x = 0;
    x_element1 = browser.find_element_by_id("num1")
    x += int(x_element1.text)
    #x = val.get_attribute("text")
    x_element2 = browser.find_element_by_id("num2")
    x += int(x_element2.text)
    #z = val.get_attribute("text")
    print("Значение: ", x )
    #y = calc(x)
     
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x)) 

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    print('-------------------------------')
    print(addToClipBoard)
    print('-------------------------------')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(0.1)
    # закрываем браузер после всех манипуляций
    browser.quit()