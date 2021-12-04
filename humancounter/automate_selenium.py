from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  
import os 

driver = webdriver.Chrome()
driver.maximize_window()  
driver.get("http://127.0.0.1:8000/")
driver.find_element_by_name("TrainImage").send_keys(os.getcwd()+"/upload_test.jpg")
driver.find_element_by_name("OutputImage").send_keys("a")
driver.find_element_by_id("submit_button").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()  
