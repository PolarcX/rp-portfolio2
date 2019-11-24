import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_addcat():
    
    driver = webdriver.Chrome()

    driver.get("localhost:8000/admin/")

    elem = driver.find_element_by_id("id_username")
    elem.send_keys("polarcx")

    elem = driver.find_element_by_id("id_password")
    elem.send_keys("polarcx")

    elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/input")
    elem.click()

    elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]")
    elem.click()

    elem = driver.find_element_by_name("name")
    elem.send_keys("Testing")

    elem = driver.find_element_by_name("_save")
    
    elem.click()

    
