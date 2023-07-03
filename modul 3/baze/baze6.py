import sqlite3
import os
os.chdir("modul 3/baze/")

database_name = "TvrtkaDB.db"


delete_query = """
DELETE FROM Employees WHERE id = ?

"""
try:
    sc = sqlite3.connect(database_name)
    cursor = sc.cursor()
    cursor.execute(delete_query, ("4"))
    records = cursor.fetchall()

    for record in records:
        print(record)
    cursor.close()

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    if sc:
        sc.close()
    