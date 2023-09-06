from sense_emu import SenseHat
import time
import requests
import json
from datetime import datetime
 
current_date=datetime.now()
#print(type(current_date))
str_current_date=current_date.strftime("%Y-%m-%d")
print(str_current_date)
str_current_month=int(current_date.strftime("%m"))
str_current_day=int(current_date.strftime("%d"))
print(str_current_month, str_current_day) #dvije varijable koje sadrze brojke za mjesec i trenutni dan
 
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
 
velicina_podataka=len(data)
 
 
for indeks,praznik in enumerate(data):
    #print(praznik['date'])
    mjesec=int(praznik['date'][5:7])
    dan=int(praznik['date'][8:10])
 
    if str_current_month>mjesec:
        continue
    else:
        if mjesec>str_current_month:
            print('Sljedeci: ',dan,mjesec)
            break
        else:
            if dan>=str_current_day:
                print('Sljedeci: ',dan,mjesec)
                break
            else:
                continue
print(indeks) 
 
'''
0-sve, 1-fix. 2-non-fix (sve za global/local)
3-sve, 4-fix, 5-non-fix (samo global)
6-sve, 7-fix, 8-non-fix (samo local)
 
+-1(0-2) -> joystick up
+-3*(0-2) -> joystick down
 
score = up+3*down
 
 
'''
 
while True:
    events=sense.stick.get_events()
    if events:
        for event in events:
            if event.action=='pressed':
                if event.direction=='left' and indeks>0:
                    indeks-=1
                elif event.direction=='right' and indeks<(velicina_podataka-1):
                    indeks+=1
                elif event.direction=='up':
                    trenutna_lista+=1
                    if trenutna_lista==3:
                        trenutna_lista=0
                    if trenutna_lista==0:
                        lista=data
                        print('Svi:')
                        for indeks,praznik in enumerate(lista):
                            #print(praznik['date'])
                            mjesec=int(praznik['date'][5:7])
                            dan=int(praznik['date'][8:10])
 
                            if str_current_month>mjesec:
                                continue
                            else:
                                if mjesec>str_current_month:
                                    print('Sljedeci: ',dan,mjesec)
                                    break
                                else:
                                    if dan>=str_current_day:
                                        print('Sljedeci: ',dan,mjesec)
                                        break
                                    else:
                                        continue
                    elif trenutna_lista==1:
                        lista=fixeddata
                        print('Nepromjenjivi datumi')
                        for indeks,praznik in enumerate(lista):
                            #print(praznik['date'])
                            mjesec=int(praznik['date'][5:7])
                            dan=int(praznik['date'][8:10])
 
                            if str_current_month>mjesec:
                                continue
                            else:
                                if mjesec>str_current_month:
                                    print('Sljedeci: ',dan,mjesec)
                                    break
                                else:
                                    if dan>=str_current_day:
                                        print('Sljedeci: ',dan,mjesec)
                                        break
                                    else:
                                        continue
 
 
 
                    else:
                        lista=nonfixeddata
                        print('Promjenjivi datumi')
                        for indeks,praznik in enumerate(lista):
                            #print(praznik['date'])
                            mjesec=int(praznik['date'][5:7])
                            dan=int(praznik['date'][8:10])
 
                            if str_current_month>mjesec:
                                continue
                            else:
                                if mjesec>str_current_month:
                                    print('Sljedeci: ',dan,mjesec)
                                    break
                                else:
                                    if dan>=str_current_day:
                                        print('Sljedeci: ',dan,mjesec)
                                        break
                                    else:
                                        continue
 
                elif event.direction=='down':
                    pass
                elif event.direction=='middle':
                    print(data[indeks]['date'])
                    sense.show_message(data[indeks]['localName'])
                    sense.show_message(data[indeks]['date'])
    time.sleep(1)