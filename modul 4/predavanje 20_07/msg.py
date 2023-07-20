from sense_emu import SenseHat
import time
sense = SenseHat()

#sense.show_message("Pozdrav svima!")

plava = (0,0,255)
crvena = (255,0,0)
zuta = (255,255,0)
cyan = (0,255,255)
magenta = (255,0,255)
orange = (255,122,56)

#sense.show_message("I'm blue, didada, didada", text_colour=magenta, back_colour = zuta,
#                   scroll_speed = 0.03)


sense.show_letter("P", text_colour=plava, back_colour = zuta)
time.sleep(1)

sense.clear()
sense.set_pixel(0,0,cyan)
time.sleep(1)

sense.clear(zuta)
sense.set_pixel(7,7,plava)
time.sleep(1)

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
W = (255,255,255)
K = (0,0,0)

slika = [
    G,G,G,G,R,R,R,R,
    B,B,B,B,W,W,W,W,
    G,G,G,G,R,R,R,R,
    B,B,B,B,W,W,W,W,
    G,G,G,G,R,R,R,R,
    B,B,B,B,W,W,W,W,
    G,G,G,G,R,R,R,R,
    B,B,B,B,W,W,W,W,
    
    ]

sense.set_pixels(slika)
time.sleep(1)

sense.set_rotation(90)

kutevi = [0,90,180,270,0,90,180,270]
for kut in kutevi:
    sense.set_rotation(kut)
    time.sleep(1)



