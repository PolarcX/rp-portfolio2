from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

def test_addpost():
    
   driver = webdriver.Chrome()

   driver.get("localhost:8000/admin/")

   elem = driver.find_element_by_id("id_username")
   elem.send_keys("polarcx")

   elem = driver.find_element_by_id("id_password")
   elem.send_keys("polarcx")

   elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/input")
   elem.click()

   driver.get("http://localhost:8000/admin/blog/post/add/")

   elem = driver.find_element_by_name("title")
   elem.send_keys("test")

   elem = driver.find_element_by_name("body")
   elem.send_keys("test1")

   from selenium.webdriver.support.ui import Select

   elem = Select(driver.find_element_by_name("categories"))
   elem.select_by_value('1')

   elem = driver.find_element_by_name("_save") 
   elem.click()

    
