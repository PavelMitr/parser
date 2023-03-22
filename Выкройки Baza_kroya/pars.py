# pip install BeautifulSoup4 lxml

from bs4 import BeautifulSoup as BS
import requests
import sqlite3

url = "https://baza-kroya.ru/?brands=burda"

req = requests.get(url)

soup = BS(req.content, "lxml")


"""Описание выкройки и ссылка на неё"""
# print(soup)
args = []

html = soup.select("div.pattern-card")

for elements in html:
    urls = elements.select_one("a")
    item_url = urls.get("href")
    img = urls.select_one("img")
    img_item = img.get("data-src")
    name = img.get("alt")
    el_text = name.split("-", 2)
    dec = el_text[-1]
    name1 = el_text[0]
    
    args.append((name1, dec, item_url, img_item ))
    
    print(dec)
    
# a = /home/compasspro1/Рабочий стол/python_work1/Parsing/Выкройки Baza_kroya/download
"""Преренос информации в базу данных"""
  
con = sqlite3.connect("patterns.sqlite")

cursor = con.cursor() 

cursor.executemany(" INSERT INTO pattern VALUES (?,?,?,?)", args )

con.commit()
con.close()
