from sense_emu import SenseHat
import time

sense = SenseHat()

while True:
    events = sense.stick.get_events()
    print( events)
    time.sleep(1)