import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/]

@pytest.mark.parametrize('link', links)
def test_basket_button(browser, link):
    
    browser.get(f"{link}")
    
    submit = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//form[@id='add_to_basket_form']/button"))
        )
    assert submit, "Button 'Add to basket' not found"

