from sense_emu import SenseHat#type: ignore
import time
import random

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

#jos 2 boje

colors = [B, R, Y, C, M, O, W, P, Gr, K]

sense.clear(Dg)
time.sleep(2)
curx=0
cury=0

sense.set_pixel(curx,cury,W)

# polje 0,0 ima boju G, istu boju mora imati i 0,1 i 1,0 i 1,1

# 0,1,2,3,4,5,6,7
# 8,9,10,11,12,13,14
# 15,16...
#


prikaz=[]
skriveno=[]
for _ in range(64):
    prikaz.append('')
    skriveno.append(Dg)
    

stanje=[B, R, Y, C, M, O, G, P, B, R, Y, C, M, O, G, P]
random.shuffle(stanje)
print(stanje)
for index,polje in enumerate(stanje):
    #print(index, polje)
    prikaz[(index//4)*16+(index%4)*2]=stanje[index]
    prikaz[(index//4)*16+(index%4)*2+1]=stanje[index]
    prikaz[(index//4)*16+(index%4)*2+8]=stanje[index]
    prikaz[(index//4)*16+(index%4)*2+9]=stanje[index]
    
    
    
#print(prikaz)
    
sense.set_pixels(prikaz)
    
sense.set_pixel(curx,cury,Gr)
eventcounter=0
while True:
    
    events=sense.stick.get_events()
    if events:
        
        exx=curx
        exy=cury
        exindex=2*exy+exx//2
        #rint(exx,exy)
        for event in events:
            if event.action=='pressed':
                if event.direction=='up':
                    cury-=2
                    if cury<0:
                        cury=0
                    #print('Y:',cury)
                    pass
                elif event.direction=='down':
                    cury+=2
                    if cury>6:
                        cury=6
                    #print('Y:',cury)
                    pass
                elif event.direction=='left':
                    curx-=2
                    if curx<0:
                        curx=0
                    #print('X:',curx)
                    pass
                elif event.direction=='right':
                    curx+=2
                    if curx>6:
                        curx=6
                    #print('X:',curx)
                    pass
                elif event.direction=='middle':
                    eventcounter+=1
                    print(exindex)
                    print(eventcounter)
                    if eventcounter==1:
                        #print('usli u prvi')
                        skriveno[(exindex//4)*16+(exindex%4)*2]=stanje[exindex]
                        skriveno[(exindex//4)*16+(exindex%4)*2+1]=stanje[exindex]
                        skriveno[(exindex//4)*16+(exindex%4)*2+8]=stanje[exindex]
                        skriveno[(exindex//4)*16+(exindex%4)*2+9]=stanje[exindex]
                        exexindex=exindex
                        sense.set_pixels(skriveno)
                    else:
                        #print('usli u drugi')
                        skriveno[(exindex//4)*16+(exindex%4)*2]=stanje[exindex]
                        skriveno[(exindex//4)*16+(exindex%4)*2+1]=stanje[exindex]
                        skriveno[(exindex//4)*16+(exindex%4)*2+8]=stanje[exindex]
                        skriveno[(exindex//4)*16+(exindex%4)*2+9]=stanje[exindex]
                        sense.set_pixels(skriveno)
                        time.sleep(2)
                        skriveno[(exindex//4)*16+(exindex%4)*2]=Dg
                        skriveno[(exindex//4)*16+(exindex%4)*2+1]=Dg
                        skriveno[(exindex//4)*16+(exindex%4)*2+8]=Dg
                        skriveno[(exindex//4)*16+(exindex%4)*2+9]=Dg
                        if stanje[exindex]==stanje[exexindex]: #type: ignore
                            skriveno[(exindex//4)*16+(exindex%4)*2]=stanje[exindex]
                            skriveno[(exindex//4)*16+(exindex%4)*2+1]=stanje[exindex]
                            skriveno[(exindex//4)*16+(exindex%4)*2+8]=stanje[exindex]
                            skriveno[(exindex//4)*16+(exindex%4)*2+9]=stanje[exindex]
                            skriveno[(exexindex//4)*16+(exexindex%4)*2]=stanje[exindex] #type: ignore
                            skriveno[(exexindex//4)*16+(exexindex%4)*2+1]=stanje[exindex] #type: ignore
                            skriveno[(exexindex//4)*16+(exexindex%4)*2+8]=stanje[exindex] #type: ignore
                            skriveno[(exexindex//4)*16+(exexindex%4)*2+9]=stanje[exindex] #type: ignore
                            print('isti su')
                        else:
                            exindex=exexindex #type: ignore
                            skriveno[(exindex//4)*16+(exindex%4)*2]=Dg
                            skriveno[(exindex//4)*16+(exindex%4)*2+1]=Dg
                            skriveno[(exindex//4)*16+(exindex%4)*2+8]=Dg
                            skriveno[(exindex//4)*16+(exindex%4)*2+9]=Dg
                        sense.set_pixels(skriveno)
                        eventcounter=0
                    pass
                
        if exx!=curx or exy!=cury:
            #sense.set_pixel(exx,exy,boje[1])
            sense.clear()
            sense.set_pixels(skriveno)
            sense.set_pixel(curx,cury,Gr) 