import sqlite3

connection = sqlite3.connect("baza.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Vasya');")
connection.commit()
connection.close()

