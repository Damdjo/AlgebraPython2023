from sense_emu import SenseHat
from time import sleep
sense = SenseHat()

"""
while True:
    events = sense.stick.get_events()
    print( events)
    time.sleep(1)

"""

"""
while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
"""

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                sense.show_letter("U")
                
            elif event.direction == "down":
                sense.show_letter("D")
                
            elif event.direction == "left":
                sense.show_letter("L")
                
            elif event.direction == "right":
                sense.show_letter("R")
                
            elif event.direction == "middle":
                sense.show_letter("M")
        elif event.action == "released":
            sense.clear()






