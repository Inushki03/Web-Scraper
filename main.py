import requests
from bs4 import BeautifulSoup
import csv
import time


for page_num in range(1,51):
    URL = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"Scraping page {page_num}...")

    response = requests.get(URL)

    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}")
        break

    soup = BeautifulSoup(response.content, "html.parser")   

    # Fisrt Book
    # first_book = soup.find("article",class_="product_pod")
    # title = first_book.h3.a["title"]
    # price = first_book.find("p",class_="price_color").text
    # rating = first_book.find("p",class_="star-rating")["class"][1]

    all_books = soup.find_all("article",class_="product_pod")
    books_data = []

    for book in all_books:
        title = book.h3.a["title"]
        price = book.find("p",class_="price_color").text
        rating = book.find("p",class_="star-rating")["class"][1]

        books_info = {
            "title":title,
            "price":price,  
            "rating":rating
        }

        books_data.append(books_info)

    print(f"page {page_num} waiting for 1 second...")
    time.sleep(1)
    
with open("book.csv","w",newline="",encoding="utf-8") as file:
    header = ["title","price","rating"]
    writer = csv.DictWriter(file,fieldnames=header) 
    writer.writeheader()
    writer.writerows(books_data)

print("Data has been written to book.csv")



