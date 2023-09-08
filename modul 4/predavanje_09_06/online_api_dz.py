from sense_emu import SenseHat
import time
import requests
import json
from datetime import datetime

current_date = datetime.now()
str_current_date = current_date.strftime('%Y-%m-%d')
#print(str_current_date)

current_month = int(str_current_date[5:7])
current_day = int(str_current_date[8:10])

#print(current_month,current_day)

sense = SenseHat()

R=(255,0,0)
G=(0,255,0)
B=(0,0,255)
W=(255,255,255)
K=(0,0,0)

url='https://date.nager.at/api/v3/PublicHolidays/2023/HR'

response=requests.get(url)

#print(type(response.text))

data=json.loads(response.text)
#print(type(data))
#print(data)



index=0  #varijabilno i ovisi o trenutnom datumu
def fetch_index(data_list:list):
    global index
    for index, praznik in enumerate(data_list):
        mjesec = int(praznik["date"][5:7])
        dan = int(praznik["date"][8:10])
        #print(mjesec, dan)
        if current_month > mjesec:
            continue
        else:
            if current_month < mjesec:
                
                print("sljedeci praznik: ", dan,mjesec)
                break
            else:
                if dan >= current_day:
                    print("sljedeci praznik: ", dan,mjesec)
                    break

datum=data[index]['date']
datum = datetime.strptime(datum, '%Y-%m-%d').strftime('%Y-%m-%d')
print(datum)
#mjesec = datum[5:7]
#dan = datum[8:10]

#print(mjesec,dan)


naziv=data[index]['localName']
#print(naziv)
na_isti_dan=data[index]['fixed']
svjetski_praznik=data[index]['global']


velicina_podataka=len(data)
def parse_data(kljuc=None, vrijednost=None) -> list:
    global data, velicina_podataka
    temp_list = []
    if kljuc != None and vrijednost !=None:
        for element in data:
            if element[kljuc] == vrijednost:
                temp_list.append(element)
            else:
                pass
    else:
        velicina_podataka = len(data)
        return data
    velicina_podataka = len(temp_list)
    return temp_list
 
def filter_data(global_filter:int, fixed_filter:int) -> list:
    global_filter_values = [None,True,False]    
    fixed_filter_values = [None,True,False]
    
    if global_filter != 0:
        temp_list = parse_data("global", global_filter_values[global_filter])
    else:
        temp_list = parse_data()
        
    if fixed_filter != 0:
        temp_list = parse_data("fixed", fixed_filter_values[fixed_filter])
    else:
        temp_list = parse_data()
     
    return temp_list

def ispis(lista:list)-> None:
    for praznik in lista:
        print(f"{praznik['date']} {praznik['name']}")
    print("-"*50,"\n")

lista=data
global_local = 0
GL_text = ["Globalni i lokalni praznici","Samo globalni praznici","Samo lokalni praznici"]
fix_nonfix = 0
FNF_text = ["sa fiksnim i ne fiksnim datumima:","sa fiksnim datumima:","sa ne fiksnim datumima:"]

print(f"{GL_text[global_local]} {FNF_text[fix_nonfix]}")

while True:
    events=sense.stick.get_events()
    if events:
        for event in events:
            if event.action=='pressed':
                if event.direction=='left' and fix_nonfix>0:
                    fix_nonfix-=1
                    print(f"{GL_text[global_local]} {FNF_text[fix_nonfix]}")
                    
                elif event.direction=='right' and fix_nonfix<2:
                    fix_nonfix+=1
                    print(f"{GL_text[global_local]} {FNF_text[fix_nonfix]}")
                    
                elif event.direction=='up' and global_local>0:
                    global_local -= 1
                    print(f"{GL_text[global_local]} {FNF_text[fix_nonfix]}")    

                elif event.direction=='down' and global_local<2:
                    global_local += 1
                    print(f"{GL_text[global_local]} {FNF_text[fix_nonfix]}")    
                    
                elif event.direction=='middle':
                    lista = filter_data(global_local, fix_nonfix)
                    ispis(lista)
                    
    time.sleep(0.125)







