import random, time
from sense_emu import SenseHat
sense = SenseHat()

print(random.randint(0,10))

def rand_boja():
    prva = random.randint(0,255)
    druga = random.randint(0,255)
    treca = random.randint(0,255)
    boja = (prva,druga,treca)
    return boja

for i in range(10):
    print(rand_boja())

def pomak(pos:list):
    direction = ("U","D","L","R")
    smjer = random.choice(direction)
    #smjer = input("Enter movement direction for the snake (U,D,L,R)").upper()
    if smjer == "R" and pos[0] != 7:
        new_pos = list(pos)
        new_pos[0] +=  1
        color = rand_boja()
        return (new_pos[0],new_pos[1],color)
    elif smjer == "L" and pos[0] != 0:
        new_pos = list(pos)
        new_pos[0] -=  1
        color = rand_boja()
        return (new_pos[0],new_pos[1],color)
    elif smjer == "D" and pos[1] != 7:
        new_pos = list(pos)
        new_pos[1] +=  1
        color = rand_boja()
        return (new_pos[0],new_pos[1],color)
    elif smjer == "U" and pos[1] != 0:
        new_pos = list(pos)
        new_pos[1] -=  1
        color = rand_boja()
        return (new_pos[0],new_pos[1],color)
    else:
        new_pos = list(pos)
        new_pos[0] =  new_pos[0]%8        
        new_pos[1] =  new_pos[1]%8
        color = rand_boja()
        return (new_pos[0],new_pos[1],color)
            

sense.clear()
current_pos = (4,4)
sense.set_pixel(4,4,(255,255,255))
counter = 0
pixel_list = [(4,4,(255,255,255))]
while counter < 300:
    
    current_pos = pomak(pixel_list[-1])
    pixel_list.append(current_pos)
    sense.clear()
    for pixel in pixel_list:
       sense.set_pixel(pixel[0],pixel[1],pixel[2])
    
    counter += 1
    
