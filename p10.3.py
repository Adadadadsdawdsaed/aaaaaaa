import sqlite3

connection = sqlite3.connect("baza.sl3", 5)
cur = connection.cursor()
cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")

connection.commit()


res = cur.fetchall()
print(res)
connection.close()
