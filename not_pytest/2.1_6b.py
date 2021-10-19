from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"


try: 

    browser = webdriver.Chrome()
    browser.get(link)

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of people radio: ", robots_checked)
    assert robots_checked is None

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()