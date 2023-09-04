from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
url = "https://google.com/ncr"
driver = webdriver.Chrome()
time.sleep(2)
driver.get(url)
driver.find_element(By.NAME,"q").send_keys("wikipedia python"+Keys.ENTER)
time.sleep(2)
time.sleep(3)#//*[@id='rso']/div[1]/div/div/div[1]/div/div/a
action = webdriver.ActionChains(driver)
action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

driver.find_element(By.XPATH,"//*[@id='rso']/div[7]/div/div/div[1]/div/div/a").click()

# the_content = driver.find_element(By.ID,"mw-content-text").text
time.sleep(3)