import sqlite3

connection = sqlite3.connect("baza.sl3", 5)
cur = connection.cursor()
cur.execute("UPDATE first_table SET name='LOX' WHERE rowid=4;")

connection.commit()

connection.close()
