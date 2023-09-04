import json
import sqlite3

#POCETNE VRIJEDNOSTI



admin = [[2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [3, 0, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [4, 0, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0], [5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 0]] ,
smajlic = [[2, 2, 0], [2, 4, 0], [3, 5, 0], [4, 5, 0], [5, 2, 0], [5, 4, 0]]
    
save_pattern = [[0, 0, 0], [0, 7, 0], [7, 0, 0], [7, 7, 0]]

database = "test"

create_table_query = """
CREATE TABLE IF NOT EXISTS Pattern (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
lock_pattern TEXT NOT NULL UNIQUE
)
"""

insert_query = """
INSERT INTO Pattern (name, lock_pattern)
VALUES (?, ?)
"""

select_query = """
SELECT * FROM Pattern WHERE lock_pattern = ?
"""



jsonadmin = json.dumps(admin)


natragadmin = json.loads(jsonadmin)


try:
    sc = sqlite3.connect(database)
    cursor = sc.cursor()
    cursor.execute(create_table_query)
    #records = cursor.fetchall()

    
    cursor.close()

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    if sc:
        sc.close()
        
izbor = input("1 - unos, 2 - provjera")
if izbor == "1":
    try:
        sc = sqlite3.connect(database)
        cursor = sc.cursor()
        cursor.execute(insert_query,("admin",jsonadmin))
        

        sc.commit()
        cursor.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if sc:
            sc.close()
    
elif izbor == "2":
    try:
        sc = sqlite3.connect(database)
        cursor = sc.cursor()
        cursor.execute(select_query,(jsonadmin,))
        records = cursor.fetchall()
        if not records:
            print("Nema zapisa")
        for record in records:
            print(record)
        cursor.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if sc:
            sc.close()
    
else:
    print("Krivi unos")