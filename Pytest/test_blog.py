import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_login():
    driver = webdriver.Chrome()
    
    driver.get("localhost:8000/blog/")
    
