import sqlite3

try:
    konekcija = sqlite3.connect('TvrtkaDb.db')
    cursor = konekcija.cursor()
    cursor.execute('SELECT * FROM Employees')
    rows = cursor.fetchall()
    if len(rows) == 0:
        print('Tablica "Employees" je već prazna.')
    
    else:
        cursor.execute('DELETE FROM Employees')
        konekcija.commit()
        print('Podaci uspješno izbrisani.')
    konekcija.close()

except sqlite3.Error as err:
    print("Došlo je do greške prilikom brisanja redaka:", err) #drugačiji način ispisa errora nego pod baze3_write

finally:
       if konekcija:
        konekcija.close()