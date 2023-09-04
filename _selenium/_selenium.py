from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "http://sadikturan.com"
driver.get(url)
# time.sleep(2)
driver.maximize_window()
driver.save_screenshot("screenshot.png")
print(driver.title)

url = "https://www.youtube.com/results?search_query=selenium+python+download+for+116.0.5845.141+chromw"
driver.get(url)
print(driver.title)
driver.back()
time.sleep(2)
driver.close()