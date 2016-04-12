from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

usr = "INSERT username here"
pwd = "INSERT password here"

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("INSERT URL here")
#The URL above should contain only birthday posts to like, not your whole timeline

assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

while True:
      try:
	   scroll = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='u_0_9']/li[6]/a")))
      except TimeoutException:
	 break
      scroll.click() 

#the part of code below is not working, suggestions welcome!

#METHOD 1 
driver.execute_script("document.getElementsByClassName('commentable_item').click();");

#METHOD 2
#buttons =  driver.find_elements_by_tag_name("input")
#for element in buttons:
#    ActionChains(driver).click(element).perform()
