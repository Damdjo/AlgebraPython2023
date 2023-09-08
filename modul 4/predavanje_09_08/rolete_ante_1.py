'''
na sensehat, lijeva polovica-lijeva roleta, desna-desna roleta
upravljanje l-r pomocu l-r joysticka
upravljanje u-d pomocu u-d joysticka
middle-all stop
pritisak na istu tipku start-stop, znaci ide npr. up, krece se red po red na displeyu,
i na istu tipku mozemo stati
postoje razine rolete od 0 do 8, 0 je skroz otvoreno, 8 je skroz spustena (gore sve led)
 
tkinter
napraviti app koja ce "komunicirati" sa raspijem (sensehat) i omoguciti da upravljamo roletama
na jednak nacin kao i na fizickom modulu
razlika: svaka roleta ima svoja dva botuna (u-d)
dodati botun Auto koji ce uzimati u obzir vrijeme dana (zora, vrijeme ustajanja, sumrak) i obveze
npr. odlazak na posao radnim danom, duze spavanje vikendom
'''
 
from sense_emu import SenseHat
import time
import requests
import json
from datetime import datetime
 
sense=SenseHat()
B = (0,0,255)
R = (255,0,0)
G = (0,255,0)
Y = (255,255,0)
C = (0,255,255)
M = (255,0,255)
O = (66, 245, 147)#(255,122,56)
W = (255, 255, 255)
K = (0, 0, 0)
P = (42,98,61)#(160, 32, 240)
Gr = (190, 190, 190)
Dg = (40, 40, 40)
Br=(146, 87, 76)
Br2=(139,69,19)
 
prozori=[
    Br, Br, Br, G, Dg, Br, Br, Br,
    Br, Br, Br, G, Dg, Br, Br, Br,
    Br, Br, Br, G, Dg, Br, Br, Br,
    Br, Br, Br, G, Dg, Br, Br, Br,
    Br, Br, Br, G, Dg, Br, Br, Br,
    Br, Br, Br, G, Dg, Br, Br, Br,
    Br, Br, Br, G, Dg, Br, Br, Br,
    C, C, C, G, Dg, C, C, C
    ]
 
sense.set_pixels(prozori)
 
r1apr2=[Br, Br, Br, G, Dg, Br, Br, Br]
r1par2=[Br, Br, Br, Dg, G, Br, Br, Br]
 
rol1=4 #polozaj rolete 1 -> -1 je otvoreno, 7 je potpuno spusteno
rol2=2 #polozaj rolete 2 -> -1 je otvoreno, 7 je potpuno spusteno
 
rol1active=True #po defaultu je rol1 aktivna
rol2active=False #po defaultu je rol2 pasivna
 
def rolete(rol1,rol2):
    for index in range(64):
        row=index//8
        rowstart=row*8
        if rowstart==0:
            col=index
        else:
            col=index%rowstart
        #print(index, row, rowstart, col)
        '''0-2 rol1, 5-7 rol2'''
        if col<3:
            #sense.set_pixel(col, row, C) #za test
            #prozori[index]=C
            if rol1==-1:
                prozori[index]=C
            elif row<=rol1:
                prozori[index]=Br
            else:
                prozori[index]=C
        if col>4:
            #sense.set_pixel(col, row, C) #za test
            #prozori[index]=C
            if rol2==-1:
                prozori[index]=C
            elif row<=rol2:
                prozori[index]=Br
            else:
                prozori[index]=C
 
 
rolete(rol1,rol2)
sense.set_pixels(prozori)
 
 
while True:
    #sense.clear()
    events=sense.stick.get_events()
    if events:
        for event in events:
            if event.action=='pressed':
                if event.direction=='left':
                    pass
                elif event.direction=='right':
                    pass
                elif event.direction=='up':
                    if rol1active and rol1>-1:
                        rol1-=1
                    if rol2active and rol2>-1:
                        rol2-=1
                elif event.direction=='down':
                    if rol1active and rol1<7:
                        rol1+=1
                    if rol2active and rol2<7:
                        rol2+=1    
                elif event.direction=='middle':
                    pass
    rolete(rol1,rol2)
    sense.set_pixels(prozori)
    time.sleep(0.5)
 
 
 
 
 
 
 
 