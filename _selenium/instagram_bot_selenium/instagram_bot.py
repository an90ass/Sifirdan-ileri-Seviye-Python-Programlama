'''
This code snippet is a Python script that uses the Selenium library 
to automate interactions with Instagram. It includes functionality for logging in, retrieving followers, 
, following and unfollowing specific users.
'''
from instagram_user_inforomation import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    def __init__(self,username,password):
        # self.browserProfile = webdriver.ChromeOptions()
        # self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome()#'chromedriver.exe', chrome_options=self.browserProfile
        self.username = username
        self.password = password
    

    def sigin(self):
        url ="https://www.instagram.com/accounts/login/"
        self.browser.get(url)
        time.sleep(2)
        username_input = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        password_input = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
        
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        user = self.username
        self.browser.get(f"https://www.instagram.com/{user}")
        time.sleep(2)
        followers_link = self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_r/']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/a[2]")
        followers_link.click()    
        time.sleep(2)
        dialog =self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog] ul")
        follower_count = len(dialog.find_elements(By.CSS_SELECTOR,"li")) 
        print(f"First count {follower_count}")
        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            new_follower_count= len(dialog.find_elements(By.CSS_SELECTOR,"li"))
            
            if new_follower_count != follower_count:
                follower_count=new_follower_count
                print(f"Second count {follower_count}")
                time.sleep(1)
                pass
            else:
                break
              
        followers= dialog.find_elements(By.CSS_SELECTOR,"li")
        follower_list =[]
        for user in followers:
            link = user.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            follower_list.append(link)
        with open("followers.text","w",encoding="UTF-8")as file:
            for item in follower_list:
                file.write(item+"\n")    

    def followUser(self,username):
        self.browser.get("https://www.instagram.com/"+ username)
        followButton = self.browser.find_element(By.CSS_SELECTOR, 'button:contains("Follow")')
        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following")
        time.sleep(30)
    def unfollowUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(1)
        followButton = self.browser.find_element(By.TAG_NAME,"button")
        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)
            self.browser.find_element(By.XPATH,'//bottun[text()=Unfollow]').click()
        else:
            print("You are already unfollowing")


instagram = Instagram(username,password)
instagram.sigin()
instagram.getFollowers()

list_of_followers_to_following = ['kod_evreni']
for user in list_of_followers_to_following:
 instagram.followUser(user)
