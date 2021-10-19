import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

@pytest.mark.skip
def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
    #pytest -v --tb=line --reruns 1 test_rerun