import sqlite3
import os
os.chdir("m3/baze/")

select_query = "SELECT sqlite_version();"
print(select_query)

try:
    sqliteConnection = sqlite3.connect("SQLite_Python.db")
    cursor = sqliteConnection.cursor()
    print("Veza je uspostavljena!")

    cursor.execute(select_query)
    records = cursor.fetchall()

    print(f"SQLite verzija je: {records}")

    cursor.close()
    print("Resursi cursora su otpušteni!")

except sqlite3.Error as e:
    print(f"Database error: {e}")

else:
    pass

finally:
    if sqliteConnection: 
        cursor.close()
        sqliteConnection.close()
        print("SQLite veza je zatvorena")

