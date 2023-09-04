from sense_emu import SenseHat #type: ignore
from time import sleep
import random

#OPCIJA 2: Memory s kockicama 2x2 (ukupno 16 polja, 8 boja za pamćenje)


def assign_colors():
    global iskoristene_boje
    for square in grid.values():
        while True:        
            boja = random.choice(boje_kljucevi)
            if iskoristene_boje.count(boja) == 2:        
                boja = random.choice(boje_kljucevi)
            else:
                iskoristene_boje.append(boja)
                break
                
        square["color"] = boja
    
def make_pairs():
    global pairs
    for color, pair in pairs.items():
        for name,square in grid.items():
            if square["color"] == color:
                pair.append(name)
    for pair in pairs.values():
        pair.sort()
        
def draw():
    for square in grid.values():
        for pixel in square["pixels"]:
            sense.set_pixel(pixel[0],pixel[1],boje[square["color"]])

def draw_pointer(coord,number):
    global pointer, old_color
    old_coord = pointer.copy()
    sense.set_pixel(old_coord[0],old_coord[1],old_color)
    pointer[coord] = (pointer[coord]+number)%8
    old_color = sense.get_pixel(pointer[0],pointer[1]).copy()
    sense.set_pixel(pointer[0],pointer[1],(255,255,255))
def select():
    global counter, selected_squares, matched_colors
    
    for name,square in grid.items():
        if pointer in square["pixels"]:
            selected_squares.append(name)
            
            draw_square(name)
            
            
    
    counter += 1
    if counter == 2:
        selected_squares.sort()
        for name,pair in pairs.items():
            pair.sort()
            if selected_squares == pair and name not in matched_colors:
                matched_colors.append(name)
                break
            
        counter = 0
        selected_squares.clear()
        sleep(0.5)
        sense.clear((100,100,100))
        draw_pointer(0,0)
    print(matched_colors)
    
def draw_square(name):
    for pixel in grid[name]["pixels"]:
        sense.set_pixel(pixel[0],pixel[1],boje[grid[name]["color"]])
        

#INIT VALUES
sense = SenseHat()
grid = {
    "row1L" : {"pixels":([0,0],[0,1],[1,0],[1,1]), "color":None},
    "row1ML" : {"pixels":([2,0],[2,1],[3,0],[3,1]),"color":None},
    "row1MR" : {"pixels":([4,0],[4,1],[5,0],[5,1]),"color":None},
    "row1R" : {"pixels":([6,0],[6,1],[7,0],[7,1]),"color":None},
    
    "row2L" : {"pixels":([0,2],[0,3],[1,2],[1,3]),"color":None},
    "row2ML" : {"pixels":([2,2],[2,3],[3,2],[3,3]),"color":None},
    "row2MR" : {"pixels":([4,2],[4,3],[5,2],[5,3]),"color":None},
    "row2R" : {"pixels":([6,2],[6,3],[7,2],[7,3]),"color":None},
    
    "row3L" : {"pixels":([0,4],[0,5],[1,4],[1,5]),"color":None},
    "row3ML" : {"pixels":([2,4],[2,5],[3,4],[3,5]),"color":None},
    "row3MR" : {"pixels":([4,4],[4,5],[5,4],[5,5]),"color":None},
    "row3R" : {"pixels":([6,4],[6,5],[7,4],[7,5]),"color":None},
    
    "row4L" : {"pixels":([0,6],[0,7],[1,6],[1,7]),"color":None},
    "row4ML" : {"pixels":([2,6],[2,7],[3,6],[3,7]),"color":None},
    "row4MR" : {"pixels":([4,6],[4,7],[5,6],[5,7]),"color":None},
    "row4R" : {"pixels":([6,6],[6,7],[7,6],[7,7]),"color":None},
    }

boje = {
    "red" : (255,0,0),
    "green" : (0,255,0),
    "blue" : (0,0,255),
    "zuta" : (255,255,0),
    "cyan" : (0,255,255),
    "magenta" : (255,0,255),
    "orange" : (255,122,56),
    "tan" : (255,255,134)
    }
white = (255,255,255)
boje_kljucevi = ["red","green","blue","zuta","cyan","magenta"
                 ,"orange","tan"]
iskoristene_boje = []

pairs = {
    "red" : [],
    "green" : [],
    "blue" : [],
    "zuta" : [],
    "cyan" : [],
    "magenta" : [],
    "orange" : [],
    "tan" : []
    }
pointer = [0,0]
old_color = (100,100,100)
counter = 0
selected_squares = []
matched_colors = []
#MAIN    
def main():
    global old_color
    assign_colors()    
    make_pairs()
    sense.clear((100,100,100))
    #draw()
    old_color = sense.get_pixel(0,0)
    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":         
                if event.direction == "up":
                    draw_pointer(1,-1)
                    
                elif event.direction == "down":
                    draw_pointer(1,1)
                    
                elif event.direction == "left":                
                    draw_pointer(0,-1)
                    
                elif event.direction == "right":
                    draw_pointer(0,1)
                    
                elif event.direction == "middle":
                   
                    select()
        if matched_colors != []:
            for color in matched_colors:
                for square in pairs[color]:
                    draw_square(square)
                    draw_pointer(0,0)
        if len(matched_colors) == 8:
            print("Victory")
            break
        
main()
    

                    
