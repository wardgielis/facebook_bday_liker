from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
#this loop scrolls down the page
while True:
      try:
	   scroll = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='u_0_9']/li[6]/a")))
      except TimeoutException:
	 break
      scroll.click()

#Javascript executor is needed to click on JS generated elements such as the like button. Check the Class using web inspector
driver.execute_script("var elems = document.getElementsByClassName('UFILikeLink _4x9- _4x9_ _48-k');for(var i= 0;i<elems.length;i++){elems[i].click();}");
