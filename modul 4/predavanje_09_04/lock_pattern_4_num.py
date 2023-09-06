from sense_emu import SenseHat  #type:ignore
import time
#import json
import sqlite3

def convert_to_num(pattern_list:list):
    total = 0
    num = 0
    for broj, coord in enumerate(pattern_list):
        num = (coord[1]*8+coord[0])+(broj*64)
        total += num
    return total


database='uzoraknum.db'
 
create_table='''CREATE TABLE IF NOT EXISTS Uzorak (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
pattern TEXT NOT NULL UNIQUE);'''
 
insert_into_table='''INSERT INTO Uzorak (name, pattern) VALUES (?, ?)'''
 
select_pattern='''SELECT * FROM Uzorak WHERE pattern=?'''

delete_pattern='''DELETE FROM Uzorak WHERE pattern=?'''

update_pattern = """
UPDATE Uzorak 
SET pattern = ?
WHERE pattern = ?
"""

 
try:
    sc=sqlite3.connect(database)
    cursor=sc.cursor()
    cursor.execute(create_table)
    sc.commit()
    cursor.close()
except sqlite3.Error as err:
    print('Greska')
finally:
    if sc: #type:ignore
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
edit_mode = False
modify_mode=False
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
                        uz_current.append((col,row)) #type:ignore
                elif event.direction=='right':
                    col+=1
                    if col==8:
                        col=7
                    else:
                        uz_current.append((col,row)) #type:ignore
                elif event.direction=='up':
                    row-=1
                    if row==-1:
                        row=0
                    else:
                        uz_current.append((col,row)) #type:ignore
                elif event.direction=='down':
                    row+=1
                    if row==8:
                        row=7
                    else:
                        uz_current.append((col,row)) #type:ignore
                elif event.direction=='middle':
                    if save_mode:
                        conv_pattern=convert_to_num(uz_current)
                        username='user'+str(user)
                        try:
                            sc=sqlite3.connect(database)
                            cursor=sc.cursor()
                            cursor.execute(insert_into_table, (username,conv_pattern))
                            sc.commit()
                            cursor.close()
                        except sqlite3.Error as err:
                            error = str(err)
                            if error == "UNIQUE constraint failed: Uzorak.pattern":
                                save_mode=False
                                edit_mode = True
                                print("Pomaknite pokazivac lijevo za brisanje uzorka, ili lijevo za uredivanje!")
                            else:
                                print('Greska')
                        finally:
                            if sc: #type:ignore
                                sc.close()
                        user+=1
                        save_mode=False
                    elif edit_mode:
                        print(edit_mode)
                        print(uz_current)
                        ###DELETE####
                        if uz_current == [(3,3),(2,3)]:
                            print("delete")
                            try:
                                sc=sqlite3.connect(database)
                                cursor=sc.cursor()
                                cursor.execute(delete_pattern, (conv_pattern,)) #type:ignore
                                sc.commit()
                                cursor.close()
                            except sqlite3.Error as err:
                                print('Greska')
                            finally:
                                if sc: #type:ignore
                                    sc.close()
                            
                            edit_mode = False
                        ###MODIFY####
                        elif uz_current == [(3,3),(4,3)]:
                            print("edit")
                            modify_mode=True
                            
                            edit_mode = False
                        else:
                            print("Edit error")
                            edit_mode = False 
                        
                        
                    elif modify_mode:
                        
                        
                        new_pattern = convert_to_num(uz_current)
                        try:
                            sc=sqlite3.connect(database)
                            cursor=sc.cursor()
                            cursor.execute(update_pattern, (new_pattern,conv_pattern,)) #type:ignore
                            sc.commit()
                            cursor.close()
                        except sqlite3.Error as err:
                            print('Greska')
                        finally:
                            if sc: #type:ignore
                                sc.close()
                        modify_mode = False
                        
                    else:
                        postoji=False
                        korisnik=None
                        conv_pattern=convert_to_num(uz_current)
                        try:
                            sc=sqlite3.connect(database)
                            cursor=sc.cursor()
                            cursor.execute(select_pattern, (conv_pattern,))
                            records=cursor.fetchall()
                            if not records:
                                postoji=False
                            for record in records:
                                postoji=True
                            cursor.close()
                        except sqlite3.Error as err:
                            print('Greska')
                        finally:
                            if sc: #type:ignore
                                sc.close()
                        if postoji and not modify_mode:
                            print('Dopusten ulaz')
                            print(records) #type:ignore
                            sense.clear(G)
                        else:
                            print('Ulaz zabranjen')
                            sense.clear(R)
                    if edit_mode:
                        
                        print('Edit mod')
                        sense.clear()
                        col=3
                        row=3
                        uz_current.clear()
                        uz_current=[(3,3)]
                        
                    elif uz_new==uz_current:
                        print('Save mod')
                        save_mode=True
                        sense.clear()
                        col=0
                        row=0
                        uz_current.clear()
                        uz_current=[(0,0)]
                    elif modify_mode:
                        print('Modify mod')
                        sense.clear()
                        col=0
                        row=0
                        uz_current.clear()
                        uz_current=[(0,0)]
                        
                    else:
                        col=0
                        row=0
                        #uz_current.clear()
                        uz_current=[(0,0)]
                        
                    time.sleep(1)
                    sense.clear()
                    
 
          
                sense.set_pixel(col,row,G)
 
 
 
 
 
    time.sleep(1)
 
