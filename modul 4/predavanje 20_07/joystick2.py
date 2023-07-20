from sense_emu import SenseHat
from time import sleep
sense = SenseHat()


sense.clear()
x,y = 4,3
sense.set_pixel(x,y,(255,255,255))
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                y = (y-1)%8
                
            elif event.direction == "down":
                y = (y+1)%8
                
            elif event.direction == "left":
                x = (x-1)%8
                
            elif event.direction == "right":
                x = (x+1)%8
                
            elif event.direction == "middle":
               pass
        sense.clear()
        sense.set_pixel(x,y,(255,255,255))