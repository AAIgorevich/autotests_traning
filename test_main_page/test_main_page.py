import pytest
from selenium import webdriver


def should_be_login_link(self):
    self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()