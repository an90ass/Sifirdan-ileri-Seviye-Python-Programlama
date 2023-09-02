import requests
import json

class The_Movie_Db:
    def __init__(self) :
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "be1b84ea090f7b87f91e1055648ac131"
        
    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        # return response.json()
        json_data = json.loads(response.text)  # JSON nesnesi python nesnesine dönüştürme
        return json_data
    
    def getSearchMovie(self,keyword):
      response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
      response = json.loads(response.text)
      return response

movieApi = The_Movie_Db()  
while True:
    choice=input("1- Popular Movies\n2- Search Movie\n3- Exit\nYour choice :")
    if choice =='3':
        break
    else:
        if choice =="1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])

        elif choice =="2":
            key_word = input("Enter your key word: ")
            movies = movieApi.getSearchMovie(key_word)
            for movie in movies['results']:
                print(movie['name'])
