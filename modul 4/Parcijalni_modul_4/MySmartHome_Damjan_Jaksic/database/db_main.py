import sqlite3
import datetime as dt
from datetime import datetime


database='database/sensor_data_database.db'
 
create_table='''CREATE TABLE IF NOT EXISTS SensorData (
id INTEGER PRIMARY KEY,
time TEXT NOT NULL,
type TEXT NOT NULL,
temp TEXT NOT NULL,
humidity TEXT NOT NULL,
pressure TEXT NOT NULL);'''
 
insert_into_table='''INSERT INTO SensorData (time, type, temp, humidity, pressure) VALUES (?, ?, ?, ?, ?)'''
 
select_pattern='''SELECT * FROM SensorData'''

delete_pattern='''DELETE FROM SensorData WHERE id=?'''

update_pattern = """
UPDATE SensorData 
SET time = ?
WHERE time = ?
"""




def insert_sensor_data(sensor_type, temp, humidity, pressure):
    time = datetime.now()
    try:
        sc=sqlite3.connect(database)
        cursor=sc.cursor()
        cursor.execute(insert_into_table, (time, sensor_type, temp, humidity, pressure))
        sc.commit()
        cursor.close()
    except sqlite3.Error as err:
        print('Greska: ',err)
    finally:
        if sc:
            sc.close()
            
            
def main():
    database='sensor_data_database.db'
    try:
        sc=sqlite3.connect(database)
        cursor=sc.cursor()
        cursor.execute(select_pattern)
        records=cursor.fetchall()
        if not records:
            postoji=False
        for record in records:
            print(record)
        cursor.close()
        cursor.close()
    except sqlite3.Error as err:
        print('Greska: ',err)
    finally:
        print("success")
        if sc:
            sc.close()
def show_data():
    try:
        sc=sqlite3.connect(database)
        cursor=sc.cursor()
        cursor.execute(select_pattern)
        records=cursor.fetchall()
        if not records:
            postoji=False
        for record in records:
            print(record)
        cursor.close()
        cursor.close()
    except sqlite3.Error as err:
        print('Greska: ',err)
    finally:
        if sc:
            sc.close()

if __name__ == "__main__":
    main()