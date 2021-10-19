from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 

    browser = webdriver.Chrome()
    browser.get(link)

    val = browser.find_element_by_id("treasure")
    x = val.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))

    button = browser.find_element_by_id("robotCheckbox")
    button.click()

    button = browser.find_element_by_id("robotsRule")
    button.click()

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
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()