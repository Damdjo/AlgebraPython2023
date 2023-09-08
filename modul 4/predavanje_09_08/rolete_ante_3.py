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
left=True
 
def rolete(rol1,rol2,left):
    for index in range(64):
        row=index//8
        rowstart=row*8
        if rowstart==0:
            col=index
        else:
            col=index%rowstart
        #print(index, row, rowstart, col)
        if col==3:
            if left:
                prozori[index]=G
            else:
                prozori[index]=Dg
        if col==4:
            if left:
                prozori[index]=Dg
            else:
                prozori[index]=G
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
    sense.set_pixels(prozori)
 
 
 
 
rolete(rol1,rol2,True)
sense.set_pixels(prozori)
stst1=False
stst2=False
xrol1=rol1
xrol2=rol2
 
while True:
    #sense.clear()
    #xrol1=rol1
    #xrol2=rol2
    events=sense.stick.get_events()
    if events:
        print('event')
        for event in events:
            if event.action=='pressed':
                if event.direction=='left':
                    rol1active=True
                    rol2active=False
                    left=True
                    stst1=False
                    stst2=False
                    rolete(rol1,rol2,left)
                elif event.direction=='right':
                    rol1active=False
                    rol2active=True
                    left=False
                    stst1=False
                    stst2=False
                    rolete(rol1,rol2,left)
                elif event.direction=='up':
                    if rol1active:
                        stst1 = not stst1
                    if rol2active:
                        stst2 = not stst2
                    if rol1active and rol1>-1:
                        rol1-=1
                    if rol2active and rol2>-1:
                        rol2-=1
                elif event.direction=='down':
                    if rol1active:
                        stst1 = not stst1
                    if rol2active:
                        stst2 = not stst2
                    if rol1active and rol1<7:
                        rol1+=1
                    if rol2active and rol2<7:
                        rol2+=1    
                elif event.direction=='middle':
                    pass
    if xrol1==rol1 and xrol2==rol2:
        continue
    if stst1 and xrol1>rol1:
        rolete(rol1,rol2,left)
        time.sleep(1)
        xrol1=rol1
        rol1-=1
    if stst1 and xrol1<rol1:
        rolete(rol1,rol2,left)
        time.sleep(1)
        xrol1=rol1
        rol1+=1
    if stst2 and xrol2>rol2:
        rolete(rol1,rol2,left)
        time.sleep(1)
        xrol2=rol2
        rol2-=1
    if stst2 and xrol2<rol2:
        rolete(rol1,rol2,left)
        time.sleep(1)
        xrol2=rol2
        rol2+=1
 
 
 
    #rolete(rol1,rol2,left)
    #sense.set_pixels(prozori)
    time.sleep(0.5)
 
 
 
 
 
 
 
 
 
 
 
 