from sense_emu import SenseHat
import time
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
uz_save=[(0,0),(1,0),(2,0),(2,1),(3,1)]
uz_current=[(0,0)]
korisnici={'Mate':uz_save, 'Stipe':[(0,0),(0,1),(0,2),(0,3),(1,3),(2,3)]}
col=0
row=0
sense.set_pixel(uz_save[0][0],uz_save[0][1],G)
save_mode=False
user=2
 
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
                    if uz_new==uz_current:
                        print('Save mod')
                        save_mode=True
                        sense.clear()
                        col=0
                        row=0
                        uz_current.clear()
                        uz_current=[(0,0)]
                    if save_mode:
                        korisnici[user]=uz_current
                        user+=1
                        print(korisnici)
                        save_mode=False
                    else:
                        postoji=False
                        korisnik=None
                        for key,value in korisnici.items():
                            print(value)
                            if value==uz_current:
                                postoji=True
                                korisnik=key
                        if postoji:
                            print('isti su')
                            print(f'Pozdrav {korisnik}')
                            sense.clear(G)
                        else:
                            print('nisu isti')
                            sense.clear(R)
                    time.sleep(1)
                    sense.clear()
                    col=0
                    row=0
                    uz_current.clear()
                    uz_current=[(0,0)]
 
                sense.set_pixel(col,row,G)
 
 
 
 
    print(events)
    print(uz_current)
 
    time.sleep(1)