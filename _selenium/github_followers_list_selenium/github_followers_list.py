'''
This code snippet is a Python script that uses Selenium to automate interactions with GitHub.
It enables users to log in, retrieve a list of their followers, and store those follower usernames in a list.
'''
from user_information import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


class Githb:
    def __init__(self,username,password) :
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.url = "https://github.com/login"
        self.browser.get(self.url)   
        time.sleep(2) 

        username = self.browser.find_element(By.NAME,"login")
        password = self.browser.find_element(By.XPATH,"//*[@id='password']")

        username.send_keys(self.username)
        password.send_keys(self.password)

        time.sleep(1)
        self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[13]").click()
        # time.sleep(5)
    def loadfollowers(self):
        items = self.browser.find_elements(By.CLASS_NAME, "d-table table-fixed col-12 width-full py-4 border-bottom color-border-muted")
        for i in items:
            try:
                username_element = i.find_element(By.XPATH, "//*[@id='user-profile-frame']/div/div[1]/div[2]/a/span[2]")
                username = username_element.text
                self.followers.append(username)
            except NoSuchElementException:
                continue
    def getFollowers(self):
        username = self.username
        self.browser.get(f"https://github.com/{username}?tab=followers")
        time.sleep(2)

        self.loadfollowers()


        while True: 
            #In order to move to other pages where other followers are located, by clicking on the Next button
            links = self.browser.find_element(By.XPATH,"//*[@id='user-profile-frame']/div/div[51]/div").find_elements(By.TAG_NAME,"a")
            if len(links)==1:
                if links[0].text =="Next":
                    links[0].click()
                    time.sleep(1)
                     
                    self.loadfollowers()

                else: #This means that we have reached the last page
                 break


            else: #If more than one link comes, it means that there is more than one page
              for link in links:
                 if link.text == "Next":
                    link.click()  
                    time.sleep(1)

                    self.loadfollowers()

                 else:
                  continue         

    
githb = Githb(username,password)
githb.signIn()
githb.getFollowers()
print(githb.followers)