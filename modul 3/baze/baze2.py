import sqlite3
import os
os.chdir("m3/baze/")

create_table_query = """

CREATE TABLE IF NOT EXISTS Employees (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE
);

"""

database_name = "TvrtkaDB.db"

try:
    sc = sqlite3.connect(database_name)
    cursor = sc.cursor()
    print("Veza je uspostavljena!")

    cursor.execute(create_table_query)
    sc.commit()
    cursor.close()

except sqlite3.Error as e:
    print(f"Database error: {e}")

else:
    pass

finally:
    if sc:
        sc.close()
