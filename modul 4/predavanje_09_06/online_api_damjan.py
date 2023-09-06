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



#index=0  #varijabilno i ovisi o trenutnom datumu
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
fetch_index(data)
datum=data[index]['date']
datum = datetime.strptime(datum, '%Y-%m-%d').strftime('%Y-%m-%d')
print(datum)
mjesec = datum[5:7]
dan = datum[8:10]

print(mjesec,dan)


naziv=data[index]['localName']
#print(naziv)
na_isti_dan=data[index]['fixed']
svjetski_praznik=data[index]['global']

trenutna_lista=0
lista=data
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
            

while True:
    events=sense.stick.get_events()
    if events:
        for event in events:
            if event.action=='pressed':
                if event.direction=='left' and index>0:
                    index-=1
                elif event.direction=='right' and index<(velicina_podataka-1):
                    index+=1
                elif event.direction=='up':
                    trenutna_lista+=1
                    if trenutna_lista==3:
                        trenutna_lista=0
                    if trenutna_lista==0:
                        lista=parse_data()
                        fetch_index(lista)
                        print('Svi')
                    elif trenutna_lista==1:                        
                        lista=parse_data("fixed", True)
                        fetch_index(lista)
                        print('Nepromjenjivi datumi')
                    else:                        
                        lista=parse_data("fixed", False)
                        fetch_index(lista)
                        print('Promjenjivi datumi')

                elif event.direction=='down':
                    trenutna_lista-=1
                    if trenutna_lista==-1:
                        trenutna_lista=2
                    if trenutna_lista==0:
                        lista=parse_data()
                        print('Svi')
                        fetch_index(lista)
                    elif trenutna_lista==1:                        
                        lista=parse_data("fixed", True)
                        print('Nepromjenjivi datumi')
                        fetch_index(lista)
                    else:                        
                        lista=parse_data("fixed", False)
                        print('Promjenjivi datumi')
                        fetch_index(lista)
                elif event.direction=='middle':
                    print(index)
                    print(lista[index]) 
    time.sleep(0.125)