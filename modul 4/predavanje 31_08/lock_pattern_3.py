from sense_emu import SenseHat
from time import sleep

#POCETNE VRIJEDNOSTI
sense = SenseHat()

boje_kljucevi = ["red","green","blue","white"]
boje = {
    "red" : (255,0,0),
    "green" : (0,255,0),
    "blue" : (0,0,255),
    "white" : (255,255,255)
    }

users = {
    "admin" : [[2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [3, 0, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [4, 0, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0], [5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 0]] ,
    "smajlic" : [[2, 2, 0], [2, 4, 0], [3, 5, 0], [4, 5, 0], [5, 2, 0], [5, 4, 0]],
    }
users_counter = 1
save_pattern = [[0, 0, 0], [0, 7, 0], [7, 0, 0], [7, 7, 0]]
pos_x = 0
pos_y = 0
add_user = False
last_two = [1]



K = (0,0,0)
G = (0,255,0)

add = [K, K, K, G, G, K, K, K, 
    K, K, K, G, G, K, K, K,
    K, K, K, G, G, K, K, K,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    K, K, K, G, G, K, K, K,
    K, K, K, G, G, K, K, K,
    K, K, K, G, G, K, K, K,
    ]

pattern = []

def draw_pointer(x,y):
    sense.set_pixel(x,y,boje["white"])
def draw_pattern(pattern_list:list):
    for pixel in pattern_list:
        sense.set_pixel(pixel[0],pixel[1],boje[boje_kljucevi[pixel[2]]])

def check():
    global add_user
    if pattern == save_pattern and add_user == False:
        pattern.clear()
        return 2
    
    for user, usr_pattern in users.items():
        print(user,end="\n")
        if pattern == usr_pattern:
            msg = f"Welcome {user}"
            sense.show_message(msg)
            return 0
        else:
            continue
    if add_user == True:
        return 2
    return 1

#FUNKCIJE
def save_last_two(last_two_list:list,last_pixel:list):
    global pattern, users_counter, status, add_user
    if add_user == True:
        if last_two_list == [1]:
            last_two_list.clear()
        if len(last_two_list)<2:
            last_two_list.append(last_pixel)
        elif len(last_two_list)==2:
            if last_pixel == last_two_list[0] and last_pixel == last_two_list[1]:
                add_new_user_pattern(pattern,users_counter)
                status = 1
                add_user = False
                pattern = []
            else:
                last_two_list.pop(0)
                last_two_list.append(last_pixel)

def add_new_user_pattern(pattern_to_add:list, user_counter:list):
    global save_pattern
    if add_user == True:
        if pattern_to_add != save_pattern and pattern_to_add not in users.values():
            users[f"user_{user_counter}"] = pattern_to_add
            user_counter += 1
        else:
            print("Invalid pattern")
        


sense.clear()
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
                    save_last_two(last_two,selected_pixel)
                else:
                    pattern.remove(selected_pixel)
                pattern.sort()
                print(pattern)
                print(last_two)
            
            print(status, " test1 ",add_user)
            status = check()
            
            #print(status, " 2 ",add_user)
            
            if status == 1 and add_user == False:                
                sense.clear()
                draw_pattern(pattern)
                draw_pointer(pos_x,pos_y)
            elif status == 2 and add_user == False:
                add_user = True
                sense.set_pixels(add)
                sleep(0.5)
                sense.clear()
                pos_x = 0
                pos_y = 0
                draw_pointer(pos_x,pos_y)
            elif status == 2 and add_user == True:
                #sense.show_message("2 and true")
                sense.clear()
                draw_pattern(pattern)
                draw_pointer(pos_x,pos_y)
            
                
            
            

