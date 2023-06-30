import sqlite3
import os
os.chdir("m3/baze/")

database_name = "TvrtkaDB.db"

insert_query = """
INSERT INTO employees (name, email)
VALUES (?, ?)


"""

lista_djelatnika = [
("Mate Matic","mmatic@alg.hr"),
("Jure Juric", "jjuric@brzi.hr"),
("Ivana Ivanovic", "ive@net.hr")

]

try:
    sc = sqlite3.connect(database_name)
    cursor = sc.cursor()
    for djelatnik in lista_djelatnika:
        cursor.execute(insert_query, djelatnik)

    sc.commit()
    cursor.close()
    
except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    sc.close()