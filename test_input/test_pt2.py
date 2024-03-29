from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input")
    input1.send_keys("Ivan")
    input3 = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input")
    input3.send_keys("NEPOMNYou@mail.ru")
    input4 = browser.find_element_by_xpath("//div[@class='second_block']/div[@class='form-group first_class']/input")
    input4.send_keys("SUMSUNG")
    input5 = browser.find_element_by_xpath("//div[@class='second_block']/div[@class='form-group second_class']/input")
    input5.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    def test_abs1(self):
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)
if __name__ == "__main__":
    unittest.main()