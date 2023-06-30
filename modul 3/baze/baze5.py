import sqlite3
import os
os.chdir("m3/baze/")

database_name = "TvrtkaDB.db"

update_query = """
UPDATE Employees 
SET name = ?
WHERE email = ?


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
        cursor.execute(update_query, ("Ivana Ivanovic-Krolo","ive@net.hr"))

    sc.commit()
    cursor.close()
    
except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    sc.close()