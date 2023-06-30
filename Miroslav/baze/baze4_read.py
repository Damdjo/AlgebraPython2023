import sqlite3

try:
    konekcija = sqlite3.connect('TvrtkaDb.db')
    cursor = konekcija.cursor()
    cursor.execute('SELECT * FROM Employees')
    baza = cursor.fetchall()
    for zapis in baza:
        print(zapis)

except sqlite3.Error as err:
    print(f'Greška pri izčitavnju podataka {err}')

finally:
    if konekcija:
        konekcija.close()