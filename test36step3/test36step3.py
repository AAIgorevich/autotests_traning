#test36step3.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest

#@pytest.mark.skip()
def test_exception1():
    try:
    	answer = math.log(int(time.time()))
    	
    	browser = webdriver.Chrome()
    	browser.get("https://stepik.org/lesson/236895/step/1")

    	input1 = WebDriverWait(browser, 12).until(
    		EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    		)

    	input1.send_keys(str(answer))
    	button = browser.find_element_by_xpath("//button[@class='submit-submission']")
    	button.click()
    	
    	a = WebDriverWait(browser, 15).until(
    		EC.visibility_of_element_located((By.TAG_NAME, "pre"))
    		).text
    	f = "Correct!"

    	assert f == a, print(a) 
    		   	
    finally:
    	browser.quit()

#@pytest.mark.skip()
def test_exception2():
    try:
    	answer = math.log(int(time.time()))
    	
    	browser = webdriver.Chrome()
    	browser.get("https://stepik.org/lesson/236896/step/1")

    	input1 = WebDriverWait(browser, 12).until(
    		EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    		)

    	input1.send_keys(str(answer))
    	button = browser.find_element_by_xpath("//button[@class='submit-submission']")
    	button.click()

    	a = WebDriverWait(browser, 15).until(
    		EC.visibility_of_element_located((By.TAG_NAME, "pre"))
    		).text
    	f = "Correct!"

    	assert f == a, print(a) 
    		    	
    finally:
    	browser.quit()

#@pytest.mark.skip()
def test_exception3():
    try:
    	answer = math.log(int(time.time()))
    	
    	browser = webdriver.Chrome()
    	browser.get("https://stepik.org/lesson/236897/step/1")

    	input1 = WebDriverWait(browser, 12).until(
    		EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    		)
    	
    	input1.send_keys(str(answer))
    	button = browser.find_element_by_xpath("//button[@class='submit-submission']")
    	button.click()

    	a = WebDriverWait(browser, 15).until(
    		EC.visibility_of_element_located((By.TAG_NAME, "pre"))
    		).text
    	f = "Correct!"

    	assert f == a, print(a) 
    		
    finally:
    	browser.quit()

#@pytest.mark.skip()
def test_exception4():
    try:
    	answer = math.log(int(time.time()))
    	
    	browser = webdriver.Chrome()
    	browser.get("https://stepik.org/lesson/236898/step/1")

    	input1 = WebDriverWait(browser, 12).until(
    		EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    		)
    	
    	input1.send_keys(str(answer))
    	button = browser.find_element_by_xpath("//button[@class='submit-submission']")
    	button.click()

    	a = WebDriverWait(browser, 15).until(
    		EC.visibility_of_element_located((By.TAG_NAME, "pre"))
    		).text
    	f = "Correct!"

    	assert f == a, print(a) 
    		  	
    finally:
    	browser.quit()

#@pytest.mark.skip()
def test_exception5():
    try:
    	answer = math.log(int(time.time()))
    	
    	browser = webdriver.Chrome()
    	browser.get("https://stepik.org/lesson/236899/step/1")

    	input1 = WebDriverWait(browser, 12).until(
    		EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    		)
    	
    	input1.send_keys(str(answer))
    	button = browser.find_element_by_xpath("//button[@class='submit-submission']")
    	button.click()

    	a = WebDriverWait(browser, 15).until(
    		EC.visibility_of_element_located((By.TAG_NAME, "pre"))
    		).text
    	f = "Correct!"

    	assert f == a, print(a) 
    		   	
    finally:
    	browser.quit()

#@pytest.mark.skip()
def test_exception6():
    try:
    	answer = math.log(int(time.time()))
    	
    	browser = webdriver.Chrome()
    	browser.get("https://stepik.org/lesson/236903/step/1")

    	input1 = WebDriverWait(browser, 12).until(
    		EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    		)
    	
    	input1.send_keys(str(answer))
    	button = browser.find_element_by_xpath("//button[@class='submit-submission']")
    	button.click()

    	a = WebDriverWait(browser, 15).until(
    		EC.visibility_of_element_located((By.TAG_NAME, "pre"))
    		).text
    	f = "Correct!"

    	assert f == a, print(a) 
    		  	
    finally:
    	browser.quit()

#@pytest.mark.skip()
def test_exception7():
    try:
    	answer = math.log(int(time.time()))
    	
    	browser = webdriver.Chrome()
    	browser.get("https://stepik.org/lesson/236904/step/1")

    	input1 = WebDriverWait(browser, 12).until(
    		EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    		)
    	
    	input1.send_keys(str(answer))
    	button = browser.find_element_by_xpath("//button[@class='submit-submission']")
    	button.click()

    	a = WebDriverWait(browser, 15).until(
    		EC.visibility_of_element_located((By.TAG_NAME, "pre"))
    		).text
    	f = "Correct!"

    	assert f == a, print(a) 
    		   	
    finally:
    	browser.quit()

#@pytest.mark.xfail()
def test_exception8():
    try:
    	answer = math.log(int(time.time()))
    	
    	browser = webdriver.Chrome()
    	browser.get("https://stepik.org/lesson/236905/step/1")

    	input1 = WebDriverWait(browser, 12).until(
    		EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    		)
    	
    	input1.send_keys(str(answer))
    	button = browser.find_element_by_xpath("//button[@class='submit-submission']")
    	button.click()

    	a = WebDriverWait(browser, 15).until(
    		EC.visibility_of_element_located((By.TAG_NAME, "pre"))
    		).text
    	f = "Correct!"
    	assert f == a, print(a) 
    		
    finally:
    	browser.quit()
    	#The owls are not what they seem! OvO