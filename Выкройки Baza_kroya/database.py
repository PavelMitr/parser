import sqlite3

con = sqlite3.connect("patterns.sqlite")


sql = "CREATE TABLE patterns (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,  description TEXT, url TEXT, image TEXT , path TEXT)"


coursor = con.cursor()
coursor.execute(sql)


con.close()
