from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:

	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_name("firstname")
	input1.send_keys("Абвгдеёж")

	input2 = browser.find_element_by_name("lastname")
	input2.send_keys("Абвгдеёжз")

	input3 = browser.find_element_by_name("email")
	input3.send_keys("Абвгдеёж@mail.ru")

	#current_dir = os.path.abspath(os.path.dirname(__file__))
	#file_name = "file.txt"
	#file_path = os.path.join(current_dir, file_name)
	#print('-------------------------------')
	#print("Вывод file_name: " , file_name)
	#print("Вывод file_path: " , file_path)
	#print('-------------------------------')
	element = browser.find_element_by_id("file")
	#element.send_keys(file_path)

	element.send_keys("C:/Users/wtolk/Desktop/Утиль/file.txt")

	button = browser.find_element_by_xpath("//button[@type='submit']")
	button.click()

	alert = browser.switch_to.alert
	alert_text = alert.text
	addToClipBoard = alert_text.split(': ')[-1]
	print('-------------------------------')
	print(addToClipBoard)
	print('-------------------------------')

finally:

	time.sleep(1)
	browser.quit()
	