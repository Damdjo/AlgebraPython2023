from sense_emu import SenseHat
#from time import sleep

sense = SenseHat()

boje_kljucevi = ["red","green","blue","white"]
boje = {
    "red" : (255,0,0),
    "green" : (0,255,0),
    "blue" : (0,0,255),
    "white" : (255,255,255)
    }

def draw_pointer(x,y):
    sense.set_pixel(x,y,boje["white"])
def draw_pattern(pattern_list:list):
    for pixel in pattern_list:
        sense.set_pixel(pixel[0],pixel[1],boje[boje_kljucevi[pixel[2]]])

def check():
    if pattern == p_lock:
        msg = f"Welcome"
        sense.set_pixels(unlock)
        return 0
    else:
        return 1

pos_x = 0
pos_y = 0

#smajlic pattern
# = [[2, 2, 1], [2, 4, 1], [3, 5, 1], [4, 5, 1], [5, 2, 1], [5, 4, 1]]

#lokot pattern
#lock = [[0, 4, 1], [0, 5, 1], [0, 6, 1], [0, 7, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1], [2, 1, 1], [2, 4, 1], [2, 5, 1], [2, 6, 1], [2, 7, 1], [3, 1, 1], [3, 4, 1], [3, 5, 1], [3, 6, 1], [3, 7, 1], [4, 1, 1], [4, 4, 1], [4, 5, 1], [4, 6, 1], [4, 7, 1], [5, 1, 1], [5, 4, 1], [5, 5, 1], [5, 6, 1], [5, 7, 1], [6, 2, 1], [6, 3, 1], [6, 4, 1], [6, 5, 1], [6, 6, 1], [6, 7, 1], [7, 4, 1], [7, 5, 1], [7, 6, 1], [7, 7, 1]]

p_lock = [[2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [3, 0, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [4, 0, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0], [5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 0]]
K = (0,0,0)
G = (0,255,0)


unlock =[K, K, G, G, G, G, K, K, 
    K, K, G, K, K, G, K, K,
    K, K, G, K, K, K, K, K,
    K, K, G, G, G, G, K, K,
    K, K, G, G, G, G, K, K,
    K, K, G, G, G, G, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    ]

pattern = []
sense.clear()
#sense.set_pixels(lock)
status = 1
while status != 0:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            
            #gornji gumb (pomak gore)
            if event.direction == "up":
                if pos_y != 0:
                    pos_y -= 1
                else:
                    pos_y = 7
                
            #donji gumb (pomak dolje)
            elif event.direction == "down":
                if pos_y != 7:
                    pos_y += 1
                else:
                    pos_y = 0
            
            #lijevi gumb (pomak ulijevo)
            elif event.direction == "left":
                if pos_x != 0:
                    pos_x -= 1
                else:
                    pos_x = 7
                    
            #desni gumb (pomak udesno)
            elif event.direction == "right":
                if pos_x != 7:
                    pos_x += 1
                else:
                    pos_x = 0
                    
            #srednji gumb (mijenjanje boja)
            elif event.direction == "middle":
                selected_pixel = [pos_x,pos_y,0]
                if selected_pixel not in pattern:
                    pattern.append(selected_pixel)
                else:
                    pattern.remove(selected_pixel)
                pattern.sort()
                print(pattern)
                
            sense.clear()
            draw_pattern(pattern)
            draw_pointer(pos_x,pos_y)
            status = check()
            