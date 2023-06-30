import sqlite3
import os
os.chdir("m3/baze/")

database_name = "TvrtkaDB.db"


select_query = """
SELECT * FROM Employees WHERE email = ?

"""

select_query2 = """
SELECT name, email FROM Employees WHERE email = ?

"""

try:
    sc = sqlite3.connect(database_name)
    cursor = sc.cursor()
    cursor.execute(select_query2, ("ive@net.hr",))
    records = cursor.fetchall()

    for record in records:
        print(record)
    cursor.close()

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    if sc:
        sc.close()
    