import sqlite3

con = sqlite3.connect("patterns.sqlite")

sql = "CREATE TABLE patterns (name TEXT,  description TEXT, url TEXT, image TEXT)"

coursor = con.cursor()

coursor.execute(sql)

con.close()