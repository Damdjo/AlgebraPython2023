from sense_emu import SenseHat
from time import sleep
sense = SenseHat()


roll,pitch,yaw = sense.get_orientation().values()

roll = round(roll,2)
pitch = round(pitch,2)
yaw = round(yaw,2)

print(roll,pitch,yaw)

mjerenje = f"Roll: {roll}; Pitch: {pitch}; Yaw: {yaw}"
#sense.show_message(mjerenje)
sense.show_letter("P")
accel = sense.get_accelerometer_raw().values()
print(accel)
x,y,z = sense.get_accelerometer_raw().values()

x = round(x,0)
y = round(y,0)
z = round(z,0)

while True:
    x,y,z = sense.get_accelerometer_raw().values()

    x = round(x,0)
    y = round(y,0)
    z = round(z,0)
    print(x,y)
    if x == -1:
        sense.set_rotation(180)
    elif y == 1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)


