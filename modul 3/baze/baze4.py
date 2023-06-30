import sqlite3
import os
os.chdir("m3/baze/")

database_name = "TvrtkaDB.db"


select_query = """
SELECT * FROM Employees

"""
try:
    sc = sqlite3.connect(database_name)
    cursor = sc.cursor()
    cursor.execute(select_query)
    records = cursor.fetchall()

    for record in records:
        print(record)
    cursor.close()

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    if sc:
        sc.close()
    