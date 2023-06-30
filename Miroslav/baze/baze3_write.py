#baze3_write

import sqlite3

employee_data = [
        (1, 'Mate Matic', 'mmatic@yahoo.com'),
        (2, 'Stipe Stipic', 'sstipic@yahoo.com'),
        (3, 'Jure Juric', 'jjuric@yahoo.com')
    ]
try:
    konekcija = sqlite3.connect('TvrtkaDb.db')
    cursor = konekcija.cursor()
    cursor.executemany('INSERT INTO Employees (id, name, email) VALUES (?, ?, ?)', employee_data)
    konekcija.commit()
    konekcija.close()
    

except sqlite3.Error as err:
    print(f'Greska {err}')
finally:
    if konekcija:
        konekcija.close()

    



# Potvrda promjena


# Zatvaranje veze s bazom podataka

