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
    for user, usr_pattern in users.items():
        print(user,end="\n")
        if pattern == usr_pattern:
            msg = f"Welcome {user}"
            sense.show_message(msg)
            return 0
        else:
            pass

users = {
    "admin" : [[2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [3, 0, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [4, 0, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0], [5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 0]] ,
    "smajlic" : [[2, 2, 0], [2, 4, 0], [3, 5, 0], [4, 5, 0], [5, 2, 0], [5, 4, 0]],
    }

pos_x = 0
pos_y = 0



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
            
