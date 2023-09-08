from sense_emu import SenseHat
from time import sleep
import tkinter as tk
import threading
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

def button_press(koja_roleta,smjer):
    if smjer == "gore":
        if koja_roleta[0]:
            koja_roleta[0],koja_roleta[1] = False, "up"
        else:
            koja_roleta[0],koja_roleta[1] = True, "up"
    elif smjer == "dolje":
        if koja_roleta[0]:
            koja_roleta[0],koja_roleta[1] = False, "down"
        else:
            koja_roleta[0],koja_roleta[1] = True, "down"

def full_stop(koja_roleta):
    if koja_roleta == "lijeva":
        l_roleta_stats[0],l_roleta_stats[1] = False, "down"
    elif koja_roleta == "desna":
        r_roleta_stats[0],r_roleta_stats[1] = False, "down"
    else:
        pass

def main_gui():
    #dio za GUI
    root = tk.Tk()

    root.title("Rolete")
    root.geometry("600x200")
    root.columnconfigure(0, weight = 1)
    
    root.columnconfigure(1, weight = 1)
    
    left_window_frame = tk.Frame(root, width = 300, height = 100, background = "Red", padx = 30, pady = 20)
    left_window_frame.grid(row = 0,column = 0, columnspan = 3, sticky = "NSW")
    
    #Lijevo gore
    left_button_up = tk.Button(left_window_frame, text = "/\\", height = 1, pady = 0, command = lambda: button_press(l_roleta_stats,"gore"))
    left_button_up.grid(row = 0, column = 0, padx = (0,15) ,pady = 2)
    #Lijevo dolje
    left_button_down = tk.Button(left_window_frame, text = "\/", height = 1, pady = 0, command = lambda: button_press(l_roleta_stats,"dolje"))
    left_button_down.grid(row = 1, column = 0, padx = (0,15) ,pady = 2)
    #Lijevo stop
    left_button_stop = tk.Button(left_window_frame, text = " STOP ", height = 2, pady = 0, command = lambda: full_stop("lijeva"))
    left_button_stop.grid(row = 0, column = 1,rowspan = 2, padx = (0,15) ,pady = 2)
    #Lijevo auto
    left_button_auto = tk.Button(left_window_frame, text = " AUTO ", height = 2, pady = 0, command = lambda: full_stop())
    left_button_auto.grid(row = 0, column = 2,rowspan = 2, padx = (0,15) ,pady = 2)
    
    
    
    
    right_window_frame = tk.Frame(root, width = 300, height = 100, background = "Blue", padx = 30, pady = 20)
    right_window_frame.grid(row = 0,column = 1, columnspan = 3, sticky = "NSE")
    
    #Desno gore
    right_button_up = tk.Button(right_window_frame, text = "/\\", height = 1, pady = 0, command = lambda: button_press(r_roleta_stats,"gore"))
    right_button_up.grid(row = 0, column = 0, padx = (0,15) ,pady = 2)
    #Desno dolje
    right_button_down = tk.Button(right_window_frame, text = "\/", height = 1, pady = 0, command = lambda: button_press(r_roleta_stats,"dolje"))
    right_button_down.grid(row = 1, column = 0, padx = (0,15) ,pady = 2)
    #Desno stop
    right_button_stop = tk.Button(right_window_frame, text = " STOP ", height = 2, pady = 0, command = lambda: full_stop("desna"))
    right_button_stop.grid(row = 0, column = 1,rowspan = 2, padx = (0,15) ,pady = 2)
    #Lijevo auto
    right_button_auto = tk.Button(right_window_frame, text = " AUTO ", height = 2, pady = 0, command = lambda: full_stop())
    right_button_auto.grid(row = 0, column = 2,rowspan = 2, padx = (0,15) ,pady = 2)


    #dio za elemente GUI-a




    #glavna petlja
    root.mainloop()




def main():
    global selected
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


t1 = threading.Thread(target = main, group = None).start()
t2 = threading.Thread(target = main_gui, group = None).start()


