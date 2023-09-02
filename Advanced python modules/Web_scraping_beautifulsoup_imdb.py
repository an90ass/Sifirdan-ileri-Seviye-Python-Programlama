'''
IMDb Top 50 Movies Scraper
Description: The IMDb Top 50 Movies Scraper is a Python script that extracts and displays information about the 
top-rated movies on IMDb. It utilizes web scraping techniques with the help of the requests library and BeautifulSoup
to fetch data from the IMDb website. The script parses the HTML content of the IMDb Top 250 chart page, extracts details 
such as movie title, release year, and IMDb rating, and then presents the information in a neatly formatted list.
'''
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr",limit=50)
count = 1

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text

    print(f"{count}- film: {title.ljust(50)} yıl: {year} değerlendirme: {rating}")
    count+=1