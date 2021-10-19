from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_xpath("//button[@type='submit']")
	button.click()

	confirm = browser.switch_to.alert
	confirm.accept()

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)

	input1 = browser.find_element_by_id("answer")
	input1.send_keys(str(y))

	button = browser.find_element_by_xpath("//button[@type='submit']")
	button.click()

	alert = browser.switch_to.alert
	alert_text = alert.text
	addToClipBoard = alert_text.split(': ')[-1]
	print('-------------------------------')
	print(addToClipBoard)
	print('-------------------------------')

finally:
	
	time.sleep(2)
	browser.quit()