from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

boje_kljucevi = ["red","green","blue"]
boje = {
    "red" : (255,0,0),
    "green" : (0,255,0),
    "blue" : (0,0,255)
    }
delay = 0.5


column_1 = [0,7,0]
column_2 = [2,7,1]
column_3 = [4,7,2]

column_lists = [column_1,column_2,column_3]
selected_col_index = 0

def draw_col(column:list):
    for broj_temp in range (7,int(column[1])-1,-1):
        sense.set_pixel(column[0],broj_temp,boje[boje_kljucevi[column[2]]])

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            
            #gornji gumb (pomak gore)
            if event.direction == "up":
                if column_lists[selected_col_index][1] != 0:
                    column_lists[selected_col_index][1] -= 1

            
            #donji gumb (pomak dolje)
            elif event.direction == "down":
                if column_lists[selected_col_index][1] != 7:
                    column_lists[selected_col_index][1] += 1
            
            #lijevi gumb (pomak ulijevo)
            elif event.direction == "left":
                if selected_col_index != 0:
                    selected_col_index -=1
                else:
                    selected_col_index =2
            #desni gumb (pomak udesno)
            elif event.direction == "right":
                if selected_col_index != 2:
                    selected_col_index +=1
                else:
                    selected_col_index =0
            #srednji gumb (mijenjanje boja)
            elif event.direction == "middle":
                if column_lists[selected_col_index][2] != 2:
                   column_lists[selected_col_index][2] += 1
                else:                    
                   column_lists[selected_col_index][2]=0
    
    sense.clear()
    draw_col(column_1)    
    draw_col(column_2)    
    draw_col(column_3)        
    
    sleep(delay)