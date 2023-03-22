# pip install BeautifulSoup4 lxml

from bs4 import BeautifulSoup as BS
import requests
import sqlite3

url = "https://korfiati.ru/vyikroyki-odezhdyi/ready-made-patterns/"

req = requests.get(url)

soup = BS(req.content, "lxml")


"""Описание выкройки и ссылка на неё"""


args = []
html = soup.select("div.post-thumbnail")

for elements in html:
    urls = elements.select_one("a")
    title = urls.get("title")
    item_url = urls.get("href")
    img = elements.select_one("img")
    img_item = img.get("src")
    for dec in soup.select("div.entry.excerpt p "):
        decs = dec.text
    args.append((title, decs, item_url, img_item ))
       
    print(img_item)

    
    
# """Преренос информации в базу данных"""
  
# con = sqlite3.connect("patterns.sqlite")

# cursor = con.cursor() 

# cursor.executemany(" INSERT INTO patterns VALUES (?,?,?,?)", args )

# con.commit()
# con.close()
