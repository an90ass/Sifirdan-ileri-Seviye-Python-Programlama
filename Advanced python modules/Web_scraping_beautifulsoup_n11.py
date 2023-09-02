'''
 N11 Product Scraper
Description: The N11 Product Scraper is a Python script designed to extract and display product information from 
the N11.com website. It employs web scraping techniques using the requests library and BeautifulSoup to fetch data
from the specified URL. The script targets a specific category, in this case, "dizustu-bilgisayar" (laptops), and 
retrieves details such as product name, product link, old price, and new price for each laptop listed on the webpage.
'''
import requests
from bs4 import BeautifulSoup

# The URL of the webpage you want to scrape
url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
# Sending an HTTP GET request to the URL and getting the HTML content
html = requests.get(url).content
# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
# Finding all the list items that contain product information
product_list = soup.find_all("li", {"class": "column"})

for product in product_list:   
    product_name = product.div.a.h3.text.strip()#Extracting the name of the product
    product_link = product.div.a.get("href") # Extracting the link to the product   
    old_price = product.find("div", {"class": "proDetail"}).find_all("a")[0].text.strip().strip('TL')#extracting the old price of the product  
    new_price = product.find("div", {"class": "proDetail"}).find_all("a")[1].text.strip().strip('TL') #extracting the new price of the product  
    print(f"Product Name: {product_name}\nLink: {product_link}\nOld Price: {old_price} TL\nNew Price: {new_price} TL\n")
