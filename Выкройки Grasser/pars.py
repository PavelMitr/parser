# pip install BeautifulSoup4 lxml

from bs4 import BeautifulSoup as BS
import requests
import sqlite3

url = "https://grasser.ru/vykrojki/besplatnye-vykrojki"

req = requests.get(url)

soup = BS(req.content, "lxml")


"""Описание выкройки и ссылка на неё"""

args = []

html = soup.select("div.catalog-three div.catalog__info a ")

for elements in html:
    item_url = elements.get("href")
    for img in soup.select("div.catalog-three__block img"):
        img_item = img.get("src")
        p = f"https://grasser.ru{img_item}"
    el_text = elements.text.split(",", 2)
    el_text = elements.text.strip()
    name = el_text.split(",")
    dec = name[-1]
    name1 = name[0]
    url = f"https://grasser.ru{item_url}"
    args.append((name1, dec, url, p ))
    print(p)
    
"""Преренос информации в базу данных"""
  
# con = sqlite3.connect("patterns.sqlite")

# cursor = con.cursor() 

# cursor.executemany(" INSERT INTO patterns VALUES (?,?,?,?)", args )

# con.commit()
# con.close()
