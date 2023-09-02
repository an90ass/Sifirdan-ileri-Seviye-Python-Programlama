'''
GitHubProfileAnalyzer
Description: GitHubProfileAnalyzer is a Python-based project that interacts with the GitHub API to provide 
users with valuable insights into GitHub profiles. Users can search for GitHub users, retrieve their public
repositories, and even create new repositories right from the command line. The project's main features include 
user information retrieval, repository listing, and repository creation. GitHubProfileAnalyzer simplifies the process of 
exploring GitHub profiles and repositories, making it a valuable tool for both developers and GitHub enthusiasts.
'''

import requests
import json

class User:
    def __init__(self, username, repos, followers):
        self.username = username
        self.repos = repos
        self.followers = followers

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = ''
        self.users = []

    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        response_json = response.json()

        user_info = {
            "name": response_json.get('name', ''),
            "public_repos": response_json.get('public_repos', ''),
            "followers": response_json.get('followers', '')
        }
        user = User(username=user_info['name'], repos=user_info['public_repos'], followers=user_info['followers'])
        self.users.append(user)
        self.saveToFile()
        return response_json
    
    def saveToFile(self):
        data_to_save = []
        for user in self.users:
            user_data = {
                "name": user.username,
                "public_repos": user.repos,
                "followers": user.followers
            }
            data_to_save.append(user_data)
            print(data_to_save)

        with open('Save_information_file.json', 'w') as file:
            json.dump(data_to_save, file, ensure_ascii=False, indent=4)

    def getRipositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()

    def creatRepository(self, name):
        response = requests.post(self.api_url + '/user/repos?access_token=' + self.token, json={
            "name": name,
            "description": "I am Anas who created this repo by coding in python",
            "homepage": "https://an90ass.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()

github = Github()

while True:
    choice = input('1- Find user\n2- Get Repositories\n3- Create Repository\n4- Exit\n Your choice: ')

    if choice == '4':
        break
    else:
        if choice == '1':
            username = input('User name: ')
            result = github.getUser(username)
            print(f"name: {result['name']} , public repos: {result['public_repos']} , followers: {result['followers']}")
        elif choice == '2':
            username = input('User name: ')
            result = github.getRipositories(username)
            for repo in result:
                print(repo['name'])
        elif choice == '3':
            username = input('User name: ')
            result = github.creatRepository(username)
            print(result)
        else:
            print('You entered the wrong number')
