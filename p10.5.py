import sqlite3

connection = sqlite3.connect("baza.sl3", 5)
cur = connection.cursor()
cur.execute("DELETE FROM first_table WHERE rowid=7;")

connection.commit()

connection.close()
