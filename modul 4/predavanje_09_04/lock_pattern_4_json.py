from sense_emu import SenseHat
import time
import json
import sqlite3
 
database='uzorakjson.db'
 
create_table='''CREATE TABLE IF NOT EXISTS Uzorak (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
pattern TEXT NOT NULL);'''
 
insert_into_table='''INSERT INTO Uzorak (name, pattern) VALUES (?, ?)'''
 
select_pattern='''SELECT * FROM Uzorak WHERE pattern=?'''
 
try:
    sc=sqlite3.connect(database)
    cursor=sc.cursor()
    cursor.execute(create_table)
    sc.commit()
    cursor.close()
except sqlite3.Error as err:
    print('Greska')
finally:
    if sc:
        sc.close()
 
sense = SenseHat()
 
R=(255,0,0)
G=(0,255,0)
B=(0,0,255)
W=(255,255,255)
K=(0,0,0)
 
lock=[
    K, K, G, G, G, G, K, K, 
    K, K, G, K, K, G, K, K,
    K, K, G, K, K, G, K, K,
    K, K, G, G, G, G, K, K,
    K, K, G, G, G, G, K, K, 
    K, K, G, G, G, G, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,   
    ]
 
sense.clear()
 
uz_new=[(0,0),(1,0),(1,1),(0,1),(0,0)]
uz_current=[(0,0)]
 
col=0
row=0
sense.set_pixel(0,0,G)
save_mode=False
user=0
 
while True:
    #sense.clear()
    events=sense.stick.get_events()
    if events:
        for event in events:
            if event.action=='pressed':
                if event.direction=='left':
                    col-=1
                    if col==-1:
                        col=0
                    else:
                        uz_current.append((col,row))
                elif event.direction=='right':
                    col+=1
                    if col==8:
                        col=7
                    else:
                        uz_current.append((col,row))
                elif event.direction=='up':
                    row-=1
                    if row==-1:
                        row=0
                    else:
                        uz_current.append((col,row))
                elif event.direction=='down':
                    row+=1
                    if row==8:
                        row=7
                    else:
                        uz_current.append((col,row))
                elif event.direction=='middle':
 
                    if save_mode:
                        jsonstring=json.dumps(uz_current)
                        username='user'+str(user)
                        try:
                            sc=sqlite3.connect(database)
                            cursor=sc.cursor()
                            cursor.execute(insert_into_table, (username,jsonstring))
                            sc.commit()
                            cursor.close()
                        except sqlite3.Error as err:
                            print('Greska')
                        finally:
                            if sc:
                                sc.close()
 
                        user+=1
                        save_mode=False
 
                    else:
                        postoji=False
                        korisnik=None
                        jsonstring=json.dumps(uz_current)
                        try:
                            sc=sqlite3.connect(database)
                            cursor=sc.cursor()
                            cursor.execute(select_pattern, (jsonstring,))
                            records=cursor.fetchall()
                            if not records:
                                postoji=False
                            for record in records:
                                postoji=True
                            cursor.close()
                        except sqlite3.Error as err:
                            print('Greska')
                        finally:
                            if sc:
                                sc.close()
                        if postoji:
                            print('Dopusten ulaz')
                            sense.clear(G)
                        else:
                            print('Ulaz zabranjen')
                            sense.clear(R)
                    if uz_new==uz_current:
                        print('Save mod')
                        save_mode=True
                        sense.clear()
                        col=0
                        row=0
                        uz_current.clear()
                        uz_current=[(0,0)]
                    time.sleep(1)
                    sense.clear()
                    col=0
                    row=0
                    #uz_current.clear()
                    uz_current=[(0,0)]
 
                sense.set_pixel(col,row,G)
 
 
 
 
 
    time.sleep(1)
 
 