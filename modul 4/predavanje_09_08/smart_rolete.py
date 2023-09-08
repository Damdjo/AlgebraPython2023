from sense_emu import SenseHat
from time import sleep
import tkinter as tk
sense = SenseHat()

def draw_roleta(roleta:list,broj_redova:int=8,boja:tuple=(0,255,255)):
    for index_reda,red in enumerate(roleta):
        if index_reda < broj_redova:
            for pixel in red:
                sense.set_pixel(pixel[0],pixel[1],(139,69,19))            
        else:
            for pixel in red:
                sense.set_pixel(pixel[0],pixel[1],(0,255,255))

def check_movement(roleta_data:list):
    if roleta_data[0]:
        if roleta_data[1] == "up" and roleta_data[2] > 0:
            roleta_data[2] -= 1
        if roleta_data[1] == "down" and roleta_data[2] < 8:
            roleta_data[2] += 1



def main():
    selected = 0
    boje = {
        "red" : (255,0,0),
        "green" : (0,255,0),
        "blue" : (0,0,255),
        "zuta" : (255,200,0),
        "cyan" : (0,255,255),
        "magenta" : (255,0,255),
        "orange" : (255,122,56),
        "tan" : (200,255,134),
        "brown" : (139,69,19)
        }

    #fill l_roleta
    l_roleta = []
    for red in range(8):
        lista = []
        for stupac in range(4):
            lista.append((stupac,red))
        l_roleta.append(lista)
        
    #fill d_roleta
    r_roleta = []
    for red in range(8):
        lista = []
        for stupac in range(4,8):
            lista.append((stupac,red))
        r_roleta.append(lista)

    print(l_roleta)
    print(r_roleta)

    l_roleta_stats = [False, "down",8]
    r_roleta_stats = [False, "down",0]
    
    sense.clear()
    while True:
        
        for event in sense.stick.get_events():
            if event.action == "pressed":
                ####GORE
                if event.direction == "up" and selected == 0:
                    if l_roleta_stats[0]:
                        l_roleta_stats[0],l_roleta_stats[1] = False, "up"
                    else:
                        l_roleta_stats[0],l_roleta_stats[1] = True, "up"
                elif event.direction == "up" and selected == 1:
                    if r_roleta_stats[0]:
                        r_roleta_stats[0],r_roleta_stats[1] = False, "up"
                    else:
                        r_roleta_stats[0],r_roleta_stats[1] = True, "up"
                ###DOLJE    
                if event.direction == "down" and selected == 0:
                    if l_roleta_stats[0]:
                        l_roleta_stats[0],l_roleta_stats[1] = False, "down"
                    else:
                        l_roleta_stats[0],l_roleta_stats[1] = True, "down"
                elif event.direction == "down" and selected == 1:
                    if r_roleta_stats[0]:
                        r_roleta_stats[0],r_roleta_stats[1] = False, "down"
                    else:
                        r_roleta_stats[0],r_roleta_stats[1] = True, "down"
                    
                elif event.direction == "left" and selected!= 0:
                    selected -= 1
                    print(selected)
                    
                elif event.direction == "right" and selected!= 1:
                    selected += 1
                    print(selected)
                    
                elif event.direction == "middle":
                    l_roleta_stats[0],l_roleta_stats[1] = False, "down"
                    r_roleta_stats[0],r_roleta_stats[1] = False, "down"
                    
            
        print(f"L:{l_roleta_stats}, D:{r_roleta_stats}")
        check_movement(l_roleta_stats)
        check_movement(r_roleta_stats)
        draw_roleta(l_roleta,l_roleta_stats[2],(139,69,19))        
        draw_roleta(r_roleta,r_roleta_stats[2],(139,69,19))
        sleep(0.5)

main()

